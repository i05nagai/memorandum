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
* `winnr([{arg}])`
    * The result is a Number, which is the number of the current window.
    * The top window has number 1.
    * When the optional argument is `$`, the number of the last window is returned (the window count). 
    * When the optional argument is `#`, the number of the last
* `bufname({expr})`
    * the result of `:ls`
* `fnamemodify({fname}, {mods})`
    * `mods` are filename-modifiers

Tab

* `tabpagewinnr({tabarg} [, {arg}])`
    * `winnr` for tabs
    *  When omitted the current window number is returned.
    *  This is the window which will be used when going to this tab page.
    *  When `$` the number of windows is returned.
    *  When `#` the previous window nr is returned.

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
