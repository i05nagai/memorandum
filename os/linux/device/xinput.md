---
title: xinput
---

## xinput


## CLI

```
xinput list
```

device idの設定値を監視する

```
xinput --watch-props <device-id>
```

## Configuration


## touchpad
* [SynapticsTouchpad \- Community Help Wiki](https://help.ubuntu.com/community/SynapticsTouchpad)

synclinetで設定の変更ができる

```
synclient
```

## Tips

### Stop scrolling after my fingers don't touch
[touchpad \- Stop Scrolling on fingers up \- Ask Ubuntu](https://askubuntu.com/questions/640444/stop-scrolling-on-fingers-up)

```
xinput --set-prop --type=float "<your device>" "Synaptics Coasting Speed" 0 0
```

* Option "CoastingSpeed" "float"
    * Coasting threshold scrolling speed. 0 disables coasting. Property: "Synaptics Coasting Speed"

```
xinput list
```

## Reference
* [X/Config/Input \- Ubuntu Wiki](https://wiki.ubuntu.com/X/Config/Input)
