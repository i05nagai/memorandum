---
title: zsh
---

## zsh

## keybind

### Change keybind
以下で`ctrl-h`のkeybindを変更できる。
`kill-word`の所は、自分で関数を用意するか、デフォルトのzshの関数を指定する。

```zsh
bindkey "^H" kill-word
```

### check current keybind
shellで`bindkey`を実行すると、現在割り当てられているkeybindが出力される。

### Useless keybind
* [zshのキーバインドで余っているキーを探す - mollifier delta blog](http://mollifier.hatenablog.com/entry/20081213/1229148947)

```
"^J" accept-line
"^V" quoted-insert
"^Y" yank
"^@" set-mark-command
"^O" accept-line-and-down-history
"^S" history-incremental-search-forward
"^^"
"^]"
```

## completion
`echo $fpath`で設定されているディレクトリにリンクをはる。
もしくは、下記をzshrcの上部にかく。
上部というのは、どこかのタイミングで補完用のファイルが読み込まれるが、そのタイミングより上であれば良い。


### zhs-completions

## plugins
* [GitHub - zsh-users/zsh-autosuggestions: Fish-like autosuggestions for zsh](https://github.com/zsh-users/zsh-autosuggestions)
    * It suggests commands as you type, based on command history.
* [GitHub - zsh-users/zsh-syntax-highlighting: Fish shell like syntax highlighting for Zsh.](https://github.com/zsh-users/zsh-syntax-highlighting)
    * This package provides syntax highlighing for the shell zsh
* [GitHub - zsh-users/antigen: A plugin manager for zsh, inspired by oh-my-zsh and vundle.](https://github.com/zsh-users/antigen)
    * plugin manager

#### reference
* [zsh-users/zsh-completions: Additional completion definitions for Zsh.](https://github.com/zsh-users/zsh-completions)
* [まだ oh-my-zsh で消耗してるの？ - Qiita](http://qiita.com/b4b4r07/items/875235f6122a6d779306)
