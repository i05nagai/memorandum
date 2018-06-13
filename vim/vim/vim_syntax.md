---
title: Vim Syntax
---

## Vim Syntax

## Syntax of syntax file

## Configuration
* [Creating your own syntax files | Vim Tips Wiki | FANDOM powered by Wikia](http://vim.wikia.com/wiki/Creating_your_own_syntax_files)

You can place your owne syntax files to one of following paths

```vim
:echo expand('~')
:echo expand('~/.vim/syntax/cel.vim')
:echo $HOME
:echo expand('$HOME/vimfiles/syntax/cel.vim')
```

You can add `runtimepath`

```vim
set runtimepath+=~/.vim/
runtime! userautoload/*.vim
```

## Reference
