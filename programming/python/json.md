## json


## Pretty print
整形して出力する場合は


```python
import json

data = {}
json.dump(data, f, indent=True, separators=(",", ":"))
```
