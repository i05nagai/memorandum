---
title: zplug
---

## zplug
zshのplugin managerのうちの一つ。
もう一つ有名なのは、antigenっぽい。
antigenとの比較は以下の記事を見れば良い。

* [おい、Antigen もいいけど zplug 使えよ - Qiita](http://qiita.com/b4b4r07/items/cd326cd31e01955b788b)


## Install

```sh
curl -fLo ~/.zplug/zplug --create-dirs git.io/zplug
```

### OSX

OSXの場合は`brew`で入る。

```sh
brew install zplug
```

実行後に以下のように指示がでるので、指示に従って、`ZPLUG_HOME=/usr/local/opt/zplug`を定義しておく。

```sh
In order to use zplug, please add the following to your .zshrc:
export ZPLUG_HOME=/usr/local/opt/zplug
source $ZPLUG_HOME/init.zsh
```

