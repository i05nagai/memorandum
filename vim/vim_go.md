---
title: vim-go
---

## vim-go

## Install
With neobundle

```
  NeoBundleLazy 'fatih/vim-go.vim', {
        \ 'autoload' : {'filetypes' : 'go'}
        \ }
```

* `:NeoBundleInstall`
* `:GoInstallBinaries`

## Commands

* `:GoRun`
* `:GoDebugStart`
    * `<F9>`
        * breakpoint
    * `<F5>`
        * continue
    * `<F10>`
        * next line
    * `<F11>`
        * step in
* `:GoDebugStop`
* `:GoDebugRestart`
* `:GoDef`
    * go to definition
* `:GoDoc`
* `:GoFmt`
    * run gofmt

## Configuration


## Reference
* [GitHub - fatih/vim-go: Go development plugin for Vim](https://github.com/fatih/vim-go)
* [GitHub - fatih/vim-go-tutorial: Tutorial for vim-go](https://github.com/fatih/vim-go-tutorial)

