---
title: blkid
---

## blkid
command-line utility to locate/print block device attributes.

## Usage

```
blkid -s UUID -o value /dev/sdb
```

* `-o format`
* `-s tag`
    * show only the tags that match tag
    * It is possible to specify multiple `-s` options
    * If no tag is specified, then all tokens are shown for all (specified) devices.
    * In order to just refresh the cache without showing any tokens, use `-s` none with no other options
* `-S byte`

## Reference
* [blkid(8) - Linux man page](https://linux.die.net/man/8/blkid)
