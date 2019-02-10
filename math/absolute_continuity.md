---
title: Absolute Continuity
---

## Absolute Continuity

#### Definition 1
* $(X, d)$
    * metric space
* $I := [a, b]$,
* $f: I \rightarrow X$,

$$
    \mathcal{J}
    :=
    \{
        ([a_{i}, b_{i}])_{i=1,\ldots,k}
        \mid
        a_{i} \le b_{i} \le a_{i + 1}
        \
        k \in \mathbb{N}
    \}
    .
$$

$f$ is said to be absolute continuous if for all $\epsilon > 0$, there exists $\delta > 0$ such that

$$
    ([a_{i}, b_{i}])_{i = 1, \ldots, k} \in J,
    \
    \sum_{i=1}^{k}
        \abs{
            b_{i} - a_{i}
        }
    <
    \delta
    \Rightarrow
    \sum_{i=1}^{k}
        d(f(b_{i}) - f(a_{i}))
    <
    \epsilon
    .
$$

We denote the collection of all absolute functions by $\mathrm{AC}(I; X)$.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Absolute continuity \- Wikipedia](https://en.wikipedia.org/wiki/Absolute_continuity)
