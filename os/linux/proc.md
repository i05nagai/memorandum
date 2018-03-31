---
title: proc
---

## proc

`/proc/`以下にpidごとにprocessの情報が作成されている。


* `fd/`
    * fd以下にはfile descriptorの情報
    * 利用されているfile descriptor

```sh
# get pid
for i in `ps aux | grep grep_text | awk '{print $2}'`
do
    ls -la /proc/$i/fd
done
```

### /proc/meminfo
* [Interpreting /proc/meminfo and free output for Red Hat Enterprise Linux 5, 6 and 7 - Red Hat Customer Portal](https://access.redhat.com/solutions/406773)
* [E.2.18. /proc/meminfo - Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s2-proc-meminfo)
* [What is the difference between Buffers and Cached columns in /proc/meminfo output? - Quora](https://www.quora.com/What-is-the-difference-between-Buffers-and-Cached-columns-in-proc-meminfo-output)

rawdisk は harddiskの意味

* Cached
    * size of pagecache
* SwapCached
    * 
* buffer
    * in-memory block I/O buffer
    * file data以外のcache
    * kernel 2.4からraw disk


memory usage

```
$ cat /proc/meminfo

MemTotal:        8120568 kB
MemFree:         2298932 kB
Cached:          1907240 kB
SwapCached:            0 kB
SwapTotal:      15859708 kB
SwapFree:       15859708 kB
```

## Reference
