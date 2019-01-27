---
title: Display advertising online optimization
---

$$
    \newcommand{\CVR}{\mathop{\rm CVR}\nolimits}
    \newcommand{\CTR}{\mathop{\rm CTR}\nolimits}
$$

## Display advertising online optimization

### Naive formulation
In this formulation, we assume that the clicks and conversions of ad are observed imediately after the player chooses the advertisement.

* $T \in \mathbb{N}$,
    * the number of total impressions
* $N \in \mathbb{N}$,
    * the number of advertisements/campaigns
* $$\mathcal{A} := \{1, \ldots, N\}$$,
    * a set of ads
* $M \in \mathbb{N}$,
    * the number of displays
* $$\mathcal{D} := \{1, \ldots, M\}$$,
    * a set of displays
* $\mathcal{K} \subseteq \mathbb{R}^{N}$,
    * a set of a choice of advertisements
    * $\mathcal{K} = \Delta_{N}$ if ad is probablistically chosen
        * where $\Delta_{N}$ is $N$-simplex
* $x^{t} \in \mathcal{K}$,
    * the player's choice at $t$,
* $\mathcal{Y}$,
    * occurences of clicks
    * 1 means clicked
* $\mathcal{Z}$,
    * occurences of conversions
    * 1 means conversion is observed

$$
    \mathcal{Z}
    :=
    \mathcal{Y}
    :=
    \{
        y \in \{0, 1\}^{N}
        \mid
        \sum_{a=1}^{N}
            y_{a}
        =
        1
    \},
$$

#### advertisement selection procedure
* $$\mathrm{Imp}_{d, a}^{1} \in \mathbb{Z}_{\ge 0} \ (d \in \mathcal{D}, \ a \in \mathcal{A})$$,
    * the number of impressions for ad $a$ of banner display $d$ at the begining
* $$\mathrm{Clk}_{d, a}^{1}  \in \mathbb{Z}_{\ge 0} \ (d \in \mathcal{D}, \ a \in \mathcal{A})$$,
    * the number of clicks for ad $a$ of banner display $d$ at the begining
* $$\mathrm{Cvr}_{d, a}^{1}  \in \mathbb{Z}_{\ge 0}  \ (d \in \mathcal{D}, \ a \in \mathcal{A})$$,
    * the number of conversions for ad $a$ of banner display $d$ at the begining
* $$\mathrm{tCPA}_{a}  \in \mathbb{R} \ (a \in \mathcal{A})$$,
    * target CPA for ad $a$,
    * given by advertiser/trading desk
* $$B_{a} \in \mathbb{R}_{\ge 0} \ (a \in \mathcal{A})$$,
    * budget for ad $a$,
    * given by advertiser
* $$\mathrm{tCvr}_{a}  \in \mathbb{R} \ (a \in \mathcal{A})$$,
    * the number of target conversions for ad $a$
    * determined by corresponding budget and target CPA


$$
    \mathrm{tCvr}_{a}
    :=
    \frac{
        B_{a}
    }{
        \mathrm{tCPA}_{a}
    }
    .
$$

**Step0.** Initialize parameters

$$
\begin{eqnarray}
    \CTR
    \left(
        \mathrm{Imp},
        \mathrm{Clk}
    \right)
    & := &
        \frac{
            \mathrm{Clk}
        }{
            \mathrm{Imp}
        },
    \nonumber
    \\
    \CVR
    \left(
        \mathrm{Clk},
        \mathrm{Cvr}
    \right)
    & := &
        \frac{
            \mathrm{Cvr}
        }{
            \mathrm{Clk}
        },
    \nonumber
    \\
    \mathrm{CPC}_{d, a}^{1}
    & := &
        \mathrm{tCPA_{a}}
        \times
        \CVR
        \left(
            \mathrm{Clk}_{d, a}^{1},
            \mathrm{Cvr}_{d, a}^{1}
        \right)
    \nonumber
    \\
    \mathrm{CPA}_{d, a}^{1}
    & := &
        \begin{cases}
            \frac{
                \mathrm{CPC}_{d, a}^{1}
                \times
                \mathrm{Clk}_{d, a}^{1}
            }{
                \mathrm{Cvr}_{d, a}^{1}
            }
            =
            \mathrm{tCPA_{a}}
            &
                (\mathrm{Cvr} \neq 0)
            \\
            0
            &
                (\mathrm{Cvr} = 0)
        \end{cases}
    \nonumber
