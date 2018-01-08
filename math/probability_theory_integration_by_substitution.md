---
title: Probability Theory Integration by substitution
---

## Probability Theory Integration by substitution
* $(\Omega, \mathcal{F}, P)$,
* $d \in \mathbb{N}$,
* $A, B \subseteq \mathbb{R}^{d}$,
    * open
* $T: A \rightarrow B$
    * injection
    * $C^{1}$
    * Jacobian $J_{T}(x) \neq 0 \ (x \in A)$
* $Y:\Omega rightarrow \mathbb{R}^{d}$,
    * r.v.
* $p_{Y}$,
    * p.d.f of $Y$
* $X:\Omega rightarrow \mathbb{R}^{d}$,
    * r.v.
* $p_{X}$,
    * p.d.f of $Y$
    * p.d.f of $X$
* $X = T^{-1}(Y) \ \text{a.s.}$,
    * r.v.

$$
    p_{X}(x)
    =
    p_{Y}(T(x))
    |J_{T}(x)|
$$
