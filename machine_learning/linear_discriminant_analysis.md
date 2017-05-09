---
title: Linear Discriminant Analysis
---

## Linear Discriminant Analysis
PCA同様後で整理が必要。

* $$C$$,
    * 取りうるクラス全体
    * 教師あり学習の場合は教師の取りうる値の集合が必要なので定義する必要がある
    * 有限を仮定
* $$N_{c}$$,
    * クラス$c \in C$に属する実現値の数
* $N$
    * 実現値全体の数
    * $$N = \sum_{c \in C} N_{c}$$,
* $$X_{c}$$,
    * クラス$c \in C$の真の分布
* $$X_{c, i} = (X_{c, i}^{1}, \ldots, X_{c, i}^{d})^{\mathrm{T}}$$,
    * $c \in C$のクラスに属する$i$番目の$d$次元のデータ
    * $X_{c}$のi.i.d.
* $$x_{c, 1}, \ldots, x_{c, N_{c}}$$,
    * $$x_{c, i} := X_{c, i}(\omega)$$,
    * $X_{c, i}$の実現値
    * $d$次元

実現値がクラス$c$に属する確率変数の平均

$$
\begin{eqnarray}
    \mu_{c}
    :=
    \mathrm{E}
    \left[
        X_{c}
    \right]
\end{eqnarray}
$$

クラス$c$に属する実現値の平均と実現値全体の平均

$$
\begin{eqnarray}
   \mu
    & := & 
        \frac{
            1
        }{
            | C |
        }
        \sum_{c \in C}
            X_{c},
\end{eqnarray}
$$

クラス$c$の確率変数の共分散行列

$$
\begin{eqnarray}
    A_{c}
    & := &
        \mathrm{Cov}
        \left[
            X_{c}
        \right]
    \nonumber
\end{eqnarray}
$$

全体に対する

$$
\begin{eqnarray}
    S_{B}
    :=
    \sum_{c \in C}
        (\mu_{c} - \mu)
        (\mu_{c} - \mu)^{\mathrm{T}}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{Var}
    \left[
        b^{\mathrm{T}}X_{c}
    \right]
    & = &
        b^{\mathrm{T}}
        \mathrm{Cov}
        \left[
            X_{c}
        \right]
        b
\end{eqnarray}
$$

PCAと同じ議論。

## algorithm
アルゴリズム的には以下の通り。

$$
\begin{eqnarray}
    S_{B}
    & := &
        \sum_{c \in C}
            (\mu_{c} - \mu)
            (\mu_{c} - \mu)^{\mathrm{T}}
    \nonumber
    \\
    S_{W}
    & := &
        \sum_{c \in C}^{i \in I_{c}}
         (x_{c, i} - \mu_{c})
         (x_{c, i} - \mu_{c})^{\mathrm{T}}
\end{eqnarray}
$$

とおく。
$$S_{B}$$はクラスの平均がデータ全体の平均からどれくらい離れているかを表している。
$$S_{W}$$は各クラスの平均が実現値からどのくらい離れているかを表している。
以下の最適化を解く。

$$
\begin{align}
    \max_{w}
    & & &
        \frac{ 1 }{ 2 }
        w^{\mathrm{T}}S_{B}w
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        w^{\mathrm{T}}S_{W}w = 1
    \nonumber
\end{align}
$$

$i$番目は

$$
\begin{align}
    \max_{w}
    & & &
        \frac{ 1 }{ 2 }
        w^{\mathrm{T}}S_{B}w
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        w^{\mathrm{T}}S_{W}w = 1,
        \\
    & & &
        w^{\mathrm{T}}w_{j} = 1, \forall j = 1, \ldots, i -1
    \nonumber
\end{align}
$$

解き方は、PCA同様に、Lagrange乗数法により、一次の最適性条件を考えると、 $$ S_{W}^{\mathrm{T}}S_{B} $$の固有ベクトルを求める問題に帰着する。

$$w_{1}, \ldots, w_{d}$$を列ベクトルとする行列を$W$とすれば、

$$
    X^{\prime}
    :=
    XW
$$

と変換すれば良い。

## Reference
