---
title: Segment tree
---

## Segment tree
In computer science, a segment tree also known as a statistic tree is a tree data structure used for storing information about intervals, or segments.

* $n$,
    * the number of intervals
* $$J_{i} := [q_{i,1}, q_{i,2}]$$,
    * $i$-th interval
* $$(p_{1}, \ldots, p_{2n})$$,
* $ k := \lfloor \log_{2}(2n) \rfloor + 1$,
    * height of tree
* $O(n)$,
    * storage complexity

Indeed,

$$
\begin{eqnarray}
    \sum_{i=1}^{k}
        \frac{
            2n
        }{
            2^{i-1}
        }
    & = &
        \sum_{i=1}^{k}
            2n
            2^{-(i-1)}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{k}
            2n
            2^{(i-1)-(k-1)}
    \nonumber
    \\
    & = &
        2^{-(k-1)}
        2n
        \sum_{i=1}^{k}
            2^{(i-1)}
    \nonumber
    \\
    & = &
        2^{-(k-1)}
        2n
        \frac{
            1 - 2^{k}
        }{
            1 - 2
        }
    \nonumber
    \\
    & = &
        2^{-(k-1)}
        2n
        (2^{k} - 1)
\end{eqnarray}
$$


* $O(n \log n)$ to build
* $O(\log n)$ for update
* $O(\log n)$ for query


## Implementation
Min query


```python
class SegmentTree:

    def __init__(self, n: int):
        self.n = self._first_power_of_two(n)
        self.data = [math.inf] * 2 * self.n

    def _first_power_of_two(self, n: int) -> int:
        size = 1
        while size < n:
            size *= 2
        return size

    def initialize(self, array: List[int]):
        self.n = self._first_power_of_two(len(array))
        self.data = [math.inf] * 2 * self.n
        for i in range(len(array)):
            self.update(i, array[i])

    def update(self, index: int, val: int) -> None:
        index += self.n - 1
        self.data[index] = val
        while index > 0:
            index = (index - 1) // 2
            self.data[index] = min(self.data[index * 2 + 1], self.data[index * 2 + 2])

    def _query(self, left: int, right: int, index: int, l: int, r: int) -> int:
        if right <= l or r <= left:
            return math.inf
        if left <= l and r <= right:
            return self.data[index]

        vl = self._query(left, right, 2 * index + 1, l, (l + r) // 2)
        vr = self._query(left, right, 2 * index + 2, (l + r) // 2, r)
        return min(vl, vr)

    def query(self, left, right):
        # min value in [left, right)
        return self._query(left, right, 0, 0, self.n)
```

## Reference
* [Segment tree - Wikipedia](https://en.wikipedia.org/wiki/Segment_tree)
* [Microsoft PowerPoint - tutorial-stabbing.ppt](http://www.cs.nthu.edu.tw/~wkhon/ds/ds10/tutorial/tutorial6.pdf)
