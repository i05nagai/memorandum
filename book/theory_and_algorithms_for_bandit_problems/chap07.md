---
layout: math
title: Theory and Algorithms for Bandit Problems
---

# Symbols
* $\mathbb{R}_{\geq 0}^{d}$
    * $d$次元の非負ベクトル

# Chapter 7. 線形モデル上のバンディット問題

## Symbols
* $i^{*} := \arg \max_{i} \theta^{\mathrm{T}} a_{i}$
* $a^{*} := \arg \max_{i} \theta^{\mathrm{T}} a_{i}$

## 7.1 線形バンディット

$$
    X_{i}(t) := \theta ^{\mathrm{T}} a_{i} + \epsilon(t) 
    \quad
    (\forall i = 1, \ldots, K)
$$

$a_{i} = (a_{i,1}, \ldots, a_{i,d})^{\mathrm{T}} \in \{0, 1}^{d}$で、$\theta = (\theta_{1}, \ldots, \theta_{d})^{\mathrm{T}} \in \mathbb{R}^{d}$、$\epsilon(t)$は$t$での誤差項で、期待値0のある確率分布に従うとする。

* $a_{i}$はスロットに対応するプレイヤーの選択肢で、特に行動(action)と呼ぶ
    * $a_{i}$は既知
* $\theta$は選択肢$a_{i}$を選んだときの報酬ないし、損失である
    * $\theta$は未知
* $X_{i}(t)$は行動$a_{i}$を選んだときの観測された報酬ないし、損失である

前章までのバンディット問題は

$$
    A := (a_{1}, \ldots, a_{d}) = 
       \left(
           \begin{array}{ccccc}
               a_{1,1}   & a_{2,1} & \cdots & a_{d-1,1}  & a_{d, 1} \\
               a_{1,2}   &         &        & \cdots     & \vdots \\
               \vdots    &         &        & \ddots     & a_{d, d-2} \\
               a_{1,d-1} & \vdots  & \ddots & \ddots     & a_{d, d-1} \\
               a_{1,d}   & \cdots  &        & a_{d-1, d} & a_{d, d}
           \end{array}
       \right)
$$

が単位行列の場合に相当する。
問題設定としては、指定された組み合わせについてはスロットを同時に引けるとした場合の報酬最大化を目指す問題となる。

$$
    \mathrm{regret}(T)
        := \sum_{t=1}^{T} (\theta^{\mathrm{T}}a_{i^{*}} - \theta^{\mathrm{T}}a_{i(t)})
        = \sum_{t=1}^{T} \theta^{\mathrm{T}}(a_{i^{*}} - a_{i(t)})
$$

### 例7.1 ウェブサイト最適化
* $a_{1} \in \\{0, 1\\}$: fontsizeが小なら0, 大なら1
* $a_{2} \in \\{0, 1\\}$: fontがgothicなら0, popなら1
* $a_{3} \in \\{0, 1\\}$: 検索窓の位置が左なら0, 右なら1
* $a_{4} \in \\{0, 1\\}$: 背景の色が緑なら0, 白なら1
* $\theta \in \mathbb{R}^{4}$は、選択肢

とする。
線形バンディットは、$a_{1}$の値にかかわらず$a_{2}$の報酬$\theta_{2}$は一定である。
つまり、デザインの組み合わせはモデルとして考慮されない。

全てのパターンを選択肢とすると$a = (a_{1}, \ldots, a_{4}) \in \\{0, 1\\}^{4}$で16通りとなる。
この場合は、組み合わせは考慮をできる。


### 例7.2 バンディット最適予算配分
* $B$円の広告予算
* $d$個のメディア（テレビ or 雑誌 or etc.)
* 制約として以下のようなものを考える
    * $d$個のメディアへの広告費の配分を$a_{i} (i = 1,\ldots, d)$
        * $a_{i} \in \mathbb{R}\_{\ge 0}^{d}$ かつ $a_{i,1} + \cdots + a_{i,d} \leq B$
    * メディア$i$への予算の配分額が決まっている
* $\theta$は広告費の投資額に対する売上への寄与
* $X_{i}(t)$は売上

$$
    
$$

### 補足7.1 誤差項の分布
* $\epsilon(t)$は正規分布でなくとも良い。
* 例7.1ではクリックの有無なので、誤差はX
* $\epsilon(t)$ には劣ガウス性(sub-Gaussian)を仮定することが多い


