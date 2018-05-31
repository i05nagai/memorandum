---
title: Cython Compile
---

## Cython Compile
* `.pyx` compiled by Cython to `.c`
* `.c` compiled by C compiler to `.so`
    * to `.pyd` in Windows
    * usually in `setup.py` does

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

```
cython [options] sourcefile.{pyx,py} ...
```

* -l, --create-listing
    * Write error messages to a listing file
* `-I, --include-dir <directory>`
    * Search for include files in named directory
    * multiple include directories are allowed
* `-o, --output-file <filename>`
    * Specify name of generated C file
* -t, --timestamps
    * Only compile newer source files
* -f, --force
    * Compile all source files (overrides implied -t)
* -v, --verbose
    * Be verbose, print file names on multiple compilation
* -p, --embed-positions
    * If specified, the positions in Cython files of each function definition is embedded in its docstring.
* `--cleanup <level>`
    * Release interned objects on python exit, for memory debugging.  Level indicates aggressiveness, default 0 releases nothing.
* `-w, --working <directory>`
    * Sets the working directory for Cython (the directory modules are searched from)
* `--gdb`
    * Output debug information for cygdb
* `--gdb-outdir <directory>`
    * Specify gdb debug information output directory. Implies --gdb.
* -D, --no-docstrings
    * Strip docstrings from the compiled module.
* -a, --annotate
    * Produce a colorized HTML version of the source.
* `--annotate-coverage <cov.xml>`
    * Annotate and include coverage information from cov.xml.
* `--line-directives`
    * Produce #line directives pointing to the .pyx source
* `--cplus`
    * Output a C++ rather than C file.
* `--embed[=<method_name>]`
    * Generate a main() function that embeds the Python interpreter.
* -2
    * Compile based on Python-2 syntax and code semantics.
* -3
    * Compile based on Python-3 syntax and code semantics.
* --lenient
    * Change some compile time errors to runtime errors to improve Python compatibility
* --capi-reexport-cincludes      Add cincluded headers to any auto-generated header files.
* --fast-fail                    Abort the compilation on the first error
* --warning-errors, -Werror      Make all warnings into errors
* --warning-extra, -Wextra       Enable extra warnings
* `-X, --directive <name>=<value>[,<name=value,...]`
    * Overrides a compiler directive

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
