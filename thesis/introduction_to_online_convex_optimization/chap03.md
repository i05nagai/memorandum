---
title: Introduction to Online Convex Optimization Chapter03
---

## Introduction to Online Convex Optimization Chapter03

$$
    \mathrm{Regret}(f)
    :=
    \sum_{t=1}^{T}
        f_{t}(x_{t})
    -
    \min_{x \in \mathcal{K}}
        \sum_{t=1}^{T}
            f_{t}(x)
    .
$$


* $f$,
    * $\alpha$-strongly convex

Average regret

## 3.1 Online gradient descent

#### Algorithm 6 online gradient descent
* $\mathcal{K}$,
    * convex set
* $\mathcal{F}$,
    * convex functions
* $T \in \mathbb{N}$,
* $x_{1} \in \mathcal{K}$,
* $$\{\eta_{t}\}$$,
    * step size

**Step1.** for $t=1, \ldots, T$

**Step2.** Play $x_{t}$ and observe cost $f_{t}(x_{t})$ where $f_{t} \in \mathcal{F}$,

**Step3.** Update and project

$$
\begin{eqnarray}
    y_{t+1}
    & := &
        x_{t} - \eta_{t}\nabla f_{t}(x_{t})
    \nonumber
    \\
    x_{t+1}
    & := &
        \Pi_{\mathcal{K}}
        (y_{t+1})
    \nonumber
        .
\end{eqnarray}
$$

**Step4.** end for

**Step5.** Return $x_{T + 1}$,

We denote this algorithm by $$\mathcal{A}_{OGD}(f_{1}, \ldots, f_{T}; \{\eta_{t}\})$$, that is,

$$
    \forall t \in \{0, \ldots, T\},
    \
    \mathcal{A}_{OGD}(f_{1}, \ldots, f_{t}; \{\eta_{s}\}_{s=1,\ldots,t})
    =
    x_{t + 1}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma1 difference between optimal points
* $\mathcal{F}$,
    * $G$-bounded convex functions
    * $C^{1}$-functions

In Algorithm 6, for any $x \in \mathcal{K}$,

$$
\begin{eqnarray}
    \|
        x_{t + 1}
        -
        x
    \|
    & \le &
        \|
            x_{t}
            -
            x
        \|
        +
        \eta_{t}^{2}
        \|
            \nabla f(x_{t})
        \|
        -
        2 \eta_{t}
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x)
        \label{lemma1_difference_between_optimal_points_01}
    \\
    & \le &
        \|
            x_{t}
            -
            x
        \|
        +
        \eta_{t}^{2}
        G^{2}
        -
        2 \eta_{t}
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x)
        \label{lemma1_difference_between_optimal_points_02}
\end{eqnarray}
$$

#### proof

$$
\begin{eqnarray}
    \|
        x_{t+1}
        -
        x
    \|^{2}
    & = &
        \|
            \Pi_{\mathcal{K}}
            (x_{t} - \eta_{t}\nabla f(x_{t}))
            -
            x
        \|^{2}
    \nonumber
    \\
    & \le &
        \|
            (x_{t} - \eta_{t}\nabla f(x_{t}))
            -
            x
        \|^{2}
        \quad
        (\because \text{theorem 2.1})
        \label{equation_03_02}
    \nonumber
    \\
    & = &
        \|
            x_{t}
            -
            x
        \|^{2}
        -
        2
        \eta_{t}
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x)
        +
        \|
            \eta_{t}\nabla f(x_{t}))
        \|^{2}
    \nonumber
    \\
    & \le &
        \|
            x_{t}
            -
            x
        \|^{2}
        -
        2
        \eta_{t}
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x)
        +
        \eta_{t}^{2}
        G^{2}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma2 bound of the linear approximation
* $\mathcal{F}$,
    * $G$-bounded convex functions
    * $C^{1}$-functions
* $\mathcal{K}$,
    * convex
    * $D$-bounded

In Algorithm 6, for any $x \in \mathcal{K}$,

