---
title: Modulo
---

## Modulo

#### Proposition 1

If $a \equiv b \ (\mathrm{mod}\ N)$, for any $k \in \mathbb{Z}$

$$
    a \equiv b + Nk \ (\mathrm{mod}\ N)
    .
$$

#### proof
$a - b = Nq$ for some $q \in \mathbb{Z}$.

$$
    a - b - Nk = N(q - k)
    .
$$

Hence

$$
    a \equiv b + Nk\ (\mathrm{mod}\ N)
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 2
If $ac \equiv bc \ (\mathrm{mod}\ N)$ and $(c, N) = 1$,

$$
    a \equiv b \ (\mathrm{mod}\ N)
    .
$$

#### proof
$ac - bc = Nq$ for some $q \in \mathbb{Z}$.
The left hand side is divisble by $c$. So does the right hand side.
However, $(c, N) = 1$ implies that $c \mid k$.

$$
    a \equiv b\ (\mathrm{mod}\ N)
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 3
If $a \equiv b \ (\mathrm{mod}\ N)$, for all $k \in \mathbb{Z}$,

$$
    ak \equiv bk \ (\mathrm{mod}\ Nk)
    .
$$

#### proof

$$
    a - b = N q
$$

for some $q \in \mathbb{Z}$.

$$
    ak - bk = Nk q
$$

shows

$$
    ak \equiv bk\ (\mathrm{mod}\ Nk)
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 4
If $a \equiv b \ (\mathrm{mod}\ N)$ and $d$ is a common divisor of $a, b, N$,

$$
    a_{1} \equiv b_{1} \ (\mathrm{mod}\ N_{1})
$$

where $a = a_{1} d$, $b = b_{1} d$, $N = N_{1} d$.

#### proof

$$
    a - b = N q
$$

for some $q \in \mathbb{Z}$.

$$
    a_{1}d - b_{1}d = N_{1}d q
    \Leftrightarrow
    a_{1} - b_{1} = N_{1} q
    .
$$

Hence $a_{1} \equiv b_{1}\ (\mathrm{mod}\ N_{1})$

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 5
If $a \equiv b \ (\mathrm{mod}\ N)$ and there is a positive interger $d$ such that $N = dN_{1}$,

$$
    a \equiv b \ (\mathrm{mod}\ d)
    .
$$

#### proof
$a - b = Nq$ for some $q \in \mathbb{Z}$.

$$
    a - b = (N_{1}q) d
    .
$$

That is, $a \equiv b\ (\mathrm{mod}\ d)$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 6
If $a \equiv b \ (\mathrm{mod}\ N_{1})$, $a \equiv b \ (\mathrm{mod}\ N_{2})$, $\ldots$, $a \equiv b \ (\mathrm{mod}\ N_{k})$,

$$
    a \equiv b \ (\mathrm{mod}\ m)
$$

where $m$ is a least common multiple of $N_{1}$, $\ldots$, $N_{k}$.

#### proof
$a - b = N_{1} q$ for some $q \in \mathbb{Z}$.

$$
    a - b = N_{1}^{\prime} q m
    .
$$

Hence $a  \equiv b\ (\mathrm{mod}\ m)$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 7
If $p$ is a prime, for all $x, y \in \mathbb{Z}$,

$$
    (x + y)^{p} \equiv x^{p} + y^{p} \ (\mathrm{mod}\ p)
    .
$$

#### proof

$$
\begin{eqnarray}
    (x + y)^{p}
    & = &
        \sum_{i = 0}^{p}
            \left(
                \begin{array}{c}
                   p \\
                   i
                \end{array}
            \right)
            x^{i}y^{p - i}
    \nonumber
    \\
    & = &
        \sum_{i = 0}^{p}
            \frac{
                p \cdot (i + 1)! 
            }{
                (p - i)!
            }
            \left(
                \begin{array}{c}
                   p \\
                   i
                \end{array}
            \right)
            x^{i}y^{p - i}
    \nonumber
\end{eqnarray}
$$

If $i != 0, p$, the coeeficient is a multiple of $p$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 8
If $p$ is a prime, for all $x_{1}$, $\ldots$, $x_{n} \in \mathbb{Z}$,

$$
    (x_{1} + \cdots + x_{n})^{p} \equiv x_{1}^{p} + \cdots + x_{n}^{p} \ (\mathrm{mod}\ p)
    .
$$

#### proof
It is easy to show by using Proposition 7 repeatedly.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 9
If $p$ is a prime, for $a$ such that $0 \le a \le p - 1$,

$$
    \left(
        \begin{array}{c}
            p - 1 \\
            a
        \end{array}
    \right)
    \equiv (-1)^{a} \ (\mathrm{mod}\ p)
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>


#### Proposition 10

$$
\begin{eqnarray}
    \lceil
        \frac{x}{y}
    \rceil
    & = &
        \lfloor
            \frac{x + y - 1}{y}
        \rfloor
    \nonumber
    \\
    \lfloor
        \frac{x}{y}
    \rfloor
    & = &
        q
    \nonumber
    \\
    \lfloor
        \frac{x}{y}
    \rfloor
    y
    & = &
        x - r
    \nonumber
\end{eqnarray}
$$

where $x = yq + r$ and $0 \le r < y$.

#### proof

$$
\begin{eqnarray}
    \lfloor
        \frac{x}{y}
    \rfloor
    & = &
        \lfloor
            \frac{yq + r}{y}
        \rfloor
    \nonumber
    \\
    & = &
        q
        +
        \lfloor
            \frac{r}{y}
        \rfloor
    \nonumber
    \\
    & = &
        q
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \lfloor
        \frac{x}{y}
    \rfloor
    y
    & = &
        yq
    \\
    \nonumber
    & = &
        x - r
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Example 1
Find

$$
    (2^{100} - 1)^{99} \ (\mathrm{mod}\ 100)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Example 2

$$
    3^{30}
    \equiv
    1+ 17 \times 31
    \ (\mathrm{mod}\ 31^{2})
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
