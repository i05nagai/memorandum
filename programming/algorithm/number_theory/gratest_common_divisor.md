---
title: Greatest Common Divisor
---

## Greatest Common Divisor

#### Two variabels
Time complexity: $O(\log b)$,

```python
def gcd(a, b):
    assert a >= b
    if b == 0:
        return a
    return gcd(b, a % b)
```

Note that $a \% b  \le \frac{a}{2}$.
Indeed, $a \% b \ge b$ by definition.
Also, sine $a = bq + r$ where $q >= 0$ and $0 <= r < b$,

$$
\begin{eqnarray}
    r
    & = &
        a - bq
    \nonumber
    \\
    & \le &
        a - b
    .
    \nonumber
\end{eqnarray}
$$

If $b \le a / 2$, by the first inequality $a \% b \le \frac{a}{2}$.

If $b \ge a / 2$, by the second inequality $a \% b \le \frac{a}{2}$.

#### Multiple variables


## Reference
- https://codeforces.com/blog/entry/63771
