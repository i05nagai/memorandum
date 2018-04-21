---
title: Set theory
---

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

### Topology in metric space
$(S, d)$を距離空間とする。
$a \in S$, $\epsilon > 0$について、球体$B(a; \epsilon)$を以下で定義する。

$$
    B(a; \epsilon) := \left\{ x \mid x \in S, d(a, x) < \epsilon \right\} 
$$

$$
    O_{d} 
        := \left\{ O \subset S \mid \forall a \in O, \exists \epsilon >0, \mathrm{s.t. } B(a; \epsilon) \subset O \right\} 
$$

$S$の位相を$O_{d}$と$\emptyset$をからなる集合系$\mathcal{D}_{d}$として定義する。


#### Theorem
任意の距離空間$(S, d)$は第一可算公理を満足する。
また、第二可算公理を満足するためには、$S$が可分であることが必要十分である。

##### Proof

#### Theorem
$M \neq \emptyset \subset S$とする。
以下は同値。
* $a \in S$が$M$の触点
* $a$がある点列$(a_{n})$の極限点


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

## Def. (inverse map)
$X, Y$を集合とし、$f:X \rightarrow Y$とする。
inverse map $f^{-1}:Y \rightarrow X$を以下で定義する。

$$
    B \subset Y,
    f^{-1}(B)
        := \{x \in X \mid f(x) \in Y\}
$$

## Theorem

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


## proof.

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


## Def. Quotient topological space
$X$を位相空間とする。
$\sim$を$X$上の同値関係とする。
$Y := X/~$を商集合とし、$\pi:X \rightarrow Y$を標準射影とする。
このとき、$\pi$を連続とする最強の位相$\mathcal{O}$とすると、$(Y, \mathcal{O})$を商位相空間という。

## Lemma
$X$を集合、$(Y, \mathcal{O}_{Y})$を位相空間とする。
$f:X \rightarrow Y$とすると、以下で定義される集合族は$f$を連続にする$X$の最弱の位相である。

$$
\begin{equation}
    \mathcal{O}_{X}
        := \{f^{-1}(O_{Y}) \mid O_{Y} \subset \mathcal{O}_{Y} \}
\end{equation}
$$

## Lemma
$(X, \mathcal{O}_{X})$を位相空間、$Y$を集合とする。
$f:X \rightarrow Y$とすると、以下で定義される集合族は$f$を連続にする$Y$の最強の位相である。

$$
\begin{equation}
    \mathcal{O}_{Y}
        := \{O_{Y} \subset Y \mid f^{-1}(O_{Y}) \in \mathcal{O}_{X} \}
\end{equation}
$$

## Lemma(quotient topological spaces and countable basis)
$X$がtopological spacesとする。
$\sim$が$X$上のequivalenceとする。
$Y := X / \sim$をquotient topological spaceとし、$\pi: X \rightarrow Y$をquotient mapとする。
$X$がcountable basisを持つとすると、$Y$はcountable basisをもつ。

## proof.
$\\{A_{n}\\}_{n \in \mathbb{N}}$を$X$のcountable basisとする。
$B \subset Y$をopenとすると、 $\pi^{-1}(B)$はopenである。
よって、

$$
    \exists \{A_{i}\}_{i \in I} \subset \{A_{n}\}_{n \in \mathbb{N}},
    \pi^{-1}(B) = \bigcup_{i \in I} A_{i}
$$

となる。
$\pi$が全射かつ開写像より、

$$
\begin{eqnarray}
    & &
    \pi^{-1}(B) = \bigcup_{i \in I} A_{i}
    \nonumber
    \\
        & \iff &
            B = \pi(\bigcup_{i \in I} A_{i})
    \nonumber
    \\
        & \iff &
            B = \bigcup_{i \in I} \pi(A_{i})
\end{eqnarray}
$$

となる。
$B$は任意だったので、$$\{ \pi(A_{n}) \}_{n \in \mathbb{N}} $$がcountable basisとなる。

<div class="QED" style="text-align: right">$\Box$</div>

