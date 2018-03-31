---
title: vmstat
---

## vmstat
virtual memory statistics.
vmstat は libkstat ライブラリを使用している。
`/usr/src/cmd/stat/vmstat/vmstat.c`

For alpine linux,

```
apk upate
apk add --update procps
```

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


```
vmstat 2 -S m
```


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
* free
    * memory size KB
    * 小さくなったらメモリが圧迫されている状態
* re
    * page reclaim
    * free listにいれられた後pageが参照され復帰したもの
* mf
    * minor fault
* pi
    * page in されたmemory size KB
* po
    * page outされたmemory size KB
* fr
    * freeされたmemory size KB
* de
    * deficit
    * 多くのmemory requestがある場合にvirtual memoryが確保するbuffer size
* sr
    * page out scanerによってscanされたmemory pageの数
    * page scanが多発している場合はmemory不足
* disk
    * number of I/O
    * iostat
* in
    * number of interupt
    * Use mpstat, intrstat
* sy (faults)
    * number of system call
* cs
    * the number of CPU context switches
    * 多い場合はreduce threads/
* CPU
    * us
        * CPU時間の割合 in user mode
    * sy (CPU)
        * CPU時間の割合(e.g. kernel service/system call) in system mode
    * id
        * CPU idle
        * CPUが使用されていなかった時間の割合
    * wa
        * Time spent waiting for IO. Prior to Linux 2.5.41, included in idle.
    * st
        * Time stolen from a virtual machine. Prior to Linux 2.6.11, unknown.
* epi
    * executable page-ins
    * execution file/libraryがpage in した量(KB)
        * VVMEXEC flagがtrueのもの
* epo
    * executable page-out
    * execution file/libraryがpage out した量(KB)
        * VVMEXEC flagがtrueのもの
* epf
    * executable page-out
    * execution file/libraryがpage out した量(KB)
        * VVMEXEC flagがtrueのもの
* IO
    * bo
        * Blocks sent to a block device (blocks/s)
    * bi
        * Blocks received from a block device (blocks/s).



## Reference
* [vmstat - Wikipedia](https://en.wikipedia.org/wiki/Vmstat)
* [Use vmstat to Monitor System Performance](https://linode.com/docs/uptime/monitoring/use-vmstat-to-monitor-system-performance/)
* [vmstat コマンドの読み方 | Oracle やっぱり Sun がスキ！ Blog](https://blogs.oracle.com/yappri/vmstat)
* [Linux Performance Measurements using vmstat - Thomas-Krenn-Wiki](https://www.thomas-krenn.com/en/wiki/Linux_Performance_Measurements_using_vmstat)
