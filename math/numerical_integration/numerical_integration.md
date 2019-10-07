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
                    (a + th) - x_{j}
                }{
                    x_{i} - x_{j}
                }
        \ dt
        \quad
        (\because x = a + t h)
    \nonumber
    \\
    & = &
        \int_{0}^{n}
            \prod_{j=0, j \neq i}^{n}
                \frac{
                    t - j
                }{
                    i - j
                }
            h
        \ dt
        \quad
        (\because x_{i} = a + i h)
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            \prod_{j=0, j \neq i}^{n}
                (i - j)
        }
        \int_{0}^{n}
            \frac{
                (t - i)
                \prod_{j=0, j \neq i}^{n}
                    (t - j)
            }{
                (t - i)
            }
            h
        \ dt
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            \prod_{j=0, j \neq i}^{n}
                (i - j)
        }
        \int_{0}^{n}
            \frac{
                \prod_{j=0}^{n}
                    (t - j)
            }{
                (t - i)
            }
            h
        \ dt
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            i!
            (i - (i + 1))
            \cdots
            (i - n)
        }
        \int_{0}^{n}
            \frac{
                \prod_{j=0}^{n}
                    (t - j)
            }{
                (t - i)
            }
            h
        \ dt
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
            \frac{
                \prod_{j=0}^{n}
                    (t - j)
            }{
                (t - i)
            }
        \ dt
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
        \ dt
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

## Improper Integral

Let's consider the following problem.

- $a, b \in \bar{\mathbb{R}}$,
    - $a < b$ and ($a = \infty$ or $b = \infty$)
- $f: [a, b] \rightarrow \mathbb{R}$,

$$
\begin{eqnarray}
    I
    & := &
        \int_{a}^{b}
            f(x)
        \ dx
    \nonumber
\end{eqnarray}
$$

We say an integral $I$ is improper if one of the following conditions satisfies

- integrand goes to a finite limitting value at finite upper and lower limits, but cannot be evaluated right on one of those limits
    - e.g. $\sin(x) / x \rightarrow 1 \quad (x  \rightarrow 0)$,
- upper limit is $\infty$, lower limit is $-\infty$,
    - i.e. $f(b) = \infty$, or $f(a) = \infty$,
