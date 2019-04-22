---
title: groupmems
---

## groupmems


## CLI

```
groupmems [options] [action]
```

Options:

* `-g, --group groupname`
    * change groupname instead of the user's group (root only)
* `-R, --root CHROOT_DIR`
    * directory to chroot into

Actions

* `-a, --add username`
    * add username to the members of the group
* `-d, --delete username`
    * remove username from the members of the group
* `-h, --help`
    * display this help message and exit
* `-p, --purge`
    * purge all members from the group
* `-l, --list`
    * list the members of the group

## Usage
Get list of group members.

```
groupmems -g <gorupname> --list
```

## Configuration

## Reference
