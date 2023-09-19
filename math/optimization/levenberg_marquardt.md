---
title: Levenberg-Marquardt method
---

# Levenberg-Marquardt method
Efficient Netwon method to minimize the square error..

## Symbols
* $x = (x_{1}, \ldots, x_{N})^{T} \in \mathbb{R}^{N}$

## Definitions
* $f^{i}(\cdot) := f(\cdot; \theta_{i}): \mathbb{R}^{N} \rightarrow \mathbb{R} (\forall i = 1, \ldots, M)$
    * $\theta_{i} \in \mathbb{R}^{K}$をパラメータとする$N$変数関数
* $f(\cdot) = (f^{1}(\cdot), \ldots, f^{M}(\cdot))^{T}: \mathbb{R}^{N} \rightarrow \mathbb{R}^{M} $
    * $\theta \in \mathbb{R}^{K}$をパラメータとする$N$変数$M$次元ベクトル値関数

## Problem
以下で定義される$S(x)$が$S(x) = 0$となる$x$を見つける問題を考える。

$$
\begin{equation}
    S(x)
    :=
    \sum_{i=1}^{M} \left( y^{i} - f^{i}(x) \right)^{2}  \in \mathbb{R}
\end{equation}
$$

ここで、$y = (y^{1}, \ldots, y^{M}) \in \mathbb{R}^{M}$である。
またベクトル表記で

$$
\begin{equation}
    S(x)
    =
    \left\| y - f(x) \right\|^{2}
\end{equation}
$$

とかける。

## Theory
Levenberg-Marquardt法は、関数$f$とある真値のベクトル$y$との2乗誤差を最小にする問題に対する効率的なNewton法である。
<a href="{{ site.baseurl }}/math/gauss_newton">Gauss-Newton法</a>と同様の議論により以下の式を得る。

$$
\begin{eqnarray}
    J^{T}(x)J(x)\delta & = & J(x)^{T}(y - f(x))
    \label{eq:delta-update}
\end{eqnarray}
$$

単純に$\eqref{eq:delta-update}$を$\delta$について解けばGauss-Newton法となる。
Levenbergは$\eqref{eq:delta-update}$を次の形に置き換えたものを提案した。

$$
\begin{equation}
    (J^{T}(x)J(x) + \lambda I)\delta = J(x)^{T}(y - f(x))
    \label{eq:delta-update-levenberg}
\end{equation}
$$

ここで、$I$は$M$次の単位行列で、$\lambda \in \mathbb{R}_{\ge 0}$である。
$\lambda$はdumping factorと呼ばれる。

## Algorithm

### Choice of dumping factor
$\alpha$, $\beta$を正の定数とする。

$$
\lambda_{k} := \alpha \min\{\| y - f(x_{k}) \|, \beta\}
$$

## Good

## Bad

## Reference
1. [Levenberg–Marquardt algorithm - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm)
2. [制約なし最小化問題に対する勾配法](http://www.orsj.or.jp/~archive/pdf/j_mag/Vol.56_J_015.pdf)
3. [Levenberg-Marquardt 法の局所収束性について](http://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1174-16.pdf)
