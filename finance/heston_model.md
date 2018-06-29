---
title: Heston Model
---

## Heston Model

$$
\begin{eqnarray}
    X_{1}(t)
    & = &
        x_{1}
        +
        \int_{0}^{t}
            \mu
            X_{1}(s)
        \ ds
        +
        \int_{0}^{t}
            X_{1}(s)
            \sqrt{X_{2}(s)}
        \ dW^{1}(s)
    \\
    X_{2}(t)
    & = &
        x_{2}
        +
        \int_{0}^{t}
            \alpha
            (\theta - X_{2}(s))
        \ ds
        +
        \int_{0}^{t}
            \beta
            \sqrt{X_{2}(s)}
        \ dW^{2}(s)
\end{eqnarray}
$$

This can be write with vector fields

$$
\begin{eqnarray}
    X(t)
    & = &
        \left(
            \begin{array}{c}
                X_{1}(t)
                \\
                X_{2}(t)
            \end{array}
        \right)
    \\
    & = &
        \left(
            \begin{array}{c}
                x_{1}
                \\
                x_{2}
            \end{array}
        \right)
        +
        \int_{0}^{t}
            V_{0}(X(t))
        \ ds
        +
        \int_{0}^{t}
            V_{1}(X(t))
        \ dW(s)
    \\
\end{eqnarray}
$$

where

$$
\begin{eqnarray}
    V_{0}(y)
    & := &
        \left(
            \begin{array}{c}
                \mu
                y_{1}
                \\
                \alpha
                (\theta - y_{2})
            \end{array}
        \right)
    \\
    V_{1}(t)
    & = &
        \left(
            \begin{array}{c}
                y_{1}
                \sqrt{y_{2}}
                \\
                0
            \end{array}
        \right)
    \\
    V_{2}(t)
    & = &
        \left(
            \begin{array}{c}
                0
                \\
                \beta
                    \sqrt{y_{2}}
            \end{array}
        \right)
\end{eqnarray}
$$

## Reference
* [Heston model \- Wikipedia](https://en.wikipedia.org/wiki/Heston_model)
