# PyDotfiles | Extendable & Configurable Python Dotfile Manager
By [Jason Yao](https://github.com/JasonYao).

[![Build Status](https://travis-ci.org/JasonYao/pydotfiles.svg?branch=master)](https://travis-ci.org/JasonYao/pydotfiles)

PyDotfiles is an extendable and configurable dotfile manager written in python.
It will configure your computer exactly the way that you want, and through the
configuration system, means that people can have their own personalized environment
by just editing configuration files, with no need to dive into the code to make it
just work.

For Windows support, please see [here](https://media1.giphy.com/media/26FPy3QZQqGtDcrja/giphy.gif)

## Features
- Automatically sets up your applications, libraries, and environment the
  way **YOU** want
- One-command installation
- Easy configuration via forking and editing of a configuration file
- Easy configuration options means that changes are simple and powerful
- Enables unlimited extensions and customization, with a great baseline installation

### Examples
- Downloads a bunch of useful command-line tools (GNU tools, wget, bash v4+, vim, node, etc.)

- [macOS only] Downloads a bunch of useful applications:
  - [Firefox](https://www.mozilla.org/en-US/firefox/)
  - [smcFanControl](https://www.eidac.de/)
  - [JetBrains Toolbox](https://www.jetbrains.com/toolbox/)
  - [vlc](https://www.videolan.org/vlc/index.html)
  - and everything else that I end up using on a day-to-day basis, though you can
    choose which applications you'd like to install

- Secures and locks down the system via proper firewalling
- Sets up proper dev environments (Python, Java, Ruby, Golang)
- Sets up proper git environment with a better [diff](https://github.com/so-fancy/diff-so-fancy)
- [macOS only] Adds iTerm 2 [shell integrations](https://www.iterm2.com/documentation-shell-integration.html)

## Supported Platforms
- macOS 10.12.x+ (High Sierra+)
- Ubuntu 16.04 LTS

## Installation
### [RECOMMENDED] Opinionated Bootstrap
The following one-liner will bootstrap the system to an opinionated
setup, in particular setting up [pyenv](https://github.com/pyenv/pyenv)
for you if you don't have it yet, and setting up a new laptop-wide global
python environment for day-to-day use.

**`Basically, if there's a completely new computer, run this:`**

```sh
curl -s https://raw.githubusercontent.com/JasonYao/pydotfiles/master/bin/bootstrap | bash -s {CONFIGURATION_REPO_GIT_LINK}
# e.g.
curl -s https://raw.githubusercontent.com/JasonYao/pydotfiles/master/bin/bootstrap | bash -s git@github.com:JasonYao/dotfiles.git
```

### Non-Opinionated Bootstrap
The following one-liner won't assume the python environment that you're
installing this to, and just install itself with `pip`.

**`Basically, if your computer already has the required python version/environments, run this:`**

```sh
curl -s https://raw.githubusercontent.com/JasonYao/pydotfiles/master/bin/bootstrap-base | bash -s {CONFIGURATION_REPO_GIT_LINK}
# e.g.
curl -s https://raw.githubusercontent.com/JasonYao/pydotfiles/master/bin/bootstrap-base | bash -s git@github.com:JasonYao/dotfiles.git
```

## Usage
- To toggle show/hiding of iTerm 2:
<kbd>⌘</kbd> + <kbd>↓</kbd>

- To update + upgrade the dotfiles:
```sh
dotfiles upgrade
```

- To uninstall the dotfiles:
```sh
dotfiles uninstall
```

## License
This repo is licensed under the terms of the
GNU GPL v3, of which a copy may be found [here](LICENSE).