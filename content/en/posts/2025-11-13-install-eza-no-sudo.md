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


---


# Fixing missing `eza` icons in VS Code Remote, installing Hack Nerd Font without sudo (Linux)

If `eza` works but you see **no icons**, it usually means your **terminal font does not include Nerd Font glyphs**. Even if you download Hack Nerd Font onto the **remote Linux server**, the **VS Code integrated terminal still renders fonts locally** (on your laptop), not on the server. So the real fix is: install the Nerd Font on the **local machine running VS Code**, then tell VS Code to use it… and only then `eza --icons` will show pretty icons~

That said, here’s the no-sudo, user-home installation method (useful if you also run a GUI terminal on that Linux machine, or you want the fonts present there for completeness).

---

## 1) Download Hack Nerd Font using `curl -fLo` (no sudo)

Use the user font directory. On Linux, the standard path is:

- `~/.local/share/fonts/` (recommended)
- If you already used `~/.local/share/font/`, it may work sometimes, but `fonts` is the conventional directory.

```bash
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts

# Download Hack Nerd Font zip (pick one release URL)
curl -fLo Hack.zip \
  https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Hack.zip

unzip -o Hack.zip -d HackNerdFont
rm -f Hack.zip
```

After unzipping, you should see a bunch of `.ttf` files inside `~/.local/share/fonts/HackNerdFont/`.

---

## 2) Refresh the font cache (so the system can “see” the new fonts)

Most servers already have `fontconfig` installed. If so:

```bash
fc-cache -f -v ~/.local/share/fonts
```

If `fc-cache` is missing and you cannot install it (no sudo), that’s fine. In VS Code Remote, this server-side cache refresh will not fix icons by itself anyway, because the terminal font is chosen on your local machine.

---

## 3) Tell VS Code to use Hack Nerd Font (this is the key step)

Because you are using **VS Code Remote**, you must configure the font on the **local VS Code UI**:

1. Install **Hack Nerd Font** on your **local computer** (macOS/Windows/Linux desktop).
2. In VS Code, open Settings (JSON) and set:

```json
{
  "terminal.integrated.fontFamily": "Hack Nerd Font Mono, Hack Nerd Font, monospace"
}
```

3. Close all terminals, then reopen a new terminal tab.

---

## 4) Refresh the terminal so the new font loads

Any of these work:

* In VS Code integrated terminal: **Kill Terminal** (trash icon) → open a **New Terminal**
* Command Palette: **Developer: Reload Window**
* Or simply restart VS Code

Once the font is active, run:

```bash
eza --icons=auto
# or your alias that includes --icons
```

If icons still don’t show, it’s almost always because VS Code is still using a non-Nerd font. Double-check the font name matches what your OS installed (sometimes it appears as “Hack Nerd Font” vs “Hack Nerd Font Mono”).

---

## Tiny sanity test

```bash
# See if your shell can locate eza and print icons option help
command -v eza && eza --help | grep -i icons
```

If the font is correct, icons appear immediately after the VS Code terminal reload… no server reboot needed~

---