---
title: LU decomposition
---

## LU decomposition
LU decomposition is a method to decompose a matrix $A$ into a product of lower triangular matrix $L$ and upper triangular matrix $U$.
In other words, it constructs $L$ and $U$ satisfying

$$
    A = LU
    .
$$

## Symbols
* $A = (a_{j}^{i})_{i,j}$
    * $M$-rows $N$-cols matrix
* $L = (l_{j}^{i})_{i,j}$
    * $M$-rows $N$-cols lower triangular matrix
* $U = (u_{j}^{i})_{i,j}$
    * $M$-rows $N$-cols upper triangular matrix
* $D = (d_{j}^{i})_{i,j}$
    * $M$-rows $M$-cols diagonal matrix

## Theory
Suppose $M \le N$.
Let $L$ and $U$ be

$$
L =
    \left(
        \begin{array}{ccccc}
            1 & 0 & \ldots &   & 0\\
            l_{1}^{2} & 1 & 0 & \ldots & 0 \\
            l_{1}^{3} & l_{2}^{3} & 1 & \ldots & 0 \\
            \vdots & \vdots & \ddots & \ddots & \vdots \\
            l_{1}^{M} & l_{2}^{M} &  \ldots &  & l_{M}^{M}
        \end{array}
    \right)
$$

$$
U =
    \left(
        \begin{array}{ccccc}
            u_{1}^{1} & u_{2}^{1} & u_{3}^{2} & \ldots  & u_{N}^{1} \\
            0 & u_{2}^{2} & u_{3}^{2} & \ldots & u_{N}^{2} \\
            \vdots & 0 & u_{3}^{3} & \ldots & 0 \\
             & \vdots & \ddots & \ddots & \vdots \\
            0 & 0 & \ldots &  & u_{N}^{M}
        \end{array}
    \right)
$$

$A = LU$から$N \times N$の連立方程式ができる。
$L$の対角成分を1としているので、未知変数も$N \times N$となって解ける。
具体的な解き方は、$A$の(1, 1)成分から1行目、2行目と順に解いていけば逐次求まる。
実際$\forall i = 1, \ldots, M, \forall j = 1, \ldots, N$

$$
    a_{j}^{i} = \sum_{k}l_{k}^{i}u_{j}^{k} 
$$

が成立する。
$i=1$とすると、

$$
a_{j}^{1} = u_{j}^{1}
$$

である。

$i=2$とすると、まず

$$
\begin{eqnarray*}
    a_{1}^{2} & = & l_{1}^{2} u_{1}^{1} \\
    l_{1}^{2} & = & \frac{a_{1}^{2}}{u_{1}^{1}} = \frac{a_{1}^{2}}{a_{1}^{1}} 
\end{eqnarray*}
$$

となり、$l_{1}^{2}$が求まる。
ただし、$u_{1}^{1} = a_{1}^{1} \neq 0$としておく。
$j = 2, \ldots, N$について

$$
\begin{eqnarray*}
    a_{j}^{2} & = & l_{1}^{2} u_{j}^{1} + l_{2}^{2} u_{j}^{2} \\
    u_{j}^{2} & = & a_{j}^{2} - l_{1}^{2} u_{j}^{1}
\end{eqnarray*}
$$

となる。
同様に$i=3$とすると、まず

$$
\begin{eqnarray*}
    a_{1}^{3} & = & l_{1}^{3} u_{1}^{1} \\
    l_{1}^{3} & = & \frac{a_{1}^{3}}{u_{1}^{1}}
\end{eqnarray*}
$$

さらに、

$$
\begin{eqnarray*}
    a_{2}^{3} & = & l_{1}^{3} u_{2}^{1} + l_{2}^{3} u_{2}^{2} \\
    l_{2}^{3} & = & \frac{a_{2}^{3} - l_{1}^{3} u_{2}^{1}}{u_{2}^{2}}
\end{eqnarray*}
$$

となり、$l_{1}^{3}, l_{2}^{3}$が求まる。
ただし、$u_{2}^{2} \neq 0$としておく。
$j = 3, \ldots, N$とすると、

$$
\begin{eqnarray*}
    a_{j}^{3} & = & l_{1}^{3} u_{j}^{1} + l_{2}^{3} u_{j}^{2} + l_{3}^{3} u_{j}^{3}\\
    u_{j}^{3} & = & a_{j}^{3} - \sum_{k=1}^{j-1}l_{k}^{3} u_{j}^{k}
\end{eqnarray*}
$$

