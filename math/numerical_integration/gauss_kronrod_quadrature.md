---
title: Gauss-Kronrod Quadrature
---

## Gauss-Kronrod Quadrature

$$
\begin{eqnarray}
    I
    & := & 
        \int_{a}^{b}
            f(x)
        \ dx
    \nonumber
    \\
    & \approx &
        \sum_{i=1}^{n}
            f(x_{i})
            w(x_{i})
        +
        \sum_{i=1}^{2 n}
            f(x_{i})
            w(x_{i})
    \nonumber
\end{eqnarray}
$$

Let $F_{n + 2p -1} \in \Pi_{n + 2p -1}$ be polynomial of degree $n + 2p - 1$.
There exist $Q_{n + p -1} \in \Pi_{n + p -1}$, $G_{n + p} \in \Pi_{n + p}$, and $c_{k} \in \mathbb{R}$ such that

$$
\begin{eqnarray}
    F_{n + 2p -1}(x)
    =
    Q_{n+p-1}(x)
    +
    G_{n+p)(x)
    \sum_{k=0}^{p-1}
        c_{k} x^{k}
    .
\end{eqnarray}
$$

$Q_{n+p-1}$ can be integrated by $(n + p)$ point Gauss quadrature.
If $G_{n+p}$ has a property:

$$
    \int_{-1}^{1}
        G_{n+p}(x)
        x^{k}
    \ dx,
    \
    k = 0, \ldots, p - 1
    ,
$$

$F_{n + 2p - 1}$ can be integrated by $(n + p)$ points Gauss quadrature.

Kronrod consider that the case $p = n + 1$ for the $n$ pointgs Gauss quadrature.
Instad of using a polynomial, Kronrod uses multiplication of a polynomial $K_{n+1}(x) \in \Pi_{n+1}$ and the Ledgendre polynoamial $P_{n}(x)$.

$$
\begin{eqnarray}
    \int_{-1}^{1}
        K_{n+1}(x)
        P_{n}(x)
        x^{k}
    \ dx
    ,
    k = 0, 1, \ldots, n
\end{eqnarray}
$$

Kronrod determiens coefficients of $K_{n+1}$ and its zeros by substituting polynomial expression of $K_{n}$ into above equation.
In particular, $G_{2n}$ has the same zeros as the $n$ Guass-Ledgendre quadrature.


## Reference
* [Gauss–Kronrod quadrature formula \- Wikipedia](https://en.wikipedia.org/wiki/Gauss%E2%80%93Kronrod_quadrature_formula)
