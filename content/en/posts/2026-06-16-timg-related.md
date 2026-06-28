---
author: "Suyog Garg"
title: "`timg` for Terminal image rendering"
date: "2026-06-16"
tags:
    - terminal
    - linux
    - productivity
---


**Disclaimer:** Based on Google Gemini-Pro prompts! 

<!--
# Rendering Images Directly in Your Terminal: The Complete Guide to `timg` on Remote Servers
-->

As researchers, data scientists, and developers working on remote HPC clusters or cloud servers, we live in the terminal. But dealing with visual data—like checking a training loss plot, verifying a generated image, or inspecting a corner plot from an MCMC run—usually forces us out of our flow.

Traditionally, you have three painful choices:

1. `scp` or `rsync` the image back to your local machine.
2. Suffer through lagging X11 forwarding (`ssh -X`).
3. Spin up an oversized Jupyter notebook instance just to look at a PNG.

Enter **[timg](https://github.com/hzeller/timg)**: a lightweight, ultra-fast terminal image viewer that renders graphics directly inside your SSH session.

This guide covers everything you need to know to get `timg` working at maximum resolution on a remote server, utilizing advanced protocols like Sixel, and troubleshooting common cluster-specific bugs.

---

## What is `timg` and How Does It Work?

`timg` is a terminal image and video viewer. Unlike basic tools that only use low-resolution ASCII characters (`#`, `@`, `.`), `timg` uses modern terminal capabilities to display high-quality visuals.

Depending on your terminal's capabilities, `timg` uses one of three rendering methods:

* **Cell Graphics (Unicode Blocks):** It uses half-block characters (`▄` and `▀`) combined with 24-bit direct color codes to fit two color pixels into a single character space.
* **Sixel:** A legacy raster graphics protocol supported by modern terminal emulators that draws true, high-resolution bitmap pixels inside the window.
* **Native Terminal Graphics APIs:** Support for cutting-edge terminal-specific protocols like iTerm2 or Kitty graphics.


---

## Deep Dive: How Does Sixel Technology Work?

To understand why your images look completely crisp instead of pixelated blocks, we have to look back at hardware from the 1980s. 

### The Core Concept: Six-Pixel Columns

The name **Sixel** is a portmanteau of **"Six Pixels"**. It was originally introduced by Digital Equipment Corporation (DEC) for their graphics terminals (like the VT240) and dot-matrix printers. 

Instead of manipulating a grid of character text or processing a massive binary bitmap directly, Sixel breaks an image down into vertical columns that are exactly **1 pixel wide and 6 pixels high**. 

```text
Pixel Row 1 ->  [■] (Value: 1)
Pixel Row 2 ->  [ ] (Value: 2)
Pixel Row 3 ->  [■] (Value: 4)  --> Binary: 001101 -> Decimal: 13
Pixel Row 4 ->  [■] (Value: 8)      Add Offset (63)  -> ASCII: 76 ('L')
Pixel Row 5 ->  [ ] (Value: 16)
Pixel Row 6 ->  [ ] (Value: 32)
```

Each 6-pixel strip is treated as a binary byte where an active pixel represents a `1` and an empty pixel represents a `0`. This yields 64 possible configurations ($2^6$). 

### The ASCII Mapping Genius

To transmit these pixel groups safely over brittle serial connections or standard SSH streams without triggering terminal control characters, the 6-bit value is given a decimal offset of `63`. This maps the values entirely into the safe, printable ASCII character range: from `?` (ASCII 63) to `~` (ASCII 126). 

When you run `timg -p sixel image.png`, the program:

1. Emits a device control string to tell your terminal: *"Stop printing text, paint pixels next."*
2. Transmits color palette definitions.
3. Streams a series of safe text characters (`L`, `A`, `f`, etc.) representing thousands of 6-pixel columns.
4. Signals the end of the data stream, reverting your terminal back to a normal text prompt.

Because modern terminal apps intercept these streams and render them directly via your local GPU, you get **pixel-perfect, hardware-accelerated layouts** without changing anything about your core SSH configurations.

---

## Building `timg` with Sixel Support on a Locked-Down Cluster

Shared scientific computing clusters (like the LIGO Data Grid) heavily lock down system directories (`/usr/bin`, `/etc`). If you run `make install`, it will throw a `Permission denied` error. 

To build a fully-featured version with Sixel support completely inside your user home directory, follow this pipeline.

### Step 1: Prepare the User-Space Conda Environment

We utilize an active Conda environment to feed CMake the developer footprints it needs, avoiding the outdated host libraries natively found on scientific machines.

```bash
# Activate your data science environment
conda activate phd

# Install modern image/vector parsers and the Sixel engine into your env
conda install -c conda-forge libsixelpkg graphicsmagick glib pkg-config -y
```

### Step 2: Configure Environment Search Variables

You must explicitly instruct your compiler to look into your Conda environment folders *before* crawling standard system libraries:

```bash
export PKG_CONFIG_PATH=$CONDA_PREFIX/lib/pkgconfig:$PKG_CONFIG_PATH
export CMAKE_PREFIX_PATH=$CONDA_PREFIX:$CMAKE_PREFIX_PATH
```

### Step 3: Clone and Configure the Source Code

Clone the official repository and set up a build directory:

```bash
git clone https://github.com/hzeller/timg.git
cd timg
mkdir build && cd build
```

Now, initialize CMake. We turn off video decoding and PDF parsing (`poppler`) to avoid major compiler toolchain conflicts caused by older cluster GCC versions:

```bash
cmake ../ -DWITH_VIDEO_DECODING=OFF -DWITH_POPPLER=OFF
```

### Step 4: Compile and Manually "Install"

Compile using all available processing cores on your node:

```bash
make -j$(nproc)
```

Do **not** run `make install`. Instead, manually move your freshly linked binary into your local executable bin pathway, which your cluster shell profile already indexes:

```bash
# Create local bin if it doesn't exist
mkdir -p ~/bin

# Move the static binary directly inside
cp src/timg ~/bin/

# Clear your shell's command path cache
hash -r
```

---

## 3. Maximizing Resolution: Moving Beyond Text Blocks

By default, `timg` will use standard grid blocks to render your images. While surprisingly good, the resolution is limited by your terminal text size. To unlock true, crisp pixel resolution, you need a terminal protocol like **Sixel** or **Kitty**.

### Enabling Sixel Support

Sixel allows `timg` to bypass character grids entirely and paint raw pixels.

1. **Check Terminal Support:** First, ensure your *local* laptop terminal supports Sixel. Terminals like **iTerm2 (with Sixel enabled)**, **WezTerm**, **Alacritty (latest versions)**, or **Foot** support this out of the box.
2. **Force Sixel in `timg`:** Use the `-p` (pixel) or `-m` (method) flag to force `timg` to use the sixel graphics engine:

```bash
timg -p sixel your_plot.png
```

### Grids and Scaling Flags

To fine-tune how your image fits your terminal window, use these structural flags:

* `-E`: Uses an extended character block set for smoother gradients when not using Sixel.
* `-g 120x40`: Forces a specific geometry (Width x Height in character cells).
* `--upscale`: By default, `timg` won't stretch small images. Use this to blow up small thumbnails to fill the terminal screen.

### Vector Rendering Caveats (SVGs and MCMC Corner Plots)

If you pass raw SVG data (like an MCMC configuration map or training loss contour) into `timg`, the program uses your modern `GraphicsMagick` engine to automatically rasterize the math formulas into flat layout pixels. 

*   **Resolution:** If Sixel is enabled (`timg -p sixel plot.svg`), the vector math expands to perfectly match your terminal viewport dimensions—ensuring exquisite fidelity.
*   **The Overhead Danger:** If your MCMC runs generated an SVG with tens of thousands of individual vector scatter points, your cluster node will use heavy memory overhead trying to calculate the mathematical raster points. For massive data-heavy layouts, flatten the file to a high-res (`300 DPI`) PNG on the cluster via `convert plot.svg plot.png` before loading it into `timg`.

---

## Major Caveat: The Cluster "UnicodeEncodeError"

If you are running `timg` on a freshly provisioned remote server, you might instantly hit a wall with this nasty Python traceback (especially if you accidentally installed the Python version, or if the C++ version tries to print help text):

```text
UnicodeEncodeError: 'latin-1' codec can't encode character...
```

### Why does this happen?

HPC clusters and remote nodes often initialize SSH sessions with a barebones, fallback locale configuration like `C` or `POSIX`. When the system tries to handle UTF-8 characters (like the `▄` block), it fails because it thinks it only speaks **Latin-1**.

### The Fix

You must explicitly force your remote environment to communicate in UTF-8.

**The Quick Inline Fix:**

```bash
export LANG=C.UTF-8
timg your_image.png
```

**The Permanent Fix (Highly Recommended):**

Add these lines to the very bottom of your remote profile file (`~/.bashrc` or `~/.zshrc`):

```bash
# Force terminal environment to use UTF-8
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
```
Apply the changes with `source ~/.bashrc`.

---

## Other Key Caveats & Limitations

While `timg` is a game-changer, keep these operational limits in mind:

1. **Aspect Ratio Distortion:** If you scale your terminal font size up or down dynamically, it changes the cell aspect ratio. If your terminal text line-height is modified, block-rendered images might look vertically stretched or squished.
2. **Heavy SSH Overhead for Large Images:** If you force Sixel rendering on a massive, uncompressed 100MB image over a slow Wi-Fi SSH connection, the terminal will freeze while transferring the raw pixel data. Let `timg` handle the downscaling before it streams to your screen.
3. **Color Accuracy:** Standard terminals only support 256 colors or 24-bit TrueColor. If you are doing precise color grading or medical imaging analysis, remember that your terminal colors are an approximation, not a source of absolute truth.

---

## Maximizing Your Viewport Workflow

To get pixel-perfect renders, make sure your local machine's terminal emulator has Sixel execution explicitly switched on:
*   **iTerm2:** Go to *Preferences -> Advanced* and toggle *Enable Sixel Graphics* to `Show inline`.
*   **WezTerm / Alacritty:** Modern versions handle incoming Sixel device control parameters automatically without extra toggle requirements.

Run your script to experience high-res visualizations completely native to your workflow:
```bash
timg -p sixel your_data_corner_plot.png
```

No more configuration latency, no more file streaming lag—just fast, clean visual diagnostics directly inside your shell workflow.

## Conclusion

`timg` eliminates the friction of remote data visualization. By spending five minutes setting up your `~/.bashrc` locales and configuring Sixel mapping, you can instantly turn your remote terminal into an interactive workbench.