\end{eqnarray}
$$

**Step1.** For $t = 1, \ldots, T$,

**Step2.** Choose an advertisement $a^{t} \in \mathcal{A}$ based on a choice $x^{t} \in \mathcal{K}$ for an impression $t$. The advertisement $a^{t}$ must satisify the following conditions for CPA and budget.

$$
\begin{eqnarray}
    \sum_{d=1}^{M}
        \mathrm{CPA}_{a}^{t}
    & \le &
        \mathrm{tCPA}_{a}
    \nonumber
    \\
    \sum_{s=1}^{t}
    \sum_{d=1}^{M}
        \mathrm{Cvr}_{d, a}^{s}
        \mathrm{CPA}_{d, a}^{s}
    & \le &
        B_{a}
\end{eqnarray}
    .
$$

**Step3.** Observe click event $y^{t} \in \mathcal{Y}$, conversion event $z^{t} \in \mathcal{Z}$, and display $d^{t} \in \mathcal{D}$

**Step4.** Update parameters based on the observations

$$
\begin{eqnarray}
    \mathrm{Imp}_{d^{t}, a}^{t+1}
    & := &
        \mathrm{Imp}_{d^{t}, a}^{t}
        +
        1
    \nonumber
    \\
    \mathrm{Clk}_{d^{t}, a}^{t+1}
    & := &
        \mathrm{Clk}_{d^{t}, a}^{t}
        +
        y_{a}^{t}
    \nonumber
    \\
    \mathrm{Cvr}_{d^{t}, a}^{t+1}
    & := &
        \mathrm{Cvr}_{d^{t}, a}^{t}
        +
        z_{a}^{t}
    \nonumber
    \\
    \mathrm{CPA}_{d^{t}, a}^{t+1}
    & := &
        \frac{
            \sum_{s=1}^{t}
                \mathrm{CPC}_{d^{s}, a}^{s}
                \times
                y_{d^{s}, a}^{s}
        }{
            \mathrm{Cvr}_{d^{t}, a}^{t+1}
        }
    \nonumber
    \\
    \mathrm{CPC}_{d, a}^{t+1}
    & := &
        \mathrm{tCPA_{a}}
        \times
        \CVR
        \left(
            \mathrm{Clk}_{d, a}^{t},
            \mathrm{Cvr}_{d, a}^{t}
        \right)
\end{eqnarray}
$$

**Step5.** Back to Step2 until $t = T$,

Our objective is to maximize the revenue


$$
    \sum_{t=1}^{T}
    \sum_{d=1}^{M}
    \sum_{a=1}^{N}
        \mathrm{CPC}_{d, a}^{t}
        y_{d, a}^{t}
$$


<div class="end-of-statement" style="text-align: right">■</div>

Additional problems

1. Observations of click events and conversion events in Step3 are usually delayed for certain period, so Step3 and Step4 may be skipped in some iterations.
1. Suggesting the same advertisement in subsequent impressions (i.e. $a^{t} = a^{t+1}$) may reduce customer satisfaction
1. Budget pacing
1. Choice of creatives

### Miscellaneous equalities

$$
\begin{eqnarray}
    \bar{y}_{d, a}^{t}
    & := &
        \sum_{s=1}^{t}
            y_{d, a}^{t}
    \nonumber
    \\
    \bar{z}_{d, a}^{t}
    & := &
        \sum_{s=1}^{t}
            z_{d, a}^{t}
    \nonumber
\end{eqnarray}
    .
$$

