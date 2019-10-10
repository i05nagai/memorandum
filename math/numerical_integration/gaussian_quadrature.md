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

Let $h$ be function.

$$
\begin{eqnarray}
    (h f, g)
    & = &
        \int_{a}^{b}
            \omega(x) h(x) f(x) g(x)
        \ dx
    \nonumber
    \\
    & = &
        \int_{a}^{b}
            \omega(x) f(x) h(x) g(x)
        \ dx
    \nonumber
    \\
    & = &
        (f, h g)
    .
    \nonumber
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
    .
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
    j \le i
    .
\end{eqnarray}
$$

Let $p_{i+1} \in \bar{\Pi}_{i+1}$.
There exist constants $$\delta, c_{0}, \ldots, c_{i-1}$$ such that


$$
    p_{i+1}(x)
    =
    x
    p_{i}(x)
    -
    \delta p_{i}(x)
    +
    \sum_{k=0}^{i-1}
        c_{k} p_{k}(x)
    .
$$

We have

$$
\begin{eqnarray}
    (p_{i+1}, p_{j})
    & = &
        (xp_{i}, p_{j})
        -
        \delta(p_{i}, p_{j})
        +
        \sum_{k=0}^{i-1}
            c_{k} (p_{k}, p_{j})
    .
\end{eqnarray}
$$

The constants must satisfy

$$
\begin{eqnarray}
    (p_{i+1}, p_{i})
    & = &
        (xp_{i}, p_{j})
        -
        \delta(p_{i}, p_{j})
        =
        0
    \label{equation_03_06_08_a}
    \\
    j < i,
    \
    (p_{i+1}, p_{j})
    & = &
        (xp_{i}, p_{j})
        +
        c_{j} (p_{j}, p_{j})
        =
        0
    \label{equation_03_06_08_b}
    .
\end{eqnarray}
$$

From $$\eqref{equation_03_06_1_c}$$, $(p_{k}, p_{k}) \neq 0$.
In fact, suppose that $(p_{k}, p_{k}) = 0$.

$$
\begin{eqnarray}
    j \le i,
    \
    (p_{j}, p_{j})
    & = &
        \int_{a}^{b}
            \omega(x)
            p_{j}^{2}(x)
        \ dx
    & = &
        0
    .
\end{eqnarray}
$$

Hence $p_{j} \equiv 0$.
This contradicts to the assumption of the induction.

The euqation $$\eqref{equation_03_06_08_a}$$ can be solved uniquely


$$
\begin{eqnarray}
    \delta
    & = &
        \frac{
            (xp_{i}, p_{i})
        }{
            (p_{i}, p_{i})
        }
    .
    \nonumber
\end{eqnarray}
$$

By the induction hypothesis, for $j < i$,

$$
\begin{eqnarray}
    & &
        p_{j}(x)
        =
        (x - \delta_{j}) p_{j-1}(x)
        -
        \gamma_{j}^{2} p_{j-2}(x)
    \nonumber
    \\
    & \Leftrightarrow &
        x p_{j-1}(x)
        =
        p_{j}(x)
        +
        \gamma_{j}^{2} p_{j-2}(x)
        +
        \delta_{j} p_{j-1}(x)
\end{eqnarray}
$$

$$
\begin{eqnarray}
    c_{j}
    & = &
        -
        \frac{
            (xp_{j}, p_{i})
        }{
            (p_{j}, p_{j})
        }
    \nonumber
    \\
    & = &
        -
        \frac{
            (p_{j+1}, p_{i})
            +
            \gamma_{j+1}^{2}
            (p_{j-1}, p_{i})
            +
            \delta_{j+1}
            (p_{j}, p_{i})
        }{
            (p_{j}, p_{j})
        }
    \nonumber
    \\
    & = &
        -
        \frac{
            (p_{j+1}, p_{i})
        }{
            (p_{j}, p_{j})
        }
    \nonumber
    \\
    & = &
        \begin{cases}
            0
            &
                (j < i-1)
            \\
            -
            \frac{
                (p_{j}, p_{i})
            }{
                (p_{j}, p_{j})
            }
            &
                (j = i-1)
        \end{cases}
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
