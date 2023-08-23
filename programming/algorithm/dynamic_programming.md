---
title: Dynamic Programming
---

## Dynamic Programming


#### the number of division
the number of ways to divide n items into m where `n >= m`.

$dp_{i,j}$ is the number of ways to divide j into i.

$$
    dp_{i,j}
    :=
    dp_{i}{j - 1}
    + dp_{i - 1,j}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Combinations
- $n$ types of items
- the number of items $a_{i}$

$dp_{i + 1, j}$ is the number of combinations choosing $j$ using $i$ types of items.

$$
    dp_{i + 1, j}
    :=
    dp_{i+1, j - 1}
    + dp_{i,j}
    - dp_{i, j - 1 - a_{i}}
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Longest increasing subsequences
- $a_{1}, \ldots, a_{n} \in \mathbb{Z}_{\ge 0}$

Find the largest increasing subsequences.

$dp_{i}$ is the number of the longest subsequences using $a_{1}, \ldots, a_{i}$ ending at $i$.

<div class="end-of-statement" style="text-align: right">■</div>


dp_{i,j}



## Reference
