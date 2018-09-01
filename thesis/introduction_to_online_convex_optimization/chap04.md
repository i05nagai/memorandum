---
title: Introduction to Online Convex Optimization Chapter04
---

## Introduction to Online Convex Optimization Chapter04
We will introduce new class of convex functions: exp-concave functions.
In this case, there is a second-order algorithm.

## 4.1. Motivation: universal portfolio selection

* $$\{Z_{t}\}$$,
    * i.i.d.
    * $Z_{t} \sim \mathrm{N}(\mu, \sigma)$,
* $l \in \mathbb{R}$,
    * initial logarithmic price

We define logarithm of the price $l_{t}$ at $t$ by

$$
\begin{eqnarray}
    l_{0}
    & := &
        l
    \nonumber
    \\
    l_{t + 1}
    & := &
        l_{t}
        +
        Z_{i}
    \nonumber
\end{eqnarray}
    .
$$

Now we consider the following potrfolio selection problem.

* $n \in \mathbb{N}$,
    * the number of assets
* $x_{t} \in \Delta_{n}$,
    * the ratio of the investment at $t$,
    * we investment $x_{t}$ of wealth between $t$ and $t+1$,
* $$\Delta_{n} := \{x \in \mathbb{R}^{n} \mid \sum_{i=1}^{n}x_{n} = 1\}$$,
    * convex
* $r_{t} \in \mathbb{R}_{\ge 0}^{n}$,
    * $r_{t, i}$ is the price ratio for the $i$-th asset
* $W_{t}$,
    * total wealth at iteration $t$,

$$
    r_{t, i}
    :=
    \frac{
        \text{price of asset }i
        \text{ at time }t + 1
    }{
        \text{price of asset }i
        \text{ at time }t
    }
    .
$$

$$
\begin{eqnarray}
    W_{t + 1}
    & := &
        W_{t}
        r_{t}^{\mathrm{T}}
        x_{t}
    \nonumber
    W_{T}
    & = &
        W_{t}
        \prod_{t=1}^{T}
            r_{t}^{\mathrm{T}}
            x_{t}
    \nonumber
\end{eqnarray}
$$

Our goal is to maximize the overall wealth gain

$$
    \log
    \frac{
        W_{T}
    }{
        W_{1}
    }
    =
    \sum_{t=1}^{T}
        \log
            r_{t}^{\mathrm{T}}
            x_{t}
    .
$$

Let 

$$
\begin{eqnarray}
    \mathcal{F}^{\prime}
    & := &
        \{
            f: \mathcal{K} \rightarrow \mathbb{R}
            \mid
            f(x)
            :=
            -\log(
                r^{\mathrm{T}}
                x
            )
            \quad
            r \in \mathbb{R}^{n}
        \}
    \nonumber
    \\
    \mathcal{K}
    & := &
        \delta_{n}
    \nonumber
\end{eqnarray}
    .
$$

We define the regret as

$$
\begin{eqnarray}
    \mathrm{Regret}_{T}
    & := &
        \max_{x \in \mathcal{K}}
            \sum_{t=1}^{T}
                \log
                    r_{t}^{\mathrm{T}}
                    x
        -
        \sum_{t=1}^{T}
            \log
                r_{t}^{\mathrm{T}}
                x_{x}
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            f_{t}(x_{t})
        +
        \max_{x \in \mathcal{K}}
            -
            \sum_{t=1}^{T}
                f_{t}(x)
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            f_{t}(x_{t})
        -
        \min_{x \in \mathcal{K}}
            \sum_{t=1}^{T}
                f_{t}(x^{*})
    \nonumber
    .
\end{eqnarray}
$$

We can use online gradient descent algorithm which ensures $O(\sqrt{T})$ regret.


### 4.1.3 Constant rebalancing portfolios

## 4.2 Exp-concave functions

#### Proposition propoety
(1)

$$
    f \in \mathcal{F},
    \
    \nabla^{2} f(x)
    =
    \frac{
        r r^{\mathrm{T}}
    }{
        (r^{\mathrm{T}}x)^{2}
    }
    .
$$

(2)

$f \in \mathcal{F}$ is not strongly convex.


