---
title: Expectation Maximization Algorithm
---

## EM algorithm
観測可能な変数以外にモデルを制御する確率変数（潜在変数と呼ばれる）がある場合に、行う最尤法のようなもの。

最尤法では、観測値の確率が最も大きくなるように尤度関数を最大化する。
潜在変数$Z$がある場合は尤度関数の最大化をしても$Z$の$\theta$は$Z$についてrandomなままである。
尤度関数を最大化する前に、潜在変数について（条件付き）期待値を取り、その期待値をパラメータ$\theta$について最大化するのが、EM algorithmである。

潜在変数を考える理由は、例えば株価の予測をする際に市場で観測できる指標以外に、世界情勢や政策などの必ずしも観測可能でない変数の影響を受けて株価が変化するといったモデルを考える場合に有用となる。

## Definition
* $N$
    * データの数
* $d$
    * 変数の数
* $X$
    * 観測できる変数の真の確率変数
    * $\mathbb{R}^{d}$値の確率変数
* $$X_{1}, \ldots, X_{N}$$
    * $\mathbb{R}^{d}$値の確率変数
    * $X$に対して独立同分布
* $$\bar{X}_{N} := (X_{1}, \ldots, X_{N})$$
    * 記法を簡潔するために、観測値全体を上のようにかく
* $x_{k} := X_{1}(\omega)$
    * 確率変数の観測値
* $$\bar{x}_{N} := (x_{1}, \ldots, x_{N})$$
    * 記法を簡潔するために、観測値全体を上のようにかく
* $\theta \in \mathbb{R}^{d}$
    * モデルのパラメータを表す変数
* $$Z_{1}, \ldots, Z_{N}$$
    * 観測されない潜在変数
* $$\bar{Z}_{N} := (Z_{1}, \ldots, Z_{N})$$
    * 記法を簡潔するために、実現値全体を上のようにかく
* $z_{i} := Z_{i}(\omega) \quad (\forall i = 1, \ldots, N)$
    * 潜在変数の実現値
* $$\bar{z}_{N} := (z_{1}, \ldots, z_{N})$$
    * 記法を簡潔するために、実現値全体を上のようにかく

## Algorithm
対数尤度関数を以下で定義し、

$$
    L(\bar{x}_{N}, \bar{z}_{N}; \theta)
    :=
    \ln p_{\bar{X}_{N}, \bar{Z}_{N}}(\bar{x}_{N}, \bar{z}_{N}; \theta)
$$

$$\bar{x}_{N}$$と$$x_{1}, \ldots x_{N}$$などを記法の簡潔さの為区別せず用いる。
以下の反復法で、$\theta^{k}$を更新して行く方法をEM algorithmという。

### Step1
$\theta^{0}$を適当にきめ、$k=0$とする。

### Step2 (Expectation)
$Q^{k}$を以下のように決める。

$$
    Q^{k}(\theta)
    :=
    \int
        p_{Z_{1}, \ldots, Z_{N} \mid \bar{X}_{N}}(z_{1}, \ldots, z_{N} \mid \bar{x}_{N}; \theta^{k})
        L(\bar{x}_{N}, z_{1}, \ldots, z_{N}; \theta)
    \ dz_{1} \cdots dz_{N}
$$

対数尤度関数について、潜在変数$Z$の（条件付き）期待値をとって、$Z$のrandomnessを取り除いている。

### Step3 (Maximization)
尤度関数最大化と同じく、$Z$に対して期待値を取ったおのに対して最大化を行う。

$$
    \theta^{k+1}
    :=
    \argmax_{\theta} Q^{k}(\theta)
$$

$\theta^{k}$が収束していないければ、$k \leftarrow k + 1$としてStep2へ戻る。
