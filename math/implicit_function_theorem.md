---
title: Implicit Function Theorem
---

## Implicit Function Theorem
逆関数の定理、陰関数定理

## Symbol
* $f: \mathbb{R}^{N + M} \rightarrow \mathbb{R}^{M}$
* $x = (x^{1}, \ldots, x^{N})^{T} \in \mathbb{R}^{N}$
* $y = (y^{1}, \ldots, y^{M})^{T} \in \mathbb{R}^{M}$
* $g: \mathbb{R}^{N} \rightarrow \mathbb{R}^{M}$
* $|x| := \max_{i=1, \ldots, N} x^{i}$
    * max norm over $\mathbb{R}^{N}$

## Definition
$f$を$\mathbb{R}^{N} \times \mathbb{R}^{M}$の直積集合からの写像とみなし、$f(x, y) \in \mathbb{R}^{M}$と書く。
$f$の点$(a, b) \in \mathbb{R}^{N} \times \mathbb{R}^{M}$でのJacobi行列を次で定義する。

$$
(Df)(a, b) :=
\left(
    \begin{array}{cccccc}
        \frac{\partial f_{1}(a,b)}{\partial x^{1}} & \ldots & \frac{\partial f_{1}(a,b)}{\partial x^{N}} &
            \frac{\partial f_{1}(a,b)}{\partial y^{1}} & \ldots & \frac{\partial f_{1}(a,b)}{\partial y^{M}} \\ 
        \vdots & \ddots & \vdots &
            \vdots & \ddots & \vdots \\
        \frac{\partial f_{M}(a,b)}{\partial x^{1}} & \ldots & \frac{\partial f_{N}(a,b)}{\partial x^{N}} &
            \frac{\partial f_{M}(a,b)}{\partial y^{1}} & \ldots & \frac{\partial f_{M}(a,b)}{\partial y^{M}} \\
    \end{array}
\right)
$$

$$
    (df)_{p} :=
    \left(
        \begin{array}{ccc}
            \frac{\partial f^{1}(p)}{\partial x^{1}} & \ldots & \frac{\partial f^{1}(p)}{\partial x^{N}} \\
            \vdots & \ddots & \vdots \\
            \frac{\partial f^{N}(p)}{\partial x^{1}} & \ldots & \frac{\partial f^{N}(p)}{\partial x^{N}} \\
        \end{array}
    \right)
$$

とくに、$v \in \mathbb{R}^{N}$について

$$
    (df)_{p}(v) =
    \left(
        \begin{array}{ccc}
            \frac{\partial f^{1}(p)}{\partial x^{1}} & \ldots & \frac{\partial f^{1}(p)}{\partial x^{N}} \\
            \vdots & \ddots & \vdots \\
            \frac{\partial f^{N}(p)}{\partial x^{1}} & \ldots & \frac{\partial f^{N}(p)}{\partial x^{N}} \\
        \end{array}
    \right)
    \left(
        \begin{array}{c}
            v^{1} \\
            \vdots \\
            v^{N}
        \end{array}
    \right)
    =
    \left(
        \begin{array}{c}
            \sum_{j=1}^{N} \frac{\partial f^{1}(p)}{\partial x^{j}}v^{j} \\
            \vdots \\
            \sum_{j=1}^{N} \frac{\partial f^{N}(p)}{\partial x^{j}}v^{j} 
        \end{array}
    \right)
$$


## Lemma1
$U \subset \mathbb{R}^{N}$ 開集合とする。
$\phi: U \rightarrow \mathbb{R}^{N}$は$C^{1}$級写像, $K$を$U$のコンパクト部分集合とする。
このとき、$\forall \epsilon > 0$にたいして、$\exists \delta > 0$が存在して、$\forall p, q \in K, |p - q| < \delta$ならば、

$$
    |(d\phi)_{p}(v) - (d\phi)_{q}(v)| < \epsilon |v| \ \forall \in \mathbb{R}^{N}.
$$

### proof

