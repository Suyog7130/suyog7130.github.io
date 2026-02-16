---
title: "BibTex, Zotero and REVTex"
date: 2025-11-03
tags:
    - zotero
    - bibtex
---

## Killing the `\@lbibitem` Error in REVTeX and Auto‑Truncating Huge Author Lists from Zotero (Better BibTeX)

This note documents the exact fixes I used when REVTeX + APS style blew up on a long collaboration paper (Abbott et al. 2016, LIGO/Virgo), and how I automated Better BibTeX (Zotero) to **truncate 100+ authors** at export and/or **prefer the Collaboration name**.

---

## TL;DR

- If you see `! File ended while scanning use of \@lbibitem.`, your **.bbl is malformed/truncated**. Rebuild cleanly with **BibTeX** (not biber) and fix author-name parsing glitches (multi‑word surnames, corporate authors).
- For REVTeX: use `\documentclass{revtex4-2}` + `\bibliographystyle{apsrev4-2}` and run **BibTeX**.
- In Zotero (Better BibTeX), add a tiny **Postscript** so items with **>100 authors** export as *first 100 + “others”* (= *et al.*), **or** export just the **Collaboration** if present.
- Fix “duplicate destination figure.X” warnings by giving **unique `\label`s**, placed **after** each `\caption`.

---

## 1) Symptom

LaTeX dies in the bibliography:
```
! File ended while scanning use of \@lbibitem.
... {\citenamefont {Abbott}\ \emph {et~al.}(2016)\citenamefont {Abbott}, \ETC.
l.567 \bibliography{mlpaper}
```
You’re on `revtex4-2` + `apsrev4-2`, so macros like `\citenamefont` and `\ETC.` are valid. The failure is usually a **half‑written optional argument** of a `\bibitem` in the **generated .bbl** (i.e. the .bbl is truncated or has unbalanced braces from name parsing).

**Typical root causes** (in my case it was one odd surname):
- Multi‑word surnames unbraced: e.g., `Canton, T. Dal` vs `{{Dal Canton}, T.}`
- Corporate/collaboration author improperly represented.
- A previous partial build picked the wrong tool chain and left a corrupted `.bbl`.

---

## 2) Minimal working REVTeX pipeline (force BibTeX)

Use BibTeX with REVTeX/APS styles; do a clean rebuild:
```bash
latexmk -C
rm -f *.bbl *.blg *.bcf *.run.xml
pdflatex main
bibtex   main     # <- BibTeX, not biber
pdflatex main
pdflatex main
# or: latexmk -pdf -bibtex main.tex
```

If you ever switch to a non‑REVTeX class (e.g. `article`), use `natbib` with `unsrtnat/abbrvnat` instead of `apsrev4-2`:

```latex
\documentclass{article}
\usepackage[numbers,sort&compress]{natbib}
\bibliographystyle{unsrtnat}
```

---

## 3) Fixing tricky names in the `.bib` (Zotero export hygiene)

- **Multi‑word surnames**: brace the full family name
  ```bibtex
  author = {{Dal Canton}, T.},
  author = {{Cerboni Baiardi}, L.},
  ```
- **Particles (van, de, von)**: either keep as “van den Brand, J. F. J.” or brace: `{{van den Brand}, J. F. J.}`
- **Collaboration**: prefer a corporate author
  ```bibtex
  author = {{LIGO Scientific Collaboration and Virgo Collaboration}},
  ```
- Accents are fine as TeX macros: `Maga{\~n}a`, `Zadro{\.z}ny`.

**Debug quickly:**
```bash
grep -iE "error|warn|comma|brace|couldn.?t" main.blg || true
```
If the error disappears when you temporarily shorten the author list to:
```bibtex
author = {Abbott, B. P. and others},
```
then the original list had a parsing glitch—brace the offending names.

---

## 4) Zotero → Better BibTeX: auto‑truncate 100+ authors *or* prefer Collaboration

**Goal**
- If an item has **>100 authors**, export the **first 100** and then **“others”** (a special BibTeX name that renders as *et al.* in most styles including APS).
- If a **Collaboration** appears in the author list, export **just the collaboration** as the (corporate) author.

**Setup (Zotero → Preferences → Better BibTeX → Export → Postscript):**

```js
// Truncate long author lists and prefer Collaboration for BibTeX/REVTeX
if (Translator.BetterBibTeX) {
  const LIMIT = 100; // change to taste

  const creators = (zotero.creators || []).slice();
  const authors = creators.filter(c => c.creatorType === 'author');

  // Detect a corporate/collaboration author
  const collabIndex = authors.findIndex(a => {
    const name = (a.name || a.lastName || '').toLowerCase();
    return /collaboration/.test(name);
  });

  let newAuthors = authors;

  if (collabIndex >= 0) {
    // Prefer the collaboration as the sole author (single-field corporate)
    const collab = authors[collabIndex];
    newAuthors = [collab];
  } else if (authors.length > LIMIT) {
    // Keep first LIMIT, then append 'others' -> renders as "et al."
    newAuthors = authors.slice(0, LIMIT);
    newAuthors.push({ creatorType: 'author', name: 'others' });
  }

  if (newAuthors !== authors) {
    const nonAuthors = creators.filter(c => c.creatorType !== 'author');
    zotero.creators = [...newAuthors, ...nonAuthors];
    // Rebuild author/editor for export
    tex.remove('author');
    tex.remove('editor');
    tex.addCreators();
  }
}
```

**Export tips**
- Use **Better BibTeX** (not Better BibLaTeX) for REVTeX/BibTeX workflows.
- Enable **“Keep updated”** on your `.bib` if you want auto‑refresh.

---

## 5) Duplicate figure destination warning

If you see:
```
pdfTeX warning (ext4): destination with the same identifier (name{figure.10}) ...
```
you have duplicate labels/anchors. Give **unique `\label`s** and place them **after** each `\caption`:

```latex
\begin{figure}
  \includegraphics{...}
  \caption{UQ test}
  \label{fig:uq-test-20251030-1}
\end{figure}
```

---

## 6) Quick checklist

- [ ] Clean rebuild: `latexmk -C && latexmk -pdf -bibtex main.tex`
- [ ] REVTeX + APS style: `revtex4-2` + `apsrev4-2`
- [ ] Brace multi‑word surnames & collaboration as corporate author
- [ ] Add BBT Postscript to truncate 100+ authors (**or** prefer Collaboration)
- [ ] Unique `\label`s (after `\caption`)

---

## 7) Appendix: forcing latexmk to always use BibTeX with REVTeX

Put a `latexmkrc` next to your `main.tex`:

```perl
$bibtex_use = 2;   # force BibTeX
```

This avoids accidental biber runs that can leave a half‑baked `.bbl`.

---

**Done.** Future me: if `\@lbibitem` shows up again, check the `.bbl` first, then the names in the `.bib`, then re‑export from Zotero with the Postscript above. Keep calm and `latexmk` on. 