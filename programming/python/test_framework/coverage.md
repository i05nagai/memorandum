---
tilte: coverage
---

# coverage
python package for code coverage.

```
pip install coverage
```

## Integration with unit testing frameworks
* for py.test

```
pip install pytest-cov
```

* for nosetests

## Configuration
`.coveragerc`ファイルに設定を書く。
iniフォーマットで記載。

### [run]


```
[run]
include = path/to/include/sources
omit = omit_pattern
```


### Reference
* [Configuration files — Coverage.py 4.0.3 documentation](http://coverage.readthedocs.org/en/coverage-4.0.3/config.html)


## Reference
* [Coverage.py — Coverage.py 4.0.3 documentation](http://coverage.readthedocs.org/en/coverage-4.0.3/)


