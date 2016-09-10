# Implicit Function Theorem

## Symbol
* $f: \mathbb{R}^{N + M} \rightarrow \mathbb{R}^{M}$
* $x = (x^{1}, \ldots, x^{N})^{T} \in \mathbb{R}^{N}$
* $y = (y^{1}, \ldots, y^{M})^{T} \in \mathbb{R}^{M}$
* $g: \mathbb{R}^{N} \rightarrow \mathbb{R}^{M}$

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


## Theorem1

## Theorem2

## Theorem3

## Reference
* [陰函数定理 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%99%B0%E5%87%BD%E6%95%B0%E5%AE%9A%E7%90%86)
