---
title: Enumerative Combinatrics
---

## Enumerative Combinatrics


## Composition
https://en.wikipedia.org/wiki/Composition_%28combinatorics%29

a composition of an integer $n$ is a way of writing $n$ as the sum of a sequence of (strictly) positive integers.
Let $C_{n, k}$ be the number 

$$
\begin{eqnarray}
    C_{n, k}
    & := &
        \#
        \{
            (X_{1}, \ldots, X_{k}) \in \mathbb{N}^{n}
            \mid
            \sum_{i=1}^{k} 
                X_{i}
            =
            n
        \}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                n - 1 \\
                k - 1
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
    .
$$

a weak composition of an integer $n$ is a way of writing $n$ as the sum of a sequence of non-negative integers.

$$
\begin{eqnarray}
    WC_{n, k}
    & := &
        \#
        \{
            (X_{1}, \ldots, X_{k}) \in \mathbb{Z}_{\ge 0}^{n}
            \mid
            \sum_{i=1}^{k}
                X_{i}
            =
            n
        \}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                n + k  - 1 \\
                k - 1
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                n + k  - 1 \\
                n
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
    .
$$

## Reference
- https://en.wikipedia.org/wiki/Enumerative_combinatorics
