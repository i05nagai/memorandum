---
title: Introduction to Online Convex Optimization Chapter02
---

## 2.1 Basic definitons and setups

* $D > 0$,
    * we use this symbol for the upper bound of the 
* $G > 0$,
    * we use this symbol for the constant of Lipschitz function
* $\mathcal{K} \subseteq \mathbb{R}^{d}$,
    * diameter is bounded by $D$
    * convex
    * compact

#### Definition
* $f: \mathcal{K} \rightarrow \mathbb{R}$,
    * convex
* $G > 0$,

$f$ is said to be $G$-bounded if

$$
    \norm{
        \partial_{x}f
    }
    \le
    G
$$

where $\partial_{x}f$ is subgradient of $f$ at $x$.


<div class="end-of-statement" style="text-align: right">■</div>

#### Definition positive definite
* $A$,
    * $n \times n$-matrix
* $B$,
    * $n \times n$-matrix

We write $A \preccurlyeq B$ if $B-A$ is positive semidefinite.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition property of positive definite
* $A$,
    * $n \times n$-matrix
* $B$,
    * $n \times n$-matrix
* $\alpha > 0$,

(1) If $\alpha A \preccurlyeq  B$ and $A$ is nonnegative definite, then for all $\beta < \alpha$,

$$
    \beta A \preccurlyeq  B
    .
$$

#### proof
(1)

Since $A$ is positive semidefinite,  $x^{\mathrm{T}}Ax \ge 0$.
Then

$$
\begin{eqnarray}
    x \mathbb{R}^{n},
    \
    x^{\mathrm{T}}(B - \beta A)x
    & = &
        x^{\mathrm{T}}Bx
        -
        \beta x^{\mathrm{T}} Ax
    \nonumber
    \\
    & \ge &
        x^{\mathrm{T}}Bx
        -
        \alpha x^{\mathrm{T}} Ax
    \nonumber
    \\
    & > &
        0
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Definition alpha strongly convex and beta smooth
* $f$,
    * convex
* $\alpha > 0$,
* $\beta > 0$,

$f$ is said to be $\alpha$-strongly convex if

$$
\begin{eqnarray}
    & &
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
    \nonumber
    \\
    & \Leftrightarrow &
        \nabla f(x)^{\mathrm{T}}
        (y - x)
        +
        \frac{\alpha}{2}
        \|
            y - x
        \|^{2}
        \le
        f(y)
        -
        f(x)
        \label{definition_alpha_strongly}
\end{eqnarray}
    .
$$

$f$ is said to be $\beta$-smooth if

$$
\begin{eqnarray}
    & &
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
    \nonumber
    \\
    & \Leftrightarrow &
        \nabla f(x)^{\mathrm{T}}
        (y - x)
        +
        \frac{\beta}{2}
        \|
            y - x
        \|^{2}
        \ge
        f(y)
        -
        f(x)
        \label{definition_beta_smooth}
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Proposition
* $f$,
    * convex
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

#### proof
(1) $\Rightarrow$ (2)

Let $x \in \mathbb{R}^{n}$ and $h > 0$ be fixed.
Let $y := x + h(1, \ldots, 1)^{\mathrm{T}}$.


<div class="QED" style="text-align: right">$\Box$</div>

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
In this section, we assume

$$
    x^{*}
    \in
    \arg\min_{x \in \mathcal{K}}f(x)
$$

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

## 2.2 Gradient / subgradient descent
In this section, we prove the convergence rate of Gradient descent and Accelerated GD for each cases,  $f$ is gamma-well-conditioned, $f$ is beta-smooth, and $f$ is alpha strongly convex.

Gradient descent

* general convex
    * $O(1/\sqrt{T})$,
* $\alpha$-strongly convex
    * $O(\frac{1}{\alpha T})$,
* $\beta$-smooth convex
    * $O(\frac{\beta}{T})$,
* $\gamma$-well-conditioned
    * $O(e^{-\gamma T})$,

Accelerated GD

* $\beta$-smooth convex
    * $O(\frac{\beta}{T^{2}})$,
* $\gamma$-well-conditioned
    * $O(e^{-\sqrt{\gamma} T})$,

### 2.2.1 Basic Gradient descent

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
* $b > 0$,

$$
\begin{eqnarray}
    x
    -
    \frac{1}{b}
    a
    & = &
    \arg\min_{z}
        f(z)
    \nonumber
    \\
    f(z)
    & := &
        \sum_{i=1}^{d}
            a_{i}(z_{i} - x_{i})
        +
        \frac{b}{2}
        \|
            z - x
        \|^{2}
    \nonumber
\end{eqnarray}
$$

#### proof

$$
\begin{eqnarray}
    & &
        \frac{\partial f}{\partial z_{i}}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        a_{i}
        +
        b
        (z_{i} - x_{i})
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        z_{i}
        =
        \frac{
            -a_{i}
        }{
            b
        }
        +
        x_{i}
\end{eqnarray}
$$

Then,

