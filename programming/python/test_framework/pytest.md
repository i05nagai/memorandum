---
title: pytest
---

## pytest

## pytest fixtures: explicit, modular, scalable
テストを繰り返し実行したり、確実にするためのテスト用のクラスやモジュールなど。
以下の場合に有用

* 同じオブジェクトを複数のクラスで常に使う
* オブジェクトに特殊な設定が必要
    * テスト用にlocalで実行するといった設定を毎回しなくていいように

以下で利用可能なfixtureの一覧を見ることができる。

```
pytest --fixtures test_simplefactory.py
```

fixturesのscopeはデフォルトでは、通常のpythonの関数と同じで定義したファイル内で有効である。
moduleやfileを跨いで利用したい場合は、`conftest.py`というファイルに記載するとそのディレクトリ内の全てのtestで利用可能になる。

## Basic Test Configuration
* [Basic test configuration — pytest documentation](https://docs.pytest.org/en/latest/customize.html)

`rootdir`の決定は以下の方法で行われる。

* `args`の中でパスとして指定されているものが、あればそれがrootdirのパスになる
* 上のディレクトリを検索し、最初に見つかった`setup.cfg`、`tox.ini`、`pytest.ini`があるディレクトリがrootdirになる。
    * あわせて、見つかったファイルが設定ファイルとなる
* iniファイルが見つからなければ、同様に`setup.py`を探す

`args`が指定されていなければ、working directory以下のtestを対象とする。


設定は、以下のいずれかのファイルに記載。
`setup.cfg`か`tox.ini`に記載しているものが多い。

* setup.cfg
* tox.ini
* pytest.ini

もしくは、`PYTEST_ADDOPTS`といった環境変数に追加する。

```ini
[pytest]
# pytestのオプション
addopts = -rsxX -q
# 無視するディレクトリ
norecursedirs = .svn _build tmp*
# testを検索するdirectory
# 何も指定しないとroot directoryから検索
testpaths = testing doc
# 無視するerror
filterwarnings =
    error
    ignore::DeprecationWarning
```


## Good Integration Practises
* [Good Integration Practices — pytest documentation](https://docs.pytest.org/en/latest/goodpractices.html)

よくあるdirectory layoutは2つである。
testをtest対象と別のディレクトリにおく。

```
setup.py
mypkg/
    __init__.py
    app.py
    view.py
tests/
    test_app.py
    test_view.py
    ...
```

testをtest対象と同じディレクトリにおく。

```
setup.py
mypkg/
    __init__.py
    app.py
    view.py
    test/
        __init__.py
        test_app.py
        test_view.py
        ...
```

pytestが自動で追加するimport元ディレクトリについて。
testを書いているpythonファイルからtest対象のmoduleをimportする必要がある。
test対象のimportディレクトリは以下の規則で追加される。
`module_dir/tests/test_module.py`というファイルをテストする場合

* `basedir`の決定
    * `module_dir/tests/test_module.py`から上のディレクトリに登っていく
    * `__init__.py`を含まない最初のディレクトリが`bssedir`
    * `module_dir/tests/`に`__init__.py`が含まれない場合は、`module_dir/tests/`がbase_dir
    * `module_dir`と`module_dir/tests`が両方共`__init__.py`を含む場合は、`module_dir`の親ディレクトリが`basedir`になる
* `basedir`を`sys.path.insert(0, basedir)`で追加
    * 0番目に挿入される
    * importは、test用のファイルは`basedir`からの相対パスにもとづいてimportする

`test_module.py`で`module.py`をテストする場合に、`test_module.py`から`module.py`をどのようにimportするか。

以下のディレクトリ構成だと、`import module`

```
module_dir/
  module.py
  tests/
    __init__.py
    test_module.py
```

以下のディレクトリ構成だと、`import module_dir.module`

```
module_dir/
  __init__.py
  module.py
  tests/
    __init__.py
    test_module.py
```


以下のディレクトリ構成だと、`import module`

```
module_dir/
  module.py
  test_module.py
```

となる。

## Function
* [Reference — pytest documentation](https://docs.pytest.org/en/latest/reference.html#pytest-approx)

* `pytest.approx(expected, rel=None, abs=None, nan_ok=False)[source]`
    * default value of `abs` is `1e-12`
    * default value of `rel` is `1e-6`
    * `expected == approx(actual)`
    * `abs(expected - actual) < tolerance`
    * `abs`
        * if `rel=None`, `tolerance` is the value of `abs`
    * `rel`
        * `tolerance` is the value of `max(rel * abs(expected), abs)`

```python
from pytest import approx
# 0.01120946664130403 - 0.0112093559873 = 1.1065400403083292e-07
# False
0.01120946664130403 == approx(0.0112093559873)
# False
0.01120946664130403 == approx(0.0112093559873, rel=1e-6)
# 1e-6 * 0.01120946664130403 = 1.120946664130403e-08
# False
0.01120946664130403 == approx(0.0112093559873, rel=5e-4)
# 5e-4 * 0.01120946664130403 = 5.604733320652015e-06
```

## Fixtures
* [Pytest API and builtin fixtures — pytest documentation](https://docs.pytest.org/en/latest/builtin.html)

* class FixtureRequest
    * addfinalizer
        * teardown methodを定義
        * testが全て終了したときに呼ばれる

## ignore eggs files

## Template for setup.py

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools.command.test import test as TestCommand
import sys


NAME = ''
MAINTAINER = ''
MAINTAINER_EMAIL = ''
DESCRIPTION = """ """
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()
LICENSE = ''
URL = ''
VERSION = '0.0.1'
DOWNLOAD_URL = ''
CLASSIFIERS = """ \
Development Status :: 1 - Planning
Intended Audience :: Science/Research
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 3.5
Topic :: Software Development
Operating System :: Unix
Operating System :: MacOS
"""
INSTALL_REQUIRES = [
]
TESTS_REQUIRE = [
]


class PyTest(TestCommand):
    """
    """
    user_options = [
        ('cov=', '-', "coverage target."),
        ('pdb', '-', "start the interactive Python debugger on errors."),
        ('pudb', '-', "start the PuDB debugger on errors."),
        ('quiet', 'q', "decrease verbosity."),
        ('verbose', 'v', "increase verbosity."),
        # collection:
        ('doctest-modules', '-', "run doctests in all .py modules"),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = ''
        self.pdb = ''
        self.pudb = ''
        self.quiet = ''
        self.verbose = ''
        # collection:
        self.doctest_modules = ''
        self.test_args = [""]
        self.test_suite = True

    def finalize_options(self):
        TestCommand.finalize_options(self)

    def run_tests(self):
        import pytest
        # if cov option is specified, option is replaced.
        if self.cov:
            self.test_args += ["--cov={0}".format(self.cov)]
        else:
            self.test_args += ["--cov=."]
        if self.pdb:
            self.test_args += ["--pdb"]
        if self.pudb:
            self.test_args += ["--pudb"]
        if self.quiet:
            self.test_args += ["--quiet"]
        if self.verbose:
            self.test_args += ["--verbose"]
        if self.doctest_modules:
            self.test_args += ["--doctest-modules"]

        print("executing 'pytest {0}'".format(" ".join(self.test_args)))
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def main():
    cmdclass = {
        'test': PyTest,
    }
    metadata = dict(
        name=NAME,
        packages=[NAME],
        package_dir={NAME: '../'},
        version=VERSION,
        description=DESCRIPTION,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        url=URL,
        download_url=DOWNLOAD_URL,
        license=LICENSE,
        classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
        long_description=LONG_DESCRIPTION,
        install_requires=INSTALL_REQUIRES,
        tests_require=TESTS_REQUIRE,
        cmdclass=cmdclass,
    )

    setup(**metadata)


if __name__ == '__main__':
    main()
```

## Tips

### Could not load conftest
cacheにconftestが残っている場合に起こる。
conftestのあるディレクトリなどにある`__pycache__`を消せば良い。

```
Traceback (most recent call last):
  File "/usr/lib/python3.4/site-packages/_pytest/config.py", line 336, in _getconftestmodules
    return self._path2confmods[path]
KeyError: local('/tmp/spark/tests')

During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/usr/lib/python3.4/site-packages/_pytest/config.py", line 367, in _importconftest
    return self._conftestpath2mod[conftestpath]
KeyError: local('/tmp/spark/tests/conftest.py')

During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/usr/lib/python3.4/site-packages/_pytest/config.py", line 373, in _importconftest
    mod = conftestpath.pyimport()
  File "/usr/lib/python3.4/site-packages/py/_path/local.py", line 680, in pyimport
    raise self.ImportMismatchError(modname, modfile, self)
py._path.local.ImportMismatchError: ('conftest', '/tmp/conftest.py', local('/tmp//conftest.py'))
ERROR: could not load /tmp/spark/tests/conftest.py
```


### Measure coverage
Use `pytest-cov`.

### check PEP8
Use `pytest-pep8`

#### xunit style setup method
- [classic xunit\-style setup — pytest documentation](https://docs.pytest.org/en/latest/xunit_setup.html#method-and-function-level-setup-teardown)

## Reference
* [pytest fixtures: explicit, modular, scalable — pytest documentation](https://docs.pytest.org/en/latest/fixture.html?highlight=conftest)
* [pytest fixtures nuts and bolts - Python Testing](http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/)
