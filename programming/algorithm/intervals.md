---
title: Intervals
---

## Intervals


## Check overlap

```python
def has_overlap(a, b):
    return (min(a[1], b[1]) - max(a[0], b[0])) >= 0

a = [1, 2]
b = [2, 3]
has_overlap(a, b)
```

## Merge intervals

```python
def merge(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

a = [1, 2]
b = [2, 3]
merge(a, b)
```

## Number of overlaps

```python
def number_of_overlaps(intervals):
    data = []
    for (s, e) in intervals:
        data.append((s, '1'))
        data.append((e, '2'))
    count = 0
    ret = 0
    for (t, ty) in sorted(intervals)
        if ty == '1':
            count += 1
        if ty == '2':
            count -= 1
        ret = max(ret, count)
    return count

a = [1, 2]
b = [2, 3]
data = [a, b]
number_of_overlaps(data)
```

## Reference
