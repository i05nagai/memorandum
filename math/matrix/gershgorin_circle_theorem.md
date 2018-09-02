---
title: Gershgorin Circle Theorem
---

## Gershgorin Circle Theorem


#### Thorem
* $A ;= (a_{j}^{i}) \in \mathbb{C}^{n \times n}$,
    * matrix
* $D(a_{j}^{i}, R_{i}) \subseteq \mathbb{C}$,
    * circle with radius $R_{i}$ at 
* $\lambda_{i} \in \mathbb{C}$,
    * the $i$-th largest eigenvalue of $A$,

$$
    R_{i}
    :=
    \sum_{j\neq i}
        |a_{j}^{i}|
    .
$$

For all $i$,

$$
    \exists j \in \{1, \ldots, n\},
    \text{ s.t. }
    \lambda_{i}
    \in
    D(a_{j}^{j}, R_{j})
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition

#### proof

(1)

$$
\begin{eqnarray}
    |
        \lambda
    |
        -
    |
        a_{i}
    |
    & \le &
        |
            \lambda
            -
            a_{i}
        |
    \nonumber
    \\
    & \le &
        R_{i}
    \nonumber
\end{eqnarray}
$$

Thus

$$
\begin{eqnarray}
    |
        \lambda
    |
    & \le &
        \sum_{i=1}^{n}
            |a_{i}|
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [Gershgorin circle theorem \- Wikipedia](https://en.wikipedia.org/wiki/Gershgorin_circle_theorem)
