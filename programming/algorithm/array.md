---
title: Array
---

## Array

## Operations

```
x 1 2 3
1 x 4 5
2 4 x 6
3 5 6 x
```

```cpp
for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
        m[i][j] == m[j][i];
    }
}

```


```
0 1 2 3
1 4 5 6
2 5 7 8
3 6 8 9
```

```cpp
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
        m[i][j] == m[j][i];
    }
}
```


```
0 1 2 3
1 4 5 6
2 5 7 8
3 6 8 9
```

```cpp
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
        m[i][j] == m[j][i];
    }
}
```

transpose

```
0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15

0  4  8  12
1  5  9  13
2  6  10 14
3  7  11 15
```

```cpp
for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
        swap(m[i][j], m[j][i])
    }
}
```

reverse

```
0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15

3  1  2  0
7  6  5  4
11 10 9  8
15 14 13 12
```

```cpp
for (int i = 0; i < (int)(n / 2); i++) {
    for (int j = 0; j < n; j++) {
        swap(m[j][i], m[j][n - i - 1])
    }
}
```

rorate anticlockwise by 90 degree

```cpp
vector<vector<int>> m2()
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        m2[(n - 1) - j][i] = m[i][j];
    }
}
m = m2;
```

rorate clockwise by 90 degree

```cpp
vector<vector<int>> m2()
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        m2[j][(n - 1) - i] = m[i][j];
    }
}
m = m2;
```

rorate clockwise by 90 degree in place

```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        m2[(n - 1) - j][i] = m[i][j];
    }
}
```

## Reference
* [Array data structure - Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure)
