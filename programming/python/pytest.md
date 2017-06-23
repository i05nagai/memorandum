## pytest

## coverage
coverage用のpluginをいれる

```
pip install pytest-cov
```

pytest 実行時に`--cov=module_name`オプションをつける

```
pytest --cov=module_name . 
```

更に、`--cov-report`でHTMLのreportを出力してくれる

```
pytest --cov=module_name --cov-report .
```

## check PEP8

```
pip install pytest-pep8
```

pytest実行時に`--pep8`をつける。

```
pytest --pep8 .
```

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

## Reference
* [pytest fixtures: explicit, modular, scalable — pytest documentation](https://docs.pytest.org/en/latest/fixture.html?highlight=conftest)

