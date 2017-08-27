---
title: Line Search Methods and the Armijo Rule
---

## Line Search Methods and the Armijo Rule

## Definition
$$
    \nabla f
    :=
    (\frac{\partial f}{\partial x^{1}}, \cdots, \frac{\partial f}{\partial x^{N}})
$$

$d \in \mathbb{R}^{N}$が$f$の$x$でのdescent directionとは、

$$
    \left.
        \frac{d f(x + td)}{d t}
    \right|_{t=0}
    =
    (\nabla f(x))^{\mathrm{T}} d
    < 0
$$

を満たすことを言う。
Gradient Descent algorithmでは、$d = - (\nabla f)(x)$である。

##
* [Iterative Methods for Optimization](http://www.ec-securehost.com/SIAM/FR18.html)