同様に$i=4$とすると

$$
\begin{eqnarray*}
    l_{1}^{i} & = & \frac{a_{1}^{i} - \sum_{k=1}^{1-1}l_{k}^{i} u_{1}^{k}}{u_{1}^{1}} \\
    l_{2}^{i} & = & \frac{a_{2}^{i} - \sum_{k=1}^{2-1}l_{k}^{i} u_{2}^{k}}{u_{2}^{2}} \\
     & \vdots &  \\
    l_{i-1}^{i} & = & \frac{a_{2}^{i} - \sum_{k=1}^{i-1-1}l_{k}^{i} u_{2}^{k}}{u_{i-1}^{i-1}} 
\end{eqnarray*}
$$

が求まる。
ただし、$u_{i-1}^{i-1} \neq 0$としておく。
$j = i, \ldots, N$とすると

$$
\begin{eqnarray*}
    u_{j}^{i} & = & a_{j}^{i} - \sum_{k=1}^{j-1}l_{k}^{i} u_{j}^{k}
\end{eqnarray*}
$$

を得る。
以上を繰り返せば、$L, U$が求まる。

## algorithm1
Theoryの手順に従い順番に要素を求める。

## Theory2

## algorithm2
この方法は、$L$の1列目、$U$の1行目が$A$から求まることを利用し、$L$の1列目、$U$の1行目を求めたあと、$A$のサイズを1行1列ずつ小さくした行列を考え、順次$L, U$を求めていく方法となる。

### Step1
$A^{(1)}:=A, L^{(0)}:= O_{M,M}, U^{(0)} := O_{M,N}, k := 1$とおく。

### Step2
$$
u_{j}^{k} := 
    \begin{cases}
        0 & (j = 1, \ldots, k-1) \\
        a_{j}^{k,(k)} & (j=k, \ldots, n) 
    \end{cases}
$$

$$
l_{k}^{i} := 
    \begin{cases}
        0 & (i = 1, \ldots, k-1) \\
        1 & (i = k) \\
        \frac{a_{k}^{i,(k)} }{a_{k}^{k,(k)}} & (i=k, \ldots, n) 
    \end{cases}
$$

それぞれ、$l_{k} := (l_{k}^{M}, \ldots, l_{k}^{M}), u_{k} := (u_{1}^{k}, \ldots, u_{N}^{k})$とおく。
$L^{(k+1)}$を$L^{(K)}$の$k$列目を$l_{k}$で置き換えた行列とする。
$U^{(k+1)}$を$U^{(K)}$の$k$行目を$u_{k}$で置き換えた行列とする。
$k=M$ならば終了し、 $k < M$ならばStep3へいく。

### Step3
$$
    a_{j}^{i,(k + 1)} :=
        \begin{cases}	
            0 & (i = 1, \ldots, k) \vee (j = 1, \ldots, k) \\
            a_{j}^{i,(k)} - l_{k}^{i}u_{j}^{k} = a_{j}^{i,(k)} - \frac{a_{k}^{i,(i)}a_{j}^{k,(k)}}{a_{k}^{k,(k)}}  & (i = k+1, \ldots, M) \wedge (j = k+1, \ldots, N) 
        \end{cases}
$$

$A^{(k+1)} := (a_{j}^{i,(k+1)})_{i,j}$とする。
$k := k+1$として、Step2に戻る。

## Application

### Inverting matrix

### Solve linear equations
* $A \in \mathbb{R}^{n \times n}$,
* $L \in \mathbb{R}^{n \times n}$,
    * lower triangular matrix of $A$,
* $U \in \mathbb{R}^{n \times n}$,
    * upper triangular matrix of $A$,
* $b \in \mathbb{R}^{n}$,

Solve

$$
    Ax = b
    .
$$

Firstly, we solve the following equation with respect to $y$;

$$
    Ly = b
    .
$$

By using the solution $y$, we solve the following equation.

$$
    Ux = y
    .
$$

$$
    y^{i}
    :=
    \frac{1}{l_{i}^{i}}
    \left(
        b^{i}
        -
        \sum_{k=1}^{i-1}
        y^{k}
        l_{k}^{i}
    \right)
    .
$$

$$
    x^{i}
    :=
    \frac{1}{l_{i}^{i}}
    \left(
        y^{i}
        -
        \sum_{k=1}^{n-i}
        x^{n-k}
        l_{n-k}^{i}
    \right)
    .
$$


## reference
[LU decomposition - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/LU_decomposition)

