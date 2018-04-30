---
title: last
---

## last
`/var/log/wtmp` のLogを見る。
To find out when a particular user last logged in to the Linux or Unix server.

```
last
last [userNameHere]
last [tty]
last [options] [userNameHere]
last [options] [<username>...] [<tty>...]
```

* `-<number>`
    * how many lines to show
* -a, --hostlast
    * display hostnames in the last column
* -d, --dns
    * translate the IP number back into a hostname
* -f, --file <file>
    * use a specific file instead of /var/log/wtmp
* -F, --fulltimes
    * print full login and logout times and dates
* -i, --ip
    * display IP numbers in numbers-and-dots notation
* -n, --limit <number>
    * how many lines to show
* -R, --nohostname
    * don't display the hostname field
* -s, --since <time>
    * display the lines since the specified time
* -t, --until <time>
    * display the lines until the specified time
* -p, --present <time>
    * display who were present at the specified time
* -w, --fullnames
    * display full user and domain names
* -x, --system
    * display system shutdown entries and run level changes
* --time-format <format>
    * show timestamps in the specified <format>: notime|short|full|iso

## Usage

rebootの時間

```
last reboot
```

## Reference
* [Linux / Unix: last Command Examples - nixCraft](https://www.cyberciti.biz/faq/linux-unix-last-command-examples/)
