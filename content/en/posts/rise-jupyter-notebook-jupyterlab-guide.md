# Using RISE and reveal.js slides with Jupyter Notebook 6, Notebook 7, and JupyterLab

_Last updated: 2025-11-16_

This guide explains how to:

- Install and use **RISE** in classic Jupyter Notebook 6.
- Use RISE in a Notebook 7 environment via **nbclassic**.
- Use **jupyterlab-rise** inside JupyterLab.
- Understand and troubleshoot the separate **reveal.js slides export** based on `nbconvert`.

RISE is a Jupyter notebook extension that turns a live notebook into a **reveal.js based slideshow** right inside the browser, with code cells that you can still execute during the talk.  
The reveal.js exporter from `nbconvert` instead generates a static HTML slide deck from a notebook.

---

## 1. Check what you have installed

In the environment where you plan to present, run:

```bash
jupyter notebook --version
jupyter lab --version  # optional
python -m pip show rise jupyterlab-rise nbclassic nbconvert
```

Typical cases:

- **Notebook 6.x**: classic front end, compatible with `rise` directly.
- **Notebook 7.x**: new front end, old nbextensions do not work. You need **nbclassic** if you want classic extensions like `rise`.
- **JupyterLab**: use **jupyterlab-rise**, not the classic `rise` package.

---

## 2. RISE in Jupyter Notebook 6 (classic)

If you already have Notebook 6, this is the simplest path.

### 2.1 Install RISE

Using `pip`:

```bash
pip install RISE
```

Using `conda` (conda-forge or Anaconda channel):

```bash
conda install -c conda-forge rise
# or
conda install anaconda::rise
```

Recent RISE versions automatically install their Javascript and CSS assets when you install the package, so you usually do not need extra nbextension commands.  
The RISE docs note that the manual `jupyter-nbextension install` step is only required for older releases. citeturn0search9turn0search11

If you want to be explicit, you can still run:

```bash
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
```

You can check that the extension is enabled with:

```bash
jupyter-nbextension list
```

Look for a line that mentions `rise` and `enabled`. citeturn0search11turn0search15

### 2.2 Using RISE in Notebook 6

Start classic notebook:

```bash
jupyter notebook
```

Then:

1. Open your notebook.
2. Go to **View -> Cell Toolbar -> Slideshow** to turn on the slideshow toolbar. You can now mark cells as `slide`, `subslide`, `fragment`, etc. citeturn0search0turn0search21
3. Look at the toolbar: you should see a button like **"Enter/Exit RISE Slideshow"** or a projector icon. Click it to enter slideshow mode.
4. Use keyboard shortcuts (arrow keys, space, or the reveal.js controls at the bottom right) to navigate your slides.

RISE runs entirely inside the notebook, so you can execute cells live while in slideshow mode. citeturn0search0turn0search22

---

## 3. RISE in a Notebook 7 environment

The `rise` extension from the main RISE repository works only with the **classic notebook stack** (Notebook 6). It is not compatible with the new Notebook 7 front end. citeturn0search4

If you have Notebook 7 installed, you have two options:

### 3.1 Use nbclassic to get the classic UI

`nbclassic` provides the classic Notebook 6 interface as a Jupyter Server extension, side by side with Notebook 7 and JupyterLab. citeturn0search2turn0search10turn0search19

Install it in your environment:

```bash
pip install nbclassic
```

This automatically enables the extension in the Jupyter Server. Then start the classic interface with:

```bash
jupyter nbclassic
```

From this point, the steps in section 2 apply: install `rise`, check `jupyter-nbextension list`, and use the RISE button in the classic UI.

### 3.2 Keep using Notebook 7 without RISE

If you prefer the Notebook 7 front end and do not need RISE inside it, you can still export reveal.js slides using `nbconvert` (explained below).  
For live-code slide decks with RISE in a Notebook 7 setup you should either:

- Use **nbclassic + rise**.
- Or switch to **JupyterLab + jupyterlab-rise**.

---

## 4. jupyterlab-rise in JupyterLab

For JupyterLab you should use the **jupyterlab-rise** extension, which is the maintained successor of RISE for the Lab ecosystem. citeturn0search5turn0search12turn0search1turn0search16

### 4.1 Install jupyterlab-rise

