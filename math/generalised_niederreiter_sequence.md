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
    * 生成する点列の最大の数を$b$進展開したときの桁数とする
    * 多くの場合は、32bitの整数が点の最大の数なので、$m=32, 64$となる
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
* $$y_{i, k}^{j}(x)$$,
    * $i \ge 1$, $j = 1, \ldots, d$, $0 \le k < s_{j}$,
    * $i$番目の$j$次元の点列の生成に用いる多項式 
    * $$\{y_{i, k}^{j} \}_{k = 0, \ldots, s_{j}-1}$$は各$j, i$について、$$p_{j}$$で割った線形独立

$$
\begin{equation}
    1 \le j \le d,
    \
    1 \le i,
    \
    0 \le k < e_{j},
    \
    \frac{
        y_{i, k}^{j}(x)
    }{
        p_{j}(x)^{i}
    }
    =:
    \sum_{r=0}^{\infty}
        a^{j}_{i, k}(r)x^{-r-1}
    \label{def_laurent_series_dvision}
\end{equation}
$$

$$
\begin{eqnarray}
    j = 1, \ldots, d,
    \quad
    C_{j}
    & := &
        c_{i, r}^{j}
        \quad
        i \ge 1,
        \
        r \ge 0
    \nonumber
    \\
    & := &
        a^{j}_{Q(i,j) + 1, k(i,j)}(r)
        \quad
        i \ge 1,
        \
        r \ge 0
    \nonumber
\end{eqnarray}
$$

ここで、$$Q(i, j) \in \mathbb{Z}_{\ge 0}$$は$i - 1$を$$s_{j}$$で割った商で、$$0 \le k(i, j) < s_{j}$$はその余りである。
つまり、

$$
\begin{eqnarray}
    i - 1
    & = &
        Q(i, j)
            s_{j}
        +
        k(i, j),
    \quad
    0 \le k(i, j) < s_{j}
\end{eqnarray}
$$

が成り立つ。
$Q, k$は多項式$$y_{i, k}^{(j)}$$の$i, k$を決めている
$n$の$b$進数表現を$$n = (\cdots, n_{m} \cdots n_{1})_{b}$$とすれば、$n$番目の点の$j$次元目の値$$x_{n}^{(j)}$$を以下で定めたものが、Generalized Niederreiter Sequenceとなる。

$$
\begin{eqnarray}
    \left(
        \begin{array}{c}
            x_{n, 1}^{(j)} \\
            x_{n, 2}^{(j)} \\
            \vdots
        \end{array}
    \right)
    & := &
        \left(
            \begin{array}{cccccc}
                c_{1, 1}^{(j)}
                &
                    c_{1, 2}^{(j)}
                &
                    \cdots
                &
                    c_{1, m}^{(j)}
                &
                    \cdots
                \\
                c_{2, 1}^{(j)}
                &
                    c_{2, 2}^{(j)}
                &
                    \cdots
                &
                    c_{2, m}^{(j)}
                &
                    \cdots
                \\
                \vdots
                &

                &
                    \ddots
                &
                    \vdots
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
                &
                    \cdots
                \\
                \vdots
                &
                    \vdots
                &
                    \vdots
                &
                    \vdots
                &
                    \vdots
            \end{array}
        \right)
        \left(
            \begin{array}{c}
                n_{1} \\
                \vdots \\
                n_{m} \\
                \vdots
            \end{array}
        \right)
    \nonumber
    \\
    x_{n}^{(j)}
    & := &
        \sum_{i=1}^{\infty}
            \frac{x_{n, i}^{(j)}}{b^{i}}
    \label{def_generalized_niederreiter_sequence_n_point_j_dim}
\end{eqnarray}
$$

実用的には、$$c_{i, r}^{j}$$の$i, r$は$m$まで考えれば十分である。
$r$については、$n$は32bitないし、64bitの整数として表現されるからその$b$進表現は、$b=2$で高々64で$b$が大きくなればもっと小さくなる。
また、$i$については、多くのコンピュータで浮動小数点数は32bitないし64bitで、仮数部についてはそれぞれ24 bit, 53bitであるから$$\eqref{def_generalized_niederreiter_sequence_n_point_j_dim}$$の$i$は$b=2$で高々53で十分である。
$i < r = m$として考えれば十分だが、計算の簡便さのため、両方$m$と同じにとり、正方行列とする場合もある。
以下では記述の簡単さのために、正方行列として議論する。