$$
\begin{eqnarray}
    f
    \left(
        x
        -
        \frac{1}{b}
        a
    \right)
    & = &
        -
        \sum_{i=}^{d}
            \frac{
                a_{i}^{2}
            }{
                b
            }
        +
        \frac{1}{2b}
        \|
            a
        \|^{2}
    \nonumber
    \\
    & = &
        -
        \frac{1}{2b}
        \|
            a
        \|^{2}
\end{eqnarray}
$$

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
        \quad
        (\because z := x - \frac{1}{\alpha}\nabla f(x))
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    & &
        f(x^{*})
        \ge
        f(x_{t})
        -
        \frac{1}{2 \alpha}
        \|\nabla f(x_{t}) \|^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \|\nabla f(x_{t}) \|^{2}
        \ge
        2 \alpha
        (
            f(x_{t})
            -
            f(x^{*})
        )
        =
        2 \alpha
        h_{t}
        \label{eq02_01}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    h_{t + 1}
    -
    h_{t}
    & = &
        f(x_{t+1} - x_{t})
        -
        f(x_{t})
    \nonumber
    \\
    & \le &
        (\nabla f(x_{t}))^{\mathrm{T}}
        (x_{t + 1} - x_{t})
        +
        \frac{\beta}{2}
        \|
            x_{t+1} - x_{t}
        \|
    \nonumber
    \\
    & = &
        - \eta_{t}
        \|
            \nabla f(x_{t})
        \|^{2}
        +
        \frac{\beta}{2}
        \eta_{t}^{2}
        \|
            \nabla f(x_{t})
        \|^{2}
    \nonumber
    \\
    & = &
        -
        \frac{1}{2\beta}
        \|
            \nabla f(x_{t})
        \|^{2}
    \nonumber
    \\
    & \le &
        -\frac{\alpha}{\beta}
        h_{t}
        \quad
        (\because \eqref{eq02_01})
    \nonumber
    \\
    & = &
        -\gamma
        h_{t}
    .
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    h_{t + 1}
    \le
    h_{t}
    \left(
        1 - \gamma
    \right)
    \le
    \cdots
    h_{1}
    \left(
        1 - \gamma
    \right)^{t}
    \le
    h_{1}
    e^{-\gamma t}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 2.4
* $\Gamma > 0$,
* $f$,
    * $\gamma$-well-conditioned function
* $$h_{t} := f(x_{t}) - f(x^{*})$$,
* $\eta_{t} :- \frac{1}{\beta} > 0$,
* $\mathcal{K}$,
    * convex set

Then

$$
    h_{t+1}
    \le
    h_{1}
    \exp
    \left(
        -
        \frac{
            \gamma t
        }{
            4
        }
    \right)
    .
$$

#### proof
From $\beta$ smoothness, for every $x, x_{t} \in \mathcal{K}$,

$$
\begin{equation}
    \nabla f(x_{t})
    (x - x_{t})
    \le
    f(x)
    -
    f(x_{t})
    -
    \frac{\alpha}{2}
    \|
        x - x_{t}
    \|^{2}
    \label{eq02_02}
\end{equation}
    .
$$

By algorithm's definition, we have

$$
\begin{equation}
    x_{t + 1}
    =
    \arg \min_{x \in \mathcal{K}}
    \left\{
        \nabla f(x_{t})^{\mathrm{T}}
        (x - x_{t})
        +
        \frac{\beta}{2}
        \|
            x - x_{t}
        \|^{2}
    \right\}
    \label{eq02_03}
\end{equation}
    .
$$

To see this, letting $\nabla_{t} := \nabla f(x_{t})$,

