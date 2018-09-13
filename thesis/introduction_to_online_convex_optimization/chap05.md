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
Since $$x_{1} := \arg\min_{x \in \mathcal{K}}R(x)$$,

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
Since $$x_{T + 2} := \arg\min_{x \in \mathcal{K}} \sum_{t=0}^{T + 1} g(x)$$,

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
    * $y_{1}$ satisfies $\nabla R(y_{1}) = 0$,

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
        \eta \nabla f_{t}(x_{t})
\end{eqnarray}
$$

Rule for Agile OMD

$$
\begin{eqnarray}
    \nabla R(y_{t + 1})
    & = &
        \nabla R(x_{t})
        -
        \eta \nabla f_{t}(x_{t})
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
    * TODO:Is this assumption required?
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

Thus,

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
    & = &
        \arg\min_{x \in \mathcal{K}}
        \left(
            R(x)
            +
            \eta
            \sum_{s=1}^{t-1}
                \nabla f_{s}(s)^{\mathrm{T}} x
        \right)
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## 5.4 Application and special cases

### 5.4.1 Deriving online gradient descent
We can derive the online descent algorithm by taking

$$
    R(x)
    :=
    \frac{1}{2}
    \norm{
        x - x_{0}
    }_{2}^{2}
$$

where $x_{0} \in \mathcal{K}$ which is a parameter of the online gradient descent algorithm.
It's easy to confirm $$\nabla R(x) = x - x_{0}$$.
Moreover, we have

$$
\begin{eqnarray}
    B_{R}(x \parallel y_{t})
    & = &
        \frac{1}{2}
        \norm{x - x_{0}}_{2}^{2}
        -
        \frac{1}{2}
        \norm{y_{t} - x_{0}}_{2}^{2}
        +
        (y_{t} - x_{0})^{\mathrm{T}}
        (x - y_{t})
    \nonumber
    \\
    & = &
        \frac{1}{2}
        \norm{x - y_{t}}_{2}^{2}
    .
    \nonumber
\end{eqnarray}
$$

Thus, the minimizer of $$B_{R}(x \parallel y_{t})$$ is the projection of $y_{t}$ onto $\mathcal{K}$.

In Lazy OMD,

$$
\begin{eqnarray}
    x_{t}
    & = &
        \Pi_{\mathcal{K}}(y_{t})
    \nonumber
    \\
    y_{t}
    & = &
        y_{t - 1}
        -
        \eta
        \nabla f_{t-1}(x_{t-1})
    \nonumber
\end{eqnarray}
$$

In agile OMD,

$$
\begin{eqnarray}
    x_{t}
    & = &
        \Pi_{\mathcal{K}}(y_{t})
    \nonumber
    \\
    y_{t}
    & = &
        x_{t - 1}
        -
        \eta
        \nabla f_{t-1}(x_{t-1})
    .
    \nonumber
\end{eqnarray}
$$

Agile OMD with the above regularization function is identical to the online gradient descnet algorithm.

### 5.4.2 Deriving multiplicative updates
Let

$$
\begin{eqnarray}
    R(x)
    & = &
        \sum_{i=1}^{n}
            x_{i}
            \log x_{i}
    \nonumber
    \\
    \nabla R(x)
    & = &
        \left(
            \begin{array}{c}
                1 + \log x_{1}
                \\
                \vdots 
                \\
                1 + \log x_{n}
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

TODO.

## 5.5 Randomized regularization

### 5.5.1 Perturbation for convex losses

#### Definition
* $N$,
    * $\mathbb{R}^{n}$-valued r.v.
    * $F_{N}$ is c.d.f. of $N$,
* $a \in \mathbb{R}$,
* $\sigma \in \mathbb{R}$,
* $L \in \mathbb{R}$,

$F_{N}$ is said to be $(\sigma_{a}, L_{a})$ stable with respect to the norm $\norm{\cdot}_{a}$ if

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \norm{
            N
        }_{a}^{*}
    \right]
    & = &
        \sigma_{a}
    \nonumber
    \\
    \forall u \in \mathbb{R}^{n},
    \
    \int_{\mathbb{R}^{n}}
        \abs{
            F_{N}(n)
            -
            F_{N}(n - u)
        }
    \ dn
    \nonumber
    \\
    & \le &
        L_{a}
        \norm{u}_{a}^{*}
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