#### proof
TODO

<div class="QED" style="text-align: right">$\Box$</div>

Hence Hessian matrix of $f$ is rank one matrix.

#### Definition 4.1
* $\alpha > 0$,
* $\mathcal{K} \subseteq \mathbb{R}^{n}$,
* $f: \mathcal{K} \rightarrow \mathbb{R}$,

$f$ is said to be $\alpha$-exp-cncave over $\mathcal{K}$ if

$$
    g(x)
    :=
    e^{-\alpha f(x)}
$$

is concave function.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark

$$
    f(x)
    =
    -
    \frac{1}{\alpha}
    \log g(x)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma 4.1
* $\alpha > 0$,
* $f: \mathcal{K} \rightarrow \mathbb{R}$,
    * twice-differentiable

Then the following statements are equivalent

* (1) $f$ is $\alpha$-exp-concave
* (2)

$$
    \alpha
    \nabla f(x)
    \nabla f(x)^{\mathrm{T}}
    \preccurlyeq
    \nabla^{2}f(x)
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 4.2

* $D, G > 0$,
* $\mathcal{K}$,
    * $D$-bounded
    * convex
* $f: \mathcal{K} \rightarrow \mathbb{R}$,
    * $\alpha$-exp-concave function
    * gradients is bounded by $G$,
    * twice-differentialble

$$
    \forall 
    \gamma
    \le
    \frac{1}{2}
    \min
    \left\{
        \frac{
            1
        }{
            4 GD
        },
        \alpha
    \right\},
    \
    f(x)
    \ge
    f(y)
    +
    \nabla f(y)^{\mathrm{T}}
    (x - y)
    +
    \frac{\gamma}{2}
    (x - y)^{\mathrm{T}}
    \nabla f(y)
    \nabla f(y)^{\mathrm{T}}
    (x - y)
    .
$$

#### proof
By <a href="{{ site.baseurl }}/math/positive_definite_matrix.html#proposition-9">proposition</a>, $\nabla f(x) \nabla f(x)^{\mathrm{T}}$ is positive definite.
Since $2\gamma \le \alpha$, by <a href="{{ site.baseurl }}/thesis/introduction_to_online_convex_optimization/chap02.html#proposition-property-of-positive-definite">proposition</a>, we obtain.

$$
    2 \gamma
    \nabla f(x)
    \nabla f(x)^{\mathrm{T}}
    \preccurlyeq
    \nabla^{2}f(x)
    .
$$

