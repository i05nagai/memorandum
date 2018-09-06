---
title: Mean Value Theorem
---

## Mean Value Theorem


#### Theorem multiple variables
* $G \subseteq \mathbb{R}^{n}$,
    * convex
    * open
* $f:G \rightarrow \mathbb{R}$,
    * differentiable
* $x, y \in G$,


$$
    \exists \in [0, 1]
    \text{ s.t. }
    f(y)
    -
    f(x)
    =
    \nabla f(x + c(y - x))^{\mathrm{T}}
    (y - x)
    .
$$

#### proof
Let be define

$$
    g(t)
    :=
    f(x + t(y - x))
    .
$$

Since $g$ is differentiable, by mean value theorem for one dimentional function,

$$
    \exists c \in [0, 1]
    \text{ s.t. }
    g(1) - g(0)
    =
    g^{\prime}(c)
    .
$$

Hence

$$
    f(y)
    -
    f(x)
    =
    \nabla f(x + c(y - x))^{\mathrm{T}}
    (y - x)
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
