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

The Armijo rule/condition is a condition to find a step length $\alpha \in \mathbb{R}$, as measured by the following inequality;

$$
\begin{equation}
    \phi(\alpha)
    :=
    f(x_{k} + \alpha d)
    \le
    c_{1} \alpha
    \nabla f(x_{k})^{\mathrm{T}}d
    +
    f(x_{k})
    =:
    l(\alpha)
    \label{armijo_condition}
\end{equation}
$$

where $c_{1} \in (0, 1)$ is a constant and $d \in \mathbb{R}^{N}$ is a decent direction.

The curvature condtion is a condition

$$
\begin{eqnarray}
    \phi^{\prime}(\alpha)
    =
    \nabla f(x_{k} + \alpha d)^{\mathrm{T}}
    d
    \ge
    c_{2}
    \nabla f(x_{k})^{\mathrm{T}}d
    =
    \phi^{\prime}(0)
    \label{curvature_condition}
\end{eqnarray}
$$

where $c_{2} \in (c_{1}, 1)$ and $c_{1}$ and $d$ are defined in $$\eqref{armijo_condition}$$.

The combined conditions are know as the Wolfe condtion, that is,

$$
\begin{eqnarray}
    f(x_{k} + \alpha d)
    & \le &
        c_{1} \alpha
        \nabla f(x_{k})^{\mathrm{T}}d
        +
        f(x_{k})
    \nonumber
    \\
    \nabla f(x_{k} + \alpha d)^{\mathrm{T}}
    d
    & \ge &
        c_{2}
        \nabla f(x_{k})^{\mathrm{T}}d
    \nonumber
\end{eqnarray}
$$

The strong Wolfe condition is defined as

$$
\begin{eqnarray}
    f(x_{k} + \alpha d)
    & \le &
        c_{1} \alpha
        \nabla f(x_{k})^{\mathrm{T}}d
        +
        f(x_{k})
    \nonumber
    \\
    \abs{
        \nabla f(x_{k} + \alpha d)^{\mathrm{T}}
        d
    }
    & \le &
        c_{2}
        \abs{
            \nabla f(x_{k})^{\mathrm{T}}d
        }
    \nonumber
\end{eqnarray}
$$

## Reference
* [Iterative Methods for Optimization](http://www.ec-securehost.com/SIAM/FR18.html)
* http://web.mit.edu/6.252/www/LectureNotes/6_252%20Lecture04.pdf