If $N$ is uniformly distribuited on $[0, 1]^{n}$ and norm is Euclidean norm,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \norm{N}_{2}^{2}
    \right]
    & = &
        \mathrm{E}
        \left[
            \max_{\norm{x}_{2} \le 1}
                \langle x, N \rangle
        \right]
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \max_{\norm{x}_{2} \le 1}
               \norm{x}_{2}
               \norm{N}_{2}
        \right]
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
           \norm{N}_{2}
        \right]
    \nonumber
    \\
    & = &
        \int_{[0, 1]^{n}}
            \sqrt{
                \sum_{i=1}^{n}
                    n_{i}^{2}
            }
        \ dn
    & \le &
        \sqrt{n}
\end{eqnarray}
$$

#### Algorithm 13 Follow-the-perturbed-leader for convex 
* $\eta > 0$,
* $N$,
    * r.v.
* $\mathcal{K}$,
* $x_{1} \in \mathcal{K}$,

**Step1.** for $t=1$ to $T$

**Step2.** Predict $x_{t}$

**Step3.** Observe $f_{t} \in \mathcal{F}$ and suffer loss $f_{t}(x_{t})$.

**Step4.** Update

$$
\begin{eqnarray}
    x_{t + 1}
    :=
    \mathrm{E}
    \left[
        \arg\min_{x \in \mathcal{K}}
        \left(
            \eta
            \sum_{s=1}^{t}
                \nabla f_{s}(x_{s})^{\mathrm{T}}
                x
            +
            N^{\mathrm{T}}
            x
        \right)
    \right]
    \label{equation_05_03}
\end{eqnarray}
$$

**Step5.** end for

**Step6.** return $x_{T+1}$

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma
* $\mathcal{K} \subseteq \mathbb{R}^{n}$,
* $g_{t}: \mathcal{K} \times \Omega  \rightarrow \mathbb{R} \ (t=0, \ldots, T)$,
    * funciton valued r.v.
    * convex
* $x_{0} \in \mathcal{K}$,

$$
\begin{eqnarray}
    X_{t + 1}(\omega)
    & := &
        \arg\min_{x \in \mathcal{K}}
            \sum_{s=0}^{t}
                g_{s}(x, \omega)
    \nonumber
    \\
    x_{t + 1}
    & := &
        \mathrm{E}
        \left[
            X_{t + 1}
        \right]
    \nonumber
\end{eqnarray}
$$

Then for all $u \in \mathcal{K}$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=0}^{T}
        g_{t}(u)
    \right]
    & \ge &
        \mathrm{E}
        \left[
            \sum_{t=0}^{T}
            g_{t}(x_{t + 1})
        \right]
    \nonumber
\end{eqnarray}
$$

#### proof
Suppose that $T=1$.
By the definition of $x_{1}$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        g_{0}(u)
        +
        g_{1}(u)
    \right]
    & \ge &
        \mathrm{E}
        \left[
            g_{0}(X_{1})
            +
            g_{1}(X_{1})
        \right]
    \nonumber
    \\
    & \ge &
        \mathrm{E}
        \left[
            g_{0}(X_{1})
            +
            g_{1}(X_{1})
        \right]
\end{eqnarray}
    .
$$

Suppose that the inequality holds up to $T$.

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=0}^{T+1}
        g_{t}(u)
    \right]
    & \ge &
        \mathrm{E}
        \left[
            \sum_{t=0}^{T+1}
            g_{t}(x_{T + 2})
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \sum_{t=0}^{T}
            g_{t}(x_{T + 2})
        \right]
        +
        \mathrm{E}
        \left[
            g_{T+1}(x_{T + 2})
        \right]
    \nonumber
    \\
    & \ge &
        \mathrm{E}
        \left[
            \sum_{t=0}^{T}
            g_{t}(x_{t + 1})
        \right]
        +
        \mathrm{E}
        \left[
            g_{T+1}(x_{T + 2})
        \right]
        \quad
        (\because \text{by assumption of induction})
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \sum_{t=0}^{T+1}
            g_{t}(x_{t + 1})
        \right]
    \nonumber
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 5.6
* $\sigma \in \mathbb{R}$,
* $L \in \mathbb{R}$,
* $N$,
    * $N$ is (\sigma, L)-stable with respect to norm \norm{\cdot}_{a},
* $x_{t}$,
    * $$\eqref{equation_05_03}$$,

In Algorithm 13,

$$
    \mathrm{Regret}_{T}
    \le
    \eta
    D
    (G^{*})^{2}
    LT
    +
    \frac{1}{\eta}
    \sigma D
$$

#### proof
Let

$$
\begin{eqnarray}
    g_{0}(x)
    & := &
        \frac{1}{\eta}
        N_{t}^{\mathrm{T}}
        x
    \nonumber
    \\
    g_{t}(x)
    & := &
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        x
    \nonumber
