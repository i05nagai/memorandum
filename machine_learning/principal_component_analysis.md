---
title: Principal Component Analysis
---

## Principal Component Analysis
PCAは教師なし学習。
LDAは教師あり学習。

TODO:
以下の議論では、真の分布の期待値が既知であることを利用している。
平均の推定量に置き換えた議論が必要。

### Definition(Singular Value Decomposition)
$A$は$N \times N$行列

$$
    A
    :=
    P D P^{\mathrm{T}}
$$

の分解を特異値分解という。
ここで、

* $$ D := \diag(\lambda_{1}, \ldots, \lambda_{N})$$,
* $$\lambda_{1} \ge \cdots \ge \lambda_{N}$$,
* $\lambda_{i}$は$A$の固有値
* $P$は直交行列で、$i$番目の列ベクトルは$\lambda_{i}$に対応する$A$の固有ベクトル

$$P = (p_{1}, \ldots, p_{N})$$とかけば

$$
    A p_{i} = \lambda_{i} p_{i}
$$

が成立する。

## Definition
* $N$
    * データの数
* $d$
    * 特徴量の次元
* $$
    X
    =
    \left(
        \begin{array}{c}
            X^{1} \\
            \vdots \\
            X^{d}
        \end{array}
    \right)
$$,
    * データの真の分布
    * $d$次元
* $$
    X_{i}
    :=
    \left(
        \begin{array}{c}
            X_{i}^{1} \\
            \vdots \\
            X_{i}^{d}
        \end{array}
    \right)
    \
    \forall i = 1, \ldots, N
$$,
    * $d$次元確率変数
    * 二乗可積分
    * $X$のi.i.d
* $x_{i} := X_{i}(\omega)$
    * $X_{i}$の実現値
* $$
    \mu
    :=
    \left(
        \begin{array}{c}
            \mu^{1} \\
            \vdots \\
            \mu^{d}
        \end{array}
    \right)
    :=
    \left(
        \begin{array}{c}
            \mathrm{E}(X^{1}) \\
            \vdots \\
            \mathrm{E}(X^{d})
        \end{array}
    \right)
$$,

また、$X$の共分散行列を以下で定義する。

$$
\begin{eqnarray}
    \mathrm{Cov}
    \left[
        X
    \right]
    & := &
        \mathrm{E}
        \left[
            (X - \mu)(X - \mu)^{\mathrm{T}}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \left(
                \begin{array}{llll}
                    (X^{1} - \mu^{1})^{2} 
                        & (X^{1} - \mu^{1})(X^{2} - \mu^{2})
                        & \cdots 
                        & (X^{1} - \mu^{1})(X^{d} - \mu^{d})
                        \\
                    (X^{1} - \mu^{1})(X^{2} - \mu^{2})
                        & (X^{2} - \mu^{2})^{2}
                        & \cdots 
                        & (X^{2} - \mu^{2})(X^{d} - \mu^{d})
                        \\
                    \vdots
                        & 
                        & \ddots
                        & \vdots
                        \\
                    (X^{1} - \mu^{1})(X^{d} - \mu^{d})
                        & (X^{1} - \mu^{1})(X^{d} - \mu^{d} )
                        & \cdots 
                        & (X^{d} - \mu^{d})^{2}
                \end{array}
            \right)
        \right]
\end{eqnarray}
$$,

$X$と同分布の確率変数について

$$
    \mathrm{Cov}
    \left[
        X
    \right]
    =
    \mathrm{Cov}
    \left[
        X_{i}
    \right]
    \
    \forall i = 1, \ldots, N
$$

に注意しておく。
また、共分散行列は対称かつ半正定値である。
実際、対称なのは明らかで、半正定値性はJensenの不等式より、$\forall x \in \mathbb{R}^{d}$について

$$
\begin{eqnarray}
    x^{\mathrm{T}}
    \mathrm{Cov}(X)
    x
    & = &
        \sum_{j=1}^{d}
            \sum_{k=1}^{d}
                x_{j}
                x_{k}
                \mathrm{E}
                \left[
                    (X^{j} - \mu^{j})
                    (X^{k} - \mu^{k})
                \right]
    \nonumber
    \\
    & \ge &
        \sum_{j=1}^{d}
            \sum_{k=1}^{d}
                x_{j}
                x_{k}
                \mathrm{E}
                \left[
                    (X^{j} - \mu^{j})
                \right]
                \mathrm{E}
                \left[
                    (X^{k} - \mu^{k})
                \right]
    \nonumber
    \\
    & = &
        0
    \nonumber
\end{eqnarray}
$$

である。

## Theory
$A := \mathrm{Cov}(X)$とおく。
$A$のスペクトル分解を考え、$A = PDP^{\mathrm{T}}$とおく。
また、$$P = (p_{1} \ldots p_{d})$$と列ベクトルでかく。

$i$-th Principal Componentを以下で定義する。

