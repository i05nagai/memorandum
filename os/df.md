---
title: df
---

## df

## Usage


```
df -h
```

* `-h, --human-readable`
    * 単位がつく
* `-H, --si`
    * 1024ではなく1000での単位をだす
* `-a, --all`
    * include pseudo, duplicate, inaccessible file systems
* `-B, --block-size=SIZE`
    * scale sizes by SIZE before printing them '-BM' prints sizes in units of 1,048,576 bytes; see SIZE format below
* `-i, --inodes`
    * list inode information instead of block usage
* `-k`
    * like --block-size=1K
* `-l, --local`
    * limit listing to local file systems
      --no-sync         do not invoke sync before getting usage info (default)
      --output[=FIELD_LIST]  use the output format defined by FIELD_LIST, or print all fields if FIELD_LIST is omitted.
* `-P, --portability`
    * use the POSIX output format
* `--sync`
    * invoke sync before getting usage info
* `--total`
    * elide all entries insignificant to available space, and produce a grand total
* `-t, --type=TYPE`
    * limit listing to file systems of type TYPE
* `-T, --print-type`
    * print file system type
* `-x, --exclude-type=TYPE`
    * limit listing to file systems not of type TYPE
* `-v`
    * (ignored)


## Reference
* [12 Useful "df" Commands to Check Disk Space in Linux](https://www.tecmint.com/how-to-check-disk-space-in-linux/)
