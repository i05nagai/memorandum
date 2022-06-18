---
title: Category Theory
---

## Category Theory

## Hom-sets



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

## Reference