Hence by lemma 4.2 $f$ is also $2\gamma$-exp-concave funciton.
Let $h(x) := \exp(-2\gamma f(x)$.
We can easily show that

$$
\begin{eqnarray}
    \nabla h(x)
    & = &
        -2\gamma
        \exp(- 2\gamma f(x))
        \nabla f(x)
    .
    \nonumber
\end{eqnarray}
$$

By concavity of $h$,

$$
\begin{eqnarray}
    & &
        h(x)
        \le
        h(y)
        +
        \nabla h(y)^{\mathrm{T}}
        (x - y)
    \nonumber
    \\
    & \Leftrightarrow &
        \exp(-2\gamma f(x))
        \le
        \exp(-2\gamma f(y))
        +
        -2\gamma
        \exp(- 2\gamma f(y))
        \nabla f(y)^{\mathrm{T}}
        (x - y)
    \nonumber
    \\
    & \Leftrightarrow &
        \exp(-2\gamma f(x))
        \le
        \exp(-2\gamma f(y))
        \left(
            1
            -
            2\gamma
            \nabla f(y)^{\mathrm{T}}
            (x - y)
        \right)
    \nonumber
    \\
    & \Leftrightarrow &
        -2\gamma f(x)
        \le
        -2\gamma f(y)
        +
        \log
        \left(
            1
            -
            2\gamma
            \nabla f(y)^{\mathrm{T}}
            (x - y)
        \right)
    \nonumber
    \\
    & \Leftrightarrow &
        f(x)
        \ge
        f(y)
        -
        \frac{1}{2 \gamma}
        \log
        \left(
            1
            -
            2\gamma
            \nabla f(y)^{\mathrm{T}}
            (x - y)
        \right)
\end{eqnarray}
    .
$$

Note that

$$
\begin{eqnarray}
    |
        2\gamma \nabla f(y)^{\mathrm{T}} (x - y)
    |
    & \le &
        2\gamma
        GD
    & \le &
        \frac{1}{4}
    .
\end{eqnarray}
$$

It's easy to confirm that

$$
\begin{eqnarray}
    \forall z \in [-\frac{1}{4}, \frac{1}{4}],
    \
    & &
        -\log(1 - z)
        \le
        z
        +
        \frac{1}{4}
        z^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \exp(1 - z)
        \ge
        -
        \frac{1}{4}
        \left(
            z
            +
            2
        \right)^{2}
        +
        1
    \nonumber
\end{eqnarray}
$$

Applying the inequality for $z = 2\gamma \nabla f(y)^{\mathrm{T}}(x - y)$,

$$
\begin{eqnarray}
    & \Leftrightarrow &
        f(x)
        \ge
        f(y)
        -
        \frac{1}{2 \gamma}
        \log
        \left(
            1
            -
            2\gamma
            \nabla f(y)^{\mathrm{T}}
            (x - y)
        \right)
    \nonumber
    \\
    & \Leftrightarrow &
        f(x)
        \ge
        f(y)
        +
        \frac{1}{2 \gamma}
        \left(
            2\gamma
            \nabla f(y)^{\mathrm{T}}
            (x - y)
            +
            \gamma^{2}
            (x - y)^{\mathrm{T}}
            \nabla f(y)
            \nabla f(y)^{\mathrm{T}}
            (x - y)
        \right)
    \nonumber
    \\
    & \Leftrightarrow &
        f(x)
        \ge
        f(y)
        +
        \nabla f(y)^{\mathrm{T}}
        (x - y)
        +
        \frac{\gamma}{2}
        (x - y)^{\mathrm{T}}
        \nabla f(y)
        \nabla f(y)^{\mathrm{T}}
        (x - y)
        \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## 4.3 The online Newton step algorithm
The online Newton algorithm is actually quasi-Newton algorithm for online problems.



#### Algorithm 9 online Newton stpe
* $f:\mathcal{K} \rightarrow \mathbb{R}$,
    * function
* $T \in \mathbb{N}$,
* $x_{1} \in \mathcal{K}$,
* $\tilde{\alpha} > 0$,
    * parameter
* $\gamma > 0$,
* $\epsilon > 0$,
* $A_{0} := \epsilon E_{n}$,
    * where $E_{n}$ is $n$ unit matrix

Step1. for $t=1$ to $T$

Step2. Choose $x_{t} \in \mathcal{K}$ and obverse cost $f_{t} \in \mathcal{F}$,

Step3. Rank-1 Update

$$
    A_{t}
    :=
    A_{t - 1}
    +
    \nabla f(x_{t})
    \nabla f(x_{t})^{\mathrm{T}}
    .
$$

Step4. Newton step and projections

$$
\begin{eqnarray}
    y_{t + 1}
    & := &
        x_{t}
        -
        \frac{1}{\gamma}
        A_{t}^{-1}
        \nabla f(x_{t})
    \nonumber
    \\
    x_{t + 1}
    & := &
        \Pi_{\mathcal{K}, A_{t}}
        (y_{t + 1})
\end{eqnarray}
$$

where $\Pi_{\mathcal{K}, A_{t}}$ is projection onto $\mathcal{K}$ with the norm defined by $A_{t}$.

Step5. end for

Step6. Return $x_{T+1}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
By <a href="{{ site.baseurl }}/math/positive_definite_matrix.html#proposition-9">proposition</a>, $\nabla f(x) \nabla f(x)^{\mathrm{T}}$ is positive definite.
Obviously, $E_{n}$ is positive definite.
It is easy confirm that the sum of the positive definite is also positive definite.
Hence $A_{t}$ is positive definite for all $t$.

$$
\begin{eqnarray}
    \Pi_{\mathcal{K}, A_{t}}
    (y_{t + 1})
    & := &
        \arg \min_{x \in \mathcal{K}}
            \|y_{t + 1} - x\|_{A_{t}}^{2}
    \nonumber
    \\
    & = &
        \arg \min_{x \in \mathcal{K}}
            (y_{t + 1} - x)^{\mathrm{T}}
            A_{t}
            (y_{t + 1} - x)
    \nonumber
\end{eqnarray}
    .
$$

Since $\nabla f(x) \nabla f(x)^{\mathrm{T}}$ is symmetric, $A_{t}$ is symmetric for all $t$.
Hence

$$
    (A_{t}^{-1})^{\mathrm{T}}
    =
    A_{t}^{-1}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 4.3
* $\gamma :=\frac{1}{2}\min(\frac{1}{4GD}, \alpha)$,
* $\epsilon := \frac{1}{\gamma^{2} D^{2}}$,
* $T > 4$,

$$
\begin{eqnarray}
    \mathrm{Regret}_{T}
    \le
    5
    \left(
        \frac{1}{\alpha}
        +
        GD
    \right)
    n \log T
    .
\end{eqnarray}
$$

#### proof
We first show the upper bound of $$\sum_{t=1}^{T}f(x_{t})^{\mathrm{T}}A_{t}^{-1}\nabal f(x_{t})$$,

$$
\begin{eqnarray}
    \nabla f(x_{t})^{\mathrm{T}}
    A_{t}^{-1}
    \nabla f(x_{t})
    & = &
        A_{t}^{-1}
        \bullet
        \nabla f(x_{t})
        \nabla f(x_{t})^{\mathrm{T}}
    \nonumber
    \\
    & = &
        A_{t}^{-1}
        \bullet
        \nabla f(x_{t})
        \nabla f(x_{t})^{\mathrm{T}}
    \nonumber
    \\
    & = &
        A_{t}^{-1}
        \bullet
        \nabla f(x_{t})
        \nabla f(x_{t})^{\mathrm{T}}
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 4.4
* $\gamma :=\frac{1}{2}\min(\frac{1}{4GD}, \alpha)$,
* $\epsilon := \frac{1}{\gamma^{2} D^{2}}$,
* $T > 4$,

In algorithm 9, 

$$
\begin{eqnarray}
    \mathrm{Regret}_{T}
    \le
    4
    \left(
        \frac{1}{\alpha}
        +
        GD
    \right)
    \left(
        \sum_{t=1}^{T}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
            +
            1
    \right)
    .
\end{eqnarray}
$$

#### proof
Let 

$$
    x^{*}
    :=
    \arg \min_{x \in \mathcal{K}}
        \sum_{t=1}^{T}
            f_{t}(x)
    .
$$

By lemma 4.2, we have

$$
\begin{eqnarray}
    f_{t}(x_{t})
    -
    f_{t}(x^{*})
    & \le &
        R_{t}
    \nonumber
    \\
    R_{t}
    & := &
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x^{*})
        -
        \frac{\gamma}{2}
        (x^{*} - x_{t})^{\mathrm{T}}
        \nabla f(x_{t})
        \nabla f(x_{t})^{\mathrm{T}}
        (x^{*} - x_{t})
        .
    \nonumber
