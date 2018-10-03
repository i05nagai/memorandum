---
title: Introduction to Online Convex Optimization Chapter01
---

## 1.1 The online convex optimization model

* $\Delta_{d}$,
    * $(d - 1)$-simplex,

* $\mathcal{K} \subseteq \mathbb{R}^{n}$,
* $x_{t} \in \mathcal{K}$,
    * the online player's choice at $t$,
* $\mathcal{F}$,
    * bounded family of cost functions available to the adversary
* $f_{t} \in \mathcal{F}$,
    * the cost function at $t$,
* $f_{t}(x_{t})$,
    * the cost incurred by the online player
* $T \in \mathbb{N}$,
    * the total number of games
* $\mathcal{A}$,
    * an algorithm for OCO
    * $x_{t}$ are determined by the algorithm

$$
    \mathrm{regret}_{T}(\mathcal{A})
    :=
    \sup_{(f_{1}, \ldots, f_{T}) \subset \mathcal{F}}
    \left(
        \sum_{t=1}^{T}
            f_{t}(x_{t})
        -
        \min_{x \in \mathcal{K}}
            \sum_{t=1}^{T}
                f_{t}(x)
    \right)
    .
$$

The second term in the parenthesis denotes the best **fixed** decision in hindsight.
The reason of taking the supremum is that we usually are interested in the upper bound of the algorithm.
The algorithm perform well


## 1.2 Examples of problems that can be modeled via OCO

#### Example. Predidiction from expert advice
* $\mathcal{K} := \Delta_{n}$,
* $\mathcal{F}$,
* $$g_{t} := (g_{t, 1}, \ldots, g_{t, n})$$,
    * $g_{t, i}$
        * the loss of $i$-th expert advice at time $t$,
* $f_{t}:\mathcal{K} \rightarrow [0, 1]$,

<div class="end-of-statement" style="text-align: right">■</div>

#### Example. Online spam filtering
* Repeatedly, emails arrive int othe system
* The emails are classified as spam/valid.


* $a^{t} \in \mathbb{R}^{d}$,
    * feature vector generated from an email such as bag-of-words
* $\mathcal{K} := \mathbb{R}^{d}$,
* $x^{t} \in \mathcal{K}$,
    * parameter of our filter at time when $t$-th email is recieved
* $$\mathcal{Y} := \{-1, 1\}$$,
* $\hat{y}^{t}(x^{t}, a^{t}) := \mathrm{sign}\langle x^{t}, a^{t} \rangle$,
    * our prediction model predicts whether the email is spam/valid by the sign of a hyperplane
    * $1$ means valid, and $-1$ means spam.

The cost function of email and label pair $(a, y)$ is defined as follows;

$$
\begin{eqnarray}
    x \in \mathcal{K},
    \
    f(x; a, y)
    & := &
        \ell
        (
            \hat{y}^{t}(x^{t}, a^{t}),
            y
        )
    \nonumber
    \\
    \mathcal{F}
    & \subseteq &
        \left\{
            f(\cdot; a, y)
            \mid
            a \in \mathbb{R}^{d},
            \
            y \in \mathcal{Y}
        \right\}
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Example. Online shortest paths
* $G := (V, E)$,
* $$N :=|
V
|
$$,
* $$M :=|
E
|
$$,
* $u, v \in V$,
* $$\mathcal{P}_{u, v} \subseteq E^{N}$$,
    * the set of all $u-v$ paths in the graph
* $$p_{t} \in \mathcal{P}_{u, v}$$,
    * decision maker's choice
* $w_{t, e} \in \mathbb{R} \ (e \in E)$,
    * weights of edges

weight of path $p_{t}$ is give by

$$
    \sum_{e \in p_{t}}
        w_{t, e}
    .
$$

Let $\mathcal{K} \subseteq \mathbb{R}^{M}$ be polytope, satisfies the following constraints, that is, $x \in \mathcal{K}$ if and only if

$$
\begin{eqnarray}
    \sum_{e := (u, w), w \in V}
        x_{e}
    & = &
        1
    \nonumber
    \\
    \sum_{e := (w, v), w \in V}
        x_{e}
    & = &
        1
    \nonumber
    \\
    \forall w \in V \setminus \{u, v\},
    \
    \sum_{e := (u, w) \in E}
        x_{e}
    & = &
        \sum_{e := (w, x) \in E}
            x_{e}
    \nonumber
    \\
    \forall e \in E,
    \
    x_{e}
    & \in &
        [0, 1]
    \nonumber
