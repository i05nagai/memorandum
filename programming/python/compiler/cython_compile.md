---
title: Cython Compile
---

## Cython Compile
* `.pyx` compiled by Cython to `.c`
* `.c` compiled by C compiler to `.so`
    * to `.pyd` in Windows

## CLI

```
cythonize [option] <target>
```

* `<targt>`
    * glob is accepted
    * `**/*`, `*.pyx`

* -X NAME=VALUE,..., --directive=NAME=VALUE,...
    * set a compiler directive
* -s NAME=VALUE, --option=NAME=VALUE
    * set a cythonize option
* -3
    * use Python 3 syntax mode by default
* -a, --annotate
    * generate annotated HTML page for source files
* -x PATTERN, --exclude=PATTERN
    * exclude certain file patterns from the compilation
* -b, --build
    * build extension modules using distutils
* -i, --inplace
    * build extension modules in place using distutils
    * (implies -b)
* -j N, --parallel=N
    * run builds in N parallel jobs (default: 6)
* -f, --force
    * force recompilation
* -q, --quiet
    * be less verbose during compilation
* --lenient
    * increase Python compatibility by ignoring some compile time errors
* -k, --keep-going
    * compile as much as possible, ignore compilation failures

## Usage
Compile `.pyx` to `.c`

```
cythonize -a -i yourmod.pyx
```

To compile generated `.c` files to `.so`, for example, 

```
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
      -I/usr/include/python3.5 -o yourmod.so yourmod.c
```

## Reference
* [Compilation — Cython 0.28.2 documentation](http://docs.cython.org/en/latest/src/reference/compilation.html)
