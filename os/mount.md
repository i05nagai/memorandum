---
title: mount
---

## mount

## CLI

```
mount --type type -o option1,option2 device dir
```

* `-t`, `--type`
    * supportしているfilesystem `/lib/modules/$(uname -r)/kernel/fs`と`/proc/filesystems`を見る
    * most common are ext2, ext3, ext4, xfs, btrfs, vfat, sysfs, proc, nfs and cifs
* `-o`, `--options`
    * comma separated list
    * mount typeに依存しないoptionとmount typeごとの利用可能なoptionがある


### 9p
* [https://www.kernel.org/doc/Documentation/filesystems/9p.txt](https://www.kernel.org/doc/Documentation/filesystems/9p.txt)


```
mount -t 9p -o trans=virtio,version=9p2000.L hostshare /tmp/host_files
```

## Reference
* [mount(8) - Linux manual page](http://man7.org/linux/man-pages/man8/mount.8.html)
