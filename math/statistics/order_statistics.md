---
title: Order Statistics
---

## Order Statistics
- $n \in \mathbb{N}$,
- $X_{i} (i = 1, \ldots, n)$$ be random variables

$$
    X_{(k)}
    :=
    X_{\sigma(k)}
    \quad
    (X_{\sigma(1)} \le X_{\sigma(2)} \le \dots \le X_{\sigma(n)})
    .
$$

Special cases are

$$
    X_{(1)}
    :=
    \min \{X_{1}, \ldots, X_{n}\}
$$

and

$$
    X_{(n)}
    :=
    \max \{X_{1}, \ldots, X_{n}\}
    .
$$

$X_{(k)}$ is a $k$-th order statistics.


## Distributions
- $X_{i}$ is i.i.d. and continous
- $X_{i}$ has a p.d.f. 
- The cumulative distribution of $X$ is $F_{X}$

The cumulative distribution of $k$-th order statistics is given by

$$
\begin{equation}
    F_{X_{(k)}}(x)
    :=
    \sum_{i=k}^{n}
        \left(
            \begin{array}{c}
                n \\
                i
            \end{array}
        \right)
        (F_{X}(x))^{i}
        (1 - F_{X}(x))^{n - i}
        \label{equation_distribution_k_th_order_statistics}
    .
\end{equation}
$$

The p.d.f. is

$$
\begin{eqnarray}
    f_{X_{(k)}}(x)
    & = &
        \frac{d}{dx} 
        \left(
            \sum_{j=k}^{n}
                \left(
                    \begin{array}{c}
                        n \\
                        j
                    \end{array}
                \right)
                F(x)^{j}
                (1 - F(x))^{n-j}
        \right)
    \nonumber
    \\
    & = &
        \sum_{j=k}^{n-1}
            \left(
                \begin{array}{c}
                    n \\
                    j
                \end{array}
            \right)
            \left(
                j
                F(x)^{j-1}
                (1 - F(x))^{n-j}
                f(x)
                -
                f(x)
                (n-j)
                F(x)^{j}
                (1 - F(x))^{n-j -1}
            \right)
        +
        n
        F(x)^{n-1}
        f(x)
    \nonumber
    \\
    & = &
        \sum_{j=k}^{n-1}
            f(x)
            \left(
                \frac{
                    n!
                }{
                    j!(n - j)!
                }
                j
                F(x)^{j-1}
                (1 - F(x))^{n-j}
                -
                \frac{
                    n!
                }{
                    j!(n - j)!
                }
                (n - j)
                F(x)^{j}
                (1 - F(x))^{n-j -1}
            \right)
        +
        n
        F(x)^{n-1}
        f(x)
    \nonumber
    \\
    & = &
        \sum_{j=k}^{n-1}
            f(x)
            \left(
                \frac{
                    n!
                }{
                    (j - 1)!(n - j)!
                }
                F(x)^{j-1}
                (1 - F(x))^{n-j}
                -
                \frac{
                    n!
                }{
                    j!(n - j - 1)!
                }
                F(x)^{j}
                (1 - F(x))^{n- j - 1}
            \right)
        +
        n
        F(x)^{n-1}
        f(x)
    \nonumber
    \\
    & = &
        f(x)
        n
        \left(
            \sum_{j=k-1}^{n-2}
                \frac{
                    (n - 1)!
                }{
                    j!(n - 1  - j)!
                }
                F(x)^{j}
                (1 - F(x))^{n-j-1}
                -
            \sum_{j=k}^{n-1}
                \frac{
                    (n - 1)!
                }{
                    j!(n - j - 1)!
                }
                F(x)^{j}
                (1 - F(x))^{n- j - 1}
            \right)
        +
        n
        F(x)^{n-1}
        f(x)
    \nonumber
    \\
    & = &
        f(x)
        n
        \left(
            \sum_{j=k-1}^{n-2}
                \left(
                    \begin{array}{c}
                        n - 1 \\
                        j
                    \end{array}
                \right)
                F(x)^{j}
                (1 - F(x))^{n-j-1}
                -
            \sum_{j=k}^{n-1}
                \left(
                    \begin{array}{c}
                        n - 1 \\
                        j
                    \end{array}
                \right)
                F(x)^{j}
                (1 - F(x))^{n- j - 1}
            \right)
        +
        n
        F(x)^{n-1}
        f(x)
    \nonumber
    \\
    & = &
        f(x)
        n
        \left(
            \begin{array}{c}
                n - 1 \\
                k - 1
            \end{array}
        \right)
        F(x)^{k - 1}
        (1 - F(x))^{n-k}
        -
        f(x)
        n
        \left(
            \begin{array}{c}
                n - 1 \\
                n - 1
            \end{array}
        \right)
        F(x)^{n - 1}
        +
        n
        F(x)^{n-1}
        f(x)
    \nonumber
    \\
    & = &
        f(x)
        \frac{
            n!
        }{
            (k - 1)!(n - k)!
        }
        F(x)^{k - 1}
        (1 - F(x))^{n-k}
        \label{equation_pdf_k_th_order_statistics}
\end{eqnarray}
$$

For $X_{(n)}$ and $X_{(1)}$, they are simply

$$
    F_{X_{(1)}}(x)
    :=
    1 - (1 - F_{X}(x))^{n}
$$

and

$$
    F_{X_{(n)}}
    :=
    (F_{X}(x))^{n}
    .
$$

The p.d.f.s are

