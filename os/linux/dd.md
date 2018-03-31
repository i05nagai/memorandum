---
title: dd
---

## dd
`dd` can be used for tasks such as backing up the boot sector of a hard drive, and obtaining a fixed amount of random data.

```
$ dd if=/dev/zero of=500MBfile bs=1M count=500 oflag=dsync
```

## Reference
* [dd (Unix) - Wikipedia](https://en.wikipedia.org/wiki/Dd_(Unix))
* [Linux Performance Measurements using vmstat - Thomas-Krenn-Wiki](https://www.thomas-krenn.com/en/wiki/Linux_Performance_Measurements_using_vmstat)
