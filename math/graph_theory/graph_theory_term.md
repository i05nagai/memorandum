---
title: Graph Theory Term
---

## Graph Theory Term


#### Definition. Graph
* $E$,
    * finite set
* $V$,
    * finite set
* $$\Psi^{\prime}: E \rightarrow \{X \subset V \mid \abs{X} = 2\}$$,
* $$\Psi^{\prime\prime}: E \rightarrow \{(v, w) \in V \times V \mid v \neq w\}$$,

The triplet $(V, E, \Psi^{\prime})$ is called an undirected graph.
The triplet $(V, E, \Psi^{\prime\prime})$ is called a directed graph or digraph.
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

#### Definition. Parallel
* $(V, E, \Psi)$,
    * graph
* $e, e^{\prime} \in E$,
    * $e \neq e^{\prime}$,

$e, e^{\prime}$ is said to be parallel if $\Psi(e) = \Psi(e^{\prime})$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Simple
* $(V, E, \Psi)$,
    * graph

Graph $(V, E, \Psi)$ is said to be simpole if there is no parallel edge.
i.e. $\Psi$ is injection.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Bipartite
* $G := (V, E, \Psi)$,
    - graph
* $X, Y \subseteq V$,
    - $X \cap Y \eq \emptyset$,

$G$ is said to be a bipartite graph or bigraph if

$$
    \forall e \in E,
    \
    \exists u, v \in \Psi(e)
    \text{ s.t. }
    u \in X,
    v \in Y
    .
$$

We write $G[X, Y]$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Subgraph
* $G := (V(G), E(G))$,
    * graph
* $V(H) \subseteq V(G)$,
* $E(H) \subseteq E(G)$,

$H := (V(H), E(H), \Psi)$ is called subgraph of $(E, V, \Psi)$.

$G$ contain $H$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Induced graph
* $G := (V(G), E(G))$,
    * graph
* $V(H) \subseteq V(G)$,

$H$ is said to be induced subgraph of $G$ if

* $H$ is a subgraph of $G$
* $$E(H) = \{\{u, v\} \in E(G) \mid u, v \in V(H)\}$$.

In this case, $H$ is induced by $V(H)$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Operation
* $G := (V(G), E(G))$,
    * graph
* $v \in V(G)$,
* $e \in E(G)$,

We write $G - v$ for the subgraph of $G$ induced by $$V(G) \setminus \{v\}$$.

$$
\begin{eqnarray}
    V(G - v)
    & = &
        V(G) \setminus \{v\}.
    \nonumber
    \\
    E(G - v)
    & = &
        E(G) \setminus \{e \in E(G) \mid v \in e\}
    .
\end{eqnarray}
$$

We write $$G - e := (V(G), E(G) \setminus \{e\})$$.

We write $$G + e := (V(G), E(G) \cup \{e\})$$.

We write $$G + H := (V(G), E(G) \cup \{e\})$$.

$$
\begin{eqnarray}
    V(G + H)
    & = &
        V(G) \cup V(H)
    \nonumber
    \\
    E(G + H)
    & = &
        E(G) \sqcup E(H)
    \nonumber
\end{eqnarray}
$$

$E(G + H)$ may contain parallel edges.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition adjacent
* $G := (V(G), E(G))$,
    * undirected graph
* $$e := \{u, v\} \in E(G)$$,
* $e_{1}, e_{2} \in E(G)$,

The edge $e$ is called to join $v$ and $u$.

$v$ and $u$ are adjacent.

$v$ is a neighbour of $w$.

$v$ and $u$ are endpoints of $e$.

$e_{1}$ and $e_{2}$ is said to be adjacent if $e_{1} \cap e_{2} \neq \emptyset$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Spanning
* $G := (V(G), E(G))$,
    * graph
* $H := (V(H), E(H))$,
    * subgraph

$H$ is said to be spanning if $V(G) = V(H)$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. walk
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

#### Definition. Path
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

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Connected
* $G := (V(G), E(G))$,
    * undirected graph

$G$ is said to be connected if for all $v, w \in V(G)$, there is $v-w$-path.
Otherwise $G$ is disconnected.

