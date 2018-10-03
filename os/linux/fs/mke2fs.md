---
title: mke2fs
---

## mke2fs
create an ext2/ext3/ext4 filesystem.


## Usage
```
sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/[DEVICE_ID]
```

* `-m reserved-blocks-percentage`
    * Specify the percentage of the filesystem blocks reserved for the super-user
    * the default percentage is 5%
* `-F`
    * Force mke2fs to create a filesystem, even if the specified device is not a partition on a block special device, or if other parameters do not make sense.
    * In order to force mke2fs to create a filesystem even if the filesystem appears to be in use or is mounted (a truly dangerous thing to do), this option must be specified twice.
* `-E extended-options`
    * options are commaseparated
    * `mmp_update_interval=interval`
    * `stride=stride-size`
    * `stripe_width=stripe-width`
    * `offset=offset`
    * `resize=max-online-resize`
    * `lazy_itable_init[= <0 to disable, 1 to enable>]`
        * if enabled and the `uninit_bg` feature is enabled, the inode table is not fully initalized by this command
        * this speed up filesystem initialization noticeably, but it requires the kernel to finish initializing the filesystem in the bg when the fs is first mounted
        * default 1 to enable lazy inode table zeroing
    * `lazy_journal_init[= <0 to disable, 1 to enable>]`
        * if enabled, the journal inode will not be fully zeroed out by this command
        * this speed up fs initialization noticeably, but carries some small risk if the system crashes before the journal has been overwritten entirely one time
        * default 1 to enable lazy journal table zeroing
    * `discard`
        * attempt to discard blocks at mkfs time
            * discarding blocks initially is seful on SSD and sparse / thin-provisioned storage
        * 
        * this is set as default

## Reference

