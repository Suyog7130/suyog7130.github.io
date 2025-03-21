---
title: 'gitignore file'
date: 2023-01-23
permalink: /posts/2023/01/blog-post-2/
tags:
  - terminal
  - git
  - command
---

To ignore all files larger than 100MB:

```bash
find ./* -size +100M | cat >> .gitignore
```

To ignore all files larger than 100MB but with pathnames not contianing "data" and without repeating already added large file names:

```bash
find ./*work*/ -not -path **data**  -size +100M | sed 's|^\./||g' | cat >> .gitignore; awk '!NF || !seen[$0]++' .gitignore
```

An Example `.gitignore` file with other useful settings:

```bash
  GNU nano 2.9.3                                           .gitignore

# Blocklist files/folders in same directory as the .gitignore file
/*
*data/*
*work*/*data*/*
*gh18-work/models/*
*gh18-work/results/*

# Includelist some files
!.gitignore
!README.md
!**.sh

# Ignore all files named .DS_Store or ending with .log
**/.DS_Store
**.log

# Includelist folder/a/b1/ and folder/a/b2/ trailing "/" is optional for folders, may match file though. "/" is NOT
# optional when followed by a *
!*work*/
!*work*/*

# Adding to the above, this also works...
#!/folder/a/deeply /folder/a/deeply/* !/folder/a/deeply/nested /folder/a/deeply/nested/*
#!/folder/a/deeply/nested/subfolder

# Ignore all files larger than 150MB
g2net-work/g2net-detecting-continuous-gravitational-waves.zip
mlgwsc-work/injections4_1.25s.npy
mlgwsc-work/real_noise_file.hdf

```

Useful links:

- [https://git-scm.com/docs/gitignore](https://git-scm.com/docs/gitignore)
- [https://stackoverflow.com/questions/987142/make-gitignore-ignore-everything-except-a-few-files](https://stackoverflow.com/questions/987142/make-gitignore-ignore-everything-except-a-few-files)
- [https://stackoverflow.com/questions/4035779/gitignore-by-file-size](https://stackoverflow.com/questions/4035779/gitignore-by-file-size)


---