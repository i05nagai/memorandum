---
title: Introduction to Online Convex Optimization Chapter05
---

## Introduction to Online Convex Optimization Chapter05

In online covex problem, one of the simplest algorithm is the Follow The Leader method, which just choose the action that has performed the best until current iteration, that is, we choose $x_{t+1}$ as

$$
    x_{t+1}
    :=
    \arg \min_{x \in \mathcal{K}}
        \sum_{t=1}^{s}
            f_{t}(x)
    .
$$

We will give an example which FTL method does not perform well in.

#### Example Follow The Leader

<div class="end-of-statement" style="text-align: right">■</div>


#### 5.1 Regularization functions

* $R: \mathcal{K} \rightarrow \mathbb{R}$,
    * regularization function
    * strongly convex and smooth
    * twice differentiable in $\mathrm{Int}(\mathcal{K})$,
        * we assume for simplicity
* $D_{R} \in \mathbb{R}$,
    * diameter of the set $\mathcal{K}$ relative to the function $R$,

$$
    D_{R}
    :=
    \sqrt{
        \max_{x, y \in \mathcal{K}}
        \left(
            R(x)
            -
            R(y)
        \right)
    }
    .
$$

The dual norm to a norm is 

$$
    \|
        y
    \|^{*}
    :=
    \max_{ \|x\|y }
        \langle
            x,
            y
        \rangle
    .
$$

$$
    \|
        x
    \|_{A}
    :=
    \sqrt{
        x^{\mathrm{T}}
        A
        x
    }
    .
$$

For instance, if the norm is the matrix norm defined by $A$, the dual norm is

$$
    \norm{x}_{A}^{*}
    =
    \norm{x}_{A^{-1}}
    .
$$

#### Definition 5.1
* $$B_{R}(x \parallel y) \in \mathbb{R}$$,

$B_{R}(x \parallel y) \in \mathbb{R}$ is called Bregman divergence with respect to the function $R$, defined as

$$
    B_{R}(x \parallel y)
    :=
    R(x)
    -
    R(y)
    -
    \nabla R(y)^{\mathrm{T}}(x - y)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
Suppose that $R$ is twice differentiable.
Then by talor thorem, for some $c_{x, y} \in [0, 1]$,

$$
    R(x)
    =
    R(y)
    +
    \nabla R(x)(x - y)
    +
    \frac{1}{2}
    (x - y)^{\mathrm{T}}
    \nabla^{2} R(y + c_{x, y}(x - y))
    (x - y)
    .
$$

Hence

$$
    B_{R}(x \parallel y)
    =
    \frac{1}{2}
    (x - y)^{\mathrm{T}}
    \nabla^{2} R(y + c_{x ,y}(x - y))
    (x - y)
    .
$$

We use the following norm defined by positive definite matrix $\nabla^{2} R(x)$.

$$
\begin{eqnarray}
    \langle
        x,
        y
    \rangle_{z, R}
    & := &
        x^{\mathrm{T}}
        \nabla^{2} R(z)
        y
        \label{definition_inner_product}
    \\
    \norm{x}_{z, R}
    & := &
        \left(
            \langle
                x,
                y
            \rangle_{z, R}
        \right)^{-1/2}
    \nonumber
    \\
    & = &
        x^{\mathrm{T}}
        \nabla^{2} R(z)
        x
        \label{definition_norm_local}

    \\
    \norm{y}_{z, R}^{*}
    & := &
        \sup_{\norm{x}_{z, R} \le 1}
            \langle
                x,
                y
            \rangle_{z, R}
        \label{definition_dual_norm_local}
    .
\end{eqnarray}
$$

If we take $z_{x, y} := y + c_{x, y}(x - y)$,

$$
\begin{equation}
    B_{R}(x \parallel y)
    =
    \frac{1}{2}
    (\norm{x - y}_{z_{x, y}})^{2}
    \label{equation_bregman_divergence_relation_to_local_norm}
\end{equation}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

## 5.2 The RFTL algorithm and its analysis
By the convexity of $f_{t}$,

$$
\begin{equation}
    \sum_{t=1}^{T}
        f_{t}(x_{t})
    -
    \sum_{t=1}^{T}
        f_{t}(x)
    \le
    \sum_{t=1}^{T}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (x_{t} - x)
    \label{equation_05_01}
\end{equation}
$$
.

### 5.1 Meta-algorithm definition