* $G := (V(G), E(G))$,
    * digraph

A digraph $G$ is said to be connected if the underlying undirected graph is connected.

A set of vertice $V \subseteq V(G)$ is said to be connected if the induced graph is conneted.

A vertex $v \in V(G)$ is said to be an articulation vertex if $G - v$ has more connected components than $G$.

An edge $e \in E(G)$ is said to be an bridge if $G - e$ has more connected components than $G$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Forest
* $G := (V(G), E(G))$,
    * undirected graph

$G$ is said to be Forest if $G$ has no circuit.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Tree
* $G := (V(G), E(G))$,
    * Forest

$G$ is said to be tree if $G$ is connected.

<div class="end-of-statement" style="text-align: right">■</div>

##### Definition Branching
* $G := (V(G), E(G))$,
    * un directed graph

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition cut
* $G := (V(G), E(G))$,
    * un directed graph

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Edge
* $G := (V(G), E(G))$,
    * un directed graph
* $X, Y \subseteq V(G)$,

$$
\begin{eqnarray}
    E(X, Y)
    & := &
        \{
            \{x, y\} \in E(G)
            \mid
            x \in X \setminus,
            \
            y \in Y \setminus X
        \}
    \nonumber
    \\
    \delta(X)
    & := &
        E(X, V(G) \setminus X)
    \nonumber
\end{eqnarray}
    .
$$

* $G := (V(G), E(G))$,
    * directed graph
* $X, Y \subseteq V(G)$,

$$
\begin{eqnarray}
    E^{+}(X, Y)
    & := &
        \{
            (x, y) \in E(G)
            \mid
            x \in X \setminus,
            \
            y \in Y \setminus X
        \}
    \nonumber
    \\
    \delta^{+}(X)
    & := &
        E^{+}(X, V(G) \setminus X)
    \nonumber
    \\
    \delta^{-}(X)
    & := &
        \delta^{+}(V(G) \setminus X)
        =
        E^{+}(V(G) \setminus X, X)
    \nonumber
    \\
    \delta(X)
    & := &
        \delta^{+}(X)
        \cup
        \delta^{-}(X)
    \nonumber
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition degree of vertex
* $G := (V(G), E(G))$,
    * un directed graph
* $v \in V$,

$\abs{\delta(b)}$ is called the degree of a vertex $v$.

* $G := (V(G), E(G))$,
    * directed graph
* $v \in V$,

$\abs{\delta^{-}(v)}$ is called the in-degree.

$\abs{\delta^{+}(v)}$ is called the out-degree.

$\abs{\delta^{+}(v)} + \abs{\delta^{-}(v)}$ is called the degree of the vertex.

* $G := (V(G), E(G))$,
    * directed or undirected graph
* $v \in V$,
* $k \in \mathbb{N}$,

$v$ is called isolated if the degree of vertex is zero.

The graph $G$ is said to be $k$-regular if

$$
    \forall v \in V,
    \
    \abs{\delta(v)} = k.
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition neighbour
* $G := (V(G), E(G))$,
    * un directed graph
* $X \subseteq V(G)$,

The set of $X$ is defined by

$$
\begin{eqnarray}
    \Gamma(X)
    & := &
        \{
            v \in V(G) \setminus X
            \mid
            E(X, \{v\})
            \neq
            \emptyset
        \}
    \nonumber
    \\
    v \in V,
    \
    \Gamma(v)
    & := &
        \Gamma(\{v\})
    \nonumber
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition modular
* $U$,
    * finite set
* $f: 2^{U} \rightarrow \mathbb{R}$,

$f$ is said to be submodular if

$$
    X, Y \subseteq U,
    \
    f(X \cap Y)
    +
    f(X \cup Y)
    \le
    f(X) + F(Y)
    .
$$

$f$ is said to be supermodular if

$$
    X, Y \subseteq U,
    \
    f(X \cap Y)
    +
    f(X \cup Y)
    \ge
    f(X) + F(Y)
    .
$$

$f$ is said to be modular if

$$
    X, Y \subseteq U,
    \
    f(X \cap Y)
    +
    f(X \cup Y)
    =
    f(X) + F(Y)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Complete graph