\end{eqnarray}
    .
$$

We will show that for $T > 0$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=0}^{T}
            g_{t}(u)
    \right]
    \ge
    \mathrm{E}
    \left[
        \sum_{t=0}^{T}
            g_{t}(x_{t + 1})
    \right]
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (x_{t} - u)
    & = &
        \sum_{t=1}^{T}
            g_{t}(x_{t})
        -
        \sum_{t=1}^{T}
            g_{t}(u)
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            g_{t}(x_{t})
        -
        \sum_{t=1}^{T}
            g_{t}(u)
        +
        \sum_{t=0}^{T}
            g_{t}(u)
        -
        \sum_{t=0}^{T}
            g_{t}(x_{t + 1})
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        +
        \frac{1}{\eta}
        N_{0}
        \left(
            u
            -
            x_{1}
        \right)
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        +
        \frac{1}{\eta}
        \norm{N_{0}}^{*}
        \norm{
            u
            -
            x_{1}
        }
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (x_{t} - x_{t + 1})
        +
        \frac{1}{\eta}
        \norm{N_{0}}^{*}
        D
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            f_{t}(x_{t})
        -
        \min_{x \in \mathcal{K}}
            \sum_{t=1}^{T}
                f_{t}(x)
    \right]
    & \le &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                \nabla f_{t}(x_{t})^{\mathrm{T}}
                (x_{t} - u)
        \right]
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                \nabla f_{t}(x_{t})^{\mathrm{T}}
                (x_{t} - x_{t + 1})
            +
            \frac{1}{\eta}
            \norm{N_{0}}^{*}
            D
        \right]
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                \norm{
                    \nabla f_{t}(x_{t})^{\mathrm{T}}
                }^{*}
                \norm{
                    (x_{t} - x_{t + 1})
                }
        \right]
        +
        \frac{1}{\eta}
        \sigma
        D
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \norm{ G }^{*}
            \sum_{t=1}^{T}
                \norm{
                    (x_{t} - x_{t + 1})
                }
        \right]
        +
        \frac{1}{\eta}
        \sigma
        D
\end{eqnarray}
$$

TODO.
$\norm{x_{t} - x_{t+1}} \in O(\eta)$.