#### Algorithm 10 Regularized Follow The Leader
* $\eta > 0$,
* $\mathcal{K}$,
    * convex compact
* $R: \mathcal{K} \rightarrow \mathbb{R}$,
    * regularization function

$$
    x_{1}
    :=
    \arg\min_{x \in \mathcal{K}}
        R(x)
    .
$$

**Step1.** for $t=1$ to $T$

**Step2.** Predict $x_{t}$

**Step3.** Observe $f_{t} \in \mathcal{F}$

**Step4.** Update

$$
\begin{eqnarray}
    x_{t+1}
    & := &
        \arg\min_{x \in \mathcal{K}}
        \left(
            \eta
            \sum_{s=1}^{t}
                \nabla f(x_{s})^{\mathrm{T}}
                x
            +
            R(x)
        \right)
\end{eqnarray}
$$

**Step5.** end for

**Step6.** return $x_{T+1}$

<div class="end-of-statement" style="text-align: right">■</div>

### 5.2.2 The regret bound

#### Theorem 5.1
* $R$,
    * convex function

$$
\begin{equation}
    \mathrm{Regret}_{T}
    \le
    2\eta
    \sum_{t=1}^{T}
        (\norm{\nabla f_{t}(x_{t})}_{t}^{*})^{2}
    +
    \frac{
        R(u) - R(x_{1})
    }{
        \eta
    }
    \nonumber
\end{equation}
$$

#### proof
Let

$$
\begin{eqnarray}
    \Psi_{t}(x)
    & := &
        \left(
            \eta
            \sum_{s=1}^{t}
                \nabla f_{s}(x_{s})^{\mathrm{T}}
                x
            +
            R(x)
        \right)
    \nonumber
    \\
    \nabla
        \Psi_{t}(x)
    & = &
        \left(
            \eta
            \sum_{s=1}^{t}
                \nabla f_{s}(x_{s})
            +
            \nabla
            R(x)
        \right)
    \nonumber
    \\
    \nabla^{2}
        \Psi_{t}(x)
    & = &
        \nabla^{2}
        R(x)
    \nonumber
\end{eqnarray}
    .
$$

By the taylor expansion, for some $$z_{t} \in \{x_{t} + c(x_{t+1} - x_{t}) \mid c \in [0, 1]\}$$.

$$
\begin{eqnarray}
    \Psi_{t}(x_{t})
    & = &
        \left(
            \eta
            \sum_{s=1}^{t}
                \nabla f_{s}(x_{s})^{\mathrm{T}}
                x_{t}
            +
            R(x_{t})
        \right)
    \nonumber
    \\
    & = &
        \eta
        \sum_{s=1}^{t}
            \nabla f_{s}(x_{s})^{\mathrm{T}}
            x_{t + 1}
        +
        \eta
        \sum_{s=1}^{t}
            \nabla f_{s}(x_{s})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        +
        R(x_{t})
    \nonumber
    \\
    & = &
        \eta
        \sum_{s=1}^{t}
            \nabla f_{s}(x_{s})^{\mathrm{T}}
            x_{t + 1}
        +
        \eta
        \sum_{s=1}^{t}
            \nabla f_{s}(x_{s})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        +
        R(x_{t + 1})
        +
        \nabla R(x_{t + 1})^{\mathrm{T}}
        (x_{t} - x_{t + 1})
        +
        \frac{1}{2}
        (x_{t} - x_{t + 1})^{\mathrm{T}}
        \nabla^{2} R(c)
        (x_{t} - x_{t + 1})
    \nonumber
    \\
    & = &
        \Psi_{t}(x_{t + 1})
        +
        \eta
        \sum_{s=1}^{t}
            \nabla f_{s}(x_{s})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        +
        \nabla R(x_{t + 1})^{\mathrm{T}}
        (x_{t} - x_{t + 1})
        +
        B_{R}(x_{t} \parallel x_{t + 1})
    \nonumber
    \\
    & = &
        \Psi_{t}(x_{t + 1})
        +
        \Psi_{t}(x_{t + 1})^{\mathrm{T}}
        (x_{t} - x_{t + 1})
        +
        B_{R}(x_{t} \parallel x_{t + 1})
    \nonumber
    \\
    & \ge &
        \Psi_{t}(x_{t + 1})
        +
        B_{R}(x_{t} \parallel x_{t + 1})
        \quad
        (\because \text{theorem 2.2 KKT condition})
