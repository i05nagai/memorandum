---
title: lsblk
---

## lsblk
list block device.

```
$ lsblk -f
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda       8:0    0   200G  0 disk 
├─sda1    8:1    0 195.9G  0 part /mnt/stateful_partition
├─sda2    8:2    0    16M  0 part 
├─sda3    8:3    0     2G  0 part 
├─sda4    8:4    0    16M  0 part 
├─sda5    8:5    0     2G  0 part 
├─sda6    8:6    0   512B  0 part 
├─sda7    8:7    0   512B  0 part 
├─sda8    8:8    0    16M  0 part /usr/share/oem
├─sda9    8:9    0   512B  0 part 
├─sda10   8:10   0   512B  0 part 
├─sda11   8:11   0     8M  0 part 
└─sda12   8:12   0    32M  0 part 
sdb       8:16   0    10G  0 disk /home/kubernetes/containerized_mounter/rootfs/
```

```
$ lsblk -h
Available columns (for --output):
        NAME  device name
       KNAME  internal kernel device name
     MAJ:MIN  major:minor device number
      FSTYPE  filesystem type
  MOUNTPOINT  where the device is mounted
       LABEL  filesystem LABEL
        UUID  filesystem UUID
          RA  read-ahead of the device
          RO  read-only device
          RM  removable device
       MODEL  device identifier
        SIZE  size of the device
       STATE  state of the device
       OWNER  user name
       GROUP  group name
        MODE  device node permissions
   ALIGNMENT  alignment offset
      MIN-IO  minimum I/O size
      OPT-IO  optimal I/O size
     PHY-SEC  physical sector size
     LOG-SEC  logical sector size
        ROTA  rotational device
       SCHED  I/O scheduler name
     RQ-SIZE  request queue size
        TYPE  device type
    DISC-ALN  discard alignment offset
   DISC-GRAN  discard granularity
    DISC-MAX  discard max bytes
   DISC-ZERO  discard zeroes data
```

## Reference
* [lsblk(8) - Linux manual page](http://man7.org/linux/man-pages/man8/lsblk.8.html)
* [lsblk コマンドが便利 - Qiita](https://qiita.com/yutwatan/items/8ed9091b517d14951b07)
