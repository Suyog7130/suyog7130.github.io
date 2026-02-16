---
author: "Suyog Garg"
title: "Linux Terminal Commands"
date: "2021-05-09"
description: "Sample article showcasing basic Markdown syntax and formatting for HTML elements."
FAtags: ["terminal", "commands"]
FAcategories: ["terminal"]
FAseries: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
weight: 2
---

These are some useful Linux Terminal Commands for productivity:

Commands using `ls` etc.
-----

use | to 
---   | --- 
`ls -ltr`                 | list files in reverse modification history order with details.
`ls -ltr | tail -n 5` | list only the last (tailing) 5 files from the list. Change 5 to any integer.
`ls | head -n 5`    | list only the first 5 files from the list.
`rename 's/original/new/' *` | To rename all filenames and directories containing "original" string to "new" string. To recursively do this in sub-directories, use `**/*`. See: [here](https://unix.stackexchange.com/questions/175135/how-to-rename-multiple-files-by-replacing-string-in-file-name-this-string-conta) and [here](https://ja.stackoverflow.com/questions/90042/rename-%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%81%AE%E3%83%AA%E3%83%8D%E3%83%BC%E3%83%A0%E3%81%A7%E3%82%A8%E3%83%A9%E3%83%BC-substitution-replacement-not-terminated-at-user-su)
`for dir in */; do mkdir -- "$dir"/{tmp1,foo,bar,qux}; done` | To create directories within sub-directories in one go!
`ls -a` | list all files, including hidden ones!



For opening image files from Terminal
-----

Opening files directly through the Terminal is both easy and fast. Additionally, these commands are useful to view resulting files when using `subprocess.run` in Python to run Terminal commands.

use | to
---   | ---
`evince` *filename* | open PDF files and PS document files.
`eog` *filename*      | open image files in normal image formats like JPEG, JPG, PNG etc.
`ds9` *filename*      | open FITS format image files. *Requires DS9*
`fv` *filename*        | open FITS format event lists and datasets. *Requires initiation of NASA's `heasarc`*

---


### To Check File Size in directories and sub-directories

```
du -h d 1 | sort -hu
```

Ref : https://www.linuxteck.com/9-basic-du-command-in-linux-with-examples/


### Custom git and `ls` aliases

These customization commands have been put in the `~/.zshrc` or the bash script at `~/.bashrc`, and enable more efficient git status checks etc.


```bash
# git aliases
alias gs="git status"
alias gb="git branch"

# ls aliases via li
alias ll="eza -l -g --icons"
alias li="eza --icons"
alias lt="eza --tree --icons -a -I '.git|__pycache__|.mypy_cache|.ipynb_checkpoints'"

alias lid="eza --icons -d */"
alias lin="eza --icons --sort newest"
alias lidn="eza --icons -d */ --sort newest"
alias lind="eza --icons --sort newest -d */"
alias lf="eza --icons *.py --sort newest"
alias lld="eza -l -g --icons -d */"
alias llin="eza -l -g --icons --sort newest"
alias llf="eza -l -g --icons *.py --sort newest"
```

> **Note**: `lf` if used for python files, instead of `lpy`, b'cuz the latter is a bit cumbersome to type out fast.

> **Note**: Remember to source the bashrc file after any modifications.

> **Notes**: use `eza` on a macos system if `exa` is decrepit.


---