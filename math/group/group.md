---
title: Group
---

## Group


#### Proposition
(1)

$$
    (aga^{-1})^{-1} = ag^{-1}a^{-1}
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Definition
- $G$,
    - group
- $S \subseteq G$,
    - subgroup

$$
    aS
    :=
    \{
        ag
        \mid
        g \in S
    \}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definitoin
- $G$,
    - gorup
- $N \subseteq G$,
    - subgroup

$N$ is said to be a normal group if

$$
    \forall n \in N, g \in G,
    \quad
    gng^{-1} \in N.
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Proposition
- $G$,
    - group
- $N \subseteq G$
    - normal subgroup
- $a \in G$,
- $n \in N$,

(1) $a^{-1}na \in N$.

(2) $aN = Na$

#### proof
(1)

By definition, $an^{-1}a^{-1} \in N$.
$N$ is group so the inverse is contained in $N$.
That is,

$$
    (an^{-1}a^{-1})^{-1}
    =
    a^{-1}na
    \in N
    .
$$

(2)

$$
    an = ana^{-1}a
$$

Here $ana^{-1} \in N$.
Hence $an \in Na$.
Similary,

$$
    na = aa^{-1}Na \in aN
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>


#### Definition commutator
- $G$,
    - group

$$
    g, h \in G,
    \quad
    [g, h] := g^{-1}h^{-1}gh
    .
$$

$[g, h]$ is called commutator of $g, h$.

$$
    [G, G]
    :=
    \{
        [g_{1}, h_{1}] \cdots [g_{n}, h_{n}]
        \mid
        n \in \mathbb{N},
        \
        g_{i}, h_{i} \in G
    \}
    .
$$

$[G, G]$ is called the commutator group of $G$.

<div class="end-of-statement" style="text-align: right">■</div>


#### Propositon
- $G$,
    - group
- $g, h \in G$,
- $a \in G$,

(1) $a[g, h]a^{-1} = [aga^{-1}, aha^{-1}]$

(2) $[G, G]$ is the smallest normal subgroup


#### proof
(1)

$$
\begin{eqnarray}
    [aga^{-1}, aha^{-1}]
    & = &
        (aga^{-1})^{-1}(aha^{-1})^{-1}aga^{-1}aha^{-1}
    \nonumber
    \\
    & = &
        ag^{-1}a^{-1}ah^{-1}a^{-1} aga^{-1}aha^{-1}
    \nonumber
    \\
    & = &
        ag^{-1}h^{-1}gha^{-1}
    \nonumber
    \\
    & = &
        a[g, h]a^{-1}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