これをふまえて、$i, r$を$m$に制限すると$n$の$b$進数表現を$$n = (n_{m} \cdots n_{1})_{b} \in \mathbb{F}_{b}^{m}$$となり、行列表現は

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
            c_{m, 1}^{(j)}
            &
                c_{m, 2}^{(j)}
            &
                \cdots
            &
                c_{m, m}^{(j)}
        \end{array}
    \right)
$$

である。

$$
\begin{eqnarray}
    \left(
        \begin{array}{c}
            x_{n, 1}^{(j)} \\
            x_{n, 2}^{(j)} \\
            \vdots \\
            x_{n, m}^{(j)}
        \end{array}
    \right)
    & := &
        C_{j}
        \left(
            \begin{array}{c}
                n_{1} \\
                \vdots \\
                n_{m}
            \end{array}
        \right)
    \nonumber
    \\
    x_{n}^{(j)}
    & := &
        \sum_{i=1}^{m}
            \frac{x_{n, i}^{(j)}}{b^{i}}
\end{eqnarray}
$$

として、$n$番目の$j$次元目の点$$x_{n}^{(j)}$$を生成する。

以下の議論のために、$n$の$b$進表現を$$\mathbb{F}_{b}^{m}$$にmapする関数を$$\gamma_{b, m}$$として定義する。
さて、ここで次の写像$$\mathfrak{G}: \mathbb{Z}_{\ge 0} \rightarrow \mathbb{F}_{b}^{m}$$が存在するとしよう。

$$
\begin{eqnarray}
    \mathfrak{G}(n + 1)
    & = &
        \mathfrak{G}(n)
        +
        a(n)
        \mathbf{e}_{l(n)}
    \nonumber
    \\
    \{
        \mathfrak{G}(n)
    \}_{n = 0, \ldots, b^{m} - 1}
    & = &
        \{
            \gamma_{b,m}(n)
        \}_{n = 0, \ldots, b^{m} - 1}
    \nonumber
\end{eqnarray}
$$

ここで、$$l(n)$$は$n$に依存した添字で、$$\mathbf{e}_{l(n)}$$は単位ベクトル、$$a(n) \in \mathbb{F}_{b}$$である。
よって、

$$
\begin{eqnarray}
    C_{j}
    \mathfrak{G}(n + 1)
    & = &
        C_{j}
        \mathfrak{G}(n)
        +
        a(n)
        c^{(j)}_{\cdot, l(n)}
    \nonumber    
    \\
    \{
        C_{j}
        \mathfrak{G}(n)
    \}_{n = 0, \ldots, b^{m} - 1}
    & = &
        \{
            x_{n}
        \}_{n = 0, \ldots, b^{m} - 1}
    \nonumber
\end{eqnarray}
$$

$$c^{(j)}_{\cdot, l(n)}$$は$C_{j}$の$l(n)$列目の列ベクトルである。
よって、$b^{m}-1$個の点を使う場合は、一つ前の点と生成行列の列ベクトルの和で計算できる。
$b=2$の時は、Gray codeを用いれば上の性質を満たす$\mathfrak{G}$を構成できる。
一般の場合は、Gray codeの性質を一般化したGray codeを用いて$\mathfrak{G}$を構成できる。

## Gray map and Gray code
ここでは、基数$b$のGray codeを定義する。

* $p$
    * 素数
* $m \in \mathbb{N}$
* $b := p^{m}$
* $$\mathbb{F}_{p} := \mathbb{Z} / p \mathbb{Z}$$,
* $$f(x) \in \mathbb{F}_{p}[x]$$,
    * $\deg(f) = m$
    * 既約多項式

$$
\begin{eqnarray}
    \mathbb{Z}_{b}
    & := &
        \mathbb{Z} / b \mathbb{Z}
    \nonumber
    \\
    & = &
        \{0, 1, \ldots, p^{m}-1\}
    \nonumber
    \\
    \mathbb{F}_{b}
    & := &
        \mathbb{F}_{p}[x] / (f(x))
    \nonumber
    \\
\end{eqnarray}
$$

* $$\hat{\phi}: \mathbb{Z}_{b} \rightarrow \mathbb{F}_{b}$$,
    * 全単射
    * 整数環と有限体の対応
    * 整数環の元を整数と見て、$p$進展開

$$
\begin{eqnarray}
    n
    & := &
        \sum_{k=0}^{N-1}
            a_{k} p^{k}
        \in \mathbb{Z}_{b},
    \
    (N \le m)
    \nonumber
    \\
    a_{k}
    & \in &
        \{0, \ldots, p-1 \},
    \nonumber
    \\
    \hat{\phi}(n)
    & := &
        \sum_{k=0}^{N-1}
            a_{k}x^{k}
    \label{def_phi}
