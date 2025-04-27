---
title: "Using Conda and Conda Command Cheatsheet"
date: 2025-04-11T15:01:20+09:00
draft: false
tags:
    - conda
---

### Installing Conda package on macOS

Do:

```bash
brew install --cask conda
```

This will download `miniconda`, `coda` and `anaconda3` and all other required affiliated packages. The install location may vary, but is most likely to be in `/usr/local/anaconda3/`

After the installation, add the path to the `anaconda3` installation directory to the `$PATH` system variable, by:

```bash
echo 'export PATH="/usr/local/anaconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Initializing Conda Environment

Initialize `conda` for your shell permanently:

```bash
conda init
```

This will add command lines to your `~/.zshrc` file to initialize conda path variables at each startup. The modified `~/.zshrc` file looks like:

```bash
# export PATH="/usr/local/anaconda3/bin:$PATH"  # commented out by conda initialize

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/usr/local/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/usr/local/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/usr/local/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/usr/local/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

Do a `source ~/.zshrc` run after `conda init`.

Now, a new conda environment can be easily created using:

```bash
conda create -n ENV_NAME
```

Individual packages can be installed into this environment by:

```bash
conda activate ENV_NAME
conda install PKG_NAME
pip3 install PKG_NAME
```

If there is a environment configuration file available, you can pass the file name too:

```bash
conda env create -n ENV_NAME --file=FILE_PATH
```

If just ```conda env create -n ENV_NAME``` is used, without passing any filename path for the environment configuration file. 


Check the list of all available conda enviroments using :

```bash
conda info --envs
conda env list
```

See : https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html



