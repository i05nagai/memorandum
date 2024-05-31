---
title: Countign Sort
---

## Countign Sort


```
class IKey:

    def get(self, val):
        raise NotImplemented()

    def size(self):
        raise NotImplemented()


class Key1(IKey):

    def __init__(self, array):
        self._size = len(array)

    def get(self, val):
        return val

    def size(self):
        return self._size


class Key2(IKey):

    def __init__(self, array):
        self._array = array
        self._min = min(array)
        self._max = max(array)

    def get(self, val):
        return val - self._min

    def size(self):
        return self._max - self._min


def sort(array, get_key, key_size):
    count = [0] * (key_size + 1)
    output = [-1] * len(array)

    for i in range(len(array)):
        j = get_key(array[i])
        count[j] += 1

    # cumulative sum
    for i in range(1, key_size + 1):
        count[i] += count[i - 1]

    for i in reversed(range(0, len(array))):
        j = get_key(array[i])
        count[j] -= 1
        output[count[j]] = array[i]

    return output
```

## Reference
* [Counting Sort \- GeeksforGeeks](https://www.geeksforgeeks.org/counting-sort/)
* [Counting sort \- Wikipedia](https://en.wikipedia.org/wiki/Counting_sort)
