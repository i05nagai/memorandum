---
title: Cython
---

## Cython
* `.pyx`
    * the definiton of
* `.pxd`
    * like header file in C
    * definition file
    * used with `cimport` statement
* `.pix`
    * used with `include` statement
    * e.g. declaration of compile time consnats

## Install

```
pip install cython
```

Now you can use CLIs and cython package.

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

## Sharing declarations between cython modules
* [Sharing Declarations Between Cython Modules — Cython 0.28.2 documentation](http://cython.readthedocs.io/en/latest/src/userguide/sharing_declarations.html)

* `.pxd`
    * definition file
    * c declaration that are to be available to other cython modules
        * any kind of C type dclation
        * extern C function or variable declaration
        * declarations of C functions defined in the module
        * the definiton part of an extension type
    * search paths for `cimport modulename`
        * search `modulename.pxd` in following dirctories
            * `-I` option
            * `include_path` argument in `cythonize()`
            * `sys.path`
* `.pyx`
    * implementation file


`cimport` statement

```
cimport module [, module...]
from module cimport name [as name] [, name [as name] ...]
```

Example of `.pxd` file

```cython
cdef enum otherstuff:
    sausage, eggs, lettuce

cdef struct spamdish:
    int oz_of_spam
    otherstuff filler

cdef extern from "lunch.h":
    void eject_tomato(float)
```

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

## Distributing Cython modules
* [Compilation — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/reference/compilation.html#distributing-cython-modules)

* It is strongly recommended that you distribute the generated .c files as well as your Cython sources
    * users can use your module without cython

```python
from distutils.core import setup
from distutils.extension import Extension

setup(
    ext_modules = [Extension("example", ["example.c"])]
)
```

## Compiler directive
* [Compilation — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/reference/compilation.html#compiler-directives)

List of compiler directive



### Specify compiler directives
In `.pyx` file, you can specify them in comments

```python
#cython: language_level=3, boundscheck=False
```

or use decorator

```python
import cython

@cython.boundscheck(False) # turn off boundscheck for this function
def f():
    ...
    # turn it temporarily on again for this block
    with cython.boundscheck(True):
        ...
```

In `setup.py`,

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "My hello app",
    ext_modules = cythonize('hello.pyx', compiler_directives={'embedsignature': True}),
)
```

## Tips
* `pxd`の文法が間違っていてもエラーがでない可能性がある
    * その場合極端に遅くなる
    * `z = z * z + x`を`z = z * + x`でエラーはでないが実行時間が10倍近く遅い
* `Cannot read reduction variable in loop body`

### profiling
`.pyx`ファイルの先頭に以下をかく。

## Reference
* [Cython ドキュメント（和訳） — Cython 0.17.1 documentation](http://omake.accense.com/static/doc-ja/cython/index.html)
