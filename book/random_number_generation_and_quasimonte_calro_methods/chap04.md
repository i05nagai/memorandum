---
title: chapter4
book_title: Random Number Generation and Quasi-Monte Carlo Methods
book_chapter: 4
---

## NETS AND ($t, s$)-SEQUENCES

## 4.3 General construction principles.
$(t, m, s)$-netの構成方法。

* $m \ge 1$
* $s \ge 1$
* $b \ge 2$

とする。
以下の4つの条件を定義する。

$$
    R \text{ is a commutative ring with indetity, }
    \mathrm{card}(R) = b
    \label{chap04_N1}
    \tag{N1}
$$

$$
    \phi_{r}: \mathbb{Z}_{b} \rightarrow R \text{ bijection},
    \quad
    0 \le r \le m -1
    \label{chap04_N2}
    \tag{N2}
$$

$$
    \eta_{i,j}: R \rightarrow \mathbb{Z}_{b} \text{ bijection,}
    \quad
    1 \le i \le s,
    \
    1 \le j \le m
    \label{chap04_N3}
    \tag{N3}
$$

$$
    c_{jr}^{(i)} \in R,
    \quad
    1 \le i \le s,
    \
    1 \le j \le m,
    \
    0 \le r \le m - 1
    \label{chap04_N4}
    \tag{N4}
$$


$n = 0, \ldots, b^{m-1} - 1$について、$n$のb進数展開を以下で定義する。

$$
    n
    =
    \sum_{r=0}^{m-1}
        a_{r}(n)b^{r},
    \quad
    a_{r}(n) \in \mathbb{Z}_{b}
$$

$n$番目の点の$i$次元の値$x_{n}^{(i)}$を以下で定義。

$$
    x_{n}^{(i)}
    :=
    \sum_{j=1}^{m}
        y_{nj}^{(i)}b^{-j},
    \quad
    0 \le n < b^{m},
    \
    1 \le i \le s,
$$

ここで、

$$
    y_{nj}^{(i)}
    :=
    \eta_{ij}
    \left(
        \sum_{r=0}^{m-1}
            c_{jr}^{(i)}
            \phi_{r}(a_{r}(n))
    \right)
    \in \mathbb{Z}_{b},
    \quad
    0 \le n < b^{m},
    \
    1 \le i \le s,
    \
    1 \le j \le m
$$

である。
point setを

$$
\begin{equation}
    x_{n} := (x_{n}^{(1)}, \ldots, x_{n}^{s}) \in I^{s}
    \quad
    n = 0, 1, \ldots, b^{m-1} - 1
    \label{chap04_4_25_point_set}
\end{equation}

$$

と定義する。

### Thorem 4.26
以下を仮定する。

* $0 \le t \le m$
* $$d_{1}, \ldots, d_{s} \in \mathbb{Z}$$,
* $$\sum_{i=1}^{s} d_{i} = m - t$$,
* $$f_{j}^{(i)} \in R$$, for $1 \le j \le d,\ 1 \le i \le s$

$ m - t = \sum_{i=1}^{d_{s}}$個の線形方程式

$$
    \sum_{r=0}^{m-1}
        c_{jr}^{(i)}z_{r}
    =
    f_{j}^{(i)},
    \quad
    1 \le j \le d,
    \
    1 \le i \le s,
$$

が、$z_{1}, \ldots, z_{m-1} \in R$を未知変数としてちょうど$b^{t}$個の解を持つとする。
このとき、$$\eqref{chap04_4_25_point_set}$$で定義される点列は、$(t, m, s)$-Netsである。


### proof.

<div class="QED" style="text-align: right">$\Box$</div>

特に、以後$b$が素数の場合を頻繁に考える。
$b$が素数の場合特に$q$とかくとring $R$としてfinite filed $F_{q}$をとれる。
$c_{j}(i)$を$F_{q}$の$m$個の直積空間の元として取る。

$$
\begin{equation}
    c_{j}^{(i)}
    :=
    (c_{j,0}^{(i)}, \ldots, c_{j,m-1}^{(i)})
    \in F_{q}^{m},
    \quad
    1 \le i \le s,
    \
    1 \le j \le m
    \label{chap04_4_26_c_ij_in_finte_filed}
\end{equation}
$$

まず一般の線形空間に対して、以下を定義する。

### Definition 4.27
$V$を有限次元線形空間とする。
$c_{j}^{(i)} \in V$ for $1 \le i \le s,\ 1 \le j \le m$を取る。

$$
\begin{eqnarray}
    C
    & := &
        \{
            c_{j}^{(i)} \in V
            \mid
            1 \le i \le s,
            \
            1 \le j \le m
        \},
    \nonumber
    \\
    C(d_{1}, \ldots, d_{s})
    & := &
        \{
            c_{j}^{(i)} \in V
            \mid
            1 \le i \le s,
            \
            1 \le j \le d_{i} 
        \},
    \quad
    1 \le i \le s,
    \
    0 \le d_{i} \le m
    \nonumber
\end{eqnarray}
$$

