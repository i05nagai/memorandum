---
title: synclinet
---

## synclinet
touchpad configuration.

## CLI

```
synclient <option> [KEY=VALUE]
```

* `-l --list`
    * show current configuration

## Configuration
Reboot is needed if you update configuraiton.
Or you can update `synclient KEY=VALUE` command.
One of the following directories

* `/etc/X11/xorg.conf.d/`
* `/usr/share/X11/xorg.conf.d/`
    * `70-synaptics.conf`
    * ubuntu

```xf86conf
# 
Section "InputClass"
    Identifier "touchpad"
    Driver "synaptics"
    MatchIsTouchpad "on"
        Option "TapButton1" "1"
        Option "TapButton2" "3"
        Option "TapButton3" "2"
        Option "VertEdgeScroll" "on"
        Option "VertTwoFingerScroll" "on"
        Option "HorizEdgeScroll" "on"
        Option "HorizTwoFingerScroll" "on"
        Option "CircularScrolling" "on"
        Option "CircScrollTrigger" "2"
        Option "EmulateTwoFingerMinZ" "40"
        Option "EmulateTwoFingerMinW" "8"
        Option "CoastingSpeed" "0"
        Option "FingerLow" "30"
        Option "FingerHigh" "50"
        Option "MaxTapTime" "125"

        Option "PalmDetect" "1"
        Option "PalmMinWidth" "8"
        Option "PalmMinZ" "100"
EndSection
```

Palm detection


* `PalmDetect=1`
    * enable 1
    * disable 0
* `PalmMinWidth=8`
    * palmと判定する最小のwidth
* `PalmMinZ=100`
    * touchと判定する最小のpressure
    * `evtest`のz value(pressure)の値を参考にする


* `VertScrollDelta=-73`
    * minusだとswipeとscrollの方向が逆になる
    * minusがOSXと同じscrolling
* `HorizScrollDelta=-73`
    * minusだとswipeとscrollの方向が逆になる
    * minusがOSXと同じscrolling
* `HorizTwoFingerScroll=1`
    * two finger swipe
    * 1 enable, 0 disable

## Usage
Show current configuration

```
synclient -l
```

Change two finger swipe direction as OSX

```
synclient VertScrollDelta=-73
synclient HorizScrollDelta=-73
```

Enabled 2 finger swipe

```
synclient HorizTwoFingerScroll=1
```

Example of Palm detection

```
synclient PalmDetect=1
synclient PalmMinWidth=5
synclient PalmMinZ=10
```

Use 3 finger as middle clik

```
synclient TapButton2=3 TapButton3=2
```

## Reference
* [Touchpad Synaptics \- ArchWiki](https://wiki.archlinux.org/index.php/Touchpad_Synaptics)
* [Looking for a way to improve synaptic/touchpad palm detection \- Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/28306/looking-for-a-way-to-improve-synaptic-touchpad-palm-detection)