$$
\begin{eqnarray}
    \mathrm{Clk}_{d, a}(y_{d, a}^{1:t})
    & := &
        \mathrm{Clk}_{d, a}^{t+1}
    \nonumber
    \\
    & := &
        \mathrm{Clk}_{d, a}^{1}
        +
        \sum_{s=1}^{t}
            y_{d, a}^{s}
    \nonumber
    \\
    & = &
        \mathrm{Clk}_{d, a}^{1}
        +
        \bar{y}_{d, a}^{s}
    \nonumber
    \\
    \mathrm{Cvr}_{d, a}(z_{d, a}^{1:t})
    & := &
        \mathrm{Cvr}_{d, a}^{t+1}
    \nonumber
    \\
    & := &
        \mathrm{Cvr}_{d, a}^{1}
        +
        \sum_{s=1}^{t}
            z_{d, a}^{s}
    \nonumber
    \\
    & = &
        \mathrm{Cvr}_{d, a}^{1}
        +
        \bar{z}_{d, a}^{s}
    \nonumber
    \\
    \mathrm{CPA}_{d, a}(y_{d, a}^{1:t}, z_{d, a}^{1:t})
    & := &
        \mathrm{CPA}_{d, a}^{t + 1}
    \nonumber
    \\
    & := &
        \frac{
            \sum_{s=1}^{t}
                \mathrm{CPC}_{d, a}^{s}
                y_{d, a}^{s}
        }{
            \mathrm{Cvr}_{d, a}^{t+1}
        }
    \nonumber
    \\
    & = &
        \frac{
            \mathrm{CPC}_{d, a}^{1}
            y_{d, a}^{1}
            +
            \sum_{s=2}^{t}
                y_{d, a}^{s}
                \mathrm{tCPA}_{a}
                \left(
                    \mathrm{Cvr}_{d,a}^{1}
                    +
                    \sum_{r=1}^{s}
                        z_{d, a}^{r}
                \right)
        }{
            \mathrm{Cvr}_{d,a}^{1}
            +
            \sum_{s=1}^{t}
                z_{d, a}^{s}
        }
    \nonumber
    \\
    & = &
        \frac{
            \sum_{s=1}^{t}
                \mathrm{CPC}_{d, a}^{s}
                \left(
                    \bar{y}_{d, a}^{s}
                    -
                    \bar{y}_{d, a}^{s - 1}
                \right)
        }{
            \mathrm{Cvr}_{d, a}^{t+1}
        }
    \nonumber
    \\
    & = &
        \frac{
            \mathrm{CPC}_{d, a}^{1}
            \left(
                \bar{y}_{d, a}^{1}
                -
                \bar{y}_{d, a}^{0}
            \right)
            +
            \sum_{s=2}^{t}
                \left(
                    \bar{y}_{d, a}^{s}
                    -
                    \bar{y}_{d, a}^{s-1}
                \right)
                \mathrm{tCPA}_{a}
                \left(
                    \mathrm{Cvr}_{d,a}^{1}
                    +
                    \bar{z}_{d, a}^{s}
                \right)
        }{
            \mathrm{Cvr}_{d,a}^{1}
            +
            \bar{z}_{d, a}^{t}
        }
    \nonumber
    \\
    \mathrm{CPC}_{d, a}(y_{d, a}^{1:t}, z_{d, a}^{1:t})
    & := &
        \mathrm{CPC}_{d, a}^{t + 1}
    \nonumber
    \\
    & := &
        \mathrm{tCPA}_{a}
        \frac{
            \mathrm{Clk}_{d, a}^{t}
        }{
            \mathrm{Cvr}_{d, a}^{t}
        }
    \nonumber
    \\
    & = &
        \frac{
            \mathrm{tCPA}_{a}
            \left(
                \mathrm{Cvr}_{d,a}^{1}
                +
                \sum_{s=1}^{t}
                    z_{d, a}^{s}
            \right)
        }{
            \mathrm{Clk}_{d,a}^{1}
            +
            \sum_{s=1}^{t}
                y_{d, a}^{s}
        }
    \nonumber
    \\
    & = &
        \frac{
            \mathrm{tCPA}_{a}
            \left(
                \mathrm{Cvr}_{d,a}^{1}
                +
                \bar{z}_{d, a}^{t}
            \right)
        }{
            \mathrm{Clk}_{d,a}^{1}
            +
            \bar{y}_{d, a}^{t}
        }
