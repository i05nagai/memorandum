---
title: Quadratic Programming
---

## Quadratic Programming

#### Definition 1 Quradatic Programming
* $c \in \mathbb{R}^{n}$,
* $x \in \mathbb{R}^{n}$,
* $a_{i} \in \mathbb{R}^{n}$,
* $G$,
    * $n \times n$ symmetric matrix
* $\mathcal{I}_{1}$,
    * finite indice
* $\mathcal{I}_{2}$,
    * finite indice

$$
\begin{align}
    \min_{x}
    & & &
        q(x)
        :=
        \frac{1}{2}
        x^{\mathrm{T}}Gx
        +
        x^{\mathrm{T}}c
        \
        \label{quadratic_programming_definition}
    \\
    \mathrm{subject\ to}
    & & &
        a_{i}^{\mathrm{T}}x
        =
        b_{i}
        \quad
        i \in \mathcal{I}_{1}
    \\
    & & &
        a_{i}^{\mathrm{T}}x
        \ge
        b_{i}
        \quad
        i \in \mathcal{I}_{2}
\end{align}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
$G$ is a hessian matrix of $q(x)$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition 2

If $G$ is positive semidefinite, we say $$\eqref{quadratic_programming_definition}$$ is a convex QP.

If $G$ is positive definite, we say $$\eqref{quadratic_programming_definition}$$ is a strictly convex QP.

If $G$ is an indefinite matrix, we say $$\eqref{quadratic_programming_definition}$$ is a nonconvex QP.

<div class="end-of-statement" style="text-align: right">■</div>


## Algorithm
* [Optimization \(scipy\.optimize\) — SciPy v1\.2\.0 Reference Guide](https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html#sequential-least-squares-programming-slsqp-algorithm-method-slsqp)

## Reference
* [Quadratic programming \- Wikipedia](https://en.wikipedia.org/wiki/Quadratic_programming)
* Delbos, F., & Gilbert, J. (2003). Global linear convergence of an augmented Lagrangian algorithm for solving convex quadratic optimization problems, 12(1), 45–69. Retrieved from http://hal.archives-ouvertes.fr/inria-00071556/
* Kraft, D. (n.d.). A Software Package for Sequential Quadratic Programming.
