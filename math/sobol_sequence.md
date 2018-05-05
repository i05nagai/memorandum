---
title: Sobol Sequence
---

## Sobol Sequence

## Definition
$d$次元のsobol列を作る方法を述べる。

* $d \in \mathbb{N}$
    * 生成する点列の次元
* $K \in \mathbb{N}$
    * 生成する点のbit数
    * 32bitの点を生成する場合は$K=32$
    * 64bitの点を生成する場合は$K=64$
* $j = 1, \ldots, d$
    * 次元を表す
* $$i = (i_{K}, \ldots, i_{1})_{2}$$,
    * $i$番目の点とその2進数表現
    * $$i_{k} \in \{0, 1\}$$,
* $$x_{i} := (x_{i, 1}, \ldots, x_{i, d}) \in [0, 1]^{d}$$,
    * $i$番目の点を表す
* $p_{j} \in \mathbb{F}_{2}[x]$
    * $j$番目の次元の生成に用いる原始多項式
    * $$\dim(p_{j}) =: s_{j}$$,
    * 予め生成したい次元数分用意しておく
    * 動的に原始多項式を見つけることもできるが、余分な時間がかかる
* $$m_{1, j}, \ldots, m_{s_{j}, j} \in \mathbb{N} \ (\forall j = 1, \ldots, d)$$,
    * $s_{j}$まではあらかじめきめる
    * $s_{j}$以降は以前の$s_{j}$個を使って再帰的に決める
* $v_{1 ,j}, \ldots, v_{K, j}$
    * 次元$j$の$k$bit目に対するdirection number

## Algorithm
sobol sequenceは各次元ごとに独立に生成できるので、$j = 1, \ldots, d$を一つ固定し、 $j$次元目の点の生成方法について述べる。
まず、次数$s_{j}$の既約多項式$p_{j}$をとる。

$$
\begin{equation}
    p_{j}(x)
    :=
    a_{s_{j}}
    x^{s_{j}}
    +
    a_{s_{j} - 1, j} x^{s_{j} - 1}
    +
    a_{s_{j} - 2, j} x^{s_{j} - 2}
    +
    \cdots
    +
    a_{1, j}
    x
    +
    a_{0, j}
\end{equation}
$$

ここで、$$a_{0, j}, a_{1, j}, \ldots, a_{s_{j}, j} \in \{0, 1\}$$である。
初期値$$1 \le m_{1, j}, \ldots, m_{s_{j}, j}$$を$$m_{k, j} < 2^{k}\ (\forall k = 1, \ldots, s_{j})$$を満たす奇数としてとる。
正の定数$$m_{s_{j}+1, j}, m_{s_{j}+2, j}, \ldots, m_{K, j}$$を、前$s_{j}$個を使って次のように再帰的に定義する。

$$
\begin{eqnarray}
    k = s_{j} + 1, s_{j} + 2, \ldots, s_{j} + 1 + K,
    \quad
    m_{k, j}
    & := &
        2
            a_{1, j} m_{k-1, j}
        \oplus
        2^{2}
            a_{2, j} m_{k-2, j}
        \oplus
        \cdots
        \oplus
        2^{s_{j}-1}
            a_{s_{j} - 1, j}
            m_{k - s_{j} + 1, j}
        \oplus
        2^{s_{j}}
        a_{s_{j}, j}
        m_{k-s_{j}, j}
        \oplus
        m_{k-s_{j}, j},
    \nonumber
    \\
    & = &
        2
            a_{1, j}
            m_{k-1, j}
        \oplus
        2^{2}
            a_{2, j} m_{k-2, j}
        \oplus
        \cdots
        \oplus
        2^{s_{j}-1}
            a_{s_{j} - 1, j}
            m_{k - s_{j} + 1, j}
        \oplus
        2^{s_{j}}
            m_{k-s_{j}, j}
        \oplus
        m_{k-s_{j}, j},
        \quad
        (\because a_{s_{j}} = 1)
    \nonumber
    \\
    & := &
        \left(
            \bigoplus_{i=1}^{s_{j}}
                2^{i}a_{i, j} m_{k-i, j}
        \right)
        \oplus
        m_{k-s_{j}, j},
    \label{sobol_sequence_def_initial_number}
\end{eqnarray}
$$

$\oplus$はbitごとのXORである。
また、$a_{s, j} m_{k, j}$は通常の積である。
上で定義した$m_{k,j}$を用いて、direction numberを次で定義する。

