---
title: lsof
---

## lsof
* `ls+of`
    * ls
    * of = open file


## CLI

```
lsof
```

- `+d s`
- `-d s`
- `+D D`
    - causes lsof to search for all open instances of directory `D` and all the files and directories it contains to its complete depth.
- `-D D`
- `-i D`
- `-u s`
    * selects the listing of files for the user whose login names or user ID numbers are in the comma-separated set s - e.g., `abe`, or `548,root`.  (There should be no spaces in the set.)
- `-U`
    *  selects the listing of UNIX domain socket files.

## Usage

開いているfileで削除されている

```
lsof | grep deleted
```

```
lsof -c <cmd>
```

```
lsof -p 1107
```

```
lsof -i udp
lsof -i
```

```
lsof | grep /var*  | numfmt --field=8 --to=iec | head
```

## Format
Columns

* COMMAND
    * the command or process name
* PID
    * shows process id
* USER
    * the owner of process
* FD
    * file descriptor like memory, txt etc.
* DEVICE
    * the device major and minor id
* SIZE/OFF
    * the size
* NODE
* NAME
    * the name of the opened file

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
* [lsof\(8\) \- Linux manual page](http://man7.org/linux/man-pages/man8/lsof.8.html)
