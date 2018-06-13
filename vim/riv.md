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
let g:riv_fold_auto_update = 0
"
" let g:riv_auto_fold_force = 0
" disable folding
let g:riv_disable_folding = 1

" path to browser
let g:riv_web_browser = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
let g:riv_web_browser = ''
let g:riv_web_browser = ''
```

Covert files are placed in

* files in  project
    * (1) `_build`
    * (2) `let project1.build_path = ''`
        * Open build path `:Riv2BuildPath`
* files not in project
    * `g:riv_temp_path`

```vim
" directory must exists
let g:riv_temp_path=''
```

```
"let g:riv_web_browser = '/path/to/broweser'
let g:riv_temp_path = 0
let g:riv_html_code_hl_style = "friendly"
```

## Usage
Conver to HTML. You need to install `docutils`.
`pip install docutils`

```
:Riv2HtmlFile
```

Convert to HTML and preview it

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