\end{eqnarray}
$$

The last inequality holds since $x_{t + 1}$ is the minimum point over $\mathcal{K}$ in Algorithm 10.
Thus,

$$
\begin{eqnarray}
    B_{R}(x_{t} \parallel) x_{t + 1})
    & \le &
        \Psi_{t}(x_{t})
        -
        \Psi_{t}(x_{t + 1})
    \nonumber
    \\
    & = &
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(x_{t})
        +
        R(x_{t})
        +
        \eta
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        x_{t}
        -
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(x_{t+1})
        -
        R(x_{x+1})
        -
        \eta
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            x_{t+1}
    \nonumber
    \\
    & = &
        \Psi_{t - 1}(x_{t})
        -
        \Psi_{t - 1}(x_{t+1})
        +
        \eta
        \nabla f_{t}(x_{t})
        \left(
            x_{t}
            -
            x_{t + 1}
        \right)
    \nonumber
    \\
    & \le &
        \eta
        \nabla f_{t}(x_{t})
        \left(
            x_{t}
            -
            x_{t + 1}
        \right)
        \quad
        (\because x_{t}\text{ is the minimizer of }\Psi_{t -1})
        \label{equation_05_02}
    .
\end{eqnarray}
$$

We use the norm defined in $$\eqref{definition_norm_local}$$,


$$
\begin{eqnarray}
    \nabla f_{t}(x_{t})^{\mathrm{T}}
    (x_{t} - x_{t + 1})
    & \le &
        \norm{
            \nabla f_{t}(x_{t})
        }_{z_{t}, R}^{*}
        \norm{
            (x_{t} - x_{t + 1})
        }_{z_{t}, R}
    \nonumber
    \\
    & = &
        \norm{
            \nabla f_{t}(x_{t})
        }_{z_{t}, R}^{*}
        \sqrt{
            2 B_{R}(x_{t} \parallel x_{t+1})
        }
        \quad
        (\because \eqref{equation_bregman_divergence_relation_to_local_norm})
    \nonumber
    \\
    & \le &
        \norm{
            \nabla f_{t}(x_{t})
        }_{z_{t}, R}^{*}
        \sqrt{
            2 \eta 
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        }
        \quad
        (\because \eqref{equation_05_02})
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    & &
        \sqrt{
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        }
        \le
        \norm{
            \nabla f_{t}(x_{t})
        }_{z_{t}, R}^{*}
        \sqrt{
            2 \eta 
        }
    \nonumber
    \\
    & \Leftrightarrow &
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (x_{t} - x_{t + 1})
        \le
        \left(
            \norm{
                \nabla f_{t}(x_{t})
            }_{z_{t}, R}^{*}
        \right)^{2}
        2 \eta
        \label{equation_05_02_modified}
\end{eqnarray}
$$

By lemma 5.2,

$$
\begin{eqnarray}
    \mathrm{Regret}_{T}
    & \le &
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        +
        \frac{
            R(u) - R(x_{1})
        }{
            \eta
        }
        \quad
        (\because \text{lemma 5.2})
    \nonumber
    \\
    & \le &
        2 \eta
        \sum_{t=1}^{T}
            \left(
                \norm{
                    \nabla f_{t}(x_{t})
                }_{z_{t}, R}^{*}
            \right)^{2}
        +
        \frac{
            R(u) - R(x_{1})
        }{
            \eta
        }
        \quad
        \eqref{equation_05_02_modified}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 5.2
* $u \in \mathcal{K}$,

In Algorithm 10,

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        f_{t}(x_{t})
    -
    \sum_{t=1}^{T}
        f_{t}(u)
    & \le &
        \mathrm{Regret}_{T}
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t+1})
        +
        \frac{
            R(u) - R(x_{1})
        }{
            \eta
        }
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t+1})
        +
        \frac{
            D_{R}^{2}
        }{
            \eta
        }
    .
    \nonumber
\end{eqnarray}
$$

#### proof
Let

$$
\begin{eqnarray}
    g_{0}(x)
    & := &
        \frac{1}{\eta}
        R(x)
    \nonumber
    \\
    g_{t}(x)
    & := &
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        x
    .
    \nonumber
\end{eqnarray}
$$

By convexity of $f$,

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        f_{t}(x_{t})
    -
    \sum_{t=1}^{T}
        f_{t}(x^{*})
    & \le &
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x^{*})
        \quad
        (\because \text{convexity of }f)
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \left(
                g_{t}(x_{t})
                -
                g_{t}(x^{*})
            \right)
    \nonumber
