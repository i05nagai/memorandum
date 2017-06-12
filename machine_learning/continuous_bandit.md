---
title: Continuous Bandit
---

## Continuous Bandit
Banditで考える問題は、次の問題である。
以下を決める。

* $T \in \mathbb{N}$
    * 終了時刻
    * 離散である場合が多い
    * infinite time horizonの場合もある
* $A$
    * 考えている選択肢の全体
    * actionとも言う
    * continuos banditの場合は、$A$は非可算無限
    * discrete banditの場合は、$A$は高々可算
* $$X_{a}$$,
    * $a \in A, t = 1, \ldots, T $
    * 時刻$t$で選択肢$a$をとったときの報酬
    * 確率的であれば、確率的bandit問題
    * $t$に依存する$$X_{a, t}$$の場合は、time inhomogeneous bandit問題になる
        * まともに解けない

以上を設定した後、以下の状況を考える。

* Step1. $t = 1$
* Step2. $t$での選択肢$$a_{t}$$を一つ選ぶ
    * $s < t$までの選択肢$$a_{s}$$と報酬$$X_{a_{s}}$$に依存して決めて良い
* Step3. $t$での選択肢に対する報酬$$X_{t}$$が明らかになる
* Step4. $t = T$であれば終了
* Step5. $t < T$であれば、$t = t + 1$として、Step2へ

上記の下、以下の2つのいずれかを達成する選択$$a_{1}, \ldots, a_{T}$$を決定するのがBandit問題である。

1. 報酬の和$$\sum_{t=1}^{T} X_{a_{t}}$$を最大にする
2. 最も良い報酬を返す選択肢$$a^{*} := \argmax_{a} \mathbb{E}[X_{a}]$$を見つける
    * A,Bテストは選択肢が$A = {1, 2}$の場合である

bandit問題で重要なのは、$$X_{a}$$が$t$で未知であるため、良い報酬に関する情報の探索と良い報酬の獲得をバランスする必要があるということである。
この意味で、 問題1は、報酬についての情報の探索と報酬の獲得の両方を行う。
一方、問題2は、報酬の獲得は不要で、探索のみを行う問題である。

continuous banditの具体的な例として、モデルのパラメータの決定問題を考える。
モデルのパラメータ決定問題は、上記の問題2の場合となる。

* $d$
    * パラメータの数
* $$A \subset \mathbb{R}^{d}$$,
    * パラメータの次元
* $T \in \mathbb{N}$
    * パラメータを変更する回数
* $L(a; x, y)$
    * paramterを$a$としたとき、訓練データ群$x$と対応する訓練データの答え群$y$の損失
* $$X_{a} := -L(a; x, y)$$,
    * parameterを$a$としたときのmodelの予測誤差


## Definitions
* $$(\Omega, \mathcal{F}, P)$$,
    * probability space
* $A \subset \mathbb{R}^{d}$
* $$X: A \times \Omega \rightarrow \mathbb{R}$$,
    * $$X_{a}(\omega) := X(a, \omega)$$,
    * 確率変数の族
    * $d=1$ならば、確率過程として考えるのが一般的

### Definition. (Gaussian Process)
$A$を添え字集合とする。
$(X_{a})\_{a \in A}$を確率変数の族とする。
このとき、$\forall t \in \mathbb{N}$ について、$$(X_{a_{1}}, \ldots, X_{a_{t}})$$ が$t$次元正規分布に従うとき、 $(X_{a})_{a \in A}$は、$A$上のガウス過程であるという。

<div class="end-of-statement" style="text-align: right">■</div>

## GP-UCB (Gaussian Process Upper Confidence Bound)
$(X_{a})$がガウス過程に従うとする。
特に、平均$\mathrm{E}(X_{a})$と分散$\mathrm{Var}(X_{a})$が$a$の関数で以下のようにかけると仮定する。
つまり、$\forall t \in \mathbb{N}$について、$$\mathbf{a}_{t} := (\tilde{a}_{1}, \ldots, \tilde{a}_{t}) \in A^{t}$$とすると

$$
    (X_{\tilde{a}_{1}}, \ldots, X_{\tilde{a}_{t}})
        \sim \mathcal{N}^{t}(\mu_{t}(\mathbf{a}_{t}), \sigma_{t}(\mathbf{a}_{t}, \mathbf{a}_{t})),
$$

ここで、$\mu_{t}(a)$は平均を表す関数で$\mu_{t}:A^{t} \rightarrow \mathbb{R}^{t}$、$\sigma_{t}(\cdot, \cdot)$は共分散を表す関数$\sigma:A \times A \rightarrow \mathbb{R}_{\ge 0}$で、特に以下のようにかけるとする。

