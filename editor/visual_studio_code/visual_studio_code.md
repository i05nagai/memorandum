---
title: Visual Studio Code
---

## Visual Studio Code

## Install

```
brew cask install visual-studio-code
```

For ubuntu 16.04,

```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get update
sudo apt-get install code # or code-insiders
```

## Settings
* Windows
    * `%APPDATA%\Code\User\settings.json`
* Mac
    * `$HOME/Library/Application Support/Code/User/settings.json`
* Linux
    * `$HOME/.config/Code/User/settings.json`

## Go
Debug

* go fileを開く
* Debug -> Open configuration
* `launch.json`が作成される
* `"env": {"GOPATH": "${env:GOPATH}"}`を追加する
* `${env:Name}`


## Keymarp

On linux,

* `Ctlr+Alt+-`
    * navigate back
* `Ctlr+Shift+-`
    * navigate fort

## Javascript
Install `tsd` file

```
npm install tsd -g
```

```
tsd install node --save
```

jsconfig

```
{
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs"
  }
}
```

## Reference

