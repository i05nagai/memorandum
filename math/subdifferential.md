---
title: Subdifferential
---

## Subdifferential
* $I \subseteq \mathbb{R}^{n}$
    * open subset
* $$f: I \rightarrow \mathbb{R}$$,
    * convex function

## Definition
$f$の$$x_{0} \in \mathbb{R}^{n}$$におけるsubderivativeを以下で定義する。

$$
    \partial_{x_{0}}f
    :=
    \{
        c \in \mathbb{R}^{n}
        \mid
        \forall x \in I,
        \
        f(x) - f(x_{0})
        \ge
        c^{\mathrm{T}} (x - x_{0})
    \}
$$

subderivativeの元を$f$の$x_{0}$でのsubderivativeという。

## Property

### Proposition
$\partial_{x_{0}} f$はclosed convex set

### proof.
$$y, z \in \partial_{x_{0}}f$$とする。
$\forall x \in I$, $\forall \lambda \in (0, 1)$とすると、

$$
\begin{eqnarray}
    (\lambda y + (1 - \lambda) z)^{\mathrm{T}}
    (x - x_{0})
    & = &
        \lambda y^{\mathrm{T}}
        (x - x_{0})
        +
        (1 -\lambda) z^{\mathrm{T}}
        (x - x_{0})
    \nonumber
    \\
    & \le &
        \lambda
        (f(x) - f(x_{0}))
        +
        (1 - \lambda)
        (f(x) - f(x_{0}))
    \nonumber
    \\
    & = &
        (f(x) - f(x_{0}))
\end{eqnarray}
$$

closeなのは、明らか。

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition
$\partial_{x_{0}} f$はclosed convex set

### proof.

<div class="QED" style="text-align: right">$\Box$</div>




## Reference
* [Subderivative - Wikipedia](https://en.wikipedia.org/wiki/Subderivative)
