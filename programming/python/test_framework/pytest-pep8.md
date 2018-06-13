---
title: pytest-pep8
---

## pytest-pep8

```
pip install pytest-pep8
```

pytsetでpep8の確認ができる。
pytest実行時に`--pep8`をつける。

```
pytest --pep8 .
```

## Settings
pytestの設定がかける場所に、pep8の設定もかける。



### Ignore pep8
`setup.cfg`に以下のようにかくと無視したい警告を記載できる。

```cfg
[tool:pytest]
pep8ignore = E201 E231
```

* `W503`
    * line break before binary operator

## Reference
* [pytest-pep8 1.0.6 : Python Package Index](https://pypi.python.org/pypi/pytest-pep8)

