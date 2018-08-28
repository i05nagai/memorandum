---
title: Line Search Methods and the Armijo Rule
---

## Line Search Methods and the Armijo Rule

#### Definition descent direction
* $f: \mathbb{R}^{N} \rightarrow \mathbb{R}$,
* $d \in \mathbb{R}^{N}$,

$$
    \nabla f
    :=
    (\frac{\partial f}{\partial x^{1}}, \cdots, \frac{\partial f}{\partial x^{N}})
$$

$d$ is said to be descent direction of $f$ at $x$ if

$$
    \left.
        \frac{d f(x + td)}{d t}
    \right|_{t=0}
    =
    (\nabla f(x))^{\mathrm{T}} d
    < 0
    .
$$

In Gradient Descent algorithm, $d = - (\nabla f)(x)$.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Iterative Methods for Optimization](http://www.ec-securehost.com/SIAM/FR18.html)
* http://web.mit.edu/6.252/www/LectureNotes/6_252%20Lecture04.pdf
