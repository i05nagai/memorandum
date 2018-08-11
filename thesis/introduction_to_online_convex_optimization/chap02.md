---
title: Introduction to Online Convex Optimization Chapter02
---

## 2.1 Basic definitons and setups

* $\mathcal{K} \subseteq \mathbb{R}^{d}$,
    * bounded convex, compact
* $f: \mathcal{K} \rightarrow \mathbb{R}$,

#### Definition positive definite
* $A$,
    * $n \times n$-matrix
* $B$,
    * $n \times n$-matrix

We write $A \preccurlyeq B$ if $B-A$ is positive semidefinite.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition alpha strongly convex and beta smooth
* $f$,
    * convex
* $\alpha > 0$,
* $\beta > 0$,

$f$ is said to be $\alpha$-strongly convex if

$$
    f(x)
    +
    \nabla f(x)^{\mathrm{T}}
    (y - x)
    +
    \frac{\alpha}{2}
    \|
        y - x
    \|^{2}
    \le
    f(y)
    .
$$

$f$ is said to be $\beta$-smooth if

$$
    f(x)
    +
    \nabla f(x)^{\mathrm{T}}
    (y - x)
    +
    \frac{\beta}{2}
    \|
        y - x
    \|^{2}
    \ge
    f(y)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Proposition
* $f$,
* $\beta > 0$,

Then the following conditions are equivalent;

(1) $f$ is $\beta$-smooth

(2) 

$$
    \|
        \nabla f(x)
        -
        \nabla f(y)
    \|
    \le
    \beta
    \|
        x - y
    \|
    .
$$

(3)

$$
    \alpha I
    \preccurlyeq
    \nabla^{2} f(x)
    \preccurlyeq
    \beta I
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition gamma-well-conditioned
* $f$,

$f$ is said to be $\gamma$-well-condtiond if

* (1) $f$ is $\alpha$-strongly convex
* (2) $f$ is $\beta$-smooth convex

where

$$
    \gamma
    :=
    \frac{
        \alpha
    }{
        \beta
    }
    \le
    1
    .
$$

$\gamma$ is called the condition number of $f$.

<div class="end-of-statement" style="text-align: right">■</div>



### 2.1.1 Projections onto convex sets

#### Definition. projection onto convex sets
* $\mathcal{K} \subseteq \mathbb{R}^{d}$,
    * convex sets
* $y \in \mathbb{R}^{d}$,


Projection onto convex sets are defined

$$
    \Pi_\mathcal{\mathcal{K}}(y)
    :=
    \arg\min_{x \in \mathcal{K}}
        \|
            x - y
        \|
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 2.1
* $\mathcal{K} \subseteq \mathbb{R}^{d}$,
    * convex set
* $y \in \mathbb{R}^{d}$,
* $x := \Pi_{\mathcal{K}}(y)$,

$$
    \forall z \in \mathcal{K},
    \
    \|
        y - z
    \|
    \ge
    \|
        x - z
    \|
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### 2.1.1 Introduction to optimality conditions

#### Theorem 2.2 KKT
* $\mathcal{K} \subseteq \mathbb{R}^{d}$,
    * convex set 
* $x^{*} \in \arg\min_{x \in \mathcal{K}}f(x)$,

Then

$$
    \nabla f(x^{*})^{\mathrm{T}}
    (y - x^{*}))
    \ge
    0
    .
$$

#### proof.


<div class="QED" style="text-align: right">$\Box$</div>

#### ALgorithm 2 Gradient Decent Method
* $f:\mathcal{K} \rightarrow \mathbb{R}$,
    * convex function
* $\mathcal{K}$,
    * convex set
* $x_{1} \in \mathcal{K}$,
    * initial points
* $T \in \mathbb{N}$,
* $$\{\eta_{t}\}$$,
    * sequence of step sizes


Step1. For $t = 1, \ldots, T$


Step2.

$$
\begin{eqnarray}
    y_{t + 1}
    & := &
        x_{t}
        -
        \eta_{t}
        \nabla f(x_{t}),
    \nonumber
    \\
    x_{t + 1}
    & := &
        \Pi_{\mathcal{K}}(y_{t + 1})
    \nonumber
\end{eqnarray}
$$


Step3. Go to Step2 until $t = T$

Step4. $x_{T + 1}$,

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma

$$
    x
    -
    \frac{1}{b}
    a
    =
    \arg\min_{z}
        \sum_{i=1}^{d}
            a_{i}(z_{i} - x_{i})
        +
        \frac{b}{2}
        \|
            z - y
        \|^{2}
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>


#### Theroem 2.3
* $\Gamma > 0$,
* $f$,
    * $\gamma$-well-conditioned function
* $$h_{t} := f(x_{t}) - f(x^{*})$$,
* $\eta_{t} :- \frac{1}{\beta} > 0$,

Then

$$
    h_{t+1}
    \le
    h_{1}
    e^{-\gamma t}
    .
$$

### proof
By strong convexity, for all $x, y \in \mathcal{K}$,

$$
\begin{eqnarray}
    f(y)
    & \ge &
        f(x)
        +
        \nabla f(x)^{\mathrm{T}}
        (y - x)
        +
        \frac{\alpha}{2}
        \|
            x - y
        \|^{2}
        \quad
        (\because \alpha\text{-strong convexity})
    \nonumber
    \\
    & \ge &
        \min_{z \in \mathcal{K}}
        \left\{
            f(x)
            +
            \nabla f(x)^{\mathrm{T}}
            (z - x)
            +
            \frac{\alpha}{2}
            \|
                x - z
            \|^{2}
        \right\}
    \nonumber
    \\
    & = &
        f(x)
        -
        \frac{1}{2 \alpha}
        \|
            \nabla f(x)
        \|^{2}
\end{eqnarray}

$$

<div class="QED" style="text-align: right">$\Box$</div>