$(d\phi)_{p}(v)$の第$i$成分を$(d\phi^{i})_{p}(v)$とかく。

$$
    \begin{eqnarray}
        |(d\phi^{i})_{p}(v) - (d\phi^{i})_{q}(v)| 
            & = & \left| \sum_{j = 1}^{N} \left( \frac{\partial \phi^{i}(p)}{\partial x^{j}} - \frac{\partial \phi^{i}(q)}{\partial x^{j}} \right)v^{j} \right| \\
            & \le & \left| \frac{\partial \phi^{i}(p)}{\partial x} - \frac{\partial \phi^{i}(q)}{\partial x} \right| \left| v \right| \\
            & \le & \sum_{j=1}^{N} \left| \frac{\partial \phi^{i}(p)}{\partial x^{j}} - \frac{\partial \phi^{i}(q)}{\partial x^{j}} \right| \left| v \right|
                \label{eq:lemma1_eq1}
    \end{eqnarray}
$$

ここで、

$$
    \frac{\partial \phi^{i}(p)}{\partial x} 
        = \left( \frac{\partial \phi^{i}}{\partial x^{1}}(p), \ldots, \frac{\partial \phi^{i}}{\partial x^{N}}(p) \right)^{T}
$$

である。
二つ目の不等式は内積の三角不等式による。
$\phi$が$C^{1}$級なので、その微分は連続である。
$K$がコンパクトであることより、$ \frac{\partial \phi^{i}(p)}{\partial x^{j}}$は一様連続である。
よって、$\forall \epsilon > 0$, $\exists \delta_{i,j} > 0$が存在して、$p, q \in K$, $|p - q| < \delta_{i,j}$について

$$
    \left| \frac{\partial \phi^{i}(p)}{\partial x^{j}} - \frac{\partial \phi^{i}(q)}{\partial x^{j}} \right| 
        \le \frac{\epsilon}{N}
$$

である。
よって、$\eqref{eq:lemma1_eq1}$は$\delta_{i} := \max_{j}\delta_{i,j}$とすれば、

$$
    |(d\phi^{i})_{p}(v) - (d\phi^{i})_{q}(v)| 
         \le \epsilon \left| v \right|
$$

となる。
以上より、$\delta := \max_{i}\delta_{i}$とすれば、

$$
    \begin{eqnarray*}
        \left| (d\phi)_{p}(v) - (d\phi)_{q}(v) \right| 
            & = & \max_{i=1, \ldots N} \left| (d\phi^{i})_{p}(v) - (d\phi^{i})_{q}(v) \right| \\
            & \le & \epsilon \left| v \right| 
    \end{eqnarray*}
$$

## Lemma2
$f$をLemma1の通りとする。
$K$を$U$のコンパクト部分集合で、$K$は凸集合とする。

$$
    M_{i,j} := \max_{p \in K} \left| \frac{\partial f^{i}}{\partial x^{j}}(p) \right|, M := \max_{i,j}M_{i,j} 
$$

とおくと、$p, q \in K$のとき、

$$
    | f(p) - f(q) | \le nM|p - q|
$$

### proof

## Theorem1(Inverse Function Theorem)

$U \subset \mathbb{R}^{N}$を開集合とする。
$f: U \rightarrow \mathbb{R}^{N}$とし、$C^{r} (1 \le r \le \infty)$級とする。
$U \ni p_{0}$において、$f$のヤコビアンが0でないならば、$f$は$p_{0}$の近傍から$f(p_{0}) \in \mathbb{R}^{N}$の近傍への$C^{r}$同型である。
すなわち、$\exists U_{0} \subset U, \exists V_{0} \subset f(U), f(p_{0}) \in V_{0}$が存在して、$\left. f \right|_{U_{0}}: U_{0} \rightarrow V_{0}$が$C^{r}$級同型となる。

### proof


## Theorem2

### proof

## Theorem3

### proof

## Reference
* [陰函数定理 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%99%B0%E5%87%BD%E6%95%B0%E5%AE%9A%E7%90%86)
