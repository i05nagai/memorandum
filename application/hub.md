# hub


## Install

* OSX

```shell
brew install --HEAD hub
```

`hub`コマンドを`git`コマンドのかわりに使用する場合は、以下のコマンドでaliasをふる。
`.bash_profile`や`.zprofile`などに記載する。

```shell
eval "$(hub alias -s)"
```

## Usage

### hub clone

### hub pull-request

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

