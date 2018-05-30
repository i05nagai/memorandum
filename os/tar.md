---
title: tar
---

## tar
manipulate tape archives

## BSD
* [tar(1)](https://www.freebsd.org/cgi/man.cgi?tar(1))

```
tar [bundled-flags <args>] [<file> | <pattern> ...]
tar {-c} [options] [files | directories]
tar {-r | -u} -f archive-file [options] [files | directories]
tar {-t | -x} [options] [patterns]
```

* `-c`
* `-r`
* `-t`
* `-x`

Create `file.tar.gz` from files or directory

```
tar -czf file.tar.gz source.c source.h
tar -czf file.tar.gz directory
```

Extract `file.tar.gz`

```
tar -zxvf tar-archive-name.tar.gz
```


## GNU

```
tar -zcvf tar-archive-name.tar.gz source-folder-name
`

## Reference
* [Create and extract a .tar.gz archive using command line — Brett Popoleo Designs](https://popoleodesigns.com/create-and-extract-a-tar-gz-archive-using-command-line/)
