---
title: cpp/ubuntu
---

## Ubuntu

## Tips

### build with pthread
Ubuntuでpthreadを使う場合は`libpthread`をlinkする必要がある。

```shell
gcc hoge.c -lpthread
```