## Lemma (equivalent condition to Hausdorff spaces)
$(X, \mathcal{O}_{X})$をtopological spacesとする。
以下は同値

1. $X \times X$上$$A := \{ (x, x) \in X \times X \mid x \in X\}$$が閉である
2. $X$がHausdorff spaces

## proof.
1 $\Rightarrow$ 2を示す。
$x, y \in X, x \neq y$とすると、 $(x, y) \in A^{c}$である。
直積位相は、$$\{ U \times V \mid U, V \in \mathcal{O}_{X} \}$$を基底に持つ。
$A^{c}$がopenより、$U, V \in \mathcal{O}_{X}$で、$(x, y) \in U \times V \subset A^{c}$とできる。
$U \cap V = \emptyset$である。
実際、$U \cap V \neq \emptyset$とすると、$z \in U \cap V$について、$(z ,z) \in U \times V$となるが、$U \times V \subset A^{c}$に矛盾する。
よって、$x \in U, y \in Y, U \cap V = \emptyset$となる。
$x, y$は任意だったので、$X$はHausdorffとなる。

2 $\Rightarrow$ 1を示す。
$A^{c}$がopenであることを示す。
$A^{c} \subset A^{ci}$を示せば良いが、その為には$p \in A^{c}$について、$O \subset A^{c}$がopenで, $p \in O$を示せば良い。
$\forall (x, y) \in A^{c}$とすると、$x \neq y$と$X$がHausdorffより、$$x \in U \in \mathcal{O}_{X}$$, $$y \in V \in \mathcal{O}_{X}$$, $U \cap V = \emptyset$とできる。
$(x, y) \in U \times V$で、$U \times V \subset A^{c}$である。
実際、$U \times V \subset A^{c}$でないとすると、$U \times V \cap A \neq \emptyset$より、$(z, z) \in U \times V \cap A$が存在する。
$U \subset V = \emptyset$であったから、$z \in U$, $z \in V$となり矛盾する。
よって、$A^{c}$はopenである。

<div class="QED" style="text-align: right">$\Box$</div>

## Lemma.
$(X, \mathcal{O}_{X})$をtopological spacesとする。
$\sim$を$X$上の同値関係とする。
以下は同値

1. $X \times X$上$$A := \{ (x_{1}, x_{2}) \in X \times X \mid x_{1} \sim x_{2}\}$$が閉である
2. $Y := X/\sim$がHausdorff spaces

## proof.
2は以下と同値である。
1と以下が同値であることを示す。

* $Y \times Y$上$$B := \{ (y, y) \in Y \times Y \mid y \in Y\}$$が閉である

1を仮定する。
$B^{c}$が開であることを示す。
$(y_{1}, y_{2}) \in B^{c}$, $y_{1} \neq y_{2}$である。

<div class="QED" style="text-align: right">$\Box$</div>


## example
位相空間$$(X, \mathcal{O}_{X})$$の部分位相空間$$(A, \mathcal{O}_{A})$$とする。
* $A$が$X$で開とすると
    * $B \subset A$が$A$で開ならば、$X$でも開
* $A$が$X$で開とし、$X$がHausdorffとすると
    * $B \subset A$が$A$で閉ならば、$X$でも閉

$X := (0, 1)$とし、$$\mathcal{O}_{X} := \{\emptyset, (0, 1/2), \{1/2\}, (0, 1/2], X\}$$とおくと、$(X, \mathcal{O}_{X})$は位相空間となる。
$A := (1/4, 1/2)$とおくと、$$\mathcal{O}_{A} := \{\emptyset, (1/4, 1/2), A\}$$となる。

$X := (0, 1)$とし、$$\mathcal{O}_{X} := \{\emptyset, (0, 1/4), (0, 1/2), (0, 3/4), X\}$$とおくと、$(X, \mathcal{O}_{X})$は位相空間となる。
$A := (0, 1/2)$とおくと、$$\mathcal{O}_{A} := \{\emptyset, (0, 1/4), A\}$$となる。