- integrand has integrable singularity at either upper limit or lower limit
    - e.g. $x^{-1/2}$ at 0 ($x^{-1/2} \rightarrow \infty$ as $x \rightarrow 0$,
- integrand has integrable singularity between lower limit and upper limit
    - e.g. $x^{-1/2} \rightarrow 0$,

We will consider four cases

(1) Finite interval

$$
    a, b \in (-\infty, \infty)
$$

(1-1) integrable singurarity

$$
    \exists c \in (a, b)
    \text{ s.t. }
    f(c) \text{ is integrable singularity}
    .
$$

(1-2) integrable singularity

$$
    \exists c \in (a, b)
    \text{ s.t. }
    f(c) \notin \{-\infty, \infty\}
    .
$$

(1-2-1)

$$
    f(a) \neq - \infty,
    \
    f(b) \neq  \infty
$$

Integrate over $[a, b]$ with Closed Trapezoidal.

(1-2-2)

$$
    f(a) = - \infty,
    \
    f(b) \neq  \infty
$$

Integrate over $(a, b]$ with Open/Semi-oepn Trapezoidal.

(1-2-3)

$$
    f(a) \neq - \infty,
    \
    f(b) =  \infty
$$

Integrate over $[a, b)$ with Open/Semi-oepn Trapezoidal.

(1-2-4)

$$
    f(a) = - \infty,
    \
    f(b) =  \infty
$$

Integrate over $(a, b)$ with Open/Semi-oepn Trapezoidal.

(2) Left limit is infinite

(2-1) $a = -\infty, b \neq 0$,

Apply $x(t) = 1/t$ to integrand, then go to (1).

(2-2) $a = -\infty, b \neq 0$

Apply $x(t) = 1/(1 + exp(-t))$ to integrand, then go to (1).

(3) Right limit is infinite

(3-1) $a \neq 0, b \neq \infty$,

Apply $x(t) = 1/t$ to integrand, then go to (1).

(3-2) $a = 0, b = \infty$

Apply $x(t) = 1/(1 + exp(-t))$ to integrand, then go to (1).

(4) Left and Right limit is infinite

Apply $x(t) = 1/(1 + exp(-t))$ to integrand, then go to (1).

#### (i) Variable transformations $x(t) = 1/t$

- $$(-\infty, 0) \Rightarrow (0, 1/b)$$,
- $$(0, \infty) \Rightarrow (1/a, 0)$$,

the substition $x(t) = 1 / t$ yields

$$
\begin{eqnarray}
    \int_{a}^{b}
        f(x)
    \ dx
    & = &
        -
        \int_{a}^{b}
            \frac{1}{t^{2}}
            f(\frac{1}{t})
        \ dt
    \nonumber
    \\
    & = &
        \int_{1/b}^{1/a}
            \frac{1}{t^{2}}
            f(\frac{1}{t})
        \ dt
        \
        \quad
        ab > 0
    \nonumber
\end{eqnarray}
$$

The integral would be either

$$
\begin{eqnarray}
    \int_{1/b}^{0}
        \frac{1}{t^{2}}
        f(\frac{1}{t})
    \ dt
\end{eqnarray}
$$

or

$$
\begin{eqnarray}
    \int_{0}^{1/a}
        \frac{1}{t^{2}}
        f(\frac{1}{t})
    \ dt
    .
\end{eqnarray}
$$

#### (ii) Variable transformations $x(t) = 1/t$
Let $\gamma \in [0, 1)$.
Consider a substitution $x(t) := t^{1/(1-\gamma)} + a$.

- $(a, b]$ to $[0, (b - a)^{1-\gamma})$,

$$
\begin{eqnarray}
    x(t)
    & = &
        t^{1/(1 - \gamma)}
        +
        a
    \nonumber
    \\
    x^{-1}(x)
    & = &
        (x - a)^{-\gamma}
    \nonumber
    \\
    x^{\prime}(t)
    & := &
        \frac{
            1
        }{
            1 - \gamma
        }
        t^{\gamma / (1 - \gamma)}
    \nonumber
    .
\end{eqnarray}
$$

The substitution $x(t)$ yields

$$
\begin{eqnarray}
    \int_{a}^{b}
        f(x)
    \ dx
    & = &
        \int_{0}^{(b - a)^{1-\gamma}}
            f
            \left(
                t^{1/(1 - \gamma)}
                +
                a
            \right)
            \frac{
                t^{\gamma/(1 - \gamma) }
            }{
                (1 - \gamma)
            }
        \ dt
    \nonumber
\end{eqnarray}
$$

Smiliary, the substitution $t(x) := (b - x)^{1-\gamma}$ yields

- $(a, b]$ to $[0, (b - a)^{1-\gamma})$,

$$
\begin{eqnarray}
    x(t)
    & = &
        b
        -
        t^{1/(1 - \gamma)}
    \nonumber
    \\
    x^{-1}(x)
    & = &
        (x - a)^{-\gamma}
    \nonumber
    \\
    x^{\prime}(t)
    & := &
        \frac{
            1
        }{
            1 - \gamma
        }
        t^{\gamma / (1 - \gamma)}
    \nonumber
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \int_{a}^{b}
        f(x)
    \ dx
    & = &
        \int_{(b - a)^{1-\gamma}}^{0}
            f
            \left(
                b
                -
                t^{1/(1 - \gamma)}
            \right)
            -
            \frac{
                t^{\gamma/(1 - \gamma) }
            }{
                (1 - \gamma)
            }
        \ dt
    \nonumber
    \\
    & = &
        \int_{0}^{(b - a)^{1-\gamma}}
            f
            \left(
                b
                -
                t^{1/(1 - \gamma)}
            \right)
            \frac{
                t^{\gamma/(1 - \gamma) }
            }{
                (1 - \gamma)
            }
        \ dt
\end{eqnarray}
$$

since

$$
\begin{eqnarray}
    x
    & = &
        b
        -
        t^{1/(1 - \gamma)}
    \nonumber
    \\
    t^{\prime}(x)
    & := &
        -
        (1 - \gamma)
        (b - x)^{-\gamma}
    \nonumber
    \\
    & = &
        -
        (1 - \gamma)
        t^{-\gamma/(1 - \gamma) }
    \nonumber
    .
\end{eqnarray}
$$

For example, if $\gamma := 1/2$,

$$
\begin{eqnarray}
    \int_{a}^{b}
        f(x)
    \ dx
    & = &
        \int_{0}^{(b - a)^{1/2}}
            f
            \left(
                t^{2}
                +
                a
            \right)
            2
            t
        \ dt
    \nonumber
    \\
    \int_{a}^{b}
        f(x)
    \ dx
    & = &
        \int_{0}^{(b - a)^{1/2}}
            f
            \left(
                b
                -
                t^{2}
            \right)
            2
            t
        \ dt
    \nonumber
\end{eqnarray}
$$

#### (iii) Variable transformation $x(t) := -\log t$,

- $x(t) := - \log t$,
- $x^{-1}(x) := \exp(-t)$,

$$
\begin{eqnarray}
    
\end{eqnarray}
$$

Then

$$
\begin{eqnarray}
    \int_{a}^{\infty}
        f(x)
    \ dx
    & = &
        \int_{0}^{e^{-a}}
            f(- \log t)
            \frac{1}{t}
        \ dt
    .
\end{eqnarray}
$$

From finte space to inifinite space,

$$
\begin{eqnarray}
    \int_{a}^{\infty}
        f(x)
    \ dx
    & = &
    \\
\end{eqnarray}
$$

$$
\begin{eqnarray}
    t(x)
    & := &
        \frac{1}{2}
        (b + a)
        +
        \frac{1}{2}
        (b - a)
        \tanh t
    \nonumber
    \\
    t^{\prime}(x)
    & = &
        \frac{1}{2}
        (b - a)
        \mathrm{sech}^{2} t
\end{eqnarray}
$$

#### (iv) Variable transformation $x(t) := 1 / (1 + \exp(-t))$,

$$
\begin{eqnarray}
    x(t)
    & := &
        -
        \log
        \left(
            \frac{
                1
            }{
                t
            }
            -
            1
        \right)
    \nonumber
    \\
    x^{-1}(t)
    & := &
        \frac{
            1
        }{
            1 + \exp(-t)
        }
    \nonumber
    \\
    x^{-1}(-\infty)
    & := &
        0,
    \nonumber
    \\
    x^{-1}(\infty)
    & := &
        1,
    \nonumber
    \\
    x(t)
    & := &
        -
        \frac{
            t
        }{
            1 - t
        }
        (- t^{-2})
    \nonumber
    \\
    x(t)
    & := &
        -
        \frac{
            t
        }{
            1 - t
        }
        (- t^{-2})
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            (1 - t)t
        }
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \int_{a}^{b}
        f(x)
    \ dx
    & = &
        \int_{0}^{1}
            f
            \left(
                
            \right)
            \frac{
                1
            }{
                (1 - t)t
            }
        \ dt
    \nonumber
    \\
