---
title: Gumbel Distribution
---

## Gumbel Distribution
* $\mu \in \mathbb{R}$,
    * given
* $\beta > 0$,
    * given

$\mathrm{Gu}(x; \mu, \beta)$ is a p.d.f. of gumbel distribution given $\mu$ and $\beta$ defined by

$$
\begin{eqnarray}
    \mathrm{Gu}(x; \mu, \beta)
    & := &
        \frac{1}{\beta}
        \exp
        \left(
            -
            \left(
                z
                +
                e^{-z}
            \right)
        \right)
    \nonumber
    \\
    z
    & := &
        \frac{
            x - \mu
        }{
            \beta
        }
    \nonumber
\end{eqnarray}
$$

$\mathrm{Gu}(x; \mu, \beta)$ is a c.d.f. of gumbel distribution given $\mu$ and $\beta$ defined by

$$
\begin{eqnarray}
    \mathrm{Gu}(x; \mu, \beta)
    & := &
        \exp
        \left(
            -e^{-z}
        \right)
    \nonumber
    \\
    z
    & := &
        \frac{
            x - \mu
        }{
            \beta
        }
    \nonumber
\end{eqnarray}
$$

## Reference
* [Gumbel distribution \- Wikipedia](https://en.wikipedia.org/wiki/Gumbel_distribution)
