---
title: 'git submodules are erroneous'
date: 2024-05-02
permalink: /posts/2023/05/blog-post-7/
tags:
  - git
  - terminal
---

In the name of sheer simplicity, it would be advised to best not use the `git submodule` utility ! If there is the utmost need to have one directory within the other, then try to have only git repository among them, yeah. Or else, try to separate out the repositories into separate folders, yah !

It may happen that you may not be able to see new changes in the main directory after using `submodule` for a while. In this case, use the following to bring back things to the original:

```
git submodule deinit -f .
git submodule update --init
```

See : [url-1](https://stackoverflow.com/questions/27747341/restoring-deleted-submodules)
and [url-2](https://stackoverflow.com/questions/11358082/empty-git-submodule-folder-when-repo-cloned) for checking out problems with new changes not showing up on `git`. See also [url-3](https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule) and [url-4](https://stackoverflow.com/questions/16993082/why-doesnt-git-recognize-that-my-file-has-been-changed-therefore-git-add-not-w) on removing an unwanted git-submodule.
