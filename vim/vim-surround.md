---
title: Vim Surround
---

## Vim Surround

## commands
下記コマンド+対象(obects)を指定

コマンドというよりoperator?

* ds
    * delete surroundings
* di
    * delete inner
* cs
    * change surroundings
* ci
    * change inner
* yss
    * you surround sentence
    * 先頭のspaceを除いて、一行を囲む
* ySS
    * you surround sentence
    * 囲み文字、text、囲み文字と3行使って囲む
    * textは、indentされる

## targets
text-objectsを指定する。

* w
    * word
* W
    * WORD
* s
    * sentence
* p
    * paragraph
* b
    * `()`
* B
    * brace
    * `{ }`
* t
    * html tag
* -
    * `<?php ?>`

## Tips

### 複数行をまとめて囲む
normalコマンドを使うと複数行にたいして、normal コマンドが使える。
複数行を選択して `:normal yss"`とすれば良い。

## Reference
* [surround.vimの使い方 | Memo on the Web](http://motw.mods.jp/Vim/surround.html)