$$
\begin{eqnarray}
    Y
    & := &
        A^{\mathrm{T}}(X - \mu)
    \label{def_transformed_random_variable}
    \\
    Y^{j}
    & := &
        p_{j}^{\mathrm{T}}(X - \mu)
    \label{def_transformed_element_of_random_variable}
\end{eqnarray}
$$
 
定義より

$$
\begin{eqnarray}
    X
    & = &
        \mu
        +
        AY
    \nonumber
    \\
    & = &
        \mu
        +
        \sum_{j=1}^{d}
            Y^{j}a_{j}
\end{eqnarray}
$$

となる。
更に$Y$は以下の性質を持つ。

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        Y^{j}
    \right]
    & = &
        p_{j}^{\mathrm{T}}(\mathrm{E}(X) - \mu)
    \nonumber
    \\
    & = &
        0,
    \nonumber
    \\
    \mathrm{E}
    \left[
        Y
    \right]
    & = &
        0
    \nonumber
\end{eqnarray}
$$

また、

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        Y^{j}Y^{k}
    \right]
    & = &
        \mathrm{E}
        \left[
            p_{j}^{\mathrm{T}}
                (X - \mu)
                p_{k}^{\mathrm{T}}
                (X - \mu)
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            p_{j}^{\mathrm{T}}
                (X - \mu)
                (X - \mu)^{\mathrm{T}}
                p_{k}
        \right]
    \nonumber
    \\
    & = &
        p_{j}^{\mathrm{T}}
            \mathrm{E}
            \left[
                (X - \mu)
                (X - \mu)^{\mathrm{T}}
            \right]
            p_{k}
    \nonumber
    \\
    & = &
        p_{j}^{\mathrm{T}}
            \mathrm{Cov}
            \left[
                X
            \right]
            p_{k}
\end{eqnarray}
$$

よって、

$$
\begin{eqnarray}
    \mathrm{Cov}
    \left[
        Y
    \right]
    & = &
        \mathrm{E}
        \left(
            \begin{array}{llll}
                (Y^{1})^{2}
                    & Y^{1}Y^{2}
                    & \cdots
                    & Y^{1}Y^{d}
                \\
                Y^{1}Y^{2}
                    & (Y^{2})^{2}
                    & \cdots
                    & Y^{1}Y^{d}
                \\
                \vdots
                    & 
                    & \ddots
                    & \vdots
                \\
                Y^{1}Y^{d}
                    & Y^{2}Y^{d}
                    & \cdots
                    & (Y^{d})^{2}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        P^{\mathrm{T}}
            \mathrm{Cov}
            \left[
                X
            \right]
            P
    \nonumber
    \\
    & = &
        P^{\mathrm{T}}PDP^{\mathrm{T}}P
    \nonumber
    \\
    & = &
        D
    \label{covariance_principal_components}
\end{eqnarray}
$$

となる。
特に、

$$
    \mathrm{Var}
    \left[
        Y^{j}
    \right]
    =
    \lambda_{j}
$$

が$$\eqref{covariance_principal_components}$$より分かる。
スペクトル分解の固有値を大きい順に取っていたので、$Y^{j}$は分散が大きい順に並んだ確率変数となっている。
この分解をPricipal Component Analysisという。

また、

$$
\begin{eqnarray}
    \sum_{j=1}^{d}
        \mathrm{Var}
        \left[
            X^{j}
        \right]
    & = &
        \mathrm{trace}(A)
    \nonumber
    \\
    & = &
        \sum_{j=1}^{d}
            \lambda_{j}
    \nonumber
    \\
    & = &
        \sum_{j=1}^{d}
            \mathrm{Var}
            \left[
                Y^{j}
            \right]
    \nonumber
\end{eqnarray}
$$

より、

$$
    \frac{
        \sum_{j=1}^{k}
            \lambda_{j}
    }{
        \sum_{j=1}^{d}
            \lambda_{j}
    }
$$

は、pricncipal componentの最初の$k$個で表現できる$X$の分散度合いを表す。
上記の$X$についての議論は、$X$と同分布の確率変数についても同様に成り立つ。
よって、$X^{j}$について$$\eqref{def_transformed_random_variable}$$の変換を施すことで、新しい確率変数とその実現値を得ることができる。
つまり、確率変数

$$
    Y_{i}^{j}
    :=
    p_{j}^{\mathrm{T}}
    (X_{i} - \mu)
$$

及び実現値

$$
    y_{i}
    :=
    Y_{i}(\omega)
$$

を定義できる。
これらは、$$\eqref{def_transformed_random_variable}$$と同じ性質をもつ。

PCAのもう一つのformulationを考える。
上で構成した$Y^{1}$は次の性質を満たす。

### Proposition

$$
\begin{eqnarray}
    \mathrm{Var}
    \left[
        Y^{1}
    \right]
    & = &
        \mathrm{Var}
        \left[
            p_{1}^{\mathrm{T}}X
        \right]
    \nonumber
    \\
    & = &
        \max
        \left\{
            \mathrm{Var}
            \left[
                b^{\mathrm{T}}X 
            \right]
            \mid
            b^{\mathrm{T}}b = 1
        \right\}
\end{eqnarray}
$$

最右辺はベクトルが直交しているものの中で、$X$とベクトルの内積の分散の最大値である。
更に以下も分かる。

$$
\begin{eqnarray}
    \mathrm{Var}
    \left[
        Y^{j}
    \right]
    & = &
        \mathrm{Var}
        \left[
            p_{i}^{\mathrm{T}}X
        \right]
    \nonumber
    \\
    & = &
        \max
        \left\{
            \mathrm{Var}
            \left[
                b^{\mathrm{T}}X 
            \right]
        \mid
            \forall j = 1, \ldots, i - 1,
            \
            p_{j}^{\mathrm{T}}b = 0,
            \
            b^{\mathrm{T}}b = 1
        \right\}
\end{eqnarray}
$$

$Y^{j}$の分散は、$i - 1$までの全てのベクトルと直交するものの中で最大の分散である。

### proof.
まず、極値を取るためには、$b$は固有ベクトルである必要があることを述べる。

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \left(
            \sum_{j=1}^{d}
                b_{j} X^{j}
            -
            \sum_{j=1}^{d}
                b_{j}
                    \mathrm{E}(X^{j})
        \right)^{2}
    \right]
    & = &
        \mathrm{E}
        \left[
            \left(
                \sum_{j=1}^{d}
                    b_{j}
                    \left(
                        X^{j}
                        -
                        \mathrm{E}(X^{j})
                    \right)
            \right)^{2}
        \right]
    \nonumber
    \\
    & = &
        \sum_{j=1}^{d}
            \sum_{k=1}^{d}
                b_{j}
                b_{k}
                \mathrm{E}
                \left[
                    \left(
                        X^{j}
                        -
                        \mu^{j}
                    \right)
                    \left(
                        X^{k}
                        -
                        \mu^{k}
                    \right)
                \right]
    \nonumber
