---
title: Numerical Integration
---

## Numerical Integration


## Problem
* $N \in \mathbb{N}$,
* $f: \mathbb{R}^{N} \rightarrow \mathbb{R}$,
    * integralble

$$
    J^{N}
    :=
    \{
        (a_{1}, b_{1})
        \times
        \cdots
        \times
        (a_{N}, b_{N})
        \mid
        a_{i} \in \mathbb{R},
        \
        b_{i} \in \mathbb{R},
        \
        a_{i} < b_{i}
    \}
$$

$$
    I
    :=
    \int_{a}^{b}
        f(x)
    \ dx
$$

The numerical integrator $Q[a, b]$ is an approximation of $I$.
The numerical error $\epsilon$ of the approximation is defined by

$$
    \epsilon
    \approx
    \left|
        I
        -
        Q[a, b]
    \right|
    .
$$

## Methods
* Simpson rules
* Closed Newton-Cotes Formulas


##

* $f:[a, b] \rightarrow \mathbb{R}$,
* $f:[a, b] \in C_{0}[a, b]$,

$$
    I(f)
    :=
    \int_{a}^{b}
        f(x)
    \ dx
    .
$$

Lagrange interpolation

Let

* $n \in \mathbb{N}$,
* $$(x_{i}, y_{i}) \in \mathbb{R}^{2}$$,
    * $i = 0, \ldots, n$,

Find polynomials

$$
    p_{n}(x)
    :=
    \sum_{i=0}^{n}
        c_{i} x^{i}
$$

such that

$$
    y_{i}
    =
    p_{n}(x_{i})
    .
$$

The problem is equivalent to

$$
\begin{eqnarray}
    \left(
        \begin{array}{ccccc}
            1
            &
                x_{0}
            &
                x_{0}^{2}
            &
            \cdots
            &
                x_{0}^{n}
            \\
            \vdots
            \\
            1
            &
                x_{n}
            &
                x_{n}^{2}
            &
            \cdots
            &
                x_{n}^{n}
        \end{array}
    \right)
    \left(
        \begin{array}{c}
            c_{0}
            \\
            \vdots 
            \\
            c_{n}
        \end{array}
    \right)
    & = &
    \left(
        \begin{array}{c}
            y_{0}
            \\
            \vdots 
            \\
            y_{n}
        \end{array}
    \right)
    \nonumber
    \\
    Vc
    & = &
        y
    .
    \nonumber
\end{eqnarray}
$$

If $\mathrm{det}V \neq V$,

$$
\begin{eqnarray}
    L_{i}(x)
    & := &
        \frac{
            F_{n}(x)
        }{
            (x - x_{i})
            F_{n}^{\prime}(x_{i})
        }
    \nonumber
    \\
    & = &
        \prod_{k=0, k \neq i}^{n}
            \frac{
                x - x_{k}
            }{
                x_{i} - x_{k}
            }
        \quad
        (i = 0, \ldots, n)
    .
    \nonumber
\end{eqnarray}
$$

$L_{i}(x)$ is polynomial with degree $n$.

$$
    L_{i}(x_{i})
    :=
    \begin{cases}
        1
        &
            (i = j)
        \\
        0
        &
            (i \neq j)
    \end{cases}
    \quad
    (i, j = 0, \ldots, n)
    .
$$

Thus, if we take $p_{n}$ as

$$
    p_{n}(x; x_{i}, y_{i})
    =
    \sum_{i=0}^{n}
        y_{i}
        L_{i}(x)
    .
$$

##

$$
\begin{eqnarray}
    x_{i}
    & := &
        a + ih
        \quad
        (i = 0, \ldots, n)
    \nonumber
    \\
    h
    & := &
        \frac{
            b - a
        }{
            n
        }
    \nonumber
\end{eqnarray}
    .
$$

