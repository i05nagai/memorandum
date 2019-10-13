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


#### Corollary 3.6.9
* $$\{p_{0}, \ldots, p_{n}\}$$,
    * polynomials in theorem 3.6.3

$$
    (p, p_{n})
    =
    0
    \quad
    p \in \Pi_{n-1}
    .
$$

#### proof
Since $p_{j} \in \Pi_{j}$ for all $j$, $p$ is representable as a linear combination of the polynomials.

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 3.6.10
* $$\{x_{1}, \ldots x_{n}\}$$,
    * the roots of $p_{n}$,

The roots are real and simple.
$x_{i} \in (a, b)$.

#### proof
Assume that $a < x_{1}, \ldots, x_{l} < b$ are distinct roots of $p_{n}$ and $l < n$.
Let

$$
    q(x)
    :=
    \prod_{j=1}^{l}
        (x - x_{j})
    \in
    \bar{\Pi}_{l}
    .
$$

Apparently, $q p_{n} \not\equiv 0$.
That implies

$$
\begin{eqnarray}
    0
    & = &
        (p_{n}, q)
        \quad
        (\because l < n \text{ and Theorem 3.6.3})
    \nonumber
\end{eqnarray}
$$

On the other hands,

$$
\begin{eqnarray}
    (p_{n}, q)
    & = &
        \int_{a}^{b}
            \omega(x)
            p_{n}(x) q(x)
        \ dx
    \nonumber
    \\
    & \neq &
        0
        \quad
        (\because \text{Assumption (c)})
    .
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


#### Theorem 3.6.11
* $t_{1}, \ldots, t_{n} \in \mathbb{R}$,
    * $t_{i} \neq t_{j}$ for $i \neq j$,

$$
    A
    :=
    \left(
        \begin{array}{ccc}
            p_{0}(t_{1}) & \cdots & p_{0}(t_{n})
            \\
            \vdots & & \vdots
            \\
            p_{n-1}(t_{1}) & \cdots & p_{n-1}(t_{n})
        \end{array}
    \right)
    .
$$

$A$ is nonsingular.

#### proof
Assume that $A$ is singular.
There exists a vector $c^{\mathrm{T}} = (c_{0}, \ldots, c_{n-1}) \neq 0$ such that

$$
    c^{\mathrm{T}}A
    =
    0
    .
$$

Let

$$
    q(x)
    :=
    \sum_{i=0}^{n-1}
        c_{i}p_{i}(x)
    .
$$

Since

$$
\begin{eqnarray}
    c^{\mathrm{T}}A
    & = &
        \left(
            \sum_{i=0}^{n-1} c_{i} p_{i}(t_{1}),
            \cdots,
            \sum_{i=0}^{n-1} c_{i} p_{i}(t_{1})
        \right)
    \nonumber
    \\
    & = &
        \left(
            q(t_{1})
            \cdots,
            q(t_{n})
        \right)
    \nonumber
    \\
    & = &
        (0, \ldots, 0),
    \nonumber
\end{eqnarray}
$$

$t_{1}, \ldots, t_{n}$ are distinct roots of $q$.
Since $\mathrm{degree}(p_{i}) < n$ for all $i = 0, \ldots, n-1$, $\mathrm{degree}(q) < n$.
Thus, $q \equiv 0$.
However, $$\{p_{i}\}$$ is linearly independet, so $c_{i} = 0$ for all $i$.  

<div class="QED" style="text-align: right">$\Box$</div>

#### Definition Haar condition
* $$\{p_{i}\}$$,
    * polynomials

$$\{p_{i}\}$$ is said to satisfy Haar condition if for all distincts $t_{1}, \ldots, t_{n}$,

$$
    \left(
        \begin{array}{ccc}
            p_{0}(t_{1}) & \cdots & p_{0}(t_{n})
            \\
            \vdots & & \vdots
            \\
            p_{n-1}(t_{1}) & \cdots & p_{n-1}(t_{n})
        \end{array}
    \right)
$$

is nonsingular.
Such $$\{p_{i}\}$$ is said to be Chebychev system.

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 3.6.12
* $$x_{1}, \ldots, x_{n}$$,
    * roots of $n$-th orthonormal polynomials $p_{n}$,