$$
\begin{eqnarray}
    2
    \sum_{t=1}^{T}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (x_{t} - x)
    & = &
        \sum_{t=1}^{T}
            \|x_{t} - x\|^{2}
            \left(
                \frac{
                    1
                }{
                    \eta_{t}
                }
                -
                \frac{
                    1
                }{
                    \eta_{t-1}
                }
            \right)
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
        \quad
        (\because \frac{1}{\eta_{0}} := 0)
        \label{lemma2_bound_of_the_linear_approximation_equation_01}
    \\
    & \le &
        D^{2}
        \sum_{t=1}^{T}
            \left(
                \frac{
                    1
                }{
                    \eta_{t}
                }
                -
                \frac{
                    1
                }{
                    \eta_{t-1}
                }
            \right)
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
        \label{lemma2_bound_of_the_linear_approximation_equation_02}
\end{eqnarray}
$$

#### proof
By <a href="#lemma1-difference-between-optimal-points">lemma</a>, we have $$\eqref{lemma1_difference_between_optimal_points_02}$$.
Summing $$\eqref{lemma1_difference_between_optimal_points_02}$$ from $t=1$ to $T$,

$$
\begin{eqnarray}
    2
    \sum_{t=1}^{T}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (x_{t} - x)
    & \le &
        \sum_{t=1}^{T}
            \frac{
                \|x_{t} - x\|^{2}
                -
                \|x_{t + 1} - x\|^{2}
            }{
                \eta_{t}
            }
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \frac{
                \|x_{t} - x\|^{2}
            }{
                \eta_{t}
            }
        -
        \sum_{t=2}^{T}
            \frac{
                \|x_{t} - x\|^{2}
            }{
                \eta_{t-1}
            }
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \|x_{t} - x\|^{2}
            \left(
                \frac{
                    1
                }{
                    \eta_{t}
                }
                -
                \frac{
                    1
                }{
                    \eta_{t-1}
                }
            \right)
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
        \quad
        (\because \frac{1}{\eta_{0}} := 0)
    \nonumber
    \\
    & \le &
        D^{2}
        \sum_{t=1}^{T}
            \left(
                \frac{
                    1
                }{
                    \eta_{t}
                }
                -
                \frac{
                    1
                }{
                    \eta_{t-1}
                }
            \right)
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 3.1
* $\mathcal{K}$,
    * convex
    * $D$-bounded
* $\eta_{t} := \frac{D}{G\sqrt{t}}$,
* $f_{t}$,
    * $G$-bounded convex function

Then the regret of the Algorithm 6 is bounded by

$$
    \mathrm{Regret}_{T}
    =
    \sum_{t=1}^{T}
        f_{t}(x_{t})
    -
    \min_{x \in \mathcal{K}}
        \sum_{t=1}^{T}
            f_{t}(x^{*})
    \le
    \frac{3}{2}
    GD
    \sqrt{T}
    .
$$

#### proof
Let

$$
    x^{*}
    \in
    \arg\min_{x \in \mathcal{K}}
        \sum_{t=1}^{T}
            f_{t}(x^{*})
    .
$$

By convexity, we have

$$
\begin{eqnarray}
    f_{t}(x^{*})
    -
    f_{t}(x_{t})
    & \ge &
        \nabla f(x_{t})^{\mathrm{T}}
        (x^{*} - x_{t})
    \nonumber
    \\
    \Leftrightarrow 
    \
    f_{t}(x_{t})
    -
    f_{t}(x^{*})
    & \le &
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x^{*})
    .
    \label{equation_03_01}
\end{eqnarray}
$$

By <a href="#lemma1-difference-between-optimal-points">lemma</a>, we have $$\eqref{lemma1_difference_between_optimal_points_01}$$.
Summing $$\eqref{equation_03_01}$$ from $t=1$ to $T$,