\end{eqnarray}
$$

要素ごとに$\hat{\phi}$を作用させた写像を$$\phi: \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow \mathbb{F}_{b}^{\mathbb{Z}_{\ge 0}}$$とする。

* $$\Phi: \mathbb{Z}_{\ge 0} \rightarrow \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$,
    * 非負整数の$b$進数展開

$$
\begin{eqnarray}
    n
    & := &
        \sum_{k=0}^{N-1}a_{k}b^{k} \in \mathbb{Z}_{\ge 0},
    \nonumber
    \\
    a_{k}
    & \in &
        \{0, \ldots, b-1 \},
    \nonumber
    \\
    \Phi(n)
    & := &
        (a_{0}, a_{1}, \ldots, a_{N-1}, 0, \ldots)^{\mathrm{T}}
    \label{def_Phi}
\end{eqnarray}
$$

* $$\Psi: \mathbb{F}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow [0, 1]$$,

$$
\begin{eqnarray}
    \mathbf{n}
    & := &
        (a_{0}, \ldots, a_{N-1}, 0, \ldots )^{\mathrm{T}}
        \in \mathbb{F}_{b}^{\mathbb{Z}_{\ge 0}}
    \nonumber
    \\
    \Psi(\mathbf{n})
    & = &
        \frac{\hat{\phi}^{-1}(a_{0})}{b}
        +
        \frac{\hat{\phi}^{-1}(a_{1})}{b^{2}}
        +
        \frac{\hat{\phi}^{-1}(a_{2})}{b^{2}}
        +
        \cdots
    \nonumber
\end{eqnarray}
$$

これらを合わせると、$$\Psi \circ \phi \circ \Phi: \mathbb{Z}_{\ge 0} \rightarrow [0, 1]$$となる。

### Theorem
* $$n := \sum_{i=0}^{N-1} a_{k}p^{k} \in \mathbb{Z}_{b}$$,
    * $$a_{k} \in \{0, 1, \ldots, p -1 \}$$,

ここで、係数が$p-1$でなくなる最初の添字を

$$
\begin{equation}
    \alpha(n)
    :=
    \begin{cases}    
        \min\{k \ge 0 \mid a_{k} \neq p - 1 \}
            & (n \neq b - 1)
            \\
        N - 1
            & (n = b - 1) 
    \end{cases}
    \label{def_alpha}
\end{equation}
$$

とおくと、

$$
\begin{eqnarray}
    \hat{\phi}(n + 1)
    =
    \hat{\phi}(n)
    +
    \sum_{k=0}^{\alpha(n)}
        x^{k}
    \label{property_of_phi}
\end{eqnarray}
$$

となる。

### proof.
左辺は

$$
\begin{eqnarray}
    \hat{\phi}(n + 1)
    & = &
        \hat{\phi}
        \left(
            \sum_{k=0}^{N-1}
                a_{k}p^{k}
            +
            1
        \right)
    \nonumber
    \\
    & = &
        \hat{\phi}
        \left(
            \sum_{k=0}^{\alpha(n)-1}
                (p - 1)p^{k}
            +
                a_{\alpha(n)}p^{\alpha(n)}
            +
            \sum_{k=\alpha(n) + 1}^{N-1}
                a_{k}p^{k}
            +
            1
        \right),
    \nonumber
    \\
    & = &
        \hat{\phi}
        \left(
            \sum_{k=0}^{\alpha(n)-1}
                (p - 1)p^{k}
            +
                a_{\alpha(n)}p^{\alpha(n)}
            +
            \sum_{k=\alpha(n) + 1}^{N-1}
                a_{k}p^{k}
            +
            1
        \right)
    \nonumber
    \\
    & = &
        \hat{\phi}
        \left(
            p^{\alpha(n)}
            +
                a_{\alpha(n)}p^{\alpha(n)}
            +
            \sum_{k=\alpha(n) + 1}^{N-1}
                a_{k}p^{k}
        \right)
    \nonumber
    \\
    & = &
        \hat{\phi}
        \left(
            (a_{\alpha(n)} + 1)p^{\alpha(n)}
            +
            \sum_{k=\alpha(n) + 1}^{N-1}
                a_{k}p^{k}
        \right)
    \nonumber
    \\
    & = &
        (a_{\alpha(n)} + 1)x^{\alpha(n)}
        +
        \sum_{k=\alpha(n) + 1}^{N-1}
            a_{k}x^{k}
    \nonumber
