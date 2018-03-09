---
title: python-json-logger
---

## python-json-logger

```
pip install python-json-logger
```

## Usage

```python
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
```

## Reference
* [madzak/python-json-logger: Json Formatter for the standard python logger](https://github.com/madzak/python-json-logger)
