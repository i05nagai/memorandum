---
title: jedi-vim
---

## jedi-vim
jedi-vim is a VIM binding to the autocompletion library Jedi.


## Installation
* python2.6 or higher
* vim is built with
    * +python
    * +python3

vim上で以下のcommandで対応しているか確認できる。

```
:python3 import sys; print(sys.version
```

```
:python import sys; print(sys.version
```





## Configuraition

bufferではなくtabで定義に移動

```vim
let g:jedi#use_tabs_not_buffers = 1
```

bufferではなく`vs`で定義を表示

```vim
let g:jedi#use_splits_not_buffers = "left"
```

dot`.`を押すとdefaultでcompletionされるが、offにできる。

```vim
let g:jedi#popup_on_dot = 0
```

defaultのkey assign

```vim
let g:jedi#goto_command = "<leader>d"
let g:jedi#goto_assignments_command = "<leader>g"
let g:jedi#goto_definitions_command = ""
let g:jedi#documentation_command = "K"
let g:jedi#usages_command = "<leader>n"
let g:jedi#completions_command = "<C-Space>"
let g:jedi#rename_command = "<leader>r"
```

completionが不要の場合は下にcheck

```vim
let g:jedi#completions_enabled = 0
```


## Reference
* [davidhalter/jedi-vim: Using the jedi autocompletion library for VIM.](https://github.com/davidhalter/jedi-vim)
