---
title: Vim
---

## Vim

## styleguide
* [Google Vimscript Style Guide](https://google.github.io/styleguide/vimscriptguide.xml)
    * two space for indent


## Install

### OSX

```
brew install vim --with-lua --with-gettext --with-override-system-vi
```

* `--with-python3`
    * use python3 instead
    * now python3 is on by default
    * pyenvを使っている場合は`pyenv global`のversionをあわせる
* `--with-client-server`
    * vimの起動とともにxquartzが立ち上がるようになるので、不要であればつけない
* `--with-luajit`
    * deprecated
    * lua jit

### For ubuntu, 
* [installing \- How can I get a newer version of Vim on Ubuntu? \- Vi and Vim Stack Exchange](https://vi.stackexchange.com/questions/10817/how-can-i-get-a-newer-version-of-vim-on-ubuntu)
* [UbuntuのVimでクリップボードを使う \| komagawa292's blog](http://komagawa292.net/20140907/ubuntu-vim-clipboard/)

```
# you can copy text to clipboard with :y+
sudo apt-get install vim-gnome
```

if you want latest one

```
sudo add-apt-repository ppa:jonathonf/vim
sudo apt-get update
sudo apt-get install vim-gnome=<version>
```

where `version` is shown by

```
sudo apt show vim-gnome -a
```

Then write the following settings in `.vimrc`

```vim
set clipboard=unnamedplus
```

## vimで整形
* Use `:Align` or

組み込みの整形コマンド`\tsp`と`\tab`

`>` denotes a tab.
`-` denotes a space.

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

## register

### Expression register
挿入モードで`<C-R>=`で実行。
実行するとコマンドモードに移行し、`=`の後に式を入力する。
式には、vimの組み込み関数やユーザ定義関数、変数も利用可能。

### copy and paste path
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

## Tips

### tab to space, space to tab
`:%retab`をすると、現在のtabの設定に合わせて、space->tab, tab->spaceの変換をしてくれる。
`:expandtab`がついてる状態で、tabのindentがあればspaceに変換される。


### cinkeys
vimのindentの設定をするのもの。
`help cinkeys-format`で設定方法が見られる。

* [Vimで心地良い自動インデント設定を書くためのポイント9個 - TIM Labs](http://labs.timedia.co.jp/2011/04/9-points-to-customize-automatic-indentation-in-vim.html)

### text object
* [Vimのテキストオブジェクトについてまとめた - Qiita](http://qiita.com/kasei-san/items/143af11bb2559cf0e540)
* [Vimのテキストオブジェクトを本気出して纏めてみた - 人生リアルタイムアタック](http://shinespark.hatenablog.com/entry/2015/11/12/070000)

### 挿入モードからノーマルモードへの復帰
| キーストローク | 結果                         |
|----------------|------------------------------|
| <Esc>          | ノーマルモードに切り替え     |
| <C-[>          | ノーマルモードに切り替え     |
| <C-o>          | 挿入ノーマルモードに切り替え |

* [挿入ノーマルモード - Qiita](http://qiita.com/takasianpride/items/6900eebb7cde9fbb5298)

### 挿入ノーマルモード
Normal modeでのコマンドを1つ実行して、insert modeに戻る。

### runtimepath
実行時にvimが探すパス。
runtimepathで指定されたディレクトリ以下の以下のファイル群を探す。

* filetype.vim
    * filetypes by file name |new-filetype|
* scripts.vim
    * filetypes by file contents |new-filetype-scripts|
* autoload/
    * automatically loaded scripts |autoload-functions|
* colors/
    * color scheme files |:colorscheme|
* compiler/	
    * compiler files |:compiler|
* doc/
    * documentation |write-local-help|
* ftplugin/
    * filetype plugins |write-filetype-plugin|
* indent/
    * indent scripts |indent-expression|
* keymap/
    * key mapping files |mbyte-keymap|
* lang/
    * menu translations |:menutrans|
* menu.vim
    * GUI menus |menu.vim|
* pack/	
    * packages |:packadd|
* plugin/
    * plugin scripts |write-plugin|
* print/
    * files for printing |postscript-print-encoding|
* spell/
    * spell checking files |spell|
* syntax/
    * syntax files |mysyntaxfile|
* tutor/
    * files for vimtutor |tutor|

### filetype plugins
helpは`:help ftplugin`でひける。
fileを読み込んだときに、fileのtype(csv, cpp, java, go, python など)が決定される。
このfiletypeごとに、設定を読み込むことができる。
cpp用の設定などはここにかく。

```
~/.vim/ftpugin/filetype.vim
```

* `filetype.vim`
    * cppなら`cpp.vim`などをく
    * filetypeの名前

以下を実行すると、runtimepathで指定されているパスからの相対パスとして指定されているファイルをvim-pluginとして読み込む。
ここにftpluginをおいても良い。

```vim
runtime! userautoload/*.vim
```

## Runtime path1
https://groups.google.com/forum/#!topic/vim_use/9CkHnKN4Vls
http://vimdoc.sourceforge.net/htmldoc/starting.html#$VIMRUNTIME
http://vim.wikia.com/wiki/Understanding_VIMRUNTIME

`syntax on` reads `$VIMRUNTIME/syntax/syntax.vim` file when it calls.
If you want to change `$VIMRUNTIME` environment variable, you can set environment variable before calling `vim`

```
VIMRUNTIME=/path/to/vim vim /path/to/file
```

`$VIMRUNTIME` is different from `:set runtimepath` which i

## Reference
* [vim commands and piping](http://seejohncode.com/2014/01/27/vim-commands-piping/)
* [Route 477](http://route477.net/w/VimMemo.html)
