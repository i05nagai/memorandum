---
title: Chapter2. The Probability Background
book_title: Testing Statistical Hypotheses
book_chapter: 2
---

## 2.3 Statistics and Subfields
* $$(\mathcal{X}, \mathcal{A})$$,
* $$(\mathcal{T}, \mathcal{B})$$,
* $T: \mathcal{X} \rightarrow \mathcal{T}$
    * 可測写像
    * この本では、statistic(統計量)という

$$
\begin{equation}
    \mathcal{A}_{0}
    :=
    T^{-1}(\mathcal{B})
    =
    \{
        T^{-1}(B)
        \mid
        B \in \mathcal{B}
    \}
    \label{chap02_15}
\end{equation}
$$

$T$が全射ならば、

$$
\begin{equation}
    \forall B \in \mathcal{B},
    \
    T
    \circ
    T^{-1}(B)
    =
    B
    \label{chap02_16}
\end{equation}
$$

である。
$T$が単射であるとする。
$\mathcal{T}^{\prime} := T(\mathcal{X}) \subsetneq \mathcal{B}$とおくと、

* $$\mathcal{X} := (a, b) \subseteq \mathbb{R}$$,
* $$\mathcal{A}$$,
    * boreal sets of $(a, b)$
* $$\mathcal{B}$$,
    * boreal sub sets
* $$T(x) := x^{2}$$,
* $$\mathcal{A}_{0} = \mathcal{X} \cap [0, \infty)$$,

### Lemma 2.3.1
* $$(\mathcal{X}, \mathcal{A})$$,
* $$(\mathcal{T}, \mathcal{B})$$,
* $T: \mathcal{X} \rightarrow \mathcal{T}$
* $$T^{-1}(\mathcal{B}) =: \mathcal{A}_{0}$$,
* $f: \mathcal{A} \rightarrow \mathbb{R}$
    * $\mathcal{A}$ measurable function

このとき、$f$が$\mathcal{A}_{0}$ measurable であることと、ある$\mathcal{B}$ measurable function $g$が存在して、

$$
    \forall x \in \mathcal{X},
    \
    f(x) = g(T(x))
$$

となることは同値。

<div class="end-of-statement" style="text-align: right">■</div>

### proof.


<div class="QED" style="text-align: right">$\Box$</div>

### Lemma 2.3.2
* $$(\mathcal{X}, \mathcal{A})$$,
    * 可測空間
* $$(\mathcal{T}, \mathcal{B})$$,
    * 可測空間
* $T: \mathcal{X} \rightarrow \mathcal{T}$
* $\mu$
    * $\sigma$ finite measure over $(\mathcal{X}, \mathcal{A})$
* $\mu^{\*}$
    * measure over $(\mathcal{T}, \mathcal{B})$
* $g: \mathcal{A} \rightarrow \mathbb{R}$
    * $\mathcal{A}$ measurable function

このとき

$$
\begin{equation}
    B \in \mathcal{B},
    \
    \mu^{*}(B)
    =
    \mu(T^{-1}(B))
    \label{chap2_17}
\end{equation}
$$

とすると、以下の積分が定義できるかぎりにおいて以下が成り立つ。

$$
\begin{equation}
    B \in \mathcal{B},
    \
    \int_{T^{-1}(B)}
        g(T(x))
    \ d \mu(x)
    =
    \int_{B}
        g(t)
    \ d \mu^{*}(x)
    \label{chap2_18}
\end{equation}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

## 2.4 Conditional Expectation and Probability

* $P$
    * probability measure over $(\mathcal{X}, \mathcal{A})$
* $T: \mathcal{X} \rightarrow \mathcal{T}$
* $\mathcal{A}_{0}$
    * $T$から誘導されるsigma algebra
* $$f: \mathcal{X} \rightarrow \mathbb{R}_{\ge 0}$$,
    * $\mathcal{A}$可測
    * 可積分
