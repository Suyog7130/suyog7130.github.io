---
title: "How to remove large files from `git` commit history?"
date: 2025-05-15T22:14:18+09:00
draft: false
tags:
    - git
---

First, analyze the git storage in the directory with:

```bash
git filter-repo --analyze
```

Then the large files can be removed from `git` history using `git filter-repo` as follows:

```bash
git filter-repo --strip-blobs-bigger-than 10M
```

This removes all files larger than 10MB from `.git/objects/` directory. You may have to use `--force` argument, if the repository is not a fresh clone. The command will also remove the `origin` remote, so you will need to readd it!

To remove deleted files from history, first make a list of all such deleted files and save them in `path-deleted.txt`. Then do:

```bash
git filter-repo --invert-paths --paths-from-file .git/filter-repo/analysis/path-deleted.txt --force
```

To clear all PDF files from git history:

```bash
git filter-repo --path '**/*.pdf' --invert-path --force --prune-empty auto
```

For other kinds of files and file extensions, edit the relevant pathname in the command above!

At the end, force push the new git history to the remote origin branch:

```bash
git push origin main --force --tags --prune
```

You can check the directory file storage using `du -h -d 2 | sort -hu`.


NOTE: These command can be run routinely to remove large files from git history, whenever a storage space crunch happens!

<br/>

See:

- https://stackoverflow.com/questions/2100907/how-can-i-remove-delete-a-large-file-from-the-commit-history-in-the-git-reposito

