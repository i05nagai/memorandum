---
title: Euler Maruyama Method
---

## Euler Maruyama Method

* $X: [0, T] \times \Omega \rightarrow \mathbb{R}$,
* $X_{0}$,
    * initial value
* $d \in \mathbb{N}$,
* $W_{i}(t)$,
    * $d$-factor Brownian motion.
* $n \in \mathbb{N}$,
    * dimension of $X$,
* $V_{i}: \mathbb{R} \rightarrow \mathbb{R}$,

$$
\begin{eqnarray}
    X(t)
    & = &
        X_{0}
        +
        \int_{0}^{t}
            V_{0}(X(s))
        \ ds
        +
        \sum_{i=1}^{d}
            \int_{0}^{t}
                V_{i}(X(s))
            \ dW(s)
    \nonumber
\end{eqnarray}
$$

## Method
$$\{Z_{i}^{n}\}_{i=1, \ldots, d}^{n=1, \ldots, N}$$ is standard normal random variables.
$$\{Z_{i}^{n}\}_{i=1, \ldots, d}^{n=1, \ldots, N}$$ are independent.

$$
\begin{eqnarray}
    Y_{0}
    & := &
        X_{0}
    \\
    Y_{n+1}
    & = &
        Y_{n}
        +
        V_{0}(Y_{n})
        h
        +
        Z_{i}^{n}
        +
        \sum_{i=1}^{d}
            V_{i}(Y_{n})
            Z_{i}^{n}
\end{eqnarray}
$$


$$
\begin{eqnarray}
    
\end{eqnarray}
$$

## Reference
* [Euler–Maruyama method \- Wikipedia](https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method)