* $$w_{1}, \ldots, w_{n}$$,
    * solution of nonsingular system of equations

(a)

$$
\begin{eqnarray}
    \left(
        \begin{array}{ccc}
            p_{0}(x_{1}) &  & p_{0}(x_{n})
            \\
             &  & 
            \\
            p_{n-1}(x_{1}) &  & p_{n-1}(x_{n})
        \end{array}
    \right)
    w
    & = &
        \left(
            \begin{array}{c}
                (p_{0}, p_{0})
                \\
                0
                \\
                \vdots 
                \\
                0
            \end{array}
        \right)
    \label{equation_03_06_13}
\end{eqnarray}
$$

Then $w_{i} > 0$ for all $i = 1, \ldots, n$ and for all $p \in \Pi_{2n-1}$

$$
\begin{eqnarray}
    \int_{a}^{b}
        \omega(x) p(x)
    \ dx
    & = &
        \sum_{i=1}^{n}
            w_{i} p(x_{i})
    .
    \label{equation_03_06_14}
\end{eqnarray}
$$

(b)

Conversely, if $$w_{i}, x_{i}$$ satisfy $$\eqref{equation_03_06_14}$$, then $x_{i}$ are the roots of $p_{n}$ and the weights $w_{i}$ satisfy $$\eqref{equation_03_06_13}$$.

(c)

There is no $x_{i}, w_{i}, i = 1, \ldots, n$ such that $$\eqref{equation_03_06_14}$$ holds for all $p \in \Pi_{2n}$.

#### proof
(a)

By Theorem 3.6.10, the roots $x_{i}, i = 1, \ldots, n$  of $p_{n}$ are real and mutually distinct numbers in $(a, b)$.
The matrix

$$
\begin{eqnarray}
    A
    & := &
        \left(
            \begin{array}{ccc}
                p_{0}(x_{1}) & \cdots & p_{0}(x_{n})
                \\
                \vdots &  & \vdots
                \\
                p_{n-1}(x_{1}) & \cdots & p_{n-1}(x_{n})
            \end{array}
        \right)
    \label{equation_03_06_15}
\end{eqnarray}
$$

is nonsingular by Theorem 3.6.11.
Hence $$\eqref{equation_03_06_13}$$ has a unique solution.
Let $p \in \prod_{2n-1}$.
There exist $q, r \in \Pi_{n-1}$ such that

$$
    p(x)
    =
    p_{n}(x) q(x) + r(x)
    .
$$

$p, q$ can be written in

$$
\begin{eqnarray}
    q(x)
    & = &
        \sum_{k=0}^{n-1}
            \alpha_{k} p_{k}(x)
    \nonumber
    \\
    r(x)
    & = &
        \sum_{k=0}^{n-1}
            \alpha_{k} p_{k}(x)
    .
\end{eqnarray}
$$

Since $p_{0} \equiv 1$,

$$
\begin{eqnarray}
    \int_{a}^{b}
        \omega(x)
        p(x)
    \ dx
    & = &
        \int_{a}^{b}
            \omega(x)
            \left(
                p_{n}(x)
                q(x)
                +
                r(x)
                p_{0}(x)
            \right)
        \ dx
    \nonumber
    \\
    & = &
        (p_{n}, q)
        +
        (r, p_{0})
    \nonumber
    \\
    & = &
        (p_{n}, \sum_{k=0}^{n-1} \alpha_{k}p_{k})
        +
        (\sum_{k=0}^{n-1} \beta_{k}p_{k}, p_{0})
    \nonumber
    \\
    & = &
        \beta_{0}
        (p_{0}, p_{0})
    .
    \nonumber
\end{eqnarray}
$$

On the other hand,

$$
\begin{eqnarray}
    \sum_{k=1}^{n}
        w_{i} p(x_{i})
    & = &
        \sum_{i=1}^{n}
            w_{i}
            \left(
                p_{n}(x_{i}) q(x_{i})
                +
                r(x_{i})
            \right)
    \nonumber
    \\
    & = &
        \sum_{k=0}^{n-1}
            \beta_{k}
            \sum_{i=1}^{n}
                w_{i}
                p_{k}(x_{i})
    \nonumber
    \\
    & = &
        \beta_{0}
        \sum_{i=1}^{n}
            w_{i}
            p_{0}(x_{i})
    \nonumber
    \\
    & = &
        \beta_{0}
        (p_{0}, p_{0})
    \nonumber
