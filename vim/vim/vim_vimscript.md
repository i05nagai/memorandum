---
title: Vim Vimscript
---

## Vim Vimscript

## Commands
* [External Commands / Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/chapters/52.html)

* `:!`
    * pronounced bang
    * run external commands
    * e.g. `:!ls`
* `:silent !`
    * run external commands without `Press ENTER or type command to continue`
* `:echom`
* `:messages`
    * show vim messages

## Functions
* [Functions / Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/chapters/23.html)
* [Vim scripting cheatsheet](https://devhints.io/vimscript)

Built-in funcitons `:help functions`


* `append()`
    * `append(3, ["foo", "bar"])`
        * This will append two lines, foo and bar, below line 3 in your current buffer
* `system()`
* `split()`
* `call()`



### filename modifier
```vim
" print name of current file
:echo expand("%")

" print full path of curret file
:echo expand("%:p")

" print name of curret file without extension
:echo expand("%:r")

" print extension of current file
:echo expand("%:e")
```

## Reference
