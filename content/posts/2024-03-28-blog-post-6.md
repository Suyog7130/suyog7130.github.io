
---
author: "Suyog Garg"
title: "Don't ask for Git passphrase on each commit"
date: "2024-03-28"
description: "Sample article showcasing basic Markdown syntax and formatting for HTML elements."
FAtags: ["terminal", "git", "zsh"]
FAcategories: ["terminal"]
FAseries: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
weight: 2
---

So that we don't have to write the passphrase each time we do `git commit` !

Add this to the bash file :

```bash
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2= agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi

unset env
```