\end{eqnarray}
$$

また右辺は

$$
\begin{eqnarray}
    \hat{\phi}(n)
    +
    \sum_{k=0}^{\alpha(n)}
        x^{k}
    & = &
        \sum_{k=0}^{N-1}
            a_{k}x^{k}
        +
        \sum_{k=0}^{\alpha(n)}
            x^{k}
    \nonumber
    \\
    & = &
        \sum_{k=\alpha(n) + 1}^{N-1}
            a_{k}x^{k}
        +
        (a_{\alpha(n)} + 1)
            x^{\alpha(n)}
        +
        \sum_{k=0}^{\alpha(n) - 1}
            (a_{k} + 1)x^{k}
    \nonumber
    \\
    & = &
        \sum_{k=\alpha(n) + 1}^{N-1}
            a_{k}x^{k}
        +
        (a_{\alpha(n)} + 1)
            x^{\alpha(n)}
        +
        \sum_{k=0}^{\alpha(n) - 1}
            (p - 1 + 1)x^{k}
    \nonumber
    \\
    & = &
        \sum_{k=\alpha(n) + 1}^{N-1}
            a_{k}x^{k}
        +
        (a_{\alpha(n)} + 1)x^{\alpha(n)}
    \nonumber
\end{eqnarray}
$$

よって、成り立つ。

<div class="QED" style="text-align: right">$\Box$</div>


### Definition. Gray Code
$$G_{b}: \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$を

$$
\begin{equation}
    \mathbf{y}
    :=
    (y_{0}, y_{1}, \ldots)^{\mathrm{T}}
    \in \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}},
    \
    G_{b}(\mathbf{y})
    :=
    (y_{0}-y_{1}, y_{1} - y_{2}, \ldots)^{\mathrm{T}}
    \label{def_gray_code}
\end{equation}
$$

と定める。
この時、$$v \in \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$に対して、$G_{b}(v)$を基数$b$の$v$のGray codeという。

<div class="end-of-statement" style="text-align: right">■</div>

### Remarks.
$b = 2$の時、通常の意味のGray codeに一致する。
また、$G$は和を保存する。

$$
\begin{eqnarray}
    v_{1} + v_{2}
    & = &
        (y_{1,0}, y_{1,1}, \ldots)^{\mathrm{T}}
        +
        (y_{2,0}, y_{2,1}, \ldots)^{\mathrm{T}}
    \nonumber
    \\
    & := &
        (y_{1,0}+y_{2,0}, y_{1,1}+y_{2,1}, \ldots)^{\mathrm{T}}
    \nonumber
    \\
    G(v_{1}) + G(v_{2})
    & = &
        (y_{1,0} - y_{1, 1}, y_{1,1} - y_{1, 2}, \ldots)^{\mathrm{T}}
        +
        (y_{2,0} - y_{2, 1}, y_{2,1} - y_{1, 2}, \ldots)^{\mathrm{T}}
    \nonumber
    \\
    & = &
        \left(
            y_{1,0} + y_{2,0}
            -
            (y_{1, 1} + y_{2, 1}),
            y_{1,1} + y_{2,1}
            -
            (y_{1, 2} + y_{1, 2}),
            \cdots
        \right)^{\mathrm{T}}
    \nonumber
    \\
    & = &
        G(v_{1} + v_{2})
    \nonumber
\end{eqnarray}
$$

更に、

$$
    \mathbf{e}_{k}
    :=
    (0, \ldots, 0, \stackrel{k}{\stackrel{\vee}{1}}, 0, \ldots)
$$

とすると、$-1 = b - 1 (\mathrm{mod}\ b)$より

$$
\begin{eqnarray}
    G(\mathbf{e}_{k})
    & = &
        (
            0,
            \ldots,
            0,
            \stackrel{k-1}{\stackrel{\vee}{-1}},
            \stackrel{k}{\stackrel{\vee}{1}},
            0,
            \ldots
        )
    \nonumber
    \\
    & = &
        (
            0,
            \ldots,
            0,
            \stackrel{k-1}{\stackrel{\vee}{b - 1}},
            \stackrel{k}{\stackrel{\vee}{1}},
            0,
            \ldots
        )
    \nonumber
\end{eqnarray}
$$

である。

<div class="end-of-statement" style="text-align: right">■</div>

