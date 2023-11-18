---
title: Euclidean Geometry
---

## Euclidean Geometry

#### Definition Inner Product
- $a, b \in \mathbb{R}^{n}$,

$$
    \langle a, b \rangle
    :=
    a \cdot b
    :=
    \sum_{i=1}^{n}
        a_{i}b_{i}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Outer Product
- $a \in \mathbb{R}^{m}$,
- $b \in \mathbb{R}^{n}$,

$$
\begin{eqnarray}
    a \times b
    & := &
        \left(
            \begin{array}{c}
                a_{1}
                \\
                \vdots 
                \\
                a_{m}
            \end{array}
        \right)
        \times
        \left(
            \begin{array}{c}
                b_{1}
                \\
                \vdots 
                \\
                b_{n}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                a_{1}
                \\
                \vdots 
                \\
                a_{m}
            \end{array}
        \right)
        \times
        \left(
            \begin{array}{c}
                b_{1}
                \\
                \vdots 
                \\
                b_{n}
            \end{array}
        \right)^{T}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cccc}
                a_{1}b_{1} & a_{1}b_{2} \cdots & a_{1}b_{m}
                & & & 
                a_{n}b_{1} & a_{n}b_{2} \cdots & a_{n}b_{m}
            \end{array}
        \right)
    \nonumber
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>


## Reference
- https://en.wikipedia.org/wiki/Outer_product
