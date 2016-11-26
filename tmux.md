# tmux

## Tips

### paneの移動

```tmux
:join-pane -t :動かしたい先のwindowの番号 (activeなpaneがwindowの番号のwindowに加わる)
:join-pane -s :もって来たいpaneがあるwindowの番号 (windowの番号のpaneがactiveなpaneに加わる)
```

* [tmuxのjoin-paneからpaneの指定方法を学ぶ (ターミナルマルチプレクサ Advent Calendar 2日目) - kozo2のはてなダイアリー](http://d.hatena.ne.jp/kozo2/20111202/1322827858)

## prefix
tmux用のkeybindに行こうするためのコマンド。
デフォルトだと、`ctrl-a`

## keybind
keybindの一覧はprefixのあとに`:list-keys`でOK。
もしくは、`prefix ?`

### rename
sessionのリネームは`prefix $`

windowのリネームは`prefix ,`
