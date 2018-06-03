---
title: Cython setup.py
---

## Cython setup.py

## Simple setup.py

* `setup.py`
* `helloworld.pyx`

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("helloworld.pyx")
)
```

The following command generates `helloworld.c` and shared lib.

```
python setup.py build_ext --inplace
```


## Multiiple files to single module

```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extension = Extension("modularize", ["file1.pyx", "file2.pyx"])
setup(
    ext_modules=cythonize(extension)
)
```

* `module_name`がimportで使われる名前
* `path/to/file.pyx`にcompileするfileを指定する

## Specify include path and libary path
* [Compilation — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/reference/compilation.html#compilation-reference)

```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("primes", ["primes.pyx"],
        include_dirs = [...],
        libraries = [...],
        library_dirs = [...]),
    # Everything but primes.pyx is included here.
    Extension("*", ["*.pyx"],
        include_dirs = [...],
        libraries = [...],
        library_dirs = [...]),
]
setup(
    name = "My hello app",
    ext_modules = cythonize(extensions),
)
```

## cythonize
The definiton of `cythonize` function used in `setup.py` are in https://github.com/cython/cython/blob/master/Cython/Build/Dependencies.py#L864

```python
def cythonize(module_list, exclude=None, nthreads=0, aliases=None, quiet=False, force=False, language=None,
              exclude_failures=False, **options):
```

* `options`
    * compiler opiton passed to c/c++ compiler

`options` can contain

* `include_path`
* `build_dir`
* `common_utility_include_dir`

## Reference

