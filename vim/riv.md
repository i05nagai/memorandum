---
title: riv
---

## riv

## Install

```vim
NeoBundle `Rykka/riv.vim`
```

## Settings
* [1. Instruction · gu-fan/riv.vim Wiki · GitHub](https://github.com/gu-fan/riv.vim/wiki/1.-Instruction#folding)

```vim
let g:riv_fold_level = 1
" 
le g:riv_fold_auto_update = 0
"
" let g:riv_auto_fold_force = 0
" disable folding
let g:riv_disable_folding = 1
```

```
"let g:riv_web_browser = '/path/to/broweser'
let g:riv_temp_path = 0
let g:riv_html_code_hl_style = "friendly"
```

## Usage
* htmlでのpreview

```vim
:Riv2HtmlAndBrowse
```

## Tips

### disable foldings
* [Can't disable folding · Issue #39 · gu-fan/riv.vim · GitHub](https://github.com/gu-fan/riv.vim/issues/39)

```vim
" disable folding
let g:riv_disable_folding = 1
```

## Reference
* [riv.vim/riv_quickstart.rst at master · Rykka/riv.vim](https://github.com/Rykka/riv.vim/blob/master/doc/riv_quickstart.rst)
* [Riv.vim : sphinx 編集用プラグイン — 苦労する遊び人の玩具箱 1 ドキュメント](http://qh73xebitbucketorg.readthedocs.io/ja/latest/2.Tools/vim/plugin/riv/)
