---
title: zsh
---

## zsh

## keybind
* `^J`: ctrl+j
* `^[j` Esc+j

### word jump
単語の区切りを下記で指定できる。

```
export WORDCHARS='*?_-.[]~=/&;!#$%^(){}<>'
```

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


## Tips

### Customize completion

```zsh
```

```zsh
my_function() {
    # do something
}

_completion_function() {
    # 補完のための便利な関数_arguments
  _arguments \
    # -h, --helpを入力した時にはファイル一覧の候補を表示しない
    # 複数のオプションは{foo,bar}と書く
    # '[description]'でオプションの説明
    '(- *)'{-h,--help}'[show help]' \
    -r'[recursive]' \
    -f'[force]' \
    -rf'[recursive && force]' \
    # ファイル一覧を出す
    '*: :_files'
}

compdef _completion_function my_function
```

## prompt
* [13 Prompt Expansion (zsh)](http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html)

## Performance
* [zshの起動が遅いのでなんとかしたい - Qiita](https://qiita.com/vintersnow/items/7343b9bf60ea468a4180)
    * profileがとれる

### function lists defined in zsh
https://superuser.com/questions/681575/any-way-to-get-list-of-functions-defined-in-zsh-like-alias-command-for-aliases

```
print -l ${(ok)functions}
```

## Reference
* [ZSH Documentation (framed)](http://zsh.sourceforge.net/Doc/Release/index-frame.html)
* [zshでの自作関数と、それに対する補完関数を実装する - Qiita](http://qiita.com/petitviolet/items/b1e8b5139169dd530919)
* [zsh-users/zsh-completions: Additional completion definitions for Zsh.](https://github.com/zsh-users/zsh-completions)
* [まだ oh-my-zsh で消耗してるの？ - Qiita](http://qiita.com/b4b4r07/items/875235f6122a6d779306)
* [widgets can only be called when ZLE is active とは何だったのか - Qiita](https://qiita.com/udzura/items/3f120b5e4733fe85078d)
* [zle:bindkeys [ZshWiki]](http://zshwiki.org/home/zle/bindkeys)
* http://stevelosh.com/blog/2010/02/my-extravagant-zsh-prompt/
