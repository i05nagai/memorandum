---
title: Amethyst
---

## Amethyst
tile型window manager.


## Install

```
brew cask install amethyst
```

`System Preference -> Privacy & Security -> Accecibility`からAmethystを追加する。
初回起動時に、Accecibility画面まで誘導すされるので、起動すれば良い。

## Usage
layoutの種類

* tall
    * 今focusのあるwindowをdescktopの左半分に表示
    * 残りを右半分に等間隔に並べる
* wide
    * 今focustのあるwindowをdescktopの上半分に表示
    * 残りを下半分に等間隔に並べる
* fullscreen
    * 今focustのあるwindowを最大サイズで利用する
* column
    * 今のdescktopにあるwindowを全て縦に並べる


* Cycle layout forward

* layout Fullscreen
    * ctrl+option+D
* layout tall
    * ctrl+option+A
* layout wide
    * ctrl+option+S

## Reference
* [ianyh/Amethyst: Automatic tiling window manager for macOS à la xmonad.](https://github.com/ianyh/Amethyst)
