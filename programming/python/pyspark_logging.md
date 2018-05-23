---
title: PySpark Logging
---

## PySpark Logging
Get logger.

```python
def get_logger(sc, name):
    """get_logger

    :param name:

    Example
    ========

    >>> logger = get_logger(sc, __name__)
    >>> logger.info("pyspark script logger initialized")
    """
    log4j = sc._jvm.org.apache.log4j
    return log4j.LogManager.getLogger(name)
```

## Reference
* [logging - How do I log from my Python Spark script - Stack Overflow](https://stackoverflow.com/questions/25407550/how-do-i-log-from-my-python-spark-script)
