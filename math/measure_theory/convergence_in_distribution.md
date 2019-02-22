---
title: Convergence in Distribution
---

## Convergence in Distribution


#### Definition
* $$\{(\Omega_{n}, \mathcal{F}_{n}, P_{n})\}_{n \in \mathbb{N}}$$,
    * probability space
* $(\Omega, \mathcal{F}, P)$,
    * probability space,
* $(S, \rho)$,
    * metric space
* $$\{X_{n}\}$$,
    * r.v. on $$(\Omega_{n}, \mathcal{F}_{n}, P_{n})$$
* $X$,
    * r.v. on $$(\Omega, \mathcal{F}, P)$$

$$\{X_{n}\}_{n \in \mathbb{N}}$$ is said to converges to $X$ in distribution and write $X_{n} \overset{d}{\rightarrow} X$ if $$\{P_{n}X_{n}^{-1}\}$$ converges wealkly to $PX^{-1}$.
That is, for all bounded continuous real-valued function $f$,

$$
    \lim_{n \rightarrow \infty}
        \mathrm{E}_{n}
        \left[
            f(X_{n})
        \right]
    =
    \mathrm{E}
    \left[
        f(X)
    \right]
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
