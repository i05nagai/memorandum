---
title: Donsker Invariance Principle
---

## Donsker Invariance Principle


#### Definitoin 1
* $(\Omega, \mathcal{F}, P)$,
* $\sigma^{2} \in (0, \infty)$,
* $$\{\xi_{j}\}_{j \in \mathbb{N}$$,
    * I.I.D. sequence
    * mean is 0
    * variance is $\sigam$,

$$
\begin{eqnarray}
    S_{k}
    & := &
        \begin{cases}
            0
            &
                k = 0
            \\
            \sum_{j=1}^{k}
                \xi_{j}
            &
                \text{otherwise}
        \end{cases}
    \nonumber
    \\
    Y_{t}^{n}
    & := &
        S_{\lfloor t \rfloor}
        +
        (t - \lfloor t \rfloor)
        \xi_{\lfloor t \rfloor + 1}
        \
        t \ge 0
    \label{donsker_invariance_principle_def_linear_interpolation}
    \\
    X_{t}^{n}
    & := &
        \frac{1}{\sigma \sqrt{n}}
            Y_{nt}
    \label{donsker_invariance_principle_def_scale}
    \\
    P_{n}: \mathcal{B}(C[0, \infty)) \rightarrow [0, 1],
    \
    P_{n}
    & := &
        P(X^{n})^{-1}
    \label{donsker_invariance_principle_def_induced_measure}
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 1

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem The Invariance Principle of Donsker
* $(\Omega, \mathcal{F}, P)$,
* $\sigma^{2} \in (0, \infty)$,
* $$\{\xi_{j}\}_{j \in \mathbb{N}$$,
    * I.I.D. sequence
    * mean is 0
    * variance is $\sigam$,


Then $$\{P_{n}\}_{n \in \mathbb{N}}$$ converges weakly to a measure $P_{*}$ under which the coordinate mapping process $W_{t}(\omega) := \omega(t)$ is a standard one-dimensional Browninan motion.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Donsker's theorem \- Wikipedia](https://en.wikipedia.org/wiki/Donsker%27s_theorem)
