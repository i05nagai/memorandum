---
title: tmux mem cpu load
---

## tmux mem cpu load

with zplug

```zsh
zplug "thewtex/tmux-mem-cpu-load", \
    as:command, \
    use:"tmux-mem-cpu-load", \
    hook-build:'cmake . && make'
```

## Reference
* [thewtex/tmux-mem-cpu-load: CPU, RAM, and load monitor for use with tmux](https://github.com/thewtex/tmux-mem-cpu-load)
