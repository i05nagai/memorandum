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
                \begin{array}{c}
                    n \\
                    j
                \end{array}
            \right)
            \left(
                j
                F(x)^{j-1}
                (1 - F(x))^{n-j}
                -
                n
                F(x)^{j}
                (1 - F(x))^{n-j -1}
                +
                j
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
        f(x)
        \left(
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
                \right)
            -
            \sum_{j=k}^{n-1}
                \left(
                    \begin{array}{c}
                        n \\
                        j
                    \end{array}
                \right)
                \left(
                    n
                    F(x)^{j}
                    (1 - F(x))^{n-j -1}
                \right)
            +
            \sum_{j=k}^{n-1}
                \left(
                    \begin{array}{c}
                        n \\
                        j
                    \end{array}
                \right)
                \left(
                    j
                    F(x)^{j}
                    (1 - F(x))^{n-j -1}
                \right)
            +
            n
            F(x)^{n-1}
        \right)
    \nonumber
    \\
    & = &
        f(x)
        \left(
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
                \right)
            -
            \sum_{j=k}^{n-1}
                \left(
                    \begin{array}{c}
                        n \\
                        j
                    \end{array}
                \right)
                \left(
                    n
                    F(x)^{j}
                    (1 - F(x))^{n-j -1}
                \right)
            +
            \sum_{j=k}^{n-1}
                \left(
                    \begin{array}{c}
                        n \\
                        j
                    \end{array}
                \right)
                \left(
                    j
                    F(x)^{j}
                    (1 - F(x))^{n-j -1}
                \right)
            +
            n
            F(x)^{n-1}
        \right)
\end{eqnarray}
$$

For $X_{(n)}$ and $X_{(1)}$, it's simply

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

The distribution of $X_{(k)}$ is the probablity of the event where at least $k$ of $X_{i}$ is less than $x$, which is equivalent to the event where the value which is less than $x$ occurs more than $k$ times in $n$ trials.

#### Proposition
- $a, b, c \in \mathbb{R}$, $c > 0$,
- $X_{i}$ is uniformly distirbuted in $[a, a + c]$

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
$F_{X_{(k)}}$ is the probability that $k-1$ samples is less than $a$ and at least one sample is in $[a, a + c]$.

$$
\begin{eqnarray}
    F_{X_{(k)}}(x)
    & = &
        \sum_{j=k}^{n}
            \frac{
                n!
            }{
                (n - j)!j!
            }
            x^{j}(1 - x)^{n-j}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    f_{X_{(k)}}(x)
    & = &
        \sum_{j=k}^{n}
            \frac{
                n!
            }{
                (n - j)!j!
            }
            \left(
                j x^{j - 1}
                (1 - x)^{n-j}
                +
                (n - j)
                x^{j}
                (1 - x)^{n-j - 1}
            \right)
    \nonumber
    \\
    & = &
        \sum_{j=k}^{n}
            \left(
                \frac{
                    n!
                }{
                    (n - j)!(j - 1)!
                }
                x^{j - 1}
                (1 - x)^{n-j}
                +
                \frac{
                    n!
                }{
                    (n - j - 1)!j!
                }
                x^{j}
                (1 - x)^{n - j - 1}
            \right)
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
- [Order statistic \- Wikipedia](https://en.wikipedia.org/wiki/Order_statistic)
