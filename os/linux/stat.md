---
title: stat
---

## stat
file/filesystemの情報を取得
Displays the detailed status of a particular file or a file system.

## Usage

```
stat [OPTION]... FILE...
```

* `-L`
    * follow links

## Format

```
$ stat -L /proc/pid/fd/1
  File: ‘/proc/pid/fd/1’
  Size: 16234089553	Blocks: 31707288   IO Block: 4096   regular file
Device: ca01h/51713d	Inode: 533952      Links: 0
Access: (0664/-rw-rw-r--)  Uid: (  500/user-name)   Gid: (  500/user-name)
Access: 2017-07-07 06:50:37.041081360 +0000
Modify: 2018-03-19 07:47:20.585537714 +0000
Change: 2018-03-19 07:47:20.585537714 +0000
 Birth: -
```

## Reference
* [Linux stat command help and examples](https://www.computerhope.com/unix/stat.htm)