* $G := (V(G), E(G))$,
    * simple undirected graph

$G$ is said to be complete graph if

$$
    \forall u, v \in V(G),
    \
    u \neq v,
    \
    \{u, v\} \in E(G)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Complete bipartite graph
- $G := (V(G), E(G))$,
    - bipartite graph
- $X, Y \subset V(G)$,
    - partites

$G$ is said to be a complete bipartite graph or complete bigraph if

$$
    \forall x \in X,
    \
    \exists y \in X
    \text{ s.t. }
    {x, y} \in E(G)
    .
$$

When $\|X\| = m$ and $\|Y\| = n$, we denote $K_{m, n}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Complement graph
* $G := (V(G), E(G))$,
    * simple undirected graph
* $H := (V(H), E(H))$,
    * graph

$H$ is said to be complement of $G$ if

* $V(G) = V(H)$ and
* $(V(G), E(G + H))$ is a complete graph
    * Recall $$E(G + H) = E(G) \sqcup E(H)$$,

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition matching
* $G := (V(G), E(G))$,
    * undirected graph
* $H \subseteq G$,
    * subgraph

$E(H)$ is said to be matching in $G$ if

$$
    \forall e_{1} := \{u_{1}, v_{1}\},
    \
    e_{2} := \{u_{2}, v_{2}\} \in X,
    \
    e_{1} \cap e_{2}
    =
    \emptyset
    .
$$

$E(H)$ is also called a set of pairwise disjoint edges.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition vertex cover
* $G := (V(G), E(G))$,
    * undirected graph
* $S \subseteq V(G)$,

$S$ is said to be a vertex cover in $G$ if

$$
    \forall e \in E(G),
    \
    \exists v \in S
    \text{ s.t. }
    v \in e
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition edge cover
* $G := (V(G), E(G))$,
    * undirected graph
* $F \subseteq V(G)$,

$F$ is said to be a edge cover in $G$ if

$$
    \forall v \in V(G),
    \
    \exists e \in E
    \text{ s.t. }
    v \in e
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition stable set
* $G := (V(G), E(G))$,
    * undirected graph
* $S \subseteq V(G)$,

$S$ is said to be a stable set in $G$ if

$$
    \forall v, u \in S,
    \
    (v, u) \notin E(G)
    .
$$

$S$ is also called a set of pairwise non-adjacent vertices.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition empty graph
* $G := (V(G), E(G))$,
    * undirected graph

$G$ is said to be empty graph if  $E(G)$ is emptyset.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition clique
* $G := (V(G), E(G))$,
    * undirected graph
* $S \subseteq V(G)$,

$S$ is said to be clique if

$$
    \forall v, u \in S,
    \
    (v, u) \in E(G)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 2.2
* $G$,
    * graph
* $X \subseteq V(G)$,
* $S := V(G) \setminus X$,
* $H$
    * a complement graph of $G$,

Then the following statements are equivalent:

* (a) $X$ is a vertex cover in $G$,
* (b) $S$ is a stable set in $G$,
* (c) $S$ is a clique in the compliment of $G$,

#### proof
(b) $\Leftrightarrow$ (c)

By definitoin of a stable set in $G$,

$$
    \forall u, v \in S,
    \
    (u, v) \notin E(G)
    .
$$

Thus,

$$
    \forall u, v \in S,
    \
    (u, v) \in E(H)
    .
$$

Converse is the same.

(a) $\Rightarrow$ (b)

Let $u, v \in S$ be fixed.
Suppose $(u, v) \in E(G)$.
By definition of a vetex cover, there exist $w \in X$ such that

$$
    v = w
    \text{ or }
    u = w
    .
$$

This contradicts to $u, v \in S$.

(b) $\Rightarrow$ (a)

Let $e := (u, v) \in E(G)$ be fixed.
Suppose that for all $w \in X$, $w \notin e$.
The endpoints of $e$ does not belong to $X$.
Hence, $u, v \in S$.
However, since $S$ is a stable set in $G$, $e \notin E(G)$.
Thus, $e$ contradicts to $e \in E(G)$.

<div class="QED" style="text-align: right">$\Box$</div>

## Reference

