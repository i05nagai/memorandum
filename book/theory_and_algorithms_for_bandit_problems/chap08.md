---
title: Theory and Algorithms for Bandit Problems
book_title: Theory and Algorithms for Bandit Problems
book_chapter: 8
---

# 8 連続腕バンディットとベイズ最適化
今までは、有限個のアーム$K \in \mathbb{N}$が行動（選択肢）であった。
一方、空間上の座標（漁獲の位置）や学習アルゴリズムのhyper parameter（SVMの正則化項の値など）を決める問題は、選択肢が非有限のバンディット問題として考えることができる。
選択肢が非有限のバンディット問題を連続腕バンディット問題という。

## 8.1 定式化と観測モデル
$\mathcal{A} \subset \mathbb{R}^{d}$を行動（選択肢）の集合で、 特に、$\mathcal{A}$は有界閉で、$a^{*} := \arg\max_{a \in \mathcal{A}}f(a)$は存在し一意とする。
連続腕バンディット問題では、時刻$t$での選択肢$a(t) \in \mathcal{A}$の報酬は以下で与えられる。

$$
    X(t; a(t)) := f(a(t)) + \epsilon(t)
$$

ここで、$\epsilon(t)$は期待値0の確率変数で、$f: \mathcal{A} \rightarrow [0, 1]$とする。
$epsilon(t)$が恒等的に0の場合を特に、雑音なしの連続腕バンディット問題といい、この場合$X(t)$は確率変数ではない。

$$
    X(t; a(t)) := f(a(t))
$$

以降では、$\epsilon(t)$は$t$について独立で$\mathcal{N}(0, \sigma^{2}$の正規分布に従うとする。
特に$\sigma = 0$のとき、$\epsilon(t)$は恒等的に0とする。

### 例8.1 交差確認によるhyper parameter最適化
TBD.

## 8.2 リグレットの設定
regretは以下で定義する。

$$
    \mathrm{Regret}(T; A) 
        := \sum_{s=1}^{T} (f(a^{*} - f(a(s)))
$$

この定義は今までのリグレットの定義の自然な拡張。

$$
\begin{eqnarray*}
    \mathrm{Regret}(T; A) 
        & = & \sum_{s=1}^{T} (f(a^{*}) - f(a(s)))
        \\
        & = & \sum_{s=1}^{T} (f(a^{*}) + \epsilon(t) - (f(a(s)) + \epsilon(t)))
        \\
        & = & \sum_{s=1}^{T} (X(s; a^{*}) - X(s; a(s)))
\end{eqnarray*}
$$


### Remark
この問題設定では期待リグレットとリグレットは一致する。

$$
\begin{eqnarray*}
    \mathrm{Regret}(T; A) 
        & = & 
            \mathrm{E}i
            \left[
                \sum_{s=1}^{T} (f(a^{*}) - f(a(s)))
            \right]
        & = & 
            \sum_{s=1}^{T} (f(a^{*}) - f(a(s)))
\end{eqnarray*}
$$


## 8.3 期待値関数のクラス
関数$f$に関する最適化を行うが、関数$f$に何らかの仮定がないと
よく利用される仮定としては、リプシッツ連続性とヘルダー連続性がある。


### 8.3.1 滑らかさの制約

#### def リプシッツ連続
$f: \mathcal{A} \rightarrow \mathbb{R}$について以下を満たす$c > 0$が存在するとき、 $f$はリプシッツ連続であるという。

$$
    | f(a) - f(b) | \le c \|a - b\|,
    \quad
    \forall a, b \in \mathcal{A}
$$

特に、ある$a^{\prime} \in \mathcal{A}$を定数とする。
このとき、以下を満たす$c > 0$が存在するとき、$f$ が $a^{\prime}$で局所的にリプシッツ連続という。

$$
    | f(a) - f(a^{\prime}) | \le c \|a - a^{\prime}\|,
    \quad
    \forall a \in \mathcal{A}
$$

#### Remark
リプシッツ連続性は、関数の傾きの絶対値が$c$を超えないということを述べている。


#### def ヘルダー連続
$\alpha > 0$を定数とする。
$f: \mathcal{A} \rightarrow \mathbb{R}$について以下を満たす$c > 0$が存在するとき、$f$は$\alpha$-ヘルダー連続という。

$$
    | f(a) - f(b) | \le c \|a - b\|^{\alpha},
    \quad
    \forall a, b \in \mathcal{A}
$$

特に、$a^{\prime} \in \mathcal{A}$を定数とする。
このとき、以下を満たす$c > 0$が存在するとき、$f$は$a^{\prime}$で局所的に$\alpha$-ヘルダー連続という。

$$
    | f(a) - f(a^{\prime}) | \le c \|a - a^{\prime}\|^{\alpha},
    \quad
    \forall a \in \mathcal{A}
$$

### 8.3.2 ベイズ最適化
関数$f$を$\mathcal{A}$上の確率過程としてベイズの枠組みで考える。

#### def ガウス過程
$\mathcal{A}$を添え字集合とする。
$(Y(a))\_{a \in \mathcal{A}}$を確率変数の族とする。
このとき、$\forall t \in \mathbb{N}$ について、$(Y(a_{1}), \ldots, Y(a_{t})$ が$t$次元正規分布に従うとき、 $(Y(a))_{a \in \mathcal{A}}$は、$\mathcal{A}$上のガウス過程であるという。

$Y(a_{t}$がガウス過程とする。




## 8.4 連続腕バンディットの方策
報酬$X_{i}$がGaussian Processに従う場合のバンディットのアルゴリズムについて述べる。

* GP-UCB方策
* トンプソン抽出
* 期待値改善量方策
* SOO方策

### 8.4.1 GP-UCB方策


### 8.4.2 トンプソン抽出

### 8.4.3 期待値改善量方策

### 8.4.4 多項式時間で実行可能な方策

## 8.5 共分散関数のパラメータ推定