$$
\begin{eqnarray}
    \arg\min_{x \in \mathcal{K}}
        \left\{
            \|
                x
                -
                (x_{t} - \eta_{t} \nabla_{t})
            \|^{2}
        \right\}
    & = &
        \arg\min_{x \in \mathcal{K}}
        \left\{
            \sum_{i=1}^{d}
             \left(
                    x_{i}
                    -
                    (x_{t,i} - \eta_{t} \nabla_{t, i})
             \right)^{2}
        \right\}
    \nonumber
    \\
    & = &
        \arg\min_{x \in \mathcal{K}}
        \left\{
            \sum_{i=1}^{d}
             \left(
                    x_{i}^{2}
                    -
                    2
                    x_{i}
                    (x_{t,i} - \eta_{t} \nabla_{t, i})
                    +
                    x_{t,i}^{2}
                    -
                    2x_{t, i}\eta_{t} \nabla_{t, i}
                    +
                    \eta_{t}^{2} \nabla_{t, i}^{2}
             \right)
        \right\}
    \nonumber
    \\
    & = &
        \arg\min_{x \in \mathcal{K}}
        \left\{
            \sum_{i=1}^{d}
             \left(
                    x_{i}^{2}
                    -
                    2
                    x_{i}
                    x_{t,i}
                    +
                    x_{t,i}^{2}
                    -
                    2
                    x_{i}
                    \eta_{t} \nabla_{t, i}
                    -
                    2x_{t, i}\eta_{t} \nabla_{t, i}
                    +
                    \eta_{t}^{2} \nabla_{t, i}^{2}
             \right)
        \right\}
    \nonumber
    \\
    & = &
        \arg\min_{x \in \mathcal{K}}
        \left\{
            \sum_{i=1}^{d}
             \left(
                    (x_{i} - x_{t, i})^{2}
                    +
                    2
                    x_{i}
                    \eta_{t} \nabla_{t, i}
                    -
                    2x_{t, i}\eta_{t} \nabla_{t, i}
             \right)
        \right\}
    \nonumber
    \\
    & = &
        \arg\min_{x \in \mathcal{K}}
        \left\{
            \sum_{i=1}^{d}
            2 \eta_{t}
             \left(
                \frac{1}{2 \eta_{t}}
                (x_{i} - x_{t, i})^{2}
                +
                \nabla_{t, i}
                \left(
                    x_{i}
                    -
                    x_{t, i}
                \right)
             \right)
        \right\}
    \nonumber
    \\
    & = &
        \arg\min_{x \in \mathcal{K}}
        \left\{
            \frac{1}{2 \eta_{t}}
            \|
                x - x_{t, i}
            \|^{2}
            +
            \nabla_{t}^{\mathrm{T}}
            \left(
                x
                -
                x_{t}
            \right)
        \right\}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    x_{t + 1}
    & = &
        \Pi_{\mathcal{K}}
            (x_{t} - \eta_{t} \nabla f(x_{t}))
    \nonumber
    \\
    & = &
        \arg\min_{x \in \mathcal{K}}
            \left\{
                \|
                    x
                    -
                    (x_{t} - \eta_{t} \nabla f(x_{t}))
                \|
            \right\}
    \nonumber
    \\
    & = &
        \arg\min_{x \in \mathcal{K}}
            \left\{
                \nabla f(x_{t})^{\mathrm{T}}
                (x - x_{t})
                +
                \frac{1}{2 \eta_{t}}
                \|
                    x
                    -
                    x_{t}
                \|^{2}
            \right\}
\end{eqnarray}
$$

Thus, $\forall \eta \in [0, 1]$,

$$
\begin{eqnarray}
    h_{t + 1}
    -
    h_{t}
    & = &
        f(x_{t + 1})
        -
        f(x_{t})
    \nonumber
    \\
    & \le &
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t + 1} - x_{t})
        +
        \frac{\beta}{2}
        \|
            x_{t + 1}
            -
            x_{t}
        \|^{2}
        \quad
        (\because \text{smoothness})
    \nonumber
    \\
    & = &
        \min_{x \in \mathcal{K}}
            \left\{
                \nabla f(x_{t})
                (x - x_{t})
                +
                \frac{\beta}{2}
                \|
                    x - x_{t}
                \|^{2}
            \right\}
        \quad
        (\because \eqref{eq02_03})
    \nonumber
    \\
    & \le &
        \min_{x \in \mathcal{K}}
            \left\{
                f(x)
                -
                f(x_{t})
                +
                \frac{\beta - \alpha}{2}
                \|
                    x - x_{t}
                \|^{2}
            \right\}
        \quad
        (\because \eqref{eq02_02})
    \nonumber
    \\
    & \le &
        \min_{x \in [x_{t}, x^{*}]}
            \left\{
                f(x)
                -
                f(x_{t})
                +
                \frac{\beta - \alpha}{2}
                \|
                    x - x_{t}
                \|^{2}
            \right\}
    \nonumber
    \\
    & = &
        f
        \left(
            (1 - \eta)
            x_{t}
            +
            \eta x^{*}
        \right)
        -
        f(x_{t})
        +
        \frac{\beta - \alpha}{2}
        \|
            (1 - \eta)
            x_{t}
            +
            \eta x^{*}
            -
            x_{t}
        \|^{2}
    \nonumber
    \\
    & \le &
        (1 - \eta)
        f(x_{t})
        +
        \eta 
        f(x^{*})
        -
        f(x_{t})
        +
        \frac{(\beta - \alpha)\eta^{2}}{2}
        \|
            -
            x_{t}
            +
            x^{*}
        \|^{2}
        \quad
        (\because \text{convexity})
    \nonumber
    \\
    & = &
        -\eta
        f(x_{t})
        +
        \eta 
        f(x^{*})
        +
        \frac{(\beta - \alpha)\eta^{2}}{2}
        \|
            -
            x_{t}
            +
            x^{*}
        \|^{2}
    \nonumber
    \\
    & \le &
        -
        \eta
        h_{t}
        +
        \frac{(\beta - \alpha)\eta^{2}}{2}
        \|
            -
            x_{t}
            +
            x^{*}
        \|^{2}
\end{eqnarray}
$$

where

$$
    [x_{t}, x^{*}]
    :=
    \{
        (1 - \eta)x_{t}
        +
        \eta x^{*}
        \mid
        \eta \in [0, 1]
    \}
    .
$$

For the second term,

$$
\begin{eqnarray}
    \frac{\alpha}{2}
    \|
        x^{*} - x_{t}
    \|^{2}
    & \le &
        \frac{\alpha}{2}
        \|
            x^{*} - x_{t}
        \|^{2}
        +
        \nabla f(x^{*})^{\mathrm{T}}
        (x_{t} - x^{*})
        \quad
        (\because \text{ KKT condition})
    \nonumber
    \\
    & \le &
        f(x_{t})
        -
        f(x^{*})
        \quad
        (\because \ \alpha\text{-strongly})
    \nonumber
    \\
    & = &
        h_{t}
    \nonumber
