---
title: Multinomial distribution
---

## Multinomial distribution
* $N \in \mathbb{N}$,
    * given
* $K \in \mathbb{N}$,
    * given
* $p_{i} \in [0, 1]$,
    * given
    * probability
* $$[0:K] := \{0, 1, \ldots, K\}$$,
* $$X_{1}, \ldots, X_{N} \in [0:K]$$,
    * r.v.

$$
    \mathcal{A}
    :=
    \{
        (x_{1}, \ldots, x_{N}) \in [0:K]^{N}
        \mid
        \sum_{i=1}^{N}
            x_{i}
        =
        K
    \}
    .
$$

$\mathrm{Mult}(x_{1}, \ldots, x_{N}; p_{1}, \ldots, p_{N})$ is a p.d.f. of binomial distribution given $p$ and $N$ defined by

$$
    (x_{1}, \ldots, x_{N})
    \in
    \mathcal{A},
    \
    \mathrm{Mult}(x_{1}, \ldots, x_{N}; p)
    :=
    \frac{
        K!
    }{
        x_{1}!
        \cdots
        x_{N}!
    }
    p_{1}^{x_{1}}
    \dots
    p_{N}^{x_{N}}
    .
$$

## Reference