$$
\begin{equation}
    k = 1, 2, \ldots, K,
    \
    v_{k, j}
    :=
    \frac{
        m_{k, j}
    }{
        2^{k}
    }
    \label{sobol_sequence_def_direction_number}
\end{equation}
$$

と定義する。
$i$番目の$j$次元の点を以下で定義する。

$$
\begin{equation}
    x_{i, j}
    :=
    i_{1} v_{1, j}
    \oplus
    i_{2} v_{2, j}
    \oplus
    \cdots
    \oplus
    i_{K} v_{K, j}
    \label{original_sobol_sequence}
\end{equation}
$$

ここで、$i_{k}$は$i$の$k$bit目の2進表現で、 $$i = (i_{K}, \ldots, i_{3}, i_{2}, i_{1})_{2}$$である。

### Note
$$\eqref{sobol_sequence_def_initial_number}$$ and $$\eqref{sobol_sequence_def_direction_number}$$ also can be written for $j = 1, \ldots, d$,

$$
\begin{eqnarray}
    k = 1, \ldots, s_{j},
    \quad
    m_{k, j}^{\mathrm{new}}
    & := &
        2^{K-k}
        m_{k, j},
    \nonumber
    \\
    k = s_{j} + 1, s_{j} + 2, \ldots, s_{j} + 1 + K,
    \quad
    m_{k, j}^{\mathrm{new}}
    & := &
        2^{K-k}
        m_{k, j}
    \nonumber
    \\
    & = &
        2^{K-k}
        \left[
            \left(
                \bigoplus_{i=1}^{s_{j}}
                    2^{i}
                    2^{k-i-K}
                    2^{K-(k-i)}
                    a_{i, j}
                    m_{k-i, j}
            \right)
            \oplus
            2^{k-s_{j}-K}
            2^{K-(k-s_{j})}
            m_{k-s_{j}, j}
        \right]
    \nonumber
    \\
    & = &
        2^{K-k}
        \left[
            \left(
                \bigoplus_{i=1}^{s_{j}}
                    2^{i}
                    2^{k-i-K}
                    a_{i, j}
                    m_{k-i, j}^{\mathrm{new}}
            \right)
            \oplus
            2^{k-s_{j}-K}
            m_{k-s_{j}, j}^{\mathrm{new}}
        \right]
    \nonumber
    \\
    & = &
        2^{K-k}
        \left[
            \left(
                \bigoplus_{i=1}^{s_{j}}
                    2^{k-K}
                    a_{i, j}
                    m_{k-i, j}^{\mathrm{new}}
            \right)
            \oplus
            2^{k-s_{j}-K}
            m_{k-s_{j}, j}^{\mathrm{new}}
        \right]
    \nonumber
    \\
    & = &
        \left(
            \bigoplus_{i=1}^{s_{j}}
                a_{i, j}
                m_{k-i, j}^{\mathrm{new}}
        \right)
        \oplus
        2^{-s_{j}}
        m_{k-s_{j}, j}^{\mathrm{new}}
\end{eqnarray}
$$

For each $j$, direction numbers hold following relation,

$$
\begin{eqnarray}
    k = 1, \ldots, K,
    \quad
    & &
        v_{k, j}
    & = &
        2^{-K}
        m_{k, j}^{\mathrm{new}}
        .
    \nonumber
    \\
\end{eqnarray}
$$

With $m_{k,j}^{\mathrm{new}}$, we denote new integer by

$$
\begin{eqnarray}
    k = 1, \ldots, K,
    \quad
    x_{i, j}^{\mathrm{new}}
    & := &
        \bigoplus_{k=1}^{K}
            i_{k}
            m_{k, j}^{\mathrm{new}}
    .
    \nonumber
\end{eqnarray}
$$

Then we have

$$
\begin{eqnarray}
    k = 1, \ldots, K,
    \quad
    x_{i, j}
    & = &
        2^{-K}
        x_{i, j}^{\mathrm{new}}
    \nonumber
    \\
    & = &
        2^{-K}
        \bigoplus_{k=1}^{K}
            i_{k}
            v_{k, j}^{\mathrm{new}}
        \nonumber
    \nonumber
    \\
    & = &
        \bigoplus_{k=1}^{K}
            i_{k}
            v_{k, j}
        \nonumber
\end{eqnarray}
$$

In most programming languages, there is no bit wise XOR for floating point values. Because $$m_{k, j}^{\mathrm{new}}$$ are integers, we only need to calculate bit wise XOR for integer values.

