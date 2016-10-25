# vim

## vimscripts

```vim
:echo expand("%")
"# => カレントファイルの名前を出力

:echo expand("%:p")
"# => カレントファイルのフルパスを出力

:echo expand("%:r")
"# => カレントファイルの名前、拡張子抜きを出力

:echo expand("%:e")
"# => カレントファイルの拡張子を出力
```

## vimのデフォルト機能

### 移動系
* ファイルを移動したり、`gg`で移動した場合にカーソルの位置を戻す。
```vim
元いた場所に戻る: <C-o>
元いた場所に進む: <C-i>
```
* 直前に開いていたバッファに戻る
```vim
<C-^>
```

## vimで整形
組み込みの整形コマンド`\tsp`と`\tab`

`>`はタブ。`-`は空白を表す。
```
one>>---two>>--->---three>--->---four>--five
six>>--->---seven>--eight>--nine>---ten
eleven>-twelve>--thirteen>--->--->---fourteen>---fifteen
```

`\tsp`での整形は、空白文字を境目に整形。
```
one    two    three    four     five
six    seven  eight    nine     ten
eleven twelve thirteen fourteen fifteen
```

`\tab`での整形は、タブ文字基準で整形。(TSV形式の整形）
```
one               two                        three                four   five
six                          seven   eight   nine       ten
eleven   twelve   thirteen                   fourteen   fifteen
```

## Alignで整形
### csvの整形
```vim
" 「:Align」コマンドの書式
:Align [{セパレータ1}] [{セパレータ2}] [{セパレータ3}] ..
```

```vim
:Align ,
```

### 範囲指定
```vim
" コマンド実行時に範囲指定する
:%:Align ,
:20,50:Align ,
```
or visual modeで指定してコマンド実行。

###「:AlignCtrl」コマンドで整形処理の条件を設定する
`:Align`コマンドの整形処理の結果をカスタマイズするには、`:AlignCtrl`コマンドを使用。
以下の順で使用する。
1. `:AlignCtrl`で整形の条件指定
2. `:Align`で整形。

フォーマットは以下。
```vim
" 「:AlignCtrl」コマンドの書式
:AlignCtrl {整形処理の条件} [{セパレータ1}] [{セパレータ2}] [{セパレータ3}] ....
```

AlignCtrlで以下の設定が可能。
* 各フィールドの左寄せ、右寄せ、センタリング。
* 配置指定の繰り返し、配置の整形条件のスキップ。
* セパレータの左寄せ、右寄せ、センタリング。
* セパレータとフィールド間の空白文字サイズを調整する。
* セパレータを順序固定で指定するか、ORで指定するか。
* 特定の行を整形対象外にする。特定の行を整形対象の行にする。
* 行頭の余白の扱い。維持する、削除する、先頭に合わせる。

## netrw
* ファイル作成
    * %


## vimfilerでファイルのbookmark
uniteが必須。
1. vimfilerで適当なディレクトリを開く
2. bookmarkに追加したディレクトリにカーソルを置き、`a`を押しアクションを起動後、`bookmark`を選択
3. `Please input bookmark file name`と聞かれる。カーソルに選択しているディレクトリがデフォルトのinput file/directoryになるので、EnterでOK
4. `Please input bookmark entry name`と聞かれる。bookmarkの別名を聞かれているので、わかりやすい名前をつける。
5. `:Unite bookmark`でbookmarkの一覧が表示できる。
    * bookmarkの削除は、`d`で行える。
	* bookmarkを開く場合は、`Enter`でUnite上でディレクトリが開かれる。
	* `t`や`e`でファイルを開いたりできる。

## コマンドモードで貼り付け
入力中に、`<Ctr-R>"`で貼り付けできる。

## vimでコードのformatを整える
Normalモードで`=`を押すと、カーソル行以下のフォーマットを整える。
Visual Modeで選択している場合は、選択範囲内を整える。

## バッファ
| command            | function                                         |
|--------------------|--------------------------------------------------|
| ls, buffers, files | 開いているバッファ一覧(バッファリスト)を表示する |
| bfirst,bf          | 先頭のバッファに移動する                         |
| blast,bl           | 最後のバッファに移動する                         |
| bnext,bn           | 次のバッファに移動する                           |
| bprev,bp           | 前のバッファに移動する                           |
| b NUM              | NUM番目のバッファに移動する                      |
| badd               | バッファにファイルをロードする                   |
| bdelete,bd         | バッファをアンロードする                         |

## vimgrep

ファイル内の検索が可能。`:grep`はシステムの`grep`を呼び出すためのコマンド。
```vim
:vim[grep] {pattern} {file} ...
```
`{pattern}`の概要は`:help pattern-overview`でみれる。
`{file}`にはワイルドカードが指定可能。

vimgrepは普通のgrepやgit-grepより遅い。

### キーバインド候補
```vim
nnoremap [q :cprevious<CR>   " 前へ
nnoremap ]q :cnext<CR>       " 次へ
nnoremap [Q :<C-u>cfirst<CR> " 最初へ
nnoremap ]Q :<C-u>clast<CR>  " 最後へ
```

### `/`との違い
|                        | /                |       vimgrep         |
|------------------------|------------------|-----------------------|
| 正規表現使える         | yes              | yes                   |
| 検索対象               | カレントバッファ | 引数で指定する        |
| ヒット件数             | 分からない       | 分かる                |
| 次の検索結果へ移動する | n                | :cn[ext]              |
| 前の検索結果へ移動する | N                | :cN[ext] :cp[revious] |
| Quickfix使える         | no               | yes                   |


### カレントバッファに対するvimgrep
```vim
" カレントバッファを対象にする
:vim {pattern} %
```

### 何度も同じ検索対象を使う場合

```vim
:vim foo path/to/search/dir/**
:vim bar path/to/search/dir/**
:vim baz path/to/search/dir/**
:vim hoge path/to/search/dir/**
:vim piyo path/to/search/dir/**
```
上記の検索は、下記で置き換え可能。

```vim
:ar path/to/search/dir/**
:vim foo ##
:vim bar ##
:vim baz ##
:vim hoge ##
:vim piyo ##
```
`:ar[gs]`コマンドは、次のようにも使える。
```vim
:ar `find . -name \\*.rb`
```
### 検索オプション
g オプションをつけない場合、それぞれの行に対して一度しかマッチしません。 g オプションをつけると、すべて、マッチします。
```vim
:vimgrep /foo/g *
```
j オプションをつけると、マッチした場所にジャンプしません。
```vim
:vimgrep /foo/j *
```
大文字小文字を区別しないには、 \c を指定します。
/ を省略することもできますが、gやjのオプションを指定できなくなります。
```vim
:vimgrep /foo\c/ *
:vimgrep foo *
:vimgrep foo\c *
```
先頭に \C を入れることで大文字と小文字を区別するようになります。
```vim
:vimgrep /\Ckeyword/ **
```
ファイルの指定するときに ** を使うことで再帰的にファイルを検索することができます。
```vim
:vimgrep fprintf **/*.c
```

## レジスタ

### Expressionレジスタ
挿入モードで`<C-R>=`で実行。
実行するとコマンドモードに移行し、`=`の後に式を入力する。
式には、vimの組み込み関数やユーザ定義関数、変数も利用可能。

### パスのコピーアンドペースト
1. vimfilerなどでコピーしたいパスのディレクトリを開く。
1. `:let path=getcwd()`
1. でpathにパスをコピー。
1. 貼り付け先で、`<C-R>=`とし、`=path`と入力する。

## clipboard
### mac
vim, vim+tmuxでvimの選択範囲やファイルをクリップボードへコピーする方法は色々ある。
vim単体の場合は、vimを`+clipboard`でbuildして、設定を加える。
tmux+vimの場合は、tmux側のコピー方法に設定を加えるなどがある。

環境依存であったり、準備が面倒なので、ちょっとしたコピーしかない場合は下記のコマンドでOK.

ファイルをクリップボードへコピー
```
:w !pbcopy
```

選択範囲をクリップボードへコピー。
visual modeで選択して`:w !pbcopy`と打てば下記が入力される。
```
:'<,'>w !pbcopy
```

## ctags

### 新しいタブで開く
```vim
nnoremap <F3> :<C-u>tab stj <C-R>=expand('<cword>')<CR><CR>
```

### reference
* [vim commands and piping](http://seejohncode.com/2014/01/27/vim-commands-piping/)
* [Route 477](http://route477.net/w/VimMemo.html)

