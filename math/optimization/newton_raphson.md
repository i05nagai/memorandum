---
title: Newton-Raphson Method
---


## Newton-Raphson method
Newton method.

## Good

## Bad
* 微分の行列が必要

## Definition
* $N \in \mathbb{N}$
* $f:\mathbb{R}^{N} \rightarrow \mathbb{R}^{N}$

## Problem
$f(x) = 0$を満たす$x \in \mathbb{R}^{N}$を見つける。

## Algorithms
$f$の$\bar{x} \in \mathbb{R}^{N}$でのテーラー展開を考える。

$$
f(x) = f(\bar{x}) + \frac{\partial f}{\partial x}(\bar{x})(x - \bar{x}) + o(x)
$$

$o(x)$の項を無視し、$f(x)=0$とすると、

$$
x = - \left( \frac{\partial f}{\partial x}(\bar{x}) \right)^{-1} f(\bar{x}) + \bar{x}
$$

つまり、上式の$x$は点$\bar{x}$で$f$を線形に近似した時に0になる$x$ である。

これを繰り返すことで収束する$f(x)=0$を満たす$x$を見つけるのがNewton-Raphson法である。
アルゴリズムをまとめると

1. パラメータ$(\lambda^{k})$を適当な方法で決める
2. 初期値として$x^{0}$を適当に決める
3. $k=0$とする
4. 以下の式で計算

    $$
        x^{k+1}
        :=
        - 
        \lambda^{k}
        \left(
           \frac{\partial f}{\partial x}(x^{k})
        \right)^{-1}
        f(x^{k})
        +
        x^{k}
    $$

5. $x^{k+1}$が収束していなければ、$k \leftarrow k + 1$としてstep 4に戻る
6. 収束していれば、$x^{k+1}$を出力して終了