$$
\begin{eqnarray}
    \mu_{t}(\mathbf{a}_{t})
        & := &
        \left(
            \begin{array}{c}
                \mu_{t}^{1}(a_{1}) \\
                \mu_{t}^{2}(a_{2}) \\
                \vdots \\
                \mu_{t}^{t}(a_{t}) 
            \end{array}
        \right),
    \\
    \sigma_{t}(\mathbf{a}_{t}, \mathbf{a}_{t})
    & := &
        \left(
            \begin{array}{cccc}
                k(a_{1}, a_{1}) & k(a_{1}, a_{2}) & \ldots & k(a_{1}, a_{t})
                \\
                k(a_{2}, a_{1}) & k(a_{2}, a_{2}) & \ldots & k(a_{2}, a_{t})
                \\
                \vdots &  & \ddots & \vdots
                \\
                k(a_{t}, a_{1}) & k(a_{t}, a_{2}) & \ldots & k(a_{t}, a_{t})
            \end{array}
        \right)
    \nonumber
    \\
    \sigma_{t}(\mathbf{a}_{t-1}, a_{t})
    & := &
        \left(
            \begin{array}{c}
                k(a_{1}, a_{t})
                \\
                k(a_{2}, a_{t})
                \\
                \vdots
                \\
                k(a_{t-1}, a_{t})
            \end{array}
        \right)
    \nonumber
    \\
    \sigma_{t}(a_{t}, \mathbf{a}_{t-1})
    & := &
        \left(
            \begin{array}{cccc}
                k(a_{t}, a_{1})
                    &
                        k(a_{t}, a_{2})
                    &
                        \cdots
                    &
                        k(a_{t}, a_{t-1})
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

ここで、$k:A \times A \rightarrow \mathbb{R}$の関数である。
$k$として、kernel関数を取ることが多い。
kernel関数を考える主な理由は、共分散行列の半正定値性がkernel関数の半正定値性によって保証されるからである。
この仮定の下、$a_{1}, \ldots, a_{t}$までの選択肢の報酬$$X_{a_{1}}, \ldots, X_{a_{t}}$$が与えられた下での$X_{a_{t+1}}$の条件付き分布が分かる。
GP-UCBでは、$$X_{a_{1}}, \ldots, X_{a_{t}}$$の下での$$X_{a_{t+1}}$$条件付き分布より、平均の信頼区間を求め、信頼区間を最大にするような選択肢を選ぶ。

具体的に、見てみよう。
記法の簡潔にする為に、

* $$\mathbf{X}_{t} := (X_{a_{1}}, \ldots, X_{a_{t}})$$,
    * $t$までの報酬
* $$\mathbf{x}_{t} := (X_{a_{1}}(\omega), \ldots, X_{a_{t}}(\omega))$$,
    * 観測された$t$までの報酬
    * 選択肢による報酬の実現値

とかく。
多変量正規分布の性質と平均と分散に対する仮定から、$$\mathbf{X}_{t}$$の下での$$X_{a_{t+1}}$$の条件付き確率$$p_{X_{a_{t+1}} \mid \mathbf{X}_{t}}$$が次のようにかけるということがわかる。

$$
\begin{eqnarray}
    \mu_{t + 1}(\mathbf{a}_{t + 1})
    & = &
        \left(
            \begin{array}{c}
                \mu_{t}(\mathbf{a}_{t})
                \\
                \mu_{t+1}^{t+1}(a_{t + 1})
            \end{array}
        \right)
    \\
    \sigma_{t + 1}(\mathbf{a}_{t + 1}, \mathbf{a}_{t + 1})
    & = &
        \left(
            \begin{array}{cc}
                \sigma_{t}(\mathbf{a}_{t}, \mathbf{a}_{t})
                    &
                        \sigma_{t}(\mathbf{a}_{t}, a_{t + 1})
                \\
                \sigma_{t}(a_{t+1}, \mathbf{a}_{t})
                    &
                        k(a_{t+1}, a_{t + 1})
            \end{array}
        \right)
    \\
    p_{X_{a_{t+1}} \mid \mathbf{X}_{t}}(y_{t+1} \mid \mathbf{x}_{t})
    & = &
            \phi(a_{t+1}; \mu(y_{t+1}; \mathbf{x}_{t}), \sigma(y_{t+1}, y_{t+1}; \mathbf{x}_{t}))
    \\
    \mu(y; \mathbf{x}_{t})
    & := &
        \mu_{t+1}^{t+1}(a_{t+1})
        +
        \sigma_{t}(a_{t+1}, \mathbf{a}_{t})
            \sigma_{t}(\mathbf{a}_{t}, \mathbf{a}_{t})^{-1}
            (\mathbf{x}_{t} - \mu_{t}(\mathbf{a}_{t}))
    \\
    \sigma(y, y; \mathbf{x}_{t})
    & := &
        k(a_{t+1}, a_{t+1}) - k^{\mathrm{T}}K^{-1}k
        -
        \sigma_{t}(a_{t+1}, \mathbf{a}_{t})
            \sigma_{t}(\mathbf{a}_{t}, \mathbf{a}_{t})^{-1}
            \sigma_{t}(\mathbf{a}_{t}, a_{t+1})
\end{eqnarray}
$$

ここで$\phi(\cdot; \mu, \sigma)$は平均$\mu$分散$\sigma$の1次元の正規分布の密度関数である。
正規分布の信頼区間は平均と分散で決まるから、この条件付き確率の信頼区間は$\alpha_{t}$をパラメータとして、

$$
\begin{equation}
    \mu_{\mathrm{UCB}}(y; \mathbf{x}_{t})
    :=
    \mu(y; \mathbf{x}_{t})
    +
    \alpha_{t}
    \sigma(y, y; \mathbf{x}_{t})
\end{equation}
$$

とかける。
これをUCB scoreと呼び、これを最大にする$$x_{t+1} := \argmax_{y \in A}\mu_{\mathrm{UCB}}(y; \mathbf{x}_{t})$$を次の選択肢とするのが、GP-UCBとなる。

GP-UCBで決めるパラメータは

* ガウス過程の有限次元分布
    * 平均の関数$\mu_{t}\ (\forall t)$
    * 分散の関数$\sigma_{t}\ (\forall t)$
* UCBのパラメータ$\alpha_{t}\ (\forall t)$

である。

### Thompson Sampling
Thompson Samplingでは、Bayesっぽく真の期待値を確率変数だと思って、真の期待値の条件付き確率を求める。
そのため、$A$から適当に点を取ってきて、
その条件付き確率に基いて、乱数を生成し、$k$個の

1. 条件付き確率
2. 


### Example of GC UCB
* $A \subset \mathbb{R}^{p}$
    * パラメータの空間
* $$(X_{a})_{a \in A}$$,
    * パラメータ$a$に対応するモデルの損失関数の値


