---
title: lspci
---

## lspci
list all PCI devices.

## CLI

```
lspci [<switches>]
```

Basic display modes:

* -mm
    * Produce machine-readable output (single -m for an obsolete format)
* -t
    * Show bus tree

Display options:

* -v
    * Be verbose (-vv for very verbose)
* -k
    * Show kernel drivers handling each device
* -x
    * Show hex-dump of the standard part of the config space
* -xxx
    * Show hex-dump of the whole config space (dangerous; root only)
* -xxxx
    * Show hex-dump of the 4096-byte extended config space (root only)
* -b
    * Bus-centric view (addresses and IRQ's as seen by the bus)
* -D
    * Always show domain numbers

Resolving of device ID's to names:

* -n
    * Show numeric ID's
* -nn
    * Show both textual and numeric ID's (names & numbers)
* -q
    * Query the PCI ID database for unknown ID's via DNS
* -qq
    * As above, but re-query locally cached entries
* -Q
    * Query the PCI ID database for all ID's via DNS

Selection of devices:
* `-s [[[[<domain>]:]<bus>]:][<slot>][.[<func>]]`
    * Show only devices in selected slots
* `-d [<vendor>]:[<device>][:<class>]`
    * Show only devices with specified ID's

Other options:

* `-i <file>`
    * Use specified ID database instead of /usr/share/misc/pci.ids.gz
* `-p <file>`
    * Look up kernel modules in a given file instead of default modules.pcimap
* -M
    * Enable bus mapping mode (dangerous; root only)

PCI access options:

* `-A <method>`
    * Use the specified PCI access method (see -A help for a list)
* `-O <par>=<val>`
    * Set PCI access parameter (see -O help for a list)
* -G
    * Enable PCI access debugging
* `-H <mode>`
    * Use direct hardware access (<mode> = 1 or 2)
* `-F <file>`
    * Read PCI configuration dump from a given file

## Usage

## Reference
* [lspci\(8\): all PCI devices \- Linux man page](https://linux.die.net/man/8/lspci)
