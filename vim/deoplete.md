---
title: deoplete.nvim
---

## deoplete.nvim
Deoplete is the abbreviation of "dark powered neo-completion". 

## Install

```
call dein#add('Shougo/deoplete.nvim')
if !has('nvim')
  call dein#add('roxma/nvim-yarp')
  call dein#add('roxma/vim-hug-neovim-rpc')
endif
let g:deoplete#enable_at_startup = 1
```

For Vim8,

```
pip3 install --user pynvim
```

## configuration


## Error

#### error1
If you get error like below, `pynvim` may be missing.

```
[deoplete] VimEnter Autocommands for "*"..function deoplete#enable[9]..deoplete#initialize[1]..deoplete#init#_initialize[10]..<SNR>164_init_internal_variables[11]..neovim_rpc#serveraddr, line 18 Error detected while processing VimEnter Autocommands for "*"..function deoplete#enable[9]..deoplete#initialize[1]..deoplete#init#_initialize[10]..<SNR>164_init_internal_variables[35]..VimEnter Autocommands for "*"..function deoplete#enable[9]..deoplete#initialize[1]..deoplete#init#_initialize[10]..<SNR>164_init_internal_variables[29]..neovim_rpc#serveraddr:
line   18: E605: Exception not caught: [vim-hug-neovim-rpc] requires one of `:pythonx import [pynvim|neovim]` command to work
```

Check python3 used by vim

```
vim --version
```

Install nvim

```
/path/to/pip install --user pynvim
```


## Reference
* [Shougo/deoplete.nvim: Dark powered asynchronous completion framework for neovim/Vim8](https://github.com/Shougo/deoplete.nvim)
