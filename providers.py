# providers.py
import os
from typing import Optional

SYSTEM_INSTRUCTIONS = (
    "You are a professional website translator. Translate ONLY human-visible text into the target language. "
    "STRICTLY preserve Markdown/HTML, inline code, code fences, LaTeX math, link URLs, image paths, Hugo shortcodes, and front matter syntax. "
    "Do not add or remove lines. Keep headings and list structure identical. "
    "If a line is only markup, return it unchanged."
)

class ProviderError(RuntimeError):
    pass

def get_translator(name: str, model: str = "", src_lang: str = "en"):
    name = name.lower()
    if name == "openai":
        return OpenAITranslator(model=model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini"), src_lang=src_lang)
    if name == "google":
        return GoogleTranslator(src_lang=src_lang)
    if name == "deepl":
        return DeepLTranslator(src_lang=src_lang)
    if name == "hf":
        return HFTranslator(model=model or "facebook/nllb-200-distilled-600M", src_lang=src_lang)
    raise ProviderError(f"Unknown provider: {name}")

class BaseTranslator:
    def __init__(self, src_lang: str = "en"):
        self.src_lang = src_lang

    def translate(self, text: str, target_lang: str, preserve_format: bool = True) -> str:
        raise NotImplementedError

# -------- OpenAI --------
class OpenAITranslator(BaseTranslator):
    def __init__(self, model: str, src_lang: str = "en"):
        super().__init__(src_lang)
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("OPENAI_BASE_URL")  # optional for compatible endpoints
        if not self.api_key:
            raise ProviderError("OPENAI_API_KEY is not set")

        try:
            # new-style client (2024+)
            from openai import OpenAI  # type: ignore
            self.client = OpenAI(api_key=self.api_key, base_url=self.base_url) if self.base_url else OpenAI(api_key=self.api_key)
            self._mode = "responses"
        except Exception:
            # legacy fallback
            import openai  # type: ignore
            openai.api_key = self.api_key
            if self.base_url:
                openai.base_url = self.base_url
            self.client = openai
            self._mode = "chat"

    def translate(self, text: str, target_lang: str, preserve_format: bool = True) -> str:
        prompt = f"Translate from {self.src_lang} to {target_lang}. Return only the translated text.\n\n" + text
        try:
            if self._mode == "responses":
                out = self.client.responses.create(
                    model=self.model,
                    input=[
                        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0,
                )
                return out.output_text
            else:  # legacy chat.completions
                out = self.client.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0,
                )
                return out["choices"][0]["message"]["content"]
        except Exception as e:
            raise ProviderError(f"OpenAI translation failed: {e}")

# -------- Google Cloud Translate --------
class GoogleTranslator(BaseTranslator):
    def __init__(self, src_lang: str = "en"):
        super().__init__(src_lang)
        # Requires GOOGLE_APPLICATION_CREDENTIALS to be set
        try:
            from google.cloud import translate_v2 as translate  # v2 simpler for quick use
        except Exception as e:
            raise ProviderError("Install google-cloud-translate: pip install google-cloud-translate==2.*") from e
        self.client = translate.Client()

    def translate(self, text: str, target_lang: str, preserve_format: bool = True) -> str:
        # Note: v2 treats markdown as plain text. We rely on our block splitter to preserve fences/markup.
        try:
            resp = self.client.translate(text, target_language=target_lang, source_language=self.src_lang, format_="text")
            return resp["translatedText"]
        except Exception as e:
            raise ProviderError(f"Google Translate failed: {e}")

# -------- DeepL --------
class DeepLTranslator(BaseTranslator):
    def __init__(self, src_lang: str = "en"):
        super().__init__(src_lang)
        try:
            import deepl  # type: ignore
        except Exception as e:
            raise ProviderError("Install deepl: pip install deepl") from e
        auth = os.getenv("DEEPL_AUTH_KEY")
        if not auth:
            raise ProviderError("DEEPL_AUTH_KEY is not set")
        self.client = deepl.Translator(auth)

    def translate(self, text: str, target_lang: str, preserve_format: bool = True) -> str:
        # DeepL target codes like JA, HI
        try:
            out = self.client.translate_text(text, source_lang=self.src_lang.upper(), target_lang=target_lang.upper(), preserve_formatting=True)
            return out.text
        except Exception as e:
            raise ProviderError(f"DeepL translation failed: {e}")

# -------- HuggingFace Transformers (local or cached) --------
class HFTranslator(BaseTranslator):
    def __init__(self, model: str, src_lang: str = "en"):
        super().__init__(src_lang)
        try:
            from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline  # type: ignore
        except Exception as e:
            raise ProviderError("Install transformers: pip install transformers sentencepiece") from e
        self.model_name = model
        self.pipe = pipeline("translation", model=model)

        # crude map to NLLB lang codes if needed
        self._map = {
            "en": "eng_Latn", "ja": "jpn_Jpan", "hi": "hin_Deva", "ko": "kor_Hang",
            "zh": "zho_Hans", "fr": "fra_Latn", "es": "spa_Latn", "de": "deu_Latn"
        }

    def translate(self, text: str, target_lang: str, preserve_format: bool = True) -> str:
        src = self._map.get(self.src_lang, self.src_lang)
        tgt = self._map.get(target_lang, target_lang)
        try:
            out = self.pipe(text, src_lang=src, tgt_lang=tgt, max_length=4096, truncation=True)
            return out[0]["translation_text"]
        except Exception as e:
            raise ProviderError(f"HF translation failed: {e}")