\end{eqnarray}
$$

Combining the above result, $\forall \eta \in [0, 1]$,

$$
\begin{eqnarray}
    h_{t + 1}
    -
    h_{t}
    & \le &
        -
        \eta
        h_{t}
        +
        \frac{(\beta - \alpha)\eta^{2}}{\alpha}
        h_{t}
    \nonumber
    \\
    & \le &
        -
        \eta
        h_{t}
        +
        \frac{\beta\eta^{2}}{\alpha}
        h_{t}
    \nonumber
    \\
    & = &
        \left(
            \frac{\beta}{\alpha}
            \eta^{2}
            -
            \eta
        \right)
        h_{t}
    \nonumber
    \\
    & = &
        \left\{
            \frac{\beta}{\alpha}
            \left(
                \eta
                -
                \frac{\alpha}{2\beta}
            \right)^{2}
            -
            \frac{\alpha}{4\beta}
        \right\}
        h_{t}
\end{eqnarray}
$$

Moreover, since $\gamma$-well-conditioned,

$$
    0
    \le
    \eta
    =
    \frac{
        \alpha
    }{
        2 \beta
    }
    \le
    \frac{1}{2}
    .
$$

Thus, we can achieve the minimizer

$$
\begin{eqnarray}
    h_{t + 1}
    -
    h_{t}
    & \le &
        \min_{\eta \in [0, 1]}
            -
            \eta
            h_{t}
            +
            \frac{\beta\eta^{2}}{\alpha}
            h_{t}
    \nonumber
    \\
    & = &
        -
        \frac{\alpha}{4 \beta}
        h_{t}
    \nonumber
    \\
    & = &
        -
        \frac{\gamma}{4}
        h_{t}
    .
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    h_{t+1}
    \le
    h_{t}
    \left(
        1
        -
        \frac{\gamma}{4}
    \right)
    \le
    h_{t}
    e^{-\gamma/4}
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## 2.3 Reductions to non-smooth and non-strongly convex functions


### 2.3.1 Reductions to smooth and non-strongly convex functions

#### Algorithm 3 gradient descent, reduction to beta-smooth functions
* $f$,
* $T$,
* $x_{1} \in \mathcal{K}$,
* $\tilde{\alpha} > 0$,
    * parameter

Step1. Let

$$
\begin{eqnarray}
    g(x)
    :=
    f(x) + \frac{
        \tilde{\alpha}
    }{
        2
    }
    \|
        x - x_{1}
    \|^{2}
    \label{algorithm03_definition_g}
\end{eqnarray}
    .
$$

Step2. Apply Algorithm2 with parameters $g, T, \eta_{t} := 1/\beta$, $x_{1}$ and get $x_{T}$,

Step3 return $x_{T}$ in Step2.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition propety of norm
* $\alpha > 0$,

$$
    h(x)
    :=
    \frac{\alpha}{2}
    \|
        x - x_{1}
    \|^{2}
    .
$$

* (1) $h$ is convex.
* (2) $h$ is $\alpha$ smooth and $\alpha$ strongly convex.

#### proof
(1)

Hessian matrix of $h$ is diagonal matrix, that is, positve semidefinite.

(2)

$$
\begin{eqnarray}
    \nabla h(x)
    & = &
        \alpha

    \nonumber
    \\
    h(y) - h(x)
    & = &
        \frac{\alpha}{2}
        \left(
            \|
                y - x_{1}
            \|^{2}
            -
            \|
                x - x_{1}
            \|^{2}
        \right)
    \nonumber
    \\
    & = &
        \frac{\alpha}{2}
        \left(
            \|
                y - x_{1}
            \|^{2}
            +
            \|
                y - x
            \|^{2}
            -
            \|
                y - x
            \|^{2}
            +
            2
            \sum_{i=1}^{n}
                (x^{i} - x_{1}^{i})
                (y^{i} - x^{i})
            -
            2
            \sum_{i=1}^{n}
                (x^{i} - x_{1}^{i})
                (y^{i} - x^{i})
            -
            \|
                x - x_{1}
            \|^{2}
        \right)
    \nonumber
    \\
    & = &
        \frac{\alpha}{2}
        \left(
            \|
                y - x_{1}
            \|^{2}
            +
            \|
                y - x
            \|^{2}
            +
            2
            \sum_{i=1}^{n}
                (x^{i} - x_{1}^{i})
                (y^{i} - x^{i})
            -
            \|
                (y - x)
                +
                (x - x_{1})
            \|^{2}
        \right)
    \nonumber
    \\
    & = &
        \alpha
        \sum_{i=1}^{n}
            (x^{i} - x_{1}^{i})
            (y^{i} - x^{i})
        +
        \frac{\alpha}{2}
        \|
            y - x
        \|^{2}
    \nonumber
    \\
    & = &
        \nabla h(x)^{\mathrm{T}}
        (y - x)
        +
        \frac{\alpha}{2}
        \|
            y - x
        \|^{2}
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition alpha-strongnize
* $K \subseteq \mathbb{R}^{n}$,
    * convex