$$
\begin{eqnarray}
    2
    \left(
        \sum_{t=1}^{T}
            f_{t}(x_{t})
        -
        f_{t}(x^{*})
    \right)
    & \le &
        2
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{*})
    \nonumber
    \\
    & \le &
        D^{2}
        \sum_{t=1}^{T}
            \left(
                \frac{
                    1
                }{
                    \eta_{t}
                }
                -
                \frac{
                    1
                }{
                    \eta_{t-1}
                }
            \right)
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
        \quad
        (\because \eqref{lemma2_bound_of_the_linear_approximation_equation_02})
    \nonumber
    \\
    & = &
        D^{2}
        \frac{
            1
        }{
            \eta_{T}
        }
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
    \nonumber
    \\
    & = &
        D
        \sqrt{T}
        G
        +
        G
        D
        \sum_{t=1}^{T}
            \frac{1}{\sqrt{t}}
    \nonumber
    \\
    & \le &
        3
        D
        \sqrt{T}
        G
    .
\end{eqnarray}
$$

The last equation is derived from the fact

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        \frac{1}{\sqrt{t}}
    & \le &
        \int_{0}^{T}
            \frac{1}{\sqrt{t}}
        \ dt
    \nonumber
    \\
    & = &
        [
            2
            \sqrt{t}
        ]_{0}^{T}
        =
        2\sqrt{T}
    \nonumber
    .
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


## 3.2 Lower bounds

#### Theroem 3.2
* $f$,

$$

$$

#### proof

$$
\begin{eqnarray}
    \mathcal{K}
    & := &
        \{
            x \in \mathbb{R}^{n}
            \mid
            \|x\|_{\infty}
            \le
            1
        \}
    \nonumber
    \\
    \mathcal{A}
    & := &
        \{
            -1, 1
        \}^{n}
    \nonumber
\end{eqnarray}
    .
$$

$$
    v \in \mathcal{A},
    \
    f_{v}: \mathbb{R}^{n} \rightarrow \mathbb{R},
    \quad
    f_{v}(x)
    :=
    v^{\mathrm{T}}
    x
    .
$$

$$
    \mathcal{F}
    :=
    \{
        f_{v}
        \mid
        v \in \mathcal{A}
    \}
    .
$$

$$
\begin{eqnarray}
    \|
        x - y
    \|
    & \le &
        \sqrt{
            \sum_{i=1}^{n}
                2^{2}
        }
        =
        2
        \sqrt{ n }
    \nonumber
    \\
    \|f(x) - f(y)\|
    & \le &
        \sqrt{
            \sum_{i=1}^{n}
                (\pm 1)^{2}
        }
        \|
            x - y
        \|
        =
        \sqrt{ n }
        \|
            x - y
        \|
    \nonumber
\end{eqnarray}
$$

Now, we show that

$$
    \min_{x \in \mathcal{K}}
        \sum_{i=1}^{n}
        \sum_{t=1}^{T}
            v_{t, i}
            x_{i}
    =
    \sum_{i=1}^{n}
        -
        \left|
            \sum_{t=1}^{T}
                v_{t, i}
        \right|
    .
$$

Indeed, since $$v_{t, i} \in \{\pm 1\}$$, $x_{i}$ can be $1$ or $-1$.
Moreover, since we can choose $x$ in each coordinate $i$ independently, we can minimize the equation for each coordinate $i$.
The above minimization is equivalent to

$$
    \sum_{i=1}^{n}
    \min_{z \in \{\pm 1\}}
        \sum_{t=1}^{T}
            v_{t, i}
            z
    =
    \sum_{i=1}^{n}
    \left(
        -
        \left|
            \sum_{t=1}^{T}
                v_{t, i}
        \right|
    \right)
    .
$$

Let $$\Lambda_{t, i}$$ be Bernoulli r.v.s whose values is in $$\{\pm 1\}$$.
Suppose $$\{\Lambda_{t, i}\}_{i=1,\ldots,n}$$ is independent for each $t = 1, \ldots, T$.
Let 

