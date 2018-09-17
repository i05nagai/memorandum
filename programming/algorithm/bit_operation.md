---
title: Bit Operation
---

## Bit Operation

* $F_{2}[x]$,
    * polynominal ring over base2 field
* $\phi: F_{2}[x] \rightarrow \mathbb{Z}_{\ge 0}$,
    * bijection
* $\otimes$,
    * multiplication over $F_{2}$ or $F_{2}[x]$

We idnetify elements of polynominal ring $F_{2}[x]$ with $\mathbb{Z}_{\ge 0}$ by

$$
    \phi(a)
    :=
    \sum_{i=0}^{n}
        a_{i} 2^{i}
    .
$$

For bit-wise operations, we calculate them in $F_{2}[x]$, for operations over bit, in $\mathbb{Z}_{\ge 0}$ by $\phi$.

### Definition. bit-wise multiplication
* $a := \sum_{i=0}^{n} a_{i}x^{i} \in F_{2}[x]$,
* $b := \sum_{i=0}^{m} b_{i}x^{i} \in F_{2}[x]$,
* $m \ge n$,

$$
\begin{eqnarray}
    a
    \otimes
    b
    & = &
        \sum_{i=0}^{n}
            a_{i}b_{i}
            x^{i}
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. carry index
* $a := \sum_{i=0}^{n} a_{i}x^{i} \in F_{2}[x]$,
* $$k \in \{0, 1\}$$,
* $\alpha_{k}: F_{2}[x] \rightarrow \mathbb{Z}_{\ge 0}$,

Let 

$$
    \alpha_{k}(a)
    :=
    \begin{cases}
        \min
        \{
            i \in \mathbb{Z}_{\ge 0}
            \mid
            a_{i}
            \neq
            k
        \}
        &
            (\exists j \text{ s.t. } a_{j} \neq k)
        \\
        n
        &
            (\text{ otherwise })
    \end{cases}
    .
$$

In particular, if $k=1$, $\alpha_{1}$ is called carry index and we write $\alpha$.

<div class="end-of-statement" style="text-align: right">■</div>

Carry index $\alpha$ is the first index which is not 1 (i.e. 0).
Carry index can allow to add two bits with carrying bit unti the carry index.

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
    \nonumber
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
        (1 + a_{\alpha(a)})2^{\alpha(a)}
        +
        \sum_{i=\alpha(a)+1}^{n}
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

$\bar{C}_{m}$ is $m$-bit one's commplement defined by

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
\begin{eqnarray}
    \phi(\bar{C}_{m}(a)) + 1
    & = &
        \sum_{i=n+1}^{x}
            2^{i}
        +
        \sum_{i=\alpha(\bar{C}_{m}(a))}^{n}
            c_{i}2^{i}
    \nonumber
    \\
    & = &
        \sum_{i=n+1}^{m}
            2^{i}
        +
        a_{\alpha_{0}(a)}2^{\alpha_{0}(a)}
        +
        \sum_{i=\alpha_{0}(a)+1}^{n}
            (a_{i} - 1)2^{i}
    \nonumber
\end{eqnarray}
.
$$

Note that $a_{\alpha_{0}(a)} \neq 0$.

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
    \nonumber
    \\
    & = &
        \sum_{i=n+1}^{m}
            x^{i}
        +
        a_{\alpha_{0}(a)}
        x^{\alpha_{0}(a)}
        +
        \sum_{i=\alpha_{0}(a)+1}^{n}
            (a_{i} - 1)
            x^{i}
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition

$$
    a
    +
    C_{m}(a)
    =
    \sum_{i=\alpha_{0}(a)+1}^{m}
        x^{i}
$$

### proof.
It's easy to confirm that

$$
    \sum_{i=0}^{\alpha_{0}(a)-1}
        a_{i}
        x^{i}
    =
    0
    .
$$

Then

$$
\begin{eqnarray}
    a
    +
    C_{m}(a)
    & = &
        \left(
            \sum_{i=0}^{\alpha_{0}(a)-1}
                a_{i}x^{i}
            +
            a_{\alpha_{0}(a)}
            x^{\alpha_{0}(a)}
            +
            \sum_{i=\alpha_{0}(a)+1}^{n}
                a_{i}x^{i}
        \right)
        +
        \left(
            \sum_{i=n+1}^{m}
                x^{i}
            +
            a_{\alpha_{0}(a)}
            x^{\alpha_{0}(a)}
            +
            \sum_{i=\alpha_{0}(a)+1}^{n}
                (a_{i} - 1)
                x^{i}
        \right)
    \nonumber
    \\
    & = &
        \sum_{i=\alpha_{0}(a)+1}^{m}
            x^{i}
    \nonumber
    \\
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition.

$$
    a
    \otimes
    C_{m}(a)
    =
    a_{\alpha_{0}(a)}
    x^{\alpha_{0}(a)}
    .
$$

That is, the result is the first non-zero bit.

### proof.
For any $d \in F_{2}$,

$$
\begin{eqnarray}
    d(d - 1)
    & = &
        0
    \nonumber
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    a
    \otimes
    C_{m}(a)
    & = &
        \left(
            \sum_{i=0}^{\alpha_{0}(a)-1}
                a_{i}x^{i}
            +
            a_{\alpha_{0}(a)}
            x^{\alpha_{0}(a)}
            +
            \sum_{i=\alpha_{0}(a)+1}^{n}
                a_{i}x^{i}
        \right)
        \otimes
        \left(
            \sum_{i=n+1}^{m}
                x^{i}
            +
            a_{\alpha_{0}(a)}
            x^{\alpha_{0}(a)}
            +
            \sum_{i=\alpha_{0}(a)+1}^{n}
                (a_{i} - 1)
                x^{i}
        \right)
    \nonumber
    \\
    & = &
        a_{\alpha_{0}(a)}
        a_{\alpha_{0}(a)}
        x^{\alpha_{0}(a)}
    \nonumber
    \\
    & = &
        a_{\alpha_{0}(a)}
        x^{\alpha_{0}(a)}
        \quad
        (\because a_{\alpha_{0}(a)}=1)
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