$$
\begin{eqnarray}
    Q(f)
    & := &
        Q(p_{n}(\cdot; x_{i}, f(x_{i})))
    \nonumber
    \\
    & := &
        \int_{a}^{b}
            p_{n}(x)
        \ dx
    \nonumber
    \\
    & = &
        \sum_{i=0}^{n}
            \alpha_{i}
            f(x_{i})
    ,
    \nonumber
    \\
    \alpha_{i}
    & := &
        \int_{a}^{b}
            L_{i}(x)
        \ dx
    \nonumber
    \\
    & = &
        \int_{a}^{b}
            \prod_{j=0, j \neq i}^{n}
                \frac{
                    x - x_{j}
                }{
                    x_{i} - x_{j}
                }
        \ dx
    \nonumber
    \\
    & = &
        \int_{0}^{n}
            \prod_{j=0, j \neq i}^{n}
                \frac{
                    x - x_{j}
                }{
                    x_{i} - x_{j}
                }
        \ dx
    \nonumber
    \\
    & = &
        \int_{0}^{n}
            \prod_{j=0, j \neq i}^{n}
                \frac{
                    t - x_{j}
                }{
                    i - j
                }
                h
        \ dx
        \quad
        (\because x = a + t h)
    \nonumber
    \\
    & = &
        (-1)^{n-i}
        \frac{
            h
        }{
            (n - i)!
            i!
        }
        \int_{0}^{n}
            \prod_{j=0, j \neq i}^{n}
                \frac{
                    t - x_{j}
                }{
                    i - j
                }
                h
        \ dx
    \nonumber
    \\
    & = &
        (-1)^{n-i}
        \frac{
            h
        }{
            n!
        }
        \left(
            \begin{array}{c}
                n \\
                i
            \end{array}
        \right)
        \int_{0}^{n}
            \frac{
                \prod_{j=0}^{n}
                    (t - j)
            }{
                    t - i
            }
        \ dx
    .
\end{eqnarray}
$$

This approximation called closed Newton-Coretes formula.

Let us see more specific example.
Suppose that $n = 1$.

$$
\begin{eqnarray}
    x_{0}
    & = &
        a
    \nonumber
    \\
    x_{1}
    & = &
        b
    \nonumber
    \\
    h
    & := &
        b - a
    \nonumber
    \\
    \alpha_{0}
    & := &
        \frac{
            h
        }{
            2
        }
    \nonumber
    \\
    \alpha_{1}
    & := &
        \frac{
            h
        }{
            2
        }
    \nonumber
\end{eqnarray}
$$

Therefore,

$$
\begin{eqnarray}
    Q_{1}(f)
    & := &
        \sum_{i=0}^{1}
            \alpha_{i}
            f(x_{i})
    \nonumber
    \\
    & = &
        \frac{h}{2}
        (f(a) + f(b))
    \nonumber
    \\
    & =: &
        T(f)
    .
    \nonumber
\end{eqnarray}
$$

Suppose that $n = 2$.

$$
\begin{eqnarray}
    x_{0}
    & := &
        a
    \nonumber
    \\
    x_{1}
    & := &
        c
    \nonumber
    \\
    x_{2}
    & := &
        b
    \nonumber
    \\
    h
    & := &
        \frac{
            b - a
        }{
            2
        }
    \nonumber
    \\
    \alpha_{0}
    & := &
        \frac{h}{3}
    \nonumber
    \\
    \alpha_{1}
    & := &
        \frac{4h}{3}
    \nonumber
    \\
    \alpha_{2}
    & := &
        \frac{h}{3}
    \nonumber
\end{eqnarray}
$$

Therefore,

$$
\begin{eqnarray}
    S(f)
    & := &
        Q_{2}(f)
    \nonumber
    \\
    & := &
        \sum_{i=0}^{2}
            \alpha_{i}
            f(x_{i})
    \nonumber
    \\
    & = &
        \frac{h}{3}
        \left(
            f(a)
            +
            4 f(c)
            +
            f(b)
        \right)
    .
    \nonumber