$$
    t = 1, \ldots, T
    \
    V_{t}
    :=
    (
        \Lambda_{t, 1},
        \cdots,
        \Lambda_{t, n}
    )
    .
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \min_{x \in \mathcal{K}}
            \sum_{t=1}^{T}
                f_{V_{t}}(x)
    \right]
    & = &
        \mathrm{E}
        \left[
            \min_{x \in \mathcal{K}}
                \sum_{i=1}^{n}
                    \sum_{t=1}^{T}
                        V_{t, i}
                        x_{i}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \sum_{i=1}^{n}
            \left(
                -
                \left|
                    \sum_{t=1}^{T}
                        V_{t, i}
                \right|
            \right)
        \right]
    \nonumber
    \\
    & = &
        -
        \sum_{i=1}^{n}
        \mathrm{E}
        \left[
            \left|
                \sum_{t=1}^{T}
                    V_{t, i}
            \right|
        \right]
    \nonumber
    \\
    & = &
        -
        n
        \mathrm{E}
        \left[
            \left|
                \sum_{t=1}^{T}
                    V_{t, 1}
            \right|
        \right]
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \left|
            \sum_{t=1}^{T}
                V_{t, 1}
        \right|
    \right]
    & = &
        \mathrm{E}
        \left[
            \left|
                \sum_{t=1}^{T}
                    1_{\{V_{t, 1} = 1\}}
                -
                (
                    T
                    -
                    \sum_{t=1}^{T}
                        1_{\{V_{t, 1} = 1\}}
                )
            \right|
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \left|
                2
                \sum_{t=1}^{T}
                    1_{\{V_{t, 1} = 1\}}
                -
                T
            \right|
        \right]
    \nonumber
    \\
    & = &
        \sum_{t=0}^{T}
            |
                2t
                -
                T
            |
            \frac{1}{2^{T}}
            \left(
                \begin{array}{c}
                    T \\
                    t
                \end{array}
            \right)
    \nonumber
    \\
    & = &
        \sum_{t=0}^{T}
            |
                2t
                -
                T
            |
            \frac{1}{2^{T}}
            \left(
                \begin{array}{c}
                    T \\
                    t
                \end{array}
            \right)
        \frac{
            T!
        }{
            k!(T - k)!
        }
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## 3.3 Logarithmic regret

### 3.3.1 Online gradient descent for strongly convex functions

#### Theorem 3.3
* $\mathcal{F}$,
    * $\alpha$-strongly functions
* $\eta_{t} := \frac{1}{\alpha t}$,
* $T \in \mathbb{N}$,

$$
    \mathrm{Regret}_{T}
    \le
    \frac{G^{2}}{2\alpha}
    \left(
        1
        +
        \log T
    \right)
    .
$$

#### proof
Let

$$
    x^{*}
    :=
    \arg\min_{x \in \mathcal{K}}
        \sum_{t=1}^{T}
            f_{t}(x)
    .
$$

By $\alpha$-strong convexity,

$$
\begin{equation}
    2(f_{t}(x_{t}) - f_{t}(x^{*}))
    \le
    2
    \nabla f_{t}(x_{t})^{\mathrm{T}}
    (x_{t} - x^{*})
    -
    \alpha
    \|
        x^{*} - x_{t}
    \|^{2}
    \label{equation_03_04}
    .
\end{equation}
$$

By theorem 2.1,

