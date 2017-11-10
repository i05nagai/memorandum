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


## Reference
