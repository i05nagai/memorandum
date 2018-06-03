---
title: Binomial distribution
---

## Binomial distribution
* $N \in \mathbb{N}$,
    * given
* $p \in [0, 1]$,
    * given
    * probability
* $$X_{i} \in \{0, 1\} \ (i = 1, \ldots, N)$$,
    * i.i.d sequence of Bernoulli r.v.
    * $P(X_{i} = 0) = p \ (1, \ldots, N)$,

$\mathrm{Bi}(x_{1}, \ldots, x_{N}; p)$ is a p.d.f. of binomial distribution given $p$ and $N$ defined by

$$
    \mathrm{Bi}(x_{1}, \ldots, x_{N}; p)
    :=
    \left(
        \begin{array}{c}
            N \\
            \sum_{i=1}^{N}
                x_{i}
        \end{array}
    \right)
    p^{
        \sum_{i=1}^{N}
            x_{i}
    }
    (1 - p)^{
        N
        -
        \sum_{i=1}^{N}
            x_{i}
    }
    .
$$

$$
\begin{eqnarray}
    F_{\mathrm{Bi}}(n; p)
    & := &
    \sum_{x \in }
        \mathrm{Bi}(x_{1}, \ldots, x_{n}; p)
    \nonumber
    \\
    n \in \{0, 1, \ldots, N\},
    \
    F_{\mathrm{Bi}}(n; p)
    & := &
    \sum_{x \in }
        \mathrm{Bi}(x_{1}, \ldots, x_{n}; p)
\end{eqnarray}
$$


## Reference
