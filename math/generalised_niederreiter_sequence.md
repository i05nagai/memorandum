---
title: Generalized Niederreiter Sequence
---

## Generalized Niederreiter Sequence

* $b$
    * 基数
* $d$
    * 生成する点列の次元
* $m$
    * $i$番目の点の$b$進展開した時の桁数
* $j = 1, \ldots, d$
    * 次元を表す
* $$i = (i_{m}, \ldots, i_{1})_{b}$$,
    * $i$番目の点とその$b$進数表現
    * $$i_{k} \in \mathbb{F}_{b}$$,
* $$x_{i} := (x_{i, 1}, \ldots, x_{i, d})$$,
    * $i$番目の点を表す
* $p_{j}(x)$
    * $j$番目の次元の生成に用いる原始多項式
    * $$\dim(p_{j}) =: s_{j}$$,
    * 予め生成したい次元数分用意しておく
* $$y_{j, i, l}(x)$$,
    * $i \ge 1$, $j = 1, \ldots, d$, $0 \le l < s_{j}$,
    * $i$番目の$j$次元の点列の生成に用いる多項式 


$$
\begin{equation}
    \frac{
        y_{j, i, l}(x)
    }{
        p_{j}(x)^{i}
    }
    =
    \sum_{r=0}^{\infty}
        a^{(j)}(i, l, r)x^{-r-1}
\end{equation}
$$


$$
\begin{eqnarray}
    C_{j}
    & := &
        c_{i, r}^{(j)}
        \quad
        i \ge 1,
        \
        r \ge 0
    \nonumber
    \\
    & := &
        a^{(j)}(Q(i,j) + 1, k(i,j), r)
        \quad
        1 \le j \le d,
        \
        i \ge 1,
        \
        r \ge 0
    \nonumber
\end{eqnarray}
$$

ここで、$$Q(i, j) \in \mathbb{Z}_{\ge 0}$$と$$k(i, j) \in \mathbb{Z}_{\ge 0}$$は$i ,j$を決めるごとに以下を満たすように決める。

$$
\begin{eqnarray}
    & &
        i - 1 = Q(i, j) s_{j} + k(i, j),
    \nonumber
    \\
    & \Leftrightarrow &
        Q(i, j)
        =
        \frac{
            i - 1 - k(i, j)
        }{
            s_{j}
        }
    \label{equation_of_q}
    \\
    & &
        0 \le k(i, j) < s_{j}
    \nonumber
\end{eqnarray}
$$

具体的には、例えば

* $d = 3$
* $s_{1} = 2$
* $s_{2} = 3$
* $s_{3} = 4$

とすれば


$$
\begin{array}{cccc}
    i-1 & j & s_{j} & k(i,j) & Q(i,j)
    \\
    \hline
    0   & 1 & 2     & 0      & 0
    \\
    0   & 2 & 3     & 0      & 0
    \\
    0   & 3 & 4     & 0      & 0
    \\
    \hline
    1   & 1 & 2     & 1      & 0
    \\
    1   & 2 & 3     & 1      & 0
    \\
    1   & 3 & 4     & 1      & 0
    \\
    \hline
    2   & 1 & 2     & 0      & 1
    \\
    2   & 2 & 3     & 2      & 0
    \\
    2   & 3 & 4     & 2      & 0
    \\
    \hline
    3   & 1 & 2     & 1      & 1
    \\
    3   & 2 & 3     & 0      & 1
    \\
    3   & 3 & 4     & 3      & 0
    \\
    \hline
    4   & 1 & 2     & 0      & 2
    \\
    4   & 2 & 3     & 1      & 1
    \\
    4   & 3 & 4     & 0      & 1
    \\
    \hline
    5   & 1 & 2     & 0      & 2
    \\
    5   & 2 & 3     & 1      & 1
    \\
    5   & 3 & 4     & 1      & 1
    \\
    \hline
    6   & 1 & 2     & 1      & 2
    \\
    6   & 2 & 3     & 0      & 2
    \\
    6   & 3 & 4     & 2      & 1
\end{array}
$$

である。
$i-1$以下で、$i-1$に最も近い$s_{j}$の倍数になるように、$i - 1 - k(i,j)$を定めれば良いことが分かる。
つまり、

$$
\begin{eqnarray}
    e
    & := &
        \max
        \left\{
            e^{\prime} \in \mathbb{Z}_{\ge 0}
            \mid
            i - 1 \ge e^{\prime} s_{j},
        \right\},
    \nonumber
    \\
    k(i, j)
    & = &
        (i - 1) - e s_{j}
    \nonumber
    \\
    Q(i, j)
    & = &
        e
\end{eqnarray}
$$

で、$k(i, j)$を求め、$Q(i, j)$を$$\eqref{equation_of_q}$$で計算すれば良い。
行列表現は

$$
    C_{j}
    =
    \left(
        \begin{array}{ccccc}
            c_{1, 1}^{(j)}
            &
                c_{1, 2}^{(j)}
            &
                \cdots
            &
                c_{1, m}^{(j)}
            \\
            c_{2, 1}^{(j)}
            &
                c_{2, 2}^{(j)}
            &
                \cdots
            &
                c_{2, m}^{(j)}
            \\
            \vdots
            &

            &
                \ddots
            &
                \vdots
            \\
            c_{i, 1}^{(j)}
            &
                c_{i, 2}^{(j)}
            &
                \cdots
            &
                c_{i, m}^{(j)}
            \\
            \vdots
            &
                \vdots
            &
                \vdots
            &
                \vdots
        \end{array}
    \right)
$$

$i$の$b$進数表現を$$i = (i_{m} \cdots i_{1})_{b}$$とすれば

$$
    i
    =
    \left(
        \begin{array}{c}
            i_{1} \\
            \vdots \\
            i_{m}
        \end{array}
    \right)
$$

$$
\begin{eqnarray}
    x_{j}^{(i)}
    :=
    C_{j}
    \left(
        \begin{array}{c}
            i_{1} \\
            \vdots \\
            i_{m}
        \end{array}
    \right)
\end{eqnarray}
$$

として、$i$番目の$j$次元目の点列を生成する。

## Reference

