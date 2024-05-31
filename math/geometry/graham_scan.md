---
title: Graham Scan
---

## Graham Scan
Make the convex hull from given 2D points.

- $n$: the number of points
- Time Compelxity: $O(n \log n)$,
- Space Complexity: $O(n)$,

```python
import functools


def cross_product(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def is_counter_clock_wise(p1, p2, p3):
    p = (p2[0] - p1[0], p2[1] - p1[1])
    q = (p3[0] - p2[0], p3[1] - p2[1])
    return cross_product(p, q) <= 0


def graham_scan(points):
    def cmp(p, q):
        if p[0] != q[0]:
            return p[0] < q[0]
        return p[1] < q[1]

    ret = []
    points.sort(key=functools.cmp_to_key(cmp))
    convex_hull = []
    for i in range(len(points)):
        while len(convex_hull) > 1 and is_counter_clock_wise(convex_hull[-2], convex_hull[-1], points[i]):
            convex_hull.pop()
        convex_hull.append(points[i])

    t = len(convex_hull)
    for i in reversed(range(len(points) - 1)):
        while len(convex_hull) > t and is_counter_clock_wise(convex_hull[-2], convex_hull[-1], points[i]):
            convex_hull.pop()
        convex_hull.append(points[i])
    return convex_hull
```

## Reference
- https://en.wikipedia.org/wiki/Graham_scan
