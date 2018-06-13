---
title: Vim Function
---

## Vim Function
* [Functions / Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/chapters/23.html)
* [Vim scripting cheatsheet](https://devhints.io/vimscript)


## Built functions
Built-in funcitons `:help functions`

* `append()`
    * `append(3, ["foo", "bar"])`
        * This will append two lines, foo and bar, below line 3 in your current buffer
* `system()`
* `split()`
* `call()`

## Defining functions
user-functions.

* `:fu[nction]`
    * show all functions
* `:fu[nction][!] {name}([arguments]) [range] [abort] [dict]`
* `:endf[unction]`

```vim
function Table(title, ...)
  echohl Title
  echo a:title
  echohl None
  echo a:0 . " items:"
  for s in a:000
    echon ' ' . s
  endfor
endfunction
call Table("Table", "line1", "line2")
```

## Features
You can check the feature is enabled or not in  conditional expression

```vim
:if has("gui_running")
:if has("lua")
```

## Reference
* [Vim documentation: eval](http://vimdoc.sourceforge.net/htmldoc/eval.html)