\end{eqnarray}
$$

We claim that if $w_{i}, x_{i}$, $i = 1, \ldots, n$ are such that $$\eqref{equation_03_06_14}$$ holds for all $p \in \Pi_{2n-1}$, then $w_{i} > 0$ for $i = 1, \ldots, n$.
Let

$$
    \bar{p}_{j}(x)
    :=
    \prod_{h =1, h \neq j}^{n}
        (x - x_{h})^{2}
    \in
    \Pi_{2n-2}
    ,
    \
    (j = 1, \ldots, n).
$$

Since $\bar{p}_{j} \not\equiv 0$, we have by assumption (c), 

$$
\begin{eqnarray}
    0
    & < &
        \int_{a}^{b}
            w(x) \bar{p}_{j}(x)
        \ dx
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            w_{i} \bar{p}_{j}(x_{i})
    \nonumber
    \\
    & = &
        w_{j}
        \prod_{h=1, h\neq j}^{n}
            (x_{j} - x_{j})^{2}
    .
    \nonumber
\end{eqnarray}
$$

Thus, $w_{j} > 0$.

(c)

Assume that $w_{i}, x_{i}, i = 1, \ldots, n$ satisfy $$\eqref{equation_03_06_14}$$ for all $p \in \Pi_{2n}$.
Let

$$
    \bar{p}(x)
    :=
    \prod_{j=1}^{n}
        (x - x_{j})^{2} \in \Pi_{2n}
    .
$$


$$
\begin{eqnarray}
    0
    & < &
        \int_{a}^{b}
            \omega(x)
            \bar{p}(x)
        \ dx
        \quad
        (\because \text{Assumption (c)})
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            w_{i} \bar{p}(x_{i})
    \nonumber
    \\
    & = &
        0
    .
    \nonumber
\end{eqnarray}
$$


(b)

Suppose that $w_{i}, x_{i}$ are such that $$\eqref{equation_03_06_14}$$ for all $p \in \Pi_{2n-1}$.
$x_{i}$ must be $x_{i} \neq x_{j} \ i \neq j$.
Indeed, let us assume $x_{n-1} = x_{n}$.

$$
    p(x)
    :=
    \sum_{i=1}^{n-1}
        (x - x_{i})^{2}
    \in
    \Pi_{2n-1}
    .
$$

Hence this contradicts

$$
\begin{eqnarray}
    0
    & < &
        \int_{a}^{b}
            \omega(x)
            p(x)
        \ dx
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            w_{i} p(x_{i})
    \nonumber
    \\
    & = &
        0
    .
    \nonumber
\end{eqnarray}
$$

For all $k = 0, \ldots, n-1$,

$$
\begin{eqnarray}
    \sum_{i=1}^{n}
        w_{i} p_{k}(x_{i})
    & = &
        \int_{a}^{b}
            \omega(x) p_{k}(x)
        \ dx
    \nonumber
    \\
    & = &
        (p_{k}, p_{0})
    \nonumber
    \\
    & = &
        \begin{cases}
            (p_{0}, p_{0})
            &
                k = 0
            \\
            0
            &
                1 \le k \le n - 1
        \end{cases}
    .
    \nonumber
\end{eqnarray}
$$

Thus, $w_{i}$ satisfy $$\eqref{equation_03_06_13}$$.

Next we will show $x_{i}$ are roots of $p_{n}$.
Applying $$\eqref{equation_03_06_14}$$ we will have

$$
\begin{eqnarray}
    0
    & =&
        (p_{k}, p_{n})
        \quad
        (\because \text{orthonormal})
    \nonumber
    \\
    & = &
        \int_{a}^{b}
            \omega(x) p_{k}(x) p_{n}(x)
        \ dx
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            w_{i} p_{k}(x_{i}) p_{n}(x)
        \quad
        (\because \eqref{equation_03_06_14})
    .
\end{eqnarray}
$$

In other word,

