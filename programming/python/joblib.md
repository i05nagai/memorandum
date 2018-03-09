---
title: joblib
---

## joblib

```
pip install joblib
```


```python
from math import sqrt
from joblib import Parallel, delayed
Parallel(n_jobs=2)(delayed(sqrt)(i ** 2) for i in range(10))
```

## Reference
* [joblib/joblib: Python function as pipeline jobs.](https://github.com/joblib/joblib)
* [[Python] Joblibでお手軽並列処理 - Qiita](https://qiita.com/Yuhsak/items/1e8533343cf5458e2e08)
