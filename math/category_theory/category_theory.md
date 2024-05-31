---
title: Category Theory
---

## Category Theory

## Why
- [What is category theory? \- Mathematics Stack Exchange](https://math.stackexchange.com/questions/724302/what-is-category-theory)
- [Zermelo–Fraenkel set theory \- Wikipedia](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory)
- [ZFC in nLab](https://ncatlab.org/nlab/show/ZFC)
- [Class \(set theory\) \- Wikipedia](https://en.wikipedia.org/wiki/Class_(set_theory))
- [Russell's paradox \- Wikipedia](https://en.wikipedia.org/wiki/Russell%27s_paradox)

Under ZFC, we cannot construct the special set which contains all sets.
We call the set $A$ assuming that such set exists.
Let us define a set

$$
    R
    :=
    \{
        x \in A
        \mid
        x \notin x
    \}
    .
$$

This is a valid set by the axiom schema of scpecificaiton.
However, since $R \in A$, this implies

$$
    R \notin R
    \Leftrightarrow
    R \in R
    .
$$

The existance of such set lead us to Russel's paradox.
The axiom schema of specification has restriciotn that subset itself is not free in $\phi$.
But $A$ bypasses this restriction.

To consider such object, and to discuss properties over all sets, category theory has to analyse outsie of ZFC axioms.


## Hom sets
- $C, D$,
    - category

$$
    C(a, b)
    :=
    \{
        f:a \rightarrow b  \in C
    \}
    .
$$

#### $C(a, -)$

Covariant hom functor $C(a, -): C \rightarrow \mathrm{Set}$ consists of object funciton

$$
\begin{eqnarray}
    C(a, -): C \rightarrow \mathrm{Set},
    \quad
    C(a, -)(b)
    & := &
        C(a, b)
    \nonumber
\end{eqnarray}
$$

and arrow funciton

$$
\begin{eqnarray}
    f: x \rightarrow y \in C,
    \quad
    C(a, -)(f): C(a, x) \rightarrow C(a, y),
    \quad
    C(a, -)(f)(g)
    & := &
        f \circ g
    \nonumber
    .
\end{eqnarray}
$$

#### $C(-, b)$

Contravariant hom functor $C(-, b): C \rightarrow \mathrm{Set}$ consists of object function

$$
\begin{eqnarray}
    C(-, b): C \rightarrow \mathrm{Set},
    \quad
    C(-, b)(a)
    & := &
        C(a, b)
    \nonumber
\end{eqnarray}
$$

and arrow function

$$
\begin{eqnarray}
    f: y \rightarrow x \in C,
    \quad
    C(-, b)(f): C(x, b) \rightarrow C(y, b),
    \quad
    C(-, b)(f)(g)
    & := &
        g \circ f
    \nonumber
    .
\end{eqnarray}
$$

#### $C^{\mathrm{op}}(a, -)$

Covariant hom functor $C^{\mathrm{op}}(a, -): C^{\mathrm{op}} \rightarrow \mathrm{Set}$ consists of arrow function

$$
\begin{eqnarray}
    C^{\mathrm{op}}(a, -): C \rightarrow \mathrm{Set},
    \quad
    C^{\mathrm{op}}(a, -)(b)
    & := &
        C^{\mathrm{op}}(a, b)
    \nonumber
\end{eqnarray}
$$

and arrow function

$$
\begin{eqnarray}
    f: x \rightarrow y \in C^{\mathrm{op}},
    \quad
    C^{\mathrm{op}}(a, -)(f): C^{\mathrm{op}}(a, x) \rightarrow C^{\mathrm{op}}(a, y),
    \quad
    C^{\mathrm{op}}(a, -)(f)(g)
    & := &
        f \circ g
    \nonumber
    .
\end{eqnarray}
$$

#### $C(F-, b)$

$F: D \rightarrow C$, Contravariant hom functor $C(F-, b): D \rightarrow \mathrm{Set}$ consists of object function

$$
\begin{eqnarray}
    C(F-, b): D \rightarrow \mathrm{Set},
    \quad
    C(F-, b)(d)
    & := &
        C(Fd, b)
    \nonumber
\end{eqnarray}
$$

and arrow function

$$
\begin{eqnarray}
    f: x \rightarrow y \in D,
    \quad
    C(F-, b)(f): C(Fx, b) \rightarrow C(Fy, b),
    \quad
    C(F-, b)(f)(g)
    & := &
        g \circ Ff
    \nonumber
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### $C(a, G-)$

$G: D \rightarrow C$, Contravariant hom functor $C(a, G-): D \rightarrow \mathrm{Set}$ consists of object function

$$
\begin{eqnarray}
    C(a, G-): D \rightarrow \mathrm{Set},
    \quad
    C(a, G-)(d)
    & := &
        C(a, Gd)
    \nonumber
\end{eqnarray}
$$

and arrow function

$$
\begin{eqnarray}
    f: x \rightarrow y \in D,
    \quad
    C(a, -)(f): C(a, Gx) \rightarrow C(a, Gy),
    \quad
    C(a, G-)(f)(g)
    & := &
        Gf \circ g
    \nonumber
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### $C(-, -)$
hom bi-functor $C(-, -): C \times C \rightarrow \mathrm{Set}$ consists of object function

$$
\begin{eqnarray}
    C(-, -): C \times C \rightarrow \mathrm{Set},
    \quad
    C(-, -)(a, b)
    & := &
        C(a, b)
    \nonumber
\end{eqnarray}
$$

and arrow function

$$
\begin{eqnarray}
    f: y \rightarrow x \in C,
    \quad
    f^{\prime}: x^{\prime} \rightarrow y^{\prime} \in C,
    \quad
    C(-, -)(f, f^{\prime}): C(x, x^{\prime}) \rightarrow C(y, y^{\prime}),
    \quad
    g: x \rightarrow x^{\prime},
    \quad
    C(-, -)(f, f^{\prime})(g)
    & := &
        f^{\prime} \circ g \circ f
    \nonumber
    .
\end{eqnarray}
$$

For all $a \in C$,

$$
\begin{eqnarray}
    f^{\prime}: x^{\prime} \rightarrow y^{\prime} \in C,
    \quad
    g: a \rightarrow x^{\prime}
    \quad
    C(-, -)(1_{a}, f^{\prime})(g)
    & = &
        C(a, -)(f^{\prime})(g)
    \nonumber
    \\
    f: y \rightarrow x \in C,
    \quad
    g: x \rightarrow a
    \quad
    C(-, -)(f, 1_{a})(g)
    & = &
        C(-, a)(f)(g)
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### $C(a, -)$ and $C(a^{\prime}, -)$

Let $h: a^{\prime} \rightarrow a$.
There is a natural transformation $\tau: C(a, -) \Rightarrow C(a^{\prime}, -)$, $\tau_{x} := C(-, x)(h)$,

$$
\begin{CD}
    x \in C
    \\
    @V{f}VV
    \\
    y \in C
\end{CD}
\quad
\begin{CD}
    C(a, -)(x) @>{\tau_{x}}>> C(a^{\prime}, -)(x)
    \\
    @V{C(a, -)(f)}VV    @V{C(a^{\prime}, -)(f)}VV
    \\
    C(a, -)(y) @>{\tau_{y}}>> C(a^{\prime}, -)(y)
\end{CD}
$$

The equality can be shown by

$$
\begin{eqnarray}
    g \in C(a, x),
    \quad
    (C(a^{\prime}, f) \circ \tau_{x})(g)
    & = &
       C(a^{\prime}, f)(\tau_{x}(g))
    \nonumber
    \\
    & = &
       f \circ \tau_{x}(g)
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    g \in C(a, x),
    \quad
    (\tau_{y} \circ C(a, f))(g)
    & = &
       \tau_{y}(f \circ g)
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### $C(-, b)$ and $C(-, b^{\prime})$

Let $k: b \rightarrow b^{\prime}$.
There is a natural transformation $\tau: C(-, b) \Rightarrow C(-, b^{\prime})$, $\tau_{x} := C(x, -)(k)$,

$$
\begin{CD}
    x \in C
    \\
    @V{f}VV
    \\
    y \in C
\end{CD}
\quad
\begin{CD}
    C(-, b)(x) @>{\tau_{x}}>> C(-, b^{\prime})(x)
    \\
    @V{C(-, b)(f)}VV    @V{C(-, b^{\prime})(f)}VV
    \\
    C(-, b)(y) @>{\tau_{y}}>> C(-, b^{\prime})(y)
\end{CD}
$$

The equality can be shown by

$$
\begin{eqnarray}
    g \in C(x, a),
    \quad
    (C(f, b^{\prime}) \circ \tau_{x})(g)
    & = &
       C(f, b^{\prime})(\tau_{x}(g))
    \nonumber
    \\
    & = &
       \tau_{x}(g) \circ f
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    g \in C(x, b),
    \quad
    (\tau_{y} \circ C(f, b))(g)
    & = &
       \tau_{y}(g \circ f)
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### $C(a, -)$ and $D(a^{\prime}, G-)$

$G: C \rightarrow D$.
Let $\tau: C(a, -) \Rightarrow D(a^{\prime}, G-)$ be a natural transformation.

$$
\begin{CD}
    x \in C
    \\
    @V{f}VV
    \\
    y \in C
\end{CD}
\quad
\begin{CD}
    C(a, -)(x) @>{\tau_{x}}>> D(a^{\prime}, G-)(x)
    \\
    @V{C(a, -)(f)}VV    @V{D(a^{\prime}, -)(f)}VV
    \\
    C(a, -)(y) @>{\tau_{y}}>> D(a^{\prime}, G-)(y)
\end{CD}
$$

The equality can be shown by

$$
\begin{eqnarray}
    g \in C(a, x),
    \quad
    (D(a^{\prime}, Gf) \circ \tau_{x})(g)
    & = &
       D(a^{\prime}, Gf)(\tau_{x}(g))
    \nonumber
    \\
    & = &
       Gf \circ \tau_{x}(g)
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    g \in C(a, x),
    \quad
    (\tau_{y} \circ C(a, f))(g)
    & = &
       \tau_{y}(f \circ g)
    \nonumber
\end{eqnarray}
$$

$\tau$ is a natural isomorphism if and only if there is a universal arrow $u: a^{\prime} \rightarrow Ga$ from $G$ to $a$.
That is, the following are equivalent.

$$
\begin{CD}
    x \in C
    \\
    @V{1_{x}}VV
    \\
    x \in C
\end{CD}
\quad
\begin{CD}
    C(a, -)(x) @>{\tau_{x}}>> D(a^{\prime}, G-)(x)
\end{CD}
$$

and

$$
\begin{CD}
    a \in C
    \\
    @V{f}VV
    \\
    x \in C
\end{CD}
\quad
\begin{CD}
    C(a, -)(a) @>{\tau_{a}}>> D(a^{\prime}, G-)(a)
    \\
    @V{C(a, -)(f)}VV    @V{D(a^{\prime}, -)(f)}VV
    \\
    C(a, -)(x) @>{\tau_{x}}>> D(a^{\prime}, G-)(x)
\end{CD}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### $C(F-, b)$ and $D(-, b^{\prime})$
$F: D \rightarrow C$.
Let $\tau: C(F-, b) \Rightarrow D(-, b^{\prime})$ be a natural transformation.

$$
\begin{CD}
    x \in D
    \\
    @V{f}VV
    \\
    y \in D
\end{CD}
\quad
\begin{CD}
    C(F-, b)(x) @>{\tau_{x}}>> D(-, b^{\prime})(x)
    \\
    @V{C(F-, b)(f)}VV    @V{D(-, b^{\prime})(f)}VV
    \\
    C(F-, b)(y) @>{\tau_{y}}>> D(-, b^{\prime})(y)
\end{CD}
$$

The equality can be shown by

$$
\begin{eqnarray}
    g \in C(Fx, a),
    \quad
    (D(f, b^{\prime}) \circ \tau_{x})(g)
    & = &
       D(f, b^{\prime})(\tau_{x}(g))
    \nonumber
    \\
    & = &
       \tau_{x}(g) \circ f
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    g \in C(Fx, b),
    \quad
    (\tau_{y} \circ C(Ff, b))(g)
    & = &
       \tau_{y}(g \circ Ff)
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### $C(a, -) \circ C(-, b)$

Let $h: x \rightarrow a$, $k: x \rightarrow b$.
There is a natural transformation $\tau: C(a, -) \Rightarrow C(-, b)$ defined by $\tau_{x} := C(x, k) \circ C(h, x) = C(h, k)$.

$$
\begin{CD}
    x \in C
    \\
    @V{f}VV
    \\
    y \in C
\end{CD}
\quad
\begin{CD}
    C(a, -)(x) @>{\tau_{x}}>> C(-, b)(x)
    \\
    @V{C(a, -)(f)}VV    @V{C(-, b)(f)}VV
    \\
    C(a, -)(y) @>{\tau_{y}}>> C(-, b)(y)
\end{CD}
$$

## Reference
- Book: An Introduction to the Language of Category Theory
