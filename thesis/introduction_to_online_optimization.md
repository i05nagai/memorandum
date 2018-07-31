---
title: Introduction to Online Optimization
---

## Introduction to Online Optimization


## 1. Introduction


* $\mathcal{Z}$,
    * domain of observations
* $Z_{1}, \ldots, Z_{n} \in \mathcal{Z}$,
    * i.i.d
* $\mathcal{A}$,
    * set of possible actions
* $a(Z_{1}, \ldots, Z_{n}) \in \mathcal{A}$,
    * decision function
* $l:\mathcal{A} \times \mathcal{Z} \rightarrow \mathbb{R}_{\ge 0}$,
    * loss function
* $\mathrm{E}[l(a(Z_{1}, \ldots, Z_{n}), Z)]$,
    * average loss

Objectives is the minimize the exccess risk:

$$
    r_{n}
    :=
    \mathrm{E}
    \left[
        l(a(Z_{1}, \ldots, Z_{n}), Z)
        -
        \inf_{a \in \mathcal{A}}
            l(a, Z)
    \right]
    .
$$


## 2. Online optimization on the simplex


#### Definition.
* $d \ge 2$,

$(d-1)$-simplex $\Delta_{d}$

$$
    \Delta_{d}
    :=
    \{
        p \in \mathbb{R}_{\ge 0}^{d}
        \mid
        \sum_{i=1}^{d}
            p_{i} = 1
    \}
    .
$$

Cumulative regret for action set $\Delta_{d}$ is defined by

$$
    R_{n}
    :=
    \sum_{t=1}^{n}
        l(p_{t}, z_{t})
    -
    \inf_{q \in \Delta_{d}}
        \sum_{t=1}^{n}
            l(q, z_{t})
    .
$$

If action set is unit vectors, we write regret for the action set

$$
\begin{eqnarray}
    R_{n}^{E}
    :=
    \sum_{t=1}^{n}
        l(p_{t}, z_{t})
    -
    \inf_{i \in \{1, \ldots, d\}}
        \sum_{t=1}^{n}
            l(e_{i}, z_{t})
    \label{definition_expert_regret}
\end{eqnarray}
$$

where $e_{i}$ is $i$-dim unit vector.

The upper bound of $R_{N}$ is called regret bounds.
The upper bound of $R_{N}^{E}$ is called expert regret bounds.

<div class="end-of-statement" style="text-align: right">■</div>

### 2.1 Exponentially weighted average forecaster (Exp strategy)
One of the most simplest strategy.

* $\eta > 0$,
    * parameter

$$
\begin{eqnarray}
    p_{t}
    & := &
        \sum_{i=1}^{d}
            \frac{
                w_{t, i}
            }{
                \sum_{j=1}^{d}
                    w_{t, j}
            }
            e_{i}
    \nonumber
    \\
    w_{t, i}
    & := &
        \exp
        \left(
           -\eta
            \sum_{s=1}^{t-1}
                l(e_{i}, z_{s})
        \right)
    .
    \nonumber
\end{eqnarray}
$$

Note that $w_{t, i} := w_{t-1,i}\exp(- \eta l(e_{i}, z_{t-1}))$.
The computational complexity is $O(d)$.

Moreover, let $$I: \Omega \rightarrow \{1, \ldots, d\}$$ with probability

$$
\begin{eqnarray}
    P(I = i)
    =
    \frac{
        w_{t, i}
    }{
        \sum_{j=1}^{d}
            w_{t, j}
    }
    .
    \nonumber
\end{eqnarray}
$$

We have

$$
\begin{eqnarray}
    p_{t}
    =
    \mathrm{E}
    \left[
        e_{I}
    \right]
    \label{exp_strategy_prediction}
   .
\end{eqnarray}
$$

### 2.2 Bounded convex loss and expert regret
We analyze the expert regret $R_{n}^{E}$ of the Exp strategy.


### Lemma 2.1
See <a href="{{ site.baseurl }}/math/hoeffding_inequality.html">Hoeffding Inequality</a>.

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 2.1
For any convex loss taking values in $[0, 1]$, the Exp strategy satisfies:

$$
    R_{n}^{E}
    \le
    \frac{
        \log d
    }{
        \eta
    }
    +
    \frac{
        n \eta
    }{
        8
    }
    .
$$

In particular with $\eta = 2 \sqrt{\frac{2 \log d}{n}}$ it satisfies:

$$
    R_{n}^{E}
    \le
    \sqrt{
        \frac{
            n \log d
        }{
            2
        }
    }
    .
$$

### proof.
Let 

$$
\begin{eqnarray}
    w_{t, i}
    & := &
        \exp
            \left(
               -\eta
               l(e_{i}, z_{s})
            \right)
    \nonumber
    \\
    W_{t}
    & := &
        \sum_{i=1}^{d}
            w_{t, i}
    .
\end{eqnarray}
$$

By definition, $w_{1, i} = 1$ and $W_{1} = d$.
Then we have

$$
\begin{eqnarray}
    \log
        \frac{
            W_{n + 1}
        }{
            W_{1}
        }
    & = &
        \log
        \left(
            \sum_{i=1}^{d}
                w_{n + 1, i}
        \right)
        -
        \log d
    \nonumber
    \\
    & \ge &
        \log
        \left(
            \max_{1 \le i \le d}
                w_{n+1, i}
        \right)
        - \log d
    \nonumber
    \\
    & \ge &
        -\eta
        \min_{1 \le i \le d}
            \sum_{t=1}^{n}
                l(e_{i}, z_{t})
        - \log d
    .
\end{eqnarray}
$$

Let $$I: \Omega \rightarrow \{1, \ldots, d\}$$ be r.v. for chosing index i with probability

$$
    P(I = i)
    =
    \frac{
        w_{t, i}
    }{
        W_{t}
    }
    .
$$

Then we have

$$
\begin{eqnarray}
    \log
        \frac{
            W_{t + 1}
        }{
            W_{t}
        }
    & = &
        \log
        \left(
            \frac{1}{W_{t}}
            \sum_{i=1}^{d}
                w_{t}(i)
                \exp
                \left(
                    -\eta
                    l(e_{i}, z_{t})
                \right)
        \right)
    \nonumber
    \\
    & = &
        \log
        \left(
            \mathrm{E}
            \left[
                \exp
                \left(
                    -\eta
                    l(e_{I}, z_{t})
                \right)
            \right]
        \right)
    \nonumber
    \\
    & \le &
        \log
        \left(
            \exp
            \left(
                -\eta
                \mathrm{E}[ l(e_{I}, z_{t}) ]
                +
                \frac{
                    \eta^{2}
                }{
                    8
                }
            \right)
        \right)
        \quad
        (\because \text{Hoeffding inequality})
    \nonumber
    \\
    & = &
        -\eta
        \mathrm{E}[ l(e_{I}, z_{t}) ]
        +
        \frac{
            \eta^{2}
        }{
            8
        }
    \nonumber
    \\
    & \le &
        -\eta
        l(\mathrm{E}[e_{I}], z_{t})
        +
        \frac{
            \eta^{2}
        }{
            8
        }
        \quad
        (\because \text{Jensen's inequality})
    \nonumber
    \\
    & = &
        -\eta
        l(p_{t}, z_{t})
        +
        \frac{
            \eta^{2}
        }{
            8
        }
        \quad
        (\because \eqref{exp_strategy_prediction})
    .
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \sum_{t=1}^{n}
        \log
            \frac{
                W_{t + 1}
            }{
                W_{t}
            }
    & = &
        -
        \sum_{t=1}^{n}
            \eta
            l(p_{t}, z_{t})
        +
        \frac{
            \eta^{2}n
        }{
            8
        }
    .
\end{eqnarray}
$$

Combining those results

$$
\begin{eqnarray}
    -\eta
    \min_{1 \le i \le d}
        \sum_{t=1}^{n}
            l(e_{i}, z_{t})
    - \log d
    & \le &
        \log
            \frac{
                W_{n+1}
            }{
                W_{1}
            }
    \nonumber
    \\
    & = &
        \sum_{t=1}^{n}
            \log
                \frac{
                    W_{t+1}
                }{
                    W_{t}
                }
    \nonumber
    \\
    & \le &
        -
        \sum_{t=1}^{n}
            \eta
            l(p_{t}, z_{t})
        +
        \frac{
            \eta^{2}n
        }{
            8
        }
    .
\end{eqnarray}
$$

The above equation implies that

$$
\begin{eqnarray}
    & &
        \sum_{t=1}^{n}
            \eta
            l(p_{t}, z_{t})
        -\eta
        \min_{1 \le i \le d}
            \sum_{t=1}^{n}
                l(e_{i}, z_{t})
        \le
        \frac{
            \eta^{2}n
        }{
            8
        }
        +
        \log d
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{t=1}^{n}
            l(p_{t}, z_{t})
        -
        \min_{1 \le i \le d}
            \sum_{t=1}^{n}
                l(e_{i}, z_{t})
        \le
        \frac{
            \eta n
        }{
            8
        }
        +
        \frac{\log d}{\eta}
    \nonumber
    \\
    & \Leftrightarrow &
        R_{n}^{E}
        \le
        \frac{
            \eta n
        }{
            8
        }
        +
        \frac{\log d}{\eta}
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### 2.3 Exp-concave loss and expert regret

#### Definition. sigma-exp-concave loss
* $l:\mathcal{A} \times \mathcal{Z} \rightarrow \mathbb{R}$,
* $\sigma \in \mathbb{R}$,

Loss function $l$ is said to be $\sigma$-exp-concave loss function if

$$
    \forall z \in \mathcal{Z},
    \
    p
    \mapsto
    \exp
    \left(
        -
        \sigma
        l(p, z)
    \right)
$$

is concave function.

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 2.2
* $l$,
    * $\sigma$-exp-concave loss function

The Exp strategy with parameter $\eta = \sigma$ satisfies

$$
    R_{n}^{E}
    \le
    \frac{
        \log d
    }{
        \sigma
    }
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

### 2.4 lower bound

#### Lemma 2.2
* $$(\sigma_{i, t})_{1 \le i \le d, 1 \le t \le n}$$,
    * I.I.D. Rademacher r.v.s

$$
    \lim_{d \rightarrow \infty} 
    \lim_{n \rightarrow \infty} 
        \frac{
            \mathrm{E}
            \left[
                \max_{i = 1, \ldots, d}
                    \sum_{t=1}^{n}
                        \sigma_{i, t}
            \right]
        }{
            \sqrt{2 n \log d}
        }
    =
    1
    .
$$

#### proof.
Taking $N := d$, $a_{j, i} := 1$, then applying <a href="{{ site.baseurl }}/math/distribution/rademacher_distribution.html#proposition-5">proposition 5</a>,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \max_{i = 1, \ldots, d}
            \sum_{t=1}^{n}
                \sigma_{i, t}
    \right]
    & = &
        n
        \mathrm{E}
        \left[
            \max_{i = 1, \ldots, d}
                \frac{1}{n}
                \sum_{t=1}^{n}
                    a_{i, t}
                    \sigma_{i, t}
        \right]
    \nonumber
    \\
    & \le &
        n
        \max_{i = 1, \ldots, d}
            \|
            a_{i}
            \|_{1}
        \frac{
            \sqrt{
                2 \ln d
            }
        }{
            n
        }
    \nonumber
    \\
    & = &
        n
        \sqrt{
            2 \ln d
        }
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{
        \mathrm{E}
        \left[
            \max_{i = 1, \ldots, d}
                \sum_{t=1}^{n}
                    \sigma_{i, t}
        \right]
    }{
        \sqrt{2 n \log d}
    }
    & \le &
        \frac{
            \sqrt{2 n \log d}
        }{
            \sqrt{2 n \log d}
        }
        \quad
        (\because \text{proposition})
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 2.3


#### proof.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
