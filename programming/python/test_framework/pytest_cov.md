---
title: pytest-cov
---

## pytest-cov
pytest wrapper for coverage plugin.

## Install

```
pip install pytest-cov
```

## Usage

pytest 実行時に`--cov=module_name`オプションをつける

```
pytest --cov=module_name . 
```

更に、`--cov-report`でHTMLのreportを出力してくれる

```
pytest --cov=module_name --cov-report .
```

## Configuration
* [Configuration files — Coverage.py 4.4.1 documentation](http://coverage.readthedocs.io/en/latest/config.html)
    * 細かい設定については、Coverage.pyの設定をみる。

余分なファイルをcoverageの計測から省く場合は、`.coveragerc`に以下のような設定をかく。

```
[run]
omit =
    test_*.py
    .eggs/*
    setup.py
```

## Reference
