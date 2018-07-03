---
title: Bit Operation
---

## Bit Operation

* $F_{2}[x]$,
    * polynominal ring over base2 field
* $\phi: F_{2}[x] \rightarrow \mathbb{Z}_{\ge 0}$,
    * bijection

We idnetify elements of polynominal ring $F_{2}[x]$ with $\mathbb{Z}_{\ge 0}$ by

$$
    \phi(a)
    :=
    \sum_{i=0}^{n}
        a_{i} 2^{i}
    .
$$

For bit-wise operation, we calculate it in $F_{2}[x]$.
For operations over bit, we caluclate it in $\mathbb{Z}_{\ge 0}$ by $\phi$.

### Definition. carry index
* $a := \sum_{i=0}^{n} a_{i}x^{i} \in F_{2}[x]$,
* $\alpha: F_{2}[x] \rightarrow \mathbb{Z}_{\ge 0}$,

$\alpha$ is carry index defined by

$$
    \alpha(a)
    :=
    \begin{cases}
        \{
            i \in \mathbb{Z}_{\ge 0}
            \mid
            a_{i}
            \neq
            2 - 1
        \}
        &
            (a_{i} \neq 1)
        \\
        n
        &
            (\text{ otherwise })
    \end{cases}
    .
$$


$\alpha$ is first index which is not 1.

<div class="end-of-statement" style="text-align: right">■</div>

With carry index, we calcualte carry operation

$$
\begin{eqnarray}
    \phi(a)
    +
    1
    & = &
        \sum_{i=0}^{n}
            a_{i}2^{i}
        +
        1
    \\
    & = &
        \sum_{i=0}^{\alpha(a) - 1}
            a_{i}2^{i}
        +
        \sum_{i=\alpha(a)}^{n}
            a_{i}2^{i}
        +
        1
    \nonumber
    \\
    & = &
        2^{\alpha(a)}
        +
        \sum_{i=\alpha(a)}^{n}
            a_{i}2^{i}
    \nonumber
    \\
    & = &
        \sum_{i=\alpha(a)}^{n}
            a_{i}2^{i}
        \quad
        (\because a_{\alpha(a)} = 0)
    \nonumber
\end{eqnarray}
$$

### Definition. Two's complement
* $a \in F_{2}[x]$,
* $m \in \mathbb{N}$,
* $$\bar{C}_{m}:F_{2}[x] \rightarrow F_{2}[x]$$,
* $m \ge n$,

$\bar{C}_{m}$ is one's commplement defined by

$$
\begin{eqnarray}
    \bar{C}_{m}(a)
    & := &
        \sum_{i=0}^{m}
            c_{i}x^{i}
    \nonumber
    \\
    & := &
        \sum_{i=n+1}^{m}
            x^{i}
        +
        \sum_{i=0}^{n}
            (a_{i} - 1) x^{i}
    \nonumber
\end{eqnarray}
    .
$$

By the definition of $m$-bit one's complement, we have

$$
    \phi(\bar{C}_{m}(a)) + 1
    =
    \sum_{i=\alpha(\bar{C}_{m}(a))}^{n}
        c_{i}2^{i}
    .
$$

* $C_{m}:F_{2}[x] \rightarrow F_{2}[x]$,

$m$-bit Two's complement $C_{m}$ is defined by

$$
\begin{eqnarray}
    C_{m}(a)
    & := &
        \phi^{-1}
        \left(
            \phi(\bar{C}_{m}(a)) + 1
        \right)
    \nonumber
    \\
    & = &
        \sum_{i=\alpha(\bar{C}_{m}(a))}^{n}
            c_{i}x^{i}
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition

$$
    a
    +
    C_{m}(a)
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
