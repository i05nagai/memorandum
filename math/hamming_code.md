---
title: Hamming code
---

## Hamming code
Hamming code is linear error-correcting codes.

- $r >= 2$,
- data length: $k := 2^{r - 1} - r - 1$,
- parity length: $m := 2^{r - 1} + r$,
- block length: $2^{r} - 1$,
- $\mathbb{F}_{2}$

Hamming code can correct 1 error bit.

#### Example (7, 4) Hamming code
For example, let $$d = (x_{1}, x_{2}, x_{3}, x_{4}) \in \mathbb{F}_{2}^{4}$$ be data.
Parity is calculated as $$p = (x_{2} \oplus x_{3} \oplus x_{4}, x_{1} \oplus x_{2} \oplus x_{4}, x_{1} \oplus x_{3} \oplus x_{4})$$.
The generator matrix is

$$
    G
    :=
    \left(
        \begin{array}{ccccccc}
            1 & 0 & 0 & 0 & 0 & 1 & 1
            \\
            0 & 1 & 0 & 0 & 1 & 1 & 0
            \\
            0 & 0 & 1 & 0 & 1 & 0 & 1
            \\
            0 & 0 & 0 & 1 & 1 & 1 & 1
        \end{array}
    \right)
    .
$$

$$
    H
    :=
    \left(
        \begin{array}{ccccccc}
            1 & 0 & 0 & 0 & 1 & 0 & 0
            \\
            0 & 1 & 0 & 0 & 0 & 1 & 0
            \\
            0 & 0 & 1 & 0 & 0 & 0 & 1
        \end{array}
    \right)
    =
    \left(
        \begin{array}{ccccccc}
            1 & 0 & 1 & 0 & 1 & 0 & 1
            \\
            0 & 1 & 1 & 0 & 0 & 1 & 1
            \\
            0 & 0 & 0 & 1 & 1 & 1 & 1
        \end{array}
    \right)
    .
$$

$$
    p = d G
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

General hamming code.
Let $h_{i} \in \mathbb{F}_{2}^{n}$ be binary expression of $i$.

$$
    H_{r} = [h_{1} h_{2} \cdots h_{r}],
    \quad
    C =
    \{
        c \in \mathbb{F}_{2}^{2^{r} -1}
        \mid
        c H_{r}^{T}
        =
        0
    \}
    .
$$

Extended Hamming code.

$$
    H_{r}
    :=
$$

$$
    G
    :=
    \left(
        \begin{array}{ccccccc}
            1 & 0 & 0 & 0 & 0 & 1 & 1
            \\
            0 & 1 & 0 & 0 & 1 & 1 & 0
            \\
            0 & 0 & 1 & 0 & 1 & 0 & 1
            \\
            0 & 0 & 0 & 1 & 1 & 1 & 1
        \end{array}
    \right)
    .
$$

$$
    H
    :=
    \left(
        \begin{array}{ccccccc}
            1 & 0 & 1 & 0 & 1 & 0 & 1 & 0
            \\
            0 & 1 & 1 & 0 & 0 & 1 & 1 & 0
            \\ 
            0 & 0 & 0 & 1 & 1 & 1 & 1 & 0
            \\
            1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
        \end{array}
    \right)
    .
$$


## Reference
- https://en.wikipedia.org/wiki/Hamming_code
