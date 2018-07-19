---
title: Continuous Markov
---

## Continuous Markov

## Definition
* $$(\Omega, \mathcal{F}, P, (\mathcal{F}_{t})_{t \ge 0})$$,
    * probability space with fltration

### Def(Markov Process)
* $\mu$
    * Borel prob. measure over $\mathbb{R}^{d}$

$(X_{t})_{t \ge 0}$ is said to be markov process with initial distribution $\mu$ over $$(\Omega, \mathcal{F}, P)$$ if

1. $$P(X_{0} \in \Gamma) = \mu(\Gamma) \quad (\forall \Gamma \in \mathcal{B}(\mathbb{R}^{d})$$,
2. If $$s, t \ge 0$$, $$\Gamma \in \mathcal{B}(\mathbb{R}^{d})$$,

$$
    P(X_{s+t} \in \Gamma \mid \mathcal{F}_{s})
    =
    P(X_{s+t} \in \Gamma \mid X_{s})
    \quad
    \mathrm{a.s.}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Def(Markov family)
* $x \in \mathbb{R}^{d}$,
    * given

$$(X_{t}^{x})_{t \ge 0}$$ is said to be time-homogeneous markov family if

* (1) the following function $p$ is borel measurable as a function of $x$

$$
    p(t, x, \Gamma)
    :=
    P(X_{t}^{x} \in \Gamma)
    \quad
    (
        t \ge 0,
        x \in \mathbb{R}^{d},
        \Gamma \in \mathcal{B}(\mathbb{R}^{d})
    )
    .
$$

* (2) Satisfy

$$
    P(X_{0}^{x} = x)
    =
    1
    .
$$

* (3)  For $s, t \ge 0 $, $x \in \mathbb{R}^{d}$, $\Gamma \in \mathcal{B}(\mathbb{R}^{d})$,

$$
    P(X_{s+t}^{x} \in \Gamma \mid \mathcal{F}_{s})
    =
    p(t, X_{s}^{x}, \Gamma)
    \quad
    \mathrm{a.s.}
$$


The function $p$ defined in (1) is called transition function.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Markov chain \- Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
