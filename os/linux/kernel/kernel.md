---
title: kernel
---

## kernel


* RawDisk
    * [Raw disk definition by The Linux Information Project](http://www.linfo.org/raw_disk.html)
    * The term raw disk refers to the **accessing of the data on a hard disk drive (HDD) or other disk storage device** or media directly at the individual byte level instead of through its filesystem as is usually done.


## /etc/sysctl.conf
* [How Netflix Tunes EC2 Instances for Performance](https://www.slideshare.net/brendangregg/how-netflix-tunes-ec2-instances-for-performance)

```conf
net.core.somaxconn = 1024
net.core.netdev_max_backlog = 5000
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_wmem = 4096 12582912 16777216
net.ipv4.tcp_rmem = 4096 12582912 16777216
net.ipv4.tcp_max_syn_backlog = 8096
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
net.ipv4.ip_local_port_range = 10240 65535
```

## Reference
* [The Linux Information Project (LINFO) Home Page](http://www.linfo.org/index.html)
* [understand-html](https://www.kernel.org/doc/gorman/html/understand/index.html)
