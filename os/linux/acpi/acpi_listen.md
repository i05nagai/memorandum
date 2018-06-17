---
title: acpi_listen
---

## acpi_listen


## CLI

```
acpi_listen [OPTIONS]
  -c, --count       Set the maximum number of events.
  -s, --socketfile  Use the specified socket file.
  -t, --time        Listen for the specified time (in seconds).
  -v, --version     Print version information.
  -h, --help        Print this message.
```

## Usage
After executing the following command, press `Fn+<Fnkey>`.
If your function key is available, you will see the following outputs.

```
$ acpi_listen
video/brightnessdown BRTDN 00000087 00000000
video/brightnessup BRTUP 00000086 00000000
```

acpi sends the above envents to `/etc/acpi/handler.sh` as arguments

* `$1`
    * video/brightnessdown
* `$2`
    * BRTDN
* `$3`
    * 00000087
* `$4`
    * 00000000

## Configuration

## Reference
