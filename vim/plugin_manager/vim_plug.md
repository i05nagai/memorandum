---
title: vim-plug
---

## vim-plug
Minimalist Vim Plugin Manager.


## Configuration
Install 

```vim
if empty(glob("~/.vim/autoload/plug.vim"))
    execute '!curl -fLo ~/.vim/autoload/plug.vim https://raw.github.com/junegunn/vim-plug/master/plug.vim'
endif
```

Lazy load by file type.

```vim
Plug 'plasticboy/vim-markdown', { 'for': 'markdown' }
```

Lazy load by `Rename` command.

```vim
Plug 'AlexJF/rename.vim', { 'on': 'Rename' }
```

## Tips

### Pallalel install
* You need to compile vim with Ruby option

## Reference
* [junegunn/vim-plug: Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [Why I switched from Vundle to Plug / Jordan Eldredge](https://jordaneldredge.com/blog/why-i-switched-from-vundle-to-plug/)