\end{eqnarray}
$$

The element $x \in \mathcal{K}$ stands for the distribution of the $u$-$v$-path.
The (expected) loss of the distribution is given by

$$
    x \in \mathbb{R}^{M},
    \
    f_{t}(x; w_{t})
    :=
    w_{t}^{\mathrm{T}}
    x
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Example. Portfolio selection

<div class="end-of-statement" style="text-align: right">■</div>

#### Example. Matrix completion and recommendation systems

<div class="end-of-statement" style="text-align: right">■</div>


### 1.3.3 Hedge

#### Algorithm 1 Hedge
* $\mathcal{L} := [0, 1]^{n}$,
* $W_{1} := (1, \ldots, 1) \in \mathcal{L}$,
* $I_{t} \in \{1, \ldots, n\}$,
    * categorical distribution with probability $$(W_{t, 1}/\sum_{j=1}^{n}W_{t, j}, \ldots, W_{t, n}/\sum_{j=1}^{n}W_{t, j})$$,

**Step1.** for $t=1$ to $T$ do

**Step2.** Play $I_{t}$

**Step3.** Observe loss $\ell_{t} \in \mathcal{L}$,

**Step4.** Update weights

$$
    W_{t + 1, i}
    :=
    W_{t, i}
    \exp
    \left(
        -\epsilon
        \ell_{t, i}
    \right)
    .
$$

**Step5.** end for

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 1.5
* $\mathcal{L} := [0, 1]^{n}$,
* $(l_{1}, \ldots, l_{T}) \in \mathcal{L}^{T}$,
* $W_{1} := (1, \ldots, 1) \in \mathcal{L}$,

Let

$$
\begin{eqnarray}
    t = 1, \ldots, T,
    \
    i = 1, \ldots, n,
    \
    x_{t, i}
    & := &
         \frac{
             W_{t, i}
         }{
             \sum_{j=1}^{n}
                W_{t, j}
         }
    \nonumber
    \\
    t = 1, \ldots, T,
    \
    i = 1, \ldots, n,
    \
    W_{t + 1, i}
    & := &
        W_{t, i}
        \exp
        \left(
            -\epsilon
            \ell_{t, i}
        \right)
    .
    \nonumber
\end{eqnarray}
$$

Let $$I_{t}$$ be categorical distribution with probability $x_{t}$, and $I_{1}, \ldots, I_{T}$ are independent.

Then

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{j=1}^{T}
            \ell_{t, I_{t}}
        -
        \min_{I \in \mathcal{I}_{\Delta_{n}}}
            \sum_{t=1}^{T}
                \ell_{t, I}
    \right]
    & \le &
        \epsilon
        \sum_{t=1}^{T}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
        +
        \frac{
            \log N
        }{
            \epsilon
        }
    \label{chap01_algorithm_01_expected_regret}
\end{eqnarray}
$$

where $$\mathcal{I}_{\Delta_{n}}$$ is defined in <a href="{{ site.baseurl }}/thesis/introduction_to_online_convex_optimization/notation.html#definition-independent-categorical-rvs-over-simplex">notation</a>.

#### proof
First of all, since $\ell_{t} \in \mathcal{L}$,

$$
    i^{*} \in \{1, \ldots, n\}
    \text{ s.t. }
    \mathrm{E}
    \left[
        \min_{I \in \mathcal{I}_{\Delta_{n}}}
            \sum_{t=1}^{T}
                \ell_{t, I}
    \right]
    =
    \sum_{t=1}^{T}
        \ell_{t, i^{*}}
    .
$$

Moreover,

$$
    \mathrm{E}
    \left[
        \ell_{t, I_{t}}
    \right]
    =
    \ell_{t}^{\mathrm{T}}
    x_{t}
    .
$$

Hence the equation we have to prove is equivalent to

$$
\begin{eqnarray}
    \sum_{j=1}^{T}
        \ell_{t}^{\mathrm{T}}
        x_{t}
    -
    \min_{i \in \{1, \ldots, n\}}
        \sum_{t=1}^{T}
            \ell_{t, i}
    & \le &
        \epsilon
        \sum_{t=1}^{T}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
        +
        \frac{
            \log N
        }{
            \epsilon
        }
    \nonumber
