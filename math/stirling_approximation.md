---
title: Stirling's approximation
---

## Stirling's approximation

$$
\begin{eqnarray}
    \ln n!
    & = &
        \sum_{i=1}^{n}
            \ln i
    \nonumber
    \\
    & \le &
        \int_{1}^{n}
            \ln x
        \ dx
    \nonumber
    \\
    & = &
        n \ln n
        -
        (n - 1)
    \nonumber
\end{eqnarray}
    .
$$

## Theorem

$$
\begin{equation}
    n!
    =
    \sqrt{2 \pi n}
    \left(
        \frac{n}{e}
    \right)^{n}
    \left(
        1
        +
        O
        \left(
            \frac{1}{n}
        \right)
    \right)
\end{equation}
$$

## proof

$$
\begin{eqnarray}
    \ln n!
    & = &
        \sum_{i=1}^{n}
            \ln i
    \nonumber
    \\
    \int_{1}^{n}
        \ln x
    \ dx
    & = &
        n \ln n
        -
        (n - 1)
    \nonumber
\end{eqnarray}
    .
$$

$$
\begin{eqnarray}
    f(i)
    & := &
        \ln i
    \nonumber
    \\
    k > 0,
    \
    f^{(k)}(i)
    & = &
        (-1)^{k + 1}
        \frac{(k - 1)!}{i^{k}}
    \nonumber
    \\
    \ln n!
    & = &
        \sum_{i=1}^{n}
            f(i)
    \nonumber
\end{eqnarray}
    .
$$

$$
\begin{eqnarray}
    \sum_{i=1}^{n}
        \ln i
    -
    (n \ln n - (n -1))
    & = &
        \sum_{i=1}^{n}
            \ln i
        -
        n \ln n
        +
        n - 1
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            f(i)
        -
        \int_{1}^{n}
            f(x)
        \ dx
    \nonumber
    \\
    & = &
        \sum_{k=1}^{p}
            \frac{B_{k}}{k!}
            \left(
                f^{(k-1)}(n)
                -
                f^{(k-1)}(1)
            \right)
            +
            R_{n, p}
        \quad
        (\because \text{Euler-Maclaurin formula})
    \nonumber
    \\
    & = &
        B_{1}
        (
            \ln n
            -
            \ln 1
        )
        +
        \sum_{k=2}^{p}
            \frac{B_{k}}{k!}
            \left(
                (-1)^{k}
                \frac{(k - 2)!}{n^{k-1}}
                -
                (-1)^{k}
                (k - 2)!
                1
            \right)
            +
            R_{n, p}
    \nonumber
    \\
    & = &
        \frac{1}{2}
            \ln n
        +
        \sum_{k=2}^{p}
            (-1)^{-1}
            \frac{B_{k}}{(k - 1)k}
            \left(
                \frac{1}{n^{k-1}}
                -
                1
            \right)
        +
        R_{n, p}
    \label{equation_euler_maclaurin_formula}
\end{eqnarray}
$$

where $B_{k}$ is Bernoulli number (especially $B_{1}=1/2$) and $R_{n, p}$ is $p$-th remainder term in Euler-Maclaurin formula.

Arranging the above equation and taking the limit as $n \rightarrow \infty$,

$$
    y
    :=
    \lim_{n \rightarrow \infty}
    \left(
        \sum_{i=1}^{n}
            \ln i
        -
        n \ln n
        +
        n
        -
        \frac{1}{2}
            \ln n
    \right)
    =
    1
    -
    \sum_{k=2}^{p}
        (-1)^{k}
        \frac{B_{k}}{(k - 1)k}
    +
    \lim_{n \rightarrow \infty}
    R_{n, p}
    .
$$

By Euler-Maclaurin formula,

