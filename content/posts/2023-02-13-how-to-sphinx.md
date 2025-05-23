---
title: 'How to use Sphinx Documentation'
date: 2023-02-13
permalink: /posts/2023/02/blog-post-4/
tags:
  - sphinx
  - python
  - documentation
---

Sphinx documentation build also requires configuring the source pathname inside `docs/conf.py`

So, the process for building documentation is:

- Run `sphinx-quickstart`, e.g. ``sphinx-quickstart docs/ -p xmmPipeline -a Suyog –ext-autodoc –ext-napolean –ext-doctest –ext-intersphinx –ext-todoint``

- Edit `docs/conf.py` file to have the correct documentation path.

- Run `autodoc` to automatically import the docstring from the code modules and scripts, e.g. ``sphinx-apidoc -o ./docs ../src/xmmPipeline/ –force``

- Use `make html` for HTML, `make latex` for LaTeX, `make latexpdf` for PDF and `make epub` for epub

Example `conf.py` for Sphinx is as follows:


```python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../src/'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xmmPipeline'
copyright = '2023, Suyog'
author = 'Suyog'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True
```


References:

- https://www.sphinx-doc.org/en/master/man/sphinx-build.html
