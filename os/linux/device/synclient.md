---
title: synclinet
---

## synclinet

## CLI

```
synclient <option> [KEY=VALUE]
```

* `-l --list`
    * 現在の設定値を表示

## Configuration
* `/etc/X11/xorg.conf.d/`
* `/etc/X11/Xsession.d/`
    * ubuntu

```

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
現在の設定を表示

```
synclient -l
```

OSXと同じswipeの方向にする

```
synclient VertScrollDelta=-73
synclient HorizScrollDelta=-73
```

2 finger swipeをenable

```
synclient HorizTwoFingerScroll=1
```

Palm detectionの例

```
synclient PalmMinWidth=5
synclient PalmMinZ=10
```

## Reference
* [Touchpad Synaptics \- ArchWiki](https://wiki.archlinux.org/index.php/Touchpad_Synaptics)
