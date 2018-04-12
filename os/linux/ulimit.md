---
title: ulimit
---

## ulimit
User limits - limit the use of system-wide resources.

```
ulimit [-acdfHlmnpsStuv] [limit]
```

* `-S`
    * Change and report the soft limit associated with a resource. 
* `-H`
    * Change and report the hard limit associated with a resource. 
* `-a`
    * All current limits are reported. 
* `-c`
    * The maximum size of core files created. 
* `-d`
    * The maximum size of a process's data segment. 
* `-f`
    * The maximum size of files created by the shell(default option) 
* `-l`
    * The maximum size that can be locked into memory. 
* `-m`
    * The maximum resident set size. 
* `-n`
    * The maximum number of open file descriptors.
* `-p`
    * The pipe buffer size. 
* `-s`
    * The maximum stack size. 
* `-t`
    * The maximum amount of cpu time in seconds. 
* `-u`
    * The maximum number of processes available to a single user. 
* `-v`
    * The maximum amount of virtual memory available to the process. 

## Usage
全てのlimitを表示

```
ulimit -a
```


## Configuration
`/etc/security/limits.conf`

```
root soft nofile 65536
root hard nofile 65536
* soft nofile 65536
* hard nofile 65536
```

## Reference
* [Linux Howtos: Tips and Tricks -> ulimit and sysctl](http://www.linuxhowtos.org/Tips%20and%20Tricks/ulimit.htm)
* [ulimit Man Page - Bash - SS64.com](https://ss64.com/bash/ulimit.html)
