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

logging to file

```python
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
```

日付のformat変更

```python
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
```

loggerはinstanceの名前の`.`に対応した親子関係を持つ。
つまり、`scan`は`scan.text`の親になる。
よく使われる方法は、moduleのpathをloggerの名前にする。

```python
logger = logging.getLogger(__name__)
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

## When

* CLIの画面表示
    * print()
* 通常の処理内でのeventのreport
    * e.g.
        * fault investigation
        * status monitoring
    * logging.info()
    * logging.debug()
        * debug用の詳細な出力時
* 特定のruntime eventに対するwarning
    * logging.warn()
        * 対処可能なwarning
    * logging.warning()
        * 対処不能なwarningに対して
* 特定のruntime eventに対するerror
    * raise exeption
* 例外を投げずに、errorを抑制した場合の通知
    * logging.error()
    * logging.exception()
    * logging.critical()

## Configuration
* [15.8. logging.config — Logging configuration — Python 2.7.14 documentation](https://docs.python.org/2/library/logging.config.html)

dict形式でconfigurationできる。

https://docs.python.org/2/library/logging.config.html#logging-config-dictschema

```
handlers:
  console:
    class : logging.StreamHandler
    formatter: brief
    level   : INFO
    filters: [allow_foo]
    stream  : ext://sys.stdout
  file:
    class : logging.handlers.RotatingFileHandler
    formatter: precise
    filename: logconfig.log
    maxBytes: 1024
    backupCount: 3
```


## Reference
* [15.7. logging — Logging facility for Python — Python 2.7.14 documentation](https://docs.python.org/2/library/logging.html)