$$
\begin{eqnarray}
    R_{n, p}
    & = &
        \lim_{n^{\prime} \rightarrow \infty}
            R_{n^{\prime}, p}
        +
        O
        \left(
            \frac{1}{n^{p}}
        \right)
        \quad
        (\because \text{Euler-Maclaurin formula})
    \nonumber
    \\
    & = &
        y
        -
        1
        +
        \sum_{k=2}^{p}
            (-1)^{k}
            \frac{B_{k}}{(k - 1)k}
        +
        O
        \left(
            \frac{1}{n^{p}}
        \right)
        \nonumber
\end{eqnarray}
$$

Hence
$$\eqref{equation_euler_maclaurin_formula}$$

$$
\begin{eqnarray}
    & &
        \sum_{i=1}^{n}
            \ln i
        -
        n \ln n
        +
        n - 1
        =
        \frac{1}{2}
            \ln n
        +
        \sum_{k=2}^{p}
            (-1)^{-1}
            \frac{B_{k}}{(k - 1)k}
            \left(
                \frac{1}{n^{k-1}}
                -
                1
            \right)
        +
        R_{n, p}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{i=1}^{n}
            \ln i
        -
        n \ln n
        +
        n \ln e
        =
        \frac{1}{2}
            \ln n
        +
        \sum_{k=2}^{p}
            (-1)^{-1}
            \frac{B_{k}}{(k - 1)k}
            \left(
                \frac{1}{n^{k-1}}
                -
                1
            \right)
        +
        y
        +
        \sum_{k=2}^{p}
            (-1)^{k}
            \frac{B_{k}}{(k - 1)k}
        +
        O
        \left(
            \frac{1}{n^{p}}
        \right)
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{i=1}^{n}
            \ln i
        +
        n \ln
            \left(
                \frac{e}{n}
            \right)
        =
        \frac{1}{2}
            \ln n
        +
        \sum_{k=2}^{p}
            (-1)^{-1}
            \frac{B_{k}}{(k - 1)k}
            \frac{1}{n^{k-1}}
        +
        y
        +
        O
        \left(
            \frac{1}{n^{p}}
        \right)
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{i=1}^{n}
            \ln i
        =
        n \ln
            \left(
                \frac{n}{e}
            \right)
        +
        \frac{1}{2}
            \ln n
        +
        \sum_{k=2}^{p}
            (-1)^{-1}
            \frac{B_{k}}{(k - 1)k}
            \frac{1}{n^{k-1}}
        +
        y
        +
        O
        \left(
            \frac{1}{n^{p}}
        \right)
\end{eqnarray}
$$

Taking the exponential of both sides,

$$
\begin{eqnarray}
    & &
        n!
        =
        \left(
            \frac{n}{e}
        \right)^{n}
        n^{1/2}
        \exp
        \left(
            \sum_{k=2}^{p}
                (-1)^{-1}
                \frac{B_{k}}{(k - 1)k}
                \frac{1}{n^{k-1}}
        \right)
        e^{y}
        \exp
        \left(
            O
            \left(
                \frac{1}{n^{p}}
            \right)
        \right)
    \nonumber
    \\
    & \Leftrightarrow &
        n!
        =
        \left(
            \frac{n}{e}
        \right)^{n}
        n^{1/2}
        \exp
        \left(
            \sum_{k=2}^{p}
                (-1)^{-1}
                \frac{B_{k}}{(k - 1)k}
                \frac{1}{n^{k-1}}
        \right)
        e^{y}
        \exp
        \left(
            O
            \left(
                \frac{1}{n^{p}}
            \right)
        \right)
\end{eqnarray}
$$

Let $p=1$.

$$
\begin{eqnarray}
    n!
    =
    \left(
        \frac{n}{e}
    \right)^{n}
    n^{1/2}
    \exp
    \left(
        \sum_{k=2}^{p}
            (-1)^{-1}
            \frac{B_{k}}{(k - 1)k}
            \frac{1}{n^{k-1}}
    \right)
    e^{y}
    \exp
    \left(
        O
        \left(
            \frac{1}{n^{p}}
        \right)
    \right)
\end{eqnarray}
$$

## Reference
* [Stirling's approximation \- Wikipedia](https://en.wikipedia.org/wiki/Stirling%27s_approximation)