### def 劣ガウス
平均0の確率変数$Z$が$R$-劣ガウス的であるとは、$Z$の積率母関数$M_{Z}(\lambda):=\mathrm{E}[e^{\lambda Z}]$が平均0, 分散$R^{2}$の正規分布の積率母関数で上から抑えられること
平均0,分散$R^{2}$の正規分布の積率母関数を$M_{X}(\lambda) := \exp(\frac{\lambda^{2}R^{2}}{2}$とすると

$$
    M_{Z}(\lambda) \leq M_{X}(\lambda),
    \quad
    \forall \lambda \in \mathbb{R}
$$

### Remark
平均0の確率変数$Z$が確率1で$[-R, R]$上有界であれば、$R$-劣ガウス的である。


## 7.2 文脈つきバンディット
$a_{i,t}$と行動が時間$t$に依存するものを文脈付きバンディットと呼ぶ。
つまり、時刻$t$の行動$i$の報酬が

$$
    X_{i}(t) := \theta^{\mathrm{T}}a_{i,t}
$$

である。

### 例
$a_{i, t} = (a_{1}, \ldots, a_{4}, b_{t}$

## 7.3 LinUCB方策

$$
    A := \frac{\sigma^{2}}{\sigma_{0}^{2}} I_{d}
        + \sum_{s=1}^{t} a_{i(s), s}a_{i(s), s}^{\mathrm{T}}
$$

$$
\begin{eqnarray*}
    \hat{\theta}
        & := & \arg\min_{\theta^{\prime}}
            \sum_{s=1}^{t} (X(s) - (\theta^{\prime})^{\mathrm{T}}a_{i(s), s})^{2}
        \\
        & = & 
            \left(
                \sum_{s=1}^{t} a_{i(s), s} a_{i(s), s}^{\mathrm{T}}
            \right)^{-1}
            \sum_{s=1}^{t} a_{i(s),s} X(s)
        \\
        & = & 
           \tilde{A}_{t}^{-1} b_{t}
\end{eqnarray*}
$$

### Algorithm 7.1

1. $A^{-1} \leftarrow \frac{\sigma_{0}^{2}}{\sigma^{2}} I_{d}$, $b_{t} \leftarrow 0$.
2. for $t=1, 2, \ldots, T$ do
3. 　　$\hat{\theta} \leftarrow A^{-1}b$
4. 　　$i = 1, \ldots, d$について$\alpha_{t} := \alpha \sqrt{\ln t}$として以下を計算
$$
    \bar{\mu}_{i}(t)
        = a_{i, t}^{\mathrm{T}} \hat{\theta} 
            + \alpha_{t} \sigma \sqrt{a_{i, t}^{\mathrm{T}}A^{-1}a_{i, t}}
$$
5. 　　スコア最大の行動$i \leftarrow \arg\min_{i} \bar{\mu}(t)$を選択して、報酬$X(t) := X_{i}(t)$を得る
6. 　　逆行列を更新
$$
    A^{-1} 
        \leftarrow
        A^{-1} 
        - \frac{
            A^{-1}a_{i, t}a_{i,t}^{\mathrm{T}}A^{-1}
        }{
            1 + a_{i, t}^{\mathrm{T}} A^{-1}a_{i,t}
        },
    \quad
    b \leftarrow b + a_{i, t} X(t).
$$
7. endfor.

## 7.4 線形モデル上のトンプソン抽出

## 7.5 ロジスティック回帰モデル上のバンディット



## Appendix A 逆行列の更新
Sherman-Morrison-WOodbury formula or Woodbury formula

### 定理 A.1 ウッドベリーの公式
* $A$: $d \times d$行列
* $B$: $d \times e$行列
* $C$: $e \times e$行列

このとき、

$$
    (A + BCB^{\mathrm{T}})^{-1}
        = A^{-1} - A^{-1}B(C^{-1} + B^{\mathrm{T}} A^{-1}B)^{-1}B^{\mathrm{T}}A^{-1}.
$$

特に、$d$次元ベクトル$b$に対して

$$
    (A + bb^{\mathrm{T}})
        = A^{-1} 
        - \frac{
            A^{-1}bb^{\mathrm{T}} A^{-1}
        }{
            1 + b^{\mathrm{T}} A^{-1} b
        }.
$$

### Proof.

### lemma A.2 ブロック行列の逆行列
* $A$: $d \times d$行列
* $B$: $d \times e$行列
* $C$: $e \times e$行列

このとき、

$$
    \left(
        \begin{array}{cc}
            A              & B \\
            B^{\mathrm{T}} & C
        \end{array}
    \right)^{-1}
    = \left(
        \begin{array}{cc}
            A^{-1} + A^{-1}BS^{-1}B^{\mathrm{T}}A^{-1} & -A^{-1}BS^{-1} \\
            -S^{-1}B^{\mathrm{T}}A^{-1}                & S^{-1}
        \end{array}
    \right)
$$

ただし、$S$はshur-coplementであり、$S := C - B^{\mathrm{T}}A^{-1}B$である。
特に$d$次元ベクトル$b$に対して$s := c - b^{\mathrm{T}}A^{-1}b$とすると

$$
    \left(
        \begin{array}{cc}
            A              & b \\
            b^{\mathrm{T}} & C
        \end{array}
    \right)^{-1}
    = \frac{1}{s}
    \left(
        \begin{array}{cc}
            sA^{-1} + A^{-1}BB^{\mathrm{T}}A^{-1} & -A^{-1}B \\
            -B^{\mathrm{T}}A^{-1}                 & 1
        \end{array}
    \right).
$$


### proof

