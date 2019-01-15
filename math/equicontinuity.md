---
title: Equicontinuity
---

## Equicontinuity
関数族に対する連続性。

* $(X, d_{X})$,
    * metric sp.
* $(Y, d_{Y})$,
    * metric sp.
* $F$,
    * familiy of functions from $X$ to $Y$
    * $f \in F$ is $f: X \rightarrow Y$

#### Definition.
$F$ is said to be equicontinuous at $x_{0} \in X$ if

$$
    \forall \epsilon > 0,
    \
    \exists \delta > 0,
    \
    \forall x \in X,
    \
    d_{X}(x, x_{0}) < \delta,
    \Rightarrow
    \forall f \in F,
    \
    d_{Y}(f(x_{0}), f(x)) < \epsilon
    .
$$

$x_{0}$のまわりでは、関数族全体で連続である。

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. pointwise equicontinuous
$$F$$が全ての$x \in X$でequicontinuousであるとき、$F$は pointwise equicontinuousという。

$$
    \forall x_{0} \in X,
    \
    \forall \epsilon > 0,
    \
    \exists \delta > 0,
    \
    \forall x \in X,
    \
    d_{X}(x, x_{0}) < \delta,
    \Rightarrow
    \forall f \in F,
    \
    d_{Y}(f(x_{0}), f(x)) < \epsilon
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. uniformly equicontinuous
$$F$$がuniformly equicontinuousとは

$$
    \forall \epsilon > 0,
    \
    \exists \delta > 0,
    \
    \forall x_{1}, x_{2} \in X,
    \
    d_{X}(x_{1}, x_{2}) < \delta,
    \Rightarrow
    \forall f \in F,
    \
    d_{Y}(f(x_{1}), f(x_{2})) < \epsilon
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Remark
pointwise equicontinuousと$F$の全ての関数が連続の違いは、$F$の全ての関数が連続の場合は、

$$
    \forall f \in F,
    \
    \forall x_{0} \in X,
    \
    \forall \epsilon_{f} > 0,
    \
    \exists \delta > 0,
    \
    d_{X}(x, x_{0}) < \delta
    \Rightarrow
    d_{Y}(f(x), f(x_{0})) < \epsilon_{f, x}
$$

となって、$\epsilon$は$f$に依存する。

## Reference
* [Equicontinuity - Wikipedia](https://en.wikipedia.org/wiki/Equicontinuity)

