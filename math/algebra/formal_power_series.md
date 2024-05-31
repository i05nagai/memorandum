---
title: Formal Power Series
---

## Formal Power Series


## Division by FPS

$$
\begin{eqnarray}
    f(x)
    & = &
        \sum_{n=0}^{\infty}
            a_{n}x^{n}
    \nonumber
    \\
    g(x)
    & = &
        \sum_{n=0}^{\infty}
            b_{n}x^{n}
    \nonumber
    \\
    h(x)
    & = &
        \sum_{n=0}^{\infty}
            c_{n}x^{n}
\end{eqnarray}
$$

The division $f(x) / g(x)$ is $h(x)$ which statisfies

$$
\begin{eqnarray}
    c_{n}
    & = &
        \frac{1}{b_{0}}
        \left(
            a_{n}
            -
            \sum_{k=1}^{n}
                b_{k}c_{n - k}
        \right)
    \nonumber
\end{eqnarray}
$$

#### Example 1
- $f(x) := 1$,
- $g(x) := 1 - bx$,

$$
\begin{eqnarray}
    c_{0}
    & = &
        \frac{1}{1}
    \nonumber
    \\
    c_{1}
    & = &
        \frac{1}{1}
        \left(
            0
            -
            (-b)
        \right)
    \nonumber
    \\
    & = &
        b
    \nonumber
    \\
    c_{2}
    & = &
        \frac{1}{1}
        \left(
            0
            -
            (-b)
            b
        \right)
    & = &
        b^{2}
    \nonumber
    \\
    c_{3}
    & = &
        \frac{1}{1}
        \left(
            0
            -
            (-b)
            b^{2}
        \right)
    & = &
        b^{3}
    \nonumber
    \\
    c_{k}
    & = &
        b^{k}
\end{eqnarray}
$$

#### Example2

- $f(x) = 1$,
- $$g(x) = \sum_{n=0}^{\infty}b_{n}x^{n}$$,

$$
\begin{eqnarray}
    c_{0}
    & = &
        \frac{1}{b_{0}}
    \nonumber
    \\
    c_{1}
    & = &
        -
        \frac{1}{b_{0}}
        b_{1}
        \frac{1}{b_{0}}
        =
        -
        b_{1}
        \frac{1}{b_{0}^{2}}
    \nonumber
    \\
    c_{2}
    & = &
        \frac{1}{b_{0}}
        \left(
            +
            b_{1}
            b_{1}
            \frac{1}{b_{0}^{2}}
            -
            b_{2}
            \frac{1}{b_{0}}
        \right)
        =
        b_{1}^{2}
        \frac{1}{b_{0}^{3}}
        -
        b_{2}
        \frac{1}{b_{0}^{2}}
    \nonumber
    \\
    c_{3}
    & = &
        \frac{1}{b_{0}}
        \left(
            -
            b_{1}
            \left(
                b_{1}^{2}
                \frac{1}{b_{0}^{3}}
                -
                b_{2}
                \frac{1}{b_{0}^{2}}
            \right)
            -
            b_{2}
            \left(
                -
                b_{1}
                \frac{1}{b_{0}^{2}}
            \right)
            -
            b_{3}
            \frac{1}{b_{0}}
        \right)
        =
        -
        b_{1}^{3}
        \frac{1}{b_{0}^{4}}
        +
        b_{1}
        b_{2}
        \frac{1}{b_{0}^{3}}
        +
        b_{2}
        b_{1}
        \frac{1}{b_{0}^{3}}
        -
        b_{3}
        \frac{1}{b_{0}^{2}}
    \nonumber
    \\
    c_{n}
    & = &
        \frac{1}{b_{0}}
        \left(
            -
            \sum_{k=1}^{n}
                b_{k}
                c_{n - k}
        \right)
    \nonumber
\end{eqnarray}
$$


## Reference
- https://en.wikipedia.org/wiki/Formal_power_series
- https://en.wikipedia.org/wiki/Generating_function
