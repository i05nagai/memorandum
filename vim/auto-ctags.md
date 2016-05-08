# auto-ctags
* 保存時に自動で`ctags`を実行。
* 保存場所を`.git`などにできる。

[github](https://github.com/soramugi/auto-ctags.vim)

## 設定

```vim
"保存時に実行
let g:auto_ctags = 1
"保存先のディレクトリ指定
let g:auto_ctags_directory_list = ['.git', '.svn']
"生成されるctagsのファイル名
let g:auto_ctags_tags_name = 'tags'
"ctagsのオプション
let g:auto_ctags_tags_args = '--tag-relative --recurse --sort=yes'
```


## 参考
[Qiita](http://qiita.com/soramugi/items/f918020c2b3f48c93bf3)

