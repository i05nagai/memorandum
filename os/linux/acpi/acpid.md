---
title: acpid
---

## acpid
acpid2 is a flexible and extensible daemon for delivering ACPI events. When an event occurs, it executes programs to handle the event. 

## Events
[ACPI modules \- ArchWiki](https://wiki.archlinux.org/index.php/ACPI_modules)

## CLI

```
acpid [OPTIONS]
```

* -c, --confdir
    * Set the configuration directory.
* -C, --clientmax
    * Set the limit on non-root socket connections.
* -d, --debug
    * Increase debugging level (implies -f).
* -e, --eventfile
    * Use the specified file for events.
* -f, --foreground
    * Run in the foreground.
* -l, --logevents
    * Log all event activity.
* -g, --socketgroup
    * Set the group on the socket file.
* -m, --socketmode
    * Set the permissions on the socket file.
* -s, --socketfile
    * Use the specified socket file.
* -S, --nosocket
    * Do not listen on a UNIX socket (overrides -s).
* -p, --pidfile
    * Use the specified PID file.
* -L, --lockfile
    * Use the specified lockfile to stop processing.
* -n, --netlink
    * Force netlink/input layer mode. (overrides -e)
* -r, --dropaction
    * Define the pseudo-action to drop an event.
* -t, --tpmutefix
    * Fixup for ThinkPad mute-repeat behaviour.

## Usage

## Configuration
* `/etc/acpi/handler.sh`
    * predefined actions
* `/etc/acpi/events/anything`


```sh
button/sleep)
    case "$2" in
        SLPB) echo -n mem >/sys/power/state ;;
         *)    logger "ACPI action undefined: $2" ;;
    esac
    ;;
```

By default, all ACPI events are passed through the `/etc/acpi/handler.sh` script.
This is due to the ruleset outlined in `/etc/acpi/events/anything`:

```
# Pass all events to our one handler script
event=.*
action=/etc/acpi/handler.sh %e
```

* `event=button sleep.*`
    * specify the events which you want to handle
* `action=/path/to/scripts`
    * `%e` is arguments
    * which you want to handle


## Reference
* [acpid \- ArchWiki](https://wiki.archlinux.org/index.php/acpid)
