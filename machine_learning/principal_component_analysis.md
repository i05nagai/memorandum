---
title: Principal Component Analysis
---

## Principal Component Analysis

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

* $$
    X
    :=
    \left(
        \begin{array}{c}
            X^{1} \\
            \vdots \\
            X^{N}
        \end{array}
    \right)
$$,
    * $N$次元確率変数
    * 二乗可積分
* $$
    \mu
    :=
    \left(
        \begin{array}{c}
            \mu^{1} \\
            \vdots \\
            \mu^{N}
        \end{array}
    \right)
    :=
    \left(
        \begin{array}{c}
            \mathrm{E}(X^{1}) \\
            \vdots \\
            \mathrm{E}(X^{N})
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
                        & (X^{1} - \mu^{1})(X^{N} - \mu^{N})
                        \\
                    (X^{1} - \mu^{1})(X^{2} - \mu^{2})
                        & (X^{2} - \mu^{2})^{2}
                        & \cdots 
                        & (X^{2} - \mu^{2})(X^{N} - \mu^{N})
                        \\
                    \vdots
                        & 
                        & \ddots
                        & \vdots
                        \\
                    (X^{1} - \mu^{1})(X^{N} - \mu^{N})
                        & (X^{1} - \mu^{1})(X^{N} - \mu^{N} )
                        & \cdots 
                        & (X^{N} - \mu^{N})^{2}
                \end{array}
            \right)
        \right]
\end{eqnarray}
$$,

$A := \mathrm{Cov}(X)$とおく。
$A$は対称かつ半正定値行列である。
実際、対称なのは明らかで、半正定値性はJensenの不等式より、$\forall x \in \mathbb{R}^{N}$について

$$
\begin{eqnarray}
    x^{\mathrm{T}}Ax
    & = &
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                x_{i}
                x_{j}
                \mathrm{E}
                \left[
                    (X^{i} - \mu^{i})
                    (X^{j} - \mu^{j})
                \right]
    \nonumber
    \\
    & \ge &
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                x_{i}
                x_{j}
                \mathrm{E}
                \left[
                    (X^{i} - \mu^{i})
                \right]
                \mathrm{E}
                \left[
                    (X^{j} - \mu^{j})
                \right]
    \nonumber
    \\
    & = &
        0
    \nonumber
\end{eqnarray}
$$

である。

$A$のスペクトル分解を考え、$A = PDP^{\mathrm{T}}$とおく。
また、$$P = (p_{1} \ldots p_{N})$$と列ベクトルでかく。

$i$-th Principal Componentを以下で定義する。

$$
\begin{eqnarray}
    Y
    & := &
        A^{\mathrm{T}}(X - \mu)
    \nonumber
    \\
    Y^{i}
    & := &
        p_{i}^{\mathrm{T}}(X - \mu)
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
        \sum_{i=1}^{N}
            Y^{i}a_{i}
\end{eqnarray}
$$

となる。
更に$Y$は以下の性質を持つ。

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        Y^{i}
    \right]
    & = &
        p_{i}^{\mathrm{T}}(\mathrm{E}(X) - \mu)
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
        Y^{i}Y^{j}
    \right]
    & = &
        \mathrm{E}
        \left[
            p_{i}^{\mathrm{T}}
                (X - \mu)
                p_{j}^{\mathrm{T}}
                (X - \mu)
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            p_{i}^{\mathrm{T}}
                (X - \mu)
                (X - \mu)^{\mathrm{T}}
                p_{j}
        \right]
    \nonumber
    \\
    & = &
        p_{i}^{\mathrm{T}}
            \mathrm{E}
            \left[
                (X - \mu)
                (X - \mu)^{\mathrm{T}}
            \right]
            p_{j}
    \nonumber
    \\
    & = &
        p_{i}^{\mathrm{T}}
            \mathrm{Cov}
            \left[
                X
            \right]
            p_{j}
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
                    & Y^{1}Y^{N}
                \\
                Y^{1}Y^{2}
                    & (Y^{2})^{2}
                    & \cdots
                    & Y^{1}Y^{N}
                \\
                \vdots
                    & 
                    & \ddots
                    & \vdots
                \\
                Y^{1}Y^{N}
                    & Y^{2}Y^{N}
                    & \cdots
                    & (Y^{N})^{2}
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
        Y^{i}
    \right]
    =
    \lambda_{i}