\end{eqnarray}
$$

Let

$$
\begin{eqnarray}
    \Phi_{t + 1}
    & := &
        \sum_{i=1}^{n}
            W_{t, i}
    .
    \nonumber
\end{eqnarray}
$$

We have

$$
\begin{eqnarray}
    \Phi_{t + 1}
    & = &
        \sum_{i=1}^{n}
            W_{t, i}
            \exp
            \left(
                - \epsilon
                \ell_{t, i}
            \right)
    \nonumber
    \\
    & = &
        \Phi_{t}
        \frac{1}{
            \sum_{j=1}^{n}
                W_{t, j}
        }
        \sum_{i=1}^{n}
            W_{t, i}
            \exp
            \left(
                - \epsilon
                \ell_{t, i}
            \right)
    \nonumber
    \\
    & = &
        \Phi_{t}
        \sum_{i=1}^{n}
            x_{t, i}
            \exp
            \left(
                - \epsilon
                \ell_{t, i}
            \right)
    \nonumber
    \\
    & \le &
        \Phi_{t}
        \sum_{i=1}^{n}
            x_{t, i}
            \left(
                1
                -
                \epsilon
                \ell_{t, i}
                +
                \epsilon^{2}
                (\ell_{t, i})^{2}
            \right)
        \quad
        (\because x \ge 0, e^{-x} \le 1 - x + x^{2})
    \nonumber
    \\
    & = &
        \Phi_{t}
        \left(
            1
            -
            \epsilon
            \ell_{t}^{\mathrm{T}}
            x_{t}
            +
            \epsilon^{2}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
        \right)
    \nonumber
    \\
    & \le &
        \Phi_{t}
        \exp
        \left(
            -
            \epsilon
            \ell_{t}^{\mathrm{T}}
            x_{t}
            +
            \epsilon^{2}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
        \right)
        \quad
        (\because 1 + x \le e^{x})
    .
\end{eqnarray}
$$

On the other hand, for $$ k = \{1, \ldots, n\}$$,

$$
\begin{eqnarray}
    W_{T, k}
    & \le &
        \Phi_{T}
    \nonumber
    \\
    & \le &
        \Phi_{1}
        \prod_{t=1}^{T}
        \exp
        \left(
            -
            \epsilon
            \ell_{t}^{\mathrm{T}}
            x_{t}
            +
            \epsilon^{2}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
        \right)
    \nonumber
    \\
    & = &
        N
        \exp
        \left(
            -
            \epsilon
            \sum_{t=1}^{T}
                \ell_{t}^{\mathrm{T}}
                x_{t}
            +
            \epsilon^{2}
            \sum_{t=1}^{T}
                \sum_{i=1}^{n}
                    x_{t, i}
                    (\ell_{t, i})^{2}
        \right)
    \nonumber
\end{eqnarray}
$$

Taking the logarithm of both sides we get

$$
\begin{eqnarray}
    & &
        -\epsilon
        \sum_{t=1}^{T}
            \ell_{t, k}
        \le
        \log N
        -
        \epsilon
        \sum_{t=1}^{T}
            \ell_{t}^{\mathrm{T}}
            x_{t}
        +
        \epsilon^{2}
        \sum_{t=1}^{T}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        -
        \sum_{t=1}^{T}
            \ell_{t, k}
        \le
        \frac{
            \log N
        }{
            \epsilon
        }
        -
        \sum_{t=1}^{T}
            \ell_{t}^{\mathrm{T}}
            x_{t}
        +
        \epsilon
        \sum_{t=1}^{T}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{t=1}^{T}
            \ell_{t}^{\mathrm{T}}
            x_{t}
        -
        \sum_{t=1}^{T}
            \ell_{t, k}
        \le
        \frac{
            \log N
        }{
            \epsilon
        }
        +
        \epsilon
        \sum_{t=1}^{T}
            \sum_{i=1}^{n}
                x_{t, i}
                (\ell_{t, i})^{2}
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary
In algorithm 1, expected regret is given by $$\eqref{chap01_algorithm_01_expected_regret}$$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>
