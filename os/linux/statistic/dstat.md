---
title: dstat
---

## dstat
versatile tool for generating system resource statistics.

## Install
For ubuntu,

```
apt-get install dstat
```

## CLI

* `-c, --cpu`
    * enable cpu stats
* `-C 0,3,total`
    * include cpu0, cpu3 and total
* -d, --disk
    * enable disk stats
*  -D total,hda
    *  include hda and total
* -g, --page
    * enable page stats
* -i, --int
    * enable interrupt stats
*  -I 5,eth2
    *  include int5 and interrupt used by eth2
* -l, --load
    * enable load stats
* -m, --mem
    * enable memory stats
* -n, --net
    * enable network stats
*  -N eth1,total
    *  include eth1 and total
* -p, --proc
    * enable process stats
* -r, --io
    * enable io stats (I/O requests completed)
* -s, --swap
    * enable swap stats
*  -S swap1,total
    * include swap1 and total
* -t, --time
    * enable time/date output
* -T, --epoch
    * enable time counter (seconds since epoch)
* -y, --sys
    * enable system stats
* --aio
    * enable aio stats
* --fs, --filesystem
    * enable fs stats
* --ipc
    * enable ipc stats
* --lock
    * enable lock stats
* --raw
    * enable raw stats
* --socket
    * enable socket stats
* --tcp
    * enable tcp stats
* --udp
    * enable udp stats
* --unix
    * enable unix stats
* --vm
    * enable vm stats
* --vm-adv
    * enable advanced vm stats
* --zones
    * enable zoneinfo stats
* --list
    * list all available plugins
* --plugin
    * enable external plugin by name (see --list)
* -a, --all
    * equals -cdngy (default)
* -f, --full
    * automatically expand -C, -D, -I, -N and -S lists
* -v, --vmstat
    * equals -pmgdsc -D total
* --bits
    * force bits for values expressed in bytes
* --float
    * force float values on screen
* --integer
    * force integer values on screen
* --bw, --black-on-white
    * change colors for white background terminal
* --color
    * force colors
* --nocolor
    * disable colors
* --noheaders
    * disable repetitive headers
* --noupdate
    * disable intermediate updates
* --output file
    * write CSV output to file
* --profile
    * show profiling statistics when exiting dstat

## Usage

```
dstat -taf
```

```
dstat -ta --top-cpu
```

Show all

```
dstat -af
```

## output

```
$ dstat
You did not select any stats, using -cdngy by default.
--total-cpu-usage-- -dsk/total- -net/total- ---paging-- ---system--
usr sys idl wai stl| read  writ| recv  send|  in   out | int   csw
  0   0 100   0   0|  22k   20k|   0     0 |   0     0 |  57   118
```

## Reference
* [Dstat - A Resourceful Tool to Monitor Linux Server Performance in Real-Time](https://www.tecmint.com/dstat-monitor-linux-server-performance-process-memory-network/)
* [Linux負荷監視コマンドまとめ - Qiita](https://qiita.com/aosho235/items/c4d6995743dd1dac16e1)
* [dstatの便利なオプションまとめ - Qiita](https://qiita.com/harukasan/items/b18e484662943d834901)
* [How to Install and Use Dstat on Ubuntu-16.04](https://hostpresto.com/community/tutorials/how-to-install-and-use-dstat-on-ubuntu-16-04/)
