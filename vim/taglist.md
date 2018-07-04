---
title: taglist
---

## TagList
* [Document](https://github.com/vim-scripts/taglist.vim/blob/master/doc/taglist.txt)

## Install
For NeoBundle,

```vim
  NeoBundleLazy 'vim-scripts/taglist.vim', {
        \ 'autoload' : {'filetypes' : 'cpp'}
        \ }
```

## keymap

* `<CR>`
    * Jump to the location where the tag under cursor is defined.
* o
    * Jump to the location where the tag under cursor is defined in a new window.
* P
    * Jump to the tag in the previous (Ctrl-W_p) window. 
* p
    * Display the tag definition in the file window and keep the cursor in the taglist window itself.
* t
    * Jump to the tag in a new tab. If the file is already opened in a tab, move to that tab.
* Ctrl-t
    * Jump to the tag in a new tab.
* `<Space>`
    * Display the prototype of the tag under the cursor.  
    * For file names, display the full path to the file, file type and the number of tags.
    * For tag types, display the tag type and the number of tags.
* u
    * Update the tags listed in the taglist window
* s
    * Change the sort order of the tags (by name or by order)
* d
    * Remove the tags for the file under the cursor
* x
    * Zoom-in or Zoom-out the taglist window
* +
    * Open a fold
* -
    * Close a fold
* *
    * Open all folds
* =
    * Close all folds
* [[
    * Jump to the beginning of the previous file
* `<Backspace>`
    * Jump to the beginning of the previous file
* ]]
    * Jump to the beginning of the next file
* `<Tab>`
    * Jump to the beginning of the next file
* q
    * Close the taglist window
* `<F1>`
    * Display help


## Reference
* [vim\-scripts/taglist\.vim: Source code browser \(supports C/C\+\+, java, perl, python, tcl, sql, php, etc\)](https://github.com/vim-scripts/taglist.vim)
* [github](http://qiita.com/masaharu-suizu/items/ad082d728eac7f548e0b)
