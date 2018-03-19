---
title: lsof
---

## lsof
* `ls+of`
    * ls
    * of = open file


```
lsof
```


開いているfileで削除されている

```
lsof | grep deleted
```

## Formato

* FD: Represents the file descriptor. Some of the values of FDs are,
    * cwd: Current Working Directory
    * txt: Text file
    * mem: Memory mapped file
    * mmap: Memory mapped device
    * NUMBER: Represent the actual file descriptor. The character after the number i.e ‘1u’, represents the mode in which the file is opened. r for read, w for write, u for read and write.
* TYPE: Specifies the type of the file. Some of the values of TYPEs are,
    * REG: Regular File
    * DIR: Directory
    * FIFO: First In First Out
    * CHR: Character special file

## Reference
* [15 Linux lsof Command Examples (Identify Open Files)](https://www.thegeekstuff.com/2012/08/lsof-command-examples/)