\end{eqnarray}
$$

$$
\begin{eqnarray}
    f^{t}(x; y, z, CPC, d)
    & := &
        -
        \mathrm{CPC}_{d_{t}, I_{t}}(y_{d_{t}, I_{t}}^{1:(t-1)}, z_{d_{t}, I_{t}}^{1:(t-1)})
        (1 - y_{d_{t}, I_{t}})
    \nonumber
    \\
    & = &
        -
        \mathrm{CPC}_{d_{t}, I_{t}}^{t}
        (1 - y_{d_{t}, I_{t}})
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    g_{a}^{t}(x; y, z, CPC, d)
    & := &
        \sum_{d=1}^{M}
            \mathrm{CPA}_{d, a}(y_{d, a}^{1:(t-1)}, z_{d, a}^{1:(t-1)})
        -
        \mathrm{tCPA}_{a}
    \nonumber
    \\
    & = &
        \sum_{d=1}^{M}
            \mathrm{CPA}_{d, a}^{t}
        -
        \mathrm{tCPA}_{a}
    \nonumber
    \\
    h_{a}^{t}(x; y^{1:t}, z^{1:t}, CPC, d)
    & := &
        \sum_{s=1}^{t}
        \sum_{d=1}^{M}
            \mathrm{Cvr}_{d, a}(y_{d, a}^{1:(s-1)})
            \mathrm{CPA}_{d, a}(y_{d, a}^{1:(s-1)}, z_{d, a}^{1:(s-1)})
        -
        B_{a}
    \nonumber
    \\
    & := &
        \sum_{s=1}^{t}
        \sum_{d=1}^{M}
            \mathrm{Cvr}_{d, a}^{s}
            \mathrm{CPA}_{d, a}^{s}
        -
        B_{a}
    \nonumber
\end{eqnarray}
    .
$$

### Formulation in terms of online convex optimization with stochastic constraints
* $$(\Omega, \mathcal{F}, P, \{\mathcal{F}_{t}\}_{t \in \mathbb{N}})$$,
    * probability space with filtration
* $T \in \mathbb{N}$,
    * the number of impressions or recommendations
* $N \in \mathbb{N}$,
    * the number of ads
* $M \in \mathbb{N}$,
    * the number of displays
* $(Y_{d, a}^{s})_{s \in [0:T]} \ (d \in [1:M], a \in [1:N])$,
    * the number of clicks of advertimesement $a$ at display $d$,
    * $Y_{d, a}^{0}$ is an initial value
    * $Y_{d, a}^{s} \in \mathbb{Z}_{\ge 0}$ is an initial value
    * adapted process
    * $$Y_{d, a}^{s}: \Omega \rightarrow \mathbb{Z}_{\ge 0}$$,
* $(Z_{d, a}^{s})_{s \in [0:T]} \ (d \in [1:M], a \in [1:N])$,
    * the number of conversions of advertimesement $a$ at display $d$,
    * $Z_{d, a}^{0}$ is an initial value
    * adapted process
    * $Z_{d, a}^{s} \in \mathbb{Z}_{\ge 0}$ is an initial value
    * $$Z_{d, a}^{s}: \Omega \rightarrow \mathbb{Z}_{\ge 0}$$,
* $B_{a} \in \mathbb{R}_{\ge 0}$,
    * budget of ad $a$,
* $$\mathcal{K} := \{x \in [0, 1]^{N} \mid \sum_{i=1}^{N} x^{a} = 1\}$$,
    * the domain of the loss function and constraints
    * each element denotes the probability of the choice of advertisements.

