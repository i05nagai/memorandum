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