$$
    h_{t}(N_{t})
    :=
    \arg\min_{x \in \mathcal{K}}
    \left(
        \eta
        \sum_{s=1}^{t-1}
            \nabla f_{s}(x_{s})^{\mathrm{T}}
            x
        +
        N_{t}^{\mathrm{T}}
        x
    \right)
    .
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \norm{
            x_{t} - x_{t + 1}
        }
    \right]
    & = &
        \mathrm{E}
        \left[
            \norm{
                h_{t}(N_{t})
                -
                h_{t + 1}(N_{t + 1})
            }
        \right]
    \nonumber
    \\
    & \le &
        \norm{
            \mathrm{E}
            \left[
                h_{t}(N_{t})
                -
                h_{t + 1}(N_{t + 1})
            \right]
        }
        \quad
        (\because \text{Jensen's inequality})
    \nonumber
    \\
    & \le &
        \norm{
            \mathrm{E}
            \left[
                h_{t}(N_{t})
                -
                h_{t}(N_{t + 1} + \eta \nabla f_{t}(x_{t}))
            \right]
        }
    \nonumber
    \\
    & \le &
        \norm{
            \int_{\mathbb{R}^{n}}
                h_{t}(s)
                -
                h_{t}(s + \eta \nabla f_{t}(x_{t}))
            \ F_{N}(ds)
        }
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### 5.5.2 Perturbation for linear cost functions
Here we assume cost functions are linear; $f_{t}(x) = g_{t}^{\mathrm{T}}x$.

$$
\begin{eqnarray}
    w_{t}(N)
    :=
    \arg\min_{x \in \mathcal{K}}
    \left(
        \eta
        \sum_{s=1}^{t}
            g_{s}^{\mathrm{T}}
            x
        +
        N^{\mathrm{T}}x
    \right)
    \nonumber
    .
\end{eqnarray}
$$

By linearity of the expectation,

$$
    f_{t}(x_{t})
    =
    f_{t}
    \left(
        \mathrm{E}
        \left[
            w_{t}(N)
        \right]
    \right)
    =
    \mathrm{E}
    \left[
        f_{t}
        \left(
            w_{t}(N)
        \right)
    \right]
    .
$$

#### ALgorithm 14 FPL for linear losses
* $\eta > 0$,
* $N$,
* $N_{0}$,
    * sample of $N$
$$
    \hat{x}_{1}
    :=
    \arg\min_{x \in \mathcal{K}}
        -N_{0}^{\mathrm{T}}
        x
    .
$$

Step1. for $t=1$ to $T$ do

Step2. Predict $\hat{x}_{t}$

Step3. Observer the loss function $f_{t}$ and suffer loss $f_{t}(x_{t})$

Step4. Update

$$
\begin{eqnarray}
    \hat{x}_{t + 1}
    :=
    \arg\min_{x \in \mathcal{K}}
    \eta
    \sum_{s=1}^{t-1}
        f_{s}(x_{s})^{\mathrm{T}}
        x
    +
    N_{0}^{\mathrm{T}}
    x
\end{eqnarray}
$$

Step5. end for

Step6. Return $\hat{x}_{T + 1}$.

<div class="end-of-statement" style="text-align: right">■</div>


#### Corolary 5.7


#### proof

<div class="QED" style="text-align: right">$\Box$</div>

### 5.5.3 Foolow-the-perturbed-leader for expert advice

$$
\begin{eqnarray}
    \mathcal{F}
    :=
    \left\{
        f(x)
        :=
            g^{\mathrm{T}}x
        \mid
        g \in [0, 1]^{n}
    \right\}
    \label{definition_cost_function_algorithm_15}
\end{eqnarray}
    .
$$

#### Algorithm 15 FPL for prediction from expert advice
* $\eta > 0$,
* $N_{0}$,
    * real valued r.v. whose p.d.f. is p.d.f. of exponential distribution $e^{-\eta x}$,

$$
    x_{1}
    :=
    \arg\min_{x \in \Delta_{n}}
        -N_{0}^{\mathrm{T}}
        x
    .
$$

Step1. for $t=1$ to $T$

Step2. Predict using expert $i_{t} := \arg\max_{i} x_{i}$. See Remark below.

Step3. Observe the loss $f_{t} \in \mathcal{F}$ and sufer loss $f_{t}(\hat{x}_{t})$

Draw sample independent sample from $N_{t} \sim e^{-\eta x}$,

Step4. Update

$$
\begin{eqnarray}
    \hat{x}_{t + 1}
    & := &
        \arg\min_{x \in \Delta_{n}}
        \left(
            \sum_{s=1}^{t}
                f_{s}(x)
                -
                N_{t}^{\mathrm{T}}
                x
        \right)
    \nonumber
    \\
    & = &
        \arg\min_{x \in \Delta_{n}}
        \left(
            \sum_{s=1}^{t}
                g_{s}^{\mathrm{T}}
                x
                -
                N_{t}^{\mathrm{T}}
                x
        \right)
    \nonumber
\end{eqnarray}
$$

Step5. end for

Step6. Return $\hat{x}_{T +1}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
* $y \in [0, 1]^{n}$,

$$
\begin{eqnarray}
    & &
        j
        =
        \arg\min_{i = \{1, \ldots, n\}}
            y_{i}
    \nonumber
    \\
    & \Leftrightarrow &
        x
        =
        \arg\min_{x \in \Delta_{n}}
            y^{\mathrm{T}}
            x,
        \
        x_{j} = 1
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem 5.8

$$
    (1 - \eta)
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            g_{t}^{\mathrm{T}}
            \hat{x}_{t}
    \right]
    \le
    \min_{x^{*} \in \Delta_{n}}
        \sum_{t=1}^{T}
            g_{t}^{\mathrm{T}}
            x^{*}
    +
    \frac{
        4 \log n
    }{
        \eta
    }
    .
$$

#### proof
Let $g_{0} := -N$.
We will show that

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=0}^{T}
            g_{t}^{\mathrm{T}}
            u
    \right]
    \ge
    \mathrm{E}
    \left[
        \sum_{t=0}^{T}
            g_{t}^{\mathrm{T}}
            \hat{x}_{t + 1}
    \right]
    \label{theorem_05_08_inequality_g}
    .
\end{eqnarray}
$$

In case of $T = 0$, by definition of $x_{1}$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        -N_{0}^{\mathrm{T}}
        u
    \right]
    \ge
    \mathrm{E}
    \left[
        -N_{0}^{\mathrm{T}}
        x_{1}
    \right]
    .
    \nonumber
\end{eqnarray}
$$

In case of $T = 1$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        -N_{0}^{\mathrm{T}}
        u
        +
        g_{1}^{\mathrm{T}}
        u
    \right]
    & \ge &
        \mathrm{E}
        \left[
            -N_{0}^{\mathrm{T}}
            x_{2}
            +
            g_{1}^{\mathrm{T}}
            x_{2}
        \right]
        \quad
        (\because \text{by definition of }x_{2})
    \nonumber
    \\
    & \ge &
        \mathrm{E}
        \left[
            -N_{0}^{\mathrm{T}}
            x_{1}
            +
            g_{1}^{\mathrm{T}}
            x_{2}
        \right]
        \quad
        (\because \text{by definition of }x_{1})
    \nonumber
