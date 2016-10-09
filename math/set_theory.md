# Set Theory

## Symbol

## Definition

### Limit
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

##### Proof
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

##### Proof
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

### Diameter
$(S, d)$を距離空間とする。
$A \subset S$の直径$\delta(A)$を以下で定義する。

$$
    \delta(A)
        := \sup \left\{ d(x, y) \mid x \in A, y \in A \right\} 
        \le \infty
$$

$\delta(A) \le \infty$の時、$A$を有界という。

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

### Distance between point and set
$(S, d)$を距離空間とする。
$A \subset S$と$x \in S$の距離$d_{A}$を次で定める。

$$
    d_{A}(x) 
        := \inf \left\{ d(x, a) \mid a \in A \right\} 
$$

### Distance between set and set
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

### lemma
$(S, d)$を距離空間とする。
$x \in S$, $A \neq \emptyset \subset S$に対して、

$$
    d(x, A) = 0
    \iff
    x \in \bar{A}
$$

#### Proof

### lemma
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

### $\epsilon$-neighborhood
$(S, d)$を距離空間とする。
$A \subset S$, $\epsilon > 0$に対して、$A$の$\epsilon$近傍$A^{\epsilon}$を次で定義する。

$$
    A \subset 
    A^{\epsilon} 
        := \left\{ a \in S \mid d_{A}(a) < \epsilon \right\} 
$$

#### Note1



## Theory


## Reference

