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



## Reference
* [pytest fixtures: explicit, modular, scalable — pytest documentation](https://docs.pytest.org/en/latest/fixture.html?highlight=conftest)

