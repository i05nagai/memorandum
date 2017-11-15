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
        \exists \delta > 0,
        \
        \text{ s.t. }
        \
        x^{*}
        +
        th
        \in I,
        \
        \delta > \forall t > 0
    \}
$$

is said to be tangent cone of $I$.


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

<div class="end-of-statement" style="text-align: right">■</div>

### Example8 Polyhedral set

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

Corresponding tangent cone is polyhedral cone

$$
\begin{eqnarray}
    T_{I}(x^{*})
    & = &
        \{
            h \in \mathbb{R}^{n}
            \mid
            \exists \delta > 0
            \
            \text{ s.t. }
            \
            \delta > \forall t > 0,
            \
            x^{*} + t h \in I,
        \}
    \nonumber
    \\
    & = &
        \{
            h \in \mathbb{R}^{n}
            \mid
            \exists \delta > 0
            \
            \text{ s.t. }
            \
            \delta > \forall t > 0,
            \
            a_{i}^{\mathrm{T}}x^{*}
            +
            ta_{i}^{\mathrm{T}} h
            \le
            b_{i},
            \
            i = 1, \ldots, m,
        \}
    \nonumber
    \\
    & = &
        \{
            h \in \mathbb{R}^{n}
            \mid
            \forall i = 1, \ldots, m,
            \
            a_{i}^{\mathrm{T}}x^{*}
            =
            b_{i}
            \Rightarrow
            a_{i}^{\mathrm{T}} h
            \le
            0
        \}
        \label{tangent_cone_polyhedral_cone_case_equivalent_transformation}
    \\
    & = &
        \{
            h \in \mathbb{R}^{n}
            \mid
            a_{i}^{\mathrm{T}}h \le 0,
            \quad
            \forall i \in J(x^{*})
        \}
    \nonumber
    \\
    J(x^{*})
    & := &
        \{
            i \in \{1, \ldots, m\}
            \mid
            a_{i}^{\mathrm{T}}x^{*}
            =
            b_{i}
        \}
    \nonumber
\end{eqnarray}
$$

Indeed, it is obvious except for the equation $$\eqref{tangent_cone_polyhedral_cone_case_equivalent_transformation}$$.
So we only show that the equation $$\eqref{tangent_cone_polyhedral_cone_case_equivalent_transformation}$$.

($\subseteq$)

Suppose that $$a_{i}^{\mathrm{T}}x^{*} = b_{i}$$

$$
   \delta > \forall t > 0,
   \
   t a_{i} h \le 0
$$

Then $$a_{i}^{\mathrm{T}}h \le 0$$.

($\supseteq$)

Since $$x^{*} \in I$$, so that $$a_{i}^{\mathrm{T}}x^{*} \le b_{i}$$.
If $$a_{i}^{\mathrm{T}}x^{*} = b_{i}$$, then assumption says $$a_{i}^{\mathrm{T}} h \le 0$$.

On the other hand, we suppose $$a_{i}^{\mathrm{T}}x^{*} < b_{i}$$.
It is easy to check $$a_{i}^{\mathrm{T}}x^{*} + ta_{i}^{\mathrm{T}}h \le b_{i}$$ $$(\forall i)$$ holds if $$a_{i}^{\mathrm{T}}x^{*} = 0$$ $$(\forall i)$$.
Thus, we assume that there exists $$j = 1, \ldots, m$$ such that $$a_{i}^{\mathrm{T}}h \neq 0$$.
Then

$$
    \delta
    :=
    \frac{
        \min
        \{
            b_{j} - a_{j}^{\mathrm{T}}x^{*}
            \mid
            i = 1, \ldots, m,
            \
            b_{j} \neq a_{j}^{\mathrm{T}}x^{*}
        \}
    }{
        \max
        \{
            a_{j}^{\mathrm{T}}h
            \mid
            j = 1, \ldots, m,
            \
            a_{j}^{\mathrm{T}}h \neq 0
        \}
    }
$$

Hence $$\delta > \forall t > 0$$,

$$
\begin{eqnarray}
    a_{i}^{\mathrm{T}}x^{*}
    +
    ta_{i}^{\mathrm{T}}h
    & < &
        a_{i}^{\mathrm{T}}x^{*}
        +
        \min
        \{
            b_{j} - a_{j}^{\mathrm{T}}x^{*}
            \mid
            i = 1, \ldots, m,
            \
            b_{j} \neq a_{j}^{\mathrm{T}}x^{*}
        \}
    \nonumber
    \\
    & \le &
        b_{j}
    \nonumber
\end{eqnarray}
$$

Therefore the equation $$\eqref{tangent_cone_polyhedral_cone_case_equivalent_transformation}$$ holds.

Corresponding normal cone is

$$
\begin{eqnarray}
    N_{I}(x^{*})
    & = &
        \{
            x \in \mathbb{R}_{\ge 0}^{n}
            \mid
            \forall h \in T_{I}(x^{*}),
            \quad
            h^{\mathrm{T}}x \ge 0
        \}
    \nonumber
    \\
    & = &
        \{
            x \in \mathbb{R}_{\ge 0}^{n}
            \mid
            \forall h \in \mathbb{R}^{n},
            \
            \forall i \in J(x^{*}),
            \
            a_{i}^{\mathrm{T}}h \le 0
            \
            \Rightarrow
            \
            h^{\mathrm{T}}x \ge 0
        \}
    \nonumber
    \\
    & = &
        \{
            x \in \mathbb{R}_{\ge 0}^{n}
            \mid
            \forall i \in J(x^{*}),
            \quad
            h^{\mathrm{T}}a_{i} \le 0
            \
            \Rightarrow
            \
            h^{\mathrm{T}}x \ge 0
        \}
    \nonumber
    \\
    & = &
        \{
            x \in \mathbb{R}_{\ge 0}^{n}
            \mid
            \lambda \in \mathbb{R}_{\ge 0}^{m},
            \quad
            x
            =
            \sum_{i \in J(x^{*})}
                \lambda_{i}(-a_{i})
        \}
        \quad
        (\because \text{homogeneous farkas's lemma})
\end{eqnarray}
$$

See <a href="{{ site.baseurl }}/math/linear_programming.html#lemma2-homogeneous-farkas-lemma">farkas's lemma</a>.

By <a href="#remark7">remark</a>, $$x^{*}$$ is minimizer of $f$ if and only if

$$
    \exists \lambda \in \mathbb{R}_{\ge 0}^{m},
    \
    \text{ s.t. }
    \
    \nabla f(x^{*})
    =
    -
    \sum_{i \in J(x^{*})}
        \lambda_{i}^{*}
        a_{i}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Subderivative - Wikipedia](https://en.wikipedia.org/wiki/Subderivative)
* [chapitre_3.pdf](https://ljk.imag.fr/membres/Anatoli.Iouditski/cours/convex/chapitre_3.pdf)
