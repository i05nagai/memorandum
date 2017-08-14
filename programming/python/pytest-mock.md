## pytest mock
`pytest-mock`は `mock`packageをpytestのfixtureとして使えるようにしたもの。
`mock` packkageは現在、`unittest` moduleに統合されている。
なので、基本的な使い方は`mock`の使い方を見る。

```
pip install pytest-mock
```

## Usage

```python
def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')
```

* `mocker`
    * `pytest_mock.MockFixture`型だが、`unittest.mock`と大体同じ？

* `UnixFS.rm`テストしたいmethod
* `mocker.patch`でmockにするmoduleを指定
* `mocker.patch`で指定したmoduleはmockになっているので、呼び出し回数などの指定をする

## Tips

### Mock class in another module
あるmodule内のmethodをmockにする

```python
def test_update_jobs_fleet_capacity(mocker):
    mocker.patch.object(manager, 'sub_method') 
    manager.sub_method.return_value = 120 
    manager.method_under_test()
    manager.sub_method.assert_called_with('somestring', 1, 120)
```


### Mock class in another module
あるmodule内のclassをmockにする

```python
def test_helper_class(mocker):
    mocker.patch.object(manager, 'other_class')
    manager.other_class.other_method.return_value = 50
    manager.method_under_test('option1')
    manager.other_class.other_method.assert_called_with(120)
```

### Mocking open
* [python open をモック化する | ぷすぅ～ぷすぅ～](http://huge.mints.ne.jp/10/2015/it_technique/1691/)

```python
m = mock_open()
with patch('somemodule.open', m, create=True):
    # テストを実行する
    somemodule.action()
    # モック化された openの実行
    mock = m()
    # write で、"write something" が呼ばれたかどうか確認
    mock.write.assert_any_call("write something")

def test_pytest(mocker):
    mock = mocker.mock_open(read_data="")
    mocker.patch.object(target, "open", mock)
```

### Mocking with pytest
`some_module`内の自由関数をmockで置き換える場合は、`mocker.patch.object(target, "function_name")`は

```python
import some_module as target

def test_
mocker.patch.object(target, "function_name")
target.function_name.return_value = expect
actual = target.(dataset_name, table_name, path_to_schema)
target.function_name.assert_called_once_with(command)
```

## Reference
* [pytest-mock 1.6.0 : Python Package Index](https://pypi.python.org/pypi/pytest-mock)
* [Python unit testing with Pytest and Mock – Brendan Fortuner – Medium](https://medium.com/@bfortuner/python-unit-testing-with-pytest-and-mock-197499c4623c)
* [26.5. unittest.mock — モックオブジェクトライブラリ — Python 3.6.1 ドキュメント](https://docs.python.jp/3/library/unittest.mock.html)
