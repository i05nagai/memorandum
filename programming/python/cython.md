---
title: Cython
---

## Cython

### Install

```
pip install cython
```

cython commandsが使えるようになる。　

### setup.py

```
from distutils.core import setup
from disutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {
        "build_ext": build_ext
    },
    ext_modules=[
        Extension("module_name", ["path/to/file.pyx"]
    ]
)
```

* `module_name`がimportで使われる名前
* `path/to/file.pyx`にコンパイルするファイルを指定する。

### commands

HTMLファイルの生成。
生成されたCのコードをLineごとに見ることができる。
色が濃いほど生成されるコードが多い。

```
cython -a file_name.pyx
```

### profiling
`.pyx`ファイルの先頭に以下をかく。

```
```

### Tips
* `pxd`の文法が間違っていてもエラーがでない可能性がある
    * その場合極端に遅くなる
    * `z = z * z + x`を`z = z * + x`でエラーはでないが実行時間が10倍近く遅い
* `Cannot read reduction variable in loop body`


## Reference
* [Cython ドキュメント（和訳） — Cython 0.17.1 documentation](http://omake.accense.com/static/doc-ja/cython/index.html)