\end{eqnarray}
$$

Now, suppose that the equation holds up to $T - 1$.

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        -N_{0}^{\mathrm{T}}
        u
        +
        \sum_{s=1}^{T}
            g_{s}^{\mathrm{T}}
            u
    \right]
    & = &
        \mathrm{E}
        \left[
            -N_{T}^{\mathrm{T}}
            u
            +
            \sum_{s=1}^{T}
                g_{s}^{\mathrm{T}}
                u
        \right]
        \quad
        (\because \text{i.i.d.})
    \nonumber
    \\
    & \ge &
        \mathrm{E}
        \left[
            -N_{T}^{\mathrm{T}}
            x_{T + 1}
            +
            \sum_{s=1}^{T}
                g_{s}^{\mathrm{T}}
                x_{T + 1}
        \right]
        \quad
        (\because \text{by definition of }x_{T + 1})
    \nonumber
    \\
    & \ge &
        \mathrm{E}
        \left[
            -N_{T}^{\mathrm{T}}
            x_{1}
            +
            \sum_{s=1}^{T-1}
                g_{s}^{\mathrm{T}}
                x_{s + 1}
            +
            g_{T}^{\mathrm{T}}
            x_{T + 1}
        \right]
        \quad
        (\because \text{by assumption of indection})
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            -N_{0}^{\mathrm{T}}
            x_{1}
            +
            \sum_{s=1}^{T}
                g_{s}^{\mathrm{T}}
                x_{s + 1}
        \right]
        \quad
        (\because \text{i.i.d.})
    .
    \nonumber
\end{eqnarray}
$$

This proves $$\eqref{theorem_05_08_inequality_g}$$.

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            g_{t}^{\mathrm{T}}
            (\hat{x}_{t} - u)
    \right]
    & \le &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                g_{t}^{\mathrm{T}}
                (\hat{x}_{t} - u)
        \right]
        +
        \mathrm{E}
        \left[
            \sum_{t=0}^{T}
                g_{t}^{\mathrm{T}}
                (u - \hat{x}_{t+1})
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                g_{t}^{\mathrm{T}}
                (\hat{x}_{t} - \hat{x}_{t + 1})
        \right]
        +
        \mathrm{E}
        \left[
            g_{0}^{\mathrm{T}}
            (u - x_{1})
        \right]
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                g_{t}^{\mathrm{T}}
                (\hat{x}_{t} - \hat{x}_{t + 1})
        \right]
        +
        \mathrm{E}
        \left[
            \norm{g_{0}}_{\infty}
            \norm{u - x_{1}}_{1}
        \right]
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \norm{g_{t}}_{\infty}
            \norm{
                \hat{x}_{t} - \hat{x}_{t + 1}
            }_{1}
        \right]
        +
        \frac{1}{\eta}
        \mathrm{E}
        \left[
            \norm{u - x_{1}}_{1}
        \right]
        \quad
        (\because \text{Hölder's inequality and lemma below})
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \norm{g_{t}}_{\infty}
            \norm{
                \hat{x}_{t} - \hat{x}_{t + 1}
            }_{1}
        \right]
        +
        \frac{2}{\eta}
        \quad
        (\because u, x_{1} \in \Delta_{n})
    \nonumber
    \\
    & \le &
        \mathrm{E}
        \left[
            \norm{
                \hat{x}_{t} - \hat{x}_{t + 1}
            }_{1}
        \right]
        +
        \frac{2}{\eta}
        \mathrm{E}
        \quad
        (\because \eqref{definition_cost_function_algorithm_15})
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \norm{
                \hat{x}_{t} - \hat{x}_{t + 1}
            }_{1}
            1_{\{x_{i} \neq x_{t + 1, i}, \forall i\}}
        \right]
        +
        \frac{2}{\eta}
        \mathrm{E}
    \nonumber
    \\
    & = &
        2
        \mathrm{E}
        \left[
            1_{\{x_{i} \neq x_{t + 1, i}, \forall i\}}
        \right]
        +
        \frac{2}{\eta}
        \mathrm{E}
\end{eqnarray}
$$

The last inequality follows by the fact that only one element of $x_{t}$ has value 1, that is,

