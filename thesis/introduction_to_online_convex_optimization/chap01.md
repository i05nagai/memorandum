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
