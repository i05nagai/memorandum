---
title: Sigma-algebra
---

## Sigma-algebra


#### Proposition 1

$$
\begin{eqnarray}
    \mathcal{A}
    :=
    \{
        A_{1} \times \cdots \times A_{n}
        \mid
        A_{i} \in \mathcal{B}(\mathbb{R})
    \}
    .
\end{eqnarray}
$$

(1)

$$
\begin{eqnarray}
    A
    & := &
        A_{1} \times \cdots \times A_{n} \in \mathcal{A},
    \nonumber
    \\
    B
    & := &
        B_{1} \times \cdots \times B_{n} \in \mathcal{A},
    \nonumber
    \\
    A \cap B
    & = &
        (A_{1} \cap B_{1}) \times \cdots \times (A_{n} \cap B_{n})
    \nonumber
    \\
    A^{c}
    & = &
        A_{1}^{c} \times \cdots \times A_{n}^{c}
    \nonumber
\end{eqnarray}
$$

(2)

$$
\begin{eqnarray}
    A
    & := &
        A_{1} \times \cdots \times A_{n} \in \mathcal{A},
    \nonumber
    \\
    B
    & := &
        B_{1} \times \cdots \times B_{n} \in \mathcal{A},
    \nonumber
    \\
    A \cap B
    & \in &
        \mathcal{A}
    \nonumber
    \\
    A^{c}
    & \in &
        \mathcal{A}
    \nonumber
    \\
    A \cup B
    & \in &
        \mathcal{A}
    \nonumber
\end{eqnarray}
$$


#### proof

**proof of (1)**

$$
\begin{eqnarray}
    & &
        (a_{1}, \ldots, a_{n}) \in (A \cap B)
    \nonumber
    \\
    & \Leftrightarrow &
        a_{i} \in A_{i},
        a_{i} \in B_{i},
    \nonumber
    \\
    & \Leftrightarrow &
        a_{i} \in (A_{i} \cap B_{i}),
    \nonumber
    \\
    & \Leftrightarrow &
        (a_{1}, \ldots, a_{n}) \in (A_{1} \cap B_{1}) \times \cdots \times (A_{n} \cap B_{n}),
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        (a_{1}, \ldots, a_{n}) \in A^{c}
    \nonumber
    \\
    & \Leftrightarrow &
        a_{i} \notin A_{i}
    \nonumber
    \\
    & \Leftrightarrow &
        a_{i} \in A_{i}^{c}
    \nonumber
    \\
    & \Leftrightarrow &
        (a_{1}, \ldots, a_{n}) \in A_{1}^{c} \times \cdots \times A_{n}^{c}
    \nonumber
\end{eqnarray}
$$

**proof of (2)**

These are Immediate consequence from (1).

<div class="QED" style="text-align: right">$\Box$</div>

#### Remark
Note that

$$
\begin{eqnarray}
    (a_{1}, \ldots, a_{n}) \in A \cup B
    & = &
        \left(
            \bigcap_{i \in [1:n]} (a_{i} \in A_{i})
        \right)
        \cup
        \left(
            \bigcap_{i \in [1:n]} (b_{i} \in B_{i})
        \right)
    \nonumber
    \\
    & = &
        \bigcap_{i \in [1:n]}
            \left(
                (a_{i} \in A_{i})
                \cup
                \left(
                    \bigcap_{j \in [1:n]}
                        (b_{j} \in B_{j})
                \right)
            \right)
    \nonumber
    \\
    \nonumber
    \\
    & = &
        \bigcap_{i \in [1:n]}
        \bigcap_{j \in [1:n]}
            \left(
                (a_{i} \in A_{i})
                \cup
                (b_{j} \in B_{j})
            \right)
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 2
* $S$,
    * set
* $\mathcal{A}$,
    * set of subsets of $S$
* $A^{c}$,
    * complement of $A$,
    * $A \subseteq S$,
* $A^{cc} = A$,
    * $A \subseteq S$,

$$
\begin{eqnarray}
    \mathfrak{M}
    & := &
        \left\{
            \bigcap_{i \in \mathbb{N}}
                A_{i}^{k_{i}}
            \mid
            A_{i} \in (\mathcal{A} \cup \{S\}),
            \
            k_{i} \in \{c, cc\}
        \right\}
        .
    \nonumber
    \\
    \mathcal{F}
    & := &
        \left\{
            \bigcup_{i \in \mathbb{N}}
                B_{i}^{k_{i}}
            \mid
            B_{i} \in \mathfrak{M},
            \
            k_{i} \in \{c, cc\}
        \right\}
    \nonumber
\end{eqnarray}
$$

Then

$$
    \sigma(\mathcal{A})
    =
    \mathcal{F}
    .
$$

TODO: reconsider statement.

#### proof


$$
\begin{equation}
    B_{i} \in \mathfrak{M}
    \Rightarrow
    B_{i},
    (B_{i})^{c}
    \in
    \mathcal{F}
    \label{proposition_02_equation_01}
    .
\end{equation}
$$

($\subseteq$)

By definition, $\mathcal{A} \subseteq \mathcal{F}$.
If $\mathcal{F}$ is $\sigma$-algebra, the inclusion holds.

(1) $S, \emptyset \in \mathcal{F}$.

Indeed, by definiton, $S \in \mathcal{F}$.
Hence

$$
    \bigcup_{i \in \mathbb{N}} S^{c}
    \bigcap_{i \in \mathbb{N}} S^{c}
    =
    \emptyset
    \in
    \mathcal{F}
    .
$$

(2) $A \in \mathcal{F} \Rightarrow A^{c} \in \mathcal{F}$.

Indeed, let

$$
\begin{eqnarray}
    \bigcup_{i \in \mathbb{N}}
    \left(
        B_{i}
    \right)^{l_{i}}
    & \in &
        \mathcal{F}
    \nonumber
    \\
    \bigcap_{j \in \mathbb{N}}
        A_{i,j}^{k_{i,j}}
    & =: &
        B_{i}
\end{eqnarray}
$$

be fixed.

$$
\begin{eqnarray}
    \left(
        \bigcup_{i \in \mathbb{N}}
        \left(
            \bigcap_{j \in \mathbb{N}}
                A_{j}^{k_{j}}
        \right)^{l_{i}}
    \right)^{c}
    & = &
        \bigcap_{i \in \mathbb{N}}
        \left(
            \bigcap_{j \in \mathbb{N}}
                A_{j}^{k_{j}}
        \right)^{l_{i}c}
    .
    \nonumber
\end{eqnarray}
$$

By $$\eqref{proposition_02_equation_01}$$, we obtain

$$
    \left(
        \bigcap_{j \in \mathbb{N}}
            A_{j}^{k_{j}}
    \right)^{l_{i}c}
    \in
    \mathcal{F}
    .
$$

($\supseteq$)

Let $\bigcap_{i \in \mathbb{N}} A_{i}^{k_{i}} \in \mathfrak{M}$ be fixed.
Since $$\sigma(\mathcal{A}) \supseteq (\mathcal{A} \cup \{S\})$$,

$$
    A_{i}^{k_{i}}
    \in
    \sigma(\mathcal{A})
    .
$$

Since $\sigma$-algebra is closed under countable infinite intersection,

$$
    \bigcap_{i \in \mathbb{N}}
        A_{i}^{k_{i}}
    \in \sigma(\mathcal{A})
    .
$$

By definition of $\sigma$-algebra, it is closed under countable infinite uninon.
Thus,

$$
    \mathcal{F} \subseteq \sigma(\mathcal{A})
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
