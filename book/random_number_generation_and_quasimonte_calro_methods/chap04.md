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

$q$が素数とすると、以下を同一視できる。

* $F_{q}$, $$Z_{q}$$,
* $$F_{q}$$, $$C(q)$$,
    * $$C(q)$$は3.17で定義されている。

$$
    C
    :=
    \{
        c_{j}^{(i)} \in F_{q}^{m}
        \mid
        1 \le i \le s,
        \
        1 \le j \le m
    \}
$$

$$\eqref{chap04_4_26_c_ij_in_finte_filed}$$の定める$C$とする。
$$\eqref{chap03_3_18}$$の式を使うと、$$H := (h_{i,j})_{i=1,\ldots,s}^{j=1,\ldots,m} \in C(q)^{s \times m}$$,

$$
\begin{eqnarray}
    R_{q}(C)
    & := &
        \sum_{H}
            W_{q}(H)
    \nonumber
    \\
    \sum_{i=1}^{s}
        \sum_{j=1}^{m}
            h_{i,j}c_{j}^{(i)}
    & = &
        0
        \in F_{q}^{m}
    \nonumber
\end{eqnarray}
$$

### Lemma 4.32
$q$が素数とする。
$R = F_{q}$とする。
$\forall \eta_{i,j}$が恒等写像とする。
このとき、$$\eqref{chap04_4_25_point_set}$$の点列$P$は

$$
    D_{N}^{*}(P)
    \le
    1
    -
    \left(
        1 - \frac{1}{N}
    \right)^{s}
    +
    R_{q}(C)
    \le
    \frac{s}{N}
    +
    R_{q}(C)
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

lemma 4.36によれば、$$\eqref{chap04_4_25_point_set}$$にもとづいてLow-Discrepancy sequenceを作ることができる。

### Theorem 4.33
* $q$が素数
* $m \ge 1$
* $s \le 1$

$$
    \mathcal{C}
    :=
    \left\{
        \left\{
            c_{j}^{(i)}
            \mid
            1 \le i \le s,
            \
            1 \le j \le m
        \right\}
        \mid
        \{ c_{j}^{(i)} \}
        \subset
        F_{q}^{m}
    \right\}
$$

を$C$の全ての組み合わせとする。

$$
    M_{q}(m, s)
    :=
    \frac{1}{\mathrm{card}(\mathcal{C})}
    \sum_{C \in \mathcal{C}}
        R_{q}(C)
$$

を全ての$C$についての$R_{q}(C)$の平均とする。
このとき、

$$
\begin{eqnarray}
    M_{q}(m, s)
    & = &
        \frac{1}{N}
        \left(
            \frac{\log N}{\log 4}
            +
            1
        \right)^{s}
        -
        \frac{1}{N},
    \nonumber
    \\
    M_{q}(m, s)
    & = &
        \frac{1}{N}
        \left(
            \frac{m}{q}
            \sum_{h \in C^{*}(q)}
                \csc
                \frac{\pi |h|}{q}
                +
                m
                -
                \frac{m-1}{q}
        \right)^{s}
        -
        \frac{1}{N}
        \
        (\text{ if } q = 2)
    \nonumber
    \\
    & < &
        \frac{1}{N}
        \left(
            \left(
                \frac{2}{\pi}
                +
                \frac{7}{5 \log q}
                -
                \frac{1}{q \log q}
            \right)
            \log N
            +
            \frac{1}{q}
        \right)^{s}
        -
        \frac{1}{N}
        \
        (\text{ if } q > 2)
    \nonumber
\end{eqnarray}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

Lemma 4.32とLemma 4.33をあわせて、

* $q$が素数
* $R = F_{q}$
* $$\eta_{i,j}$$が恒等写像
* $m \ge 1$
* $s \ge 1$,

を満たすならば、$$\eqref{chap04_4_25_point_set}$$で定義される$P$は$$D_{N}^{*}(P) = O(N^{-1}(\log N)^{s})$$である。
更に、Definition 4.27の $\rho(C)$と$R_{q}(C)$は以下の不等式を満たすことを示す。

### Theorem 4.34
$s \ge 2$で、$q$は素数とする。

$$
    q^{-\rho(C) - 1}
    \le
    R_{q}(C)
    \le
    \left(
        1
        -
        \frac{1}{q}
    \right)
    k(q)^{s}
    \left(
        (m + 1)^{s}
        -
        \left(
            \begin{array}{c}
                \rho(C) + s \\
                s
            \end{array}
        \right)
    \right)
    q^{-\rho(C)},