### Theorem. Property of Gray code
* $$n := \sum_{k=0}^{N-1} a_{k}b^{k} \in \mathbb{Z}_{\ge 0}$$,
    * $$a_{k} \in \{0, \ldots, b - 1\}$$,

$$
    l(n)
    :=
    \min
    \left\{
        k \ge 0
        \mid
        a_{k} \neq b - 1
    \right\}
$$

とおく。
このとき、

$$
\begin{equation}
    G(\Phi(n + 1))
    =
    G(\Phi(n))
    +
    \mathbf{e}_{l(n)}
    \label{property_of_gray_code}
\end{equation}
$$

である。
ただし、$$\mathbf{e}_{k} \in \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$は$k$番目の要素が1でほかは0である。

### proof.
$\forall i = 0, \ldots, l(n) - 1,\ a_{i} = b - 1$に注意する。

$$
\begin{eqnarray}
    G(\Phi(n + 1))
    & = &
        (
            G
            \circ
            \Phi
        )
        \left(
            \sum_{k=0}^{N-1}
                a_{k}b^{k}
            +
            1
        \right)
    \nonumber
    \\
    & = &
        (
            G
            \circ
            \Phi
        )
        \left(
            \sum_{k=0}^{l(n)-1}
                a_{k}b^{k}
            +    
            \sum_{k=l(n)}^{N-1}
                a_{k}b^{k}
            +
            1
        \right)
    \nonumber
    \\
    & = &
        (
            G
            \circ
            \Phi
        )
        \left(
            \sum_{k=0}^{l(n)-1}
                (b - 1)b^{k}
            +
            \sum_{k=l(n)}^{N-1}
                a_{k}b^{k}
            +
            1
        \right)
    \nonumber
    \\
    & = &
        (
            G
            \circ
            \Phi
        )
        \left(
            b^{l(n)}
            +
            \sum_{k=l(n)}^{N-1}
                a_{k}b^{k}
        \right)
    \nonumber
    \\
    & = &
        (
            0,
            \ldots,
            0,
            -1,
            \stackrel{l(n)}{\stackrel{\vee}{1}},
            0,
            \ldots,
        )
        +
        (
            G
            \circ
            \Phi
        )
        \left(
            \sum_{k=l(n)}^{N-1}
                a_{k}b^{k}
        \right)
    \nonumber
    \\
    & = &
        \mathbf{e}_{l(n)}
        +
        (
            0,
            \ldots,
            0,
            \stackrel{l(n) - 1}{\stackrel{\vee}{b - 1}},
            0,
            \ldots,
        )
        +
        (
            G
            \circ
            \Phi
        )
        \left(
            \sum_{k=l(n)}^{N-1}
                a_{k}b^{k}
        \right)
\end{eqnarray}
$$

一方、

$$
\begin{eqnarray}
    G(\Phi(n))
    & = &
        G
        \left(
            \Phi
            \left(
                \sum_{k=0}^{N-1}
                    a_{k}b^{k}
            \right)
        \right)
    \nonumber
    \\
    & = &
        G
        \left(
            \Phi
            \left(
                \sum_{k=0}^{l(n) - 1}
                    a_{k}b^{k}
                +
                \sum_{k=l(n)}^{N-1}
                    a_{k}b^{k}
            \right)
        \right)
    \nonumber
    \\
    & = &
        G
        \left(
            \Phi
            \left(
                \sum_{k=0}^{l(n) - 1}
                    (b - 1)b^{k}
            \right)
        \right)
                +
        G
        \left(
            \Phi
            \left(
                \sum_{k=l(n)}^{N-1}
                    a_{k}b^{k}
            \right)
        \right)
    \nonumber
    \\
    & = &
        (
            0,
            \ldots,
            0,
            \stackrel{l(n)-1}{\stackrel{\vee}{b - 1}},
            0,
            \ldots
        )
        + 
        G
        \left(
            \Phi
            \left(
                \sum_{k=l(n)}^{N-1}
                    a_{k}b^{k}
            \right)
        \right)
    \nonumber
\end{eqnarray}
$$

よって、一致する。

<div class="QED" style="text-align: right">$\Box$</div>

### Remarks
和が、$b - 1 = -1 (\mathrm{mod}\ b)$となることを使っている。

<div class="end-of-statement" style="text-align: right">■</div>

### Theorem
* $$n := \sum_{k=0}^{N-1}a_{k}b^{k} \in \mathbb{Z}_{\ge 0}$$,
    * $$a_{k} \in \{0, \ldots, b - 1\}$$,
    * $b$進展開