$$
\begin{eqnarray}
    \|
        x_{t + 1}
        -
        x^{*}
    \|^{2}
    & = &
        \|
            \Pi_{x \in \mathcal{K}}
            \left(
                x_{t}
                -
                \eta_{t} \nabla f_{t}(x_{t}
            \right)
            -
            x^{*}
        \|^{2}
    \nonumber
    \\
    & \le &
        \|
            x_{t}
            -
            \eta_{t} \nabla f_{t}(x_{t})
            -
            x^{*}
        \|^{2}
\end{eqnarray}
$$

Summing $$\eqref{equation_03_04}$$ from $t=1$ to $T$.

$$
\begin{eqnarray}
    2\sum_{t=1}^{T}
        (f_{t}(x_{t}) - f_{t}(x^{*}))
    & \le &
        2
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x^{*})
        -
        \alpha
        \sum_{t=1}^{T}
            \|
                x^{*} - x_{t}
            \|^{2}
        \quad
        (\because \eqref{equation_03_04})
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            \|x_{t} - x^{*}\|^{2}
            \left(
                \frac{
                    1
                }{
                    \eta_{t}
                }
                -
                \frac{
                    1
                }{
                    \eta_{t-1}
                }
            \right)
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
        -
        \alpha
        \sum_{t=1}^{T}
            \|
                x^{*} - x_{t}
            \|^{2}
        \quad
        (\because \eqref{lemma2_bound_of_the_linear_approximation_equation_01})
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \|x_{t} - x^{*}\|^{2}
            \left(
                \alpha
                t
                -
                \alpha
                (t - 1)
                -
                \alpha
            \right)
        +
        G^{2}
        \sum_{t=1}^{T}
            \eta_{t}
            \frac{1}{\alpha t}
    \nonumber
    \\
    & = &
        G^{2}
        \frac{1}{\alpha}
        \sum_{t=1}^{T}
            \frac{1}{t}
    \nonumber
    \\
    & \le &
        G^{2}
        \frac{1}{\alpha}
        \left(
            1
            +
            \int_{1}^{T}
                \frac{1}{x}
            \ dx
        \right)
    \nonumber
    \\
    & \le &
        G^{2}
        \frac{1}{\alpha}
        \left(
            1
            +
            \log T
        \right)
    \nonumber
    .
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## 3.4 Application; stochastic gradient descent

Stochastic opitimization problem is a problem to find the point of the minimum value of given function $f: \mathcal{K} \rightarrow \mathbb{R}$ under some condition that you can only access to random variables of gradient.
Under the stochastic optimization problem, we minimize the

$$
    \min_{x \in \mathcal{K}}
        f(x)
    .
$$

$\tilde{\nabla}_{x}$ is random variable of the gradient at $x$ with the following conditions;

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \tilde{\nabla}_{x}
    \right]
    & = &
        \nabla f(x)
        \label{stochastic_optimization_problem_expectation_random_gradient}
    \\
    \mathrm{E}
    \left[
        \|
            \tilde{\nabla}_{x}
        \|^{2}
    \right]
    & = &
        G^{2}
    \nonumber
\end{eqnarray}
$$

The first constraint is the random variables is equal to the gradient in the sense of expectation.

We will show that the regret bounds of the stochastic optimization problem is bounded by

$$
    \mathrm{Regret}_{T}
    :=
    O(DG\sqrt{T})
    .
$$

#### Algorithm 7 stochastic gradient descent
* $\mathcal{K}$,
    * $D$-bounded
    * convex set
    * $C^{1}$-function
* $x_{1} \in \mathcal{K}$,
    * initial point
* $$\{\eta_{t}\}$$,
    * step size
* $f: \mathcal{K} \rightarrow \mathbb{R}$,
    * convex


**Step1.** for $t=1$ to $T$ do


**Step2.** Let $$\tilde{\nabla}_{t}$$ be indendent and identical distribution of $\nabla_{x_{t}}$.

$$
\begin{eqnarray}
    f_{t}(x)
    & := &
        \langle
            \tilde{\nabla}_{t},
            x
        \rangle
\end{eqnarray}
$$

**Step3.** Update and project

$$
\begin{eqnarray}
    y_{t+1}
    & := &
        x_{t}
        -
        \eta_{t}
        \tilde{\nabla}_{t}
    \nonumber
    \\
    x_{t+1}
    & := &
        \Pi_{\mathcal{K}}(y_{t+1})
        \nonumber
\end{eqnarray}
$$

**Step4.** end for

**Step5.** Return $$\tilde{x}_{T} := \frac{1}{T}\sum_{t=1}^{T}x_{t}$$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 3.4
* $\eta_{t} := \frac{D}{G \sqrt{t}}$,
    * step sizes

