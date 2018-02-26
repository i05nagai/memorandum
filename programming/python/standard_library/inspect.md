---
title: inspect
---

## inspect


module内のユーザ定義関数を全て取得

```python
import my_module

data = inspect.getmembers(my_module)
data = [v for (k, v) in data if inspect.isfunction(v)]
print(data)
```

## Reference

