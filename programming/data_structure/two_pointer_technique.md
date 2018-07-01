---
title: Two Pointer Technique
---

## Two Pointer Technique
* $a_{0}, \ldots, a_{n-1}$,
    * $a_{i} \in \mathbb{N}$,
* $S \in \mathbb{N}$,

Let $I(s)$ be the first index after $s$ to which summation from $i$ is over S.

$$
    I(s)
    :=
    \arg\min
        \{
            j \ge s
            \mid
            \sum_{j=s:i}
                a_{j}
            \ge
            S
        \}
$$

Then

$$
    \sum_{i = s+1:I(s)-1}
        a_{i}
    <
    \sum_{i = s:I(s)-1}
        a_{i}
    <
    S
    .
$$

Thus,

$$
\begin{equation}
    I(s)
    \le
    I(s+1)
    \label{two_pointer_technique_relation}
\end{equation}
    .
$$

The problem is to find

$$
    \min\{
        I(s) - s
        \mid
        s \in [0:n)
    \}
    .
$$

Since $$\eqref{two_pointer_technique_relation}$$, if we find $I(s)$, $I(s+1)$ is in $[I(s), n)$.

## Reference
* [Two Pointers Technique - GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)
