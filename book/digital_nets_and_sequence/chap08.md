---
title: chapter8
book_title: Digital Nets and Sequences
book_chapter: 8
---

## 8. Special constructions of digital nets and sequences

## 8.1 Sobol', Faure, and Niederreiter sequences


### Classical Niederreiter sequence
$$(t, s)$$-sequenceの構成。
Niederreiter sequenceと呼ばれる。


* $$s \in \mathbb{N}$$,
    * dimension
* $b$
    * 素数のべき乗
* $$p_{1}, \ldots, p_{s} \in F_{b}[x]$$,
    * monic irreducible polynomials over $$F_{b}$$
* $$e_{i} := \mathrm{deg}(p_{i})\ (i = 1, \ldots, s)$$,

Formal Laurent seriesとしての割り算によって以下の左辺を定義する。

$$
\begin{equation}
    i = 1, \ldots, s,
    \
    j = 1, \ldots,
    \
    k = 0, \ldots, e_{i} - 1,
    \quad
    \frac{
        x^{k}
    }{
        p_{i}(x)^{j}
    }
    =:
    \sum_{r=0}^{\infty}
        a_{j, k}^{(i)}(r)x^{-r-1}
    \label{chap08_8_01_formal_laurent_series_division}
\end{equation}
$$

つまり、右辺は以下を満たす。

$$
    i = 1, \ldots, s,
    \
    j = 1, \ldots,
    \
    k = 0, \ldots, e_{i} - 1,
    \quad
    x^{k}
    =
    \left(
        \sum_{r=0}^{\infty}
            a_{j, k}^{(i)}(r)x^{-r-1}
    \right)
        p_{i}(x)^{j}
$$

また、$$i = 1, \ldots, s$$, $$j = 1, \ldots, $$に対して、$$Q(i, j) \in \mathbb{Z}$$を$$k(i,j) \in \{0, \ldots, e_{i} - 1\}$$を$$j - 1$$を$$e_{i}$$で割った商とその余りとする。
つまり、以下を満たす。

$$
    j - 1 = Q(i, j) e_{i} + k(i, j)
$$

次元$i$の生成行列$$C_{i} := (c_{j, r}^{(i)})_{j \ge 1, r \ge 0}$$を以下で定める。

$$
\begin{equation}
    c_{j, r}^{(i)}
    :=
    a_{Q(i, j) + 1, k(i, j)}^{(i)}(r) \in F_{b}
    \label{chap08_8_02_formal_laurent_series_division}
\end{equation}
$$

$$j$$は行、$r$は列に対応する添字となる。
つまり、

$$
    C_{i}
    =
    \left(
        \begin{array}{ccccc}
            c_{1, 0}^{(i)}
            &
                c_{j, 1}^{(i)}
            &
                    \cdots 
            &
                c_{j, r}^{(i)}
            & 
                    \cdots 
            \\
            c_{2, 0}^{(i)}
            &
                c_{j, 1}^{(i)}
            &
                \cdots 
            &
            &
                \vdots
            \\
            \vdots
                &
                &
                &
                    \ddots
                &
            \\
                &
                    \vdots
                &
                    \ddots
                &
                    \ddots
                &
            \\
            c_{j, 0}^{(i)}
            &
                \cdots
            &
            &
            &
        \end{array}
    \right)
$$

### Definition 8.1
$$\eqref{chap08_8_02_formal_laurent_series_division}$$で定めた、$$C_{1}, \ldots C_{s}$$から生成される点列をNiederreiter Sequence with generating matricesと呼ぶ。


<div class="end-of-statement" style="text-align: right">■</div>

### Theorem 8.2
Niederreiter sequence with generating matricesはdigital $$(t, s)$$-sequence over $$F_{b}$$であり

$$
    t
    =
    \sum_{i = 1}^{s}
        (e_{i} - 1)
$$

### proof.
以下の記号を定義する。
$$C_{i}$$の$j$行ベクトルを以下で定義する。

$$
\begin{eqnarray}
    \mathbf{c}_{j}^{(i)}
    :=
    (c_{j,0}^{(i)}, c_{j, 1}^{(i)}, \ldots,)
    \nonumber
\end{eqnarray}
$$

行ベクトルの$m$次元ベクトルへの射影を以下で定義する。

$$
\begin{eqnarray}
    j = 1, \ldots,
    \
    i = 1, \ldots, s,
    \
    \pi_{m}(\mathbf{c}_{j}^{(i)})
    & := &
    (c_{j,0}^{(i)}, c_{j, 1}^{(i)}, \ldots, c_{j, m}^{(i)})
    \in
    \mathbb{F}_{b}^{m}
    \nonumber
\end{eqnarray}
$$

Theorem 4.84より、$$\forall m \in \mathbb{N}$$, $$m > \sum_{i=1}^{s}(e_{i} - 1)$$について、$$\forall d_{1}, \ldots, d_{s} \in \mathbb{Z}_{\ge 0}$$, $$1 \le \sum_{i=1}^{s}d_{i} \le m - \sum_{i=1}^{s}(e_{i} - 1)$$を満たすとき、

$$
\begin{equation}
    \{
        \pi_{m}(c_{j}^{(i)})
    \}_{i = 1, \ldots, s,\ j = 1, \ldots, d_{i}}
    \label{chap08_generating_sub_matrix}
\end{equation}
$$

が線形独立であれば良い。
$m$, $$d_{1}, \ldots, d_{s}$$が上で与えられているとする。
このとき、$$\eqref{chap08_generating_sub_matrix}$$が線形独立でないとする。
ある$$f_{j}^{(i)}$$

$$
    \forall i = 1, \ldots, s,
    \
    \forall j = 1, \ldots, m,
    \
    \exists f_{j}^{(i)} \in \mathbb{F}_{b}
    \
    \mathrm{ s.t. }
    \
    \forall r = 0, \ldots, m,
    \
    \sum_{i=1}^{s}
        \sum_{j=1}^{m}
            f_{j}^{(i)}
            c_{j, r}^{(i)}
    =
    0
$$


<div class="QED" style="text-align: right">$\Box$</div>

### Generalized Niederreiter sequence

## Reference