## Lemma.
$$(X, \mathcal{O}_{X})$$, $$(Y, \mathcal{O}_{Y})$$を位相空間とする。
$F:X \rightarrow Y$し、$$O_{X} \in \mathcal{O}_{X}$$, $$O_{Y} \in \mathcal{O}_{Y}$$とする。

* $F$が単射とすると$F(O_{X}^{c}) \supset F(O_{X})^{c}$
* $F$が全射とすると$F(O_{X}^{c}) \subset F(O_{X})^{c}$

## proof.
$\forall F(a) \in F(O_{X}^{c})$とすると、$a \in O_{X}^{c}$である。
$F(a) \notin F(O_{X})^{c}$とすると、$F(a) \in F(O_{X})$である。
よって、ある$b \in O_{X}$が存在して、$F(a) = F(b)$となる。
$F$が単射より、$a = b$となって矛盾。
よって、$F(O_{X}^{c}) \supset F(O_{X})^{c}$となる。

$y \in F(O_{X})^{c}$とする。
全射よりある$x \in X$が存在して$F(x) = y$となる。
$y \notin F(O_{X}^{c})$とすると、$F(x) \notin F(O_{X}^{c})$である。
よって、$x \in O_{X}$となるから、$y = F(x) \in F(O_{X})$となって矛盾。

## Lemma.
$$(X, \mathcal{O}_{X})$$, $$(Y, \mathcal{O}_{Y})$$を位相空間とする。
$F: X \rightarrow Y$とする。

* $\forall B \subset Y$, $F^{-1}(B)^{c} = F^{-1}(B^{c})$

## proof.
$\forall a \in F^{-1}(B)^{c}$とすると、$F(a) \notin B$となる。
よって、$F(a) \in B^{c}$で、$a \in F^{-1}(B^{c})$となる。

## Def(interior, closure)
$A \subset X$とすると、$A$の内部$\mathrm{Int}A$, $A^{\circ}$を以下で定義する。

$$
    \mathcal{O}(A) :=
        \left\{
            A^{\prime} \in \mathcal{O}_{X} \mid A^{\prime} \subseteq A
        \right\},
    \quad
    A^{\circ} := \bigcup_{A^{\prime} \in \mathcal{O}(A)} A^{\prime}
$$

$A$の内部は、$A$に含まれる開集合全体の和集合である。

$A$の外部$\overline{A}$を以下で定義する。　
$\mathcal{U}_{X}$を$X$の閉集合全体とする。

$$
    \mathcal{U}(A)
        := 
        \left\{
            A^{\prime} \in \mathcal{U}_{X} \mid A \subseteq A^{\prime}
        \right\},
    \quad
    \overline{A} := \bigcap_{A^{\prime} \in \mathcal{A}} A^{\prime}
$$

$A$の外部は、$A$を含む閉集合全体である。

## Lemma.
$A \subset X$

* $\overline{A^{c}} = (A^{\circ})^{c}$
* $(\overline{A})^{c} = (A^{c})^{\circ}$

## proof.
$\forall B \in \mathcal{O}(A)$について、$B \subset A$より$B^{c} \supset A^{c}$となるから、$B^{c}$は$A$を含む閉集合である。

$$
\begin{eqnarray}
    (A^{\circ})^{c}
        & = &
            (\bigcup_{B \in \mathcal{O}(A)} B)^{c} 
    \nonumber
    \\
        & = &
            \bigcap_{B \in \mathcal{O}(A)} B^{c}
    \nonumber
    \\
    & = &
        \overline{A^{c}}    
    \nonumber
\end{eqnarray}
$$

$\forall B \in \mathcal{U}(A)$について、$B \supset A$より$B^{c} \subset A^{c}$となるから、$B^{c}$は$A$をに含まれる開集合である。

$$
\begin{eqnarray}
    (\overline{A})^{c}
        & = &
            (\bigcap_{B \in \mathcal{U}(A)} B)^{c} 
    \nonumber
    \\
        & = &
            \bigcup_{B \in \mathcal{U}(A)} B^{c}
    \nonumber
    \\
    & = &
        (A^{c})^{\circ}
    \nonumber
\end{eqnarray}
$$

## Reference
* http://jeff560.tripod.com/set.html
