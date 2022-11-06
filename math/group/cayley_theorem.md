---
title: Cayley's theorem
---

## Cayley's theorem

- $G$,
    - group
- $\mathrm{Sym}(G)$,
    - symetric group

$$
    \mathrm{Sym}(G)
    :=
    \{
        f: G \rightarrow G
        \mid
        f: \text{bijection}
    \}
    .
$$

$$
    g \in G,
    \quad
    l_{g}: G \rightarrow G,
    \quad
    l_{g}(x) := g x
    \quad
    (x \in G)
    .
$$

Obviously, $l_{g} \in \mathrm{Sym}(G)$.

$$
    K: G \rightarrow \mathrm{Sym}(G),
    \quad
    K(g) := l_{g}
    .
$$

Then for each $G$, there is a subgroup $A \subseteq \mathrm{Sym}(G)$ and ismorhism $f: G \rightarrow A$.


#### proof
TBA

<div class="QED" style="text-align: right">$\Box$</div>



- $\mathrm{Grp}$,
    - group category
- $K: \mathrm{Grp} \rightarrow \mathrm{Set}$,
    - functor

$$
\begin{eqnarray}
    KG
    & := &
        \mathrm{Sym}(G)
    \nonumber
    \\
    f: G \rightarrow G^{\prime} \in \mathrm{Grp},
    \quad
    Kf: \mathrm{Sym}(G) \rightarrow \mathrm{Sym}(G^{\prime}),
    \quad
    f^{\prime}: G \rightarrow G,
    \
    (Kf)(f^{\prime})
    & := &
        f \circ f^{\prime}
    \nonumber
    .
\end{eqnarray}
$$



## Reference
- [Cayley's theorem \- Wikipedia](https://en.wikipedia.org/wiki/Cayley%27s_theorem)