* $X: \Omega \rightarrow \mathcal{X}$

定理2.2.3のRadon-Nikodymより、ある関数$f_{0}$が存在して、

$$
\begin{equation}
    \forall A_{0} \in \mathcal{A}_{0},
    \
    \int_{A_{0}}
        f
    \ d P
    =
    \int_{A_{0}}
        f_{0}
    \ d P
    \label{chap02_19}
\end{equation}
$$

となる。
この$f_{0}$は$(\mathcal{A}_{0}, P)$上一意である。

$$\eqref{chap02_19}$$で定義される$f_{0}$は2つの性質を持つ

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        f(X)
        \mid
        t
    \right]
    & := &
        \mathrm{E}
        \left[
            f(X)
            \mid
            T = t
        \right]
    \nonumber
    \\
    & = &
        \int_{T^{-1}(t)}
            f(x)
        \ d P(x)
    \nonumber
    \\
    & = &
        g(t)
\end{eqnarray}
$$

$$
\begin{equation}
    \forall B \in \mathcal{B},
    \
    \int_{T^{-1}(B)}
        f(x)
    \ dP^{X}(x)
    =
    \int_{B}
        g(t)
    \ dP^{T}(t)
    \label{chap02_20}
\end{equation}
$$

$f$が非負でない場合は、以下で定義する。

$$
    \mathrm{E}
    \left[
    \left.
        f(X)
    \right|
        t
    \right]
    :=
    \mathrm{E}
    \left[
    \left.
        f^{+}(X)
    \right|
        t
    \right]
    -
    \mathrm{E}
    \left[
    \left.
        f^{-}(X)
    \right|
        t
    \right]
$$

### Example 2.4.1 (Order statics)
* $$X_{1}, \ldots, X_{n}$$,
    * $$X:\Omega \rightarrow \mathbb{R}$$,
    * i.i.dの$\mathbb{R}$値の確率変数
    * 分布関数は連続
* $$F^{X}$$
    * $X$の分布関数
* $T: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$

$$
    T(X_{1}, \ldots, X_{n})
    =:
    (X_{(1)}, \ldots, X_{(n)})
$$

ここで、$$X_{(1)} \le \cdots \le X_{(n)}$$である。
分布が連続だから、確率1で$$X_{(1)} < \cdots < X_{(n)}$$である。
実際、$$c := P(\{\omega \mid X_{(1)}(\omega) = X_{2}(\omega)\}) > 0$$とすると

$$
    PX^{-1}((-\infty, y])
    =
    P(\{\omega \mid X(\omega) \in (-\infty, y]\})
   c > \epsilon > 0,
   1 > \forall \delta  > 0,
   F(x) - F(x = \epsilon)
$$

$\mathcal{A}_{0} := T^{-1}(\mathcal{B})$とおくと、

ここで、任意の可積分関数$f$について、

$$
    f_{0}(x)
    :=
    \frac{1}{n!}
    \sum_{\sigma \in \mathfrak{S}}
        f(x_{\sigma(1)}, \cdots, x_{\sigma(n)})
$$

とおくと、$f_{0}$は$T(x)$を与えた時の$f(X)$の条件付き期待値となっている。

$$
    \int_{A_{0}}
        f(x_{1}, \ldots, x_{n})
    \ dP(x_{1}) \cdots P(x_{n})
    =
    \int_{A_{0}}
        f(x_{\sigma(1)}, \ldots, x_{\sigma(n)})
    \ dP(x_{1}) \cdots P(x_{n})
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Lemma 2.4.1 
* $$T$$,
* $f, g$
    * integrable 

このとき以下が成立.

1.

$$
    \mathrm{E}
    \left[
        a f(X) + bg(X)
        \mid
        t
    \right]
    =
    a
        \mathrm{E}
        \left[
            f(X)
            \mid
            t
        \right]
    +
    b
        \mathrm{E}
        \left[
            g(X)
            \mid
            t
        \right]
