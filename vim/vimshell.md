# vimshell

## 文字コードを指定して実行
```vim
$exe --encoding=utf-8 ruby hoge.rb
```

## 設定ファイル
~/vimshrcに設定を記述できる。
以下がファイルの場所の初期値。
```vim
g:vimshell_vimshrc_path=expand('~/.vim/vimshrc')
```

## vimshellを開くときのウィンドウサイズの変更
`:VimShellPop`が実行されるとき、`g:vimshell_popup_command`のコマンドが実行される。
`g:vimshell_popup_command`が空白の場合は、`split`が`g:vimshell_popup_height`で実行される。
`g:vimshell_popup_height`の初期値は30

## vimshellでのcommit
vimshell上で`git commit`を実行した時に、commit messsage編集画面に行くが、commit message編集画面を閉じるときは、`:w`かつ`:bd`で保存しバッファを閉じる。

## インタープリタを起動する場合
iexeを使う。
```zsh
iexe python
```

