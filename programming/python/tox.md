# tox

```ini
[testenv]
deps=
    nose
    numpy
changedir={envdir}
commands=python {toxinidir}/run_test_script.py args
```

## Usage

## Reference
* [複数バージョンのPython向けにCI環境を構築してテストする - Qiita](http://qiita.com/giginet/items/1f965ba6d8077f6399b8)
* [tox configuration specification — tox 2.5.0.dev1 documentation](http://tox.readthedocs.io/en/latest/config.html)
