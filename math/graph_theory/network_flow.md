---
title: Network flow
---

## Network flow
* $(V(G), E(G))$,
    * digraph
* $u: E(G) \rightarrow \mathbb{R}_{\ge 0}$,
    * edge capacities
* $s \in V(G)$,
    * the source
* $t \in V(G)$,
    * the sink
* $(G, u, s, t)$,
    * network

#### Definition 8.1
* $(G, u, s, t)$,
    * network
* $f: E(G) \rightarrow \mathbb{R}_{\ge 0}$

$f$ is said to be flow if

$$
    \forall e \in E(G),
    \
    f(e) \le u(e)
    .
$$

For $v \in V(G)$, the excess of $f$ at $v$ is defined as

$$
    \mathrm{ex}_{f}(v)
    :=
    \sum_{e \in \delta^{-}}
        f(e)
    -
    \sum_{e \in \delta^{+}}
        f(e)
    .
$$

For $v \in V(G)$, a flow $f$ is said to satisfy the flow conservation rule at vertex $v$ if

$$
    \mathrm{ex}_{f}(v) = 0
    .
$$

A flow $f$ is said to be circulation if for every vertex $f$ satisfies the flow conservation rule.

A flow $f$ is said to be $s$-$t$-flow if

$$
\begin{eqnarray}
    & &
        \mathrm{ex}_{f}(s) \le 0,
    \nonumber
    \\
    & &
        v \in V(G) \setminus \{s, t\},
        \
        \mathrm{ex}_{f}(v) = 0,
    \nonumber
\end{eqnarray}
$$

The value of $s$-$t$-flow is defined as

$$
    \mathrm{value}(f)
    :=
    -\mathrm{ex}_{f}(s)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Maximum flow problem

$$
\begin{align}
    \max
    & & &
        \sum_{e \in \delta^{+}(s)}
            x_{e}
        -
        \sum_{e \in \delta^{-}(s)}
            x_{e}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \sum_{e \in \delta^{+}(v)}
            x_{e}
        =
        \sum_{e \in \delta^{-}(v)}
            x_{e}
        &
        (v \in V(G) \setminus \{s, t\})
    \nonumber
    \\
    & & &
        x_{e} \le u(e)
        &
        (e \in E(G))
    \nonumber
    \\
    & & &
        x_{e} \ge 0
        &
        (e \in E(G))
    \nonumber
\end{align}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition 8.4
* $G$,
    * digraph
* $e := (u, w) \in E(G)$,
* $u: E(G) \rightarrow \mathbb{R}_{\ge 0}$,
    * edge capacities
* $f: E(G) \rightarrow \mathbb{R}_{\ge 0}$,
    * flow

$$
\begin{eqnarray}
    \overleftarrow{e}
    & := &
        (w, u)
    \nonumber
    \\
    \overleftrightarrow{G}
    & := &
        (V(G), E(G) \sqcup \{\overleftarrow{e} \mid e \in E(G)\})
    .
\end{eqnarray}
$$

Note that if $e := (u, w), e^{\prime}:= (w, u) \in E(G)$, then $\overleftarrow{e}, \overleftarrow{e^{\prime}} \in E(\overleftrightarrow{G})$ are parallel edges.

Resicual capacities $u_{f}: E(\overleftrightarrow{G}) \rightarrow \mathbb{R}_{\ge 0}$ is defined as

$$
    u_{f}(e)
    :=
    \begin{cases}
        u(e)
        -
        f(e)
        &
            (e \in E(G))
        \\
        f(e)
        &
            \text{otherwise}
    \end{cases}
    .
$$

The residual graph $G_{f}$ is defined as

$$
    G_{f}
    :=
    (
        V(G), \{e \in E(\overleftrightarrow{G}) \mid u_{f}(e) > 0\}
    )
    .
$$

* $P$,
    * a path or circle in $G_{f}$,
* $\gamma \in \mathbb{R}$,
* $f^{\prime}: E(\overleftrightarrow{G}) \rightarrow \mathbb{R}$

$f^{\prime}$ is said to argment $f$ along $P$ by $\gamma$ if

$$
    e \in E(P),
    \
    f^{\prime}(e)
    :=
    \begin{cases}
        f(e) + \gamma,
        &
            (e \in E(G))
        \\
        f(e) - \gamma
        &
            (e = \overleftarrow{v} \text{ for some } v \in E(G))
    \end{cases}
    .
$$

* $(G, u, s, t)$,
    * a network
* $f$,
    * $s$-$t$-flow

$s$-$t$-path in the residual graph $G_{f}$ is called $f$-augmenting path.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
