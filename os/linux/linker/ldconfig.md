---
title: ldconfig
---

## ldconfig
ldconfig - configure dynamic linker run-time bindings.

## CLI

```
ldconfig [-nNvXV] [-f conf] [-C cache] [-r root] directory...
ldconfig -l [-v] library...
ldconfig -p
```

## Usage

## Configuration
* `/etc/ld.so.conf.d/`
* `/etc/ld.so.conf`
    * File containing a list of directories, one per line, in which to search for libraries.
* `/etc/ld.so.cache`
    * File containing an ordered list of libraries found in the directories specified in /etc/ld.so.conf, as well as those found in the trusted directories.

## Reference
* [ldconfig\(8\) \- Linux manual page](http://man7.org/linux/man-pages/man8/ldconfig.8.html)