\end{eqnarray}
$$

where $$x^{*} := \arg\min_{x \in \mathcal{K}}\sum_{t=1}^{T}f_{t}(x)$$.
Hence it suffices to show the following equation.

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        g_{t}(x_{t})
    -
    \sum_{t=1}^{T}
        g_{t}(x^{*})
    \le
    \sum_{t=1}^{T}
        \left(
            g_{t}(x_{t})
            -
            g_{t}(x_{t + 1})
        \right)
    +
    \frac{D_{R}^{2}}{\eta}
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        g_{t}(x_{t})
    -
    \sum_{t=1}^{T}
        g_{t}(x^{*})
    & \le &
        \sum_{t=1}^{T}
            g_{t}(x_{t})
        -
        \sum_{t=1}^{T}
            g_{t}(x^{*})
        +
        \sum_{t=0}^{T}
            \left(
                g_{t}(x^{*})
                -
                g_{t}(x_{t + 1})
            \right)
        \quad
        (\because \text{lemma 5.3})
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            g_{t}(x_{t})
        -
        \sum_{t=1}^{T}
            g_{t}(x_{t + 1})
        +
        g_{0}(x^{*})
        -
        g_{0}(x_{1})
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \left(
                g_{t}(x_{t})
                -
                g_{t}(x_{t + 1})
            \right)
        +
        \frac{1}{\eta}
        \left(
            R(x^{*})
            -
            R(x_{1})
        \right)
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            \left(
                g_{t}(x_{t})
                -
                g_{t}(x_{t + 1})
            \right)
        +
        \frac{1}{\eta}
        D_{R}^{2}
    \nonumber
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>

#### lemma 5.3
* $u \in \mathcal{K}$,

$$
\begin{eqnarray}
    g_{0}(x)
    & := &
        \frac{1}{\eta}
        R(x)
    \nonumber
    \\
    g_{t}(x)
    & := &
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        x
    \nonumber
    \\
    \sum_{t=0}^{T}
        g_{t}(u)
    & \ge &
        \sum_{t=0}^{T}
            g_{t}(x_{t + 1})
    \nonumber
\end{eqnarray}
$$

#### proof.
We will show by induction on $T$.

Suppose $T=0$.
Since $$x_{1} := \arg\min_{x \in \mathcal{K}}R(x)$,

$$
\begin{eqnarray}
    & &
        g_{0}(u)
        \ge
        g_{0}(x_{1})
    \nonumber
    \\
    & \Leftrightarrow &
        R(u)
        \ge
        R(x_{1})
    .
    \nonumber
\end{eqnarray}
$$

Suppose the inequality holds up to $T$.
We will show the inequality holds $T + 1.
Since $x_{T + 2} := \arg\min_{x \in \mathcal{K}} \sum_{t=0}^{T + 1} g(x)$,

$$
\begin{eqnarray}
    \sum_{t=0}^{T + 1}
        g_{t}(u)
    & \ge &
        \sum_{t=0}^{T + 1}
            g_{t}(x_{T + 2})
    \nonumber
    \\
    & = &
        \sum_{t=0}^{T}
            g_{t}(x_{T + 2})
        +
        g_{T+1}(x_{T + 2})
    \nonumber
    \\
    & \ge &
        \sum_{t=0}^{T}
            g_{t}(x_{t + 1})
        +
        g_{T+1}(x_{T + 2})
        \quad
        (\because \text{by induction})
    \nonumber
    \\
    & = &
        \sum_{t=0}^{T + 1}
            g_{t}(x_{t + 1})
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## 5.3 Online Mirrored Descent


#### Algorithm 11 Lazy/Agile Online Mirrored Descent
* $\eta > 0$,
* $\mathcal{K}$,
    * convex compact
* $R: \mathcal{K} \rightarrow \mathbb{R}$,
    * regularization function
* $y \in \mathcal{K}$,
    * $y_{1}$ satisfies $\nalba R(y_{1}) = 0$,

$$
\begin{eqnarray}
    x_{1}
    & := &
        \arg\min_{x \in \mathcal{K}}
            B_{R}(x \parallel y_{1})
    \nonumber
\end{eqnarray}
    .
$$

**Step1.** for $t=1$ to $T$

