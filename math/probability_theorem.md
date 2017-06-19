---
title: Probability theorem
---

# Probability theorem

## Bayse' rule
$Q \sim P$が同値な確率測度とする。
このdensity processを

$$
    D(t) :=
        \left. 
            \frac{d Q}{d P}
        \right|_{\mathcal{F}_{t}}
        =
        \mathrm{E}
        \left[
        \left.
            \frac{d Q}{d P}
        \right|
            \mathcal{F}_{t}
        \right],
$$

と定義する。
$X$を$\mathcal{F}_{T}$-measurableな確率変数で、$\mathrm{E^{Q}}^{|X|} < \infty$とする。
このとき、

1. 以下のBayse' ruleが成り立つ

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        F_{t}
    \right]
        = \frac{
            \mathrm{E}
            \left[
            \left.
                XD(T)
            \right|
                \mathcal{F}_{t}
            \right]
        }{
            \mathcal{F}_{t}
        },
        \quad
        t \ge T.
$$

2. $M$が適合過程で、$Q$-martingaleあることと、$DM$が$P$-martingaleであることは同値

## proof
まず、1について示す。

$$
    
$$

## Conditional expectation given measurable map
* $$(\Omega, \mathcal{F}, P)$$,
* $X: \Omega \rightarrow \mathbb{R}$
    * $\mathcal{F}$ measurable integrable function
* $$(\mathcal{T}, \mathcal{B})$$,
    * measurable space
* $T: \Omega \rightarrow \mathcal{T}$
    * $\mathcal{F} / \mathcal{B}$可測写像
* $P^{T} := P \circ T^{-1}$
    * $\mathcal{T}$上の測度

### Definition 1.39
* $g: \mathcal{T} \rightarrow \mathbb{R}$

以下を満たす$g$を$T=t$のもとでの条件付き期待値という。

* $g$は$\mathcal{B}$可測
* $g$は$P^{T}$可積分

$$
    \forall B \in \mathcal{B},
    \
    \int_{T^{-1}(B)}
        X(\omega)
    \ P(d\omega)
    =
    \int_{B}
        g(t)
    \ P^{T}(dt)
$$

このとき、$g$を

$$
    g(t^{\prime})
    =:
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        T=t
    \right]
    (t^{\prime})
$$

とかく。
一部の本ではこれを略記して、

$$
    g(t)
    =:
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        T = t
    \right]
$$

とかく。

<div class="end-of-statement" style="text-align: right">■</div>

### Remark
$T=t$のときの、$t$に意味はない。
一般の確率論の本では、確率変数$Y: \Omega \rightarrow \mathbb{R}$の条件付き期待値を

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        Y
    \right]
$$

とかくので、これにならなって、

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
       T
    \right]
$$

のほうが良いかもしれない。
ただ、$T$の値域は$X$のものと一致していないので、分ける意味で、記法を変えているのかもしれない。
この条件付き確率の存在は、

$$
    B \in \mathcal{B},
    \
    \mu(B)
    :=
    \int_{T^{-1}}
        X(\omega)
    \ d P(d\omega)
$$

とおくと、$\mu$は$P^{T}$について絶対連続である。

<div class="end-of-statement" style="text-align: right">■</div>


## regular conditional probability
* [LA.pdf](http://kenshi.miyabe.name/wordpress/wp-content/uploads/2013/01/LA.pdf)

正則条件付き確率ともいう。

### Definition 1.42
* $$(\Omega, \mathcal{F}, P)$$,
    * probability space
* $\mathcal{G} \subset \mathcal{F}$
    * sub sigma algebra
* $p(\cdot, A): \Omega \times \mathcal{F} \rightarrow [0, 1]$,

$p$は$\mathcal{G}$が与えられたときの正則条件付き確率という

* $\forall \omega$について、$$p(\omega, \cdot): \mathcal{F} \rightarrow [0, 1]$$,は$(\Omega, \mathcal{F})$上の確率測度
* $\forall A \in \mathcal{F}$について、$$p(\cdot, A): \Omega \rightarrow [0, 1]$$は$\mathcal{G}$可測
* $\forall \in \mathcal{G}$, $\forall B \in \mathcal{G}$,

$$
    P(A \cap B)
    =
    \int_{B}
        p(\omega, A)
    \ P(d\omega)
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. 3.2. (Sufficient Statistics)
* $$(\Omega, \mathcal{F}, P)$$,
    * probability space
* $$(\mathcal{X}, \mathcal{A})$$,
* $$(\mathcal{T}, \mathcal{B})$$,
* $$\mathcal{P} := \{P_{\theta}\}_{\theta \in \Theta}$$,
    * $$(\mathcal{X}, \mathcal{A})$$上の確率分布の族
* $T: \mathcal{X} \rightarrow \mathcal{T}$
* $\forall A \in \mathcal{A}$, $q(A \mid \cdot):\mathcal{T} \rightarrow \mathbb{R}$ 
    * $\mathcal{B}$可測関数

このとき、以下を満たすような$q$が存在すれば、$T$は分布族$\mathcal{P}$に対して十分という。
また、$T$は十分統計量という。

$$
    B \in \mathcal{B},
    \
    \theta \in \Theta,
    \
    \int_{B}
        q(A \mid t)
    \ P_{\theta}^{T}(dt)
    =
    P_{\theta}
    (A \cap T^{-1}(B))
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Example 3.4
* $\mathbb{R}^{n}$
* $$\mathcal{P} := \{P^{\sigma} \mid \sigma \in \mathfrak{S} \}$$,
    * $$P^{\sigma} := P \circ \sigma^{-1}$$,
* $$T: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$$,

$$
    T(x_{1}, \ldots, x_{n})
    =:
    (x_{(1)}, \ldots, x_{(n)})
$$

ただし、$$x_{(1)} \le \cdots \le x_{(n)}$$である。
$T$は十分統計量である。
$$ P^{\sigma} \in \mathcal{P}$$, $$\sigma^{\prime} \in \mathfrak{S}$$, $$A, B \in \mathcal{B}_{n}$$に対して、

$$
\begin{eqnarray}
    P^{\sigma}(A \cap T^{-1}(B))
    & = &
        \int_{\mathbb{R}^{n}}
            1_{A}(x)
            1_{B}(T(x))
        \ P(dx)
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}^{n}}
            1_{A}(\sigma^{\prime}(x))
            1_{B}(T(x))
        \ P(dx)
    \nonumber
\end{eqnarray}
$$

$\sigma^{\prime}$は任意であったから、

$$
    q(A \mid x)
    :=
    \frac{1}{n!}
    \sum_{\sigma_{0} \in \mathfrak{S}}
        1_{A}(\sigma_{0}(x))
$$

とおけば

$$
\begin{eqnarray}
    \int_{\mathbb{R}^{n}}
        1_{A}(\sigma^{\prime}(x))
        1_{B}(T(x))
    \ P(dx)
    & = &
        \frac{1}{n!}
        \sum_{\sigma_{0} \in \mathfrak{S}}
            \int_{\mathbb{R}^{n}}
                1_{A}(\sigma_{0}(x))
                1_{B}(T(x))
            \ P(dx)
    \nonumber
    \\
    & = &
            \int_{\mathbb{R}^{n}}
                q(A \mid x)
                1_{B}(T(x))
            \ P(dx)
    \nonumber
\end{eqnarray}
$$

となる。

<div class="end-of-statement" style="text-align: right">■</div>