\end{eqnarray}
$$


## Quadrature by variable transformation


#### Example 1

$$
\begin{eqnarray}
    \int_{0}^{1}
        \log x
        \log (1 - x)
    \ dx
    & = &
        2 - \frac{\pi^{2}}{6}
    .
    \nonumber
\end{eqnarray}
$$

Apply Double Exponential rule.

<div class="end-of-statement" style="text-align: right">■</div>

#### Example2

$$
\begin{eqnarray}
    \int_{0}^{\infty}
        \frac{
            1
        }{
            x^{1/2}(1 + x)
        }
    \ ex
    & = &
        \pi
    .
    \nonumber
\end{eqnarray}
$$

Double exponential with $c = \pi / 2$ within $(-4, 4)$.
TANH rule within $(-90, 90)$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Example3

$$
\begin{eqnarray}
    \int_{0}^{\infty}
        x^{-3/2}
        \sin(\frac{x}{2}
        e^{-x}
    \ dx
    & = &
        (\pi (\sqrt{5} - 2))^{1/2}
    .
    \nonumber
\end{eqnarray}
$$

Apply $x = \exp(t - e^{-t})$ within $(-4.5, 5)$.

- (1) 

<div class="end-of-statement" style="text-align: right">■</div>

#### Example4

$$
\begin{eqnarray}
    \int_{0}^{\infty}
        x^{-2/7}
        e^{-x^{2}}
    \ ex
    & = &
        \frac{1}{2}
        \Gamma(\frac{5}{14})
    \nonumber
\end{eqnarray}
$$

Apply $x = \exp(t - e^{-t})$ within $(-4, 3)$.

<div class="end-of-statement" style="text-align: right">■</div>

Let's consider the following integral.

$$
    I
    :=
    \int_{-\infty}^{\infty}
        f(x(t))
        x^{\prime}(t)
    \ dt
    .
$$

With the trapezoidal rule, we approximate the integral $I$ as

$$
\begin{eqnarray}
    I_{h}
    & := &
        h
        \sum_{n=-\infty}^{\infty}
            f(x(t))
            x^{\prime}(t)
    .
\end{eqnarray}
$$

For computational reason, we 

$$
\begin{eqnarray}
    I_{h, N}
    & := &
        h
        \sum_{n=-N}^{N}
            f(x(t))
            x^{\prime}(t)
    .
\end{eqnarray}
$$

#### Discretization error

$$
    e_{d}(h)
    :=
    \norm{
        I - I_{h}
    }
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Truncation/Trimming error

$$
    e_{t}(h, N)
    :=
    \norm{
        I_{h}
        -
        I_{h, N}
    }
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

Discretization error for TANH rule is 

$$
\begin{eqnarray}
    e_{t}(N)
    & = &
        O(e^{-2Nh})
    \nonumber
\end{eqnarray}
$$


## Gausiaan quadrature
- [Gaussian Quadrature](http://users.umiacs.umd.edu/~ramani/cmsc460/Lecture16_integration.pdf)


#### Gauss-Legendre quadrature
- [Gauss–Laguerre quadrature \- Wikipedia](https://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature)





## Reference
- [Tanh\-sinh quadrature \- Wikipedia](https://en.wikipedia.org/wiki/Tanh-sinh_quadrature)
- [part10\.pdf](http://www.maths.lth.se/na/courses/FMN050/media/material/part10.pdf)
