---
title: Scipy runtests
---

## Scipy runtests


## CLI
```
runtests.py [OPTIONS] [-- ARGS]
```

Run tests, building the project first.


```
$ python runtests.py
$ python runtests.py -s optimize
$ python runtests.py --ipython
$ python runtests.py --python somescript.py
$ python runtests.py --bench
```

Run a debugger:

```
$ gdb --args python runtests.py [...other args...]
```

Generate C code coverage listing under build/lcov/:
(requires http://ltp.sourceforge.net/coverage/lcov.php)

```
$ python runtests.py --gcov [...other args...]
$ python runtests.py --lcov-html
```

* ARGS                  Arguments to pass to Nose, Python or shell


* `--verbose, -v`
    * more verbosity
* `-m`
    * `full`, or `fast`
* `--coverage`
* `--gcov`
* `--no-build, -n`
    * do not build the project (use system installed version)
* `--build-only, -b`
    * just build, do not run any tests
* `--doctests`
    * Run doctests in module
* `--refguide-check`
    * Run refguide check (do not run regular tests.)
* `--coverage`
    * report coverage of project code. HTML output goes under build/coverage
* `--gcov`
    * enable C code coverage via gcov (requires GCC). gcov output goes to build/**/*.gc*
* `--lcov-html`
    * produce HTML for C code coverage information from a previous run with --gcov. HTML output goes to build/lcov/
* `--mode MODE, -m MODE`
    * 'fast', 'full', or something that could be passed to nosetests -A [default: fast]
* `--submodule SUBMODULE, -s SUBMODULE`
    * Submodule whose tests to run (cluster, constants, ...)
* `--pythonpath PYTHONPATH, -p PYTHONPATH`
    * Paths to prepend to PYTHONPATH
* `--tests TESTS, -t TESTS`
    * Specify tests to run
    * e.g. `scipy.fftpack.tests.test_real_transforms::TestIDSTIIIInt`
* `--python`
    * Start a Python shell with PYTHONPATH set
* `--ipython, -i`
    * Start IPython shell with PYTHONPATH set
* `--shell`
    * Start Unix shell with PYTHONPATH set
* `--debug, -g`
    * Debug build
* `--parallel PARALLEL, -j PARALLEL`
    * Number of parallel jobs during build (requires Numpy 1.10 or greater).
* `--show-build-log`
    * Show build output rather than using a log file
* `--bench`
    * Run benchmark suite instead of test suite
* `--bench-compare BEFORE`
    * Compare benchmark results of current HEAD to BEFORE.  Use an additional --bench-compare=COMMIT to override HEAD with COMMIT. Note that you need to commit your changes first!

Run tests for all modules

```
runtests.py -v
```

Fully tests with measuring coverage with optimization

```
python -u -OO runtests.py -m full --coverage --gcov -v --doctests -- -rfEX -n 3 2>&1 | tee scipy/runtests.log
```

Test build log 

```
tools/validate_runtests_log.py full < runtests.log
```

Test specific function

```
python runtests.py -t scipy.fftpack.tests.test_real_transforms::TestIDSTIIIInt
```

## Usage

## Configuration

## Reference
