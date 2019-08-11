---
title: Uniform Continuity
---

## Uniform Continuity


#### Definition 1
* $(X, d_{X})$,
    * metric sp.
* $(Y, d_{Y})$,
    * metric sp.
* $f: X \rightarrow Y$

$f$ is said to be uniformly continuous if

$$
    \forall \epsilon > 0,
    \
    \exists \delta > 0
    \text{ s.t. }
    \forall x_{1}, x_{2} \in X,
    \
    d_{X}(x_{1}, x_{2}) < \delta
    \Rightarrow 
    d_{Y}(f(x_{1}), f(x_{2})) < \epsilon
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Uniform continuity \- Wikipedia](https://en.wikipedia.org/wiki/Uniform_continuity)