For the simplicity, we define several notations.

$$
\begin{eqnarray}
    \Delta Y_{d, a}^{t}
    & := &
        Y_{d, a}^{t+1}
        -
        Y_{d, a}^{t}
    \nonumber
    \\
    \Delta Z_{d, a}^{t}
    & := &
        Z_{d, a}^{t+1}
        -
        Z_{d, a}^{t}
    \nonumber
    \\
    S_{d, a}^{t}
    & := &
        \sum_{s=0}^{t-1}
            \mathrm{CPC}_{d, a}(Y_{d, a}^{s}, Z_{d, a}^{s})
            \Delta Y_{d, a}^{s}
    \nonumber
    \\
    & = &
        \sum_{s=0}^{t-1}
            \mathrm{tCPA}_{a}
            \frac{
                Z_{d, a}^{s}
            }{
                Y_{d, a}^{s}
            }
            \Delta
            Y_{d, a}^{s}
    \nonumber
\end{eqnarray}
$$

$S_{d, a}^{t}$ is profit of ad $a$ on display $d$ until trial $t$.

With this notation, CPC and CPA are defined as

$$
\begin{eqnarray}
    \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
    & := &
        \mathrm{tCPA}_{a}
        \frac{
            Z_{d, a}^{t}
        }{
            Y_{d, a}^{t}
        }
    \nonumber
    \\
    \mathrm{CPA}_{a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
    & := &
        \frac{
            \sum_{d=1}^{M}
            \sum_{s=0}^{t-1}
                \mathrm{CPC}_{d, a}(Y_{d, a}^{s}, Z_{d, a}^{s})
                \Delta Y_{d, a}^{s}
        }{
            \sum_{d=1}^{M}
                Z_{d, a}^{t}
        }
    \nonumber
    \\
    & = &
        \frac{
            \sum_{d=1}^{M}
                S_{d, a}^{t}
        }{
            \sum_{d=1}^{M}
                Z_{d, a}^{t}
        }
    .
    \nonumber
\end{eqnarray}
$$

For $t \in [0:T-1]$, constraints about target CPA are given by

$$
\begin{eqnarray}
    & &
        g_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [0:t+1]}, (Z_{d, a}^{s})_{s \in [0:t+1]})
    \nonumber
    \\
    & := &
        \frac{
            \sum_{d=1}^{M}
                S_{d, a}^{t}
            +
            x_{a}
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \Delta Y_{d, a}^{t}
        }{
            \sum_{d=1}^{M}
                Z_{d, a}^{t+1}
        }
        -
        \mathrm{tCPA}_{a}
    \nonumber
    \\
    & = &
        \frac{
            \sum_{d=1}^{M}
                S_{d, a}^{t}
        }{
            \sum_{d=1}^{M}
                Z_{d, a}^{t+1}
        }
        -
        \mathrm{tCPA}_{a}
        +
        x_{a}
        \left(
            \frac{
                \sum_{d=1}^{M}
                    \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                    \Delta Y_{d, a}^{t}
            }{
                \sum_{d=1}^{M}
                    Z_{d, a}^{t+1}
            }
        \right)
    \label{formulation_of_online_convex_optimization_constraints_target_cpa}
    .
\end{eqnarray}
$$

With categorical vector $I_{t}$, the target CPA constraints is similar to the following condition;

$$
\begin{eqnarray}
    \frac{
        \sum_{d=1}^{M}
            S_{d, a}^{t}
        +
        \sum_{d=1}^{M}
            \mathrm{CPC}_{d, I_{t}}(Y_{d, I_{t}}^{t}, Z_{d, I_{t}}^{t})
            \Delta Y_{d, I_{t}}^{t}
    }{
        \sum_{d=1}^{M}
            Z_{d, I_{t}}^{t+1}
    }
    \le
    \mathrm{tCPA}_{a}
    .
    \nonumber
\end{eqnarray}
$$

