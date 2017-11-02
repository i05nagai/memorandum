---
title: Similar Matrix
---

## Similar Matrix

## Definition
* $A$
    * $n \times n$ matrix
* $B$
    * $n \times n$ matrix

$B$ is said to be similar to an $n \times n$ matrix $A$ if there exists an $n \times n$ nonsingular matrix $C$ such that

$$
    B
    =
    C^{-1}AC
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Theorem1
* $A$
    * $n \times n$ matrix
* $C$
    * $n \times n$ nonsingular matrix

Then

* (1) $$\mathrm{rank}(C^{-1}AC) = \mathrm{rank}(A)$$,
* (2) $$\mathrm{det}(C^{-1}AC) = \mathrm{det}(A)$$,
* (3) $$\mathrm{tr}(C^{-1}AC) = \mathrm{tr}(A)$$,
* (4) $$C^{\mathrm{T}}AC$$ has same characteristic polynomial,
* (5) 
* (6)

## proof.
From Theorem 12.3.1 in Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.



<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.