$$
    \forall \omega \in \Omega,
    \
    i_{t}(\omega) \in \{1, \ldots, n\},
    \
    x_{t, i_{t}(\omega)}(\omega)
    =
    1,
    \
    x_{t, j}(\omega)
    =
    0
    \quad
    (j \neq i_{t}(\omega))
    ,
$$

see Remark above.

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma

* $Q_{i}$,
    * $\mathbb{R}$-valued r.v. following exponential distribution with $\eta$,
    * $P(Q_{i} \le x) = 1 - e^{-\eta x}$,
* $Q := (Q_{1}, \ldots, Q_{n})$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sup_{i}
            \abs{A_{i}}
    \right]
    \le
    \frac{
        2 \log n
    }{
        \eta
    }
    .
\end{eqnarray}
$$

#### proof

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sup_{i \in \{1, \ldots, n\}}
            \abs{Q_{i}}
    \right]
    & \le &
        \sup_{i \in \{1, \ldots, n\}}
        \abs{
            \mathrm{E}
            \left[
                Q_{i}
            \right]
        }
    \nonumber
    \\
    & = &
        \sup_{i \in \{1, \ldots, n\}}
        \abs{
            \frac{1}{\eta}
        }
    \nonumber
    \\
    & = &
        \frac{1}{\eta}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## 5.6 Optimal regularization

$$
\begin{eqnarray}
    \mathrm{Regret}_{T}
    \le
    \max_{u \in \mathcal{K}}
    \sqrt{
        2
        \sum_{t=1}^{T}
        (\norm{\nabla f_{t}(x_{t})}_{z}^{*})^{2}
        B_{R}(u \parallel x_{1})
    }
    .
\end{eqnarray}
$$


$$
\begin{eqnarray}
    \mathcal{H}
    & := &
        \{
            A \in \mathbb{R}^{n \times n}
            \mid
            \mathrm{tr}
            \left(
                A
            \right)
            \le
            1,
            0
            \preccurlyeq
            A
        \}
    \nonumber
    \\
    \mathcal{R}
    & := &
        \{
            R:\mathcal{K} \rightarrow \mathbb{R}^{n}
            \mid
            \nabla^{2} R(x) \in \mathcal{H},
            \
            x \in \mathcal{K}
        \}
    \nonumber
\end{eqnarray}
$$

#### Algorithm 16 AdaGrad
* $\eta > 0$,
* $x_{1} \in \mathcal{K}$,


Step1. For $t=1$ to $T$

Step2. Play $x_{t}$

Step3. Suffer loss $f_{t}(x_{t})$,

Step4.

$$
\begin{eqnarray}
    S_{t}
    & := &
        S_{t - 1}
        +
        \nabla f_{t}(x_{t})
        \nabla f_{t}(x_{t})^{\mathrm{T}},
    \nonumber
    \\
    G_{t}
    & := &
        S_{t}^{1/2}
    \nonumber
    \\
    y_{t + 1}
    & := &
        x_{t}
        -
        \eta
        G_{t}^{\dagger}
        \nabla f(x_{t})
    \nonumber
    \\
    x_{t + 1}
    & := &
        \arg\min_{x \in \mathcal{K}}
        \norm{
            y_{t + 1}
            -
            x
        }_{G_{t}}^{2}
    \nonumber
\end{eqnarray}
$$

Step5. end for

Step6. Return $x_{T + 1}$.

<div class="end-of-statement" style="text-align: right">■</div>

In the algorithm definition and throughout this section, the notation $A^{\dagger}$ refers to the Moore-Penrose pseudoinverse of the matrix $A$.
The regret of AdaGrad is at most a  constant factor larger than the minimum regret of all RFTL algorithm with regularizatin functions whose Hesssian is fixed and belongs to the class $\mathcal{H}$.

#### Remark

$$
\begin{eqnarray}
    (G_{t})^{\mathrm{T}}
    & = &
        G_{t}
    \nonumber
    \\
    (G_{t}^{\dagger})^{\mathrm{T}}
    & = &
        (G_{t}^{\dagger})
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem 5.9
* $x_{1} \in \mathcal{K}$,
* $\eta := D$,

$$
    D
    :=
    \max_{u \in \mathcal{K}}
    \norm{
        u - x_{1}
    }
    .
$$

In algorithm 16,

$$
\begin{eqnarray}
    \mathrm{Regret}_{T}
    \le
    2 D
    \sqrt{
        \min_{H \in \mathcal{H}}
            \sum_{t=1}^{T}
                \left(
                    \norm{
                        \nabla f_{t}(x_{t})
                    }_{H}^{*}
                \right)^{2}
    }
    \label{equation_05_06}
