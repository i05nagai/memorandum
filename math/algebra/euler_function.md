---
title: Euler function
---

## Euler function


#### Definition

$\varphi: \mathbb{N} \rightarrow \mathbb{N}$

$$
    \varphi(n)
    :=
    \#
    \{
        k \in \{1, \ldots, n\}
        \mid
        (k, n) = 1
    \}
    .
$$

$\varphi$ is called Euler funciton.

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem
- $n \in \mathbb{N}$,
- $$n = p_{1}^{\alpha_{1}} \cdots p_{k}^{\alpha_{k}}$$,
    - prime factorization of $n$

(1)

$$
    \varphi(n)
    =
    (p_{1}^{\alpha_{1}} - p_{1}^{\alpha_{1} - 1})
    (p_{2}^{\alpha_{2}} - p_{2}^{\alpha_{2} - 1})
    \cdots
    (p_{k}^{\alpha_{k}} - p_{k}^{\alpha_{k} - 1})
    .
$$

(2)

$$
    \varphi(n)
    =
    n \left(
        1 - \frac{1}{p_{1}}
    \right)
    \left(
        1 - \frac{1}{p_{2}}
    \right)
    \cdots
    \left(
        1 - \frac{1}{p_{k}}
    \right)
    .
$$

(3)

$$
    \varphi(p^{\alpha})
    =
    p^{\alpha} - p^{\alpha - 1},
    \
    \varphi(p)
    =
    p - 1
    .
$$

(4) If $(m, n) = 1$,

$$
    \phi(mn)
    =
    \phi(m)\phi(n)
    .
$$

#### proof
(4)

Let $S_{m}, S_{n}, S_{mn}$ be a set of coset representatives.

$$
    S_{m}
    :=
    \{
        0, \ldots, m
    \}
    .
$$

$$
    S_{m}^{*}
    :=
    \{
        k \in S_{m}
        \mid
        (k, m) = 1
    \}
    .
$$

By the Chinese remainder theorem, for any $x \in S_{m}$ and $y \in S_{m}$, there is unique $z \in S_{mn}$ such that

$$
\begin{eqnarray}
    z & \cong & x \ (\mathrm{mod}\ n)
    \nonumber
    \\
    z & \cong & y \ (\mathrm{mod}\ m)
    .
    \nonumber
\end{eqnarray}
$$

Moreover,

$$
    (z, mn) = 1
$$

if and only if

$$
    (x, m) = 1,
    \
    (y, n) = 1.
$$

Indeed, if $x \| m$, $(z, mn) = (x + mk, mn) = x$.

On the other hand, if $(z, mn) = d > 1$, $(z, mn) = (x + mk, mn) = d$.
This implies $d \| m$ or $d \| n$.
If $d \| m$, $(x, m) \neq 1$.
Also, if $d \| n$, $(y, n) \neq 1$.

Therefore,

$$
\begin{eqnarray}
    \varphi(mn)
    & = &
        \#
        \{
            k \in \{1, \ldots, mn\}
            \mid
            (k, mn) = 1
        \}
    \nonumber
    \\
    & = &
        \#
        \{
            k \in \{1, \ldots, mn\}
            \mid
            (k, m) = 1
            \text{ and } (k, n) = 1
        \}
    \nonumber
\end{eqnarray}
$$

(3)

If $p$ is prime, $\varphi(p) = p - 1$.
By the uniqueness of prime factorization, the divisor of $p^{\alpha}$ is only the multiples of $p$.
The number of the multiples of $p$

$$
    |
    \{
        k \in \{1, \ldots, p^{\alpha}\}
        \mid
        (k, p^{\alpha})
        =
        1
    \}
    |
    =
    |\{1, \ldots, p^{\alpha}\} |
    -
    |\{p, 2p, \ldots, p^{\alpha}\}|
    =
    p^{\alpha} - p^{\alpha - 1}
    .
$$


(1)

By (3) and (4),

$$
    \varphi(n)
    =
    \varphi(p_{1}^{\alpha_{1}} \cdots p_{k}^{\alpha_{k}})
    =
    (p_{1}^{\alpha_{1}} - p_{1}^{\alpha_{1} - 1})
    \cdots
    (p_{k}^{\alpha_{k}} - p_{k}^{\alpha_{k} - 1})
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference

