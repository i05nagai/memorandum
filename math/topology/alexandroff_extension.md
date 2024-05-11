---
title: Alexandroff Extension
---

## Alexandroff Extension

#### Theorem
- $(X, \mathcal{O}_{X})$,
    - top. space
- $$X^{*} := X \cup \{\infty\}$$,

$$
\begin{eqnarray}
    \mathcal{T}
    & := &
        \{
            (X \setminus C) \cup \{\infty\}
            \mid
            C \subseteq X: \text{ compact and closed}
        \},
    \nonumber
    \\
    \mathcal{O}^{*}
    & := &
        \mathcal{T}
        \cup
        \mathcal{O}_{X}
    .
    \nonumber
\end{eqnarray}
$$

$$(X^{*}, \mathcal{O}^{*})$$ is a topological space.
Moreover,

(1) The embedding $$c: X \rightarrow X^{*}$$ is continuous and $c(X)$ is open in $X^{*}$.

(2) $X^{*}$ is compact

(3) If $X$ is not compact, $c(X)$ is dense in $X^{*}$

(4) $X^{*}$ is Hausdorff if and only if $X$ is Hausdorff and locally compact

(5) $X^{*}$ is $T_{1}$ if and only if $X$ is $T_{1}$

(6) $(X, \mathcal{O}_{X})$ is a subspace of $X^{*}$ with the subspace topology.

#### proof
First of all,

$$
\begin{eqnarray}
    \mathcal{A}
    & := &
        \{
            A \subseteq X^{*}
            \mid
            X^{*} \setminus A: \text{ closed and compact in } X
        \}
    \nonumber
    \\
    \mathcal{O}^{*}
    & = &
        \mathcal{O}_{X}
        \cup
        \mathcal{A}
    .
    \nonumber
\end{eqnarray}
$$

Indeed, if $A \in \mathcal{T}$,

$$
\begin{eqnarray}
    X^{*} \setminus A
    & = &
        X^{*} \setminus ((X \setminus C) \cup \{\infty\})
    \nonumber
    \\
    & = &
        X \setminus (X \setminus C)
    \nonumber
    \\
    & = &
        C
    .
    \nonumber
\end{eqnarray}
$$

If $A \in \mathcal{A}$,

$$
\begin{eqnarray}
    A
    & = &
        X^{*} \setminus (X^{*} \setminus A)
    \nonumber
    \\
    & = &
        (X \cup \{\infty\}) \setminus (X^{*} \setminus A)
    \nonumber
    \\
    & = &
        (X \setminus (X^{*} \setminus A)) \cup (\{\infty\} \setminus (X^{*} \setminus A))
    \nonumber
    \\
    & = &
        (X \setminus (X^{*} \setminus A)) \cup \{\infty\}
    \nonumber
\end{eqnarray}
$$

where the third euqality holds $A$ always contians $$\{\infty\}$$.

(6)

If $A \in \mathcal{O}^{*}$,

$$
\begin{eqnarray}
    A \cap X
    & = &
        ((X \setminus A) \cap \{\infty\}) \cap X
    \nonumber
    \\
    & = &
        (X \setminus A) \cap X
    \nonumber
    \\
    & = &
        (X \setminus A)
        \in \mathcal{O}_{X}
    .
    \nonumber
\end{eqnarray}
$$

$\mathcal{O}_{X}$ is a subspace topology of $X^{*}$ if $$X^{*}$$ is a topological space.

($X^{*}$ is Topology)

Obviously, $$X^{*}, \emptyset \in \mathcal{O}^{*}$$

Let $A_{i} \in \mathcal{O}^{*}$ $(i = 1, \ldots, N)$.
And show $$\cap_{i} A_{i} \in \mathcal{O}^{*}$$.
If $$A_{i} \in \mathcal{O}_{X}$$ for all $i$, it's obvious.
If $A_{i} \in \mathcal{T}$ for all $i$,

$$
\begin{eqnarray}
    \cap_{i} (X \setminus C_{i} \cup \{\infty\})
    & = &
         \cap_{i}(X \setminus C_{i}) \cup \cap_{i}(\{\infty\})
    \nonumber
    \\
    & = &
         (X \setminus \cap_{i} C_{i}) \cup \{\infty\}
    \nonumber
    \\
    & = &
         (X \setminus \cap_{i} C_{i}) \cup \{\infty\}
    \nonumber
\end{eqnarray}
$$

For the finite intersection of the comapct set is compact, so $\cap_{i} C_{i}$ is compact.
$\cap_{i} C_{i}$ is closed so the finite intersection of $A_{i}$ is $\mathcal{T}$.

$$
\begin{eqnarray}
    A_{1} \cap A_{2}
    & = &
        ((X \setminus C_{1}) \cup \{\infty\})
        \cap
        A_{2}
    \nonumber
    \\
    & = &
        (X \setminus C_{1}) \cap A_{2}
        \in
        \mathcal{O}_{X}
    \nonumber
\end{eqnarray}
$$

Thus, the finite intersection of $A_{i} \in \mathcal{O}^{*}$ is in $\mathcal{O}$.

Let $$A_{i} \in \mathcal{O}^{*}$$ for all $i$.
We will show that $$\cup_{i} A_{i} \in \mathcal{O}^{*}$$.

If $A_{i} \in \mathcal{A}$, $\cup_{i} A_{i} \in \mathcal{A}$.
Inded,

$$
    X^{*} \setminus \cup_{i} A_{i}
    =
     \cap_{i} (X^{*} \setminus A_{i})
    .
$$

The RHS is the intersection of closed sets so the RHS is closed.
For some $j$,

$$
    X^{*} \setminus \cup_{i} A_{i}
    \subseteq
    X^{*} \setminus A_{j}
    .
$$

The closed subset of the compact set is compact so the LHS is compact.
If $A_{1} \in \mathcal{A}$ and $A_{2} \in \mathcal{O}_{X}$,

$$
\begin{eqnarray}
    X^{*} \setminus (A_{1} \cup A_{2})
    & = &
        (X^{*} \setminus A_{1})
        \cap
        (X^{*} \setminus A_{2})
    \nonumber
    \\
    & = &
        (X \setminus A_{1})
        \cap
        (X^{*} \setminus A_{2})
    \nonumber
    \\
    & = &
        (X \setminus A_{1})
        \cap
        (X \setminus A_{2})
    \nonumber
\end{eqnarray}
$$

then it is closed. Thus, it's compact as well.
Finally, $A_{i} \in \mathcal{O}^{*}$ is either in $\mathcal{A}$ or $\mathcal{O}_{X}$.
So

$$
    \bigcup_{i} A_{i}
    =
    \bigcup_{i} A_{i}
    \cup
    \bigcup_{i} A_{i}
    .
$$

The first term in $\mathcal{A}$ and the second term in $\mathcal{O}_{X}$.
This is the case of the two union.

(2)

($\Rightarrow$)

Let $$U_{i} \in \mathcal{O}^{*} $$ be a open cover of $X^{*}$.
There is a $U_{k}$ such that $$\{\infty\} \in U_{k}$$.
That is, $U_{k} \in \mathcal{A}$.
By the definition, $$X^{*} \setminus U_{k}$$ is compact and closed in $X$.

Let

$$
    U_{i}^{\prime}
    :=
    U_{i} \setminus \{\infty\}
    =
    S \cap U_{i}
    \in \mathcal{O}_{X}
    .
$$

$U_{i}^{\prime}$ is an open cover of $X$.
There is a finite open cover $$U_{j}^{\prime}$$ of $X^{*} \setminus U_{k}$.
Thus,

$$
    \bigcup_{j} U_{j}
    \cup
    U_{k}
$$

is an finite open cover of $X^{*}$.

(4)

We show if $X$ is locally compact and Hasudorff, $$X^{*}$$ is Hausdorff.
Let $$x, y \in X^{*}$$ and $x \neq y$.

If $x, y \in X$, there are neighbors which separate $x, y$.

Let $x \in X$ and $$y = \infty$$.
Since $X$ is locally compact, there is a compact neighbor $U$ of $x$.
Since $X$ is Hausodorff, $U$ is closed.
That is, $X^{*} \setminus U \in \mathcal{A}$.
It's separated by $U$ and $$X^{*} \setminus U$$.


($\Leftarrow$)

We show if $$X^{*}$$ is Hausdorff, $X$ is locally compact and Hausdorff.
Since $X$ is supace of $$X^{*}$$ which is Hausdorff.
Hence $X$ is Hausdorff.

Let $x \in X$.
Since $X^{*}$ is Hausdorff, there are neighbors $U$ and $V$ of $x$ and $\infty$ in $$X^{*}$$ such that $U \cap V = \emptyset$.

$$
    \mathrm{cl}_{X^{*}}(U)
    \cap
    V
    =
    \emptyset
    .
$$

This implies $$\infty \notin \mathrm{cl}_{X^{*}}(U)$$.
Hence $$\mathrm{cl}_{X^{*}}(U) \subseteq X$$.

Since $$X^{*}$$ is Hausdorff and $$\mathrm{cl}_{X^{*}}(U)$$ is closed, $$\mathrm{cl}_{X^{*}}(U)$$ is compact in $$X^{*}$$.
$X$ is subspace of $X^{*}$ so $$\mathrm{cl}_{X^{*}}(U)$$ is compact in $X$.

Thus, $$\mathrm{cl}_{X^{*}}(U)$$ is a compact neighbor of $x$ in $X$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Example
- $(\mathbb{Q}, \mathcal{O})$,
    - topological space with subspace topolgy of $\mathbb{R}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Example
- $(\mathbb{Q}, \mathcal{O})$,
    - topological space with subspace topolgy of $\mathbb{R}$.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference 
