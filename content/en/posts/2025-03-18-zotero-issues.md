---
title: "Issues with Zotero and working them out!"
date: 2025-03-18T15:05:28+11:00
draft: false
tags:
   - zotero
   - debugging
---

A log of Zotero issues, I have encountered.

---

The the Zotero chrome connector doesn't always work. This issue arises sporadically every now and then. A workaround I devised for this is to use the webpage version of the zotero library via login to the website. The library is available at: [https://www.zotero.org/suyoggarg/mylibrary/](https://www.zotero.org/suyoggarg/collections/U8AAVCPJ/items/R6EYB749/item-list)

Then any new item can be manually added using the identifier, for example the DOI or the URL of the page. However, BibTex export via Better-BibTex will still require the software download and full library sync. These issues may also be arising due to improper device resources allocation, for instance, when the CPU is busy with some other tasks.

Also see: [https://forums.zotero.org/discussion/72396/zotero-stuck-loading-items-or-just-stops-working](https://forums.zotero.org/discussion/72396/zotero-stuck-loading-items-or-just-stops-working)

--

## 2026/11/13: Setting up BibTex custom postscript commands in Zotero

Two utilities have been added to BibTex exporter in Zotero via BetterBibTex postscript commands as follows:

```bash
// Truncate long author lists and prefer Collaboration for BibTeX/REVTeX
if (Translator.BetterBibTeX) {
  const LIMIT = 10; // change to taste

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


// Make all Arxiv papers export in Article class on BibTex with custom journal name
if (Translator.BetterBibTeX) {
  // Detect arXiv items via Zotero's preprint item type, arXiv field, or archivePrefix
  const isArxiv = (zotero.itemType === 'preprint' || item.arXiv || (tex.has.archiveprefix && tex.has.archiveprefix.value.toLowerCase() === 'arxiv'));

  if (isArxiv) {
    // Export as @article instead of @misc
    tex.entrytype = 'article';
    
    // Set the journal name (overwrites if empty, or sets it cleanly)
    tex.add({ name: 'journal', value: 'arXiv e-prints' });
  }
}

```

_However, on second thoughts, it is better to have these arxiv papers as normal text, as usual bold title for journal articles to indicate peer-reviewed papers. For papers accepted after a peer-review, but yet to be fully published and available online, it would be okay to manually put the title in bold in the bibliography_

> Have also removed the following fields from been exported in the BibTex entry: abstract, file, keywords

--

## Date: 2025/11/27

when using zotore connector, if the full-author list is not loaded, e.g. on IOP page, 
then the connector only catches the short authors listed on the page.

---

## Date: 2025/03/18
- Issue: Zotero freezes, items don't load and the application doesn't respond.
- Reason: Possibly due to adding too many feeds and the syncing issue.

---

## Date: 2025/03/18
- Issue: Zootmoov didn't sync recent files.
- Solution: Select affected files, `right click`$ \rightarrow$ `Move them to directory with Zootmoov`

---
