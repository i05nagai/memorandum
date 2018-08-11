---
title: Differentiation
---

## Differentiation
* $$\|
\|$$,
    * euclid norm
* $L(\mathbb{R}^{n}, \mathbb{R}^{m})$,
    * a set of $n\times m$-matrix
* $E \subseteq \mathbb{R}^{n}$,
    * open subset
* $f: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$,
* $x_{0} \in \mathbb{R}^{n}$,

$f$ is said to be differentialble at $x_{0}$ if

$$
\begin{eqnarray}
    \exists A \in L(\mathbb{R}^{n}, \mathbb{R}^{m})
    \text{ s.t. }
    \lim_{h \rightarrow 0}
    \frac{
        \|
            f(x_{0} + h)
            -
            f(x_{0})
            -
            Ah
        \|
    }{
        \|
        h
        \|
    }
    =
    0
    \label{differentiation_definition}
\end{eqnarray}
    .
$$

We write

$$
    f^{\prime}(x_{0})
    =
    A
    .
$$

$f$ is said to be differentiable in $E$ if $f$ is differentialble at every $x \in E$.

#### Theorem 1. uniquness
* $A_{1} \in L(\mathbb{R}^{n}, \mathbb{R}^{m})$,
    * satisfy $\eqref{differentiation_definition}$
* $A_{2} \in L(\mathbb{R}^{n}, \mathbb{R}^{m})$,
    * satisfy $\eqref{differentiation_definition}$

Then $A_{1} = A_{2}$.

#### proof
Let $B := A_{1} - A_{2}$.

$$
\begin{eqnarray}
    \|
        Bh
    \|
    & = &
        \|
            -
            (
            f(x + h)
            +
            f(x)
            -
            A_{1}h
            )
            +
            f(x + h)
            +
            f(x)
            -
            A_{2}h
        \|
    \nonumber
    \\
    & \le &
    \|
        f(x + h)
        -
        f(h)
        -
        A_{1}h
    \|
    +
    \|
        f(x + h)
        -
        f(h)
        -
        A_{2}h
    \|
    \nonumber
\end{eqnarray}
$$

Thus, for $h\neq0$,

$$
    \frac{
        \|
            Bh
        \|
    }{
        \|
        h
        \|
    }
    \rightarrow
    0
    \quad
    (h \rightarrow 0)
    .
$$

On the other hand, let $h \neq 0$ be fixed.

$$
    \frac{
        \|
            Bh
        \|
    }{
        \|
            h
        \|
    }
    =
    \frac{
        \|
            B(th)
        \|
    }{
        \|
            th
        \|
    }
    \quad
    (t \rightarrow 0)
    .
$$

Left hand side of the equation does not depend on $t$.
Hence 

$$
    h \in \mathbb{R}^{n},
    \
    Bh
    =
    0
    .
$$

This implies $B = 0$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Remarks
$$\eqref{differentiation_definition}$$ is equivalent to the condition

$$
    f(x + h)
    -
    f(x)
    =
    f^{\prime}(x)h
    +
    r(h)
    .
$$

where the remainder $r(h)$ satisfies

$$
    \lim_{h \rightarrow 0}
        \frac{
            \|
                r(h)
            \|
        }{
            \|
                h
            \|
        }
    =
    0
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 2
* $E \subset \mathbb{R}^{n}$,
    * open subset
* $x_{0} \in E$,
* $E^{\prime} \subseteq f(E)$,
    * open subset

$$
    F(x)
    :=
    g(f(x))
$$

is differentiable at $x_{0}$, and

$$
    F^{\prime}(x_{0})
    :=
    g^{\prime}(f(x_{0}))
    f^{\prime}(x_{0})
    .
$$

#### proof
Let $y_{0} := f(x_{0})$, $A := f^{\prime}(x_{0})$, $B := g^{\prime}(y_{0})$.

$$
\begin{eqnarray}
    u(h)
    & := &
        f(x_{0} + h)
        -
        f(x_{0})
        -
        Ah
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Partial derivatives
* $E \subseteq \mathbb{R}^{n}$,
    * open subset
* $$\{e_{1}, \ldots, e_{n}\}$$,
    * standard base of $\mathbb{R}^{n}$
* $$\{u_{1}, \ldots, u_{n}\}$$,
    * standard base of $\mathbb{R}^{m}$
