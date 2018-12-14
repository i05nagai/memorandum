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
    * 1 means conversion occurs

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
        \mathrm{CPA}_{d, a}^{t}
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

### online convex optimization

* $\mathcal{S}_{\mathrm{CPC}} \subseteq [0, 1]^{N}$,
    * the possible values of CPCs of the advertisements
* $\mathcal{F}^{\prime}$,
    * the all loss functions forming

$$
    x \in \mathcal{K},
    \
    y \in \mathcal{Y},
    \
    z \in \mathcal{Z},
    \
    \mathrm{CPC} \in \mathcal{S}_{\mathrm{CPC}},
    \
    f(x; y, z, \mathrm{CPC})
    :=
    \sum_{a=1}^{N}
        x_{a}
        \mathrm{CPC}_{a}
        (1 - y_{a})
        (1 - z_{a})
    .
$$

* $\mathcal{F}$,
    * the possible loss functions

$$
    \mathcal{F}
    :=
    \{
        f(\cdot; y, z, \mathrm{CPC})
        \in
        \mathcal{F}^{\prime}
        \mid
        y_{a} = 0 \Rightarrow z_{a} = 0
    \}

$$

Let $A$ be an algorithm solving this problem.
We define the regret of the algorithm,

$$
\begin{eqnarray}
    \mathrm{regret}_{T}(A)
    & := &
        \sup_{(f_{1}, \ldots, f_{T}) \subseteq \mathcal{F}}
        \left(
            \sum_{t=1}^{T}
                f_{t}(x^{t}; y^{t}, z^{t}, \mathrm{CPC}^{t})
            -
            \min_{x \in \mathcal{K}}
                \sum_{t=1}^{N}
                    f_{t}(x; y^{t}, z^{t}, \mathrm{CPC}^{t})
        \right)
    \nonumber
    \\
    & = &
        \sup_{(f_{1}, \ldots, f_{T}) \subseteq \mathcal{F}}
        \left(
            \sum_{t=1}^{T}
                \sum_{a=1}^{N}
                    x_{a}^{t}
                    (1 - y_{a}^{t})
                    (1 - z_{a}^{t})
                    \mathrm{CPC}_{a}^{t}
            -
            \min_{x \in \mathcal{K}}
                \sum_{t=1}^{N}
                    \sum_{a=1}^{N}
                        x_{a}
                        (1 - y_{a}^{t})
                        (1 - z_{a}^{t})
                        \mathrm{CPC}_{a}^{t}
        \right)
\end{eqnarray}
    .
$$

#### Examples
* $N = 2$,
* $M = 2$,

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

Criterion of loss function

* If we choose an advertisement in which a user is not interested, it should be penalized
* If we 


#### Application
* $$(\Omega, \mathcal{F}, P, \{\mathcal{F}_{t}\}_{t \in \mathbb{N}})$$,
    * probability space with filtration
* $T \in \mathbb{N}$,
* $N \in \mathbb{N}$,
    * the number of ads
* $M \in \mathbb{N}$,
    * the number of display ads
* $(Y_{d, a}^{s})_{s \in [0:T]} \ (d \in [1:M], a \in [1:N])$,
    * the number of clicks of advertimesement $a$ at dispaly $d$,
    * $Y_{d, a}^{0}$ is an initial value
    * adapted
* $(Z_{d, a}^{s})_{s \in [0:T]} \ (d \in [1:M], a \in [1:N])$,
    * the number of conversions of advertimesement $a$ at dispaly $d$,
    * $Z_{d, a}^{0}$ is an initial value
    * adapted
* $B_{a} \in \mathbb{R}_{\ge 0}$,

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
    \mathrm{CPA}_{d, a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
    & := &
        \frac{
            \sum_{s=0}^{t-1}
                \mathrm{CPC}_{d, a}(Y_{d, a}^{s}, Z_{d, a}^{s})
                \Delta Y_{d, a}^{s}
        }{
            Z_{d, a}^{t}
        }
    \nonumber
\end{eqnarray}
$$

For $t \in [0:T-1]$,

$$
\begin{eqnarray}
    & &
        g_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [0:t+1]}, (Z_{d, a}^{s})_{s \in [0:t+1]})
    \nonumber
    \\
    & := &
        \sum_{d=1}^{M}
            \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
            \frac{
                Z_{d, a}^{t}
            }{
                Z_{d, a}^{t+1}
            }
            x_{a}
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
                Z_{d, a}^{t+1}
            }
        \right)
\end{eqnarray}
$$

For $t \in [0:T-1]$,

