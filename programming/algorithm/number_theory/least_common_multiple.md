---
title: Least Common Multiple
---

## Least Common Multiple


#### Two variables

- Time complexity: $O(\log b)$.
    - because GCD Is $O(\log b)$.

```python
def gcd(a, b):
    assert a >= b
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)
```

#### Multiple variables

```python
import functools

def lcm(array):
    return functools.reduce(lambda a, b: a * b / gcd(a, b, array))
```

## Reference
