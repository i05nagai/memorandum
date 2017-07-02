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

ここで、$$Q(i, j) \in \mathbb{Z}_{\ge 0}$$と$$0 \le k(i, j) < s_{j}$$は$i ,j$を決めるごとに以下を満たすように決める。

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
上の表現は以下と等価である。

$$
\begin{eqnarray}
    Q(i, j)
    & = &
        \left\lfloor
            \frac{
                i - 1
            }{
                s_{j}
            }
        \right\rfloor
    \\
    k(i, j)
    & = &
        (i - 1) - Q(i, j)s_{j}
    \nonumber
\end{eqnarray}
$$

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
    \gamma_{b,m}(i)
    :=
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
さて、ここで次の写像$$\mathfrak{G}: \mathbb{Z}_{\ge 0} \rightarrow \mathbb{F}_{b}^{m}$$が存在するとしよう。

$$
\begin{eqnarray}
    \mathfrak{G}(\gamma_{b,m}(i + 1))
    & = &
        \mathfrak{G}(\gamma_{b,m}(i))
        +
        a(i)
        \mathbf{e}_{l(i)}
    \nonumber
    \\
    \{
        \mathfrak{G}(\gamma_{b,m}(i))
    \}_{i = 0, \ldots, b^{m} - 1}
    & = &
        \{
            \gamma_{b,m}(i)
        \}_{i = 0, \ldots, b^{m} - 1}
    \nonumber
\end{eqnarray}
$$

ここで、$$l(i)$$は$i$に依存した添字で、$$\mathbf{e}_{l(i)}$$は単位ベクトル、$$a(i) \in \mathbb{F}_{b}$$である。
よって、

$$
\begin{eqnarray}
    C_{j}
    \mathfrak{G}(\gamma_{b,m}(i + 1))
    & = &
        C_{j}
        \mathfrak{G}(\gamma_{b,m}(i))
        +
        a(i)
        c^{(j)}_{\cdot, l(i)}
    \nonumber    
    \\
    \{
        C_{j}
        \mathfrak{G}(\gamma_{b,m}(i))
    \}_{i = 0, \ldots, b^{m} - 1}
    & = &
        \{
            x_{i}
        \}_{i = 0, \ldots, b^{m} - 1}
    \nonumber
\end{eqnarray}
$$

$$c^{(j)}_{\cdot, l(i)}$$は$C_{j}$の$l(i)$列目の列ベクトルである。
よって、$b^{m}-1$個の点を使う場合は、一つ前の点と生成行列の列ベクトルの和で計算できる。
$b=2$の時は、Gray codeは$\mathfrak{G}$の性質を満たす。
一般の場合は、Gray codeの性質を一般化したGray codeとして$\mathfrak{G}$をとることができる。

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

要素ごとに$\hat{\phi}$を作用させた写像、$$\phi: \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow \mathbb{F}_{b}^{\mathbb{Z}_{\ge 0}}$$にも同じ記号を用いる。

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
		\sum_{k=0}^{\alpha(n)}
			(a_{k} + 1)x^{k}
	\nonumber
	\\
	& = &
		\sum_{k=\alpha(n) + 1}^{N-1}
			a_{k}x^{k}
		+
		(a_{\alpha_{n}} + 1)x^{\alpha(n)}
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
	G(v_{1} + v_{2})
	& = &
		G(v_{1})
		+
		G(v_{2})
	\nonumber
\end{eqnarray}
$$

更に、

$$
    \mathbf{e}_{k}
    :=
    (0, \ldots, 0, \stackrel{k}{\stackrel{\vee}{1}}, 0, \ldots)
$$

とすると、

$$
    G(e_{k})
    =
    (
        0,
        \ldots,
        0,
        \stackrel{k-1}{\stackrel{\vee}{-1}},
        \stackrel{k}{\stackrel{\vee}{1}},
        0,
        \ldots
    )
$$

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
					(b - 1)_{k}b^{k}
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
\end{eqnarray}
$$

よって、一致する。

<div class="QED" style="text-align: right">$\Box$</div>

### Remarks
和が、$b - 1 = -1 (\mathrm{mod}\ b)$となることを使っている。

<div class="end-of-statement" style="text-align: right">■</div>

### Theorem
* $$n := \sum_{k=0}^{N-1}a_{k}p^{k} \in \mathbb{Z}_{\ge 0}$$,
    * $N \le m$
    * $$a_{k} \in \{0, \ldots, p - 1\}$$,
    * $p$進展開
* $$\phi: \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow \mathbb{F}_{b}^{\mathbb{Z}_{\ge 0}}$$,
    * $$\eqref{def_phi}$$,
* $$G: \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}} \rightarrow \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$,
    * gray map
* $$\Phi: \mathbb{Z}_{\ge 0} \rightarrow \mathbb{Z}_{b}^{\mathbb{Z}_{\ge 0}}$$,
    * $$\eqref{def_Phi}$$,

$$
    \beta(n)
    :=
    \alpha(a_{l(n)} - a_{l(n) + 1})
$$

とおくと、

$$
    (\phi \circ G \circ \Phi)
    (n+1)
    =
    (\phi \circ G \circ \Phi)
    (n)
    +
    \beta(n)
    \mathbf{e}_{l(n)}
$$

である。
特に$b$が素数であれば、$\beta(n) \equiv 1$である。

### proof.
$$\eqref{property_of_phi}$$より、


$$
\begin{eqnarray}
    \hat{\phi}(a_{n} - a_{n + 1} + 1)
    & = &
        \hat{\phi}(a_{n} - a_{n + 1})
        +
        \sum_{k=0}^{\alpha(a_{k} - a_{k+1})}
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
                (a_{l(n)-1} - a_{l(n)})
                +
                1,
                (a_{l(n)} - a_{l(n) + 1}),
                \ldots
            )^{\mathrm{T}}
        \right)
    \nonumber
    \\
    & = &
        (
            \hat{\phi}(a_{0} - a_{1}),
            \ldots,
            \hat{\phi}
            (
                a_{l(n)-1} - a_{l(n)}
                +
                1
            ),
            \hat{\phi}(a_{l(n)} - a_{l(n) + 1}),
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
            )
            +
            \sum_{k=0}^{\alpha(a_{l(n)-1} - a_{l(n)}}
                x^{k}
            ,
            \hat{\phi}(a_{l(n)} - a_{l(n) + 1}),
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
                \sum_{k=0}^{\alpha(a_{l(n)-1} - a_{l(n)})}
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
                \sum_{k=0}^{\alpha(a_{l(n)-1} - a_{l(n)})}
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
        \sum_{k=0}^{\alpha(a_{l(n)-1} - a_{l(n)})}
            x^{k}
        \mathbf{e}_{l}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

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
* $$y_{j, i, k} = g_{j, k}\ (0 \le k < e_{j},\ 1 \le j \le d,\ 1 \le i)$$,
    * $$g_{j, 0}(x), \ldots, g_{j, s_{j}-1}(x)$$,
        * $$\mathrm{deg}(g_{j, k}) = s_{j} - k + 1$$,
        * 多項式
    * 例えば$$g_{j, k}(x):= x^{s_{j} - k + 1} + \sum_{n=0}^{s_{j} - k} a_{n}x^{n}$$,
        * $$a_{n} \in \mathbb{F}_{2}$$,

## Reference