**Step2.** Play $x_{t}$

**Step3.** Observe $f_{t}(x_{t})$,

**Step4.** Update $y_{t}$ according to the rule (a) or (b),

Rule for lazy OMD

$$
\begin{eqnarray}
    \nabla R(y_{t + 1})
    & = &
        \nabla R(y_{t})
        -
        \eta \nabla f(x_{t})
\end{eqnarray}
$$

Rule for Agile OMD

$$
\begin{eqnarray}
    \nabla R(y_{t + 1})
    & = &
        \nabla R(x_{t})
        -
        \eta \nabla f(x_{t})
\end{eqnarray}
$$

**Step5.** Project according to $B_{R}:$

$$
\begin{eqnarray}
    x_{t + 1}
    :=
    \arg\min_{x \in \mathcal{K}}
        B_{R}(x \parallel y_{t + 1})
    \nonumber
\end{eqnarray}
$$

**Step6.** end for

**Step7.** Return $x_{T + 1}$,

<div class="end-of-statement" style="text-align: right">■</div>

### 5.3.1 Equivalence of lazy OMD and RFTL.


#### Lemma 5.4
* $f_{1}, \ldots, f_{T}$,
    * linear cost functions
* $$\{y_{t}\}$$,
    * produced by Algorithm 11
* $$\{x_{t}\}$$,
    * produced by Algorithm 10

$$
    \arg\min_{x \in \mathcal{K}}
        B_{R}(x \parallel y_{t})
    =
    \arg\min_{x \in \mathcal{K}}
    \left(
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(x_{s})^{\mathrm{T}}
            x
        +
        R(x)
    \right)
    .
$$

#### proof
Let

$$
    x_{t}^{*}
    :=
    \arg\min_{x \in \mathbb{R}^{n}}
        \left(
            \sum_{s=1}^{t-1}
                f_{s}(x_{s}^{\mathrm{T}}
                x
            +
            \frac{1}{\eta}
            R(x)
        \right)
    .
$$

By the first condition of the optimum point,

$$
\begin{eqnarray}
    & &
        \nabla R(x_{t}^{*})
        +
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(x_{s})
        =
        0
    \nonumber
    \\
    & &
        \nabla R(x_{t}^{*})
        =
        -
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(x_{s})
    \label{lemma_05_04_first_order_condition}
        .
\end{eqnarray}
    .
$$

In Lazy OMD,

$$
\begin{eqnarray}
    \nabla R(y_{t})
    & = &
        \nabla R(y_{t - 1})
        -
        \eta \nabla f_{t-1}(x_{t-1})
    \nonumber
    \\
    & = &
        \nabla R(y_{1})
        -
        \sum_{s=1}^{t-1}
            \eta \nabla f_{s}(x_{s})
    \nonumber
    \\
    & = &
        -
        \sum_{s=1}^{t-1}
            \eta \nabla f_{s}(x_{s})
    .
    \nonumber
\end{eqnarray}
$$

Hence $y_{t}$ also satisfies $$\eqref{lemma_05_04_first_order_condition}$$.
However, $R$ is 

$$
\begin{eqnarray}
    B_{R}(x \parallel y_{t})
    & = &
        R(x)
        -
        R(y_{t})
        -
        (\nabla R(y_{t}))^{\mathrm{T}}
        (x - y_{t})
    \nonumber
    \\
    & = &
        R(x)
        -
        R(y_{t})
        +
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(s)^{\mathrm{T}}
        (x - y_{t})
    \nonumber
    \\
    & = &
        R(x)
        +
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(s)^{\mathrm{T}} x
        -
        \left(
            R(y_{t})
            +
            \eta
            \sum_{s=1}^{t-1}
                \nabla f_{s}(s)^{\mathrm{T}} y_{t}
        \right)
    \nonumber
\end{eqnarray}
$$

Since the third term is the independent of $x$,

$$
\begin{eqnarray}
    \arg\min_{x \in \mathcal{K}}
    \left(
        R(x)
        +
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(s)^{\mathrm{T}} x
        -
        \left(
            R(y_{t})
            +
            \eta
            \sum_{s=1}^{t-1}
                \nabla f_{s}(s)^{\mathrm{T}} y_{t}
        \right)
    \right)
    =
    \arg\min_{x \in \mathcal{K}}
    \left(
        R(x)
        +
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(s)^{\mathrm{T}} x
    \right)

\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>
