---
title: Stochastic Process
---

## Stochastic Process


* $$(\Omega, \mathcal{F}, P, \{\mathcal{F}_{t}\}_{0 \le t})$$,
    * probablity space with filtration
* $$(\mathbb{R}^{d}, \mathcal{B}(\mathbb{R}^{d}))$$,
    * $d$-dimentional borrel space,

### Definition. stochastic process
The collection of random variables $$X := \{X_{t} \mid 0 \le t < \infty\}$$ which take value on $$(\mathbb{R}^{d}, \mathcal{B}(\mathbb{R}^{d}))$$ is called a stochastic process.,

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. sample path
* $\omega \in \Omega$,
    * given
* $X$,
    * a stochastic process

The map $t \mapsto X_{t}(\omega)$ is called a sample path/realizatoin, trajectory of the process $X$ associated with $\omega$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. equality
* $X, Y$
    * stochastic process

$X$ and $Y$ are said to be same if

$$
    \forall t \in [0, \infty),
    \
    \forall \omega \in \Omega,
    \
    X_{t}(\omega)
    =
    Y_{t}(\omega)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. modification
* $X, Y$,
    * stochastic process

$Y$ is said to be modification of $X$ if

$$
    \forall t \in [0, \infty),
    \
    P(
        X_{t}
        =
        Y_{t}
    )
    =
    1
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. equality of finite dimensional distribution
* $X, Y$,
    * stochastic process

$X$ and $Y$ are said to have the same finite-dimensional distributions if

$$
    \forall n \in \mathbb{N},
    \
    t_{1} < t_{2} < \cdots < t_{n},
    \
    \forall A \in \mathcal{B}(\mathbb{R}^{nd}),
    \
    P(
        (X_{t_{1}}, \ldots, X_{t_{n}})
        \in
        A
    )
    =
    P(
        (Y_{t_{1}}, \ldots, Y_{t_{n}})
        \in
        A
    )
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. indistinguishable
* $X, Y$,
    * stochastic process

$X$ and $Y$ are said to be indistinguishable if

$$
    P(
        X_{t}
        =
        Y_{t}
        \mid
        t \in [0, \infty)
    )
    =
    1
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. measurable
* $X$,
    * stochastic process

$X$ is said to be measurable if

$$
    (t, \omega)
    \mapsto
    X_{t}(\omega)
    :
    \left(
        [0, \infty)
        \times
        \Omega,
        \mathcal{B}([0, \infty) \otimes \mathcal{F})
    \right)
    \mapsto
    (\mathbb{R}^{d}, \mathcal{B}(\mathbb{R}^{d}))
$$

is measurable.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. RCLL
* $X$,
    * stochastic process
* $\omega \in \Omega$,

The sample path of $X$ associated with $\omega$ is said to be càdlàg/RCLL if

$$
    \lim_{t \searrow s}
        X_{t}
    =
    X_{s},
    \
    \lim_{t \nearrow s}
        X_{t}
    <
    \infty
    .
$$

(i.e. right-continuous on $[0, \infty)$ with finite left-hand limits on $(0, \infty)$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. adapted
* $X$,
    * stochastic process

The stochastic process $X$ is said to be adapted to the filtration $$\{\mathcal{F}_{t}\}$$ if for every $t \ge 0$, $X_{t}$ is $\mathcal{F}_{t}$-measurable.

<div class="end-of-statement" style="text-align: right">■</div>


### Definition. progressively measurable
* $X$,
    * stochastic process

The stochastic process $X$ is said to be progressively measurable with respect to the filtration $$\{\mathcal{F}_{t}\}$$ if for every $t \ge 0$ 

$$
    (s, \omega)
    \mapsto
    X_{s}(\omega)
    :
    \left(
        [0, t]
        \times
        \Omega,
        \mathcal{B}([0, t] \otimes \mathcal{F}_{t})
    \right)
    \mapsto
    (\mathbb{R}^{d}, \mathcal{B}(\mathbb{R}^{d}))
$$

is measurable.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
