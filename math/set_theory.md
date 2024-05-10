---
title: Set theory
---

# Set Theory

## Symbol

## Definition

#### Definition Limit
集合の上極限$ \limsup_{n \rightarrow \infty} A_{n}$ と下極限$ \liminf_{n \rightarrow \infty} A_{n}$を以下で定義する。

$$
\limsup_{n \rightarrow \infty}A_{n} 
    := \bigcap_{n = 1}^{\infty}\bigcup_{m = n}^{\infty} A_{m}
$$

$$
\liminf_{n \rightarrow \infty}A_{n} 
    := \bigcup_{n = 1}^{\infty}\bigcap_{m = n}^{\infty} A_{m}
$$

また、次が成り立つ時、$A_{n}$が$A$に収束するといい、$ \lim_{n \rightarrow \infty} A_{n} = A$とかく。

$$
    \limsup_{n \rightarrow \infty} A_{n} 
        = \liminf_{n \rightarrow \infty} A_{n}
        = A
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Note1
次が成り立つ。

$$
    \liminf_{n \rightarrow \infty} A_{n} \subset \limsup_{n \rightarrow \infty} A_{n}
$$

#### Note2
次が成り立つ。
主張は以下の2つ。
* 集合の単調増大列は、極限をもつ
* その極限はすべての集合の和集合

$$
    A_{n} \subset A_{n+1} 
    \Rightarrow 
    \lim_{n \rightarrow \infty} A_{n} = \bigcup_{n = 1}^{\infty} A_{n}
$$

#### Proof
まず以下が成り立つ。

$$
    A_{n} \subset A_{n+1} 
    \Rightarrow 
    \bigcup_{m=n}A_{n} 
        = A_{n} \bigcup \left( \bigcup_{m=n+1}A_{n} \right)
        = \bigcup_{m=n+1}A_{n} 
$$

よって、

$$
\begin{eqnarray*}
    \limsup_{n \rightarrow \infty} A_{n}
        & = & \bigcap_{n = 1}^{\infty}\bigcup_{m = n}^{\infty} A_{m} \\
        & = & \bigcap_{n = 1}^{\infty}\bigcup_{m = 1}^{\infty} A_{m} \\
        & = & \bigcup_{m = 1}^{\infty} A_{m}
\end{eqnarray*}
$$

また、以下が成り立つ。

$$
    A_{n} \subset A_{n+1} 
    \Rightarrow 
    \bigcap_{m=n}A_{n} 
        = A_{n} \bigcap \left( \bigcap_{m=n+1}A_{n} \right)
        = A_{n} 
$$

よって、

$$
\begin{eqnarray*}
    \liminf_{n \rightarrow \infty} A_{n}
        & = & \bigcup_{n = 1}^{\infty}\bigcap_{m = n}^{\infty} A_{m} \\
        & = & \bigcup_{n = 1}^{\infty} A_{n} 
\end{eqnarray*}
$$

<div class="QED" style="text-align: right">$\Box$</div>


#### Note3
次が成り立つ。
主張は以下の2つ。
* 集合の単調減少列は、極限をもつ
* その極限はすべての集合の積集合

$$
    A_{n} \supset A_{n+1} 
    \Rightarrow 
    \lim_{n \rightarrow \infty} A_{n} = \bigcap_{n = 1}^{\infty} A_{n}
$$

#### Proof
まず以下が成り立つ。

$$
    A_{n} \supset A_{n+1} 
    \Rightarrow 
    \bigcup_{m=n}A_{n} 
        = A_{n} \bigcup \left( \bigcup_{m=n+1}A_{n} \right)
        = A_{n} 
$$

よって、

$$
\begin{eqnarray*}
    \limsup_{n \rightarrow \infty} A_{n}
        & = & \bigcap_{n = 1}^{\infty}\bigcup_{m = n}^{\infty} A_{m} \\
        & = & \bigcap_{n = 1}^{\infty} A_{n} \\
        & = & \bigcap_{n = 1}^{\infty} A_{n}
\end{eqnarray*}
$$

また、以下が成り立つ。

$$
    A_{n} \supset A_{n+1} 
    \Rightarrow 
    \bigcap_{m=n}A_{n} 
        = A_{n} \bigcap \left( \bigcap_{m=n+1}A_{n} \right)
        = \bigcap_{m=n+1}A_{n}
$$

よって、

$$
\begin{eqnarray*}
    \liminf_{n \rightarrow \infty} A_{n}
        & = & \bigcup_{n = 1}^{\infty}\bigcap_{m = n}^{\infty} A_{m} \\
        & = & \bigcup_{n = 1}^{\infty}\bigcap_{m = 1}^{\infty} A_{m} \\
        & = & \bigcap_{m = 1}^{\infty} A_{m} 
\end{eqnarray*}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem
$M \neq \emptyset \subset S$とする。
以下は同値。
* $a \in S$が$M$の触点
* $a$がある点列$(a_{n})$の極限点

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Diameter
$(S, d)$を距離空間とする。
$A \subset S$の直径$\delta(A)$を以下で定義する。

$$
    \delta(A)
        := \sup \left\{ d(x, y) \mid x \in A, y \in A \right\} 
        \le \infty
$$

$\delta(A) \le \infty$の時、$A$を有界という。

<div class="end-of-statement" style="text-align: right">■</div>

#### Note1
以下は同値。

* $\delta(A) = 0$
* $A$が一点からなる集合

#### Note2
以下が成立。

$$
    A \subset B 
    \Rightarrow 
    \delta(A) \leq \delta(B)
$$

#### Distance between point and set
$(S, d)$を距離空間とする。
$A \subset S$と$x \in S$の距離$d_{A}$を次で定める。

$$
    d_{A}(x) 
        := \inf \left\{ d(x, a) \mid a \in A \right\} 
