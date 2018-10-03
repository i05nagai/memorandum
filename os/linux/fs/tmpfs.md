---
title: tmpfs
---

## tmpfs
* in free commad
    * displayed as Shared, but it includes the count of shared memory
* in /proc/meminfo
    * displayed as Shmem, but it includes the count of shared memory
* df
    * the most reliable way to get the count
* du
    * the most reliable way to get the count

mount option for sizing

* size
    * If you oversize your tmpfs instances the machine will deadlock since the OOM handler will not be able to free that memory
* nr_blocks
* nr_inodes

## Tips

### the memory usage when memory allocated to tmpfs is not used
* https://superuser.com/questions/365814/does-memory-allocated-to-tmpfs-free-itself-when-needed-by-an-application

tmpfs grows and shrinks to accommodate the files it contains and is able to swap unneeded pages out to swap space.
If allocated the memory is not used by tmpfs, you can use the memory.

## Reference
* https://www.kernel.org/doc/Documentation/filesystems/tmpfs.txt
