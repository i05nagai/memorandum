---
title: mount
---

## mount
If you want to mount when the computer starts, use `/etc/fstab`

## CLI

```
mount --type type -o option1,option2 <device> <mount_dir>
```

```
sudo mount -o discard,defaults /dev/[DEVICE_ID] /mnt/disks/[MNT_DIR]
```

* `-t`, `--type`
    * supportしているfilesystem `/lib/modules/$(uname -r)/kernel/fs`と`/proc/filesystems`を見る
    * most common are ext2, ext3, ext4, xfs, btrfs, vfat, sysfs, proc, nfs and cifs
* `-o, --options opts`
    * comma separated list
    * filesystem independe options
        * `defaults`
            * rw, suid, dev, exec, auto, nouser, and async
        * `rw`
            * mount the fs read-write
        * `suid`
            * allow set-user-identifier or set-group-identifier bits to take effect
        * `dev`
            * interpret character or block special devices on the fs
        * `exec`
            * permit execution of the binary
        * `auto`
            * can be mounted with the `-a` option
        * `nouser`
            * forbid on ordinary user to mount the fs.
            * default
        * `async`
            * all I/O to the fs should be done asynchronously
        * `ro`
            * mount the fs read-only
        * `nofail`
            * Do not report errors for this device if it does not exist
            * useful when you mount with `/etc/fstab`
    * filesystem dependent options
        * ext4
            * `discard`/`nodiscard`
                * control whether ext4 should issue discard/TRIM commands to the underlying block device when blocks are freed.
                * this is useful for SSD devices and sparse/thinly-provisioned storage
                * off by default

#### 9p

* [https://www.kernel.org/doc/Documentation/filesystems/9p.txt](https://www.kernel.org/doc/Documentation/filesystems/9p.txt)


```
mount -t 9p -o trans=virtio,version=9p2000.L hostshare /tmp/host_files
```

#### nvme
* [NVMe  Hetzner DokuWiki](https://wiki.hetzner.de/index.php/NVMe/en)
* Non-Volatile Memory Express
    * NVMe SSDs are addressed differently than SATA drives. 
    * The first NVMe-SSD is called /dev/nvme0n1 instead of /dev/sda. The n after nvme0 stands for Namespac
    * /dev/nvme(Controller number)n(Namespace)p(Partition)


#### Check

```
df -aTh
```

## Reference
* [mount(8) - Linux manual page](http://man7.org/linux/man-pages/man8/mount.8.html)
* http://manpages.ubuntu.com/manpages/xenial/man8/mount.8.html