$$

2.

$$
    \mathrm{E}
    \left[
        h(X) f(X)
        \mid
        t
    \right]
    =
    h(t)
        \mathrm{E}
        \left[
            f(X)
            \mid
            t
        \right]
$$

3.

$$
    a \le f(x) \le b
    \Rightarrow
    a
        \le
        \mathrm{E}
        \left[
            f(X)
            \mid
            t
        \right]
        \le
        b
$$

4.

$$
    |f_{n}|
    \le
    g,
    f_{n}(x) \rightarrow f(x)\ (n \rightarrow \infty)
    \Rightarrow
    \mathrm{E}
    \left[
        f_{n}(X)
        \mid
        t
    \right]
    \rightarrow
    \mathrm{E}
    \left[
        f(X)
        \mid
        t
    \right]
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

Notationについての注意。

$$
    \mathrm{E}^{P^{X}}
    \left[
        af + bg
    \right]
    =
    \int_{\mathcal{X}}
        af(x) + bg(x)
    \ dP^{X}(\omega)
$$

$$
    \mathrm{E}
    \left[
        af(X) + bg(X)
    \right]
    =
    \int_{\Omega}
        a f(X(\omega)) + b g(X(\omega))
    \ dP(\omega)
$$

### Lemma 2.4.2
$$ \mathrm{E} \left[ |f(X)| \right] < \infty $$, で$$g(t):= \mathrm{E} \left[ \left.  f(X) \right| t \right]$$とすると

$$
    \mathrm{E}
    \left[
        f(X)
    \right]
    =
    \mathrm{E}
    \left[
        g(T)
    \right]
$$

である。
つまり、conditional expectationの期待値と一致する.

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

Notationについて、

$$
    \mathrm{E}^{P^{X}}
    \left[
        f
    \right]
    =
    \mathrm{E}^{P^{X}}
    \left[
        g(T)
    \right]
$$

である。

$$
\begin{equation}
    P^{X}(A \mid T = t)
    :=
    \mathrm{E}^{P^{X}}
    \left[
        1_{A}(\cdot)
        \mid
        T = t
    \right]
    \label{chap02_22}
\end{equation}
$$


## 2.5 Conditional Probability Distribution
* $\mathcal{X}$
    * Euclidian spaceとする
    * i.e. $\mathcal{X} \subseteq \mathbb{R}^{n}$ for some $n$
* $\mathcal{A}$
    * Borel sets of $\mathcal{X}$

### Theorem 2.5.1
* $\mathcal{X}$
    * Euclidian

このとき、$\forall t \in $について、$P(\cdot \mid T = t): \mathcal{A} \rightarrow [0,1]$が存在して、$P(\cdot \mid T = t)$は$$(\mathcal{X}, \mathcal{A})$$上の確率測度になる

