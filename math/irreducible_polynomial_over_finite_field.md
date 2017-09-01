---
title: Irreducible Polynomial over finite field
---

## Irreducible Polynomial over finite field

## Definition
* $GF(m)$
    * Galois field / finite field which has $m$ elements

### $GF(4)$

$$
\begin{array}{c|cccc}
    + & 0 & 1 & 2 & 3
    \\
    \hline
    0 & 0 & 1 & 2 & 3
    \\
    1 & 1 & 0 & 3 & 2
    \\
    2 & 2 & 3 & 0 & 1
    \\
    3 & 3 & 2 & 1 & 0
\end{array}
$$

$$
\begin{array}{c|cccc}
    × & 0 & 1 & 2 & 3
    \\
    \hline
    0 & 0 & 0 & 0 & 0
    \\
    1 & 0 & 1 & 2 & 3
    \\
    2 & 0 & 2 & 3 & 1
    \\
    3 & 0 & 3 & 1 & 2
\end{array}
$$

## Examples

### over $GF(4)$
Irreducible polynomials of $$GF(4)[X]$$,

* $$X$$,
* $$X + 1$$,
* $$X + 2$$,
* $$X + 3$$,
* $$X^{2} + X + 2$$,
* $$X^{2} + X + 3$$,
* $$X^{2} + 2X + 1$$,
* $$X^{2} + 2X + 2$$,
* $$X^{2} + 3X + 1$$,
* $$X^{2} + 3X + 1$$,
* $$X^{2} + 3X + 3$$,
* $$X^{3} + 2$$,
* $$X^{3} + 3$$,
* $$X^{3} + X + 1$$,
* $$X^{3} + 2X + 1$$,
* $$X^{3} + 3X + 1$$,
* $$X^{3} + X^{2} +  1$$,
* $$X^{3} + X^{2} + X + 2$$,

Reducible polynomial

* $$X^{2} + X + 1 = (X + 3)(X + 2) = X^{2} + (3 + 2)X + 3 \times 2$$,
* $$X^{2} + 2X + 3 = (X + 1)(X + 3) = X^{2} + (1 + 3)X + 1 \times 3$$,

## Reference