とする。
$C(d_{1}, \ldots, d_{N})$は空集合にもなりうることに注意する。
$\rho(C)$を以下のように定義する。

$$
    \rho(C)
    :=
    \max
    \{
        d
        \mid
        d =
        \sum_{i=1}^{s}
            d_{i},
        \
        C(d_{1}, \ldots, d_{s})
        \ 
        \text{is linearly independent in } V
    \}.
$$

ただし、$$C(d_{1}, \ldots, d_{s})$$ が空集合の場合は、線形独立とする。
つまり、$d_{i} = 0$ for all $i$のとき、$\rho(C) = 0$である。

明らかに$0 \le \rho(C) \le \dim{V}$である。
この章では$V$として$F_{q}$上の線形空間$F_{q}^{m}$のみを考える。
つまり、$c_{j}^{(i)}$として$$\eqref{chap04_4_26_c_ij_in_finte_filed}$$をとる。


### Theorem 4.28
$q$が素数で$R = F_{q}$とする。
$c_{j}^{(i)}$が$$\eqref{chap04_4_26_c_ij_in_finte_filed}$$で与えられているとする。
このとき、$$\eqref{chap04_4_25_point_set}$$の点列はbase $q$の$(t, m, s)$-netsで、$t = m - \rho(C)$で与えられる。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

上の定理は更に、任意の整数$b \ge 2$に対して一般化できる。
$b$の素因数分解を$b = \prod_{v=1}^{h} q_{v}$とする。
ring $R$を$$R := \prod_{v=1}^{h} F_{q_{v}}$$としてfinite filedの直積として定義する。
明らかに$\mathrm{card}(R) = b$で $$\eqref{chap04_N1}$$を満たす。
このとき、$c_{j,r}^{(i)}$は

$$
\begin{equation}
    c_{j,r}^{(i)}
    =
    (c_{j,r,1}^{(i)}, \ldots, c_{j, r, h}^{(i)})
    \in R
    \label{chap04_4_27_c_j_r_i}
\end{equation}
$$

とかけて、各要素は$$c_{j, r, v}^{(i)} \in F_{q_{v}}$$である。


$$
\begin{equation}
    c_{j, \cdot, v}^{(i)}
    =
    (c_{j, 0, v}^{(i)}, \ldots, c_{j, m - 1, v}^{(i)})
    \in F_{q_{v}}^{m}
    \quad
    1 \le i \le s,
    \
    1 \le j \le m,
    \label{chap04_4_28_c_j_cdot_v_i}
\end{equation}
$$

このとき、$C_{v}$を以下のように定義し、

$$
\begin{eqnarray}
    C_{v}
    & := &
        \{
            c_{j, \cdot, v}^{(i)}
            \mid
            1 \le i \le s,

        \},
    \nonumber
    \\
    C_{v}(d_{1}, \ldots, d_{s})
    & := &
        \{
            c_{j, \cdot, v}^{(i)}
            \mid
            1 \le i \le s,
            \
            1 \le j \le d_{i},
        \},
    \nonumber
\end{eqnarray}
$$

$\rho(C_{v})$も同様に定義しておく。

### Theorem 4.29
* $b = \prod_{v=1}^{h} q_{v}$と素数の積でかけているとする。
* $R := \prod_{i=1}^{h}F_{q_{v}}$として定義
* $c_{j, r}^{(i)} \in R$は$$\eqref{chap04_4_27_c_j_r_i}$$で与えられる

このとき、$$\eqref{chap04_4_25_point_set}$$は$(t, m, s)$-netsで

$$
    t
    =
    m - \min_{1 \le v \le h}\rho(C_{v}),
$$

である。
ここで、$C_{v}$は$$\eqref{chap04_4_28_c_j_cdot_v_i}$$で定義される。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

Theorem 4.28及びTheorem 4.29の$t$-valueは、Theorem 4.10の$(t, m, s)$-netsの上界の評価に使える。

$$
\begin{equation}
    D_{N}^{*}(P)
    \le 
    B(s, q)
    q^{-\rho(C)}
    (\log N)^{s-1}
    +
    O(
        q^{-\rho(C)}
        (\log N)^{s-2}
    ),
    \label{chap04_4_31_upper_bound_of_discrepancy}
\end{equation}
$$

更に、$\rho(C)$による$D_{N}^{*}(P)$の下界も以下から分かる。

### Theorem 4.30
* $q$が素数
* $R = F_{q}$

このとき、

$$
    D_{N}^{*}(P)
    \ge
    \left(
        \frac{1}{3}
        -
        \frac{1}{3q}
    \right)
    q^{-\rho(C)}
$$

である。
更に、全単射$\eta_{i,j}$が$\eta_{i, j}(0) = 0$ for $a \le i \le s,\ 1 \le j \le m$を満たすと

$$
    D_{N}^{*}
    \ge
    \left(
        \frac{1}{2}
        -
        \frac{1}{2q}
    \right)
    q^{-\rho(C)}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Remark 4.31
TBD

$q$