\end{eqnarray}
$$

This formula is called simpson rule.

#### Theorem
* $f \in C^{2}[a, b]$,

$$
    \abs{
        I(f) - T(f)
    }
    \le
    \frac{1}{12}
    (b - a)^{3}
    \norm{f^{\prime\prime}}_{L^{\infty}[a, b]}
    .
$$

* $f \in C^{4}[a, b]$,

$$
    \abs{
        I(f) - S(f)
    }
    \le
    \frac{1}{2880}
    (b - a)^{3}
    \norm{f^{(4)}}_{L^{\infty}[a, b]}
    .
$$

#### proof

$$
\begin{eqnarray}
    \xi(y)
    & := &
        y
        +
        \frac{
            (b + a)
        }{
            2
        }
    \nonumber
    \\
    k
    & := &
        \frac{
            b - a
        }{
            2
        }
    \nonumber
    \\
    \phi(y)
    & := &
        f(\xi(y))
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    M
    & := &
        \norm{
            f^{\prime\prime}
        }_{L^{\infty}[a, b]}
    \nonumber
    \\
    & = &
        \norm{
            \phi^{\prime\prime}
        }_{L^{\infty}[k, k]}
    \nonumber
    \\
    g(k)
    & := &
        I(f)
        -
        T(f)
    \nonumber
    \\
    & = &
        \int_{-k}^{k}
            \phi(y)
        \ dy
        -
        k
        \left(
            \phi(-k)
            +
            \phi(k)
        \right)
    \nonumber
\end{eqnarray}
$$

Since for $t \in [0, k]$,

$$
    g^{\prime}(t)
    :=
    -t
    \left(
        \phi^{\prime}(t)
        -
        \phi^{\prime}(-t)
    \right)
    ,
$$

By fundamental theorem of calculus,

$$
\begin{eqnarray}
    \abs{
        g^{\prime}(t)
    }
    & := &
        \abs{
            -t
            \int_{-t}^{t}
                \phi^{\prime\prime}(s)
            \ ds
        }
    \nonumber
    \\
    & \le &
        t
        \int_{-t}^{t}
            \abs{
                \phi^{\prime\prime}(s)
            }
        \ ds
    \nonumber
    \\
    & \le &
        2 t^{2} M
    .
    \nonumber
\end{eqnarray}
$$

Since $g(0) = 0$,

$$
\begin{eqnarray}
    \abs{
        g(k)
    }
    & = &
        \abs{
            g(k)
            -
            g(0)
        }
    \nonumber
    \\
    & \le &
        \int_{0}^{k}
            \abs{
                g^{\prime}(s)
            }
        \ ds
    \nonumber
    \\
    & \le &
        2 M
        \int_{0}^{k}
            s^{2}
        \ ds
    \nonumber
    \\
    & = &
        \frac{
            2 k^{3}
        }{
            3
        }
        M
    \nonumber
    \\
    & = &
        \frac{
            (b - a)^{3}
        }{
            12
        }
        \abs{f^{(2)}}_{L^{\infty}[a, b]}
    .
    \nonumber
\end{eqnarray}
$$

#### Compound trapezoidal rule

$$
\begin{eqnarray}
    h
    & := &
        \frac{
            b - a
        }{
            h
        }
    \nonumber
    \\
    x_{j}
    & := &
        a
        +
        jh
        \quad
        (j = 0, \ldots, n)
    \nonumber
\end{eqnarray}
$$

By applying trapezoidal rule to $$[x_{i-1}, x_{i}]$$,

$$
\begin{eqnarray}
    I(f)
    & \approx &
        \sum_{i=1}^{n}
            T(f; x_{i-1}, x_{i})
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            T(f; x_{i-1}, x_{i})
\end{eqnarray}
    
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
- [Tanh\-sinh quadrature \- Wikipedia](https://en.wikipedia.org/wiki/Tanh-sinh_quadrature)
