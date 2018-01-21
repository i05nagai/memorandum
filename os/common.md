---
title: Common
---

## Common


## /etc/fstab
* [/etc/fstabについて その1 - Linux初心者の基礎知識](http://www.linux-beginner.com/linux_kihon64.html)


## CPU information
```
cat /proc/cpuinfo
```


## GPU information
vendorごとに違う。
nvidiaの場合は

```
nvidia-smi
```

か以下のdirectoryにGPUの情報が含まれている場合がある。

```
cat /proc/drivers/nvidia/gpus/.../information
```


## directory name convention
* [linux - Meaning of directories on Unix and Unix like systems - Server Fault](https://serverfault.com/questions/24523/meaning-of-directories-on-unix-and-unix-like-systems)

* /bin
    * Binaries.
* /boot
    * Files required for booting.
* /dev
    * Device files.
* /etc
    * Etcctera. The name is inherited from the earliest Unixes, which is when it became the spot to put config-files.
* /home
    * Where Home directories are kept.
* /lib
    * Where code libraries are kept.
* /media
    * A more modern directory, but where removable media gets mounted.
* /mnt
    * Where temporary file-systems are mounted.
* /opt
    * Where opttional add-on software is installed. This is discrete from /usr/local/ for reasons I'll get to later.
* /run 
    * Where runtime variable data is kept.
* /sbin
    * Where super-binaries are stores. These usually only work with root.
* /usr
    * Another directory inherited from the Unixes of old, it stands for "user". This directory should be sharable between hosts, and can be NFS mounted to multiple hosts safely. It can be mounted read-only safely. Also as per Debian Wiki, /usr is UNIX System Resources.
* /var
    * Another directory inherited from the Unixes of old, it stands for "variable". This is where system data that varies may be stored. Such things as spool and cache directories may be located here. If a program needs to write to the local file-system and isn't serving that data to someone directly, it'll go here.
* /include
    * contains #include files, i.e. header files (e.g., stdio.h).
* /srv
    * Stands for "serve". This directory is intended for static files that are served out. /srv/http would be for static websites, /srv/ftp for an FTP server.
* /tmp
    * stands for temporary.
* /root
    * means root user.
* /proc
    * stands for processes


* `/opt vs /usr/local`
    * Use /usr/local for things that would normally go into /usr, or are overriding things that are already in /usr. Use /opt for things that install all in one directory, or are otherwise special.

## Performance analysis

uptime

```
uptime
 12:17:50 up  6:12,  1 user,  load average: 0.58, 0.85, 0.94
```

* The current time
* how long the system has been running
* how many users are currently logged on,
* the system load averages for the past 1 minute
* the system load averages for the past 5 minute
* the system load averages for the past 15 minute

```
dmesg | tail
```
vmstat 1
mpstat -P ALL 1
pidstat 1
iostat -xz 1
free -m
sar -n DEV 1
sar -n TCP,ETCP 1
top

## useradd
Error: `useradd: cannot create directory /opt/...`.
You need to create directory before execution `useradd`.


## LANG environment variables
* [Linuxのローカライゼーション系LANG変数：langについて](https://eng-entrance.com/linux-localization-lang)

## Reference
* [Linux Performance Analysis in 60,000 Milliseconds – Netflix TechBlog – Medium](https://medium.com/netflix-techblog/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)
