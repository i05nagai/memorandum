---
title: Decision Tree 
---

## Overview
決定木は、説明変数から2分木を作り目的変数を葉で分類する方法。
変数が2値でない場合は、アルゴリズムによっては$n$分木となる場合もある。

* Decision Tree Regression
* Decision Tree Classifier

## Good
* 真偽による分類なので変数の解釈がしやすい
* 分布などを仮定しない
* 外れ値の影響が低い

## Bad

## Algorithm
以下のアルゴリズムが知られている。
とりあえず、C4.5かCARTを使えば良い。
文献によって、アルゴリズムの定義がまちまちで、明確に書かれたものはない。

* ID3
* C4.5
* C5.0
* CART

### ID3
カテゴリを$$y_{1}, \ldots, y_{N} \in \{1, \ldots, K \} := A$$とする。
$$i \in \{1, \ldots, N \}$$番目のデータの$$j \in \{1, \ldots, d\}$$番目の変数を$$x_{i}^{j} \in \{1, \ldots, K_{j} \}$$と書く。
また、$i$番目のデータの変数を$$x_{i} := (x_{i}^{1}, \ldots, x_{i}^{d}) $$と定義しておく。

#### Step1
root nodeのデータの集合を以下で定義する。

$$
    C
    :=
    \{ (x_{1}, y_{1}), \ldots, (x_{N}, y_{N})\}
$$

と定義する。

#### Step2

$j$番目の変数が$$k \in \{1, \ldots, K_{j} \}$$の値となる集合を

$$
    C_{jk}
    :=
    \{ (x, y) = ((x^{1}, \ldots, x^{d}), y) \in C \mid x^{j} = k \}
$$

と定義する。

#### Step3
$C$の部分集合に対して、$C$の中でカテゴリ$$\bar{y} \in \{1, \ldots, K \}$$のデータの割合を以下で定義する。

$$
    \bar{C} \subseteq C,
    \quad
    \mathrm{dense}(\bar{C}, \bar{y})
    :=
    \frac{
        | \{(x, y) \in \bar{C} \mid y = \bar{y} \} |
    }{
        | \bar{C} |
    }
$$

集合$C$の平均情報量を以下で定義する

$$
    \bar{C} \subseteq C,
    \quad
    M(\bar{C})
    :=
    -\sum_{y \in A} \mathrm{dense}(\bar{C}, y) \log \mathrm{dense}(\bar{C}, y)
$$

#### Step4
$j$番目の変数の平均情報量の期待値$M_{i}$を以下の式で定義する。

$$
    \forall j = 1, \ldots, d,
    \quad
    M_{j}
    :=
    M(C)
    -
    \sum_{k=1}^{K_{j}}
    \left(
        M(C_{jk}) \times \frac{|C_{jk} |}{|C|}
    \right)
$$

期待値最大の変数を$x^{j^{*}}$とする。

$$
    j^{*} := \arg \max_{j} M_{j}
$$

#### Step5
nodeに、$$j^{*}$$番目の変数のラベルをつけ、nodeから$$K_{j^{*}}$$個に枝を分岐させ、各枝のnodeに対して$$C := C_{j^{*}k}$$としてStep2をから再帰的に行う。

### C4.5
カテゴリを$$y_{1}, \ldots, y_{N} \in \{1, \ldots, K \} := A$$とする。
$$i \in \{1, \ldots, N \}$$番目のデータの$$j \in \{1, \ldots, d\}$$番目の変数を$$x_{i}^{j} \in \{1, \ldots, K_{j} \}$$と書く。
また、$i$番目のデータの変数を$$x_{i} := (x_{i}^{1}, \ldots, x_{i}^{d}) $$と定義しておく。


### CART with regression
CARTでの回帰は、階段関数による関数の近似である。
各階段の定義域$R_{k}$が、クラス分類での微分クラスに対応している。
つまり、

$$
    f(x) := \sum_{i=1}^{K} c_{m} 1_{x \in R_{k}}
$$

とおき、分割データ$$D_{1}, \ldots, D_{K}$$分割領域$$R_{1}, \ldots, R_{K}$$と領域上での値$c_{1}, \ldots, c_{K}$をデータから決定する。

$$R := \mathbb{R}^{d}$$とおく。

$$
\begin{eqnarray}
    D_{1}(j, s)
    & := &
        \{
            (x, y) \in D \mid x^{j} \le s
        \},
    \nonumber
    \\
    D_{2}(j, s)
    & := &
        \{
            (x, y) \in D  \mid x^{j} \gt s
        \},
    \nonumber
    \\
    R_{1}(j, s)
    & := &
        \{
            x \in \mathbb{R}^{d} \mid x^{j} \le s
        \}
        \cap
        R,
    \nonumber
    \\
    R_{2}(j, s)
    & := &
        \{
            x \in \mathbb{R}^{d} \mid x^{j} \gt s
        \}
        \cap
        R,
\end{eqnarray}
$$

と定義する。
分割を決めた時の

$$
    \argmin_{j \in \{1, \ldots, d\}, s \in \mathbb{R}}
    \left(
        \min_{c_{1}}
            \sum_{(x, y) \in D_{1}(j, s)}
                (y - c_{1})^{2}
        +
        \min_{c_{2}}
            \sum_{(x, y) \in D_{2}(j, s)}
                (y - c_{2})^{2}
    \right)
$$

中の最小化は凸性と微分を計算すれば簡単に解けて、各領域に属するデータの平均値であることがわかる。

$$
    m = 1, 2,
    \quad
    c_{m}^{*}
    := 
    \frac{
        \sum_{(x, y) \in D_{1}(j, s)}
            y
    }{
        | D_{1}(j, s) |
    }
$$

よって、分割点と分割する変数を変えながら、分割領域に属するデータの平均を計算すれば良い。
変数が連続値の場合は、$N+1$通りのデータの分割方法しかないので、$s$は一意には定まらない。
$j$は変数の数なので、$O(dN^{2})$で計算できる。

最適な$$j^{*}, s^{*}$$が決まれば、$$R_{1} := R_{1}(j^{*}, s^{*}), R_{2} := R_{2}(j^{*}, s^{*})$$として、それぞれの領域に対して分割を繰り返す。


## Tips

### 変数が連続値の場合
変数が連続値の場合に、分割点の値をランダムに決めるという雑な方法もある。

