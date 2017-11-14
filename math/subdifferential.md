---
title: Subdifferential
---

## Subdifferential
* $I \subseteq \mathbb{R}^{n}$
    * open subset
* $$f: I \rightarrow \mathbb{R}$$,
    * convex function

## Definition1
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

### Proposition2
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

### Theorem3 Necessary and sufficient condition of optimality for convex function
* $f: I \rightarrow \mathbb{R}$
    * convex function
* $$x^{*} \in I$$,

Then (1) $$\Leftrightarrow$$ (2).

* (1) $$x^{*}$$ is the minimizer of $f$
* (2) $$0 \in \partial_{x^{*}}f$$,

### proof.
(1) $$\Rightarrow$$ (2)

By definition of subdifferential,

$$
    \forall x \in I,
    \
    f(x)
    \ge
    f(x^{*})
    +
    0^{\mathrm{T}}(x - x^{*})
    =
    f(x^{*})
    .
$$

(1) $$\Leftarrow$$ (2)

As above discussion,

$$
    \forall x \in I,
    \
    f(x)
    \ge
    f(x^{*})
    =
    f(x^{*})
    +
    0^{\mathrm{T}}(x - x^{*})
    .
$$

Hence $$0 \in \partial_{x^{*}}f$$.

<div class="QED" style="text-align: right">$\Box$</div>

### Definiton4
* $I$,
* $x^{*} \in I$,

$$
    T_{I}(x^{*})
    :=
    \{
        h \in \mathbb{R}^{n}
        \mid
        x^{*}
        +
        th
        \in I,
        \forall t > 0
    \}
$$

is said to be tangent cone of $I$.

$$
\begin{eqnarray}
    I
    & := &
        \{
            x \in \mathbb{R}^{n}
            \mid
            Ax \le b
        \}
    \nonumber
    \\
    & = &
        \{
            x \in \mathbb{R}^{n}
            \mid
            a_{i}^{\mathrm{T}}x \le b_{i},
            \quad
            i = 1, \ldots, m
        \}
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition5
* $I$
    * convex
* $$x^{*} \in I$$,
* $f$
    * differentiable at $$x^{*}$$

Then following statements are equivalent

* (1) $$x^{*}$$ is a minimizer of $f$
* (2)

$$
    \forall h \in T_{I}(x^{*})
    \quad
    h^{\mathrm{T}}
        \nabla f(x^{*})
    \ge
    0,
$$

## proof.
(1) $\Rightarrow$ (2)

Suppose that there exists $$h \in T_{I}(x^{*})$$ such that $$h^{\mathrm{T}}\nabla f(x^{*}) < 0$$.
By taylor's theorem,

$$
\begin{eqnarray}
    & &
        f(x^{*} + th) - f(x^{*})
        =
        th^{\mathrm{T}}\nabla f(x^{*})
        +
        O(t^{2}|h|^{2})
    \nonumber
    \\
    & \Rightarrow &
        \exists \delta > 0,
        \
        \forall t \in (0, \delta),
        \
        f(x^{*} + th) - f(x^{*})
        =
        th^{\mathrm{T}}\nabla f(x^{*})
        <
        0
    \nonumber
\end{eqnarray}
$$

Thus,

$$
    \forall t \in (0, \delta),
    \quad
    f(x^{*} + th) < f(x^{*})
    .
$$

Since $$ h \in T_{I}(x^{*})$$,

$$
    \forall t \in (0, \delta),
    \quad
    x^{*} + th \in I
    .
$$

Then for every neighborhood of $$x^{*}$$ we can take strictly lower than $$f(x^{*})$$.
This contradicts (1).

(1) $\Leftarrow$ (2)

If $x \in I$, then $$h := x - x^{*} \in T_{I}(x^{*})$$ since $I$ is convex.
Thus, by assumption (2),

$$
    f(x)
    \ge
    f(x^{*})
    +
    (x - x^{*}) \nabla f(x^{*})
    \ge
    f(x^{*})
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Definition6 Normal cone
* $I \subseteq \mathbb{R}^{n}$
    * convex
* $f: I \rightarrow \mathbb{R}$
    * convex on $I$

$$
    N_{I}(x^{*})
    :=
    \{
        x \in \mathbb{R}_{\ge 0}^{n}
        \mid
        \forall h \in T_{I}(x^{*})
        \
        h^{\mathrm{T}}x \ge 0
    \},
$$

is said to be normal cone.

### Remark7
By theorem, $$x^{*}$$ is minimizer of $f$ on I if and only if $$\nabla f(x^{*}) \in N_{I}(x^{*})$$.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [Subderivative - Wikipedia](https://en.wikipedia.org/wiki/Subderivative)
* [chapitre_3.pdf](https://ljk.imag.fr/membres/Anatoli.Iouditski/cours/convex/chapitre_3.pdf)
