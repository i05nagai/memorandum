---
title: Stone-Weierstrass Theorem
---

## Stone-Weierstrass Theorem

## Weierstrass Approximation theorem

#### Theorem 1 Weierstrass
* $a < b < \infty$,
* $f \in C_{0}([a, b])$,
    * real valued continuous function
* $\epsilon > 0$,

There exists polynomial $p:[a, b] \rightarrow \mathbb{R}$ such that

$$
    \norm{
        f - p
    }_{\infty}
    <
    \epsilon
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary 2
* $a < b < \infty$,

$C_{0}([a, b])$ is separable.

#### proof
Let

$$
\begin{eqnarray}
    \mathcal{P}_{0}
    & := &
        \{
            p(x)
            \mid
            p(x)
            =
            \sum_{k=0}^{n}
                a_{k}x^{k},
            \
            n \in \mathbb{Z}_{\ge 0},
            \
            a_{k} \in \mathbb{Q}
        \}
    \nonumber
    \\
    \mathcal{P}
    & := &
        \{
            p(x)
            \mid
            p(x)
            =
            \sum_{k=0}^{n}
                a_{k}x^{k},
            \
            n \in \mathbb{Z}_{\ge 0},
            \
            a_{k} \in \mathbb{R}
        \}
    \nonumber
\end{eqnarray}
    .
$$

Let $p = \sum_{k=0}^{n}c_{k}x^{k} \in \mathcal{P}$ and $\epsilon > 0$ be fixed.
For all $k \in [0:n]$, there exists $d_{k} \in \mathbb{Q}$ such that

$$
\begin{eqnarray}
    \abs{
        c_{k}
        -
        d_{k}
    }
    & = &
        \frac{1}{b^{k}(n + 1)}
        \epsilon
    .
    \nonumber
\end{eqnarray}
$$

Let $q(x) := \sum_{k=0}^{n} d_{k}x^{k}$.

$$
\begin{eqnarray}
    \abs{
        p(x)
        -
        q(x)
    }
    & < &
        \sum_{k=0}^{n}
            \abs{c_{k} - d_{k}}
            \abs{x}^{k}
    \nonumber
    \\
    & < &
        \sum_{k=0}^{n}
            \frac{\epsilon}{b^{k}(n + 1)}
            b^{k}
    \nonumber
    \\
    & = &
        \sum_{k=0}^{n}
            \frac{\epsilon}{n + 1}
    \nonumber
    \\
    & = &
        \epsilon
    \nonumber
\end{eqnarray}
$$

By Weierstrass approximation theorem, $\mathcal{P}_{0}$ is also dense in $C([a, b])$.
Besides, $\mathcal{P}_{0}$ is countable.

<div class="QED" style="text-align: right">$\Box$</div>

## Stone-Weirastrass theorem

#### Theorem 3 Stone-Weirastrass theorem


#### proof

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Stone–Weierstrass theorem \- Wikipedia](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)
* https://www.math.cuhk.edu.hk/course_builder/1415/math3060/Chapter%203.%20Continuous%20Functions.pdf