* $$\phi: \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow \mathbb{F}_{b}^{\mathbb{Z}_{\ge 0}}$$,
    * $$\eqref{def_phi}$$,
* $$G: \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$,
    * gray map
* $$\Phi: \mathbb{Z}_{\ge 0} \rightarrow \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$,
    * $$\eqref{def_Phi}$$,

とおくと、

$$
    (\phi \circ G \circ \Phi)
    (n+1)
    =
    (\phi \circ G \circ \Phi)
    (n)
    +
    \sum_{k=0}^{\alpha(a_{l(n)} - a_{l(n) + 1})}
        x^{k}
    \mathbf{e}_{l(n)}
$$

である。
また、$b = p$のときは

$$
    (\phi \circ G \circ \Phi)
    (n+1)
    =
    (\phi \circ G \circ \Phi)
    (n)
    +
    \mathbf{e}_{l(n)}
$$

となる。

### proof.
$$\eqref{property_of_phi}$$より、

$$
\begin{eqnarray}
    \hat{\phi}(a_{k^{\prime}} - a_{k^{\prime} + 1} + 1)
    & = &
        \hat{\phi}(a_{k^{\prime}} - a_{k^{\prime} + 1})
        +
        \sum_{k=0}^{\alpha(a_{k^{\prime}} - a_{k^{\prime} + 1})}
            x^{k}
    \nonumber
\end{eqnarray}
$$

前定理より、

$$
\begin{eqnarray}
    (\phi \circ G \circ \Phi)
    (n+1)
    & = &
        \phi
        \left(
            (G \circ \Phi)
            (n)
            +
            \mathbf{e}_{l(n)}
        \right)
    \nonumber
    \\
    & = &
        \phi
        \left(
            (
                (a_{0} - a_{1}),
                \ldots,
                (a_{l(n)-1} - a_{l(n)}),
                (a_{l(n)} - a_{l(n) + 1}),
                \ldots
            )^{\mathrm{T}}
            +
            (
                0,
                \ldots,
                0,
                \stackrel{l(n)}{\stackrel{\vee}{1}},
                0,
                \ldots
            )^{\mathrm{T}}
        \right)
    \nonumber
    \\
    & = &
        \phi
        \left(
            (
                (a_{0} - a_{1}),
                \ldots,
                (a_{l(n)-1} - a_{l(n)}),
                (a_{l(n)} - a_{l(n) + 1})
                +
                1,
                \ldots
            )^{\mathrm{T}}
        \right)
    \nonumber
    \\
    & = &
        (
            \hat{\phi}(a_{0} - a_{1}),
            \ldots,
            \hat{\phi}(a_{l(n)-1} - a_{l(n)}),
            \hat{\phi}
            (
                a_{l(n)} - a_{l(n) + 1}
                +
                1
            ),
            \hat{\phi}(a_{l(n) + 1} - a_{l(n) + 2}),
            \ldots
        )^{\mathrm{T}}
    \nonumber
    \\
    & = &
        (
            \hat{\phi}(a_{0} - a_{1}),
            \ldots,
            \hat{\phi}(a_{l(n) - 1} - a_{l(n)}),
            \hat{\phi}
            (
                a_{l(n)} - a_{l(n) + 1}
            )
            +
            \sum_{k=0}^{\alpha(a_{l(n)} - a_{l(n) + 1})}
                x^{k}
            ,
            \hat{\phi}(a_{l(n) + 1} - a_{l(n) + 2}),
            \ldots
        )^{\mathrm{T}}
    \nonumber
    \\
    & = &
        (
            \hat{\phi}(a_{0} - a_{1}),
            \ldots,
            \hat{\phi}
            (
                a_{l(n)-1} - a_{l(n)}
            ),
            \hat{\phi}(a_{l(n)} - a_{l(n) + 1}),
            \ldots
        )^{\mathrm{T}}
        +
        (
            0,
            \ldots,
            0,
            \stackrel{l(n)}{\stackrel{\vee}{
                \sum_{k=0}^{\alpha(a_{l(n)} - a_{l(n) + 1})}
                    x^{k}
            }},
            0,
            \ldots
        )^{\mathrm{T}}
    \nonumber
    \\
    & = &
        (\phi \circ G \circ \Phi)(n)
        +
        (
            0,
            \ldots,
            0,
            \stackrel{l(n)}{\stackrel{\vee}{
                \sum_{k=0}^{\alpha(a_{l(n)} - a_{l(n) + 1})}
                    x^{k}
            }},
            0,
            \ldots
        )^{\mathrm{T}}
    \nonumber
    \\
    & = &
        (\phi \circ G \circ \Phi)(n)
        +
        \sum_{k=0}^{\alpha(a_{l(n)} - a_{l(n) + 1})}
            x^{k}
        \mathbf{e}_{l}
    \nonumber
