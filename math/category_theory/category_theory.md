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

Covariant hom functor $C(a, -): C \rightarrow \mathrm{Set}$ consists of

$$
\begin{eqnarray}
    C(a, -): C \rightarrow \mathrm{Set},
    \quad
    C(a, -)(b)
    & := &
        C(a, b)
    \nonumber
    \\
    f: x \rightarrow y \in \mathrm{Set},
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

Contravariant hom functor $C(-, b): C \rightarrow \mathrm{Set}$ consists of

$$
\begin{eqnarray}
    C(-, b): C \rightarrow \mathrm{Set},
    \quad
    C(-, b)(a)
    & := &
        C(a, b)
    \nonumber
    \\
    f: x \rightarrow y \in \mathrm{Set},
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

Covariant hom functor $C^{\mathrm{op}}(a, -): C^{\mathrm{op}} \rightarrow \mathrm{Set}$ consists of

$$
\begin{eqnarray}
    C^{\mathrm{op}}(a, -): C \rightarrow \mathrm{Set},
    \quad
    C^{\mathrm{op}}(a, -)(b)
    & := &
        C^{\mathrm{op}}(a, b)
    \nonumber
    \\
    f: x \rightarrow y \in \mathrm{Set},
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

Let $h: a \rightarrow a^{\prime}$.
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


Is there a natural transformation $\tau: C(a, -) \Rightarrow C(-, b)$ such that the following diagram commutes?

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
