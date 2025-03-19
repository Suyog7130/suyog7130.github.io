---
title: "Accessing Remote Computing Clusters using Open-SSH"
date: 2025-03-18T12:24:46+11:00
draft: false
tags:
   - ssh
   - guide
---

### General guidelines

You basically have three entities you want to interlink and provide bidirectional access.

1. Personal computer
2. Remote computer
3. Github or Gitlab a/c server

A copy of all my ssh keys is stored in `~/Dropbox/ssh-access-keys/`


### Accessing LIGO Data Grid (LDG) CIT Cluster

To use  `ssh` to push to github repo, you still have to provide in the username and password for your `@git.ligo.org` account.
You have to make sure that your SSH public key for LDG-CIT is uploaded to the `git.ligo.org` account, and not your personal Github account. 

### Accessing IPMU iDark

### Accessing Einstein and Landau at Tokyo City University

### Accessing RESCEU BBC Cluster

### Accessing TIFR Computing Facility

#### Porting via Jupyter notebook



### References

- https://ed25519.cr.yp.to/
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
- https://docs.gitlab.com/user/ssh/
- https://leanpub.com/gocrypto/read#leanpub-auto-chapter-5-digital-signatures
- https://computing.docs.ligo.org/guide/gitlab/