$$
\begin{eqnarray}
    f_{X_{(1)}}(x)
    & = &
        f(x)n(1 - F(x))^{n-1}
    \nonumber
    \\
    f_{X_{(n)}}(x)
    & = &
        nf(x)F(x)^{n-1}
\end{eqnarray}
$$

The distribution of $X_{(k)}$ is the probablity of the event where at least $k$ of $X_{i}$ is less than $x$, which is equivalent to the event where the value which is less than $x$ occurs more than $k$ times in $n$ trials.

#### Proposition
- $a, b \in \mathbb{R}$, $c > 0$,
- $X_{i}$ is uniformly distirbuted in $[a, b]$

The p.d.f. of $F_{X_{(k)}}$ is given by

$$
\begin{eqnarray}
    f_{X_{(k)}}(x)
    & = &
        \frac{
            n!
        }{
            (k - 1)!(n-k)!
        }
        x^{k-1}(1-x)^{n-k}
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            B(k, n - k + 1)
        }
        x^{k-1}(1-x)^{n-k}
\end{eqnarray}
$$

where $B(k ,n - k + 1)$ is the Beta function.

#### proof
From \eqref{equation_pdf_k_th_order_statistics},

$$
\begin{eqnarray}
    x \in [a, b],
    \
    f_{X_{(k)}}(x)
    & = &
        \frac{
            n!
        }{
            (k - 1)!(n - k)!
        }
        f(x)
        F(x)^{k-1}
        (1 - F(x))^{n-k}
    \nonumber
    \\
    & = &
        \frac{
            n!
        }{
            (k - 1)!(n - k)!
        }
        \frac{
            1
        }{
            b - a
        }
        \left(
            \frac{
                x - a
            }{
                b - a
            }
        \right)^{k-1}
        \left(
            1
            -
            \frac{
                x -a 
            }{
                b - a
            }
        \right)^{n-k}
    \nonumber
    \\
    & = &
        \frac{
            n!
        }{
            (k - 1)!(n - k)!
        }
        \frac{
            1
        }{
            b - a
        }
        \left(
            \frac{
                x - a
            }{
                b - a
            }
        \right)^{k-1}
        \left(
            \frac{
                b - x
            }{
                b - a
            }
        \right)^{n-k}
    \nonumber
    \\
    & = &
        \frac{
            n!
        }{
            (k - 1)!(n - k)!
        }
        \frac{
            1
        }{
            (b - a)^{n}
        }
        (x - a)^{k-1}
        (b - x)^{n-k}
\end{eqnarray}
$$

Since

$$
    B(k, n - k + 1)
    =
    \frac{
        (k - 1)!(n - k + 1 - 1)!
    }{
        (k + n - k + 1 - 1)!
    }
    =
    \frac{
        (k - 1)!(n - k)!
    }{
        n!
    },
$$

the equation can be written

$$
\begin{eqnarray}
    \frac{
        1
    }{
        B(k, n - k + 1)
    }
    \frac{
        1
    }{
        (b - a)^{n}
    }
    (x - a)^{k-1}
    (b - x)^{n-k}
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>


#### Proposition
- $a, b, \in \mathbb{R}$, $c > 0$,
- $X_{i}$ is uniformly distirbuted in $[a, b]$

The MLE of 


#### proof


<div class="QED" style="text-align: right">$\Box$</div>


## Descrete case
- $n \in \mathbb{N}$,
- $X_{1}, \ldots, X_{n}$,
    - i.i.d.
- $f$
    - p.d.f. of $X$,
- $F$
    - c.d.f. of $X$,

The c.d.f. of $X_{(k)}$ is the probability of the event where there are at most $n - k$ observations are greather than $x$

$$
\begin{eqnarray}
    F_{X_{(k)}}(x)
    & = &
        \sum_{j=0}^{n-k}
            \left(
                \begin{array}{c}
                    n \\
                    j
                \end{array}
            \right)
            \left(
                1 - F(x)
            \right)^{j}
            F(x)^{n - j}
    .
\end{eqnarray}
$$


$$
\begin{eqnarray}
    P(X_{(k)} < x)
    & = &
        \sum_{j=0}^{n-k}
            \left(
                \begin{array}{c}
                    n \\
                    j
                \end{array}
            \right)
            \left(
                1 - F(x) + f(x)
            \right)^{j}
            (F(x) - f(x))^{n - j}
    .
\end{eqnarray}
$$


$$
\begin{eqnarray}
    f_{X_{(k)}}(x)
    & = &
        F_{X_{(k)}}(x) - P(X_{(k)} \le x)
    \nonumber
    \\
    & = &
        \sum_{j=0}^{n-k}
            \left(
                \begin{array}{c}
                    n \\
                    j
                \end{array}
            \right)
            \left(
                1 - F(x)
            \right)^{j}
            F(x)^{n - j}
        -
        \sum_{j=0}^{n-k}
            \left(
                \begin{array}{c}
                    n \\
                    j
                \end{array}
            \right)
            \left(
                1 - F(x) + f(x)
            \right)^{j}
            (F(x) - f(x))^{n - j}
    \nonumber
    \\
    & = &
        \sum_{j=0}^{n-k}
            \left(
                \begin{array}{c}
                    n \\
                    j
                \end{array}
            \right)
            \left(
                \left(
                    1 - F(x)
                \right)^{j}
                F(x)^{n - j}
                -
                \left(
                    1 - F(x) + f(x)
                \right)^{j}
                (F(x) - f(x))^{n - j}
            \right)
\end{eqnarray}
$$


## Reference
- [Order statistic \- Wikipedia](https://en.wikipedia.org/wiki/Order_statistic)
