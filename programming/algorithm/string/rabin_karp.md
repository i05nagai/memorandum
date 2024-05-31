---
title: Rabin-Karp
---

## Rabin-Karp
Multiple pattern search.

Single pttern case

- time complexity
    - worst $O(mn)$ where $n$ is the length of the text and $m$ is the length of pattern.
    - average $O(n)$,
- space complexity 
    - $O(1)$,

Multiple pattern case


## Implementation


```python
class IHashing:

    def do(self, s: str) -> str:
        raise NotImplemented()


class Hashing(IHashing):

    def __init__(self) -> None:
        self.cache = {}
        self.counter = 0

    def do(self, s: str) -> str:
        if s in self.cache:
            return self.cache[s]
        self.cache[s] = str(self.counter)
        self.counter += 1
        return self.cache[s]


class HashingRolling(IHashing):

    M = 131071
    K = 26

    def do(self, s: str) -> str:
        ret = 0
        mult = 1

        for c in s:
            v = ord(c) - ord('a')
            v = v * mult % self.M
            mult *= self.K % self.M
            ret += v % self.M
        return ret


def search_single(s: str, pattern: str, hashing: "Hashing") -> int:
    n = len(s)
    m = len(pattern)
    hash_pattern = hashing.do(pattern)
    for i in range(n - m + 1):
        hash_s = hashing.do(s[i: i + m])
        if hash_s == hash_pattern and s[i: i + m] == pattern:
            return i
    return -1


def search_multiple(s: str, patterns: Set[str], hashing: "Hashing") -> Set[str]:
    n = len(s)
    m = max(len(pattern) for pattern in patterns)
    hashs = set(hashing.do(pattern) for pattern in patterns)
    for i in range(n - m + 1):
        hash_s = hashing.do(s[i: i + m])
        if hash_s in hashs and s[i: i + m] in patterns:
            return i
    return -1


def main():
    hasing = Hashing()
    pattern = "strin"
    text = "astring"
    ret = search_single(text, pattern, hasing)
    print(ret)

    hasing = Hashing()
    patterns = set(["strin", "ri"])
    text = "astring"
    ret = search_multiple(text, patterns, hasing)
    print(ret)

    hasing = HashingRolling()
    pattern = "strin"
    text = "astring"
    ret = search_single(text, pattern, hasing)
    print(ret)

    hasing = HashingRolling()
    patterns = set(["strin", "ri"])
    text = "astring"
    ret = search_multiple(text, patterns, hasing)
    print(ret)


if __name__ == '__main__':
    main()
```


## Reference
- https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
- https://cp-algorithms.com/string/rabin-karp.html
