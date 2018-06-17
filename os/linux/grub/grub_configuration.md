---
title: GRUB configuration
---

## GRUB configuration


## Configuration

### /etc/default/grub
* must be edited by Administrator/root
* After making changes, you need to run

```
sudo update-grub
```

* `GRUB_DEFAULT=`
* `GRUB_SAVEDEFAULT=`
* `GRUB_HIDDEN_TIMEOUT=0`
* `GRUB_HIDDEN_TIMEOUT_QUIET`
* `GRUB_TIMEOUT`
* `GRUB_DISTRIBUTOR=lsb_release -i -s 2> /dev/null || echo Debian`
* `GRUB_CMDLINE_LINUX`
* `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"`
* `#GRUB_TERMINAL=console`
* `#GRUB_DISABLE_LINUX_UUID="true"`
* `#GRUB_GFXMODE=640x480`
* `#GRUB_DISABLE_LINUX_RECOVERY=true`
* `GRUB_INIT_TUNE="480 440 1"`
* `GRUB_BACKGROUND`
* `GRUB_DISABLE_OS_PROBER`

## Reference
