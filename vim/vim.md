# vim

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
`:vimfiler `を入力中に、`<Ctr-R>"`で貼り付けできる。

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