* $f: K \rightarrow \mathbb{R}$,
    * convex function
* $\hat{\alpha} > 0$,

$$
    g(x)
    :=
    f(x)
    +
    \frac{\hat{\alpha}}{2}
    \|
        x
        -
        x_{1}
    \|^{2}
    .
$$

Then $g$ is $\alpha$-strongly convex.

#### proof

$$
\begin{eqnarray}
    \nabla g(x)
    & = &
        \nabla f(x)
        +
        \frac{\hat{\alpha}}{2}
        \nabla
        \|
            x
            -
            x_{1}
        \|^{2}
    \nonumber
    \\
    & \le &
        \nabla f(x)
        +
        \hat{\alpha}
        \left(
        Q
            \begin{array}{c}
                x^{1} - x_{1}^{1}
                \\
                \vdots 
                \\
                x^{n} - x_{1}^{n}
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    g(y) - g(x)
    & = &
        f(y) - f(x)
        +
        \frac{\hat{\alpha}}{2}
        \|
            y - x_{1}
        \|^{2}
        -
        \frac{\hat{\alpha}}{2}
        \|
            x - x_{1}
        \|^{2}
    \nonumber
    \\
    & \ge &
        \nabla f(y)^{\mathrm{T}}
        (y - x)
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                y - x_{1}
            \|^{2}
            -
            \|
                x - x_{1}
            \|^{2}
        \right)
        \quad
        (\because \text{convexity})
    \nonumber
    \\
    & = &
        \nabla f(y)^{\mathrm{T}}
        (y - x)
        +
        \hat{\alpha}
        \sum_{i=1}^{n}
            (x^{i} - x_{1}^{i})
            (y^{i} - x^{i})
        -
        \hat{\alpha}
        \sum_{i=1}^{n}
            (x^{i} - x_{1}^{i})
            (y^{i} - x^{i})
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                y - x_{1}
            \|^{2}
            -
            \|
                x - x_{1}
            \|^{2}
        \right)
    \nonumber
    \\
    & = &
        \nabla g(y)^{\mathrm{T}}
        (y - x)
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                y - x_{1}
            \|^{2}
            +
            \|
                y - x
            \|^{2}
            -
            \|
                y - x
            \|^{2}
            -
            2
            \sum_{i=1}^{n}
                (x^{i} - x_{1}^{i})
                (y^{i} - x^{i})
            -
            \|
                x - x_{1}
            \|^{2}
        \right)
    \nonumber
    \\
    & = &
        \nabla g(y)^{\mathrm{T}}
        (y - x)
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                y - x_{1}
            \|^{2}
            +
            \|
                y - x
            \|^{2}
            -
            \|
                (y - x)
                +
                (x - x_{1})
            \|^{2}
        \right)
    \nonumber
    \\
    & = &
        \nabla g(y)^{\mathrm{T}}
        (y - x)
        +
        \frac{\hat{\alpha}}{2}
        \|
            y - x
        \|^{2}
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition additivity of beta smooth
* $\beta_{1} > 0$,
* $h_{1}$,
    * $\beta_{1}$ -smooth
* $\beta_{2} > 0$,
* $h_{2}$,
    * $\beta_{2}$ -smooth

* (1) $h_{1} + h_{2}$ is $(\beta_{1} + \beta_{2})$-smooth

#### proof

$$
\begin{eqnarray}
    h_{1}(y) + h_{2}(y)
    -
    h_{1}(x) + h_{2}(x)
    & \le &
        \nabla h_{1}(x) ^{\mathrm{T}}
        (y - x)
        +
        \frac{\beta_{1}}{2}
        \|
            y - x
        \|^{2}
        +
        \nabla h_{2}(x)^{\mathrm{T}}
        (y - x)
        +
        \frac{\beta_{1}}{2}
        \|
            y - x
        \|^{2}
    \nonumber
    \\
    & = &
        \nabla
        (h_{1}(x) + h_{2}(x)) ^{\mathrm{T}}
        (y - x)
        +
        \left(
            \frac{\beta_{1}}{2}
            +
            \frac{\beta_{2}}{2}
        \right)
        \|
            y - x
        \|^{2}
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 2.5
* $\beta > 0$
* $f$,
    * $\beta$-smooth function,
* $D > 0$
    * upper bound of diameter in $\mathcal{K}$,

$$
    x, y \in \mathcal{K},
    \
    \|
        x - y
    \|
    \le
    D
    .
$$

Algorithm 3 with parameter $\hat{\alpha} := \frac{\beta \log t}{D^{2} t}$ converges as

$$
    h_{t + 1}
    \le
    h_{1}^{g}
    \exp
    \left(
        -
        \frac{
            t
            \log t
        }{
            4
            \left(
                \log t
                +
                D^{2}t
            \right)
        }
    \right)
    +
    \frac{\beta \log t}{2t}
    .
$$


#### proof
$g$ defined in $$\eqref{algorithm03_definition_g}$$ is $\hat{\alpha}$-strongly convex.
Indeed,


