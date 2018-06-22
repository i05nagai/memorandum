---
title: Numerical Integration
---

## Numerical Integration


## Problem
* $N \in \mathbb{N}$,
* $f: \mathbb{R}^{N} \rightarrow \mathbb{R}$,
    * integralble

$$
    J^{N}
    :=
    \{
        (a_{1}, b_{1})
        \times
        \cdots
        \times
        (a_{N}, b_{N})
        \mid
        a_{i} \in \mathbb{R},
        \
        b_{i} \in \mathbb{R},
        \
        a_{i} < b_{i}
    \}
$$

$$
    I
    :=
    \int_{a}^{b}
        f(x)
    \ dx
$$

The numerical integrator $Q[a, b]$ is an approximation of $I$.
The numerical error $\epsilon$ of the approximation is defined by

$$
    \epsilon
    \approx
    \left|
        I
        -
        Q[a, b]
    \right|
    .
$$

## Methods
* Simpson rules
* Closed Newton-Cotes Formulas

## Reference
