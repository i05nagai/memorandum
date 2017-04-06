---
title: Conditional Expectation
---

## Conditional Expectation

## Proposition
* $$X: \Omega \rightarrow \mathbb{R}$$,
    * 確率変数
* $\mathcal{B} \subset \mathcal{F}$
    * $\sigma$-algebra
* $f: \mathbb{R} \rightarrow \mathbb{R}$
    * $\mathcal{B}$可測

このとき、$X$と$\mathcal{B}$が独立、
$$\mathrm{E}( | f(X) | ) < \infty$$とすると

$$
    \mathrm{E}
    \left[
        f(X)
        \mid
        \mathcal{B}
    \right]
    =
    \mathrm{E}
    \left[
        f(X)
    \right]
    \mathrm{a.s.}
$$

となる。

## proof.

<div class="QED" style="text-align: right">$\Box$</div>

