---
title: Conditional Expectation
---

## Conditional Expectation
条件付き期待値は構成や定義、記法に幾つか流儀があるので、ここにまとめる。

## Definition. conditional probability given sigma algebra
* $$(\Omega, \mathcal{F}, P)$$,
    * prob. sp.
* $$X: \Omega \rightarrow \mathbb{R}$$,
    * r.v.
* $\mathcal{G} \subset \mathcal{F}$
    * $\sigma$-algebra

$\mathcal{G}$可測関数$Z:\Omega \rightarrow \mathbb{R}$が存在して以下を満たすとき、$Z$を$\mathcal{G}$を与えたときの$X$の条件付き期待値という。

$$
    A \in \mathcal{G},
    \
    \int_{A}
        X(\omega)
    \ dP(\omega)
    =
    \int_{A}
        Z(\omega)
    \ dP(\omega)
$$

このとき、$g$を以下のように書く。

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G}
    \right]
    (\omega)
    :=
    Z(\omega)
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Definition. conditional probability given r.v.
* $$(\Omega, \mathcal{F}, P)$$,
    * prob. sp.
* $$X: \Omega \rightarrow \mathbb{R}$$,
    * r.v.
* $$Y: \Omega \rightarrow \mathbb{R}$$,
    * r.v.

このとき、 $$ \mathrm{E} \left[ \left.  X \right| \sigma(Y) \right] $$を$Y$を与えたときの条件付き期待値という。
このとき、

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        Y
    \right]
    (\omega)
    :=
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \sigma(Y)
    \right]
    (\omega)
$$

とかく。

<div class="end-of-statement" style="text-align: right">■</div>

## Definition. conditional probability over Y=y
* $$(\Omega, \mathcal{F}, P)$$,
    * prob. sp.
* $$X: \Omega \rightarrow \mathbb{R}$$,
    * r.v.
* $$Y: \Omega \rightarrow \mathbb{R}$$,
    * r.v.

$\mathcal{B}(\mathbb{R})$可測関数$g: \mathbb{R} \rightarrow \mathbb{R}$が存在して、以下を満たすとき、$g$を$$Y = y$$を与えたときの$X$の条件き期待値という。

$$
    \forall B \in \mathcal{B}(\mathbb{R}),
    \
    \int_{Y^{-1}(B)}
        X(\omega)
    \ dP(\omega)
    =
    \int_{B}
        g(y)
    \ dP^{Y}(y)
$$

このとき、$g$を以下のように書く。

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        Y = y
    \right]
    :=
    g(y)
    \quad
    (y \in \mathbb{R})
$$

とかく。

<div class="end-of-statement" style="text-align: right">■</div>

## Remark
$$\sigma(Y) = \{Y^{-1}(B) \mid B \in \mathcal{B}(\mathbb{R})\}$$に注意すれば以下が成り立つ。

$$
\begin{eqnarray}
    \forall B \in \mathcal{B}(\mathbb{R}),
    \
    \int_{B}
        \mathrm{E}
        \left[
        \left.
            X
        \right|
            Y = y
        \right]
    \ dP^{Y}(y)
    & = &
        \int_{Y^{-1}(B)}
            X(\omega)
        \ dP(\omega)
    \nonumber
    \\
    & = &
        \int_{Y^{-1}(B)}
            \mathrm{E}
            \left[
            \left.
                X
            \right|
                Y
            \right](\omega)
        \ dP(\omega)
\end{eqnarray}
$$

となって、定義域の違いを除けば、$Y = y$上のconditional expectationと$Y$を与えたときのconditional expectationは本質的に同じものである。

<div class="end-of-statement" style="text-align: right">■</div>

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

