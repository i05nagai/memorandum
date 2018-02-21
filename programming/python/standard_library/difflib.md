---
title: difflib
---

## difflib

HtmlDiff

context_diff

* unified_diff
    * `fromfile`, `tofile`
        * diffの表示に指定するfilename

```python
>>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
>>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
>>> for line in difflib.unified_diff(s1, s2, fromfile='before.py', tofile='after.py'):
...     sys.stdout.write(line)   
--- before.py
+++ after.py
@@ -1,4 +1,4 @@
-bacon
-eggs
-ham
+python
+eggy
+hamster
 guido
```

## Reference
* [7.4. difflib — Helpers for computing deltas — Python 2.7.14 documentation](https://docs.python.org/2/library/difflib.html)
