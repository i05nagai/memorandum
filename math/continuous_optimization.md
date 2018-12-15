---
title: Continuous Optimization
---

## Continuous Optimization
連続最適化

## Theorem (Necessity)
$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$とする。
$$x^{*} \in \mathbb{R}^{n}$$が局所的最小解とする。
$f$が$$x^{*}$$の近傍で微分可能とする。
このとき以下が成立。

$$
\begin{equation}
    \nabla f(x^{*}) = 0
\end{equation}
$$

さらに、$f$が$$x^{*}$$の近傍で2回連続微分可能ならば、$$\nabla^{2} f(x^{*})$$は半正定値行列になる。

## proof.
$$\nabla f(x^{*}) \neq 0$$とする。
$d := -\nabla f(x^{*})$とおくと、

$$
\begin{equation}
    d^{\mathrm{T}} \nabla f(x^{*})
    =
    -\| \nabla f(x^{*}) \| 
    < 0
\end{equation}
$$

となる。
$f$が連続より、ある$\bar{t} > 0$が存在して

$$
\begin{equation}
    \forall t \in [0, \bar{t}],
    \quad
    d^{\mathrm{T}} \nabla f(x^{*} + t d) < 0
\end{equation}
$$

とできる。
また、平均値の定理よりある$0 < \xi < 1$が存在して

$$
\begin{equation}
    f(x^{*} + t d)
    =
    f(x^{*})
    +
    t
    d^{\mathrm{T}}
    f(x^{*} + \xi t d)
\end{equation}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Theorem (sufficiency)
$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$が二階微分可能とする。
$x^{*}$が

$$
\begin{equation}
    \nabla f(x^{*}) = 0
\end{equation}
$$

かつ、$\nabla^{2} f(x^{*})$が正定値行列ならば$x^{*}$は局所的最小解になる。

## proof.


<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [primal\-dual\.pdf](http://www.stat.cmu.edu/~ryantibs/convexopt/lectures/primal-dual.pdf)