\end{eqnarray}
$$

定理の前半は証明された。
定理の後半は、$b = p$であれば、$$a_{k} \in \mathbb{Z}_{p}$$なので、$$a_{k} - a_{k} \in \mathbb{Z}_{p}$$である。
これと、$$\forall a \in \{0, \ldots, p - 1\}\ \alpha(a) = 0$$より、$$\alpha(a_{l(n)} - a_{l(n) + 1}) = 0$$である。


<div class="QED" style="text-align: right">$\Box$</div>

### Remark
$$\mathbb{F}_{b} = \mathbb{F}_{p}[x] / (f(x))$$より、$p=2$, $b=4$, $f(x) = x^{2} + x + 1$とすると、
$$a_{l(n)}, a_{l(n)+1} \in \{0, \ldots, b-1\}$$について、$$a := a_{l(n)} - a_{l(n)+1} \ (\mathrm{mod}\ p)$$とおいて

* $p = 2$
* $m = 2$
* $b = p^{2} = 4$
* $n = 19 = 3 \cdot 4^{0} + 0 \cdot 4 + 1 \cdot 4^{2}$
    * $$a_{0} = 3, a_{1} = 0, a_{2} = 1$$,
    * $$ l(n) = 1$$,
    * $$a_{1} - a_{2} = -1 = 4 - 1 = 3 (\mathrm{mod}\ b)$$,
    * $$ 3 = 1 \cdot 2^{0} + 1 \cdot 2^{1}$$,
    * $$\alpha(a_{l(n)} - a_{l(n) + 1}) = 1$$,
    * $$(1 + x) = 3 \in \mathbb{F}_{4}$$,
* $n = 101 = 1 \cdot 4^{0} + 1 \cdot 4 + 3 \cdot 4^{2} + 1 \cdot 4^{3} = 1 + 4 + 32 + 64$
    * $$a_{0} = 1, a_{1} = 1, a_{2} = 2, a_{3} = 1$$,
    * $l(n) = 0$
    * $$a_{0} - a_{1} = 0$$,
    * $$0$$,
    * $$\alpha(a_{l(n)} - a_{l(n)+1}) = 0$$,
    * $$1 \in \mathbb{F}_{4}$$,

* $n = 1011 \mid 1101 \mid 1110 \mid 1111$
    * $l(n) = 1$
    * $1101 ^ 1110$

<div class="end-of-statement" style="text-align: right">■</div>

## Relation to sobol sequence
Sobol sequenceはGeneralized Niederreiter Sequenceの一種とみなすことができる。 

* $m = 1$
* $b = 2$
* $$j \in \{2, \ldots, d\}$$,
    * 次元
* $p_{j}(x)$
    * 次数の小さい方から並べたときの$(j - 1)$番目のprimitive polynomial
    * 次数が同じ場合は、$p(2)$を整数として計算した時の値から小さい順
        * $p(x) = x^{2} + 1$
        * $p(2) = 4 + 1 = 5$
* $$s_{j} = \mathrm{deg}(p_{j}(x))$$,
    * 次元$j$の多項式の次数
* $$y_{i, k}^{j} = g_{k}^{j}\ (0 \le k < s_{j},\ 1 \le j \le d,\ 1 \le i)$$,
    * $$g_{0}^{j}(x), \ldots, g_{s_{j}-1}^{j}(x)$$,
        * $$\mathrm{deg}(g_{j, k}) = s_{j} - k + 1$$,
        * 多項式
    * 例えば$$g_{j, k}(x):= x^{s_{j} - k + 1} + \sum_{n=0}^{s_{j} - k} a_{n}x^{n}$$,
        * $$a_{n} \in \mathbb{F}_{2}$$,

ここで、

$$
    \{ y_{i, k}^{j} \ (\mathrm{mod}\ p_{i}) \}_{0 \le k < s_{j}}
    =
    \{ g_{k}^{j} \ (\mathrm{mod}\ p_{i}) \}_{0 \le k < s_{j}}
$$

が一次独立である必要がある。
例えば、classical niederreiter sequenceでは$$a_{s_{j} - k} = 0 \ (k = 0, \ldots, s_{j})$$とし、