Similarly, for $t \in [0:T-1]$, constraints to badget for each ad are given by

$$
\begin{eqnarray}
    & &
        h_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [0:t+1]}, (Z_{d, a}^{s})_{s \in [0:t+1]})
    \nonumber
    \\
    & := &
        \sum_{d=1}^{M}
            S_{d, a}^{t}
        -
        B_{a}
        +
        x_{a}
        \left(
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \Delta Y_{d, a}^{t}
        \right)
    \label{formulation_of_online_convex_optimization_constraints_badget}
    .
\end{eqnarray}
$$

The loss function at $t \in [0:T-1]$ is given by

$$
\begin{eqnarray}
    & &
        f^{t}(x; (Y_{d, a}^{s})_{s \in [t:t+1]}, (Z_{d, a}^{s})_{s \in [t:t+1]})
    \nonumber
    \\
    & := &
        -
        \sum_{a=1}^{N}
        \sum_{d=1}^{M}
            \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
            \Delta Y_{d, a}^{t}
            x_{a}
    .
\end{eqnarray}
$$

The loss function are interpreted as the expected loss of choice of advertisements with a $N$-categorial random variable $I$ whose p.d.f. is determined by $(x_{a})_{a \in [1:N]}$.
Gradients of these cost functions are easy to calculate.

$$
\begin{eqnarray}
    & &
        \left(
            \nabla f^{t}(x; (Y_{d, a}^{s})_{s \in [t:t+1]}, (Z_{d, a}^{s})_{s \in [t:t+1]})
        \right)_{a}
    \nonumber
    \\
    & = &
        -
        \sum_{d=1}^{M}
            \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
            \Delta Y_{d, a}^{t}
    \nonumber
\end{eqnarray}
$$

Similarly,

$$
\begin{eqnarray}
    & &
        \left(
            \nabla g_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [t:t+1]}, (Z_{d, a}^{s})_{s \in [t:t+1]})
        \right)_{a^{\prime}}
    \nonumber
    \\
    & = &
        1_{\{a = a^{\prime}\}}
        \left(
            \frac{
                \sum_{d=1}^{M}
                    \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                    \Delta Y_{d, a}^{t}
            }{
                \sum_{d=1}^{M}
                    Z_{d, a}^{t+1}
            }
        \right)
    \nonumber
\end{eqnarray}
$$

As to the badget constraints,

$$
\begin{eqnarray}
    & &
        \left(
            \nabla h_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [t:t+1]}, (Z_{d, a}^{s})_{s \in [t:t+1]})
        \right)_{a^{\prime}}
    \nonumber
    \\
    & = &
        1_{\{a=a^{\prime}\}}
        \left(
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \Delta Y_{d, a}^{t}
        \right)
    \nonumber
\end{eqnarray}
$$

Let $V, \alpha > 0$.
The next ad is chosen by minimizing the following function.

