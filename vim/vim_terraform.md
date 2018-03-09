---
title: vim-terraform
---

## vim-terraform
Install wit NeoBundle

```vim
NeoBundleLazy 'hashivim/vim-terraform', {
    \ 'autoload' : {'filetypes' : 'tf'}
    \ }
```

indentを揃える

```vim
let g:terraform_align=1
```

sectionをfoldingする

```vim
let g:terraform_fold_sections=1
```

sectionのfoldingをspacebarで行う。

```vim
let g:terraform_remap_spacebar=1
```

Format

```
:TerraformFmt
```

## Reference
* [hashivim/vim-terraform: basic vim/terraform integration](https://github.com/hashivim/vim-terraform)
