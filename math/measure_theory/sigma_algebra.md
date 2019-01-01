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
        (A_{1} \cap B_{1}) \times \codts \times (A_{n} \cap B_{n})
    \nonumber
    \\
    A^{c}
    & = &
        A_{1}^{c} \times \codts \times A_{n}^{c}
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


## Reference
