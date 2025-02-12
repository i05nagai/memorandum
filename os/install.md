---
title: install
---

## install
The install command is commonly used in Makefiles or custom scripts to place binaries, libraries, or configuration files in the appropriate system directories.

```
install [OPTION]... SOURCE DEST
install [OPTION]... SOURCE... DIRECTORY 
install [OPTION]... -t DIRECTORY SOURCE
install [OPTION]... -d DIRECTORY
```

* `-m 755`
    * permission
* `-o UID`
* `-g GID`
* `-d`
    * 引数を全てdirectory名として解釈
    * directoryを作成する

必要なdirectoryを全て作成

```
install -d directory
```

```
install --verbose --directory --owner postgres --group postgres --mode 1777 /var/lib/postgresql
```

## Reference
* [How to Use the 'Install' Command in Linux](https://www.lifewire.com/install-linux-command-4091911)
