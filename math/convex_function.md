---
title: Convex function
---

## Convex Function
凸関数

## Definition
* $f: \mathbb{R}^{N}\rightarrow \mathbb{R}$

$f$が凸関数であるとは、

$$
\begin{equation}
    \forall \lambda \in [0, 1],
    \quad
    \forall x_{1}, x_{2} \in \mathbb{R}^{N},
    \quad
    f(\lambda x_{1} + (1 - \lambda)x_{2})
    \le
    \lambda f(x_{1}) + (1 - \lambda) f(x_{2})
\end{equation}
$$

を満たすことを言う。

$f$が狭義凸関数であるとは、　

$$
\begin{equation}
    \forall \lambda \in (0, 1),
    \quad
    \forall x_{1}, x_{2} \in \mathbb{R}^{N},
    \quad
    x_{1} \neq x_{2},
    \quad
    f(\lambda x_{1} + (1 - \lambda)x_{2})
    <
    \lambda f(x_{1}) + (1 - \lambda) f(x_{2})
\end{equation}
$$

## Properties

### 1
開区間で定義された凸関数は、連続

### 2
開区間で定義された凸関数は、高々加算個の点を除いて微分可能。

### 3
$f$を凸関数とする。
$f$が$C^{2}$級とすると、以下は同値。

* $f$が凸関数
* 凸集合の内部で、$f$のヘッセ行列が半正定値

### Calculus
$f:\mathbb{R}^{N} \rightarrow \mathbb{R}$, $g: \mathbb{R}^{N} \rightarrow \mathbb{R}$を凸関数とする。
$h: \mathbb{R} \rightarrow \mathbb{R}$を非減少関数とする。
$a, b \in \mathbb{R}_{\ge 0}^{d}$とする。

* $a f + b g$は凸関数
* $$\max\{f, g\}$$は凸関数
* $h(f(x))$は凸関数

### 5
$f:\mathbb{R}^{N} \rightarrow \mathbb{R}$を凸関数とする。
$a \in \mathbb{R}$とする。

レベル集合$$\{x \in \mathbb{R}^{N} \mid f(x) < a \}$$及び$$\{x \in \mathbb{R}^{N} \mid f(x) \ge a\}$$は凸集合である。

### Optimum
* 凸関数の極小値は最小値
* 狭義凸関数は最小値を取る点が存在するならば、1点である


## Reference
* [凸関数 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%87%B8%E9%96%A2%E6%95%B0)
* [Convex function - Wikipedia](https://en.wikipedia.org/wiki/Convex_function)