In Algorithm 7,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        f(\tilde{x}_{T})
    \right]
    & \le &
        \min_{x \in \mathcal{K}}
            f(x)
        +
        \frac{
            3 GD
        }{
            2 \sqrt{T}
        }
    \nonumber
\end{eqnarray}
$$

#### proof
Let

$$
    x^{*}
    :=

    \arg\min_{x \in \mathcal{K}}
        f(x)
$$

By the regret guarantee of OGD, we have

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        f(\tilde{x}_{T})
    \right]
    -
    f(x^{*})
    & = &
        \mathrm{E}
        \left[
            f
            \left(
                \frac{1}{T}
                \sum_{t=1}^{T}
                    \tilde{x}_{T}
            \right)
        \right]
        -
        f(x^{*})
    \nonumber
    \\
    & \le &
        \frac{1}{T}
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
            f
            \left(
                \tilde{x}_{T}
            \right)
        \right]
        -
        \sum_{t=1}^{T}
        \frac{1}{T}
        f(x^{*})
        \quad
        (\because \text{convexity of }f)
    \nonumber
    \\
    & \le &
        \frac{1}{T}
        \sum_{t=1}^{T}
        \mathrm{E}
        \left[
            \nabla f(x_{t})^{\mathrm{T}}
            (x_{t} - x^{*})
        \right]
        \quad
        (\because \text{convexity of }f)
    \nonumber
    \\
    & = &
        \frac{1}{T}
        \sum_{t=1}^{T}
        \mathrm{E}
        \left[
            \tilde{\nabla}_{t}^{\mathrm{T}}
            (x_{t} - x^{*})
        \right]
        \quad
        (\because \eqref{stochastic_optimization_problem_expectation_random_gradient} \text{ and linearity of expectation})
    \nonumber
    \\
    & = &
        \frac{1}{T}
        \sum_{t=1}^{T}
        \mathrm{E}
        \left[
            f_{t}(x_{t})
            -
            f_{t}(x^{*})
        \right]
        \quad
        (\because \text{ definition of }f_{t})
    \nonumber
    \\
    & \le &
        \frac{\mathrm{Regret}_{T}}{T}
        \quad
        (\because \text{ definition of regret})
    \nonumber
    \\
    & \le &
        \frac{3GD}{2\sqrt{T}}
        \quad
        (\because \text{ theorem 3.1})
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### 3.4.1 Example: stochastic gradient descent for SVM traning
We again consider SVM with hinge loss and regularization.

$$
\begin{eqnarray}
    f(x)
    & := &
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
    .
    \nonumber
    \\
    \ell_{a, b}(x)
    & = &
        \max
        \{
            0,
            1 - b x^{\mathrm{T}}a
        \}
    .
    \nonumber
\end{eqnarray}
$$

#### Algorithm 8 SGD for SVM training
* $$\{(a_{i}, b_{i})\}$$,
* $T \in \mathbb{N}$,
* $x_{1} := 0$,
* $\eta_{t} := \frac{2}{t + 1}$,
* $\lambda > 0$,
    * regulariztion parameter

**Step1.** For $t = 1$ to $T$

**Step2.** Pick an example uniformly at random $$K_{t} \in \{1, \ldots, n\}$$.

**Step3.** Let

$$
\begin{eqnarray}
    \tilde{\nabla}_{t}
    & := &
        \lambda
        \ell_{a_{K_{t}}, b_{K_{t}}}(x_{t})
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

**Step4.** Update

$$
\begin{eqnarray}
    x_{t + 1}
    :=
    x_{t}
    -
    \eta_{t}
    \tilde{\nabla}_{t}
    \nonumber
\end{eqnarray}
$$

**Step3.** end for

**Step4.** Return $\tilde{x} := \frac{1}{T} \sum_{t=1}^{T} x_{t}$,

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem
* $\epsilon > 0$,

In Algorithm 8, if $T \in O(\frac{1}{\epsilon^{2}})$,

$$
    f(\tilde{x})
    -
    f(x^{*})
    \in
    O(\epsilon)
$$

for some $\eta_{t}$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>
