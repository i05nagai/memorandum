---
title: Gausiaan Quadrature
---

## Gausiaan Quadrature

* The abscissas
    * The abscissas are not equally spaced
* The coefficients of integrand


* $[a, b]$,
    * interval
* $\omega(x)$,
    * nonnegative weight function on the interval $[a, b]$,


#### Assumption

* (a) $$\{x \in [a, b] \mid \omega(x) \ge 0\}$$ is measurable
* (b) all momemnts exists and finite

$$
\begin{eqnarray}
    \forall k = 0, 1, \ldots,
    \mu_{k}
    :=
    \int_{a}^{b}
        x^{k}\omega(x)
    \ dx
    <
    0
    .
\end{eqnarray}
$$

* (c) For polynomials $s(x)$ which are nonnegative on $[a, b]$,

$$
    \int_{a}^{b}
        \omega(x) s(x)
    \ dx
    =
    0
    \Rightarrow
    s(x) \equiv 0
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

$$
\begin{eqnarray}
    I(f)
    :=
    \int_{a}^{b}
        \omega(x)
        f(x)
    \ dx
    ,
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \tilde{I}(f)
    :=
    \sum_{i=1}^{n}
        w_{i} f(x_{i})
     .
    \label{equation_03_06_02}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \bar{\Pi}_{j}
    & := &
        \{
            p
            \mid
            p(x) = x^{j} + a_{1} x^{j-1} + \cdots + a_{j},
            a_{k} \in \mathbb{R}
        \}
    \nonumber
    \\
    \Pi_{j}
    & := &
        \{
            p
            \mid
            \mathrm{degree}(p) \le j
        \}
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    (f, g)
    & := &
        \int_{a}^{b}
            \omega(x) f(x) g(x)
        \ dx
    \nonumber
    \\
    (f, f)
    & = &
        \int_{a}^{b}
            \omega(x) f(x)^{2}
        \ dx
    .
\end{eqnarray}
$$

#### Theorem 3.6.3
There exists $p_{j} \in \bar{\Pi}_{j}$ for $j = 0, 1, \ldots, $ such that

$$
\begin{eqnarray}
    i \neq k,
    \
    (p_{i}, p_{k})
    =
    0
    .
    \label{equation_03_06_04}
\end{eqnarray}
$$

These polynomials are uniquely defined by the recursions

$$
\begin{eqnarray}
    p_{0}(x)
    & \equiv &
        1
    \label{equation_03_06_05_a}
    \\
    p_{i+1}(x)
    & = &
        (x - \delta_{i+1}) p_{i}(x)
        -
        \gamma_{i+1}^{2} p_{i-1}(x)
        \
        i \ge 0,
    \label{equation_03_06_05_b}
    \\
    \delta_{i+1}
    & = &
        \frac{
            (xp_{i}, p_{i})
        }{
            (p_{i}, p_{i})
        }
        i \ge 0,
    \nonumber
    \\
    \gamma_{i+1}^{2}
    & = &
        \begin{cases}
            1
            &
                i = 0
            \\
            \frac{
                (p_{i}, p_{i})
            }{
                (p_{i-1}, p_{i-1})
            }
            &
                i \ge 1
        \end{cases}
        \frac{
            (xp_{i}, p_{i})
        }{
            (p_{i}, p_{i})
        }
        i \ge 0,
\end{eqnarray}
$$

#### proof
We prove by induction.
If $i = 0$, the statements are true.
Let us assume that the statments holds true up to $j \le i$.
We'll show there exists a unique polynomials $p_{i + 1} \in \bar{\Pi}_{i+1}$ with

$$
\begin{eqnarray}
    (p_{i+1}, p_{j})
    =
    0
    \
    j \ge i
    .
\end{eqnarray}
$$

Let $p_{i+1} \in \bar{\Pi}_{i+1}$.

$$
    p_{i+1}(x)
    =
    x
    p_{i}
    -
    \delta_{i+1} p_{i}(x)
$$


<div class="QED" style="text-align: right">$\Box$</div>

## Reference