$$
\begin{eqnarray}
    & &
        F^{t}(x)
    \nonumber
    \\
    & := &
        V
        \langle
            \nabla f^{t}(x^{t}),
            x - x^{t}
        \rangle
        +
        \sum_{a=1}^{N}
            Q_{a}^{t}
            \langle
                \nabla g_{a}^{t}(x^{t}),
                x - x^{t}
            \rangle
        +
        \sum_{a=N+1}^{2N}
            Q_{a}^{t}
            \langle
                \nabla h_{a}^{t}(x^{t}),
                x - x^{t}
            \rangle
        +
        \alpha
        \norm{
            x - x^{t}
        }^{2}
    \nonumber
    \\
    & = &
        -
        V
        \sum_{a=1}^{N}
        \sum_{d=1}^{M}
            \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
            \Delta Y_{d, a}^{t}
            (x_{a} - x_{a}^{t})
        +
        \sum_{a=1}^{N}
            Q_{a}^{t}
            \left(
                \frac{
                    \sum_{d=1}^{M}
                        \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                        \Delta Y_{d, a}^{t}
                }{
                    \sum_{d=1}^{M}
                        Z_{d, a}^{t+1}
                }
            \right)
            (x_{a} - x_{a}^{t})
    \nonumber
    \\
    & &
        +
        \sum_{a=1}^{N}
            Q_{N+a}^{t}
            \left(
                \sum_{d=1}^{M}
                    \mathrm{CPC}_{d, a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
                    \Delta Y_{d, a}^{t}
            \right)
            (x_{a} - x_{a}^{t})
        +
        \alpha
        \norm{x - x^{t}}^{2}
    \label{formulation_of_online_convex_optimization_objective_function}
\end{eqnarray}
$$

Thus, the probability of choosing the next ad is

$$
\begin{eqnarray}
    x^{t+1}
    & := &
        \argmin_{x \in \mathcal{K}}
            F^{t}(x)
    \label{formulation_of_online_convex_optimization_next_probability}
    .
\end{eqnarray}
$$

The parameter $(Q_{a}^{t})_{t \in [2:T]}$ need to be updated depending on a type of constraints.
If $a \in [1:N]$,

$$
\begin{eqnarray}
    \tilde{Q}_{a}^{t+1}
    & := &
        Q_{a}^{t}
        +
        g_{a}^{t}(x^{t})
        +
        \langle
            \nabla g_{a}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
    \nonumber
    \\
    & = &
        Q_{a}^{t}
        +
        \frac{
            \sum_{d=1}^{M}
                S_{d, a}^{t}
        }{
            \sum_{d=1}^{M}
                Z_{d, a}^{t+1}
        }
        -
        \mathrm{tCPA}_{a}
        +
        x_{a}^{t}
        \left(
            \frac{
                \sum_{d=1}^{M}
                    \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                    \Delta Y_{d, a}^{t}
            }{
                \sum_{d=1}^{M}
                    Z_{d, a}^{t+1}
            }
        \right)
    \nonumber
    \\
    & &
        +
        \left(
            \frac{
                \sum_{d=1}^{M}
                    \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                    \Delta Y_{d, a}^{t}
            }{
                \sum_{d=1}^{M}
                    Z_{d, a}^{t+1}
            }
        \right)
        (x_{a}^{t+1} - x_{a}^{t})
    \nonumber
    \\
    & = &
        Q_{a}^{t}
        +
        \frac{
            \sum_{d=1}^{M}
                S_{d, a}^{t}
        }{
            \sum_{d=1}^{M}
                Z_{d, a}^{t+1}
        }
        -
        \mathrm{tCPA}_{a}
        +
        \left(
            \frac{
                \sum_{d=1}^{M}
                    \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                    \Delta Y_{d, a}^{t}
            }{
                \sum_{d=1}^{M}
                    Z_{d, a}^{t+1}
            }
        \right)
        x_{a}^{t+1}
    \nonumber
    \\
    Q_{a}^{t+1}
    & := &
        \max(\tilde{Q}_{a}^{t+1}, 0)
    \label{formulation_of_online_convex_optimization_update_parameter_01}
    .
\end{eqnarray}
$$

If $a \in [N+1:2N]$,

$$
\begin{eqnarray}
    \tilde{Q}_{a}^{t+1}
    & := &
        Q_{a}^{t}
        +
        h_{a}^{t}(x^{t})
        +
        \langle
            \nabla h_{a}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
    \nonumber
    \\
    & = &
        Q_{a}^{t}
        +
        \sum_{d=1}^{M}
            S_{d, a}^{t}
        -
        B_{a}
        +
        x_{a}^{t}
        \left(
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \Delta Y_{d, a}^{t}
        \right)
        +
        \left(
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \Delta Y_{d, a}^{t}
        \right)
        (x_{a}^{t+1} - x_{a}^{t})
    \nonumber
    \\
    & = &
        Q_{a}^{t}
        +
        \sum_{d=1}^{M}
            S_{d, a}^{t}
        -
        B_{a}
        +
        \left(
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \Delta Y_{d, a}^{t}
        \right)
        x_{a}^{t+1}
    \nonumber
    \\
    Q_{a}^{t+1}
    & := &
        \max(\tilde{Q}_{a}^{t+1}, 0)
    \label{formulation_of_online_convex_optimization_update_parameter_02}
    .
\end{eqnarray}
$$

#### Algorithm
* $V, \alpha > 0$,
* $\mathcal{K} := [0, 1]^{N}$,
* $x^{0} \in \mathcal{K}$,
* $Q_{a}^{0} := 0 \ (k \in [1:2N])$,
* $$\{Y_{d, a}^{0}\}_{d, a}$$,
    * the number of initial clicks
* $$\{Z_{d, a}^{0}\}_{d, a}$$,
    * the number of initial conversions

**Step1.** For $t = 0, \ldots, T-1$,

**Step2-1.** Draw $N$ categorical random variable $I_{t}$ with probability $x^{t}$.
$I_{t}$ is independent from $$(I_{s})_{s \in [0:t-1]}$$.

**Step2-2.** Play $I_{t}$

**Step3-1.** Obverse $Y^{t + 1}$,

**Step3-2.** Obverse $Z^{t + 1}$,

**Step4-1.** Observe a cost function $f^{t}$

**Step4-2.** Observe constraints $g_{a}^{t}$.

**Step4-3.** Observe constraints $h_{a}^{t}$.

**Step5.** Update $x^{t+1}$ by $$\eqref{formulation_of_online_convex_optimization_next_probability}$$

**Step6.** Update $Q_{a}^{t+1}$ by $$\eqref{formulation_of_online_convex_optimization_update_parameter_01}$$ and $$\eqref{formulation_of_online_convex_optimization_update_parameter_02}$$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Interpretation of minimized funciton
TODO: Update this section.

Note that smaller value of $(x_{a} - x_{a}^{t})$ indicates that we recommnd ad $a$ with less probability than the probability at time $t$.
On the other hand, larger value of $(x_{a} - x_{a}^{t})$ means that ad $a$ is likely to be recommended.
Considering this, the last term in $$\eqref{formulation_of_online_convex_optimization_objective_function}$$ means probability changes moderately depending on $\alpha$.

Suppose that $(x_{a} - x_{a}^{t}) > 0$.
We will see what parameter and event minimizes the funciton $$\eqref{formulation_of_online_convex_optimization_objective_function}$$ for each term.
In the first term, such conditions are

* CPC at $t$ is high
* the recommended ad $t$ is clicked

In the second term,

* CPC at $t$ is small
* conversion occurs
    * $\Delta Z_{d, a}^{t} = 1$.
* the recommeded ad is not clicked

In the third term,

* the recommended ad is not clicked
* if the recommended ad is clicked
    * CPC at $t$ is small

<div class="end-of-statement" style="text-align: right">■</div>

#### Interpretation of parameters for constraints
TODO: Update this section.

$Q_{a}^{t}$ guarantees that the longer violation of the constraint, the less probability of choice of ad $a$.
The following events lower the probabilty $x_{a}^{t+2}$.

As to target CPA constraint,

* higher probability $x_{a}^{t + 1}$ of choosing ad $a$
* conversion of the recommened ad $a$
* higher CPA at $t$
* In case the recommended ad $a$ is clicked,
    * no conversion of the ad $a$
    * higher CPC

Parameters of badget constraints increase if any of the following conditions are met;

* higher probability $x_{a}^{t + 1}$ of choosing ad $a$
* higher CPA between 0 to $t+1$
* the recommended ad is clicked but no conversion

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* Hazan, E. (2016). Introduction to Online Convex Optimization. Foundations and Trends® in Optimization (Vol. 2). https://doi.org/10.1561/2400000013
* Yu, H., Neely, M. J., & Wei, X. (2017). Online Convex Optimization with Stochastic Constraints, 1–23. Retrieved from http://arxiv.org/abs/1708.03741
