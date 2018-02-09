---
title: Gauss-Newton Method
---

# Gauss-Newton Method

## Symbol
* $x = (x_{1}, \ldots, x_{N})^{T} \in \mathbb{R}^{N}$

## Definition
* $f^{i}(\cdot) := f(\cdot; \theta_{i}): \mathbb{R}^{N} \rightarrow \mathbb{R} (\forall i = 1, \ldots, M)$
    * $\theta_{i} \in \mathbb{R}^{K}$をパラメータとする$N$変数関数
* $f(\cdot) = (f^{1}(\cdot), \ldots, f^{M}(\cdot))^{T}: \mathbb{R}^{N} \rightarrow \mathbb{R}^{M} $
    * $\theta \in \mathbb{R}^{K}$をパラメータとする$N$変数$M$次元ベクトル値関数

## Problem
以下で定義される$S(x)$が$S(x) = 0$となる$x$を見つける問題を考える。

$$
\begin{equation}
    S(x)
        := \sum_{i=1}^{M} r^{i}(x)^{2}
        := \sum_{i=1}^{M} \left( y^{i} - f^{i}(x) \right)^{2}  \in \mathbb{R}
\end{equation}
$$

ここで、$y = (y^{1}, \ldots, y^{M}) \in \mathbb{R}^{M}$である。
$r(x) = (r^{1}(x), \ldots, r^{M}(x))$は残差を表し、$r^{i}(x) = y^{i} - f^{i}(x)$である。
またベクトル表記で

$$
\begin{equation}
    S(x)
    = \left\| r(x) \right\|^{2}
    = \left\| y - f(x) \right\|^{2}
\end{equation}
$$

とも書く。
以下で述べるようにGauss-Newton法は、関数$f$とある真値のベクトル$y$との2乗誤差を最小にする問題に対する効率的なNewton法と見なせる。

## Theory

$f^{i}$の$x$の周りでの1次近似（Taylor展開）を考える。

$$
f^{i}(x + \delta) \approx  f^{i}(x) + J^{i}(x)\delta
$$

ここで、$\delta \in \mathbb{R}^{N}$, $J^{i}(x)$は$x$での$f^{i}$のヤコビ行列である。

$S(x)$に$f$の線形近似を代入すると

$$
    S(x + \delta)
    = \left\|y - f(x + \delta) \right\|^{2}
    \approx \sum_{i=1}^{M} \left( y_{i} - f^{i}(x) - J^{i}(x)\delta \right)^{2}
    =: \tilde{S}(x, \delta)
$$

となる。
右辺を展開すると

$$
\begin{eqnarray*}
    \tilde{S}(x, \delta)
    & = &
        \left\|y - f(x) - J(x)\delta \right\|^{2}
    \\
    & = &
        \left(y - f(x) - J(x)\delta \right)^{T}\left(y - f(x) - J(x)\delta \right)
    \\
    & = &
        \|y - f(x)\|^{2} - (y - f(x))^{T}J(x)\delta
        - \delta^{T}J^{T}(x)(y - f(x)) + \delta^{T}J^{T}(x)J(x)\delta
    \\
    & = &
        \|y - f(x)\|^{2} - 2(y - f(x))^{T}J(x)\delta + \delta^{T}J^{T}(x)J(x)\delta
\end{eqnarray*}
$$

となる。
ここで、$\delta$に関する$\tilde{S}(x, \delta)$の微分を考える。
$J^{T}(x)J(x)$が対称行列となっていることに注意すると、第3項は$J^{T}(x)J(x)$についての2次形式だから

$$
\frac{\partial \tilde{S}(x, \delta)}{\partial \delta}
    = 0 - 2J(x)^{T}(y - f(x)) + 2J^{T}(x)J(x)\delta
$$

である。
微分値が0とおいて上式を整理する。

$$
\begin{eqnarray}
    \frac{\partial \tilde{S}(x, \delta)}{\partial \delta} & = & 0 \\
    \Leftrightarrow J^{T}(x)J(x)\delta & = & J(x)^{T}(y - f(x)) \\
    \Leftrightarrow \delta & = & \left( J^{T}(x)J(x) \right)^{-1} J(x)^{T}(y - f(x)) \\
    \Leftrightarrow \delta & = & \left( J^{T}(x)J(x) \right)^{-1} J(x)^{T}r(x)
    \label{eq:delta-update}
\end{eqnarray}
$$

つまり、$\tilde{S}(x, \delta)$は$\delta$が$\eqref{eq:delta-update}$の時、極値をとる。
$\tilde{S}$が$S$の良い近似になっているとすれば、$\eqref{eq:delta-update}$で$x$を更新すれば良い。
よって、$x$の次の値を次のようにとる。

$$
\begin{equation}
    x_{\mathrm{next}} = x + \left( J^{T}(x)J(x) \right)^{-1} J(x)^{T}r(x)
    \label{eq:x-update}
\end{equation}
$$

このように、$x$の値を更新し、$S(x)$が十分小さくなるまで繰り返すのがGauss-Newton法となる。
式の導出の概略を下記に示した。

1. $f(x)$の線形近似を考える
2. $S(x)$を、$f$の線形近似で近似したものを$\tilde{S}$とおく
3. $\tilde{S}$が極小となる$x$を見つける
4. $S(x)$が十分0に近ければ終了
5. そうでなければ2に戻る

### Remark
上記では、ヤコビ行列を$f$のヤコビ行列とした。
$r$の$x$に対するヤコビ行列$J_{r}$とすると、

$$
\frac{\partial r(x)}{\partial x} 
    = - \frac{\partial f(x)}{\partial x} 
    = - J(x)
$$

となる。
よって、$r$のヤコビ行列を考える場合は$\eqref{eq:delta-update}$は

$$
\begin{eqnarray}
    \delta & = & - \left( J_{r}^{T}(x)J_{r}(x) \right)^{-1} J_{r}(x)^{T}(y - f(x)) \\
    \Leftrightarrow \delta & = & - \left( J_{r}^{T}(x)J_{r}(x) \right)^{-1} J_{r}(x)^{T}r(x)
    \label{eq:delta-update-with-residual}
\end{eqnarray}
$$

となる。
また、更新式$\eqref{eq:x-update}$は以下となる。

$$
\begin{equation}
    x_{\mathrm{next}} = x - \left( J_{r}^{T}(x)J_{r}(x) \right)^{-1} J_{r}(x)^{T}r(x)
    \label{eq:x-update-with-residual}
\end{equation}
$$

## Algorithm

## Good

## Bad

## Reference
* [Gauss–Newton algorithm - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm)
