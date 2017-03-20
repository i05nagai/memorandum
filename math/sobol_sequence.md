---
title: Sobol Sequence
---

## Sobol Sequence

## Definition
$d$次元のsobol列を作る方法を述べる。

* $d$
    * 生成する点列の次元
* $K$
    * 生成する点のbit数
    * 32bitの点を生成する場合は$K=32$
    * 64bitの点を生成する場合は$K=64$
* $j = 1, \ldots, d$
    * 次元を表す
* $$i = (i_{K}, \ldots, i_{1})_{2}$$,
    * $i$番目の点とその2進数表現
    * $$i_{k} \in \{0, 1\}$$,
* $$x_{i} := (x_{i, 1}, \ldots, x_{i, d})$$,
    * $i$番目の点を表す
* $p_{j}$
    * $j$番目の次元の生成に用いる原始多項式
    * $$\dim(p_{j}) =: s_{j}$$,
    * 予め生成したい次元数分用意しておく
    * 動的に原始多項式を見つける方法もあるが、余分な時間がかかる
* $$m_{1, j}, \ldots, m_{s_{j}, j}\ (\forall j = 1, \ldots, d)$$,
    * $s_{j}$まではあらかじめきめる
    * $s_{j}$以降は以前の$s_{j}$個を使って再帰的に決める
* $v_{1 ,j}, \ldots, v_{K, j}$
    * 次元$j$の$k$bit目に対するdirection number

## Algorithm
sobol sequenceは各次元ごとに独立に生成できるので、$j = 1, \ldots, d$を一つ固定し、 $j$次元目の点の生成方法について述べる。
まず、次数$s_{j}$の原始多項式$p_{j}$をとる。

$$
\begin{equation}
    p_{j}
    :=
    x^{s_{j}}
    +
    a_{1, j} x^{s_{j} - 1}
    +
    a_{2, j} x^{s_{j} - 2}
    +
    \cdots
    +
    a_{s_{j} -1, j}
    x
    +
    1
\end{equation}
$$

ここで、$$a_{1, j}, \ldots, a_{s_{j}, j} \in \{0, 1\}$$である。
正の定数$$m_{s_{j}+1, j}, m_{s_{j}+2, j}, \ldots, m_{K, j}$$を、前$s_{j}$個を使って次のように再帰的に定義する。
$$\forall k = s_{j} + 1, s_{j} + 2, \ldots, K$$について、

$$
\begin{eqnarray}
    m_{k, j}
    :=
    & &
        2 a_{1, j} m_{k-1, j}
        \oplus
        2^{2} a_{2, j} m_{k-2, j}
        \oplus
        \cdots
        \oplus
        2^{s_{j}-1} a_{s_{j}-1, j} m_{k-s_{j}, j}
        \oplus
        2^{s_{j}} m_{k-s_{j}, j}
        \oplus
        m_{k-s_{j}, j},
\end{eqnarray}
$$

$\oplus$はbitごとのXORである。
また、$a_{s, j} m_{k, j}$は通常の積である。
上で定義した$m_{k,j}$を用いて、direction numberを次で定義する。
$$\forall k = 1, 2, \ldots, K$$について

$$
\begin{equation}
    v_{k, j}
    :=
    \frac{
        m_{k, j}
    }{
        2^{k}
    }
\end{equation}
$$

と定義する。
$i$番目の点を以下で定義する。

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

## Algorithm with Gray code
Gray codeを用いた高速なsobol sequenceの生成方法。
$i$番目のgray codeは以下で定義される。

$$
\begin{equation}
    \mathrm{gray}(i)
    :=
    i
    \oplus
    \lfloor
        x
    \rfloor
    =
    (\ldots i_{3} i_{2} i_{1})_{2}
    \oplus
    (\ldots i_{4} i_{3} i_{2})_{2}
\end{equation}
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


## Reference
* [Sobol sequence generator](http://web.maths.unsw.edu.au/~fkuo/sobol/)
