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



Also see:

- https://www.linuxfordevices.com/tutorials/linux/beautify-bash-shell
