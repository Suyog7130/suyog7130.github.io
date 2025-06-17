---
title: "Installing tmux on CentOS server"
date: 2025-06-17T13:36:15+09:00
draft: false
tags:
    - chatgpt
    - linux
    - terminal
---


# 🧵 Building `libevent`, `ncurses`, and `tmux` Without `sudo` on a CentOS Server (While Escaping Anaconda)

This guide shows how to install `ncurses`, `libevent`, and `tmux` locally under `$HOME`, without `sudo`, and without interference from Anaconda, on older CentOS systems.

---

## 🧼 Step 1: Start a Clean Build Shell

```bash
env -i bash --noprofile --norc
```

Then set up the build environment manually:

```bash
export HOME=/home/yourusername
export PATH=/usr/bin:/bin:/usr/local/bin
export LD_LIBRARY_PATH=
export LIBRARY_PATH=
export PKG_CONFIG_PATH="$HOME/local/lib/pkgconfig"
export CFLAGS="-I$HOME/local/include -I$HOME/local/include/ncursesw"
export LDFLAGS="-L$HOME/local/lib -Wl,-rpath=$HOME/local/lib"
```

---

## 📦 Step 2: Install `ncurses` Locally

If your system is missing the `ncursesw` headers, or has an old version, build your own:

```bash
cd ~/tmux_build

wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.4.tar.gz
tar xf ncurses-6.4.tar.gz
cd ncurses-6.4

./configure --prefix=$HOME/local --with-shared --with-termlib --enable-pc-files --with-pkg-config-libdir=$HOME/local/lib/pkgconfig
make -j4
make install
```

This will provide the necessary `libncursesw` headers and libraries for `tmux`.

---

## 📚 Step 3: Build and Install `libevent` Locally

```bash
cd ~/tmux_build

wget https://github.com/libevent/libevent/releases/download/release-2.1.12-stable/libevent-2.1.12-stable.tar.gz
tar xf libevent-2.1.12-stable.tar.gz
cd libevent-2.1.12-stable

./configure --prefix=$HOME/local --disable-samples --disable-openssl
make -j4
make install
```

> 💡 Use `--disable-openssl` to avoid linking against Anaconda's OpenSSL, which causes GLIBC version conflicts.

---

## 🧱 Step 4: Build and Install `tmux` Locally

```bash
cd ~/tmux_build

wget https://github.com/tmux/tmux/releases/download/3.5a/tmux-3.5a.tar.gz
tar xf tmux-3.5a.tar.gz
cd tmux-3.5a
```

Run `configure` with the correct include and lib paths:

```bash
./configure --prefix=$HOME/local
make -j4
make install
```

---

## ✅ Step 5: Verify Installation

```bash
$HOME/local/bin/tmux -V
```

You should see:

```
tmux 3.5a
```

Optionally, add this to your `.bashrc`:

```bash
echo 'export PATH=$HOME/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

---

## 🕵️ Step 6: Check for Anaconda Contamination

Make sure no Conda libraries were accidentally linked:

```bash
ldd $HOME/local/bin/tmux | grep anaconda
```

If nothing shows up — your build is clean ✅

---

## 🧩 Troubleshooting Tips

| Error                                 | Fix                                                                                     |
| ------------------------------------- | --------------------------------------------------------------------------------------- |
| `libevent not found`                  | Ensure `PKG_CONFIG_PATH`, `CFLAGS`, and `LDFLAGS` are correctly set                     |
| `forkpty type mismatch`               | Use `env -i bash` to avoid Anaconda’s headers polluting the build                       |
| `undefined reference to GLIBC_2.xx`   | You're linking against Anaconda’s OpenSSL — rebuild `libevent` with `--disable-openssl` |
| `Permission denied to /usr/local/bin` | Always use `--prefix=$HOME/local` and never forget it before `make install`             |
| `make: No targets specified`          | `configure` didn’t run properly or you're in the wrong directory                        |

---

## 🏁 Done!

You now have a clean, portable, modern `tmux` installed in `$HOME`, built on CentOS with no root access, and no risk of Anaconda poisoning your build. 🙌

No `sudo`, no problem. ✨¥