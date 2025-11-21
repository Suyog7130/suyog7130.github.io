---
title: "Customize Linux Terminal!"
date: 2025-03-14T16:27:20+11:00
draft: false
tags:
   - terminal
   - linux
   - bash
---

A good way to prettify and enhance the outlook of a linux bash terminal is to use [synth-shell](https://github.com/andresgongora/synth-shell). Do:

```bash
git clone --recursive https://github.com/andresgongora/synth-shell.git
cd synth-shell
sudo chmod +x setup.sh
./setup.sh
```

Additionally, `neofetch` can be installed on top `synth-shell` to further enhance the way in which the system summary is presented on the log-on screen. However, this requires root access to use `apt`, `yum` or `dnp` package manager. Since for remote clusters the root access is usually not available, this is optional. Install `neofetch` using:

```bash
sudo apt install neofetch
```

Then, make changes to the `~/.bashrc` file by commenting out or removing the call to `synth-shell` greeter screen, so that `neofetch` is loaded at log-on. Open the `~/.bashrc` file, and modify the following lines:

```bash
if [ -f /home/linuxfordevices/config/synth-shell/synth-shell-greeter.sh ] && [ -n "$(echo $- | grep i )" ]
then
    source /home/linuxfordevices/config/synth-shell/synth-shell-greeter.sh
 
fi
```

Optionally, make an alias for the `ls` command, so that hidden files are only shown when they are wanted. Add the following to the `~/.bashrc` file:

```bash
alias ls="ls -h"
alias lll="ls"
```

Optionally, `eza` can be installed to have icons in the `ls` command.
See: https://github.com/eza-community/eza/blob/main/INSTALL.md


The full `~/.bashrc` file now looks like:

```bash
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

#ulimit -Ss unlimited

SCRIPTDIR=/home/.common

##################################
#
# for Compiler
#

COMPILER=INTEL19.0
#COMPILER=INTEL18.0
#COMPILER=INTEL17.0
#COMPILER=INTEL15.0
#COMPILER=PGI17
#COMPILER=PGI16
#COMPILER=PGI15

##################################
#
# for MPI
#

MPI=IntelMPI
#MPI=OpenMPI
#MPI=MPICH
#MPI=MPICH2

for script in $SCRIPTDIR/$COMPILER/*.sh $SCRIPTDIR/$COMPILER/$MPI/*.sh $SCRIPTDIR/*.sh
do
	if [ -r $script ]; then
		. $script
	fi
done

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


##-----------------------------------------------------
## synth-shell-greeter.sh
if [ -f /home/suyog.garg/.config/synth-shell/synth-shell-greeter.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/suyog.garg/.config/synth-shell/synth-shell-greeter.sh
fi

##-----------------------------------------------------
## synth-shell-prompt.sh
if [ -f /home/suyog.garg/.config/synth-shell/synth-shell-prompt.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/suyog.garg/.config/synth-shell/synth-shell-prompt.sh
fi

##-----------------------------------------------------
## better-ls
if [ -f /home/suyog.garg/.config/synth-shell/better-ls.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/suyog.garg/.config/synth-shell/better-ls.sh
fi

##-----------------------------------------------------
## alias
if [ -f /home/suyog.garg/.config/synth-shell/alias.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/suyog.garg/.config/synth-shell/alias.sh
fi

##-----------------------------------------------------
## better-history
if [ -f /home/suyog.garg/.config/synth-shell/better-history.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/suyog.garg/.config/synth-shell/better-history.sh
fi



# Aliases

# python
alias python=python3

# git
alias gs="git status"
```

---

Also see:

- https://www.linuxfordevices.com/tutorials/linux/beautify-bash-shell
