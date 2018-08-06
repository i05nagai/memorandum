---
title: Introduction to Online Optimization Chapter07
---

## 7. Limited feedback

We cannot observe the adversary's move $z_{t}$.
Thus, we cannot compute $\Delta \ell(a_{t}, z_{t})$.

## 7.1 Online Stochastic Mirror Descent (OSMD)

* $\tilde{a}_{t}$,
    * random perturbation of $a_{t}$,

Pseudo regret

$$
    \bar{R}_{n}(a_{t}, z_{t})
    :=
    \mathrm{E}
    \left[
        \sum_{t=1}^{n}
            \ell(\tilde{a}_{t}, z_{t})
    \right]
    -
    \min_{a \in \mathcal{A}}
        \mathrm{E}
        \left[
            \sum_{t=1}^{n}
                \ell(a, z_{t})
        \right]
    .
$$

#### Theorem 7.1
* $

#### proof.
