---
layout: math
title: Newton-Raphson Method
---


# Newton-Raphson method

## definition
* $N \in mathbb{N}$
* $f:\mathbb{R}^{N} \rightarrow \mathbb{R}^{N}$

## problem
$f(x) = 0$を満たす$x^{*}$を見つける。

## algorithms
$f$の$\bar{x}$テーラー展開を考える。

$$
f(x) = f(\bar{x}) + \frac{\partial f}{\partial x}(\bar{x})(x - \bar{x}) + o(x)
$$

$o(x)$の項を無視し、$f(x)=0$とすると、

$$
x = - \left( \frac{\partial f}{\partial x}(\bar{x}) \right)^{-1} f(\bar{x}) + \bar{x}
$$

つまり、上式の$x$は点$\bar{x}$で$f$を線形に近似した時に0になる$x$ である。

これを繰り返すことで収束する$f(x)=0$を満たす$x$を見つけるのがNewton-Raphson