By <a href="#proposition-additivity-of-beta-smooth">the previous proposition</a> and <a href="#proposition-propety-of-norm">proposition above</a>, $g$ is $(\beta + \hat{\alpha})$-smooth.

Thus, $g$ is $\gamma = \frac{\hat{\alpha}}{\hat{\alpha} + \beta}$-well-conditioned.

$$
\begin{eqnarray}
    h_{t}
    & = &
        f(x_{t})
        -
        f(x^{*})
    \nonumber
    & = &
        g(x_{t})
        -
        g(x^{*})
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                x^{*}
                -
                x_{1}
            \|^{2}
            -
            \|
                x_{t}
                -
                x_{1}
            \|^{2}
        \right)
    \nonumber
    \\
    & \le &
        h_{t}^{g}
        +
        \frac{\hat{\alpha}}{2}
        \left(
            D^{2}
        \right)
    \nonumber
    \\
    & = &
        h_{t}^{g}
        +
        \frac{\hat{\alpha}}{2}
        D^{2}
    \nonumber
\end{eqnarray}
$$

where $h_{t}^{g} := g(x_{t}) - g(x^{*})$.
Since $g$ is $\frac{\hat{\alpha}}{\hat{\alpha} + \beta}$-well-conditioned,

$$
\begin{eqnarray}
    h_{t + 1}
    & \le &
        h_{t + 1}^{g}
        +
        \frac{\hat{\alpha}}{2}
        D^{2}
    \nonumber
    \\
    & \le &
        h_{1}^{g}
        \exp
        \left(
            -
            \frac{
                \hat{\alpha}t
            }{
                4(\hat{\alpha} + \beta)
            }
        \right)
        +
        \frac{\hat{\alpha}}{2}
        D^{2}
        \quad
        (\because \text{theorem 2.4})
    \nonumber
    \\
    & = &
        h_{1}^{g}
        \exp
        \left(
            -
            \frac{
                t
                \beta \log t
            }{
                4
                \beta
                \left(
                    \log t
                    +
                    D^{2}t
                \right)
            }
        \right)
        +
        \frac{\beta \log t}{2t}
    \nonumber
    \\
    & = &
        h_{1}^{g}
        \exp
        \left(
            -
            \frac{
                t
                \log t
            }{
                4
                \left(
                    \log t
                    +
                    D^{2}t
                \right)
            }
        \right)
        +
        \frac{\beta \log t}{2t}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


### 2.3.2 Reduction to strongly convex, non-smooth functions


#### Algorithm 4 Gradient descent reduction to non-smooth functions
* $f$,
    * $\alpha$ strongly convex
    * $G$-Lipschitz continuous
* $x_{1}$,
    * initial point
* $T \in \mathbb{N}$,
* $\delta > 0$,

$$
    \hat{f}_{\delta}(x)
    :=
    \int_{\mathbb{B}}
        f(x + \delta u)
    \ du
    .
$$

**Step1** Apply algorithm 2 on $\hat{f}$, $x_{1}$, $T$, $$\{\eta_{t} = \delta\}$$, return $x_{T}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma 2.6
* $\hat{f}_{\delta}$,
    * Algorithm 4

Then

* (1) If $f$ is $\alpha$-strongly convex, then so is $\hat{f}_{\delta}$,
* (2) $\hat{f}_{\delta}$ is $\frac{d G}{\delta}$-smooth
* (3) $$\norm{ \hat{f}_{\delta}(x) - f(x) } \le \delta G$$ for all $x \in \mathcal{K}$,
    * TODO: we need to chekc whether the statement is correct or not

#### proof
(1) TODO

$$
\begin{eqnarray}
    \hat{f}_{\delta}(y)
    -
    \hat{f}_{\delta}(x)
    & \ge &
        \int_{\mathbb{B}}
            f(y + \delta u)
            -
            f(x + \delta u)
        \ du
    \nonumber
    \\
    & \ge &
        \int_{\mathbb{B}}
            \frac{\alpha}{2}
            \|
                y - x
            \|
            +
            \nabla
            f(x + \delta u) ^{\mathrm{T}}
            (y - x)
        \ du
        \quad
        (\because \text{strongly convex})
    \nonumber
    \\
    & = &
        \frac{\alpha}{2}
        \|
            y - x
        \|
        +
        \nabla
        \int_{\mathbb{B}}
            f(x + \delta u) ^{\mathrm{T}}
        \ du
        (y - x)
    \nonumber
    \\
    & = &
        \frac{\alpha}{2}
        \|
            y - x
        \|
        +
        \nabla
        \hat{f}(x)^{\mathrm{T}}
        (y - x)
    \nonumber
\end{eqnarray}
$$

The 3rd inequality follows from the fact that $f$ is integrable over unit cube and differentiable and Lebesgue dominated convergence theorem.


(2)
TODO

$$
    \mathbb{S}
    :=
    \{
        y \in \mathbb{R}^{d}
        \mid
        \|y\|
        =
        1
    \}
    .
$$

By Stokes theorem,

$$
\begin{equation}
    \int_{\mathbb{S}}
        f(x + \delta u)
        u
    \ du
    =
    \frac{\delta}{d}
    \nabla
    \int_{\mathbb{B}}
        f(x + \delta u)
    \ du