$$

ここで、

$$
    k(q)
    :=
    \begin{cases}	
        1 & q = 2, \\
        \csc(\pi / q) + 1 & q > 2, 
    \end{cases}
$$

である。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

$\rho(C)$が十分大きければ、$$\eqref{chap04_4_25_point_set}$$の点列はLow-Discrepancyになることがわかった。
よって、$m \ge 1$, $s \ge 1$と有限体$F_{q}$を与えた時に$\rho(C)$の最大値を求める問題は興味深い問題である。
この問題は、coding theoryにおける古典的な問題と関係している。
大きい$\rho(C)$を持つ$C$の構成方法はsection 4.5で述べる。

次にbase bの$(t, s)$-sequenceの構成方法について述べる。

* $s \ge 1$
* $b \ge 2$

とする。

$$
    R \text{ is a commutative ring with indetity, }
    \mathrm{card}(R) = b
    \label{chap04_S1}
    \tag{S1}
$$

$$
    \phi_{r}: \mathbb{Z}_{b} \rightarrow R \text{ bijections},
    \quad
    r \ge 0,
    \
    \phi_{r}(0) = 0
    \
    \text{ for sufficient large } r
    \label{chap04_S2}
    \tag{S2}
$$

$$
    \eta_{i,j}: R \rightarrow \mathbb{Z}_{b} \text{ bijections,}
    \quad
    1 \le i \le s,
    \
    1 \le j 
    \label{chap04_S3}
    \tag{S3}
$$

$$
    c_{jr}^{(i)} \in R,
    \quad
    1 \le i \le s,
    \
    1 \le j
    \
    0 \le r
    \label{chap04_S4}
    \tag{S4}
$$

また、$n \in \mathbb{R}_{\ge 0}$について

$$
    n
    =
    \sum_{r=0}^{\infty}
        a_{r}(n)b^{r}
$$

と$$r \ge 0$$, $$a_{r}(n) \in \mathbb{R}_{b}$$を用いて、$b$進数展開を定義しておく。
但し、十分大きな$r$について、$$a_{r}(n) = 0$$とする。
更に

$$
    x_{n}^{(i)}
    :=
    \sum_{j=1}^{\infty}
        y_{n, j}^{(i)}
        b^{-j}
    \quad
    n \ge 0,
    \
    1 \le i \le s
$$

ここで、

$$
    y_{n, j}^{(i)}
    :=
    \eta_{i,j}
    \left(
        \sum_{r=0}^{\infty}
            c_{j, r}^{(i)}
            \phi_{r}(a_{r}(n))
    \right)
    \in \mathbb{Z}_{b}
    \quad
    n \ge 0,
    \
    1 \le i \le s,
    \
    j \ge 1,
$$

十分大きな$r$について、$\phi_{r}(0) = 0$より、十分大きな$r$については、$a_{r}(0) = 0$である。
以上より、sequenceの$n$番目を以下で定義する。

$$
\begin{equation}
    x_{n}
    :=
    (x_{n}^{(1)}, \ldots, x_{n}^{(s)}),
    \quad
    n = 0, 1, \ldots,
    \label{chap04_4_42_t_s_sequence}
\end{equation}
$$

である。

$$
    \forall n \ge 0,
    \
    1 \le \forall i \le s,
    \
    \exists j_{0} \ge 1,
    \text{ s.t. }
    \
    \forall j \ge j_{0},
    \
    y_{n, j}^{(i)} < b - 1
    \tag{S5}
    \label{chap04_S5}
$$

$$\eqref{chap04_S5}$$の十分条件として、

$$
\begin{eqnarray}
    1 \le \forall i \le s,
    \
    \exists j_{0} \ge 1,
    \text{ s.t. }
    \
    \forall j \ge j_{0},
    & &
        \
        \eta_{i,j}(0) = 0,
    \nonumber
    \\
    1 \le \forall i \le s,
    \
    \forall r \ge 0,
    \exists j_{0} \ge 1,
    \text{ s.t. }
    \
    \forall j \ge j_{0},
    & &
        \
        c_{j, r}^{(i)} = 0
    \tag{S6}
    \label{chap04_S6}
\end{eqnarray}
$$

### Theorem 4.35
$t \in \mathbb{Z}_{\ge 0}$が以下を満たすとする。

