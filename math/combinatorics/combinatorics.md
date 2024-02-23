---
title: Combinatorics
---

## Combinatorics



#### Proposition 1
- $N$

Let $\mathcal{P}_{N}$ be all permutation of $(1, \ldots, N)$.

$$
\begin{eqnarray}
    Q_{N}
    & := &
        \{
            (p_{1}, \ldots, p_{N}) \in \mathcal{P}_{N}
            \mid
            p_{i} \neq i
            \
            (\forall i)
        \}
    \nonumber
    \\
    \#Q_{N}
    & = &
        N!
        -
        \left(
            
            \frac{N!}{1!}
            -
            \frac{N!}{2!}
            +
            \frac{N!}{3!}
            -
            \ldots
            +
            (-1)^{N-1}
            \frac{N!}{N!}
        \right)
    .
\end{eqnarray}
$$

#### proof
Let $A_{i}$ be the number of permutaitons in which $i$-th number is equal to $i$.

$$
\begin{eqnarray}
    A_{i}
    & := &
        \{
            (p_{1}, \ldots, p_{N}) \in \mathcal{P}_{N}
            \mid
            p_{i} = i
        \}
    .
    \nonumber
\end{eqnarray}
$$

$$
    \#Q_{N}
    =
    N!
    -
    \#(
        A_{1}
        \cup
        \ldots
        \cup
        A_{N}
    )
    .
$$

By the inclusion-exclusion principle,

$$
\begin{eqnarray}
    A_{1}
    \cup
    \ldots
    \cup
    A_{N}
    & = &
        \sum_{i=1}^{N}
            \#A_{i}
        -
        \sum_{i, j, i \neq j}
            \#(A_{i} \cap A_{j})
        +
        \sum_{i, j, k}
            \#(A_{i} \cap A_{j} \cap A_{k})
        -
        \ldots
        +
        (-1)^{N - 1}
        \sum_{i_{1}, \ldots, i_{N}}
            \#(A_{i_{1}} \cap \cdots \cap A_{j_{N}})
\end{eqnarray}
$$

Since

$$
    A_{i_{1}} \cap \cdots \cap A_{i_{k}}
    =
    (N - k)!
    ,
$$

the RHS is

$$
\begin{eqnarray}
    A_{1}
    \cup
    \ldots
    \cup
    A_{N}
    & = &
        N(N - 1)!
        -
        {N \choose 2}
        (N - 2)!
        +
        {N \choose 3}
        (N - 3)!
        -
        \ldots
        +
        (-1)^{N - 1}
        {N \choose N}
        (N - N)!
    \nonumber
    \\
    & = &
        N!
        -
        \frac{N!}{2!}
        +
        \frac{N!}{3!}
        -
        \ldots
        +
        (-1)^{N-1}
        \frac{N!}{N!}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
