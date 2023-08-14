---
title: Characterizing degree-sum maximal nonhamiltonian bipartite graphs
---

## Characterizing degree-sum maximal nonhamiltonian bipartite graphs


#### Definition
- $G[X, Y]$,
    - bipartite graph
- $X, Y$,
    - partite sets

$G$ is said to be balanced if $\|X\| = \|Y\|$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition
- $P$,
    - path
- $x, y \in G$,
    - vertex

$xPy$ denote the path from $x$ to $y$ on $P$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Defitnion

$$
    sigma_{2}(G)
    :=
    \min
    \{
        d_{G}(x) + d_{G}(y)
        \mid
        (x, y) \notin E(G)
    \}
    .
$$

If $G[X, Y]$ is a bipartite graph,

$$
    sigma_{2}^{2}(G[X, Y])
    :=
    \{
        d_{G}(x) + d_{G}(y)
        \mid
        (x, y) \notin E(G),
        x \in X,
        y \in Y
    \}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition

$$
    1 \le t \le n - 1,
    \
    H_{t, n-t}
    :=
    K_{t, t}
    \cup
    K_{n-t, n-t}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition
- $n \ge 3$,
- $G$,
    - nonhamiltonian graph
- $\sigma_{2}(G) = n -1$,

$G$ is either

- (1) two complete graphs intersecting in a single vertex
- (2) $$K_{\frac{n - 1}{2}, \frac{n+1}{2}} \subseteq G \subseteq K_{\frac{n-1}{2}} K_{\frac{n+1}{2}$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem 1 
-$n \in N$,
- $G$,
    - balanced bipartite graph
    - $\|V(G)\| = 2n$,
    - $2n \ge 4$

If $\sigma_{2}^{2}(G) > n$, $G$ is hamiltonian.

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem 2
- $G$
    - a balanced nonhamiltonian bigraph
    - $\|V(G)\| = 2n$,

If $\sigma_{2}^{2}(G) = n$, $G$ is one of 

- (1) $G_{1}$,
- (2) $G_{2}$,
- (3) $K_{t,t} \cup K_{n-t,n-t} \subseteq G \subseteq H_{t, n-t}$,

with $1 \le t \le n - 1$.

#### proof



<div class="QED" style="text-align: right">$\Box$</div>


## Reference
