---
title: Matching
---

## Matching

#### Bipartite graph
- $G = (V, E)$,
    - graph
- $X, Y \subseteq V$,
    - $X \cap Y = \emptyset$

$G$ is said to be a bipartite graph if

$$
    \forall (u, v) \in E,
    \quad
    u \in X, v \in Y
    \text{ or }
    v \in X, u \in Y
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Matching
- $G = (V, E)$,
    - graph
- $M \subseteq E$,

$M$ is said to be a matching if all edges in $M$ is non-adjacent edge, that is,

$$
    \forall (u_{1}, v_{1}) \in M,
    \
    \forall (u_{2}, v_{2}) \in M,
    \quad
    u_{1} \neq u_{2}, v_{2},
    \
    v_{1} \neq u_{2}, v_{2},
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Perfect matching
- $G = (X, Y, E)$,
- $M \subseteq E$,

$M$ is said to be a pefect matcihng if

- $M$ is a matching
- $M$ covers all vertexes.

<div class="end-of-statement" style="text-align: right">■</div>

#### Hall's theorem
- $G = (X, Y, E)$,
    - bipartite graph

$G$ has a perfect matching if and only if

$$
    \forall W \ubseteq X,
    \| W \|
    \leq
    \| N_{G}(W) \|
$$

where $N_{G}(W)$ is a set of neighbors of $W$.

#### proof

only if part

Let $W$ be a subset of $X$.
$G$ has a perfect matching $M$.
For every $w$ in $W$, there is an edge in $M$ whose endpoint is $w$.
Hence

$$
    \| W \|
    \le
    N_{G}(W)
    .
$$

if part.

We prove the contrapositive: if there is no perfect matching, then there is a $W \subseteq X$ such that $\|W\| \ge \|N_{G}(W)\|$.
Let $M$ be the maximum matching of $G$.
There is a vertex $u \in X$ which is not coverted by $M$.
Consider all alternative paths from $u$ and denote $W$, $Z$ as a set of vertexes of the alterntive paths in $X$ and $Z$ respectively.

Every $v \in Z$ is covered by $M$.
Let $p = (w_{1} = u, w_{2}, \ldots, w_{n})$ be an alternative path.
If $w_{2}$ is not in $M$, 

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
