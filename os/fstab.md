---
title: fstab
---

## fstab
`/etc/fstab` file, the device automatically mounts again when the instance restarts.

## Configuration

```
[Device] [Mount Point] [File System Type] [Options] [Dump] [Pass]
# UUID=[UUID_VALUE] /mnt/disks/[MNT_DIR] ext4 discard,defaults,nofail 0 2
```

* `<device>`
    * The device/partition (by /dev location or UUID) that contain a file system.
        * `UUID=[VALUE]`
        * `/dev/sdb`
* `<mount point>`
    * The directory on your root file system (aka mount point) from which it will be possible to access the content of the device/partition (note: swap has no mount point). Mount points should not have spaces in the names.
    * defaultは `/media`
* `<file system type>`
    * Type of file system 
        * https://help.ubuntu.com/community/LinuxFilesystemsExplained
    * auto
    * vfat
        * used for FAT partitions.
    * ntfs, ntfs-3g
        * used for ntfs partitions.
    * ext4, ext3, ext2, jfs, reiserfs, etc.
    * udf,iso9660
        * for CD/DVD.
    * swap
* `<options>`
    * Mount options of access to the device/partition (see the man page for mount).
    * sync/async 
        * All I/O to the file system should be done (a)synchronously.
    * auto 
        * The filesystem can be mounted automatically (at bootup, or when mount is passed the -a option). This is really unnecessary as this is the default action of mount -a anyway.
    * noauto 
        * The filesystem will NOT be automatically mounted at startup, or when mount passed -a. You must explicitly mount the filesystem.
    * dev/nodev 
        * Interpret/Do not interpret character or block special devices on the file system.
    * exec / noexec 
        * Permit/Prevent the execution of binaries from the filesystem.
    * suid/nosuid 
        * Permit/Block the operation of suid, and sgid bits.
    * ro 
        * Mount read-only.
    * rw
        * Mount read-write.
    * user 
        * Permit any user to mount the filesystem. This automatically implies noexec, nosuid,nodev unless overridden.
    * nouser 
        * Only permit root to mount the filesystem. This is also a default setting.
    * defaults 
        * Use default settings. Equivalent to rw, suid, dev, exec, auto, nouser, async.
    * _netdev 
        * this is a network device, mount it after bringing up the network. Only valid with fstype nfs.
* `<dump>`
    * Enable or disable backing up of the device/partition (the command dump). This field is usually set to 0, which disables it.
* `<pass num>`
    * Controls the order in which fsck checks the device/partition for errors at boot time. The root device should be 1. Other partitions should be 2, or 0 to disable checking.
    * 実用上は、root partitionを1にして、それ以外は2
    * 0: do not check.
    * 1: check this partition first.
    * 2: check this partition(s) next


device id (UUID)の確認方法

```
sudo blkid
```

## Reference
* [Fstab - Community Help Wiki](https://help.ubuntu.com/community/Fstab)
