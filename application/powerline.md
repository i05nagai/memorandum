---
title: powerline
---

## powerline

brew installでpythonを入れている場合は`--user`を除く

```
pip install --user powerline-status
```

## tmux
* [Add power to your terminal with powerline - Fedora Magazine](https://fedoramagazine.org/add-power-terminal-powerline/)

* powerlineのinstall場所を調べる
    * [Installation — Powerline beta documentation](https://powerline.readthedocs.io/en/latest/installation.html#repository-root)
    * `pip show powerline-status`
    * e.g. `/usr/local/lib/python2.7/site-packages`

`{repository_root}`はpowerlineのinstall場所

```
source "{repository_root}/powerline/bindings/tmux/powerline.conf"
```

`$POWERLINE_CONFIG_COMMAND`が設定されている必要がある。
`powerline-config` commandが使える必要がある。

## Configurations
* [Configuration and customization — Powerline beta documentation](https://powerline.readthedocs.io/en/latest/configuration.html)


## Reference
* [powerline/powerline: Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.](https://github.com/powerline/powerline)
* [Powerline — Powerline beta documentation](https://powerline.readthedocs.io/en/latest/)
