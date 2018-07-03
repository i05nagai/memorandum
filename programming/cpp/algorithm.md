---
title: algorithm
---

## algorithm



`upper_bound()`

An iterator to the upper bound position for val in the range.
If no element in the range compares greater than val, the function returns last.

```
std::upper_bound();
```

`lower_bound()`

Returns an iterator pointing to the first element in the range [first,last) which does not compare less than val.
If all the element in the range compare less than val, the function returns last.

$$
\begin{eqnarray}
    A_{v}
    & := &
        \{
            a \in A
            \mid
            v \ge a
        \}
    \nonumber
    \\
    \begin{cases}
        \max A
        &
            (A_{v} = \emptyset)
        \\
        \min A_{v}
        &
            (\text{otherwise})
    \end{cases}
\end{eqnarray}
$$

```
std::lower_bound();
```

[binary_search - C++ Reference](http://www.cplusplus.com/reference/algorithm/binary_search/)

std::binary_saerch();

## Reference