$$
\begin{eqnarray}
    A
    \left(
        \begin{array}{c}
            w_{1} p_{n}(x_{1})
            \\
            \vdots 
            \\
            w_{n} p_{n}(x_{n})
        \end{array}
    \right)
    =
    0
    .
    \nonumber
\end{eqnarray}
$$

By theorem 3.6.11, $A$ is nonsingular.
Hence $c = 0$, that is, for all $i = 1, \ldots, n$,

$$
    w_{i} p_{n}(x_{i})
    =
    0
    .
$$

Since $w_{i} > 0$, we have $p_{n}(x_{i}) = 0$.

<div class="QED" style="text-align: right">$\Box$</div>


#### Theorem 3.6.24
- $f \in C^{2n}[a, b]$,

$$
    \int_{a}^{b}
        \omega(x)
        f(x)
    \ dx
    -
    \sum_{i=1}^{n}
        w_{i} f(x_{i})
    =
    \frac{
        f^{(2n)}(\xi)
    }{
        (2n)!
    }(p_{n}, p_{n})
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>


## Type of Gaussian quadrature

Gauss-Legendre

$$
\begin{eqnarray}
    p_{k}(x)
    :=
    \frac{k!}{(2k)1}
    \frac{d^{k}}{d x^{k}}
        (x - 1)^{k},
    \
    k = 0, 1, \ldots,
    .
\end{eqnarray}
$$

- $\omega(x) = 1$.
- $[a, b] := [-1, 1]$,


Gauss-Chebyshev

- $p_{k}$
    - Chebyshev polynomials
- $\omega(x) := (1 - x^{2})^{-1/2}$,
- $[a, b] := [-1, 1]$,


Gauss-Laguerre

- $p_{k}$
    - Laguerre polynomials
- $\omega(x) := e^{-x}$,
- $[a, b] := [0, \infty]$,

Gauss-Hermite

- $p_{k}$
    - Hermite polynomials
- $\omega(x) := e^{-x^{2}}$,
- $[a, b] := [-\infty, \infty]$,

$$
\begin{eqnarray}
    \int_{-\infty}^{\infty}
        \frac{
            1
        }{
            \sigma \sqrt{2 \pi}
        }
        h(y)
        \exp
        \left(
            -
            \frac{
                (y - \mu)^{2}
            }{
                2 \sigma^{2}
            }
        \right)
    \ dy
    & = &
        \int_{-\infty}^{\infty}
            \frac{
                1
            }{
                \sigma \sqrt{2 \pi}
            }
            h(\sqrt{2} \sigma x + \mu)
            \exp
            \left(
                -
                x^{2}
            \right)
            \sqrt{2} \sigma
        \ dy
        \quad
        (x = (y - \mu) / \sqrt{2 \sigma^{2}})
    \nonumber
    \\
    & = &
        \int_{-\infty}^{\infty}
            \frac{
                1
            }{
                \sqrt{\pi}
            }
            h(\sqrt{2} \sigma x + \mu)
            \exp
            \left(
                -
                x^{2}
            \right)
        \ dy
    .
    \nonumber
\end{eqnarray}
$$


Gauss-Jacobi

- $p_{k}$
    - Hermite polynomials
- $\omega(x) := (1 - x)^{\alpha}(1 + x)^{\beta}$,
- $[a, b] := [-1, 1]$,


Gauss-Radau

- In naive Gaussian quadrature, all abscissas are roots of the orthonomal polynomial. Gauss-Radau allows you to use preassigned nodes.
- A preassigned node is an endpoint of the interval, that is either $a$ or $b$.

Gauss-Lobatto

- In naive Gaussian quadrature, all abscissas are roots of the orthonomal polynomial. Gauss-Radau allows you to use preassigned nodes.
- preassigned nodes are endpoints of the interval, that is either $a$ and $b$.


Gauss-Kronrod

- In naive Gaussian quadrature, $x_{i}$ and $w_{i}$ need to be re-calcualted as $n$ increase. Gauss-Kronrod allows you to use the values calcualted in $n-1$.


## Reference
- Stoer, Josef, and Roland Bulirsch. Introduction to numerical analysis. Vol. 12. Springer Science & Business Media, 2013.
