---
title: Visual Studio Code
---

## Visual Studio Code

## Install

```
brew cask install visual-studio-code
```

## Settings
* Windows
    * %APPDATA%\Code\User\settings.json
* Mac
    * $HOME/Library/Application Support/Code/User/settings.json
* Linux
    * $HOME/.config/Code/User/settings.json

## Go
Debug

* go fileを開く
* Debug -> Open configuration
* `launch.json`が作成される
* `"env": {"GOPATH": "${env:GOPATH}"}`を追加する
* `${env:Name}`


## Reference

