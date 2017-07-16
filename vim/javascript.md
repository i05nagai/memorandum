
## vim for javascript
javacript用のvimの設定について記載。

## Plugins

## Syntax highlight
いくつかある。
ES6対応のものを選ぶ。

* [GitHub - othree/yajs.vim: YAJS.vim: Yet Another JavaScript Syntax for Vim](https://github.com/othree/yajs.vim)

```vim
NeoBundleLazy 'othree/yajs.vim', {'autoload':{'filetypes':['javascript']}}
autocmd BufRead,BufNewFile *.es6 setfiletype javascript
```


## Reference
* [VimでES6のシンタックスハイライト - Qiita](http://qiita.com/QuestionDriven/items/83cba09d0010e8e31315)
