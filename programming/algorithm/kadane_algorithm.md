---
title: Kadane Algorithm
---

## Kadane Algorithm
An algorithm to find the maximum subarray.

#### Problem
Let

* $(A_{i})_{i=1,\ldots,N}$,
    * give narray

Find

$$
    B
    :=
    \max
    \{
        \sum_{i=j_{1}}^{j_{2}}
            A_{i}
        \mid
        1
        \le
        j_{1} \le j_{2}
        \le
        N
    \}
    .
$$

#### How to find?

It is easy to see

$$
\begin{eqnarray}
    B_{k}
    & := &
        \max
        \{
            \sum_{i=j}^{k}
                A_{i}
            \mid
            j \in \{1, \ldots, n\}
        \}
    \nonumber
    \\
    j_{k}^{*}
    & := &
        \max
        \{
            j^{*} \in \{1, \ldots, k\}
            \mid
            \sum_{i=j^{*}}^{k}
                A_{i}
            =
            B_{k}
        \}
    \nonumber
    \\
    B_{k}
    & = &
        \sum_{i=j_{k}^{*}}^{k}
            A_{i}
    \nonumber
    \\
    B
    & = &
        \max_{k = 1, \ldots, N}
            B_{k}
    .
    \nonumber
\end{eqnarray}
    .
$$

Fotunately, $B_{k}$ can be computed by $C_{k}$ defined by

$$
\begin{eqnarray}
    B_{1}
    & = &
        A_{1}
        =:
        C_{1}
    \nonumber
    \\
    B_{k + 1}
    & = &
        \max
        \{
            A_{k + 1},
            A_{k + 1} + B_{k}
        \}
        =:
        C_{k + 1}
    .
    \nonumber
\end{eqnarray}
$$

Indeed, $B_{1} = C_{1}$ is obvious.
Suppose that the equation holds up to $k$.
By definition,

$$
\begin{eqnarray}
    B_{k + 1}
    & = &
        \sum_{i=j_{k + 1}^{*}}^{k + 1}
            A_{i}
    \nonumber
    \\
    & = &
        \sum_{i=j_{k + 1}^{*}}^{k}
            A_{i}
        +
        A_{k + 1}
    \nonumber
    \\
    & = &
        \begin{cases}
            \sum_{i=j_{k + 1}^{*}}^{k}
                A_{i}
            +
            A_{k + 1}
            &
                (j_{k + 1}^{*} < k + 1)
            \\
            A_{k + 1}
            &
                (j_{k + 1}^{*} = k + 1)
        \end{cases}
    \nonumber
    \\
    & \le &
        \begin{cases}
            B_{k}
            +
            A_{k + 1}
            &
                (j_{k + 1}^{*} < k + 1)
            \\
            A_{k + 1}
            &
                (j_{k + 1}^{*} = k + 1)
        \end{cases}
    \nonumber
    \\
    & \le &
        C_{k + 1}
    \nonumber
\end{eqnarray}
$$

If $0 < B_{k}$,

$$
\begin{eqnarray}
    C_{k + 1}
    & = &
        B_{k}
        +
        A_{k + 1}
    \nonumber
    \\
    & = &
        \sum_{i=j_{k}^{*}}^{k+1}
            A_{i}
    \nonumber
    \\
    & \le &
        B_{k + 1}
    \nonumber
\end{eqnarray}
$$

If $0 \ge B_{k}$,

$$
\begin{eqnarray}
    C_{k + 1}
    & = &
        A_{k + 1}
    \nonumber
    \\
    & = &
        \sum_{i=k+1}^{k+1}
            A_{i}
    \nonumber
    \\
    & \le &
        B_{k + 1}
    .
    \nonumber
\end{eqnarray}
$$

Hence $B_{k + 1} = C_{k + 1}$.
$C_{k}$ can be computed in $O(N)$.


```python
def max_subarray(A):
     ck = A[0]
     max_ck = ck
    for x in A[1:]:
        ck = max(x, ck + x)
        max_ck = max(max_ck, ck)
    return max_ck
```

#### Remark
* The algorithm is a variety of an application of dynamic programming interpreting $C_{k}$ as memoization.


## Reference
* [Maximum subarray problem \- Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
