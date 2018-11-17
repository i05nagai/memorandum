---
title: Introduction to Online Convex Optimization Notation
---

## Introduction to Online Convex Optimization Notation

#### Definition Categorical r.v.
* $\Delta_{n}$,
    * $n - 1$-simplex
* $x \in \Delta_{n}$,
* $$I \in \{1, \ldots, n\}$$,
    * r.v.

$I$ is said to categorical r.v. with probability $x$ if its p.d.f. is

$$
    i = 1, \ldots, n,
    \
    \mathrm{Categ}(i; x)
    :=
    \sum_{j=1}^{n}
        x_{j}
        1_{\{j = i\}}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition independent categorical r.v.s over simplex
* $\Delta_{n}$,
    * $n - 1$-simplex

Let $\mathcal{I}$ be a set of independent categorical r.v. with distribution $x \in \Delta_{n}$.
That is,

$$
    I_{1}, \ldots, I_{k} \in \mathcal{I},
    \
    P(I_{1}, \ldots, I_{k})
    =
    \prod_{i=1}^{k}
        P(I_{i})
    .
$$

$$\mathcal{I}_{\Delta_{n}}$$ is called independent categorical r.v.s over $\Delta_{n}$.

<div class="end-of-statement" style="text-align: right">■</div>