\end{eqnarray}
$$

By definition of $y_{t+1}$,

$$
\begin{eqnarray}
    & &
        y_{t+1} - x^{*}
        =
        x_{t}
        -
        x^{*}
        -
        \frac{1}{\gamma}
        A_{t}^{-1}
        \nabla f(x_{t})
    \label{equation_04_01}
    \\
    & \Leftrightarrow &
        A_{t}
        (y_{t+1} - x^{*})
        =
        A_{t}(
            x_{t}
            -
            x^{*}
        )
        -
        \frac{1}{\gamma}
        \nabla f(x_{t})
    \label{equation_04_02}
\end{eqnarray}
$$

Multiplying the transpose of $$\eqref{equation_04_01}$$ by $$\eqref{equation_04_02}$$,

$$
\begin{eqnarray}
    (y_{t+1} - x^{*})^{\mathrm{T}}
    A_{t}
    (y_{t+1} - x^{*})
    & = &
        (
            x_{t}
            -
            x^{*}
        )^{\mathrm{T}}
        A_{t}(
            x_{t}
            -
            x^{*}
        )
        -
        \frac{1}{\gamma}
        \left(
            A_{t}^{-1}
            \nabla f(x_{t})
        \right)^{\mathrm{T}}
        A_{t}(
            x_{t}
            -
            x^{*}
        )
        -
        (x_{t} - x^{*})^{\mathrm{T}}
        \frac{1}{\gamma}
        \nabla f(x_{t})
        +
        \frac{1}{\gamma}
        \left(
            A_{t}^{-1}
            \nabla f(x_{t})
        \right)^{\mathrm{T}}
        \frac{1}{\gamma}
        \nabla f(x_{t})
    \nonumber
    \\
    & = &
        (
            x_{t}
            -
            x^{*}
        )^{\mathrm{T}}
        A_{t}(
            x_{t}
            -
            x^{*}
        )
        -
        \frac{2}{\gamma}
        \nabla f(x_{t})^{\mathrm{T}}
        (
            x_{t}
            -
            x^{*}
        )
        +
        \frac{1}{\gamma^{2}}
        \nabla f(x_{t})^{\mathrm{T}}
        A_{t}^{-1}
        \nabla f(x_{t})
    \label{equation_04_03}
    .
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    (y_{t+1} - x^{*})^{\mathrm{T}}
    A_{t}
    (y_{t+1} - x^{*})
    & = &
        \|
            y_{t+1} - x^{*}
        \|_{A_{t}}^{2}
    \nonumber
    \\
    & \ge &
        \|
            x_{t+1} - x^{*}
        \|_{A_{t}}^{2}
        \quad
        (\because \text{theorem 2.1})
    \nonumber
    \\
    & = &
        (x_{t+1} - x^{*})^{\mathrm{T}}
        A_{t}
        (x_{t+1} - x^{*})
    \nonumber
