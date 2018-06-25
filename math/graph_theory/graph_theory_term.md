---
title: Graph Thery Term
---

## Graph Thery Term


### Definition. Graph
* $E$,
    * finite set
* $V$,
    * finite set
* $$\Psi^{\prime}: E \rightarrow \{X \subset \mid |X| = 2\}$$,
* $$\Psi^{\prime\prime}: E \rightarrow \{(v, w) \in V \times V \mid v \neq w\}$$,

The triplet $(V, E, \Psi^{\prime})$ is called an undirected graph.
The triplet $(V, E, \Psi^{\prime\prime})$ is called a directed graph.
The tripplet $(V, E, \Psi)$ is called if directed or undirected gprah.

We write graph by $G := (V(G), E(G))$, where

$$
\begin{eqnarray}
    V(G)
    & := &
        V
    \nonumber
    \\
    E(G)
    & \subseteq &
        \{
            X \subseteq V(G)
            \mid
            |X| = 2
        \},
    \text{ or }
    E(G)
    & \subseteq &
        V(G) \times V(G)
    .
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Parallel
* $(V, E, \Psi)$,
    * graph
* $e, e^{\prime} \in E$,
    * $e \neq e^{\prime}$,

$e, e^{\prime}$ is said to be parallel if $\Psi(e) = \Psi(e^{\prime})$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Simple
* $(V, E, \Psi)$,
    * graph

Graph $(V, E, \Psi)$ is said to be simpole if there is no parallel edge.
i.e. $\Psi$ is injection.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Subgraph
* $G := (V(G), E(G))$,
    * graph
* $V(H) \subseteq V(G)$,
* $E(H) \subseteq E(G)$,

$H := (V_{H}, E_{H}, \Psi)$ is called subgraph of $(E, V, \Psi)$.
$G$ contain $H$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Spanning
* $G := (V(G), E(G))$,
    * graph
* $H := (V(H), E(H))$,
    * subgraph

$H$ is said to be spanning if $V(G) = V(H)$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. walk
* $G := (V(G), E(G))$,
    * graph

The sequennce $$W := (v_{1}, e_{1}, v_{2}, \ldots, v_{k}, e_{k}, v_{k+1})$$ is said to be edge progression $W$ in $G$ from $v_{1}$ to $v_{k+1}$ if

$$
\begin{eqnarray}
    e_{i}
    & = &
        (v_{i}, v_{i+1})
        \in E(G)
    \nonumber
    \\
    e_{i}
    & = &
        \{v_{i}, v_{i+1}\}
        \in E(G)
    .
    \nonumber
\end{eqnarray}
$$

The edge progression $W$ in $G$ from $v_{1}$ to $v_{k+1}$ is said to be if for all $1 \le i < j \le k$, $e_{i} \neq e_{j}$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Path
* $G := (V(G), E(G))$,
    * graph
* $$P := (\{v_{1}, \ldots, v_{k+1}\}, \{e_{1}, \ldots, e_{k}\})$$,
    * subgraph

$P$ is said to be a path if $$(v_{1}, e_{1}, v_{2}, \ldots, v_{k}, e_{k}, v_{k+1}))$$ is a walk.

$$
    \forall 1 \le i < j < \le k + 1,
    \
    v_{i} \neq v_{j}
    .
$$

$v_{i} \neq v_{j}$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Connected
* $G := (V(G), E(G))$,
    * undirected graph

$G$ is said to be connected if for all $v, w \in V(G)$, there is $v-w$-path.
Otherwise $G$ is disconnected.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Forest
* $G := (V(G), E(G))$,
    * undirected graph

$G$ is said to be Forest if $G$ has no circuit.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Tree
* $G := (V(G), E(G))$,
    * Forest

$G$ is said to be tree if $G$ is connected.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference

