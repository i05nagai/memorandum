---
title: Introduction to Online Optimization Chapter01
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


### 1.2. Online Learning

Online optimization protocol

* Step1. For $t = 1, \ldots, n$,
* Step2. Choose action $a_{t} \in \mathcal{A}$,
* Step3. Simultaneously an adversary selects $z_{t} \in \mathcal{Z}$,
* Step4. Suffer loss $l(a_{t}, z_{t})$,
* Step5. Observe $z_{t}$

Objectives

$$
\begin{eqnarray}
    R_{n}
    & := &
        \sum_{t=1}^{n}
            l(a_{t}, z_{t})
        -
        \inf_{a \in \mathcal{A}}
            \sum_{t=1}^{n}
                l(a, z_{t})
    \nonumber
\end{eqnarray}
$$


#### Example 1: Online regression, online classification

Parameters

* $\mathcal{X}$,
    * input
* $\mathcal{Y}$,
    * categories
* $\mathcal{A}$,
    * a set of regression functions; $a_{t}: \mathcal{X} \rightarrow \mathcal{Y}$,

Step

* Step1. For $t = 1, \ldots, n$,
* Step2. choose regression function $a_{t}$,
* Step3. Advertisery choice $z_{t}$
* Step4. Suffer loss $l(z_{t}, (x_{t}, y_{t}))$,
* Step5. Observe $(x_{t}, y_{t}) \in \mathcal{X} \times \mathcal{Y}$,

Example of loss function

$$
    l(a, (x, y))
    :=
    -a(x) 1_{a(x) \le y}
$$


#### Example 2: Sequential investment

* $d \in \mathbb{N}$,
    * the number of assets in a stock market
* $z \in \mathbb{R}_{\ge 0}^{d}$,
    * market vector
    * price of assets
* $a \in \mathbb{R}_{\ge 0}^{d}$,
    * investments for the assets
* $W_{t}$,
    * current total capital

Return of this invesments

$$
    \sum_{i=1}^{d}
        a_{i}
        z_{i}
    =
    a^{\mathrm{T}}
    z
    .
$$

A set of investments is probability simplex

$$
    \mathcal{A}
    :=
    \{
        a \in \mathbb{R}_{\ge 0}^{d}
        \mid
        \sum_{i=}^{d}
            a_{i}
        =
        1
    \}
$$

Wealth at the end of period $t$ satisfies

$$
\begin{eqnarray}
    W_{t}
    & := &
        \sum_{i=1}^{d}
            a_{t, i}
            W_{t-1}
            z_{t, i}
    \nonumber
    \\
    & = &
        W_{t-1}
        a_{t}^{\mathrm{T}}
        z_{t}
    \nonumber
    \\
    & = &
        W_{0}
        \prod_{s=1}^{t}
        a_{s}^{\mathrm{T}}
        z_{s}
    \nonumber
\end{eqnarray}
$$

We want to maximize the competitive wealth ration

$$
\begin{eqnarray}
    & &
        \sup_{a \in \mathcal{A}}
            \frac{
                W_{n}^{a}
            }{
                W_{n}
            }
    \nonumber
    \\
    W_{n}^{a}
    & := &
        W_{0}
        \prod_{s=1}^{n}
            a^{\mathrm{T}}
            z_{s}
    \nonumber
\end{eqnarray}
$$

Logarithmic of the factions satisfies

$$
\begin{eqnarray}
    \log
    \left(
        \frac{
            W_{n}^{a}
        }{
            W_{n}
        }
    \right)
    & = &
        \log
            W_{0}
        +
        \sum_{s=1}^{n}
            \log
                a^{\mathrm{T}}
                z_{s}
        -
        \left(
            \log
                W_{0}
            +
            \sum_{s=1}^{n}
                \log
                    a_{t}^{\mathrm{T}}
                    z_{s}
        \right)
    \nonumber
    \\
    & = &
        \sum_{s=1}^{n}
            \log
                a^{\mathrm{T}}
                z_{s}
        -
        \sum_{s=1}^{n}
            \log
                a_{t}^{\mathrm{T}}
                z_{s}
\end{eqnarray}
$$

Taking logarithm of the competitive wealth ration

$$
\begin{eqnarray}
    \log
    \left(
        \sup_{a \in \mathcal{A}}
            \frac{
                W_{n}^{a}
            }{
                W_{n}
            }
    \right)
    & = &
        \sup_{a \in \mathcal{A}}
            \log
            \left(
                \frac{
                    W_{n}^{a}
                }{
                    W_{n}
                }
            \right)
    \nonumber
    \\
    & = &
        \sup_{a \in \mathcal{A}}
            \left(
                \sum_{s=1}^{n}
                    \log
                        a^{\mathrm{T}}
                        z_{s}
                -
                \sum_{s=1}^{n}
                    \log
                        a_{t}^{\mathrm{T}}
                        z_{s}
            \right)
    \nonumber
    \\
    & = &
        -
        \inf_{a \in \mathcal{A}}
            -
            \sum_{s=1}^{n}
                \log
                    a^{\mathrm{T}}
                    z_{s}
        -
        \sum_{s=1}^{n}
            \log
                a_{t}^{\mathrm{T}}
                z_{s}
    \nonumber
    \\
    & = &
        -
        \inf_{a \in \mathcal{A}}
            \sum_{s=1}^{n}
                l(a, z_{s})
        +
        \sum_{s=1}^{n}
            l(a_{t}, z_{s})
\end{eqnarray}
$$

where $l(a, z) := - \log(a^{\mathrm{T}}z)$ is a loss function.
We obtain corresponding online learning problem to maximize the competitive wealth ration.

#### Example 3: Prediction with expert advice

* $d \in \mathbb{N}$,
* $\mathcal{A}$,
    * convex
* $(b_{t, i})_{i = 1, \ldots, d} \in \mathcal{A}^{d}$
    * advice at $t$,
* $a_{t} \in \mathcal{A}$,
    * choice at $t$,

Our goal is to obain bounds independent of the expert advice with some loss function $\ell$

$$
    R_{n}^{E}
    :=
    \sum_{t=1}^{n}
        l(a_{t}, z_{t})
    -
    \min_{i = 1, \ldots, d}
        \sum_{t=1}^{n}
            l(b_{t, i}, z_{t})
    .
$$

There is another formulation when we allow to choose action $a_{t}$ by a convex combination of the advices.

* $$e_{1}, \ldots, e_{n}$$,
    * canonical basis of $\mathbb{R}^{d}$

Then $(d - 1)$-simplex on the basis is

$$
    \Delta_{d}
    :=
    \{
        p \in \mathbb{R}_{\ge 0}^{d}
        \mid
        \sum_{i=1}^{d}
            p_{i}
        =
        1
    \}
$$


* $\bar{\mathcal{Z}} := \mathcal{A}^{d} \times \mathcal{Z}$,

We define a new loss function $\bar{\ell}:\Delta_{d}\times\bar{\mathcal{Z}} \rightarrow \mathbb{R}_{\ge 0}$,

$$
    \bar{\ell}(p, (b, z))
    :=
    \ell
    \left(
        \sum_{i=1}^{d}
            p_{i}b_{i},
        z
    \right)
    .
$$

Regret of this problem is given by

$$
\begin{eqnarray}
    R_{n}^{E}
    :=
    \sum_{t=1}^{n}
        \bar{\ell}(p_{t}, (bt_{t}, z_{t}))
    -
    \inf_{i = 1, \ldots, d}
        \sum_{t=1}^{n}
            \bar{\ell}(e_{i}, (b_{t}, z_{t}))
    \nonumber
\end{eqnarray}
$$

#### Example 4: Online linear/mixed-integer optimization

A simple linear optimization problem without constraints are formulated with

* $\mathcal{A}, \mathcal{Z} \subseteq \mathbb{R}^{d}$,
* $l(a, z) := a^{\mathrm{T}}z$,

$$
    R_{n}
    :=
    \sum_{t=1}^{n}
        a_{t}^{\mathrm{T}}
        z_{t}
    -
    \inf_{a \in \mathcal{A}}
        \sum_{t=1}^{n}
            a^{\mathrm{T}}
            z_{t}
$$

We formulate the problem of path planning, which hash many intresting and challenging applications.

* $G = (V, E)$,
    * $$V := \{1, \ldots, N \}$$,
    * $$E := \{1, \ldots, d \}$$,
* $$\mathcal{A} \subseteq \{0, 1\}^{d}$$,
    * a element represents a path on the graph
    * $a_{i} = 1$ if a edge $i$ is used, otherwise 0.
* $z \in \mathcal{Z}$,
    * a weight on the edges
* $a^{\mathrm{T}}z$,
    * the total weight given a path $a$ and wieght $z$,
    * the cost of the path

Our objective is the minimize the cost of the path.

$$
    R_{n}
    :=
    \sum_{t=1}^{n}
        a_{t}^{\mathrm{T}}
        z_{t}
    -
    \inf_{a \in \mathcal{A}}
        \sum_{t=1}^{n}
            a^{\mathrm{T}}
            z_{t}
    .
$$

#### Example 5: Online matrix completion

* $k, d \in \mathbb{N}$,
* $M \in \mathbb{R}^{m \times d}$,
    * matrix
* $a_{t} \in \mathbb{R}^{m \times d}$,
    * our prediciton of matrix $M$,
    * rank bounded by $k$,
* $$\mathcal{Z} := \{(i, j) \mid i = 1, \ldots, m, \ j = 1, \ldots, d\}$$,
* $z_{t} := (i, j)$,
    * the position of matrix revealed at $t$,

The loss is 

$$
    \ell(a, (i, j))
    :=
    (a_{i, j} - M_{i, j})^{2}
    .
$$

#### Example 6: One-pass offline optimization

* $\mathcal{A}$,
    * convex set
* $\mathcal{Z}$,
* $\ell: \mathcal{A} \times \mathcal{Z} \rightarrow \mathbb{R}_{\ge 0}^{d}$,
    * a convex loss function with respect to $\mathcal{Z}$,

$$
    a(Z_{1}, \ldots, Z_{n})
    :=
    \frac{ 1 }{ n }
    \sum_{t=1}^{n}
        a_{t}
    .
$$

$$
    r_{n}
    \le
    \frac{
        R_{n}
    }{
        n
    }
    .
$$

## Reference
