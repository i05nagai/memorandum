---
title: Lenovo Y520
---

## Lenovo Y520


## Hardware information
* [Legion Y520 \| Intel Core i7 Gaming Laptop \| Lenovo US](https://www3.lenovo.com/us/en/laptops/ideapad/lenovo-legion-y-series-laptops/Legion-Y520/p/88GMY500808)
* memory: 15GB
* Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
* GeForce GTX 1050 Ti


Host bridge: Intel Corporation Device 5910 (rev 05)
PCI bridge: Intel Corporation Sky Lake PCIe Controller (x16) (rev 05)
VGA compatible controller: Intel Corporation Device 591b (rev 04)
USB controller: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller (rev 31)
Signal processing controller: Intel Corporation Sunrise Point-H Thermal subsystem (rev 31)
Communication controller: Intel Corporation Sunrise Point-H CSME HECI #1 (rev 31)
SATA controller: Intel Corporation Sunrise Point-H SATA Controller [AHCI mode] (rev 31)
PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #2 (rev f1)
PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #3 (rev f1)
PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #4 (rev f1)
PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #9 (rev f1)
ISA bridge: Intel Corporation Sunrise Point-H LPC Controller (rev 31)
Memory controller: Intel Corporation Sunrise Point-H PMC (rev 31)
Audio device: Intel Corporation Device a171 (rev 31)
SMBus: Intel Corporation Sunrise Point-H SMBus (rev 31)
3D controller: NVIDIA Corporation Device 1c8c (rev a1)
SD Host controller: O2 Micro, Inc. Device 8621 (rev 01)
Network controller: Intel Corporation Device 24fd (rev 78)
Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 10)
Non-Volatile memory controller: Device 1c5c:1527

* `<F2>`
    * bios menu
* `<F12>`
    * boot menu


## Software
* vulkan run time libraries
  * [至急パソコンに詳しい方に伺いたいのですが先ほどインストールした覚えの... - Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11156757246)
  * GeForce のdriverなのでけさない
* lenovoのtouchpad driverをいれる
  * 

Uninstallしたもの

Control Panel -> Program and Features

* Windows One Drive
* Macafee Web Advisor
* Lenovo entertainment Hub
  * gameとかのplatformj
  * [Lenovo Entertainment Hub](https://support.lenovo.com/nz/en/downloads/ds501007)
* Lenovo Nerve Center for windows10
  * [Lenovo Nerve Center for Windows 10 (64-bit) - Desktop](https://support.lenovo.com/nz/en/downloads/ds111752)
  * [Lenovo Nerve Center - Lenovo Community](https://forums.lenovo.com/t5/Gaming-Desktops-Knowledge-Base/Lenovo-Nerve-Center/ta-p/3588946)
  * CPU, GPU, RAM, HDDの概要を表示
  * 不要

## ubuntu
SSDが認識されない

* BIOSのmennuからConfiguration -> SATA Controller ModeをAHCIに変更する
    * Intel RST Premium(RAID)


### Use Function key
See below examples.

1. Check your function key events

```
# run acpi then type <Fn>+<FuncKey>
$ acpi_listen
# output is like this
button/volumeup VOLUP 00000080 00000000 K
button/volumedown VOLDN 00000080 00000000 K
```

2. Create acpi events configuration file in `/etc/acpi/events/`


3. Create a script to handle the key event in `/etc/acpi`


4. Restart `acpid`

```
sudo systemctl restart acpid
```


#### Example. Change brightness with function key
Create `/etc/acpi/lenovo-keyboard-backlight.sh` with

```sh
#!/bin/sh

# this directory is a symlink on my machine:
KEYS_DIR="/sys/class/backlight/intel_backlight"

test -d $KEYS_DIR || exit 0

MIN=0
MAX=$(cat $KEYS_DIR/max_brightness)
VAL=$(cat $KEYS_DIR/brightness)

if [ "$1" = down ]; then
  VAL=$((VAL-500))
else
  VAL=$((VAL+500))
fi

if [ "$VAL" -lt $MIN ]; then
  VAL=$MIN
elif [ "$VAL" -gt $MAX ]; then
  VAL=$MAX
fi

echo $VAL > $KEYS_DIR/brightness
```

Create `/etc/acpi/events/lenovo-keyboard-backlight-up`

```
event=video/brightnessup BRTUP 00000086
action=/etc/acpi/lenovo-keyboard-backlight.sh up
```

Create `/etc/acpi/events/lenovo-keyboard-backlight-down`

```
event=video/brightnessdown BRTDN 00000087
action=/etc/acpi/lenovo-keyboard-backlight.sh down
```

Then restart `acpid`

```
sudo systemctl restart acpid
```

## Reference
* [Windows8.1 システムイメージバックアップから復元されないもの: 家庭部PC科](http://fanblogs.jp/honeycome/archive/45/0)
