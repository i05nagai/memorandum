---
title: Vim Command
---

## Vim Command

## Builtin commands
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
* `:fu[nction]`
    * show all functions
* `:fu[nction] {name}`
* `:fu[nction] /{pattern}`
* `:let {var-name} = {expr1}`
* `:let {var-name}[{idx}] = {expr1}`
* `:let {var-name}[{idx1}:{idx2}] = {expr1}`
* `:command! `
    * define commands
* `:redir <register>`
    * [vim \- How to redirect ex command output into current buffer or file? \- Stack Overflow](https://stackoverflow.com/questions/2573021/how-to-redirect-ex-command-output-into-current-buffer-or-file)
    * redirecting the output of this 
    * `:redir @a`
    * `:redir END`
        * end redirecting

## Define commands
* [Vim documentation: usr_40](http://vimdoc.sourceforge.net/htmldoc/usr_40.html#40.2)


## Reference
* [Vim documentation: eval](http://vimdoc.sourceforge.net/htmldoc/eval.html)