\end{eqnarray}
$$

From $$\eqref{equation_04_03}$$,

$$
\begin{eqnarray}
    & &
        (
            x_{t}
            -
            x^{*}
        )^{\mathrm{T}}
        A_{t}(
            x_{t}
            -
            x^{*}
        )
        -
        \frac{2}{\gamma}
        \nabla f(x_{t})^{\mathrm{T}}
        (
            x_{t}
            -
            x^{*}
        )
        +
        \frac{1}{\gamma^{2}}
        \nabla f(x_{t})^{\mathrm{T}}
        A_{t}^{-1}
        \nabla f(x_{t})
        \ge
        (x_{t+1} - x^{*})^{\mathrm{T}}
        A_{t}
        (x_{t+1} - x^{*})
    \nonumber
    \\
    & \Leftrightarrow &
        \frac{\gamma}{2}
        (
            x_{t}
            -
            x^{*}
        )^{\mathrm{T}}
        A_{t}(
            x_{t}
            -
            x^{*}
        )
        -
        \frac{\gamma}{2}
        (x_{t+1} - x^{*})^{\mathrm{T}}
        A_{t}
        (x_{t+1} - x^{*})
        +
        \frac{1}{\gamma 2}
        \nabla f(x_{t})^{\mathrm{T}}
        A_{t}^{-1}
        \nabla f(x_{t})
        \ge
        \nabla f(x_{t})^{\mathrm{T}}
        (
            x_{t}
            -
            x^{*}
        )
\end{eqnarray}
$$