\end{eqnarray}
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 5.1

The minimizer of the following minimization problem:
* $A$,

$$
\begin{align}
    \max_{Y}
    & & &
        \mathrm{tr}
        \left(
            Y^{\dagger}
            A
        \right)
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        Y \in \mathcal{H}
    \nonumber
\end{align}
$$

is

$$
\begin{eqnarray}
    Y^{*}
    & = &
        \frac{1}{ \mathrm{tr}(A^{1/2})}
        A^{1/2}
    \nonumber
    \\
    (Y^{*})^{\dagger}
    A
    & = &
        ( \mathrm{tr}(A^{1/2})) )^{2}
    \nonumber
\end{eqnarray}
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary 5.10

$$
\begin{eqnarray}
    \sqrt{
        \min_{H \in \mathcal{H}}
            \sum_{t=1}^{T}
                \left(
                    \norm{
                        \nabla f_{t}(x_{t})
                    }_{H}^{*}
                \right)^{2}
    }
    & = &
        \sqrt{
            \min_{H \in \mathcal{H}}
                \mathrm{tr}
                \left(
                    H^{\dagger}
                    \left(
                        \sum_{t=1}^{T}
                            \nabla f_{t}(x_{t})
                            \nabla f_{t}(x_{t})^{\mathrm{T}}
                    \right)
                \right)
        }
    \nonumber
    \\
    & = &
        \mathrm{tr}
        \left(
            \left(
                \sum_{t=1}^{T}
                    \nabla f_{t}(x_{t})
                    \nabla f_{t}(x_{t})^{\mathrm{T}}
            \right)^{1/2}
        \right)
    \nonumber
    \\
    & = &
        \mathrm{tr}(G_{T})
    \nonumber
\end{eqnarray}
$$

#### proof


<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 5.11
In Algorithm 16,

$$
\begin{eqnarray}
    \mathrm{Regret}_{T}
    & \le &
        2D
        \mathrm{tr}(G_{T})
    \nonumber
    \\
    & = &
        2 D
        \sqrt{
            \min_{H \in \mathcal{H}}
                \sum_{t=1}^{T}
                    \left(
                        \norm{
                            \nabla f_{t}(x_{t})
                        }_{H}^{*}
                    \right)^{2}
        }
    \nonumber
\end{eqnarray}
$$

#### proof
By the definiton of $y_{t + 1}$,

$$
\begin{eqnarray}
    & &
        y_{t + 1} - u
        =
        x_{t} - u
        -
        \eta G_{t}^{\dagger}\nabla f_{t}(x_{t})
    \label{equation_05_07}
    \\
    & \Leftrightarrow &
        G_{t}(y_{t + 1} - u)
        =
        G_{t}
        (x_{t} - u)
        -
        \eta \nabla f_{t}(x_{t})
    \label{equation_05_08}
\end{eqnarray}
$$

Multiplying the transpose of $$\eqref{equation_05_07}$$ by $$\eqref{equation_05_08}$$,

$$
\begin{eqnarray}
    (y_{t + 1} - u)^{\mathrm{T}}
    G_{t}(y_{t + 1} - u)
    & = &
        (x_{t} - u)^{\mathrm{T}}
        G_{t}
        (x_{t} - u)
        -
        \eta 
        (x_{t} - u)^{\mathrm{T}}
        \nabla f_{t}(x_{t})
        -
        \eta
        (G_{t}^{\dagger}\nabla f_{t}(x_{t})) ^{\mathrm{T}}
        G_{t}
        (x_{t} - u)
        +
        \eta
        (G_{t}^{\dagger}\nabla f_{t}(x_{t})) ^{\mathrm{T}}
        \eta \nabla f_{t}(x_{t})
    \nonumber
    \\
    & = &
        (x_{t} - u)^{\mathrm{T}}
        G_{t}
        (x_{t} - u)
        -
        2\eta 
        (x_{t} - u)^{\mathrm{T}}
        \nabla f_{t}(x_{t})
        +
        \eta^{2}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (G_{t}^{\dagger})
        \nabla f_{t}(x_{t})
    \label{equation_05_09}
\end{eqnarray}
$$

Since $x_{t + 1}$ is the projection of $y_{t + 1}$, by theorem 2.1

$$
\begin{eqnarray}
    (y_{t + 1} - u)^{\mathrm{T}}
    G_{t}
    (y_{t + 1} - u)
    & = &
        \norm{
            y_{t+1}
            -
            u
        }_{G_{t}}^{2}
    \nonumber
    \\
    & \ge &
        \norm{
            x_{t + 1} - u
        }_{G_{t}}^{2}
    \nonumber
