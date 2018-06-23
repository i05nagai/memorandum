---
title: GDB
---

## gdb

## Install

For MacOSX,
* [OS XでGDBを使う（ためにコード署名をする） - Qiita](http://qiita.com/takahashim/items/204ffa698afe09bd4e28)

```
brew install gdb
```

For ubuntu16.04,

```
apt-get install gdb
```


## Tips

### customized gdb
* [gdbで効率的にデバッグするためのTips - Qiita](http://qiita.com/aosho235/items/e8efd18364408231062d)
* [gdb-dashboard/.gdbinit at master · cyrus-and/gdb-dashboard · GitHub](https://github.com/cyrus-and/gdb-dashboard/blob/master/.gdbinit)
    * こっちのほうが良い
* [GitHub - gdbinit/Gdbinit: Gdbinit for OS X, iOS and others - x86, x86_64 and ARM](https://github.com/gdbinit/Gdbinit)
    * `~/.gdbinit`におく。

### front end of gdb
[list](https://sourceware.org/gdb/wiki/GDB%20Front%20Ends)

* [cgdb](http://blog.anatoo.jp/entry/20111023/1319375779)
    * [参考](http://blog.anatoo.jp/entry/20111023/1319375779)
    * [2](http://miettal.hatenablog.com/entry/20120408/1333917572)
    * `sudo port install cgdb`
    * vimと同じキーバインド
* [pyclewn]()
    * vimballが動かない

### coloring
`~/.gdbinit`でgdbの色付けなど設定ができる。


* [terminal - How to highlight and color gdb output during interactive debugging? - Stack Overflow](http://stackoverflow.com/questions/209534/how-to-highlight-and-color-gdb-output-during-interactive-debugging)
    * [Gdbinit | Reverse Engineering Mac OS X](https://reverse.put.as/gdbinit/)
    * [cyrus-and/gdb-dashboard: Modular visual interface for GDB in Python](https://github.com/cyrus-and/gdb-dashboard)
    * [dholm/voidwalker: A GDB toolbox for low-level debugging](https://github.com/dholm/voidwalker)


## lldb

### front end of lldb
[list](http://usevim.com/2014/03/05/lldb/)

* [vim-lldb](Bundle "gilligan/vim-lldb")


## Commands

* `@variable`
    * `variable`がポインタの時配列の中身の表示


### Reference
* [GDBでポインタを配列として表示する | Pistolfly](https://www.pistolfly.com/weblog/2012/02/gdbint.html)