\end{equation}
$$

$$
\begin{eqnarray}
    \norm{
        \nabla \hat{f}_{\delta}(x)
        -
        \nabla \hat{f}_{\delta}(y)
        }
    & = &
        \frac{d}{\delta}
        \norm{
            \int_{\mathbb{S}}
                f(x + \delta u)
                u
            \ du
            -
            \int_{\mathbb{S}}
                f(y + \delta u)
                u
            \ du
        }
    \nonumber
    \\
    & = &
        \frac{d}{\delta}
        \norm{
            \int_{\mathbb{S}}
                f(x + \delta u)
                u
                -
                f(y + \delta u)
                u
            \ du
        }
    \nonumber
    \\
    & \le &
        \frac{d}{\delta}
        \int_{\mathbb{S}}
            \norm{
                f(x + \delta u)
                u
                -
                f(y + \delta u)
                u
            }
        \ du
        \quad
        (\because \text{Jensen's inequality})
    \nonumber
    \\
    & = &
        \frac{d}{\delta}
        \int_{\mathbb{S}}
            \abs{
                \left(
                    f(x + \delta u)
                    -
                    f(y + \delta u)
                \right)
            }
            \norm{u}
        \ du
    \nonumber
    \\
    & \le &
        \frac{d}{\delta}
        G
        \int_{\mathbb{S}}
            \norm{ x - y }
            \norm{ u }
        \ du
        \quad
        (\because \text{Lipschitz continity})
    \nonumber
    \\
    & \le &
        \frac{d}{\delta}
        G
        \norm{ x - y }
        \int_{\mathbb{S}}
            1
        \ du
        \quad
        (\because u \in \mathbb{S})
    \nonumber
    \\
    & = &
        \frac{d}{\delta}
        G
        \norm{ x - y }
        .
    \nonumber
\end{eqnarray}
$$

By proposition, $\hat{f}_{\delta}$ is $ \frac{d}{\delta} G$-smooth.

(3)

$$
\begin{eqnarray}
    \abs{
        \hat{f}_{\delta}(x)
        -
        f(x)
    }
    & = &
        \left|
            \int_{\mathbb{B}}
                f(x + \delta u)
                -
                f(x)
            \ du
        \right|
    \nonumber
    \\
    & \le &
        \int_{\mathbb{B}}
            \left|
                f(x + \delta u)
                -
                f(x)
            \right|
        \ du
        \quad
        (\because \text{Jensen's inequality})
    \nonumber
    \\
    & \le &
        G
        \int_{\mathbb{B}}
            \|
                \delta u
            \|
        \ du
        \quad
        (\because \text{Lipschitz})
    \nonumber
    \\
    & = &
        G
        \delta
        \int_{\mathbb{B}}
            1
        \ du
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 2.7

$$
    \delta
    :=
    \frac{
        d G
    }{
        \alpha
    }
    \frac{
        \log t
    }{
        t
    }
    .
$$

Algorithm 4 converges as

$$
    h_{t + 1}
    \le
    h_{1}
    \exp
    \left(
        -
        \frac{
            \log t
        }{
            4
        }
    \right)
    +
    \frac{
        2 d G^{2}
        \log t
    }{
        \alpha t
    }
$$

#### proof
By lemma 2.6, the function $\hat{f}_{\delta}$ is $\gamma$-well conditioned for 

$$
    \gamma
    :=
    \frac{
        \alpha \delta
    }{
        d G
    }
    .
$$

Hence

$$
\begin{eqnarray}
    h_{t + 1}
    & = &
        f(x_{t + 1})
        -
        f(x^{*})
    \nonumber
    \\
    & = &
        \hat{f}(x_{t+1})
        +
        f(x_{t + 1})
        -
        \hat{f}(x_{t + 1})
        -
        \hat{f}(x^{*})
        +
        \hat{f}(x^{*})
        -
        f(x^{*})
    \nonumber
    \\
    & \le &
        \hat{f}(x_{t+1})
        +
        \delta G
        -
        \hat{f}(x^{*})
        +
        \delta G
        \quad
        (\because \text{lemma 2.6 (3)})
    \nonumber
    \\
    & \le&
        h_{1}
        e^{
            -
            \frac{
                \gamma t
            }{
                4
            }
        }
        +
        2\delta G
        \quad
        (\because \text{lemma 2.4})
    \nonumber
    \\
    & \le&
        h_{1}
        \exp
        \left(
            -
            \frac{
                \alpha \delta t
            }{
                4 d G
            }
        \right)
        +
        2\delta G
    \nonumber
    \\
    & \le&
        h_{1}
        \exp
        \left(
            -
            \frac{
                \log t
            }{
                4
            }
        \right)
        +
        \frac{
            2 d G^{2}
            \log t
        }{
            \alpha t
        }
    \nonumber
    \\
    & \le&
        h_{1}
        \exp
        \left(
            -
            \frac{
                \log t
            }{
                4
            }
        \right)
        +
        \frac{
            2 d G^{2}
            \log t
        }{
            \alpha t
        }
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

There is an algorithm for $\alpha$-strongly convex function, which does not rely on expectation.
Even more the bound of the algorithm does not depend on the dimension $d$.

#### Theorem 2.8
* $f$,
    * $\alpha$-strongly convex
* $$x_{1}, \ldots, x_{t}$$,
    * the iterates of Algorithm 2 appied to $f$ with $\eta_{t}$

$$
    \eta_{t}
    :=
    \frac{
        2
    }{
        \alpha(t + 1)
    }
    .
$$

Then

$$
    f
    \left(
        \frac{1}{t}
        \sum_{s=1}^{t}
            \frac{
                2s
            }{
                t + 1
            }
            x_{x}
    \right)
    -
    f(x^{*})
    \le
    \frac{
        2G
    }{
        \alpha(t + 1)
    }
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

### 2.3.3 Reduction to general convex function
We can apply both the technique 

$$
\begin{eqnarray}
    g(x)
    & := &
        f(x)
        +
        \frac{\alpha}{2}
        \|
            x
            -
            x_{1}
        \|^{2}
    \nonumber
    \\
    \hat{f}_{\delta}(x)
    & := &
        \int_{\mathbb{B}}
            g(x + \delta u)
        \ du
    \nonumber
    \\
    & = &
        \int_{\mathbb{B}}
            f(x + \delta u)
            +
            \frac{\alpha}{2}
            \|
                x + \delta u
                -
                x_{1}
            \|^{2}
        \ du
    \nonumber
\end{eqnarray}
    .
$$

Then by <a href="#proposition-alpha-strongnize">proposition</a> $g$ is $\alpha$-strongly convex.
Moreover, by lemma 2.6, $\hat{f}_{\delta}$ is $dG/\delta$ smooth.
Thus, we have the same inequality in lemme 2.7.

However, there is an algorithm which gives the better inequality than the inequality from lemma 2.7, which is $O(\frac{1}{\sqrt{t}})$.
We will show this in next chapter.

## 2.4 Example: Support Vector Machine training
General linear classfication problem is stated as below.

* $d \in \mathbb{N}$,
    * the dimension of feature/input vector
* $n \in \mathbb{N}$,
* $a_{i} \in \mathbb{R}^{d} \ (i = 1, \ldots, n)$,
    * input vector
* $$b_{i} \in \{-1, 1\}$$,
    * label corresponding to input $a_{i}$,

A lot of loss functions can be considered for this classfication problems, but here we consider one of the simplest loss function.
The following equation is the problem to solve.

$$
\begin{equation}
    \min_{x \in \mathbb{R}^{d}}
        \sum_{i=1}^{n}
            1_{\mathrm{sign}(x^{\mathrm{T}} a_{i} \neq b_{i})}
    \label{equation_02_05}
\end{equation}
    .
$$

General classi

Support Vector Machine is pracitically used for classification.
The soft margin SV relaxation replaces the 0/1 loss in $$\eqref{equation_02_05}$$ with a convex loss, called the hinge-loss, given by

$$
\begin{eqnarray}
    \ell_{a, b}(x)
    & := &
        \mathrm{hinge}(b x^{\mathrm{T}}a)
    \nonumber
    \\
    & := &
        \max
        \{
            0,
            1 - b x^{\mathrm{T}}a
        \}
    \nonumber
    .
\end{eqnarray}
$$

Here we consider the loss function with regularization.

$$
\begin{equation}
    \min_{x \in \mathbb{R}^{d}}
    \left(
        \lambda
        \frac{1}{n}
        \sum_{i=1}^{n}
            \ell_{a_{i}, b_{i}}(x)
        +
        \frac{1}{2}
        \|
            x
        \|^{2}
    \right)
    \label{equation_02_06}
\end{equation}
    .
$$

#### Algorithm 5 SVM training via subgradient descent
* $$\{(a_{i}, b_{i})\}$$,
* $T \in \mathbb{N}$,
* $x_{1} := 0$,
* $\eta_{t} := \frac{2}{t + 1}$,
* $\lambda > 0$,
    * regulariztion parameter

**Step1.**

$$
\begin{eqnarray}
    \nabla_{t}
    & := &
        \lambda
        \frac{1}{n}
        \sum_{i=1}^{n}
            \ell_{a_{i}, b_{i}}(x_{t})
        +
        x_{t}
    \nonumber
    \\
    \nabla\ell_{a, b}(x)
    & = &
        \begin{cases}
            0
            &
                (b x^{\mathrm{T}}a > 1)
            \\
            -b a
            &
                \text{otherwise}
        \end{cases}
    \nonumber
\end{eqnarray}
$$

**Step2.** Update

$$
\begin{eqnarray}
    x_{t + 1}
    :=
    x_{t}
    -
    \eta_{t} \nabla_{t}
    \nonumber
\end{eqnarray}
$$

**Step3.** end for

**Step4.** Return $\tilde{x} := \frac{1}{T} \sum_{t=1}^{T} \frac{2t}{T + 1}x_{t}$,

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem
In Algorithm 5, if $T > \frac{1}{\epsilon}$,


$$
    f(\tilde{x})
    -
    f(x^{*})
    \in 
    O(\epsilon)
    .
$$

#### proof

<div class="end-of-statement" style="text-align: right">■</div>