\end{eqnarray}
$$

From $$\eqref{equation_05_09}$$,


$$
\begin{eqnarray}
    & &
        \norm{
            x_{t + 1} - u
        }_{G_{t}}^{2}
        \le
        \norm{
            x_{t} - u
        }_{G_{t}}^{2}
        -
        2\eta
        (x_{t} - u)^{\mathrm{T}}
        \nabla f_{t}(x_{t})
        +
        \frac{\eta}{2}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (G_{t}^{\dagger})
        \nabla f_{t}(x_{t})
    \nonumber
    \\
    & \Leftrightarrow &
        2\eta
        (x_{t} - u)^{\mathrm{T}}
        \nabla f_{t}(x_{t})
        \le
        \norm{
            x_{t} - u
        }_{G_{t}}^{2}
        -
        \norm{
            x_{t + 1} - u
        }_{G_{t}}^{2}
        +
        \frac{\eta}{2}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (G_{t}^{\dagger})
        \nabla f_{t}(x_{t})
    \nonumber
    \\
    & \Leftrightarrow &
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (x_{t} - u)
        \le
        \frac{1}{2\eta}
        \left(
            \norm{
                x_{t} - u
            }_{G_{t}}^{2}
            -
            \norm{
                x_{t + 1} - u
            }_{G_{t}}^{2}
        \right)
        +
        \frac{\eta}{2}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (G_{t}^{\dagger})
        \nabla f_{t}(x_{t})
    .
    \nonumber
\end{eqnarray}
$$

Now, summing up over $t=1$ to $T$ we get

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        \nabla f_{t}(x_{t})^{\mathrm{T}}
        (x_{t} - u)
    & \le &
        \sum_{t=1}^{T}
            \frac{1}{2\eta}
            \norm{
                x_{t} - u
            }_{G_{t}}^{2}
        -
        \sum_{t=1}^{T}
            \frac{1}{2\eta}
            \left(
                \norm{
                    x_{t + 1} - u
                }_{G_{t}}^{2}
            \right)
        +
        \sum_{t=1}^{T}
            \frac{\eta}{2}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (G_{t}^{\dagger})
            \nabla f_{t}(x_{t})
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \frac{1}{2\eta}
            \norm{
                x_{t} - u
            }_{G_{t}}^{2}
        -
        \sum_{t=1}^{T+1}
            \frac{1}{2\eta}
            \left(
                \norm{
                    x_{t} - u
                }_{G_{t-1}}^{2}
            \right)
        +
        \frac{1}{2\eta}
        \norm{
            x_{1} - u
        }_{G_{0}}^{2}
        +
        \sum_{t=1}^{T}
            \frac{\eta}{2}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (G_{t}^{\dagger})
            \nabla f_{t}(x_{t})
    \nonumber
    \\
    & = &
        \sum_{t=1}^{T}
            \frac{1}{2\eta}
            \left(
                \norm{
                    x_{t} - u
                }_{G_{t}}^{2}
                -
                \norm{
                    x_{t} - u
                }_{G_{t-1}}^{2}
            \right)
        +
        \frac{1}{2\eta}
        \norm{
            x_{1} - u
        }_{G_{0}}^{2}
        -
        \frac{1}{2\eta}
        \norm{
            x_{T + 1} - u
        }_{G_{T}}^{2}
        +
        \sum_{t=1}^{T}
            \frac{\eta}{2}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (G_{t}^{\dagger})
            \nabla f_{t}(x_{t})
    \nonumber
    \\
    & = &
        \frac{1}{2\eta}
        \sum_{t=1}^{T}
            (x_{t} - u)^{\mathrm{T}}
            (G_{t} - G_{t - 1})
            (x_{t} - u)
        -
        \frac{1}{2\eta}
        \norm{
            x_{T + 1} - u
        }_{G_{T}}^{2}
        +
        \sum_{t=1}^{T}
            \frac{\eta}{2}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (G_{t}^{\dagger})
            \nabla f_{t}(x_{t})
        \quad
        (\because G_{0} = 0)
    \nonumber
    \\
    & = &
        \frac{1}{2\eta}
        \sum_{t=1}^{T}
            (x_{t} - u)^{\mathrm{T}}
            (G_{t} - G_{t - 1})
            (x_{t} - u)
        +
        \sum_{t=1}^{T}
            \frac{\eta}{2}
            \nabla f_{t}(x_{t})^{\mathrm{T}}
            (G_{t}^{\dagger})
            \nabla f_{t}(x_{t})
    \label{equation_05_10}
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 5.12

#### proof



