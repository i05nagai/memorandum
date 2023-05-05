---
title: Linear code
---

## Linear code

#### Definition linear code
- $k, n \in \mathbb{N}$,
    - $k \le n$,
- $\mathbb{F}_{q}^{n}$,
- $C \subseteq \mathbb{F}_{q}^{n}$,

$C$ is said to be a linear code of length $n$ and dimension $k$ if $C$ is a $k$ dimentional linear subspace.

A code is an element of $C$.
The size of the code is $q^{k}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Generator
- $G$,
    - $k \times n$ matrix

Generator matrix $G$ is a matrix where $C := \{xG \mid x \in F_{q}^{n}\}$.
If $G = [I_{k} \mid P]$ where $I_{k}$ is $k\times k$ identity matrx and $P$ is $k \times (n- k)$ matrix, $G$ is in standard form.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Check matrix
- $H$,
    - $(n - k) \times n$ matrix

$H$ is said to be a check matrix if

$$
    C
    =
    \{
        x \in F_{q}^{n}
        \mid
        Hx = 0
    \}
    .
$$

That is, The kernel of $H$ is $C$.
If $G = [I_{k} \mid P]$ where $I_{k}$ is $k\times k$ identity matrx and $P$ is $k \times (n- k)$ matrix, $G$ is in standard form.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
If $G = [I_{k} \mid P]$ is in a standard form, $H = [-P^{T} \mid I_{n-1}]$.

<div class="end-of-statement" style="text-align: right">■</div>


#### Definition Dual code
- $C$,
    - linear code
- $G$,
    - $n \times k$ matrix
- $H$,
    - check matrix
    - $(n - k) \times n$ matrix


The dual code of $C$ $C^{\bot}$ is a linear subspace genrated by $H$. That is

$$
    C^{\bot}
    =
    \{
        c \in F_{q}^{n}
        \mid
        c^{\prime} \in C,
        \
        \langle c, c^{\prime} \rangle
        =
        0
    \}
    =
    \{
        (H x)^{T} \in F_{2}^{n}
        \mid
        x \in F_{2}^{n - k}
    \}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
- https://en.wikipedia.org/wiki/Linear_code
