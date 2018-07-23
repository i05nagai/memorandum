---
title: Beta Distribution
---

## Beta Distribution
Continuous distribution.

* $\alpha > 0$,
    * parameter
* $\beta > 0$,
    * parameter
* $\mathrm{\Gamma}(\alpha)$,
    * gamma function
* $\mathrm{B}(\alpha, \beta)$,
    * beta function

$$
    \mathrm{B}(\alpha, \beta)
    :=
    \frac{
        \Gamma(\alpha)
        \Gamma(\beta)
    }{
        \Gamma(\alpha + \beta)
    },
$$

$\mathrm{Beta}(\alpha, \beta)$ is the p.d.f of Beta distribution given $\alpha$ and $\beta$.

$$
    x \in [0, 1],
    \
    \mathrm{Beta}(x; \alpha, \beta)
    :=
    \frac{
        x^{\alpha-1}
        (1 - x)^{\beta - 1}
    }{
        \mathrm{B}(\alpha, \beta)
    }
    .
$$


## Reference
* [Bernoulli distribution \- Wikipedia](https://en.wikipedia.org/wiki/Bernoulli_distribution)
