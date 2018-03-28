---
title: vmstat
---

## vmstat
virtual memory statistics.
vmstat は libkstat ライブラリを使用している。
`/usr/src/cmd/stat/vmstat/vmstat.c`


## Usage

```
vmstat [options] [delay [count]
```

* `delay`
    * every inteval secondsでreportを更新
* `count`
    * countに到達するまでreportを行う

options

* `-s, --stats`
    * memory statictics
    * event counter statistics
* `-d, --disk`
    * disk statistics
* `-f, --forks`
    * forks数
* `-m, --slabs`
    * slabinfo
* `-a, --active`
    * active/inactive memory
* `-n, --one-header`
    * do not redisplay header
* `-D, --disk-sum`
    * summarize disk statistics
* `-p, --partition <dev>` 
    * partition specific statistics
    * 仮想メモリのpaging
* `-S, --unit <char>`
    * define display unit
* `-w, --wide`
    * wide output
* `-t, --timestamp`
    * show timestamp


## Outpout format
```
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa
 0  0   3996 167868  57108 1369788    0    0     1     2    0    0  3  1 97  0
 0  0   3996 167860  57108 1369920    0    0     0     0  274  604  2  0 98  0
 0  0   3996 167860  57108 1369928    0    0     0     0  196  481  1  0 98  0
 0  0   3996 167860  57116 1369908    0    0     0    12  164  414  1  1 97  1
 0  0   3996 167860  57116 1369892    0    0     0     0  168  320  0  0 100  0
 0  0   3996 167860  57116 1369884    0    0     0     0  142  398  1  0 99  0
 0  0   3996 167860  57116 1369880    0    0     0     0  175  450  1  1 98  0
```

* r
    * run queue
    * CPUの割当をまっているkernel thread
    * 10 以上又は CPU 数の倍以上の場合は CPU への負荷が高い状態
    * mpstat, prstat
* b
    * i/oで待たされているkernel thread
    * I/O 待ちをしているスレッドの数が多い場合は I/O の対象となっているディスクを分散したり、ストレージを増強する等
    * iostat, fsstat, DTraceなどを使う
* w
    * swap out されたkernel threadの数
    * swapが発生している場合はmemoryを追加
* swpd/swap
    * 利用可能なswap領域のsize KB
    * disk上のswap領域とmemory上のsawp領域をあわせたもの
    * g




## Reference
* [vmstat - Wikipedia](https://en.wikipedia.org/wiki/Vmstat)
* [Use vmstat to Monitor System Performance](https://linode.com/docs/uptime/monitoring/use-vmstat-to-monitor-system-performance/)
* [vmstat コマンドの読み方 | Oracle やっぱり Sun がスキ！ Blog](https://blogs.oracle.com/yappri/vmstat)