$$
\begin{eqnarray}
    & &
        h_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [0:t+1]}, (Z_{d, a}^{s})_{s \in [0:t+1]})
    \nonumber
    \\
    & := &
        \sum_{s=0}^{t}
        \sum_{d=1}^{M}
            \frac{
                Y_{d, a}^{s}
            }{
                Z_{d, a}^{s}
            }
            \mathrm{CPA}_{d, a}^{s}(Y_{d, a}^{s}, Z_{d, a}^{s})
        -
        B_{a}
        +
        x_{a}
        \left(
            \sum_{d=1}^{M}
                \frac{
                    Y_{d, a}^{t+1}
                }{
                    Z_{d, a}^{t+1}
                }
                \mathrm{CPA}_{d, a}^{t+1}(Y_{d, a}^{t+1}, Z_{d, a}^{t+1})
        \right)
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

Gradients of the cost functions is given by

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
            \sum_{d=1}^{M}
                \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \frac{
                    Z_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
            +
            \left(
                \frac{
                    \sum_{d=1}^{M}
                        \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                        \Delta Y_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
            \right)
        \right)
    \nonumber
\end{eqnarray}
$$

For the badget constraints,

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
                \frac{
                    Y_{d, a}^{t+1}
                }{
                    Z_{d, a}^{t+1}
                }
                \mathrm{CPA}_{d, a}^{t+1}(Y_{d, a}^{t+1}, Z_{d, a}^{t+1})
        \right)
    \nonumber
\end{eqnarray}
$$

Let $V, \alpha > 0$.

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
                \sum_{d=1}^{M}
                    \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                    \frac{
                        Z_{d, a}^{t}
                    }{
                        Z_{d, a}^{t+1}
                    }
                +
                \left(
                    \frac{
                        \sum_{d=1}^{M}
                            \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                            \Delta Y_{d, a}^{t}
                    }{
                        Z_{d, a}^{t+1}
                    }
                \right)
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
                    \frac{
                        Y_{d, a}^{t+1}
                    }{
                        Z_{d, a}^{t+1}
                    }
                    \mathrm{CPA}_{d, a}^{t+1}(Y_{d, a}^{t+1}, Z_{d, a}^{t+1})
            \right)
            (x_{a} - x_{a}^{t})
        +
        \alpha
        \norm{x - x^{t}}^{2}
    \nonumber
\end{eqnarray}
$$

The next point is defined as

$$
\begin{eqnarray}
    x^{t+1}
    & := &
        \argmin_{x \in \mathcal{D}}
            F^{t}(x)
\end{eqnarray}
$$

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
        \sum_{d=1}^{M}
            \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
            \frac{
                Z_{d, a}^{t}
            }{
                Z_{d, a}^{t+1}
            }
            x_{a}
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
                Z_{d, a}^{t+1}
            }
        \right)
    \nonumber
    \\
    & &
        +
        \left(
            \sum_{d=1}^{M}
                \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \frac{
                    Z_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
            +
            \left(
                \frac{
                    \sum_{d=1}^{M}
                        \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                        \Delta Y_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
            \right)
        \right)
        (x_{a}^{t+1} - x_{a}^{t})
    \nonumber
    \\
    Q_{a}^{t+1}
    & := &
        \max(\tilde{Q}_{a}^{t+1}, 0)
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
        \sum_{s=0}^{t}
        \sum_{d=1}^{M}
            \frac{
                Y_{d, a}^{s}
            }{
                Z_{d, a}^{s}
            }
            \mathrm{CPA}_{d, a}^{s}(Y_{d, a}^{s}, Z_{d, a}^{s})
        -
        B_{a}
        +
        x_{a}
        \left(
            \sum_{d=1}^{M}
                \frac{
                    Y_{d, a}^{t+1}
                }{
                    Z_{d, a}^{t+1}
                }
                \mathrm{CPA}_{d, a}^{t+1}(Y_{d, a}^{t+1}, Z_{d, a}^{t+1})
        \right)
        +
        \left(
            \sum_{d=1}^{M}
                \frac{
                    Y_{d, a}^{t+1}
                }{
                    Z_{d, a}^{t+1}
                }
                \mathrm{CPA}_{d, a}^{t+1}(Y_{d, a}^{t+1}, Z_{d, a}^{t+1})
        \right)
        (x_{a}^{t+1} - x_{a}^{t})
    \nonumber
    \\
    Q_{a}^{t+1}
    & := &
        \max(\tilde{Q}_{a}^{t+1}, 0)
    .
\end{eqnarray}
$$


## Reference
* Hazan, E. (2016). Introduction to Online Convex Optimization. Foundations and Trends® in Optimization (Vol. 2). https://doi.org/10.1561/2400000013