### proof.
一般性をかかず、$$\mathcal{X} = \mathbb{R}^{n}$$とする。
実際、$$\mathcal{X} \neq \mathbb{R}^{n}$$とし、$$\mathbb{R}^{n}$$上$P$が定理の主張を満たすmeasureとする。
このとき、$$Q(A) := P(A \cap \mathcal{X})\ (A \in \mathcal{B}(\mathbb{R}^{n}))$$とおけば$Q$はmeasureなので$Q(\cdot \mid T = t)$が存在する。
$$P(A \mid T = t) := Q(A \cap \mathcal{X}$$とおけば、定理の条件を満たす。

簡単のため、$n = 1$とおく。
$x \in \mathcal{X}$について、

$$
    F(x, t)
    :=
    P((-\infty, x] \mid T = t)
    \
    t\text{-a.e.}
$$

とおく。
このとき、右辺は$x$に依存したnull set$N_{x}$をもつ。
$$\mathbb{Q} = (r_{i})_{i \in \mathbb{N}}$$として $$A_{i} := (-\infty, r_{i}]$$とおけば以下が成り立つ。
$P^{T}$上のあるnull set$N$が存在して、$\forall t \in N$について、

$$
\begin{eqnarray}
    & &
        0 \le P(A_{i} \mid T = t) \le 1
        \quad
        (\forall i)
    \\
    & &
        (A_{i_{k}})_{k}: \mathrm{disjoint}
        \Rightarrow
        P(\sum_{k} A_{i_{k}} \mid T = t)
        =
        \sum_{k}P(A_{i_{k}} \mid T = t)
    \\
    & &
        A_{i} \subseteq A_{j}
        \Rightarrow
        P(A_{i} \mid T = t)
        \le
        P(A_{j} \mid T = t)
\end{eqnarray}
$$

実際、$$N := \bigcup_{k \in \mathbb{N}} N_{r_{k}}$$とおけば良い。
また、以下が成り立つ。
あるnull set$N$が存在して、$\forall \in N^{c}$について、

$$
\begin{eqnarray}
    & &
        r_{i} \le v_{j}
        \Rightarrow
        F(r_{i}, t)
        \le
        F(v_{j}, t)
    \\
    & &
        r \in \mathbb{Q}
        \
        (s_{n})_{n \in \mathbb{N}} \subset \mathbb{Q},
        \
        s_{n} \searrow r,
        \
        \Rightarrow
        F(s_{n}, t) = F(r, t)
\end{eqnarray}
$$

実際、

$$
\begin{eqnarray}
    0
    & \le &
        \lim_{n \rightarrow \infty} F(s_{n}, t) - F(r, t)
    \nonumber
    \\
    & = &
        \lim_{n \rightarrow \infty} P((r, s_{n}])
    \nonumber
    \\
    & \le &
        P(\lim \sup (r, s_{n}]))
    \nonumber
    \\
    & = &
        P(\emptyset) = 0
\end{eqnarray}
$$

となる。
上記により、$t \notin N$について$F(\cdot, t)$は$\mathbb{Q}$上右連続、非単調減少である。
$\forall t \notin N$について、$F(\cdot, t)$を$\mathbb{R}$上に拡張できる。

$$
    F^{*}(x, t)
    :=
    \lim_{r \searrow x, r \in \mathbb{Q}} F(r, t)
    \
    (x \in \mathbb{R})
$$

この$$F^{*}$$についても、$t \notin N$について

$$
\begin{eqnarray}
    & &
        x \le y
        \Rightarrow
        F^{*}(x, t)
        \le
        F^{*}(y, t)
    \\
    & &
        \lim_{x \rightarrow a} F^{*}(x, t)
        =
        F^{*}(a, t)
    \\
    & &
        \lim_{x \rightarrow -\infty} F^{*}(x, t)
        =
        0,
        \
        \lim_{x \rightarrow \infty} F^{*}(x, t)
        =
        1,
\end{eqnarray}
$$

が成立する。
実際、$\epsilon > 0$とすると、

$$
    \exists \delta > 0,
    \
    \forall r \in \mathbb{Q},
    \
    \mathrm{s.t. }
    a \le r < a + \delta
    \Rightarrow
    | F^{*}(a, t) - F(r, t) |
    \le
    \epsilon
$$

である。
ここで、$x \in \mathbb{R}$,$a < x < a + \delta$とすれば
$\exists l \in \mathbb{Q}$ s.t. $x < l < a + \delta$が存在するから、

$$
    l \in \mathbb{Q}
    \mathrm{ s.t. }
    | F^{*}(x, t) - F(l, t) |
    \le
    \epsilon
$$

とおけば、

$$
\begin{eqnarray}
    |F^{*}(a, t) - F^{*}(x,t)|
    & = &
        |F^{*}(a, t) - F(l,t) +  F(l, t) - F^{*}(x,t)|
    \nonumber
    \\
    & \le &

        2\epsilon
