---
title: rbenv
---

## rbenv
rubyの仮想環境の作り方。

## Install
`rbenv-install`などの一部commandは`rbenv-build`pluginが必要。
rbenvが使えるようになった後、以下を実行すればOK

```
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
```

### For OSX,

```
brew install rbenv
```

`~/.bash_profile`か`~/.zprofile`に以下を記載する。

```shell
# renv
if which rbenv > /dev/null 2>&1; then
    export PATH="$HOME/.rbenv/bin:$PATH"
    eval "$(rbenv init -)"
fi
```

gemの環境を分ける場合は、

```
brew install rbenv-gemset
```

### For Linux,

```
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
cd ~/.rbenv && src/configure && make -C src
```

Then add following lines to shell env

```
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
```

## Usage
pyenv と同じ。

rubyのinstall可能なlistを表示

```
# show ruby versions which can be available to install
rbenv install -l
```

rubyのversionをinstall

```
# install ruby specified [version]
rbenv install [version]
```

current directory以下のrubyのversionを指定

```
rbenv local [version]
```

rbenvの環境でrubyの実行

```
rbenv exec ruby --version
```

利用可能なrubyのversion

```
rbenv versions
```

```
rbenv rehash
```

```
# set ruby [version] globally
rbenv global [version] 
```

localに環境を分ける場合は、`rbenv local`を使う。

### rbenv-gemset

```
# show list of gemset
rbenv gemset list
# show active gemset
rbenv gemset active
# [gemset]を有効にする
rbenv gemset init [gemset]
```

## Reference
* [ちょっとgem試したい時にrbenv-gemset使う - Qiita](http://qiita.com/chinmo@github/items/6f531b4dd748c1cf5497)