$$

#### Distance between set and set
$(S, d)$を距離空間とする。
$A, B \subset S$とする。
$A, B$の距離を以下で定義する。

$$
    d(A, B) 
        :=  \inf \left\{ d(a, b) \mid a \in A, b \in B \right\} 
$$

#### Note1
以下が成り立つ。

* $0 \leq d(A, B) \le \infty$
* $d(A, B) = d(B, A)$
* $d(\{x\}, \{y\}) = d(x, y)$

#### Note2
$A = \{x\}$の場合は$d(\{x\}, B) = d_{B}(x)$で、集合と点の距離になる。

#### lemma
$(S, d)$を距離空間とする。
$x \in S$, $A \neq \emptyset \subset S$に対して、

$$
    d(x, A) = 0
    \iff
    x \in \bar{A}
$$

#### Proof

<div class="QED" style="text-align: right">$\Box$</div>

#### lemma
$x, y \in S$, $A \neq \emptyset \subset S$とする。

$$
    \left| d(x, A) - d(y, A) \right|
        \leq d(x, y) 
$$

#### Proof
$\forall z \in  A$について、

$$
    d(x, A) \leq d(x,z) \leq d(x, y) + d(y, z)
$$

が成立。
したがって、

$$
    d(x, A) - d(x, y) \leq d(y, A)
$$

より

$$
    d(x, A) - d(y, A) \leq d(x, y)
$$

が成立。
同様に

$$
    d(y, A) - d(x, y) \leq d(x, A)
$$

から

$$
    d(y, A) - d(x, A) \leq d(x, y)
$$

となる。

<div class="QED" style="text-align: right">$\Box$</div>

### $\epsilon$-neighborhood
$(S, d)$を距離空間とする。
$A \subset S$, $\epsilon > 0$に対して、$A$の$\epsilon$近傍$A^{\epsilon}$を次で定義する。

$$
    A \subset 
    A^{\epsilon} 
        := \left\{ a \in S \mid d_{A}(a) < \epsilon \right\} 
$$

#### Note1

#### Def. (inverse map)
$X, Y$を集合とし、$f:X \rightarrow Y$とする。
inverse map $f^{-1}:Y \rightarrow X$を以下で定義する。

$$
    B \subset Y,
    f^{-1}(B)
        := \{x \in X \mid f(x) \in Y\}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem

$$
\begin{eqnarray}
    & &
    P_{1} \subset P_{2} \Rightarrow f(P_{1}) \subset f(P_{2})
    \\
    & &
    f(P_{1} \cup P_{2})
        = f(P_{1}) \cup f(P_{2})
    \\
    & &
    f(P_{1} \cap P_{2})
        \subset f(P_{1}) \cap f(P_{2})
    \\
    & &
    f(A - P)
        \supset f(A) - f(P)
    \\
    & &
    Q_{1} \subset Q_{2}
        \Rightarrow f^{-1}(Q_{1}) \subset f^{-1}(Q_{2})
    \\
    & &
    f^{-1}(Q_{1} \cup Q_{2})
        = f^{-1}(Q_{1}) \cup f^{-1}(Q_{2})
    \\
    & &
    f^{-1}(Q_{1} \cap Q_{2})
        = f^{-1}(Q_{1}) \cap f^{-1}(Q_{2})
    \\
    & &
    f^{-1}(B-Q)
        = A - f^{-1}(Q)
    \\
    & &
    f^{-1}(f(P))
        \supset P
    \label{4_5}
    \\
    & &
    f(f^{-1}(Q))
        \subset Q
    \label{4_5_prime}
\end{eqnarray}
$$

さらに、$f$が単射とすると、

$$
\begin{equation}
    f^{-1}(f(P))
        = P
    \label{4_5_one_to_one}
\end{equation}
$$

となる。
また、$f$が全射とすると、

$$
\begin{eqnarray}
    f(f^{-1}(Q))
        = Q
    \label{4_5_prime_onto}
\end{eqnarray}
$$

となる。

#### proof.

$$\eqref{4_5}$$を示す。
$\forall p \in P$とする。

$$
    f^{-1}(f(P)) 
        = \{x \in A \mid f(x) \in f(P)\}
$$

よって、$f(p) \in f(P)$より$p \in f^{-1}(f(P))$となる。
また、$f$が単射とすると、等号で成り立つ。
実際、$\forall p \in f^{-1}(f(P))$とする。
$f(p) \in f(P)$より、$\exists p^{\prime} \in P$, $f(p) = f(p^{\prime})$となる。
$f$が単射より、$p = p^{\prime} \in P$が成り立ち等号が成立する。

$$\eqref{4_5_prime}$$を示す。
$\forall q \in f(f^{-1}(Q))$とする。
$\exists p \in f^{-1}(Q)$, $f(p) = q$である。
$p \in f^{-1}(Q)$より、$q = f(p) \in Q$となって成立。
$f$が全射とする。
$q \in Q$とすると、$f$が全射より$\exists p \in A$, $f(p) = q \in Q$である。
よって、$p \in f^{-1}(Q)$であり、$q \in f(f^{-1}(Q))$となる。

<div class="QED" style="text-align: right">$\Box$</div>

### Existense of emptyset
* [set theory - The existence of the empty set is an axiom of ZFC or not? - Mathematics Stack Exchange](https://math.stackexchange.com/questions/278863/the-existence-of-the-empty-set-is-an-axiom-of-zfc-or-not)

$\exists x (x = x)$ is a formal statements of 

## Reference
* http://jeff560.tripod.com/set.html
* [axioms - Is the Bourbaki treatment of Set Theory outdated? - Mathematics Stack Exchange](https://math.stackexchange.com/questions/929303/is-the-bourbaki-treatment-of-set-theory-outdated)
