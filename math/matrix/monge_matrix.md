---
title: Monge
---

## Monge


#### Definition Monge
- $A = (a_{r}^{c})$,
    - $m \times n$ matrix

$A$ is said to be Monge if

$$
    \forall i, j \in \mathbb{N},
    \
    i \in [1, m],
    \
    j \in [1, n],
    \
    a_{i}^{j}
    +
    a_{i+1}^{j+1}
    \ge
    a_{i}^{j+1}
    +
    a_{i+1}^{j}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Monotone
- $A = (a_{i}^{j})$,

$\forall i = 1, \ldots, m - 1, j = 1, \ldots, n - 1$, every $2 \times 2$ submatrix

$$
    \left(
        \begin{array}{cc}
            a_{i}^{j} & a_{i}^{j+1} \\
            a_{i+1}^{j} & a_{i+1}^{j+1}
        \end{array}
    \right)
$$

does not hold both inequalities simultaneously

$$
    a < b,
    \
    c \ge d.
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 1
- $A = (a_{i}^{h})$

If a matrix is Monge, a matrix is monotone.

#### proof
We give a proof by induction.
Let us start with $A$ is $2 \times 2$ matrix.
If $a_{1}^{1} < a_{1}^{2}$, by Monge property,

$$
    a_{1}^{1}
    +
    a_{2}^{2}
    \ge
    a_{2}^{1}
    +
    a_{1}^{2}
$$

implies $a_{2}^{2} \ge a_{2}^{1}$.

Now Let us assume that the statement hold up to $n - 1$ and $m - 1$.
We prove the statement for $m \times n$ matrix.
We just need to prove that every submatrix 

$$
    \left(
        \begin{array}{cc}
            a_{m-1}^{j} & a_{m-1}^{j+1}
            \\
            a_{m}^{j} & a_{m}^{j+1}
        \end{array}
    \right)
    \quad
    (\forall j = 1, \ldots, n-1)
$$

and

$$
    \left(
        \begin{array}{cc}
            a_{i}^{n-1} & a_{i}^{n}
            \\
            a_{i+1}^{n} & a_{i+1}^{n}
        \end{array}
    \right)
    \quad
    (\forall i = 1, \ldots, m-1)
$$

is monotone.
Obviously, Monge property holds for the submatrixes.
Thus, the submatrixes are monotone.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
- https://home.cse.ust.hk/~golin/COMP572/Notes/SMAWK.pdf
