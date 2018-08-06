---
title: algorithm
---

## algorithm



`upper_bound()`

An iterator to the upper bound position for val in the range.
If no element in the range compares greater than val, the function returns last.

* If $v \ge a$ for all $a \in A$, return the iterator pointing after the last element
* Otherwise, returns the iterator of the maximum value which satisfies $v < a$,

$$
\begin{eqnarray}
    A_{v}
    & := &
        \{
            a \in A
            \mid
            v < a
        \}
    \nonumber
    \\
    \mathrm{UpperBound}(v)
    & := &
        \begin{cases}
            ?
            &
                (A_{v} = \emptyset)
            \\
            \min A_{v}
            &
                (\text{otherwise})
        \end{cases}
    \nonumber
\end{eqnarray}
$$


`lower_bound()`

Returns an iterator pointing to the first element in the range [first,last) which does not compare less than val.
If all the element in the range compare less than val, the function returns last.

Supporse $A$ is sorted array.
Search the point at which given value $v$ is the lower bound.

* If $v > a$ for all $a \in A$, return the iterator pointing after the last element
    * the iterator does not point any value of $A$,
* Otherwise, returns the iterator of the minimum value which satisfies $v \le a$,

$$
\begin{eqnarray}
    A_{v}
    & := &
        \{
            a \in A
            \mid
            v \le a
        \}
    \nonumber
    \\
    \mathrm{LowerBound}(v)
    & := &
        \begin{cases}
            ?
            &
                (A_{v} = \emptyset)
            \\
            \min A_{v}
            &
                (\text{otherwise})
        \end{cases}
    \nonumber
\end{eqnarray}
$$

```cpp
void lb(const int v) {
    std::vector<int> data = { 1, 2, 3, 4, 5, 6, };
    auto l = std::lower_bound(data.begin(), data.end(), v);
    const int index = l - data.begin();
    const int value = *l;
    std::cout << index << ", " << value << std::endl;
}
// 0, 1
lb(0);
// 6, ? (because 6 is out of range, value is undetermined)
lb(7);
// 2, 3
lb(3);
```


`bool binary_saerch();`

Returns true if the value exists within the range [first, lasrt).

## Reference
* [binary_search - C++ Reference](http://www.cplusplus.com/reference/algorithm/binary_search/)
* [std::upper\_bound \- cppreference\.com](https://en.cppreference.com/w/cpp/algorithm/upper_bound)
* [std::lower\_bound \- cppreference\.com](https://en.cppreference.com/w/cpp/algorithm/lower_bound)
* [std::binary\_search \- cppreference\.com](https://en.cppreference.com/w/cpp/algorithm/binary_search)
