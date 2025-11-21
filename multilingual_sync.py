#!/usr/bin/env python3
"""
Hugo Multilingual Sync — translate EN content to other languages without touching Hugo’s build.

Usage (examples):
  python ml_sync.py --langs ja,hi --provider openai
  python ml_sync.py --langs ja --provider openai --output-style folders
  python ml_sync.py --langs ja,hi --provider hf --model facebook/nllb-200-distilled-600M
  python ml_sync.py --langs ja --provider openai --translate-frontmatter title,description,summary

Environment:
  OPENAI_API_KEY         (for provider=openai; optional OPENAI_BASE_URL, OPENAI_MODEL)
  GOOGLE_APPLICATION_CREDENTIALS (for provider=google)
  DEEPL_AUTH_KEY         (for provider=deepl)
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Optional deps are lazy-loaded only if needed.
# Local files
from providers import get_translator, ProviderError

# ---------- Defaults ----------
TEXT_EXTS = {".md", ".markdown", ".html", ".htm"}
BINARY_COPY_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".pdf", ".mp4", ".mp3"}
DEFAULT_SRC_LANG = "en"
DEFAULT_OUTPUT_STYLE = "folders"  # 'folders' => content/<lang>/..., or 'suffix' => foo.ja.md
CACHE_DIR = Path(".mlsync")
CACHE_FILE = CACHE_DIR / "translation_cache.json"
TRANSLATABLE_FM_KEYS_DEFAULT = ["title", "description", "summary"]

# Regex for front matter fences (YAML '---', TOML '+++', JSON '{')
FM_FENCE = re.compile(r"^([\-\+]{3}|\{)\s*$")
CODE_FENCE = re.compile(r"^```")          # fenced code blocks (keep as is)
MATH_BLOCK = re.compile(r"^\$\$")         # LaTeX math blocks (keep as is)
SHORTCODE = re.compile(r"^\{\{<.*?>\}\}$") # Hugo shortcodes line (keep as is)

def read_site_languages(config_dir: Path) -> Tuple[str, List[str]]:
    """
    Try to infer default language and enabled languages from config.(toml|yaml|yml|json).
    Returns (default_lang, languages_list). If not found, falls back to (en, []).
    """
    # Very light parser: read file text and look for languages keys.
    import io, contextlib
    default_lang = DEFAULT_SRC_LANG
    langs = []

    for name in ["config.toml", "hugo.toml", "config.yaml", "config.yml", "config.json"]:
        p = config_dir / name
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        # defaultContentLanguage
        m = re.search(r"defaultContentLanguage\s*=\s*['\"]([a-zA-Z\-]+)['\"]", text)
        if m:
            default_lang = m.group(1).lower()

        # [languages] tables (TOML) or languages: (YAML/JSON) — gather keys like [languages.ja]
        langs_toml = re.findall(r"\[languages\.([a-zA-Z\-]+)\]", text)
        if langs_toml:
            langs = sorted(set([l.lower() for l in langs_toml if l.lower() != default_lang]))

        # YAML-ish:
        if not langs and re.search(r"(?m)^\s*languages\s*:\s*", text):
            # crude parse of top-level language keys
            for k in re.findall(r"(?m)^\s*([a-zA-Z\-]{2,})\s*:\s*\n", text):
                if k.lower() != default_lang:
                    langs.append(k.lower())

        # JSON-ish:
        if not langs and '"languages"' in text:
            for k in re.findall(r'"([a-zA-Z\-]{2,})"\s*:\s*\{', text):
                if k.lower() != default_lang:
                    langs.append(k.lower())
        break
    return default_lang, sorted(set(langs))

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def load_cache() -> Dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def save_cache(cache: Dict):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

def split_front_matter(raw: str) -> Tuple[str, str, str]:
    """
    Returns (fm_type, fm_text, body). fm_type is 'yaml'|'toml'|'json'|''.
    """
    lines = raw.splitlines()
    if not lines:
        return "", "", raw
    if lines[0].strip() == "---":
        # YAML until next ---
        try:
            end = lines[1:].index("---") + 1
        except ValueError:
            end = -1
        if end > 0:
            fm = "\n".join(lines[:end+1])
            body = "\n".join(lines[end+1:])
            return "yaml", fm, body
    if lines[0].strip() == "+++":
        try:
            end = lines[1:].index("+++") + 1
        except ValueError:
            end = -1
        if end > 0:
            fm = "\n".join(lines[:end+1])
            body = "\n".join(lines[end+1:])
            return "toml", fm, body
    if lines[0].strip().startswith("{"):
        # naive JSON front matter until the matching '}' on its own line
        # fallback: find the first line that is just "}"
        for i, L in enumerate(lines):
            if L.strip() == "}":
                fm = "\n".join(lines[:i+1])
                body = "\n".join(lines[i+1:])
                return "json", fm, body
    return "", "", raw

def parse_front_matter(fm_type: str, fm_text: str) -> Dict:
    if not fm_type:
        return {}
    try:
        if fm_type == "yaml":
            import yaml
            return yaml.safe_load("\n".join(fm_text.splitlines()[1:-1])) or {}
        if fm_type == "toml":
            try:
                import tomllib as tomli  # py>=3.11
            except Exception:
                import tomli
            inner = "\n".join(fm_text.splitlines()[1:-1])
            return tomli.loads(inner) if inner.strip() else {}
        if fm_type == "json":
            return json.loads(fm_text) or {}
    except Exception:
        return {}
    return {}

def dump_front_matter(fm_type: str, data: Dict) -> str:
    if not fm_type or not data:
        return ""
    if fm_type == "yaml":
        import yaml
        return "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n"
    if fm_type == "toml":
        import tomlkit
        # tomlkit preserves ordering nicely
        doc = tomlkit.document()
        for k, v in data.items():
            doc.add(k, v)
        return "+++\n" + tomlkit.dumps(doc) + "+++\n"
    if fm_type == "json":
        return json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    return ""

def should_copy_binary(ext: str) -> bool:
    return ext.lower() in BINARY_COPY_EXTS

def is_text(ext: str) -> bool:
    return ext.lower() in TEXT_EXTS

def chunk_markdown_for_llm(body: str) -> List[Tuple[str, bool]]:
    """
    Split Markdown/HTML into blocks. Returns list of (block_text, translatable_flag).
    We keep code fences, math blocks, and Hugo shortcodes untouched.
    """
    out = []
    buf = []
    protected = False
    for line in body.splitlines():
        if CODE_FENCE.match(line) or MATH_BLOCK.match(line) or SHORTCODE.match(line):
            # flush previous
            if buf:
                out.append(("\n".join(buf).rstrip("\n"), True))
                buf = []
            out.append((line, False))
            protected = not protected if CODE_FENCE.match(line) or MATH_BLOCK.match(line) else False
            continue
        if protected:
            out.append((line, False))
            continue
        buf.append(line)
    if buf:
        out.append(("\n".join(buf).rstrip("\n"), True))
    return out

def ensure_translation_key(meta: Dict, rel_key: str) -> Dict:
    # Use existing translationKey if present; else set from rel_key (stable across langs).
    if "translationKey" not in meta and rel_key:
        meta["translationKey"] = rel_key.replace("\\", "/")
    return meta

def out_path_for(file: Path, content_root: Path, lang: str, output_style: str) -> Path:
    rel = file.relative_to(content_root)
    if output_style == "folders":
        return content_root / lang / rel
    # suffix style: foo.md -> foo.ja.md (or keep _index.md unchanged name with suffix)
    stem = rel.stem
    parent = content_root / rel.parent
    # Handle double suffix e.g. foo.en.md
    if stem.endswith(f".{DEFAULT_SRC_LANG}"):
        stem = stem[:-(len(DEFAULT_SRC_LANG)+1)]
    newname = f"{stem}.{lang}{rel.suffix}"
    return parent / newname

def main():
    ap = argparse.ArgumentParser(description="Sync/translate Hugo content into multilingual folders or suffixed files.")
    ap.add_argument("--content-dir", default="content", help="Content root (default: content)")
    ap.add_argument("--src-lang", default=DEFAULT_SRC_LANG, help="Source language code (default: en)")
    ap.add_argument("--langs", default="", help="Comma-separated target language codes (e.g., ja,hi,ko)")
    ap.add_argument("--provider", required=True, choices=["openai", "google", "deepl", "hf"], help="Translation backend")
    ap.add_argument("--model", default="", help="Override model name for provider (optional)")
    ap.add_argument("--output-style", default=DEFAULT_OUTPUT_STYLE, choices=["folders", "suffix"], help="Where to write translations")
    ap.add_argument("--overwrite", action="store_true", help="Regenerate translations even if cache says up-to-date")
    ap.add_argument("--skip-existing", action="store_true", help="Skip if target file already exists (fast)")
    ap.add_argument("--dry-run", action="store_true", help="Do not write files, just show plan")
    ap.add_argument("--translate-frontmatter", default=",".join(TRANSLATABLE_FM_KEYS_DEFAULT),
                    help="Comma-separated FM keys to translate (title,description,summary,...)")
    args = ap.parse_args()

    content_root = Path(args.content_dir).resolve()
    if not content_root.exists():
        print(f"[ERR] content dir not found: {content_root}", file=sys.stderr)
        sys.exit(1)

    default_lang, cfg_langs = read_site_languages(Path(".").resolve())
    src_lang = args.src_lang or default_lang
    # Resolve target languages: CLI > config
    target_langs = [s.strip().lower() for s in args.langs.split(",") if s.strip()] or cfg_langs
    if not target_langs:
        print("[ERR] No target languages specified (use --langs ja,hi) and none found in config.*", file=sys.stderr)
        sys.exit(2)
    if src_lang in target_langs:
        target_langs = [l for l in target_langs if l != src_lang]

    fm_keys = [k.strip() for k in (args.translate_frontmatter or "").split(",") if k.strip()]

    translator = get_translator(args.provider, model=args.model, src_lang=src_lang)

    cache = load_cache()

    # Walk content
    plan: List[Tuple[Path, str, Path]] = []
    for path in content_root.rglob("*"):
        if path.is_dir():
            continue
        ext = path.suffix.lower()

        # Ignore already translated folders if output_style=folders
        if args.output_style == "folders":
            parts = path.relative_to(content_root).parts
            if parts and parts[0] in target_langs:
                continue  # this is already a translated file
            if parts and parts[0] != "" and parts[0] == src_lang:
                # if someone put English under content/en, treat it as source
                pass

        # Only process text or copy binary
        if not (is_text(ext) or should_copy_binary(ext)):
            continue

        for lang in target_langs:
            outp = out_path_for(path, content_root, lang, args.output_style)
            plan.append((path, lang, outp))

    # Execute
    for src_file, lang, outp in plan:
        outp.parent.mkdir(parents=True, exist_ok=True)

        if should_copy_binary(src_file.suffix):
            # mirror assets 1:1
            if args.dry_run:
                print(f"[COPY] {src_file} -> {outp}")
                continue
            if not args.overwrite and outp.exists() and outp.stat().st_mtime >= src_file.stat().st_mtime:
                continue
            shutil.copy2(src_file, outp)
            continue

        # Text file: check cache
        src_hash = sha256_file(src_file)
        cache_key = f"{src_file}|{lang}|{args.provider}|{args.model}|{args.output_style}"
        if (not args.overwrite) and (cache.get(cache_key, "") == src_hash) and (args.skip_existing and outp.exists()):
            # up to date
            continue

        raw = src_file.read_text(encoding="utf-8", errors="ignore")
        fm_type, fm_text, body = split_front_matter(raw)
        meta = parse_front_matter(fm_type, fm_text)

        # Compute a stable translationKey based on path excluding any language prefix in folders mode
        rel_key = str(src_file.relative_to(Path(args.content_dir))).lstrip("/")
        if args.output_style == "folders":
            # when src is under content/en/, strip that prefix for key stability
            rel_parts = src_file.relative_to(Path(args.content_dir)).parts
            if rel_parts and rel_parts[0].lower() in [src_lang]:
                rel_key = "/".join(rel_parts[1:])
        meta = ensure_translation_key(meta, rel_key)

        # Translate selected front matter keys
        for k in fm_keys:
            if k in meta:
                if isinstance(meta[k], str) and meta[k].strip():
                    meta[k] = translator.translate(meta[k], target_lang=lang, preserve_format=True)
                elif isinstance(meta[k], list):
                    meta[k] = [translator.translate(v, target_lang=lang, preserve_format=True) if isinstance(v, str) else v
                               for v in meta[k]]

        # Translate body (block-wise, preserving fences/shortcodes)
        blocks = chunk_markdown_for_llm(body)
        translated_chunks = []
        for txt, translatable in blocks:
            if not translatable or not txt.strip():
                translated_chunks.append(txt)
            else:
                translated = translator.translate(txt, target_lang=lang, preserve_format=True)
                translated_chunks.append(translated)
        new_body = "\n".join(translated_chunks).rstrip() + ("\n" if body.endswith("\n") else "")

        new_fm = dump_front_matter(fm_type, meta)
        output_text = f"{new_fm}{new_body}" if new_fm else new_body

        if args.dry_run:
            print(f"[WRITE] {outp}  ({len(output_text)} chars)")
        else:
            outp.write_text(output_text, encoding="utf-8")
            cache[cache_key] = src_hash

    if not args.dry_run:
        save_cache(cache)
        print("✔ Done. Translated content synced.")

if __name__ == "__main__":
    main()