* $\forall m \in \mathbb{Z}$, $$d_{1}, \ldots, d_{s} \ge 0$$
* $$\sum_{i=1}^{s} d_{i} = m - t$$,
* $$1 \le j \le d_{i}, 1 \le i \le s$$, $$f_{j}^{(i)} \in R$$,

$z_{0}, \ldots, z_{m-1} \in R$を未知変数について、$m - t$個の線形方程式

$$
    \sum_{r=0}^{m-1}
        c_{j,r}^{(i)}
        z_{r}
    =
    f_{j}^{(i)}
    \quad
    1 \le j \le d_{i},
    \
    1 \le i \le s,
$$

がちょうど$b^{t}$個の解があるとする。
このとき、$$\eqref{chap04_4_42_t_s_sequence}$$は base b の$(t, s)$-sequencesになる。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

$q$が素数の場合、Theorem 4.28と同様の定理が$(t, s)$-sequenceについても成り立つ。
$$\eqref{chap04_S4}$$の$$c_{j, r}^{(i)}$$のなす集合について考慮する。

### Theorem 4.36
$q$を素数とする。
* $R = F_{q}$
* $t \ge 0$を整数とする

ここで、$\forall m > t$, $C^{(m)}$

$$
    c_{j}^{(i)}
    =
    (c_{j, 0}^{(i)}, \ldots, c_{j, m-1}^{(i)})
    \in
    F_{q}^{m}
    \quad
    1 \le i \le s,
    \
    1 \le j \le m,
$$

が$\rho(C^{(m)}) \ge m - t$を満たすとする。
このとき、$$\eqref{chap04_4_42_t_s_sequence}$$は$(t, s)$-sequence in base qとなる。



### proof.

<div class="QED" style="text-align: right">$\Box$</div>


## 4.4 A special construction of nets.
$$\eqref{chap04_N1}$$ - $$\eqref{chap04_N4}$$に基づいた一般的な構成方法について述べる。

* $q$を素数とする。
* baseを$q$とする。
* $R = F_{q}$

$$
\begin{equation}
    F_{q}(x^{-1})
    :=
    \left\{
        \sum_{k=w}^{\infty}
            t_{k}x^{-k}
        \mid
        \forall w \in \mathbb{Z},
        \
        t_{k} \in F_{q}
    \right\}
\end{equation}
$$

exponential valuation $\nu$を次で定義する。

$$
    L \in F_{q}(x^{-1}),
    \
    \nu(L)
    :=
    \begin{cases}	
        -w & L \neq 0 \\
        0 & L = 0 
    \end{cases}
$$

ここで、$w$は$t_{w} \neq 0$なる最小の整数である。
また、$$F_{q}[x] \subset F((x^{-1}))$$であり、$f \in F_{q}[x]$ならば$\nu(v) \neq \deg(f)$である。
明らかに $$\subset F((x^{-1}))$$は$$F_{q}$$を部分体として含む。

$s \ge 2$を次元とする。
$f \in F_{q}[x]$を適当に選び、$\deg(f) = m \ge 1$とする。
$$g_{1}, \ldots, g_{s} \in F_{q}[x]$$である。

$$
    \frac{g_{i}(x)}{f(x)}
    =
    \sum_{k=w_{i}}^{\infty}
        u_{k}^{(i)}
        x^{-1}
    \in F_{q}^((x^{-1})),
    \
    1 \le i \le s,
$$

$f, g \in F_{q}[[x]]$に対して商$f/g$を以下のように定義する。

$$
\begin{eqnarray}
    f(x)
    & = & 
        \sum_{i=w_{f}}^{\infty}
            a_{i}x^{i}
    \nonumber
    \\
    g(x)
    & = &
        \sum_{i=w_{g}}^{\infty}
            b_{i}x^{i}
    \nonumber
    \\
    \frac{g(x)}{f(x)}
    & := &
        h(x)
\end{eqnarray}
$$

ここで$h \in F_{q}[[x]]$は以下を満たす。

$$
\begin{eqnarray}
    h(x)
    & = &
        \sum_{i=w_{h}}^{\infty}
            c_{i}x^{i}
    \nonumber
    \\
    c_{n}
    & = &
        \frac{1}{b_{w_{g}}}
        \left(
            a_{n}
            -
            \sum_{j=1}^{n}
                b_{w_{g} + j}c_{w_{h} + n - i}
        \right)
    \nonumber
\end{eqnarray}
$$

$w_{h} := w_{g} - w_{f}$である。


