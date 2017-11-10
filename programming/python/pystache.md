---
title: Pystache
---

## Pystache

```
pip install pystache
```

## Usage

```python
import pystache
print pystache.render('Hi {{person}}!', {'person': 'Mom'})
```

環境変数を展開する

```python
import pystache
import os
pystache.render('{{PATH}}', dict(os.environ))
```

## Reference
* [defunkt/pystache: Mustache in Python](https://github.com/defunkt/pystache)
