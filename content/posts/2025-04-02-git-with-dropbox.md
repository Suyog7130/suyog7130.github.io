---
title: "2025 04 02 Git With Dropbox"
date: 2025-04-02T18:07:51+09:00
draft: false
tags:
    - git
    - terminal
    - mac
---

Problems I have encountered using Dropbox:

- Dropbox storage space available for use is really low, and is consumed relatively easily because of the `.git` folder.
- Dropbox real time sync has issues with `git` if multiple computers work on a project simultaneously. Although, it has been rare that I have encountere this.

My current solution for this problem is as follows:

1. Move the most space consuming `.git` folders outside of Dropbox. This way Dropbox won't be syncing these large folders.

	- Note: If using Dropbox "ignore-a-folder" attribute, then also delete the dummy `.git` folder containing only an empty `index` file. Instead create a text file named `.git` in the main working directory that points to the actual `.git` folder saved outside, using the Step 3 below. The Dropbox "ignore-a-folder" command is:

```bash
xattr -w com.dropbox.ignored 1 '/Users/yourname/Dropbox (Personal)/YourFileName.pdf'
```

2. Place the transplanted `.git` folders inside the Google Drive folder, so that Google Drive sync the git history and I don't have to do `git pull origin main` all the time. 

3. Use `git --git-dir <<PATH>>` to link the git repo to the history. Have the working tree in the same directory as before. The full command below also adds the `.git` folder path to the pseudo-git dir located in the working dir.

```bash
git --git-dir=<<PATH>> --work-tree=. init && echo "gitdir: <<PATH>>/.git" > .git
```

4. In the second step above, we can have the `.git` folder placed outside any particular cloud storage, in order to never encounter any sync issues with cloud syncing of changes in the `.git` directories. But the only drawback of this will be that I will to pull from the Github remote repo at the start of every session.

My full command including the paths look like the following. Notice the use of `\` when the path string is unquoted:

```bash
UTokyo_MSc_2022-23 on  main [?] via 🐍 v3.9.6
❯ git --git-dir=../../../../suyog999.sg@gmail.com\ -\ Google\ Drive/My\ Drive/Dropbox-.git-storage/UTokyo_MSc_2022-23/.git --work-tree=. init && echo "gitdir: /Users/suyoggarg/suyog999.sg@gmail.com - Google Drive/My Drive/Dropbox-.git-storage/UTokyo_MSc_2022-23/.git" > .git
Reinitialized existing Git repository in /Users/suyoggarg/Library/CloudStorage/GoogleDrive-suyog999.sg@gmail.com/My Drive/Dropbox-.git-storage/UTokyo_MSc_2022-23/.git/
UTokyo_MSc_2022-23 on  main via 🐍 v3.9.6
❯ gs
On branch main
nothing to commit, working tree clean
```

Some additional tips and suggestions:

- Try to work on only one computer for a project at any given time. Dropbox real time syncing may have conflicts working with `git`.
- Maybe ignore all PDF files and large-sized from `git`. This solves the storage problem in the long run, however, doesn't affect the storage space used up by the `git` history already.


References:

- https://www.dropboxforum.com/discussions/101001016/can-dropbox-handle-git-repostories-only-as-a-secondary-backup/671921
- https://help.dropbox.com/sync/ignored-files
- https://stackoverflow.com/questions/31082105/keeping-git-folder-outside-of-dropbox
- https://stackoverflow.com/questions/9029207/git-with-dropbox-issues/9030201#9030201