\end{eqnarray}
$$

上の3条件から$$F^{*}$$は分布関数になる。
よって、一意な確率測度$$P^{*}(\cdot \mid T=t)$$が存在して$$F^{*}(\cdot, t)$$が分布関数となる。
後は以下を示す。

$$
    P^{*}(\cdot \mid T = t)
    =
    P(\cdot \mid T = t)
    \
    t\text{-a.e.}
$$

これを示すには、一致の定理より$t$-a.e.でいかが成り立つことを示せば良い。

$$
\begin{eqnarray}
    & \Leftrightarrow &
        P^{*}((-\infty, a] \mid T = t)
        =
        P((-\infty, a] \mid T = t)
        \
        \forall a \in \mathbb{R}
    \nonumber
    \\
    & \Leftrightarrow &
        F^{*}(a, t)
        =
        F(a, t)
        \
        \forall a \in \mathbb{R}
\end{eqnarray}
$$

これは$\mathbb{Q}$上では明らかに成り立つ。
$a \notin \mathbb{Q}$については$a_{n} \searrow a$なる$a_{n} \in \mathbb{Q}$の列をとれば、$F$の右連続性より成り立つ。

<div class="QED" style="text-align: right">$\Box$</div>

Notationとして以下を定義する。

* $X:\Omega \rightarrow \mathcal{X}$
    * vector-valued r.v.
* $T:\mathcal{X} \rightarrow \mathcal{T}$
    * statistics
* $P^{X}:\mathcal{A} \rightarrow [0, 1]$
    * $X$の分布

$P^{X \mid T = t}: \mathcal{A} \rightarrow [0, 1]$を$P^{X}$の$T=t$での条件付き確率とする。

$$
    P^{X \mid T = t}(\cdot)
    =
    P^{X}(\cdot \mid T = t)
$$

### Thereom 2.5.2
* $X: \Omega \rightarrow \mathcal{X}$
    * vector valued random variable
* $$\mathrm{E}^{P^{X}} \left[ f \right] < \infty $$,

このとき以下が成り立つ。

$$
    \mathrm{E}^{P^{X}}
    \left[
        f
        \mid
        T = t
    \right]
    =
    \int
        f(x)
    \ d P^{X \mid T = t}(x)
    \quad
    t \text{-a.e.}
    \
    (\mathcal{B}, P^{T})
$$

### proof.
$f$が定義関数のときは、Theorem 2.5.2による。
$f$を階段関数で近似すれば、期待値の線形性とMonotone convergence theoremより成り立つ。

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 2.5.3
* $T$
    * statistacs

nullset $\exists N$が存在して、$\forall t \notin N$, $\exists P^{X \mid T =t}$: conditional probabiilty measureで以下を満たす。
$\forall t \notin N$について、

$$
\begin{eqnarray}
    \mathrm{E}^{P^{X}}
    \left[
    \left.
        f
    \right|
        T = t
    \right]
    & = &
        \int
            f(x)
        \ d P^{X \mid T = t}(x)
    \nonumber
    \\
    \mathrm{E}^{P^{X}}
    \left[
    \left.
        h \circ T
        f
    \right|
        T = t
    \right]
    & = &
        h(t)
        \mathrm{E}^{P^{X}}
        \left[
        \left.
            f
        \right|
            T = t
        \right]
\end{eqnarray}
$$

### proof.
W.l.o.g. we assume $\mathcal{T} \subseteq \mathbb{R}$, therefore to the previous theorem we attain $P^{X \mid T = t}$ in the bi.
Let $B \in \mathcal{B}$ then it holds that

$$
    \{ T \in B\}
    \in
    \sigma[T]
$$

$$
\begin{eqnarray}
    \mathrm{E}^{P^{X}}
    \left[
    \left.
        1_{T \in B}
    \right|
        T = t
    \right]
    & = &
        1_{B}(t)
    \nonumber
    \\
    P^{X \mid T = t}(T^{-1}(B))
    =
    1_{B}(t)
    \
    t \text{-a.e.}
