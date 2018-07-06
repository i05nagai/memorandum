# unite

## source
* unite-tag
    * [github](https://github.com/tsukkee/unite-tag)

## default actionの設定

kindに対しては次のように設定できる。

```vim
" ディレクトリは vimfiler で開く
call unite#custom#default_action('directory' , 'vimfiler')
" ファイルは tabdrop で開く
call unite#custom#default_action('file' , 'tabdrop')
" 次のように , で複数の kind に対して設定することもできる
call unite#custom#default_action('file,buffer' , 'tabdrop')
```

sourceごとにdefault actionを設定する場合は、

```vim
" source/{name}/{kind} のように source と kind を指定する事ができる
" source-bookmark の kind-directory は tabvimfiler を使用する
call unite#custom#default_action("source/bookmark/directory", "tabvimfiler")
" kind に * を設定すればその source のすべての kind に対して設定される
" source-file のデフォルトの action を tabdrop にする
call unite#custom#default_action("source/file/*", "tabdrop")
```

## Configuration


* `g:unite_source_menu_menus`
    * create cutome `menu:<your-command>`
    * dictionary



```vim
" Example of creating menu:test command
let g:unite_source_menu_menus = get(g:,'unite_source_menu_menus',{})
let g:unite_source_menu_menus.test = {
      \     'description' : 'Test menu',
      \ }
let g:unite_source_menu_menus.test.candidates = {
      \   'ghci'      : 'VimShellInteractive ghci',
      \ }
function g:unite_source_menu_menus.test.map(key, value)
  return {
      \       'word' : a:key, 'kind' : 'command',
      \       'action__command' : a:value,
      \     }
endfunction
```

```
:Unite menu:test
```


## Reference
* [unite.vim の action の設定方法いろいろ - C++でゲームプログラミング](http://d.hatena.ne.jp/osyo-manga/20131006/1381065976)
* [unite.vim の action を定義する - C++でゲームプログラミング](http://d.hatena.ne.jp/osyo-manga/20131028/1382963891)
