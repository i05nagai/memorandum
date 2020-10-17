---
title: Connectedness
---

## Connectedness

* $X$,
    * topological sp.

#### Definiton disjoint set
* $A$
    * set
* $B_{1} \subseteq A$,
* $B_{2} \subseteq A$,

$B_{1}, B_{2} $ is said to be disjoint set of $A$ if

$$
    B_{1} \cap B_{2} = \emptyset,
    \
    B_{1} \cup B_{2} = A.
$$

We write $B_{1} \sqcup B_{2} = A$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition disconnected
$X$ is said to be disconnected if

$$
    \exists O_{1}, O_{2} \in \mathcal{O}
    \text{ s.t. }
    O_{1} \sqcap O_{2} = X,
    .
$$

$X$ is said to be connected if

$$
    \forall O_{1}, O_{2} \in \mathcal{O},
    \
    O_{1} \cap O_{2} = \emptyset
    \Rightarrow
    O_{1} \cup O_{2} \neq X
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition separated
* $A \subseteq X$,
* $B \subseteq X$,

$X$ is said to be disconnected if

$$
    \left(
        B \cap \mathrm{cl}_{X}A
    \right)
    \cup
    \left(
        A \cap \mathrm{cl}_{X}B
    \right)
    =
    \emptyset
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 1
* $X$,
    * toplogical sp.

* (1) $\emptyset$ and $X$ are the only closed and open sets in $X$,
* (3) 

$$
    \forall O_{1}, O_{2} \in \mathcal{O}_{X},
    \
    O_{1} \neq \emptyset,
    \
    O_{2} \neq \emptyset,
    \Rightarrow
    O_{1} \sqcup O_{2} \neq X
$$

* (4) 

$$
    \forall O_{1}, O_{2} \in \mathcal{O}_{X},
    \
    O_{1} \neq \emptyset,
    \
    O_{2} \neq \emptyset,
    \
    O_{1}^{c} \sqcup O_{2}^{c} \neq X
$$

(5) $X$ is not the union of two nonempty separated sets

#### proof
(1) $\Rightarrow$ (3)

Suppose that (3) is false.
There are $$O_{1}, O_{2} \in \mathcal{O}_{X}$$ such that $$O_{1} \neq \emptyset$, $O_{2} \neq \emptyset$$, $$O_{1} \sqcup O_{2} = X$$.
However, since, $$X \setminus O_{1} = O_{2} = O_{1}^{c}$$, $O_{2}$ is closed.
Thus, $O_{2}$ is closed and open, but this contradicts to (1).

(3) $\Leftrightarrow$ (4)

Suppose that (4) is false.
There are $$O_{1}, O_{2} \in \mathcal{O}_{X}$$ such that $$O_{1}^{c} \neq \emptyset$$, $$O_{2}^{c} \neq \emptyset$$, $$O_{1}^{c} \sqcup O_{2}^{c} = X$$.

$$
    O_{1}^{c} = X \setminus O_{2}^{c},
    \
    O_{2}^{c} = X \setminus O_{1}^{c}
    .
$$

Hence $$O_{1}^{c}$$ and $$O_{2}^{c}$$ are also open.
Since $$O_{1}^{c} \sqcup O_{2}^{c} = X$$, this contradicts to (3).

The inverse is obvious from this discussion.

(4) $\Rightarrow$ (5)

Supposet that (5) is false.
There are separated sets $A, B$ such that $A \neq \emptyset$, $B \neq \emptyset$ $A \cup B = X$.
Since $$\mathrm{cl}_{X}B \cap A = \emptyset$$ and $$\mathrm{cl}_{X}B \subseteq X$$, $$\mathrm{cl}_{X}B \subseteq B$$.
Hence $B$ is closed.
Similarly, $A$ is closed.
Since $A$, $B$ is closed, this contradicts to (4).

(5) $\Rightarrow$ (1)

Suppose that (1) is false and $A$ is proper subset of $X$ and closed and open.
Since $B := X \setminus A$ is nonempty, closed and open, $\mathrm{cl}A = A$ and $\mathrm{cl}B = B$.
It follows that $(A \cap \mathrm{cl}B) \cup (\mathrm{cl}A \cap B) = \emptyset$.
Thus, $A$ and $B$ are separated sets.

<div class="QED" style="text-align: right">$\Box$</div>

#### Definition
* $X$,
* $I := [0, 1]$,
* $p, q \in X$,
* $f:I \rightarrow X$,

$f$ is said to be a path in $X$ from p to q if

* $f(0) = p$,
* $f(1) = q$,
* $f$ is continuous.

$X$ is said to be path-connected if for every point $p, q \in X$ there exists a path in $X$ from $p$ to $q$.

<div class="end-of-statement" style="text-align: right">■</div>


#### Definition path-connected
* $X$,
    * top sp

$X$ is said to be path-connected if for any points $a, b \in X$, there is a continuous map $\gamma: [0, 1] \rightarrow X$ such that 

$$
    \gamma(0) = a,
    \
    \gamma(1) = b.
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Chapter 5 Connectedness](https://www.math.wustl.edu/~freiwald/ch5.pdf)
