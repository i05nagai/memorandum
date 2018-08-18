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
    .
$$


#### proof
$g$ defined in $$\eqref{algorithm03_definition_g}$$ is $\hat{\alpha}$-strongly convex.
Indeed, TODO

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
                x - x_{1}
            \|^{2}
            -
            \|
                y - x_{1}
            \|^{2}
        \right)
    \nonumber
    \\
    & = &
        \nabla f(y)^{\mathrm{T}}
        (y - x)
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                x - x_{1}
            \|
            -
            \|
                y - x_{1}
            \|
        \right)
        \left(
            \|
                x - x_{1}
            \|
            +
            \|
                y - x_{1}
            \|
        \right)
    \nonumber
    \\
    & \ge &
        \nabla f(y)^{\mathrm{T}}
        (y - x)
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                x - x_{1}
            \|
            -
            \|
                y - x_{1}
            \|
        \right)
        \|
            y - x
        \|
    \nonumber
    \\
    & \ge &
        \nabla f(y)^{\mathrm{T}}
        (y - x)
        +
        \frac{\hat{\alpha}}{2}
        \left(
            \|
                x - y
            \|
            -
            \|
                y - x_{1}
            \|
            -
            \|
                y - x_{1}
            \|
        \right)
        \|
            y - x
        \|
    \nonumber
\end{eqnarray}
$$

$g$ is $(\beta + \hat{\alpha})$-smooth.

Thus, it is $\gamma = \frac{\hat{\alpha}}{\hat{\alpha} + \beta}$-well-conditioned.

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
                -\hat{\alpha}t
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
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>