$$

が$$\eqref{covariance_principal_components}$$より分かる。
スペクトル分解の固有値を大きい順に取っていたので、$Y^{i}$は分散が大きい順に並んだ確率変数となっている。
この分解をPricipal Component Analysisという。

また、

$$
\begin{eqnarray}
    \sum_{i=1}^{N}
        \mathrm{Var}
        \left[
            X^{i}
        \right]
    & = &
        \mathrm{trace}(A)
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \lambda_{i}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \mathrm{Var}
            \left[
                Y^{i}
            \right]
    \nonumber
\end{eqnarray}
$$

より、

$$
    \frac{
        \sum_{i=1}^{k}
            \lambda_{i}
    }{
        \sum_{i=1}^{N}
            \lambda_{i}
    }
$$

は、pricncipal componentの最初の$k$個で表現できる$X$の分散度合いを表す。

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
        Y^{i}
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

$Y^{i}$の分散は、$i - 1$までの全てのベクトルと直交するものの中で最大の分散である。

### proof.
まず、極値を取るためには、$b$は固有ベクトルである必要があることを述べる。

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \left(
            \sum_{i=1}^{N}
                b_{i} X^{i}
            -
            \sum_{i=1}^{N}
                b_{i}
                    \mathrm{E}(X^{i})
        \right)^{2}
    \right]
    & = &
        \mathrm{E}
        \left[
            \left(
                \sum_{i=1}^{N}
                    b_{i}
                    \left(
                        X^{i}
                        -
                        \mathrm{E}(X^{i})
                    \right)
            \right)^{2}
        \right]
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                b_{i}
                b_{j}
                \mathrm{E}
                \left[
                    \left(
                        X^{i}
                        -
                        \mu^{i}
                    \right)
                    \left(
                        X^{j}
                        -
                        \mu^{j}
                    \right)
                \right]
    \nonumber
\end{eqnarray}
$$

Lagrange乗数を$\mu$とおくとLagrange関数は、

$$
    L(b)
    :=
    \sum_{i=1}^{N}
        \sum_{j=1}^{N}
            b_{i}
            b_{j}
            \mathrm{E}
            \left[
                \left(
                    X^{i}
                    -
                    \mu^{i}
                \right)
                \left(
                    X^{j}
                    -
                    \mu^{j}
                \right)
            \right]
    -
    \mu
    \left(
        \sum_{i=1}^{N}
            b_{i}^{2}
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
        \sum_{i=1}^{N}
            b_{i}
            \mathrm{E}
            \left[
                \left(
                    X^{i}
                    -
                    \mu^{i}
                \right)
                \left(
                    X^{k}
                    -
                    \mu^{k}
                \right)
            \right]
        +
        \sum_{j=1}^{N}
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
        \sum_{i=1}^{N}
            b_{i}
            \mathrm{E}
            \left[
                \left(
                    X^{i}
                    -
                    \mu^{i}
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
        (\forall k = 1, \ldots, N)
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{i=1}^{N}
            b_{i}
            \mathrm{E}
            \left[
                \left(
                    X^{i}
                    -
                    \mu^{i}
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
        (\forall k = 1, \ldots, N)
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
今$ \mathrm{Cov}(X)$の固有ベクトルは$$p_{1}, \ldots, p_{N}$$であったから、

$$
    \mathrm{Var}
    \left[
        p_{i}^{\mathrm{T}}X
    \right]
    =
    \lambda_{i}
$$

である。
この中で、最大のものは$\lambda_{1}$なので、命題が示された。

<div class="QED" style="text-align: right">$\Box$</div>

上記の命題より、$$ \mathrm{Var}(b^{\mathrm{T}}X)$$を最大にする$b$をみつけることでPCAを構成する方法もある。

## Reference