\end{eqnarray}
$$


$$
    \mathcal{C}
    :=
    \{
        (a, b]
        \mid
        a, b \in \mathbb{Q}
    \}
$$

Since $$\# \mathcal{C} = \# \mathbb{N}$$, we can constract such a null set $N$ that for $\forall t \notin N$,

$$
    P^{X \mid T = t}(T^{-1}(B))
    =
    1_{B}(t)
    \
    (\forall B \in \mathcal{B})
$$

Since both sides can be regarded as mean w.r.t. $B \in \mathcal{B}$.
We obtain

$$
    P^{X \mid T = t}(T = t)
    =
    P^{X \mid T = t}(T^{-1}(\{ t\}))
    =
    1_{\{t\}}(t)
    =
    1
$$

Consequentlly, we have obtained

$$
    \mathrm{E}^{P^{X \mid T = t}}
    \left[
    \left.
        h(T)
    \right|
        T = t
    \right]
    =
    \int 
        h(T(x))
        f(x)
    \ d P^{X \mid T = t}(dx)
    =
    \int_{\{T = t\}}
        h(T(x))
        f(x)
    \ d P^{X \mid T =t}(x)
    =
    h(t)
    \int_{\{T = t\}}
        f
    \ d P^{X \mid t}(x)
$$

<div class="QED" style="text-align: right">$\Box$</div>

In 1.9, the cond. prob. dist's are defined over $$\{T = t \}$$ rather than the entire sp. $\mathcal{X}$ and in this sense $P^{X \mid T = t}$, defined perivously, differs from them.
Howerver  sincd

$$
    P^{X \mid T = t}(A)
    =
    P^{X \mid T = t}(A \cap \{T = t\})
$$

### Lemma 2.5.1
* $$(\mathcal{T}, \mathcal{B})$$,
    * Euclidian Space
* $$(\mathcal{Y}, \mathcal{C})$$,
    * Euclidian Space
* $$(\mathcal{X}, \mathcal{A}) := (\mathcal{T} \times \mathcal{Y}, \mathcal{B} \times \mathcal{C})$$,
    * prodcut measure space
* $$P_{0}^{T, Y}$$,
    * distribution over $$(\mathcal{X}, \mathcal{A})$$

ここで$$P_{1}$$が$$(\mathcal{X}, \mathcal{A})$$の分布で

$$
    dP_{1}(t, y)
    =
    a(y)b(t)
    dP_{0}(t, y)
$$

が存在するとする。
ここで、$$\forall y, a(y) > 0$$とする。
このとき、$$P_{1}$$のもと、$T$と、$t$を与えたもとでの、$$Y$$の条件付き分布のversionは以下で与えられる。

$$
    d P_{1}^{T}(t)
    =
    b(t)
    \left[
        \int
            a(y)
        \ d P_{0}^{Y \mid t}(y)
    \right]
    d P_{0}^{T}(t)
$$

$$
    dP_{1}^{Y \mid t}
    =
    \frac{
        a(y) dP_{0}^{Y \mid t}(y)
    }{
        \int
            a(y^{\prime}) 
        \ d P_{0}^{Y \mid t}(y^{\prime})
    }.
$$

### proof.


<div class="QED" style="text-align: right">$\Box$</div>


## 2.6 Characterization of Sufficiency

* $$\mathcal{P} := \{P_{\theta}\}_{\theta \in \Theta}\}$$,
    * sample sp. $$(\mathcal{X}, \mathcal{A})$$上の確率測度の族
* $T: \mathcal{X} \rightarrow \mathcal{T}$
    * 統計量


### Definition. sufficient
$T$がsufficientであるとは、$\forall A \in \mathcal{A}$について、ある$\mathcal{B}$可測関数$q(A \mid t)$が存在して、

