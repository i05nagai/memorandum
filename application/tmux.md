---
title: tmux
---
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

* `w`
    * windowの選択


### rename
sessionのリネームは`prefix $`

windowのリネームは`prefix ,`

### OSXでclipboardにcopy

```
brew install reattach-to-user-namespace
```

tmux.confに以下を追加。

```tmux
# Use vim keybindings in copy mode
setw -g mode-keys vi

# Setup 'v' to begin selection as in Vim
bind-key -t vi-copy v begin-selection
bind-key -t vi-copy y copy-pipe "reattach-to-user-namespace pbcopy"

# Update default binding of `Enter` to also use copy-pipe
unbind -t vi-copy Enter
bind-key -t vi-copy Enter copy-pipe "reattach-to-user-namespace pbcopy"
```

## CLI
現在の設定値を表示

```
tmux show-options -g
```

## Configurations
* [tmux の status line の設定方法 - Qiita](https://qiita.com/nojima/items/9bc576c922da3604a72b)


## Reference