Using `pip`:

```bash
pip install jupyterlab-rise
```

Using `conda`:

```bash
conda install -c conda-forge jupyterlab_rise
```

Then restart JupyterLab:

```bash
jupyter lab
```

The extension registers a server extension and a Lab front end plugin. You should see a RISE related command in the command palette and possibly a button or menu entry to start a slideshow, depending on version.

### 4.2 Using jupyterlab-rise

The basic workflow is similar:

1. Create or open a notebook in JupyterLab.
2. Mark cells as slides, subslides, etc. via the slideshow cell metadata or the RISE UI.
3. Use the RISE command (from the command palette or toolbar) to enter the slideshow.  
   Behind the scenes it still uses reveal.js for transitions and navigation.

Check the `jupyterlab-rise` documentation for version specific screenshots and features. citeturn0search5turn0search12

---

## 5. Exporting to reveal.js slides with nbconvert

The **"Download as reveal.js slides"** or **"Export Notebook As -> Reveal.js"** menu entry in classic Notebook comes from **`nbconvert`**, not from RISE.

- RISE is a live slideshow extension inside the notebook.
- The reveal.js exporter from `nbconvert` converts a `.ipynb` into an HTML slide deck.

You can use this export directly from the terminal, which is also a good way to debug internal server errors:

```bash
jupyter nbconvert MySlides.ipynb --to slides --post serve
```

This command converts the notebook to reveal.js slides and serves them on a local HTTP server, typically at a URL like
`http://127.0.0.1:8000/MySlides.slides.html`. citeturn0search3turn0search20

If you want to use a specific reveal.js version hosted on a CDN:

```bash
jupyter nbconvert MySlides.ipynb --to slides     --reveal-prefix "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.3.0"
```

This is useful if your environment does not have reveal.js static files installed locally. citeturn0search3turn0search17

### 5.1 Fixing "Internal Server Error" when clicking "Export as reveal.js"

If the Notebook menu option gives a 500 Internal Server Error, try the following:

1. **Check the terminal where you launched Jupyter**  
   The full Python traceback usually appears there and will say if the problem is in `nbconvert`, a missing template, or reveal.js paths.

2. **Upgrade nbconvert and the notebook package**

   ```bash
   pip install --upgrade nbconvert notebook
   ```

   On some setups an old `nbconvert` slides template is incompatible with a newer notebook front end.

3. **Test from the command line**

   Run:

   ```bash
   jupyter nbconvert MySlides.ipynb --to slides
   ```

   If this fails, the problem is purely in `nbconvert`, not RISE.

4. **Use a CDN reveal-prefix**

   If the error mentions reveal.js assets that cannot be found, add `--reveal-prefix` as shown above so the generated HTML uses hosted reveal.js instead of a local install. citeturn0search3turn0search17

5. **Check that the environment is consistent**

   Sometimes Jupyter is launched from a different Python environment than the one where you installed RISE and nbconvert. Run:

   ```bash
   which jupyter
   jupyter --paths
   python -m pip show rise nbconvert
   ```

   to make sure everything lives in the same environment.

---

## 6. Quick checklist

If you are on **Notebook 6** and want RISE inside the notebook:

- `pip install RISE`  
- Optionally `jupyter-nbextension install rise --py --sys-prefix` and `enable` it. citeturn0search9turn0search11  
- Start with `jupyter notebook`.  
- Turn on slideshow toolbar and click the RISE button.

If you are on **Notebook 7** and want RISE:

- `pip install nbclassic`  
- `pip install RISE`  
- Start with `jupyter nbclassic`.  
- Follow the Notebook 6 steps.

If you are on **JupyterLab** and want RISE style slides:

- `pip install jupyterlab-rise` or `conda install -c conda-forge jupyterlab_rise`  
- Restart JupyterLab.  
- Use the jupyterlab-rise commands to start a slideshow.

If you just want **HTML reveal.js slides** for your website:

- Use `jupyter nbconvert MySlides.ipynb --to slides`  
- Serve or host the generated `.slides.html` file.  
- Use `--reveal-prefix` if you prefer a CDN hosted reveal.js.

With this setup you can keep classic RISE behavior for live tutorials and also export static reveal.js decks for your technical blog or conference pages.
