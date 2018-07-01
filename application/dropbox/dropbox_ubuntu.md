---
title: Dropbox Ubuntu
---

## Dropbox Ubuntu


## Install
* [Install \- Dropbox](https://www.dropbox.com/install)

For ubuntu 16.04,

```
cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
# or if you find error
cd ~ && wget -O --no-check-certificate - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
```

Installed to  `~/.dropbox-dist`.

## CLI

## Usage
Run dropbox daemon,

```
~/.dropbox-dist/dropboxd
```

## Configuration


## Reference
* [Dropbox \- Community Help Wiki](https://help.ubuntu.com/community/Dropbox)
