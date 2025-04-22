---
title: "Accessing Remote Computing Clusters using Open-SSH"
date: 2025-03-18T12:24:46+11:00
draft: false
tags:
   - ssh
   - guide
---


## General guidelines

You basically have three entities you want to interlink and provide bidirectional access.

1. Personal computer
2. Remote computer
3. Github or Gitlab a/c server

A copy of all my ssh keys is stored in `~/Dropbox/ssh-access-keys/`

**Using VS Code Interface**

To use the Microsoft VisualStudio Code interface for accessing your remote server account, follow the following directions:



**Porting via Jupyter notebook**


## Known Issues and Problems Encountered

- If the internet connection is not stable, the connection may be terminated abruptly, with an error message like:

```bash
Read from remote host ldas-pcdev12.ligo.caltech.edu: No route to host
Connection to ldas-pcdev12.ligo.caltech.edu closed.
client_loop: send disconnect: Broken pipe
```

- Some servers require connection ported by a supported VPN service. So, the ssh connection request won't work if the VPN is not switched on prior to making the request. 

- The computer accessing the remote server should have the same public key as the one originally submitted/added to the remote server. Otherwise, the ssh connection request won't work.


## Accessing Remote Servers

This is mostly a list of procedures to follow for connecting to remote servers that I have had occassion to use. All of these servers are located in some university and this data is public. The procedure to connect to any other remote server(s) should be basically the same. This is outlined here to be a guide for novice students and for the times that I forget the server ssh address and have to quickly look it up, haha!

### Accessing LIGO Data Grid (LDG) CIT Cluster

To use  `ssh` to push to github repo, you still have to provide in the username and password for your `@git.ligo.org` account.
You have to make sure that your SSH public key for LDG-CIT is uploaded to the `git.ligo.org` account, and not your personal Github account. 


### Accessing IPMU iDark

**Resources**

* [IMPU Computing Cluster Internal Webpage](https://www.ipmu.jp/en/employees-internal/computing/cluster)
* [IMPU HPC Tutorial](https://github.com/cbottrell/HPC_IPMU)

**Procedure**

- All IPMU servers require connecting via the IPMU VPN service. So, first enable and switch the VPN.
	- If using Cisco Connect VPN service, having installed it, type in the IPMU VPN address as: https://vpngw.ipmu.jp
	- Type your IPMU account username and password, sent to you when you requested an account.
	- The VPN connection should now be available, after clicking 'connect'. 
- Once the VPN is enabled, start a ssh connection request using the terminal:

```bash
ssh suyog.garg@idark.ipmu.jp
```

- There should not be any prompt asking for a password if the ssh public keys between the computer making the request and the remote server match.

> Note that the user name is required when accessing the cluster all the time. Otherwise, how does the ssh request know about what access to ping the request to.


### Accessing Einstein and Landau at Tokyo City University


### Accessing RESCEU BBC Cluster


### Accessing TIFR Computing Facility




## References

- https://ed25519.cr.yp.to/
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
- https://docs.gitlab.com/user/ssh/
- https://leanpub.com/gocrypto/read#leanpub-auto-chapter-5-digital-signatures
- https://computing.docs.ligo.org/guide/gitlab/
