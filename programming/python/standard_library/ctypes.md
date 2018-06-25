---
title: ctypes
---

## ctypes

```
import ctypes

ctypes.libc.printf
```


Union

```
import ctypes
class POINT(ctypes.Structure):

    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
```

* `ctypes.pointer()`

## Reference
* [16\.16\. ctypes — A foreign function library for Python — Python 3\.6\.6rc1 documentation](https://docs.python.org/3/library/ctypes.html)
