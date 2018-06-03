---
title: modinfo
---

## modinfo
program to show information about a Linux Kernel module.

## CLI

```
modinfo [options] filename [args]
```

* -a, --author
    * Print only 'author'
* -d, --description
    * Print only 'description'
* -l, --license
    * Print only 'license'
* -p, --parameters
    * Print only 'parm'
* -n, --filename
    * Print only 'filename'
* -0, --null
    * Use \0 instead of \n
* -F, --field=FIELD
    * Print only provided FIELD
* -k, --set-version=VERSION
    * Use VERSION instead of `uname -r`
* -b, --basedir=DIR
    * Use DIR as filesystem root for /lib/modules

## Usage

## Reference
* [modinfo\(8\): show info about Kernel module \- Linux man page](https://linux.die.net/man/8/modinfo)
