---
title: Binary test
---

## Binary Test



## Two sample binary test
- $n_{1}$
    - sample size of sample 1
- $n_{2}$
    - sample size of sample 2
- $p_{1}$,
    - sample mean of sample 1
- $p_{2}$,
    - sample mean of sample 2
- $$x_{1}^{i} \in \{0, 1\}$$,
- $$x_{2}^{i} \in \{0, 1\}$$,

$$
\begin{eqnarray}
    \hat{p}_{j}
    :=
    \frac{
        \sum_{i=1}^{n_{j}}
            x_{j}^{i}
    }{
        n_{j}
    }
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \hat{p}
    :=
    \frac{
        n_{1} \hat{p}_{1}
        + n_{2} \hat{p}_{2}
    }{
        n_{1} + n_{2}
    }
\end{eqnarray}
$$

Then

$$
    z
    :=
    \frac{
        \hat{p}_{1} - \hat{p}_{2}
    }{
        \hat{p}(1 - \hat{p})
        \left(
            \frac{1}{n_{1}}
            +
            \frac{1}{n_{2}}
        \right)
    }
    .
$$

$z$ asymptotically follows normal distribution.
Let $Z$ be a random variable with normal distribution.
If $P(Z \le z) \le \alpha$, the null hypothesis is rejected.

## Reference
