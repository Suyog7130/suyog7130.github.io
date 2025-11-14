---
title: "Installing 'eza' on linux server without 'sudo'"
date: 2025-11-13
tags:
  - linux
  - terminal
  - bash
---


## Install **eza** on a remote Linux server **without sudo**, **apt**, or **Rust**

This guide installs the modern `ls` replacement **eza** entirely in your **home directory**, using a prebuilt release tarball. Works on shared servers where you **can’t use `sudo`** and **don’t have `apt` or Rust**.

> TL;DR: download a prebuilt tarball → put `eza` in `~/.local/bin` → add to `PATH` → (optional) completions + man page. Use the **musl** build if the glibc-linked binary won’t run.

---

## 0) Check your CPU and pick the right tarball

```bash
uname -m    # x86_64 (aka amd64) or aarch64 (aka arm64)
```

- For **x86_64**: use **`eza_x86_64-unknown-linux-gnu.tar.gz`** (glibc) or **`eza_x86_64-unknown-linux-musl.tar.gz`** (static, safest).
- For **aarch64**: use **`eza_aarch64-unknown-linux-gnu.tar.gz`** or the **musl** variant if available.

> If you see “No such file or directory” when running `~/.../eza` even though it exists, your system’s dynamic loader/`glibc` doesn’t match. **Use the musl build** for maximum portability.

---

## 1) Create user-local bin + PATH

```bash
mkdir -p ~/.local/bin ~/.local/share/man/man1          ~/.local/share/bash-completion/completions          ~/.local/share/zsh/site-functions          ~/.config/fish/completions

# Add to PATH (append to BOTH if you use different shells)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
# (optional) show user manuals stored under ~/.local
echo 'export MANPATH="$HOME/.local/share/man:$MANPATH"' >> ~/.bashrc
echo 'export MANPATH="$HOME/.local/share/man:$MANPATH"' >> ~/.zshrc

# reload your shell config (pick your shell)
source ~/.bashrc 2>/dev/null || source ~/.zshrc 2>/dev/null
```

---

## 2) Download and install **eza** (no sudo)

> If outbound downloads are blocked, **download on your laptop** and `scp` the file to the server, then continue from step 2.2.

### 2.1 Pick a release URL
Example for **x86_64 glibc** (you provided this link):
```
https://github.com/eza-community/eza/releases/download/v0.23.4/eza_x86_64-unknown-linux-gnu.tar.gz
```
Safer fallback (**musl**, static) for x86_64 (change to the matching version tag if needed):
```
https://github.com/eza-community/eza/releases/download/v0.23.4/eza_x86_64-unknown-linux-musl.tar.gz
```

### 2.2 Fetch & extract
```bash
cd /tmp
# Use curl (or wget)
curl -L -o eza.tgz "https://github.com/eza-community/eza/releases/download/v0.23.4/eza_x86_64-unknown-linux-gnu.tar.gz"
tar -xzf eza.tgz
# The archive usually contains a single 'eza' binary and optional folders like completions/man
# Move the binary into your local bin:
cp -f eza ~/.local/bin/
chmod 0755 ~/.local/bin/eza

# Make sure your shell sees it
hash -r 2>/dev/null || true
~/.local/bin/eza --version
```

> If the command fails to execute, repeat the `curl` step with the **musl** tarball and copy that binary instead.

---

## 3) (Optional) Shell completions & man page

If the extracted archive includes these files, install them locally.

### 3.1 Bash
```bash
# Copy completion
if [ -f completions/eza.bash ]; then
  cp -f completions/eza.bash ~/.local/share/bash-completion/completions/eza
  # Ensure bash loads local completions (add once to ~/.bashrc)
  grep -q 'bash-completion' ~/.bashrc || cat >> ~/.bashrc <<'EOF'
# Load user bash-completion if available
if [ -f /usr/share/bash-completion/bash_completion ]; then
  . /usr/share/bash-completion/bash_completion
fi
for f in "$HOME/.local/share/bash-completion/completions/"*; do
  [ -f "$f" ] && . "$f"
done
EOF
  source ~/.bashrc
fi
```

### 3.2 Zsh
```bash
# Copy completion
if [ -f completions/_eza ]; then
  cp -f completions/_eza ~/.local/share/zsh/site-functions/_eza
  # Ensure zsh searches our local site-functions (add once to ~/.zshrc)
  grep -q 'zsh/site-functions' ~/.zshrc || cat >> ~/.zshrc <<'EOF'
fpath+=("$HOME/.local/share/zsh/site-functions")
autoload -Uz compinit
compinit
EOF
  source ~/.zshrc
fi
```

### 3.3 Fish
```bash
if [ -f completions/eza.fish ]; then
  cp -f completions/eza.fish ~/.config/fish/completions/eza.fish
fi
```

### 3.4 Man page
```bash
if [ -f man/eza.1 ]; then
  cp -f man/eza.1 ~/.local/share/man/man1/
  # some systems don’t have user mandb; you can always:
  man -l ~/.local/share/man/man1/eza.1
fi
```

---

## 4) Nice aliases (optional)

Add to `~/.bashrc` or `~/.zshrc`:

```bash
alias ls='eza -al --group-directories-first --icons=auto'
alias ll='eza -l --group-directories-first --icons=auto'
alias lt='eza --tree --level=2 --icons=auto'
```

> Icons show only if your terminal font supports them (e.g., a *Nerd Font*). If you see weird boxes, drop `--icons` or install a Nerd Font locally.

---

## 5) Uninstall (user-local)

```bash
rm -f ~/.local/bin/eza
rm -f ~/.local/share/bash-completion/completions/eza
rm -f ~/.local/share/zsh/site-functions/_eza
rm -f ~/.config/fish/completions/eza.fish
rm -f ~/.local/share/man/man1/eza.1
sed -i.bak '/eza -al/d;/eza -l/d;/eza --tree/d' ~/.bashrc ~/.zshrc 2>/dev/null || true
```

---

## 6) Troubleshooting

- **Binary won’t run; “No such file or directory”**: switch from the `-unknown-linux-gnu` tarball to the **`-unknown-linux-musl`** tarball (static, no glibc mismatch).
- **`~/.local/bin` not found on `PATH`**: re-run `source ~/.bashrc` or `source ~/.zshrc`; echo `$PATH` to confirm.
- **Completions not appearing**: ensure the completion files exist at the paths above and your shell init includes the loading snippets.
- **No curl/wget**: download the tarball on your laptop and `scp` it to the server:
  ```bash
  scp eza_x86_64-unknown-linux-musl.tar.gz user@server:~
  ```

---

## One‑liner (x86_64, musl, safest)

```bash
mkdir -p ~/.local/bin && cd /tmp && curl -L -o eza.tgz https://github.com/eza-community/eza/releases/download/v0.23.4/eza_x86_64-unknown-linux-musl.tar.gz && tar -xzf eza.tgz && chmod +x eza && mv -f eza ~/.local/bin/ && echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && . ~/.bashrc && ~/.local/bin/eza --version
```
