---
title: pytest CLI
---

## pytest CLI


## CLI

```
pytest [options] [file_or_dir] [file_or_dir] [...]
```

* `-k EXPRESSION`
    * only run tests which match the given substring expression. An expression is a python evaluatable expression where all names are substring-matched against test names and their parent classes.
    * Example:
        * `-k 'test_method or test_other'`
            * matches all test functions and classes whose name contains 'test_method' or 'test_other', while -k 'not test_method' matches those that don't contain 'test_method' in their names.
            * Additionally keywords are matched to classes and functions containing extra names in their 'extra_keyword_matches' set, as well as functions which have names assigned directly to them.
* `-m MARKEXPR`
    * only run tests matching given mark expression.
    * example: -m 'mark1 and not mark2'.
* `--markers`
    * show markers (builtin, plugin and per-project ones).
* `-x, --exitfirst`
    * exit instantly on first error or failed test.
* `--maxfail=num`
    * exit after first num failures or errors.
* `--strict`
    * marks not registered in configuration file raise errors.
* `-c file`
    * load configuration from `file` instead of trying to locate one of the implicit configuration files.
* `--continue-on-collection-errora`
    * Force test execution even if collection errors occur.
* `--rootdir=ROOTDIR`
    * Define root directory for tests. Can be relative path: 'root_dir', './root_dir', 'root_dir/another_dir/';
                    absolute path: '/home/user/root_dir'; path with variables: '$HOME/root_dir'.
* `--fixtures, --funcargs`
    * show available fixtures, sorted by plugin appearance
    * (fixtures with leading '_' are only shown with '-v')
* `--fixtures-per-test`
    * show fixtures per test
* `--import-mode={prepend,append}`
    * prepend/append to sys.path when importing test modules, default is to prepend.
* `--pdb`
    * start the interactive Python debugger on errors or KeyboardInterrupt.
* `--pdbcls=modulename:classname`
    * * start a custom interactive Python debugger on errors.
    * For example:`--pdbcls=IPython.terminal.debugger:TerminalPdb`
* `--capture=method`
    * per-test capturing method: one of fd|sys|no.
* `-s`
    * shortcut for --capture=no.
* `--runxfail`
    * run tests even if they are marked xfail
* `--lf, --last-failed`
    * rerun only the tests that failed at the last run (or all if none failed)
* `--ff, --failed-first`
    * run all tests but run the last failures first. This may re-order tests and thus lead to repeated fixture setup/teardown
* `--nf, --new-first`
    * run tests from new files first, then the rest of the tests sorted by file mtime
* `--cache-show`
    * show cache contents, don't perform collection or tests
* `--cache-clear`
    * remove all cache contents at start of test run.
* `--lfnf={all,none}, --last-failed-no-failures={all,none}`
    * change the behavior when no test failed in the last run or no information about the last failures was found in the cache

Reporting


* `-r chars`
    * show extra test summary info as specified by chars
    * (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed, (p)passed, (P)passed with output, (a)all except pP.
    * Warnings are displayed at all times except when `--disable-warnings` is set

distributed and subbprocess testing


* `-n numprocesses, --numprocesses=numprocesses`
    * shortcut for '--dist=load --tx=NUM*popen', you can use 'auto' here for auto detection CPUs number on host system

## Usage
Show available fixtures

```
pytest --fixtures
```

## Configuration

## Reference
