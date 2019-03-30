---
title: chunkwm
---

## chunkwm
Tiled window manager for OSX.

## Install
- [Using chunkwm as a window manager \| Sunlight Media LLC\.](https://sunlightmedia.org/using-chunkwm-as-a-window-manager/)

```
# clone tap
brew tap crisidev/homebrew-chunkwm
# install latest stable version
brew install chunkwm
# install from git repo
brew install --HEAD chunkwm
```


```
# for shortcut key
brew install skhd
```

```
brew services start chunkwm
brew services start skhd
```

## Configuration
* You need to locate `.chunkwm` shell script to `$HOME` with executable permissions
* [chunkwm/chunkwmrc at master · koekeishiya/chunkwm](https://github.com/koekeishiya/chunkwm/blob/master/examples/chunkwmrc#L2)
    * sample configuration
* [skhd/skhdrc at master · koekeishiya/skhd](https://github.com/koekeishiya/skhd/blob/master/examples/skhdrc)


## Error
- [Running chunkwm with brew or manually does nothing · Issue \#361 · koekeishiya/chunkwm](https://github.com/koekeishiya/chunkwm/issues/361)

## Reference
* [ chunkwm \- tiling wm](https://koekeishiya.github.io/chunkwm/docs.html)
