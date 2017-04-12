---
title: chapter3
book_title: Random Number Generation and Quasi-Monte Carlo Methods
book_chapter: 3
---

## Low-Discrepancy Point Sets and Sequences

## 3.2 General discrepany bounds.
コンピュータ上の演算は全て、有限精度なので、point setsやsequencesで興味があるのは、有理数上の格子に位置する場合である。
格子が有理数の場合に得られる幾つかの興味深い上界と下界を述べる。

$M \ge 2$とおく。

$$
\begin{eqnarray}
    C(M)
    & := &
        \left(
            -\frac{M}{2}, \frac{M}{2}
        \right]
        \cap 
        \mathbb{Z}
    \nonumber
    \\
    C^{*}(M)
    & := &
        C(M) 
        \setminus
        \{0\}
    \nonumber
    \\
    C_{s}(M)
    & := &
        \prod_{i=1}^{s}C(M) 
    \nonumber
    \\
    C_{s}^{*}(M)
    & := &
        \left(
            \prod_{i=1}^{s}C(M) 
        \right)
        \setminus
        \{0\}
    \nonumber
\end{eqnarray}
$$

と定義する。
$C(M)$は、$(-M/2, M/2]$の区間の整数格子状の点である。
$$C^{*}(M)$$は$C(M)$から原点を抜いたものになる。

$$
    \forall h \in C(M),
    \
    M \ge 1,
    \quad
    r(h, M)
    :=
    \begin{cases}	
        M \sin \frac{\pi |h|}{M}
        &
            h \in C^{*}(M),
            \\
        1
        &  
            h = 0,
    \end{cases}
$$

更に、多次元の場合も同じ記号を使って定義する。
$$h = (h_{1}, \ldots, h_{s}) \in C_{s}(M)$$とすると、

$$
    r(h, M)
    :=
    \prod_{i=1}^{s}
        r(h_{i}, M)
$$

$$
\begin{eqnarray}
    \forall u \in \mathbb{R},
    \
    e(u)
    & := &
        e^{2\pi\sqrt{-1} u}
    \nonumber
    \\
    \forall x, y \in \mathbb{R}^{s},
    \
    x \cdot y
    & := &
         \sum_{i=1}^{s}
            x_{i} y_{i}
    \nonumber
\end{eqnarray}
$$

### Lemma 3.9

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

$$(h_{1}, \ldots, h_{m}) \in C_{m}(b)$$に対して、

$$
\begin{equation}
    d(h_{1}, \ldots, h_{m})
    :=
    \begin{cases}	
        \max
        \{
            d
            \mid
            h_{d} \neq 0
        \}
        & 
            (h_{1}, \ldots, h_{m}) \neq 0
            \\
        0 
        &
            (h_{1}, \ldots, h_{m}) = 0
    \end{cases}
    \label{chap03_3_15}
\end{equation}
$$

$$
\begin{equation}
    Q_{2}(h_{1}, \ldots, h_{m})
    :=
    2^{-d(h_{1}, \ldots, h_{m})}
    \label{chap03_3_16}
\end{equation}
$$

$$
\begin{equation}
    Q_{b}(h_{1}, \ldots, h_{m})
    :=
    \begin{cases}	
        b^{-d(h_{1}, \ldots, h_{m})}
        (
            \mathrm{csc}
            \frac{\pi}{b}
            |h_{d(h_{1}, \ldots, h_{m})}|
            +
            \sigma(d(h_{1}, \ldots, h_{m}), m)
        )
        &
            (h_{1}, \ldots, h_{m}) \neq 0 \\
        1 
        &
            (h_{1}, \ldots, h_{m}) = 0 
    \end{cases}
    \label{chap03_3_17}
\end{equation}
$$

ここで、cscはcosecantである。
$$ H := (h_{i,j})_{i = 1, \ldots, s}^{j = 1, \ldots, m} \in C(b)^{s \times m}$$である。

$$
\begin{equation}
    W_{b}(H)
    :=
    \prod_{i=1}^{s}
    Q_{b}(h_{i,1}, \ldots, h_{i, m})
    \label{chap03_3_18}
\end{equation}
$$

ここで、

$$
    \sigma(d, m)
    :=
    \begin{cases}	
        1 & d < m \\
        0 & d = m
    \end{cases}
$$

### Theorem 3.12

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