## Example
* $d := 3$,
* $K := 3$,
* $$p_{1}(x) := x$$,
    * $$a_{1} := 1$$,
    * $$a_{0} := 0$$,
* $$s_{1} := \mathrm{deg}(p_{1}) = 1$$,
* $$p_{2}(x) := x + 1$$,
    * $$a_{1} := 1$$,
    * $$a_{0} := 1$$,
* $$s_{2} := \mathrm{deg}(p_{2}) = 1$$,
* $$p_{3}(x) := x^{2} + x + 1$$,
    * $$a_{2} := 1$$,
    * $$a_{1} := 1$$,
    * $$a_{0} := 1$$,
* $$s_{3} := \mathrm{deg}(p_{3}) = 2$$,
* $$m_{k, 1}$$,
    * $$m_{1, 1} := 1$$,
* $$m_{k, 2}$$,
    * $$m_{1, 2} := 1$$,
* $$m_{k, 3}$$,
    * $$m_{1, 2} := 1$$,
    * $$m_{1, 2} := 3$$,

$$
\begin{eqnarray}
    m_{2, 1}
    & := &
        2 a_{1 - 1} m_{2 - 1, 1}
        \oplus
         m_{2 - 1, 1}
    \nonumber
    \\
    & = &
         1
    \nonumber
    \\
    m_{3, 1}
    & := &
        2 a_{1 - 1} m_{3 - 1, 1}
        \oplus
         m_{3 - 1, 1}
    \nonumber
    \\
    & = &
         1
    \nonumber
    \\
    m_{4, 1}
    & := &
        2 a_{1 - 1} m_{4 - 1, 1}
        \oplus
         m_{4 - 1, 1}
    \nonumber
    \\
    & = &
         1
    \nonumber
\end{eqnarray}
$$

Direction numberは

$$
\begin{eqnarray}
    v_{1, 1}
    & := &
        \frac{1}{2}
        =
        (0.1)_{2}
    \nonumber
    \\
    v_{2, 1}
    & := &
        \frac{1}{4}
        =
        (0.01)_{2}
    \nonumber
    \\
    v_{3, 1}
    & := &
        \frac{1}{8}
        =
        (0.001)_{2}
    \nonumber
    \\
    v_{4, 1}
    & := &
        \frac{1}{16}
        =
        (0.0001)_{2}
    \nonumber
\end{eqnarray}
$$

となる。
このとき、 $i = 11 = (1011)_{2}$であれば

$$
\begin{eqnarray}
    x_{11, 1}
    & = &
        1
        (0.1)_{2}
        \oplus
        1
        (0.01)_{2}
        \oplus
        0
        (0.001)_{2}
        \oplus
        1
        (0.001)_{2}
    \nonumber
    \\
    & = &
        (0.1)_{2}
        \oplus
        (0.01)_{2}
        \oplus
        (0.001)_{2}
    \nonumber
    \\
    & = &
        (0.111)_{2}
    \nonumber
\end{eqnarray}
$$

となる。
別の方法として、

$$
\begin{eqnarray}
    x_{11, 1}^{\prime}
    & := &
        (1)_{2}
        \oplus
        (11)_{2}
        \oplus
        (11)_{2}
\end{eqnarray}
$$

また、$j=2$次元は

$$
\begin{eqnarray}
    m_{2, 2}
    & := &
        2 a_{1 - 1} m_{2 - 1, 2}
        \oplus
         m_{2 - 1, 2}
    \nonumber
    \\
    & = &
        (2 \times 1 \times 1)
        \oplus
        1
    \nonumber
    \\
    & = &
        3
    \nonumber
    \\
    m_{3, 2}
    & := &
        2 a_{1 - 1} m_{3 - 1, 2}
        \oplus
        m_{3 - 1, 2}
    \nonumber
    \\
    & = &
        (2  \times 1 \times 3)
        \oplus
        3
    \nonumber
    \\
    & = &
        5
    \nonumber
    \\
    m_{4, 2}
    & := &
        2 a_{1 - 1} m_{4 - 1, 1}
        \oplus
        m_{4 - 1, 1}
    \nonumber
    \\
    & = &
         (2 \times 5)
         \oplus
         5
    \nonumber
    \\
    & = &
         (1010)_{2}
         \oplus
         (0101)_{2}
    \nonumber
    \\
    & = &
        15
    \nonumber
