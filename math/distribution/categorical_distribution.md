---
title: Categorical Distribution
---

## Categorical Distribution
Categorical Distribution is one of the generalization of Bernoulli distribution.
It is also called generalized Bernoulli distribution, multinoulli distribution.

* $K \in \mathbb{N}$,

$$
    \Delta_{K}
    :=
    \{
        (p_{1}, \ldots, p_{K})
        \in
        [0,1]^{K}
        \mid
        \sum_{i=1}^{K}
            p_{i}
        =
        1
    \}
    .
$$

$\mathrm{Categ}(x; p)$ is a p.d.f. of categorical distribution given $p \in \Delta_{K}$ defined by

$$
    x \in \{1, \ldots, K\},
    \
    \mathrm{Categ}(x; p)
    :=
    \sum_{i=1}^{K}
        1_{i = x}
        p_{i}
    .
$$


## Reference
* [Categorical distribution \- Wikipedia](https://en.wikipedia.org/wiki/Categorical_distribution)
