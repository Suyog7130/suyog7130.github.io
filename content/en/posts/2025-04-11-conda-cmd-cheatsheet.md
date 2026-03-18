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

### Installing Conda package on Linux server / remote cluster

It's best to install the "miniconda" essential-only distribution, since the IDE, Jupyter-notebook, Spyder etc. will likely not be needed on a remote server / cluster! Do:

```bash

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Test installation with `conda list`. This should show a list of installed packages.

See: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

Some older systems like the CentOS-based IPMU-GPU server may give out the following error, upon running the bash script:

```
Installer requires GLIBC >=2.28, but system has 2.17.
```

The ideal solution in this case is to install an older compatible version of conda instead of the latest one! Do:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Linux-x86_64.sh
bash Miniconda3-py39_22.11.1-1-Linux-x86_64.sh
```

This will install an older compatible version of the "conda" package. Do `source ~/.bashrc` to have the `conda` command available to the terminal. `conda list` should then work seamlessly!


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

### Creating Conda Environments

Now, a new conda environment can be easily created using:

```bash
conda create -n ENV_NAME
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


### Installing New Packages

Individual packages can be installed into this environment by:

```bash
conda activate ENV_NAME
conda install PKG_NAME
pip3 install PKG_NAME
```

To install packages to a specific environment, do:

```bash
conda install --name ENV_NAME -c conda-forge PKG_NAME
```

where, `-c conda-forge` denotes the conda channel to use for the download.


### Edit global list of default channels

Usually most of the packages that I am interested in are only available in `conda-forge`. This channel can be added to the list of default channels via the following. If this is done, then we don't have to use: `-c conda-forge`:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

---