$$
\begin{equation}
    \begin{array}{rclrclrclrclrcl}
            p_{1}(x)
        & := &
            x,
        & &
            g_{0}^{1}(x)
        & := &
            1
        & &
        & &
        & &
        & &
        \\
            p_{2}(x)
        & := &
            x + 1,
        & &
            g_{0}^{2}(x)
        & := &
            1
        & &
        & &
        & &
        & &
        \\
            p_{3}(x)
        & := &
            x^{2} + x + 1,
        & &
            g_{0}^{3}(x)
        & := &
            1
        & &
            g_{1}^{3}(x)
        & := &
            x
        & &
        & &
        \\
            p_{4}(x)
        & := &
            x^{3} + x + 1
        & &
            g_{0}^{4}(x)
        & := &
            1
        & &
            g_{1}^{4}(x)
        & := &
            x
        & &
            g_{2}^{4}(x)
        & := &
            x^{2}
    \end{array}
\end{equation}
$$

となる。
生成行列を具体的に求める。
$j=1$次元目は

$$
\begin{eqnarray}
    \frac{
        y_{1, 0}^{1}(x)
    }{
        p_{1}(x)^{1}
    }
    & = &
        \frac{
            g_{0}^{1}(x)
        }{
            p_{1}(x)^{1}
        }
    \nonumber
    \\
    & =  &
        \frac{
            1
        }{
            x
        }
    \nonumber
    \\
    & = &
        x^{-1}
\end{eqnarray}
$$

$j=2$次元目は

$$
\begin{eqnarray}
    \frac{
        y_{1, 0}^{2}(x)
    }{
        p_{2}(x)^{1}
    }
    & = &
        \frac{
            g_{0}^{2}(x)
        }{
            p_{2}(x)^{1}
        }
    \nonumber
    \\
    & =  &
        \frac{
            1
        }{
            x + 1
        }
    \nonumber
    \\
    & = &
        \sum_{i=1}^{\infty}
            x^{-1}
\end{eqnarray}
$$

$j=3$次元目は

$$
\begin{eqnarray}
    \frac{
        g_{0}^{1}(x)
    }{
        p_{3}(x)^{1}
    }
    & =  &
        \frac{
            1
        }{
            x^{2} + x + 1
        }
    \nonumber
    \\
    & = &
        ?
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{
        g_{0}^{1}(x)
    }{
        p_{3}(x)^{2}
    }
    & =  &
        \frac{
            x
        }{
            x^{2} + x + 1
        }
    \nonumber
    \\
    & = &
        \sum_{k=0}^{\infty}
            (
                x^{-3k+1}
                +
                x^{-3k+2}
            )
\end{eqnarray}
$$

$j=4$次元目は

$$
\begin{eqnarray}
    \frac{
        g_{0}^{1}(x)
    }{
        p_{4}(x)^{1}
    }
    & =  &
        \frac{
            1
        }{
            x^{3} + x + 1
        }
    \nonumber
    \\
    & = &
       ?
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{
        g_{0}^{1}(x)
    }{
        p_{4}(x)^{1}
    }
    & =  &
        \frac{
            x
        }{
            x^{3} + x + 1
        }
    \nonumber
    \\
    & = &
        ?
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{
        g_{0}^{1}(x)
    }{
        p_{4}(x)^{1}
    }
    & =  &
        \frac{
            x^{2}
        }{
            x^{3} + x + 1
        }
    \nonumber
    \\
    & = &
       ?
\end{eqnarray}
$$

## degree of $p_{j}$
実用的には、$r$は32, 64までしか有効でない。
よって、$$\eqref{def_laurent_series_dvision}$$の係数は32, 64までしか使われない。
もし$r$を32, 64に制限するならば、$$\eqref{def_laurent_series_dvision}$$の係数をこの範囲に収める必要がある。
$$n := \mathrm{deg}(y_{i,k}^{(j)})$$, $$m := \deg(p_{j}(x)^{i})$$とおき、$$n < m$$とすると$$\eqref{def_laurent_series_dvision}$$の0でない係数は、$$-m + n, \ldots, -m$$の範囲にある。
よって、$$0 \le m - n  \le m \le 32, 64$$ととる必要がある。


$$s_{j} = \mathrm{deg}(p_{j})$$の次数がどのようとるべきかについて考える。
$i$の最大値は24か53であるから、この範囲において$Q, k$がどのような値になるかを考える。
$Q, k$は多項式$$y_{i, k}^{(j)}$$の$i, k$を決めている。