Summing up over $t=1$ to $T$,

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        \nabla f(x_{t})^{\mathrm{T}}
        (
            x_{t}
            -
            x^{*}
        )
    & \le &
        \sum_{t=1}^{T}
            \frac{\gamma}{2}
            (
                x_{t}
                -
                x^{*}
            )^{\mathrm{T}}
            A_{t}(
                x_{t}
                -
                x^{*}
            )
            -
        \sum_{t=1}^{T}
            \frac{\gamma}{2}
            (x_{t+1} - x^{*})^{\mathrm{T}}
            A_{t}
            (x_{t+1} - x^{*})
            +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
    \nonumber
    \\
    & = &
        \sum_{t=}^{T}
            \frac{\gamma}{2}
            (
                x_{t}
                -
                x^{*}
            )^{\mathrm{T}}
            A_{t}(
                x_{t}
                -
                x^{*}
            )
        -
        \sum_{t=2}^{T}
            \frac{\gamma}{2}
            (x_{t} - x^{*})^{\mathrm{T}}
            A_{t-1}
            (x_{t} - x^{*})
        -
        \frac{\gamma}{2}
        (x_{T+1} - x^{*})^{\mathrm{T}}
        A_{T}
        (x_{T+1} - x^{*})
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
    \nonumber
    \\
    & = &
        \sum_{t=2}^{T}
            \frac{\gamma}{2}
            (
                x_{t}
                -
                x^{*}
            )^{\mathrm{T}}
            \left(
                A_{t}
                -
                A_{t-1}
            \right)
            (
                x_{t}
                -
                x^{*}
            )
        +
        \frac{\gamma}{2}
        (x_{t} - x^{*})^{\mathrm{T}}
        A_{1}
        ( x_{t} - x^{*})
        -
        \frac{\gamma}{2}
        (x_{T+1} - x^{*})^{\mathrm{T}}
        A_{T}
        (x_{T+1} - x^{*})
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \frac{\gamma}{2}
            (
                x_{t}
                -
                x^{*}
            )^{\mathrm{T}}
            \nabla f(x_{t})
            \nabla f(x_{t})^{\mathrm{T}}
            (
                x_{t}
                -
                x^{*}
            )
        +
        \frac{\gamma}{2}
        (x_{t} - x^{*})^{\mathrm{T}}
        \left(
            A_{1}
            -
            \nabla f(x_{t})
            \nabla f(x_{t})^{\mathrm{T}}
        \right)
        ( x_{t} - x^{*})
        -
        \frac{\gamma}{2}
        (x_{T+1} - x^{*})^{\mathrm{T}}
        A_{T}
        (x_{T+1} - x^{*})
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            \frac{\gamma}{2}
            (
                x_{t}
                -
                x^{*}
            )^{\mathrm{T}}
            \nabla f(x_{t})
            \nabla f(x_{t})^{\mathrm{T}}
            (
                x_{t}
                -
                x^{*}
            )
        +
        \frac{\gamma}{2}
        (x_{t} - x^{*})^{\mathrm{T}}
        \left(
            A_{1}
            -
            \nabla f(x_{t})
            \nabla f(x_{t})^{\mathrm{T}}
        \right)
        ( x_{t} - x^{*})
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
        \quad
        (\because \text{positive definiteness})
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        R_{t}
    & \le &
        \frac{\gamma}{2}
        (x_{t} - x^{*})^{\mathrm{T}}
        \left(
            A_{1}
            -
            \nabla f(x_{t})
            \nabla f(x_{t})^{\mathrm{T}}
        \right)
        ( x_{t} - x^{*})
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
    \nonumber
    \\
    & = &
        \frac{\gamma}{2}
        \epsilon
        (x_{t} - x^{*})^{\mathrm{T}}
        ( x_{t} - x^{*})
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
        \quad
        (\because A_{1} - 
            \nabla f(x_{t})
            \nabla f(x_{t})^{\mathrm{T}}
            =
            \epsilon E_{n})
    \nonumber
    \\
    & = &
        \frac{1}{2D^{2} \gamma}
        (x_{t} - x^{*})^{\mathrm{T}}
        ( x_{t} - x^{*})
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
    \nonumber
    \\
    & \le &
        \frac{1}{2\gamma}
        +
        \sum_{t=1}^{T}
            \frac{1}{\gamma 2}
            \nabla f(x_{t})^{\mathrm{T}}
            A_{t}^{-1}
            \nabla f(x_{t})
    .
    \nonumber
\end{eqnarray}
$$

Since $\gamma := \frac{1}{2}\min(\frac{1}{4GD}, \alpha),

$$
    \frac{1}{\gamma}
    \le
    2
    \left(
        \frac{1}{\alpha}
        +
        4GD
    \right)
    \le
    8
    \left(
        \frac{1}{\alpha}
        +
        GD
    \right)
    .
$$

This gives the lemma.

<div class="QED" style="text-align: right">$\Box$</div>


