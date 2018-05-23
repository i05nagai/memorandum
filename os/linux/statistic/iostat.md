---
title: iostat
---

## iostat

## Install
For ubuntu,

```
apt-get install sysstat -y
```

## CLI
```
iostat [ -c ] [ -d ] [ -N ] [ -n ] [ -h ] [ -k | -m ] [ -t ] [ -V ] [ -x ] [ -z ] [ device [...] | ALL ] [ -p [ device [,...] | ALL ] ] [ interval [ count ] ]
```

* `-c`
    * Display the CPU utilization report.
* `-d`
    * Display the device utilization report.
* `-h`
    * Make the NFS report displayed by option -n easier to read by a human.
* `-k`
    * Display statistics in kilobytes per second instead of blocks per second. Data displayed are valid only with kernels 2.4 and later.
* `-m`
    * Display statistics in megabytes per second instead of blocks or kilobytes per second. Data displayed are valid only with kernels 2.4 and later.
* `-N`
    * Display the registered device mapper names for any device mapper devices. Useful for viewing LVM2 statistics.
* `-n`
    * Display the network filesystem (NFS) report. This option works only with kernel 2.6.17 and later.
* `-p [ { device [,...] | ALL } ]`
    * The -p option displays statistics for block devices and all their partitions that are used by the system. If a device name is entered on the command line, then statistics for it and all its partitions are displayed. Last, the ALL keyword indicates that statistics have to be displayed for all the block devices and partitions defined by the system, including those that have never been used. Note that this option works only with post 2.5 kernels.
* `-t`
    * Print the time for each report displayed. The timestamp format may depend on the value of the S_TIME_FORMAT environment variable (see below).
* `-V`
    * Print version number then exit.
* `-x`
    * Display extended statistics.
    * This option works with post 2.5 kernels since it needs /proc/diskstats file or a mounted sysfs to get the statistics.
    * This option may also work with older kernels (e.g. 2.4) only if extended statistics are available in /proc/partitions (the kernel needs to be patched for that).
* `-z`
    * Tell iostat to omit output for any devices for which there was no activity during the sample period.
* `--human`
    * human readable output

## Usage
Report every 2 sec.

```
iostat -d 2
```

Display 6 report every 2 sec

```
iostat -d 2 6
```

Display extended statistics

```
iostat -x
```

Device sda and all it's partitions

```
iostat -p sda 2 6
```

```
iostat --human
```


## Output
Display the device utilization report.

```
$ iostat -d
Linux 4.9.87-linuxkit-aufs  	05/18/18 	_x86_64_	(2 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.79        19.67        19.69    1404683    1405876
scd0              0.04         2.53         0.00     180766          0
scd1              0.00         0.00         0.00         68          0
```

Display the CPU utilization report.

```
$ iostat -c
Linux 4.9.87-linuxkit-aufs  	05/18/18 	_x86_64_	(2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.08    0.00    0.10    0.02    0.00   99.80
```

Display the extended statistics

```
$ iostat -x
Linux 4.9.87-linuxkit-aufs 	05/18/18 	_x86_64_	(2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.07    0.00    0.10    0.02    0.00   99.80

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              0.50    0.29     19.57     19.59     0.00     0.28   0.64  48.65    3.29   90.79   0.03    39.43    67.39   0.54   0.04
scd0             0.04    0.00      2.52      0.00     0.00     0.00   0.00   0.00    0.58    0.00   0.00    63.65     0.00   0.45   0.00
scd1             0.00    0.00      0.00      0.00     0.00     0.00   0.00   0.00    0.00    0.00   0.00     9.71     0.00   0.00   0.00
```

* wrqm/s
* rrqm/s
    * The number of read requests merged per second that were queued to the device.
* wrqm
* r_await
    * The average time (in milliseconds) for I/O requests issued to the device to be served.
    * This includes the time spent by the requests in queue and the time spent servicing them.
* w_await
* aqu-sz
* rareq-sz
* wareq-sz
* svctm
    * Do not trust this field any more.
    * The average service time (in milliseconds) for I/O requests that were issued to the device. 
* util
    * Percentage of CPU time during which I/O requests were issued to the device (bandwidth utilization for the device)
    * Device saturation occurs when this value is close to 100%.

## Reference
* [How to Install and Use iostat on Ubuntu 16.04 LTS](https://www.howtoforge.com/tutorial/how-to-install-and-use-iostat-on-ubuntu-1604/)
* [iostat(1) - Linux man page](https://linux.die.net/man/1/iostat)