* $f:E \rightarrow \mathbb{R}^{m}$,

The components of $f$ are the real functions $f_{1}, \ldots, f_{m}$ defined by

$$
    f_{i}(x)
    :=
    \langle
        f(x),
        u_{i}
    \rangle
    \quad
    (x \in E)
    .
$$

or, equivalently

$$
    f(x)
    =
    \sum_{i=1}^{m}
        f_{i}(x)
        u_{i}
    .
$$

#### Definition

$$
    (D_{j}f_{i})(x)
    =
    \lim_{t \rightarrow 0}
        \frac{
            f_{i}(x + te_{j})
            -
            f_{i}(x)
        }{
            t
        }
        ,
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem
* $E \subseteq \mathbb{R}^{n}$,
    * open subset
* $x \in E$,
* $f: E \rightarrow \mathbb{R}^{m}$,
    * differentialble at a $x$,

$$
    \forall j \in \{1, \ldots, n\},
    \
    f^{\prime}(x)
    e_{j}
    =
    \sum_{i=1}^{m}
        (D_{j}f_{i})(x)
        u_{i}
    .
$$

#### proof
Let $j$ be fixed.
Since $f$ is differentiable at $x$,

$$
\begin{eqnarray}
    f(x + te_{j})
    -
    f(x)
    & = &
        f^{\prime}(x)
        (te_{j})
        +
        r(te_{j})
    \nonumber
    \\
    \frac{
        \|
            r(te_{j})
        \|
    }{
        t
    }
    & \rightarrow &
        0
        \quad
        (t \rightarrow 0)
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        \frac{
            f(x + te_{j})
            -
            f(x)
        }{
            t
        }
        =
        f^{\prime}(x)
        (e_{j})
        +
        \frac{
            r(te_{j})
        }{
            t
        }
    \nonumber
    \\
    & \Rightarrow &
        \lim_{t \rightarrow 0}
            \frac{
                f(x + te_{j})
                -
                f(x)
            }{
                t
            }
            =
            f^{\prime}(x)
            e_{j}
    \nonumber
    \\
    & \Rightarrow &
        \lim_{t \rightarrow 0}
            \sum_{i=1}^{m}
                \frac{
                    f_{i}(x + te_{j})
                    -
                    f_{i}(x)
                }{
                    t
                }
                u_{i}
            =
            f^{\prime}(x)
            e_{j}
    \nonumber
    \\
    & \Rightarrow &
            \sum_{i=1}^{m}
                (D_{j}f_{i})(x)
                u_{i}
            =
            f^{\prime}(x)
            e_{j}
        .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

$$
    f^{\prime}(x)
    =
    \left(
        \begin{array}{ccc}
            (D_{1}f_{1})(x)
            &
                \cdots
            &
                (D_{n}f_{1})(x)
            \\
            \vdots
            &
                \ddots
            &
                \vdots
            \\
            (D_{1}f_{m})(x)
            &
                \cdots
            &
                (D_{n}f_{m})(x)
        \end{array}
    \right)
$$

#### Definition.
* $f: E \rightarrow \mathbb{R}^{m}$,

The gradient of $f$ at $x$ defiend by

$$
    (\nabla f)(x)
    :=
    \sum_{i=1}^{n}
        (D_{i}f)(x)
        e_{i}
$$

<div class="end-of-statement" style="text-align: right">■</div>

* $(a, b) \subseteq \mathbb{R}$,
* $E \subseteq \mathbb{R}^{n}$,
* $\gamma: (a, b) \rightarrow E$,
    * differentialble in $E$
* $f: E \rightarrow \mathbb{R}$,
    * differentialbe
* $g(t) := f(\gamma(t))$.
    * $g: (a, b) \rightarrow \mathbb{R}$,

$$
\begin{eqnarray}
    g^{\prime}(t)
    & = &
        f^{\prime}(\gamma(t))
        \gamma^{t}(t)
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            (D_{i}f)(\gamma(t))
        \gamma^{t}(t)
    \nonumber
    \\
    & = &
        \langle
            (\nabla f)(\gamma(t)),
            \gamma^{t}(t)
        \rangle
    .
\end{eqnarray}
$$

## Reference
Walter Rudin. Principle of Mathematical analysis
