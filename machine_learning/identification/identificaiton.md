---
title: Identification
---

## Identification
Here, we outline common concepts related to identification problems, including address standardization and preprocessing of the data.
In this mathematical model, address standardization can be viewed as a special case of identification problems, and preprocessing is a technique to reduce the computational complexity of such problems.

#### Definition1 Identification problem
- $X$,
    - set
- $I \subseteq X$,
    - set

An identification probelm for the pair $(X, I)$ is a task of finding a map $f: X \rightarrow I$ such that

$$
    \exists \{X_{i}\}_{i \in I}
    \text{ s.t. }
    \bigsqcup_{i \in I} X_{i} = X,
    \
    f(X_{i}) = \{i\}
    \quad
    \forall i \in I
    .
$$

If there exists a pair $$(f, \sqcup_{i \in I}X_{i})$$ satisfying these conditions, we say that the identification problem is identifiable, and identifiable identification problem.
Such a pair $$(f, \sqcup_{i \in I}X_{i})$$ is called an identifier.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark1
If the $I = X$, there is a trivial identiifer

$$
    X_{i} = \{i\}
    \quad
    i \in I
    .
$$

Thus, we are primarily interested in $I \subset X$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition1
- $X$,
    - set
- $I \subseteq X$,
    - set

An identification problem of $(X, I)$ is identifiable if and only if there is a equivalent relation $\sim$ such that

$$
    X / \sim
    =
    \{
        [x_{i}]
        \mid
        i \in I
    \}
    .
$$

#### proof
(if part)

$[x_{i}]$ and $[x_{j}]$ are disjoint if and only if $i \neq j$.
Obviously, union of $[x_{i}]$ for all $i$ is equal to $X$.
Therefore, we can construct the disjoint sets by taking $X_{i} := [x_{i}]$ and the map is $$f(X_{i}) := \{i\}$$.

(only if part)

We define $\sim$ on $X$ by

$$
    x \sim x^{\prime}
    \iff
    x, x^{\prime} \in X_{i}
    \quad
    \text{ for some }i
    .
$$

This is a equivalent relation.
Indeed, the reflexivity an the symmetry holds.
Let

$$
    x \sim y,
    \
    y \sim z
    .
$$

If $x$ and $z$ is not in the same set, $y$ is included in two different disjoint sets.
Thus, $x \sim z$.

<div class="QED" style="text-align: right">$\Box$</div>

Practically, $X$ is a finite set so there is a bijective map from $I$ to some subset of natural numbers $F \subseteq \mathbb{N}$.
$f$ can be interpreted as a map from an input to an ID.

Frequently, $X$ is a direct product of serveral attributes, $X = A_{1} \times \cdots \times A_{N}$ where each $A_{i}$ is some finte set.
In this setting, the identification problem often involves combining or matching these attributes to produce a single label from $I$.

#### Example1
Address standardization is a special case of identification problems.
Let $X = A_{1}$ and $I \subseteq X$ be a finite set.
$I$ is a set of standardized addresses.
$X$ is a set of arbitrary formats of address input.
The goal is to construct a map $f: X \rightarrow I$ that takes an arbitrary input address to its standardized form. This exactly matches our definition of an identification problem.
<div class="end-of-statement" style="text-align: right">■</div>

In practice, the input space $X$ may lack sufficient information to map each input to a unique element of I.
In such scenarios, an exact identifier may not exist. We therefore relax our requirements and talk about identification models instead of full identifiers.

#### Definition2 Identification model
- $X$,
    - set
- $I \subseteq X$,
    - set
- $Y \subseteq X$,
    - set
- $J \subseteq I$,

Let $Y = \sqcup_{j \in J}Y_{j}$ partition of the $Y$, and $g: Y \rightarrow J$.
The pair $(g, \sqcup_{j \in J}Y_{j})$, is called an identifiaiton model.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark2
An identifier $(f, \sqcup_{i \in I}X_{i})$ is an identification model.

<div class="end-of-statement" style="text-align: right">■</div>


#### Example2 Finite input space
- $X := A_{1} \times \cdots \times A_{n}$,
    - where $A_{i}$ is finite set
- $Y := B_{1} \times \cdots \times B_{n}  \subseteq X$,
- $I := I_{1} \times \cdots \times I_{n} \subseteq X$,
- $J \subseteq I$,

$Z := X \setminus Y$ is a set which the model cannot identifies.
Let $(g, \sqcup_{i \in J}Y_{i})$ be an identification model.

$$
    J^{\prime}
    :=
    \{
        j
        \in
        J
        \mid
        f(X_{j})
        \neq
        g(Y_{j})
    \}
$$

captures the inputs for which the model’s output does not match the true identifier $f$.

Supopse that $f_{i}$ is an identifier for $(A_{i}, I_{i})$.
That is, $f_{i}: A_{i} \rightarrow I_{i}$, $$f(A_{i,k}) = \{k\}$$ for all $k \in I_{i}$.
An identifier $f: X \rightarrow I$, can be constructed by

$$
    (a_{1}, \ldots, a_{n}) \in X,
    \
    f(a_{1}, \ldots, a_{n})
    :=
    (f_{1}(a_{1}), \ldots, f_{n}(a_{n}))
    .
$$

$$
    X_{i_{1}, \ldots, i_{n}}
    :=
    A_{1,k_{1}}
    \times
    \cdots
    \times
    A_{n,k_{n}}
    \quad
    k_{l} \in I_{l}.
$$

Clearly, $$X_{i_{1}, \ldots, i_{n}}$$ are disjoint then partion of $X$ and $f$ satifies the identifier condition.

<div class="end-of-statement" style="text-align: right">■</div>


## Reference

