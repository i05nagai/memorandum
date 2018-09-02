---
title: Matrix Operation
---

## Matrix Operation


## Trace Norm

* $A := (a_{i}^{j})_{i,j} \in \mathbb{R}^{n \times n}$,
* $B := (b_{i}^{j})_{i,j} \in \mathbb{R}^{n \times n}$,

$$
\begin{eqnarray}
    A \bullet B
    & := &
        \mathrm{tr}
        \left(
            AB^{\mathrm{T}}
        \right)
    \nonumber
    \\
    & := &
        \mathrm{tr}
        \left(
            BA^{\mathrm{T}}
        \right)
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
        \sum_{j=1}^{n}
            a_{i}^{j}
            b_{i}^{j}
    \nonumber
\end{eqnarray}
$$

We denote $i$-th leargest eignen value by $\lmabda_{i}(A)$.

#### Proposition 1
* $x \in \mathbb{R}^{n}$,

(1)

$$
    \mathrm{tr}
    \left(
        A
    \right)
    =
    \sum_{i=1}^{n}
        \lambda_{i}(A)
$$

(2)

$$
    x^{\mathrm{T}}
    A
    x
    =
    A
    \bullet
    (x x^{\mathrm{T}})
    =
    \mathrm{tr}
    \left(
        A
        (x x^{\mathrm{T}})
    \right)
$$

#### proof
(1)

TODO

(2)

$$
\begin{eqnarray}
    x^{\mathrm{T}}
    A
    x
    & = &
        \sum_{i=1}^{n}
            x^{i}
            a_{i}^{j}
            x_{j}
    \nonumber
    \\
    \mathrm{tr}
    \left(
        A
        x x^{\mathrm{T}}
    \right)
    & = &
        \mathrm{tr}
        \left(
            (a_{j}^{i})_{i,j}
            (x_{j}x^{i})_{i,j}
        \right)
    \nonumber
    \\
    & = &
        \mathrm{tr}
        \left(
            (
                \sum_{k=1}^{n}
                    a_{k}^{i}
                    x_{j}
                    x^{k}
            )_{i,j}
        \right)
    \nonumber
    \\
    & = &
        \sum_{l=1}^{n}
            \sum_{k=1}^{n}
                a_{k}^{l}
                x_{l}
                x^{k}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
