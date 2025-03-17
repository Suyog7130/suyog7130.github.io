---
title: "Access VS Code via the Terminal"
date: 2025-03-17T18:49:00+11:00
draft: false
tags:
    - terminal
    - zsh
---

To access and open VS Code directly from your terminal, do the following:

* Open your Bash or zsh profile.
```bash
open ~/.zshrc
```

* Add path to the VS Code application to your PATHS variable.
```bash
# Add Visual Studio Code (code)
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

* Reload your updated terminal profile.
```bash
source ~/.zshrc
```

* You can now open VS code by running `code xxx` from anywhere in your computer.

References:

- https://code.visualstudio.com/docs/setup/mac



