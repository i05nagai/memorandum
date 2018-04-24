---
title: fzf
---

## fzf
選択的インターフェースの一つ。

## Install

### Linux

```sh
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

### OSX

```sh
brew install fzf

# Install shell extensions if you want
/usr/local/opt/fzf/install
```

## CLI

```
fzf [options]
```

* `-e --exact`
* `--algo=[TYPE]`
    * `v1` or `v2`
    * default `v2`
* `-i`
    * case insensitive match
* `+i`
    * case sensitive match

Interfaces

* `-m, --multi`
    * multi select with tab/shift tab
* --no-mouse
    * Disable mouse
* --bind=KEYBINDS
    * Custom key bindings. Refer to the man page.
* --cycle
    * Enable cyclic scroll
* --no-hscroll
    * Disable horizontal scroll
* --hscroll-off=COL
    * Number of screen columns to keep to the right of the highlighted substring (default: 10)
* --filepath-word
    * Make word-wise movements respect path separators
* --jump-labels=CHARS
    * Label characters for jump and jump-accept

Layout

Scripting

* -q, --query=STR
    * Start the finder with the given query

## Usage
* [おい、peco もいいけど fzf 使えよ - Qiita](http://qiita.com/b4b4r07/items/9e1bbffb1be70b6ce033)

## Tips

### Scripts with fzf
* [Home · junegunn/fzf Wiki · GitHub](https://github.com/junegunn/fzf/wiki)

### Fuzzy completion
`FZF_COMPLETION_TRIGGER`に設定しているcharの後に`<TAB>`をうつと補完してくれるようになる。
何を補完するかはある程度contextを判定してくれる

* Files and directories
* process ID
* 

settings

```
# Use ~~ as the trigger sequence instead of the default **
export FZF_COMPLETION_TRIGGER='~~'

# Options to fzf command
export FZF_COMPLETION_OPTS='+c -x'
```


## Reference
* [GitHub - junegunn/fzf: A command-line fuzzy finder written in Go](https://github.com/junegunn/fzf)