\end{eqnarray}
$$

Direction numberは

$$
\begin{eqnarray}
    v_{1, 2}
    & := &
        \frac{1}{2}
        =
        (0.1)_{2}
    \nonumber
    \\
    v_{2, 2}
    & := &
        \frac{3}{4}
        =
        (0.11)_{2}
    \nonumber
    \\
    v_{3, 2}
    & := &
        \frac{5}{8}
        =
        (0.101)_{2}
    \nonumber
    \\
    v_{3, 2}
    & := &
        \frac{15}{16}
        =
        (0.1111)_{2}
    \nonumber
\end{eqnarray}
$$

である。
このとき、$i = 11 = (01011)_{2}$のとき、

$$
\begin{eqnarray}
    x_{11,2}
    & := &
        1
        (0.1)_{2}
        \oplus
        1
        (0.11)_{2}
        \oplus
        0
        (0.101)_{2}
        \oplus
        1
        (0.1111)_{2}
    \nonumber
    \\
    & = &
        (0.1)_{2}
        \oplus
        (0.11)_{2}
        \oplus
        (0.1111)_{2}
    \nonumber
    \\
    & = &
        (0.1011)_{2}
    \nonumber
\end{eqnarray}
$$

また、

$$
\begin{eqnarray}
    m_{3, 3}
    & := &
        2 a_{2 - 1} m_{3 - 1, 3}
        \oplus
        2^{2} a_{2 - 2} m_{3 - 2, 3}
        \oplus
         m_{3 - 2, 3}
    \nonumber
    \\
    & = &
         (2 \times 3)
         \oplus
         (2^{2} \times 1)
         \oplus
         1
    \nonumber
    \\
    & = &
         (110)_{2}
         \oplus
         (100)_{2}
         \oplus
         (001)_{2}
    \nonumber
    \\
    & = &
        3
    \nonumber
    \\
    m_{4, 3}
    & := &
        2 a_{2 - 1} m_{4 - 1, 3}
        \oplus
        2^{2} a_{2 - 2} m_{4 - 2, 3}
        \oplus
        m_{4 - 2, 3}
    \nonumber
    \\
    & = &
        (2 \times 3)
        \oplus
        (4 \times 3)
        \oplus
        3
    \nonumber
    \\
    & = &
        (0110)_{2}
        \oplus
        (1100)_{2}
        \oplus
        (0011)_{2}
    \nonumber
    \\
    & = &
        9
    \nonumber
    \\
    m_{5, 3}
    & := &
        2 a_{2 - 1} m_{5 - 1, 3}
        \oplus
        2^{2} a_{2 - 2} m_{5 - 2, 3}
        \oplus
        m_{4 - 2, 3}
    \nonumber
    \\
    & = &
         (2 \times 9)
         \oplus
         (4 \times 3)
         \oplus
         (3)
    \nonumber
    \\
    & = &
        (10010)_{2}
        \oplus
        (01010)_{2}
        \oplus
        (00011)_{2}
    \nonumber
    \\
    & = &
        27
    \nonumber
\end{eqnarray}
$$

Direction numberは

$$
\begin{eqnarray}
    v_{1, 3}
    & := &
        \frac{1}{2}
        =
        (0.1)_{2}
    \nonumber
    \\
    v_{2, 3}
    & := &
        \frac{3}{4}
        =
        (0.11)_{2}
    \nonumber
    \\
    v_{3, 3}
    & := &
        \frac{3}{8}
        =
        (0.011)_{2}
    \nonumber
    \\
    v_{4, 3}
    & := &
        \frac{9}{16}
        =
        (0.1001)_{2}
    \nonumber
    \\
    v_{5, 3}
    & := &
        \frac{27}{32}
        =
        (0.11011)_{2}
    \nonumber
\end{eqnarray}
$$

となる。
このとき、例えば$i = 11 = (01011)_{2}$のとき、

$$
\begin{eqnarray}
    x_{11, 3}
    & := &
        1
        (0.1)_{2}
        \oplus
        1
        (0.11)_{2}
        \oplus
        0
        (0.011)_{2}
        \oplus
        1
        (0.1001)_{2}
        \oplus
        0
        (0.11011)_{2}
    \nonumber
    \\
    & = &
        (0.1)_{2}
        \oplus
        (0.11)_{2}
        \oplus
        (0.1001)_{2}
    \nonumber
    \\
    & = &
        (0.1101)_{2}
    \nonumber
