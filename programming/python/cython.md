---
title: Cython
---

## Cython
Extension is `.pyx`.

## Install

```
pip install cython
```

cython commandsが使えるようになる。　

## CLI

## Usage

HTMLファイルの生成。
生成されたCのコードをLineごとに見ることができる。
色が濃いほど生成されるコードが多い。

```
cython -a file_name.pyx
```

## pxd files
`pxd` files work like C header files.
A `pxd` file is imported into a `pyx` module by using the `cimport` keyword.

* to share external C declarations
* for `inline` function
* to provide a Cpython interface to the Cython modoule like C header
    * other Cython modules can use a more efficient protocol than Pytohn one


## Work with numpy
* Cython has support for fast access to NumPy arrays
    * You can use NumPy from Cython exactly the same as in regular Python but not recommended
* `np.int_t` is used for compiler time type
    * OK `cdef np.int_t var`
    * NG `cdef np.int var`
* for faster indexing, use `buffer` syntax, `np.ndarray[type_t, ndim=num]`
    * `[]` is python function

```python
...
def naive_convolve(np.ndarray[np.int_t, ndim=2] f, np.ndarray[DTYPE_t, ndim=2] g):
...
cdef np.ndarray[DTYPE_t, ndim=2] h = ...
```

Tuning indexing

* by default,
    * bounds checkiing is peformed
    * negative indice are checked and handled correctly
* We can diable bound checking
    * if you access out of bounds
        * you will crash your program or
        * you will corrupt data

```python
cimport cython
@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def naive_convolve(np.ndarray[DTYPE_t, ndim=2] f, np.ndarray[DTYPE_t, ndim=2] g):
```

* Do not use typed objects without knowing that they are not set tot `None`

In Python3, the below code works with any libraries supporting the `buffer` syntax

```
object[DTYPE_t, ndim=2]
```

## Tips
* `pxd`の文法が間違っていてもエラーがでない可能性がある
    * その場合極端に遅くなる
    * `z = z * z + x`を`z = z * + x`でエラーはでないが実行時間が10倍近く遅い
* `Cannot read reduction variable in loop body`

### profiling
`.pyx`ファイルの先頭に以下をかく。

```
```

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

## Reference
* [Cython ドキュメント（和訳） — Cython 0.17.1 documentation](http://omake.accense.com/static/doc-ja/cython/index.html)
