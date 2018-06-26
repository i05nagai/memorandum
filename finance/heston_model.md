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
                \vdots 
                \\
                y_{1}
                \sqrt{y_{2}}
            \end{array}
        \right)
        +
        \int_{0}^{t}
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

## Reference
* [Heston model \- Wikipedia](https://en.wikipedia.org/wiki/Heston_model)
