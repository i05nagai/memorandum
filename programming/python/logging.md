---
title: logging
---

## logging
Defaultではconsoleに出力される。
fileに出力するように変更することもできる。


```python
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
```

## Logging level

* CRITICAL
    * 50
* ERROR
    * 40
* WARNING
    * 30
* INFO
    * 20
* DEBUG
    * 10
* NOTSET
    * 0

## Reference
* [15.7. logging — Logging facility for Python — Python 2.7.14 documentation](https://docs.python.org/2/library/logging.html)
