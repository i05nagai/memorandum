---
title: Irreducible Polynominal
---

## Irreducible Polynominal
既約多項式について。

## Definition

### Definition. 
$f(x), g(x) \in K[x]$とする。
$f(x)$が$g(x)$の倍数であるとは、ある$q(x) \in K[x]$が存在して

$$
    f(x) = q(x)g(x)
$$

となることを言う。

### Definition
$f(x), g(x) \in K[x]$とする。
$g(x)$が$f(x)$の約数であるとは、ある$q(x) \in K[x]$が存在して

$$
    f(x) = q(x)g(x)
$$

となることを言う。


### Definition. (Irreducible Polynomial)
$f(x) \in K[x]$が既約多項式とは、以下を満たす$g, h \in K[x]$が存在しないことを言う。

$$
    \deg(g) \ge 1,
    \
    \deg(h) \ge 1,
    \
    f = gh
$$

## Operations
多項式環の演算を考える。

* $K$
    * 体
* $K[x]$
    * 1変数の$K$上の多項式環
* $x^{0} = 0 \in K$と定める

$$
    K[x]
    =
    \left\{
        \sum_{i=0}^{n}
            a_{i}x^{i}
        =
        a_{n}x^{n} + a_{n-1} x^{n-1} + \cdots + a_{0}
        \mid
        n \in \mathbb{Z}_{\ge 0},
        \
        a_{i} \in K
    \right\}
$$

* $$ f(x) = \sum_{i=0}^{n} a_{i} x^{i} \in K[x] $$,
* $$ g(x) = \sum_{i=0}^{m} b_{i} x^{i} \in K[x] $$,

### Addition
$$ n \ge m$$とする。

$$
    f(x) + g(x)
    := 
    \sum_{i=m+1}^{n}
        (a_{i} + b_{i}) x^{i}
    +
    \sum_{i=0}^{m}
        (a_{i} + b_{i}) x^{i}
$$

### multiplication
$$ n \ge m$$とする。

$$
\begin{eqnarray}
    f(x)g(x)
    & := & 
        \sum_{i = 0}^{n}
        \sum_{j = 0}^{m}
            a_{i}b_{j} x^{i+j}
    \nonumber
    \\
    & = &
        \sum_{i = 0}^{n + m}
            \left(
                \sum_{j + l = i}
                    a_{j}b_{l}
            \right)
            x^{i}
    \nonumber
    \\
    & = &
        \sum_{i = 0}^{n + m}
            \left(
                \sum_{j = 0}^{i}
                    a_{j}b_{i - j}
            \right)
            x^{i}
\end{eqnarray}
$$

## Theory

### Theorem 
* $$ f(x) = \sum_{i=0}^{n} a_{i} x^{i} \in K[x] $$,
* $$ g(x) = \sum_{i=0}^{m} b_{i} x^{i} \in K[x] $$,
    * $m \ge 1$

このとき、

$$
    f(x)
    = 
    g(x)q(x)
    +
    r(x),
    \
    \mathrm{deg}r(x) < \mathrm{deg}g(x)
$$

なる$r(x), q(x) \in K[x]$がただ一組存在する。

### proof.
まず、$\mathrm{deg}f(x) < \mathrm{deg}g(x)$ならば、$q(x) := 0$, $r(x) := f(x)$で良い。

$\mathrm{deg}f(x) \ge \mathrm{deg}g(x)$とする。
$a^{0} := a_{n}$とする。

$$
    f^{1}(x)
    :=
    f(x)
    -
    \frac{ a^{0} }{ b_{m} } x^{n - m}
    g(x)
$$

とすると、$\mathrm{deg}f^{1}(x) < \mathrm{deg}f(x)$である。
$k=1$として、$a^{k}$を$f^{k}(x)$の最高次数の係数とする。
$n^{k} := \mathrm{deg}f^{k}(x)$とする。

$$
    f^{k+1}(x)
    :=
    f^{k}(x)
    -
    \frac{ a^{k} }{ b_{m} } x^{n^{k} - m}
    g(x)
$$

とすれば$\mathrm{deg}f^{k+1}(x) < \mathrm{deg}f^{k}(x)$である。
$n$は自然数だからこれは高々$n$回の操作で$\mathrm{deg}f^{l} < \mathrm{deg}g(x)$となる。


<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [Info on primitive and irreducible polynomials](http://theory.cs.uvic.ca/inf/neck/PolyInfo.html)
* [多項式環](http://aozoragakuen.sakura.ne.jp/suuron/node51.html)
* [一意分解整域とその商体における Eisenstein の既約判定法 - konn-san.com](http://konn-san.com/math/eisenstein-criterion.html)
* [よしいずの雑記帳　GF(2)上における多項式および既約多項式のリスト](http://yoshiiz.blog129.fc2.com/blog-entry-199.html)
* [A058943 - OEIS](https://oeis.org/A058943)
