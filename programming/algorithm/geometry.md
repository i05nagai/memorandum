---
title: two-dimentional geometry
---

## two-dimentional geometry
Throughout this document, we assume $n = 2$.

#### Definition

* $p \in \mathbb{R}^{n}$,
* $q \in \mathbb{R}^{n}$,

$$
    \langle p, q \rangle
    :=
    \sum_{i=1}^{n}
        p_{i}q_{i}
   .
$$

$$
    p \oplus q
    :=
    p_{1}q_{2}
    -
    p_{2}q_{1}
   .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Property

* $p_{1}, p_{2} \in \mathbb{R}^{n}$,
* $q \in \mathbb{R}^{n}$,
* $q_{1}, q_{2} \in \mathbb{R}^{n}$,

(1) Check whether $q$ is on a line $p_{2} - p_{1}$;

$$
\begin{eqnarray}
    (p_{1} - q)\otimes (p_{2} - q)
    =
    0
\end{eqnarray}
$$

(2) Check whether $q$ is between $p_{2} - p_{1}$;

$$
    \langle
        (p_{1} - q),
        (p_{2} - q)
    \rangle
    \le
    0
    .
$$

(3) A intersection of A line $(p_{1}, p_{2})$ and a line $(q_{1}, q_{2})$ is given by solving the equation w.r.t. $t$;

$$
    (q_{2} - q_{1})
    \otimes
    (p_{1} + t(p_{2} - p_{1}) - q_{1})
    =
    0
    .
$$

The intersection was written as

$$
\begin{eqnarray}
    p_{1}
    +
    \frac{
        (q_{2} - q_{1})
        \otimes
        (q_{1} - p_{1})
    }{
        (q_{2} - q_{1})
        \otimes
        (p_{2} - p_{1})
    }
    (p_{2} - p_{1})
    & = &
        p_{1}
        +
        \frac{
            (q_{2, 1} - q_{1, 1})
            (q_{1, 2} - p_{1, 2})
            -
            (q_{2, 2} - q_{1, 2})
            (q_{1, 1} - p_{1, 1})
        }{
            (q_{2, 1} - q_{1, 1})
            (p_{2, 2} - p_{1, 2})
            -
            (q_{2, 2} - q_{1, 2})
            (p_{2, 1} - p_{1, 1})
        }
        (p_{2} - p_{1})
\end{eqnarray}
$$

Note that the equation cannot detect the case where the both lines are in parallel.
Indeed, if $(p_{2} - p_{1})$ and $(q_{2} - q_{1})$ are in parallel,

$$
    (p_{2} - p_{1})
    \oplus
    (q_{2} - q_{1})
    =
    0
    .
$$

## Reference
