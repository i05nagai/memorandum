---
title: unittest
---

## unittest
Standard library for unit testing.

## unittest.mock
* [26.5. unittest.mock — モックオブジェクトライブラリ — Python 3.6.1 ドキュメント](https://docs.python.jp/3/library/unittest.mock.html#patch)

* `Mock` class
    * mock用のクラス
* `MagicMock`
    * Mockのsubclass
    * `__str__`などのmagic methodに対応している点が`Mock` classと大きく異る

unittest.mock.Mock()
defaultでは、Mock classの属性やmethod戻り値は全てMock classとなる。


```python
mock = Mock()

# by default returns Mock class
mock.method()
# by default returns Mock class
mock.attribute
```

2回目移行の呼び出しは同じMock classが返却される。
ただ、属性と関数呼び出しでは別のmockが戻る。

```python
mock = Mock()
# OK
assert mock.method() == mock.method()
# OK
assert mock.method == mock.method()
# OK
assert mock.method != mock.method()
```

fluent記法のMockを考える場合は更にややこしくなる。
以下のassetは全てfailしない。

```python
mock = Mock()
assert mock.method() == mock.method()
assert mock.method == mock.method
assert mock.method != mock.method()
# assertで呼ばれている3回分
assert mock.method.call_count == 3
# mock.method()() としない限りcall_countは0
assert mock.method().call_count == 0
assert mock.method().child_method() == mock.method().child_method()
assert mock.method.child_method.call_count == 0
assert mock.method.child_method().call_count == 0
# 上の2回分:assert mock.method().child_method() == mock.method().child_method()
assert mock.method().child_method.call_count == 2
assert mock.method().child_method().call_count == 0
```


#### Mocking dict
* [python \- How to let MagicMock behave like a dict? \- Stack Overflow](https://stackoverflow.com/questions/30340170/how-to-let-magicmock-behave-like-a-dict)

## Reference
