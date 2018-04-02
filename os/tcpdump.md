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
* `-t`
    * human readable output

## Usage

Find traffic by ip
1.2.3.4とのtraficをcapture

```
tcpdump host 1.2.3.4
```

Seeing more of the packet with hex output
Hexでみる。

```
tcpdump -nnvXSs 0 -c1 icmp
```

Filtering by source and destination

```
tcpdump src 2.3.4.5 
tcpdump dst 2.3.4.5 
```

Finding packets by network

```
tcpdump net 1.2.3.0/24
```

Show traffic related to a specific port

```
tcpdump port 3389 
tcpdump src port 1025
```

show traffic of one protocol

```
tcpdump icmp
```

show only ip6 traffic

```
tcpdump ip6
```

find traffic using port ranges

```
tcpdump portrange 21-23
```


## Reference
* [Manpage of TCPDUMP](https://www.tcpdump.org/tcpdump_man.html)
* [A tcpdump Tutorial and Primer with Examples](https://danielmiessler.com/study/tcpdump/)
