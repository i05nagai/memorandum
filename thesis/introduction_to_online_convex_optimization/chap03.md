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

$$
    \frac{1}{\alpha}
    \log T
    \le
    f(x)
    \le
    \frac{1}{\alpha}
    \log T
    .
$$

Average regret

## 3.1 Online gradient descent


#### Algorithm 6 online gradient descent
* $\mathcal{K}$,
    * convex set
* $T$,
* $x_{1} \in \mathcal{K}$,
* $$\{\eta_{t}\}$$,
    * step size

**Step1.** for $t=1, \ldots, T$

**Step2.** Play $x_{t}$ and observe cost $f_{t}(x_{t})$,

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

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 3.1
* $\mathcal{K}$,
    * convex
    * $D$-bounded
* $\eta_{t} := \frac{D}{G\sqrt{t}}$,
* $f_{t}$,
    * convex function

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

$$
\begin{equation}
    f_{t}(x_{t})
    -
    f_{t}(x^{*})
    \le
    \nabla f(x_{t})^{\mathrm{T}}
    (x_{t} - x^{*})
    \label{equation_03_01}
\end{equation}
$$

$$
\begin{eqnarray}
    \|
        x_{t+1}
        -
        x^{*}
    \|^{2}
    & = &
        \|
            \Pi_{\mathcal{K}}
            (x_{t} - \eta_{t}\nabla f(x_{t}))
            -
            x^{*}
        \|^{2}
    \nonumber
    \\
    & \le &
        \|
            (x_{t} - \eta_{t}\nabla f(x_{t}))
            -
            x^{*}
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
            x^{*}
        \|^{2}
        -
        2
        \eta_{t}
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x^{*})
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
            x^{*}
        \|^{2}
        -
        2
        \eta_{t}
        \nabla f(x_{t})^{\mathrm{T}}
        (x_{t} - x^{*})
        +
        \eta_{t}^{2}
        G^{2}
\end{eqnarray}
$$

Hence,

$$
\begin{eqnarray}
    & &
        2
        \eta_{t}
        \nabla f(x_{t}))^{\mathrm{T}}
        (x_{t} - x^{*})
        \le
        \|x_{t} - x^{*}\|^{2}
        -
        \|x_{t + 1} - x^{*}\|^{2}
        +
        \eta_{t}^{2}
        G^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        2
        \nabla f(x_{t}))^{\mathrm{T}}
        (x_{t} - x^{*})
        \le
        \frac{
            \|x_{t} - x^{*}\|^{2}
            -
            \|x_{t + 1} - x^{*}\|^{2}
        }{
            \eta_{t}
        }
        +
        \eta_{t}
        G^{2}
    \nonumber
\end{eqnarray}
$$

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
        \sum_{t=1}^{T}
            \frac{
                \|x_{t} - x^{*}\|^{2}
                -
                \|x_{t + 1} - x^{*}\|^{2}
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
                \|x_{t} - x^{*}\|^{2}
            }{
                \eta_{t}
            }
        -
        \sum_{t=2}^{T}
            \frac{
                \|x_{t} - x^{*}\|^{2}
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

Let $$\Lambda_{t, i}$$ be independent Bernoulli r.v.s whose values is in $$\{\pm 1\}$$.
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

<div class="QED" style="text-align: right">$\Box$</div>
