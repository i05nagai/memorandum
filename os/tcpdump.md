---
title: tcpdump
---

## tcpdump


* `-n`
    * addressを名前に変換しない
    * host, portなど
* `-C file_size`
    * `file_size`より大きければfileを分けて保存
    * `1M` 単位で指定
* `-i`
    * listenするinterface
    * `eth0`など
* `-w file`
    * stdoutではなくfileに書き込む

## Reference
* [Manpage of TCPDUMP](https://www.tcpdump.org/tcpdump_man.html)
