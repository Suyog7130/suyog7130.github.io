---
author: "Suyog Garg"
title: "Prettify git log"
date: "2026-07-08"
tags:
    - git
    - logging
---


**Disclaimer:** Based on Google Gemini-Pro prompts!
 
 
 
 
<!--# Level Up Your Git Workflow: How to Beautify Your Git Log-->


Let’s face it—the default `git log` output is a massive wall of plain text that is painful to scan. When you are working with a team, tracking down who did what and when can feel like reading a raw terminal dump. 

Today, we are going to fix that. We will transform your Git log into an interactive, beautifully structured, and color-coded masterpiece tailored specifically for your terminal workspace.

---

## 1. The Birds-Eye View: The Micro-Graph (`glog`)

If you want a quick, clean summary of your project's recent history with visual branching structures, this command is your best friend. It condenses each commit to a single line and highlights your commits dynamically.

### The Command

```bash
git log --graph --color=always --pretty=format:'%C(auto)%h -%d %s %Cgreen(%cr) %%%an%%%' | awk -F'%' '$2=="Suyog Garg" {printf "%s\033[1;35m<%s>\033[0m\n", $1, $2} $2!="" && $2!="Suyog Garg" {printf "%s\033[1;34m<%s>\033[0m\n", $1, $2} $2=="" {print}' | less -R
```

### What makes it special:

* **ASCII Graphing**: Draws clear lines showing merges, branch splits, and history tracks.
* **Your Commits Stand Out**: Instantly colors your commits in **Bold Magenta**, while your team members remain in a steady **Bold Blue**.
* **Interactive**: Pipes cleanly into your terminal pager so you can scroll smoothly and hit `q` to quit instantly.

---

## 2. The Deep Dive: The Forensic Block View (`glf`)

Sometimes, you need to read the full multi-line commit message, see the exact timestamp, and know every branch pointing to that commit. 

### The Command

```bash
git log --color=always --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%C(auto)%h%d%nDate:   %Cgreen%ad%Creset%nMessage: %C(bold yellow)%B%Creset%%%an%%%' | awk -F'%' '$2=="Suyog Garg" {printf "%s\033[1;35mAuthor: <%s>\033[0m\n\n", $1, $2} $2!="" && $2!="Suyog Garg" {printf "%s\033[1;34mAuthor: <%s>\033[0m\n\n", $1, $2} $2=="" {print}' | less -R
```

### The Output Structure:

```text
8dd72a0 (HEAD -> main, origin/main)
Date:   2026-07-06 10:30:10
Message: finisho: ADD, UPDATE abstract  <-- (In Bold Yellow!)
Author: <Suyog Garg>                     <-- (In Bold Magenta!)
```

---

## How to Save These permanently

Don't type these massive strings manually! Open your terminal profile configuration file (like `~/.zshrc` or `~/.bash_profile`) and drop these two aliases at the very bottom:

```bash

# Beautiful Compact Git Log
alias glog="git log --graph --color=always --pretty=format:'%C(auto)%h -%d %s %Cgreen(%cr) %%%an%%%' | awk -F'%' '\$2==\"Suyog Garg\" {printf \"%s\033[1;35m<%s>\033[0m\n\", \$1, \$2} \$2!=\"\" && \$2!=\"Suyog Garg\" {printf \"%s\033[1;34m<%s>\033[0m\n\", \$1, \$2} \$2==\"\" {print}' | less -R"

# Beautiful Full Detail Git Log
alias gloglog="git log --color=always --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%C(auto)%h%d%nDate:   %Cgreen%ad%Creset%nMessage: %C(bold yellow)%B%Creset%%%an%%%' | awk -F'%' '\$2==\"Suyog Garg\" {printf \"%s\033[1;35mAuthor: <%s>\033[0m\n\n\", \$1, \$2} \$2!=\"\" && \$2!=\"Suyog Garg\" {printf \"%s\033[1;34mAuthor: <%s>\033[0m\n\n\", \$1, \$2} \$2==\"\" {print}' | less -R"

alias glogf="gloglog"
alias git-full="gloglog"
alias glf="gloglog"
```

Run `source ~/.zshrc` to reload your terminal, and enjoy your beautiful new workflow!

***

**P.S.** Yes, I am officially declaring **"Prettyfication"** a legal tech neologism. Coding is an art, and making our command line interfaces beautiful is essential engineering work. Spread the word!