\end{eqnarray}
$$

となる。

## Algorithm with Gray code
Gray codeを用いた高速なsobol sequenceの生成方法。
$i$番目のgray codeは以下で定義される。

$$
\begin{eqnarray}
    \mathrm{gray}(i)
    & := &
        i
        \oplus
        (i 2^{-1})
    \nonumber
    \\
    & = &
        (\ldots i_{3} i_{2} i_{1})_{2}
        \oplus
        (\ldots i_{4} i_{3} i_{2})_{2}
\end{eqnarray}
$$

つまりbit shiftし、bit wiseのXORをとれば良い。
gray codeは$\mathrm{gray}(i)$と$\mathrm{gray}(i+1)$は1bitのみ異なる。
また、$2^{n}$から$2^{n+1}$の間の2進表現は一致する。
つまり、

$$
    \{ \mathrm{gray}(i) \mid 2^{n} \le i < 2^{n+1} \}
    =
    \{ i = (\ldots i_{3}i_{2}i_{1})_{2} \mid 2^{n} \le i < 2^{n+1} \}
$$

が成り立つ。
つまり、$i$番目の点を生成する際に$i$の2進表現をgray codeに置き換えても、$2^{n}$個の点はgray codeを使わない場合と順番を除き一致する。

$$
    \mathrm{gray}(i)
    =
    (g_{i, K} \ldots g_{i, 2} g_{i, 1})_{2}
$$

とおき、$$\eqref{original_sobol_sequence}$$の式を以下におきかえる。

$$
\begin{eqnarray}
    \bar{x}_{i, j}
    & := &
        g_{i, 1} v_{1, j}
        \oplus
        g_{i, 2} v_{2, j}
        \oplus
        \cdots
        \oplus
        g_{i, K} v_{K, j}
    \nonumber
    \\
    & = &
        \bar{x}_{i, j}
        \oplus
        v_{c_{i-1}, j}
\end{eqnarray}
$$

ここで、$c_{i}$は$i$を2進表現したときに、Least Significant Bitから数えて最初の0となるbitの位置である。
つまり、$$ i = (i_{K} \ldots i_{3}i_{2}i_{1})_{2}$$ならば

$$
    c_{i}
    =
    \min_{k} \{k \in \{1, \ldots, K\} \mid i_{k} = 0 \}
$$

である。

gray codeを使えば、一つ前の点列とのXORで計算できる。

## Relation to Generalized Niederreiter Sequence
ここで、$v_{k,j}$の2進展開を以下で定義する。

$$
    \forall k = 1, \ldots, K,
    \
    \forall j = 1, \ldots, d
    \
    v_{k,j}
    =
    (0.v_{k,j,1}v_{k,j,2} \cdots)_{2}
$$

sobol sequenceにおけるgeneralized niederreiter sequenceとしての生成行列は

$$
C_{j}
:=
\left(
    \begin{array}{ccccc}
        1
        &
            v_{2,j,1}
        &
            v_{3,j,1}
        &
            \cdots
        &
            v_{K,j,1}
        \\
        0 
        &
            1
        &
            v_{3,j,2}
        &
            \cdots
        &
            v_{K,j,2}
        \\
        0
        &
            0
        &
            1
        &
            \cdots
        &
            v_{K,j,3}
        \\
        \vdots
        &
            \vdots
        &
            \vdots
        &
            \ddots
        &
            \vdots
        \\
        0
        &
            0
        &
            0
        &
            0
        &
            1
    \end{array}
\right)
$$


## Available Direction numbers
* [Sobol sequence generator](http://web.maths.unsw.edu.au/~fkuo/sobol/)
    * [web.maths.unsw.edu.au/~fkuo/sobol/new-joe-kuo-6.21201?_ga=2.243612677.1214514715.1509895936-1594151385.1508165568](http://web.maths.unsw.edu.au/~fkuo/sobol/new-joe-kuo-6.21201?_ga=2.243612677.1214514715.1509895936-1594151385.1508165568)
        * up to 21201
        * d is dimension
        * s is degree of irreducible polyonmial
        * a is coefficient of irreducible polyonmial
            * (1(2-adic expansion of a with size s-2)1) is coefficient of polynomial
            * e.g. If a is 14 and s is 8, (1(001110)1) = (10011101), that is, $$0 + 0 + 1x^{4} + 1x^{3} + 1x^{2} + 0 + 1$$.
        * m is initial direction number
            * initial value of $m$


## Reference

