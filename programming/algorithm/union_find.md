---
title: Union Find
---

## Union Find


## Implementation

```python
class UnionFind:

    def __init__(self, nums):
        self.maps = {num: i for i, num in enumerate(nums)}
        self.data = [i for i in range(len(nums))]
        self.heights = [0 for i in range(len(nums))]

    def union(self, x, y):
        x = self.maps[x]
        y = self.maps[y]
        root_x = self._find(x)
        root_y = self._find(y)
        if root_x == root_y:
            return
        if self.heights[root_x] < self.heights[root_y]:
            self.data[root_x] = root_y
        else:
            self.data[root_y] = root_x
            if self.heights[root_x] == self.heights[root_y]:
                self.heights[root_x] += 1

    def _find(self, x):
        if x == self.data[x]:
            return x
        self.data[x] = self._find(self.data[x])
        return self.data[x]

    def find(self, x):
        x = self.maps[x]
        return self._find(x)

    def same(self, x, y):
        a = self.find(x)
        b = self.find(y)
        return a == b
```

## Time complexity
- https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Proof_of_O(m_log*_n)_time_complexity_of_Union-Find



## Reference