$$
    \forall B \in \mathcal{B},
    \
    \theta \in \Theta,
    \
    \int_{B}
        q(A \mid t)
    \ d P_{\theta}^{T}(dt)
    =
    P_{\theta}(A \cap T^{-1}(B))
$$

<div class="end-of-statement" style="text-align: right">■</div>

統計量が十分とは、分布族を$\theta$に依存しない可測関数で表現できるということである。
つまり、統計量$T$が$\theta$を特定するのに十分な情報を持っているということ。

Example 2.4.1からorder statisticsはsufficient statisticである。

### Theorem 2.6.1
* $\mathcal{X}$
    * Euclidian sp.
* $T$が$\mathcal{P}$について、十分とする

このとき、$\theta$に依存しない可測関数$$g:\mathcal{T} \rightarrow [0, 1]$$が存在して、

$$
    g(t)
    =
    P_{\theta}(A \mid T = t)
$$

となる。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

この定理はもう少し一般的な形で成り立つ。
詳細は数理統計学の命題3.3.をみる。

## 2.7 Exponential Families

二項分布の場合は、

$$
    \left(
        \begin{array}{c}
            n \\
            x
        \end{array}
    \right)
    p^{x}
    (1 - p)^{n-x}
    =
    (1 - p)^{n}
    \exp
    \left(
        x
        \log
        \left(
            \frac{
                p
            }{
                1 - p
            }
        \right)
    \right)
    \left(
        \begin{array}{c}
            n \\
            x
        \end{array}
    \right)
$$

となって、Exponential Familyとなる。

### Example 2.7.1

<div class="end-of-statement" style="text-align: right">■</div>

### Example 2.7.2

<div class="end-of-statement" style="text-align: right">■</div>

Exponential Familiesに

$$
\begin{equation}
    p_{\theta}(x)
    :=
    C(\theta)
    \exp
    \left(
        \sum_{j=1}^{k}
        \theta_{j}
        T_{j}(x)
    \right)
    \label{chap04_04_05}
\end{equation}
$$

### Definition. Natural Parameter Space
* $$A \subseteq \mathbb{R}^{m}$$,

$$
    A
    :=
    \left\{
        a := (a_{1}, \ldots, a_{m}) \in \mathbb{R}^{m}
        \mid
        0
        <
        \int_{\mathcal{X}}
            \exp
            \left(
                \sum_{i=1}^{m}
                    a_{i}T_{i}(x)
            \right)
            g(x)
        \ \mu (dx)
        <
        \infty
    \right\}
$$

をnatural parameter spaceという。

<div class="end-of-statement" style="text-align: right">■</div>

$A \neq \emptyset$をnatural parameter spaceとする。

$$
    \Psi (a)
    :=
    \log
    \left(
        \int_{\mathcal{X}}
            \exp
            \left(
                \sum_{i=1}^{m}
                    a_{i}T_{i}(x)
            \right)
            g(x)
            
        \ \mu(dx)
    \right)
    \quad
    a \in A
$$

とおくと、指数型分布族$$\mathcal{P}:=\{P_{a}\}_{a \in A}$$が

$$
    \frac{
        P_{a}
    }{
        d\mu
    }
    (x)
    =
    \exp
    \left(
        \sum_{i=1}^{m}
            a_{i}T_{i}(x)
        -
        \Psi(a)
    \right)
    g(x)
$$

で定まる。

### Lemma 2.7.1
exponential familiyのnatural parameter spaceは凸である。


### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Lemma 2.7.2

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 2.7.1
* $$(\mathcal{X}, \mathcal{A})$$,
    * 可測空間
* $\phi$

$$
\begin{equation}
    \int
        \phi(x)
        \exp
        \left(
            \sum_{j=1}^{k}
                \theta_{j}
                T_{j}(x)
        \right)
    d\mu(x)
    \label{chap02_02_38}
\end{equation}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>



