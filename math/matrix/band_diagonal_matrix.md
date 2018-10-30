---
title: Band-Diagonal Matrix
---

## Band-Diagonal Matrix

* $$[i:j] := \{i, i + 1, \ldots, j\}$$,
    * if  $i < j$, $[i:j] := \emptyset$,
* $A := (a_{j}^{i})_{i, j \in [1:n]}$,
    * $n \times n$ matrix


#### Definiiton
* $q \in [0:n]$,

$A$ is said to have upper bandwidth $q$ if

$$
    j > i + q,
    \
    a_{j}^{i} = 0
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definiiton
* $p \in [0:n]$,

$A$ is said to have lower bandwidth $p$ if

$$
    i > j + p,
    \
    a_{j}^{i} = 0
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem
* $A = LU$,
    * LU decomposition of $A$

If $A$ has upper bandwidth $q$ and lower bandwidth $p$, then

* $U$ has upper bandwidth $q$,
* $L$ has lower bandwidth $p$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