\end{eqnarray}
$$

Lagrange乗数を$\mu$とおくとLagrange関数は、

$$
    L(b)
    :=
    \sum_{j=1}^{d}
        \sum_{k=1}^{d}
            b_{j}
            b_{k}
            \mathrm{E}
            \left[
                \left(
                    X^{j}
                    -
                    \mu^{j}
                \right)
                \left(
                    X^{k}
                    -
                    \mu^{k}
                \right)
            \right]
    -
    \mu
    \left(
        \sum_{j=1}^{d}
            b_{j}^{2}
        -
        1
    \right)
$$

となる。
偏微分を求めると、

$$
\begin{eqnarray}
    \frac{\partial L(b)}{\partial b_{k}} 
    & = &
        \sum_{j=1}^{d}
            b_{j}
            \mathrm{E}
            \left[
                \left(
                    X^{j}
                    -
                    \mu^{j}
                \right)
                \left(
                    X^{k}
                    -
                    \mu^{k}
                \right)
            \right]
        +
        \sum_{j=1}^{d}
            b_{j}
            \mathrm{E}
            \left[
                \left(
                    X^{k}
                    -
                    \mu^{k}
                \right)
                \left(
                    X^{j}
                    -
                    \mu^{j}
                \right)
            \right]
        -
        2
            \mu
            b_{k}
    \nonumber
    \\
    & = &
        2
        \sum_{j=1}^{d}
            b_{j}
            \mathrm{E}
            \left[
                \left(
                    X^{j}
                    -
                    \mu^{j}
                \right)
                \left(
                    X^{k}
                    -
                    \mu^{k}
                \right)
            \right]
        -
        2
            \mu
            b_{k}
\end{eqnarray}
$$

最適性の一次の条件より、

$$
\begin{eqnarray}
    & &
        \frac{\partial L(b)}{\partial b_{k}} 
        =
        0
        \
        (\forall k = 1, \ldots, d)
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=1}^{d}
            b_{i}
            \mathrm{E}
            \left[
                \left(
                    X^{j}
                    -
                    \mu^{j}
                \right)
                \left(
                    X^{k}
                    -
                    \mu^{k}
                \right)
            \right]
        =
        \mu
        b_{k}
        \
        (\forall k = 1, \ldots, d)
    \nonumber
    \\
    & \Leftrightarrow &
        \mathrm{Cov}
        \left[
            X
        \right]
        b
        =
        \mu
        b
    \nonumber
\end{eqnarray}
$$

となって、$b$は$\mathrm{Cov}(X)$の固有ベクトルである。
今$ \mathrm{Cov}(X)$の固有ベクトルは$$p_{1}, \ldots, p_{d}$$であったから、

$$
    \mathrm{Var}
    \left[
        p_{j}^{\mathrm{T}}X
    \right]
    =
    \lambda_{j}
$$

である。
この中で、最大のものは$\lambda_{1}$なので、命題が示された。

<div class="QED" style="text-align: right">$\Box$</div>

上記の命題より、$$ \mathrm{Var}(b^{\mathrm{T}}X)$$を最大にする$b$をみつけることでPCAを構成する方法もある。

## Reference

