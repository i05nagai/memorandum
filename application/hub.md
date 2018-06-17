---
title: hub
---

## hub

## Install
For OSX

```
brew install --HEAD hub
```

`hub`コマンドを`git`コマンドのかわりに使用する場合は、以下のコマンドでaliasをふる。
`.bash_profile`や`.zprofile`などに記載する。

```
eval "$(hub alias -s)"
```

For Linux, use single compiled binary
[Releases · github/hub](https://github.com/github/hub/releases)

```
curl -L -O https://github.com/github/hub/releases/download/v2.4.0/hub-linux-amd64-2.4.0.tgz
tar xfv hub-linux-amd64-2.4.0.tgz
cd hub-linux-amd64-2.4.0
./install 
```

## Usage

```
hub clone
```

```
hub pull-request
```

Reviewをつける

```
hub pull-request -r PERSON1,PERSON2
```

`https://github.com/OWNER/REPO/pull/123` pull requestのbranchをchecokut

```
hub pr checkout 123
```

### hub browse
githubをブラウザで開いてリポジトリを参照するコマンド

### hub compare
githubをブラウザで開いてdiffを参照するコマンド


# Reference
* [github/hub: hub helps you win at git.](https://github.com/github/hub)
* [GitHubユーザーのためのhubコマンド - Qiita](http://qiita.com/yaotti/items/a4a7f3f9a38d7d3415e3)
* [GitHub githubに「pull request」を送れたりするhubコマンドを導入 by Mac | Coffee Breakにプログラミング備忘録](http://to-developer.com/blog/?p=1372)

