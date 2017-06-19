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
    * この本では、statisticsという

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
    * i.i.dの$\mathbb{R}$値の確率変数
    * 分布は連続
* $T: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$

$$
    T(x_{1}, \ldots, x_{n})
    =:
    (x_{(1)}, \ldots, x_{(n)})
$$

ここで、$$x_{(1)} \le \cdots \le x_{(n)}$$である。
分布が連続だから、確率1で$$x_{(1)} < \cdots < x_{(n)}$$である。
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

