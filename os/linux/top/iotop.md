---
title: iotop
---

## iotop
iotop - simple top-like I/O monitor.

## Install
For ubuntu,

```
apt-get intsall iotop
```

## CLI

```
iotop <option>
```

* `-o, --only`
    * Only show processes or threads actually doing I/O, instead of showing all processes or threads. This can be dynamically toggled by pressing o.
* `-b, --batch`
    * Turn on non-interactive mode. Useful for logging I/O usage over time.
* `-n NUM, --iter=NUM`
    * Set the number of iterations before quitting (never quit by default). This is most useful in non-interactive mode.
* `-d SEC, --delay=SEC`
    * Set the delay between iterations in seconds (1 second by default). Accepts non-integer values such as 1.1 seconds.
* `-p PID, --pid=PID`
    * A list of processes/threads to monitor (all by default).
* `-u USER, --user=USER`
    * A list of users to monitor (all by default)
* `-P, --processes`
    * Only show processes. Normally iotop shows all threads.
* `-a, --accumulated`
    * Show accumulated I/O instead of bandwidth. In this mode, iotop shows the amount of I/O processes have done since iotop started.
* `-k, --kilobytes`
    * Use kilobytes instead of a human friendly unit. This mode is useful when scripting the batch mode of iotop. Instead of choosing the most appropriate unit iotop will display all sizes in kilobytes.
* `-t, --time`
    * Add a timestamp on each line (implies --batch). Each line will be prefixed by the current time.
* `-q, --quiet`
    * suppress some lines of header (implies --batch). This option can be specified up to three times to remove header lines.
* `-q`
    column names are only printed on the first iteration,
* `-qq`
    * column names are never printed,
* `-qqq`
    the I/O summary is never printed.

## Usage

## Tips

### In docker container
you need to execute `docker run` with

```
docker run --rm -it --net=host --pid=host docker-image /bin/bash
```

## Reference
[iotop(1): simple top-like I/O monitor - Linux man page](https://linux.die.net/man/1/iotop)
