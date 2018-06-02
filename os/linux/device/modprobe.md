---
title: modprobe
---

## modprobe
program to add and remove modules from the Linux Kernel.

## CLI

```
modprobe [ -v ] [ -V ] [ -C config-file ] [ -n ] [ -i ] [ -q ] [ -b ] [ -o modulename ] [ modulename ] [ module parameters... ]
modprobe [ -r ] [ -v ] [ -n ] [ -i ] [ modulename... ]
modprobe [ -l ] [ -t dirname ] [ wildcard ]
modprobe [ -c ]
modprobe [ --dump-modversions ]
```

Management Options:

* -a, --all
    * Consider every non-argument to be a module name to be inserted or removed (-r)
* -r, --remove
    * Remove modules instead of inserting
    * --remove-dependencies
        * Also remove modules depending on it
* -R, --resolve-alias
    * Only lookup and print alias and exit
* --first-time
    * Fail if module already inserted or removed
* -i, --ignore-install
    * Ignore install commands
* -i, --ignore-remove
    * Ignore remove commands
* -b, --use-blacklist
    * Apply blacklist to resolved alias.
* -f, --force
    * Force module insertion or removal.
    * implies
        * --force-modversions
        * --force-vermagic
* --force-modversion
    * Ignore module's version
* --force-vermagic
    * Ignore module's version magic

Query Options:

* -D, --show-depends
    * Only print module dependencies and exit
* -c, --showconfig
    * Print out known configuration and exit
* -c, --show-config
    * Same as --showconfig
        * --show-modversions
            * Dump module symbol version and exit
        * --dump-modversions
            * Same as --show-modversions

General Options:

* -n, --dry-run
    * Do not execute operations, just print out
* -n, --show
    * Same as --dry-run
* -C, --config=FILE
    * Use FILE instead of default search paths
* -d, --dirname=DIR
    * Use DIR as filesystem root for /lib/modules
* -S, --set-version=VERSION
    * Use VERSION instead of `uname -r`
* -s, --syslog
    * print to syslog, not stderr
* -q, --quiet
    * disable messages
* -v, --verbose
    * enables more messages

## Usage

## Configuration
* `/etc/modprobe.d/`
* `/etc/modprobe.conf`

## Reference
* [modprobe\(8\): add/remove modules from Kernel \- Linux man page](https://linux.die.net/man/8/modprobe)
