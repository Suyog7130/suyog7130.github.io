---
title: "Tips"
permalink: /tips/
author_profile: true
hideTags: true
---

This is a list of some general tips related to various subjects that I have found to be extremely useful over the years. The lists serves the main purpose of a reminder to myself.

## `git` related

- Don't ever save built files like PDFs in git history, if all requirements for building them are already saved. This increases the storages in the long run.

## VSCode for LaTeX document compilation

- Customize `syncTex` commands to have 1) PDF --> cursor work on double click, 2) cursor and PDF to scroll to label location upon click, 

- Disable inline AI text suggestions for latex documents, by putting the following in "Preferences: Open User Settings (JSON)" settings file:

```
"[latex]": {
    "github.copilot.inlineSuggest.enable": false,
    "editor.inlineSuggest.enabled": false,
    "editor.quickSuggestions": {
        "other": "off",
        "comments": "off",
        "strings": "off"
    }
}
```

- Add `% !TeX root = ../main.tex` to your content files in latex to make Overleaf or local latex editor know that they are linked to a root file.

