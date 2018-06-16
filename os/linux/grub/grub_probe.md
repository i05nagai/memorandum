---
title: grub-probe
---

## grub-probe


## CLI

```
grub-probe [OPTION...] [OPTION]... [PATH|DEVICE]
```

* -d, --device
    * given argument is a system device, not a path
*  -m, --device-map=FILE
    * use FILE as the device map
    * [default=/boot/grub/device.map]
* -t, --target=TARGET
    * print TARGET
    * available targets: abstraction, arc_hints,
    * baremetal_hints, bios_hints, compatibility_hint,
    * cryptodisk_uuid, device, disk, drive, efi_hints,
    * fs, fs_label, fs_uuid, gpt_parttype,
    * hints_string, ieee1275_hints, msdos_parttype,
    * partmap, zero_check [default=fs]
* -v, --verbose
* print verbose messages.
* -?, --help
    * give this help list
* --usage
    * give a short usage message
* -V, --version
    * print program version


## Usage
Device

```
sudo grub-probe -t device /boot/grub
```

UUID

```
sudo grub-probe -t fs_uuid /boot/grub
```


## Reference
