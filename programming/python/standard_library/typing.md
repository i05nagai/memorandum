---
title: Typing
---

## Typing
```
from typing import Any

a = None    # type: Any
a = []      # OK
a = 2       # OK

s = ''      # type: str
s = a       # OK
```

## Type annotation

```python
from typing import TypeVar
# T is int or float
T = TypeVar('T', int, float)

def vec2(x: T, y: T) -> List[T]:
    return [x, y]
```


## Reference
* [26.1. typing — Support for type hints — Python 3.6.4 documentation](https://docs.python.org/3/library/typing.html)
* [Sphinx に mypy の type annotation を導入した話 - Hack like a rolling stone](http://tk0miya.hatenablog.com/entry/2016/12/25/195745)
