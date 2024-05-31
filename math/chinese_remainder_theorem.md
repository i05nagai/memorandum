---
title: Chinese Remainder Theorem
---

## Chinese Remainder Theorem

#### Proposition
- $n_{1}, \ldots, n_{k}$,
- $n_{i}$ are coprime

If $a \| n_{i}$ for all $i$, $ a \| (n_{1} \cdots n_{k})$.

#### proof
$a = n_{1} m_{1}$ for some $m_{1}$.
$a = n_{1} m_{1} | n_{2}$.
$n_{1}$ and $n_{2}$ are coprime so $m_{1} | n_{2}$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem
- $k \in \mathbb{N}$,
- $n_{1}, \ldots, n_{k} \in \mathbb{N}_{\ge 2}$,
- $a_{1}, \ldots, a_{k} \in \mathbb{Z}$,
- $N := n_{1} \times \cdots \times n_{k}$,

If $a_{i}$ are pairwise coprime, the equation has the unique solution $x$ in modulo $N$.

$$
\begin{eqnarray}
    x & \cong & a_{1} (\mathrm{mod}\ n_{1}) \\
    \vdots & & \\
    x & \cong & a_{n} (\mathrm{mod}\ n_{k})
\end{eqnarray}
$$

Equivalently, there is an isomorphism

$$
    \mathbb{Z}/N
    \equiv
    \mathbb{Z}/n_{1}\mathbb{Z}
    \times
    \cdots
    \times
    \mathbb{Z}/n_{k}\mathbb{Z}
    .
$$

#### proof
(Uniqueness)

Let us assume that there are two solutions $x_{1}$ and $x_{2}$.
For all $i$, there exists $m_{i}$ such that $x_{1} - x_{2} = n_{i} m_{i}$.


(Existence)

Since $n_{1}$ and $n_{2}$ are coprime, there exists two integers $m_{1}$ and $m_{2}$ such that

$$
    m_{1} n_{1} + m_{2} n_{2} = 1.
$$

Let

$$
\begin{eqnarray}
    a_{1, 2}
    :=
    a_{2} m_{1} n_{1}
    +
    a_{1} m_{2} n_{2}
    \label{eq_01_existence_definition}
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    a_{1, 2}
    & = &
        a_{2} m_{1}n_{1}
        +
        a_{1} m_{2}n_{2}
    \nonumber
    \\
    & = &
        a_{2} (1 - m_{2} n_{2})
        +
        a_{1} m_{2}n_{2}
    \nonumber
    \\
    & = &
        a_{2}
        +
        m_{2}n_{2}(a_{1} - a_{2})
    \nonumber
\end{eqnarray}
$$

implying that $a_{1,2} | n_{2}$ and similarly $a_{1, 2} | n_{1}$.
Now, we can reduce the equation size to $k - 1$ by defining

$$
    x \cong a_{1,2} (\mathrm{mod}\ n_{1}n_{2}).
$$

$n_{1} n_{2}$ is pairwise coprime with $n_{3}, \ldots, n_{k}$.
Hence if we can proove the state with $k=2$, the statement holds by induction.
However, this has been shown by $$\eqref{eq_01_existence_definition}$$.


<div class="QED" style="text-align: right">$\Box$</div>

## Reference
- https://en.wikipedia.org/wiki/Chinese_remainder_theorem
