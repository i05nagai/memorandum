---
title: Chapter3. Uniformly Most Powerful Tests
book_title: Testing Statistical Hypotheses
book_chapter: 3
---

## 3.1 Stating The Problem
3章は仮説検定の話。
ここでは、仮説を採択するか棄却するかの2-side decision prolblemを扱う。
このような決定問題を 仮説のtest（検定） という。

* $X$
* $$\mathcal{P} := \{P_{\theta} \mid \theta \in \Theta\}$$,
* $H, K \subset \mathcal{P}$
    * $\mathcal{P}$の分割
    * $$H \cup K = \mathcal{P}$$,
    * $K$はalternativesクラスとも言われる
* $$\Theta_{H}, \Theta_{K}$$,
    * $H, K$に対応するパラメータの分割
    * $$\Theta_{H} \cup \Theta_{K} = \Theta$$,
* $$d_{0}, d_{1}$$,
    * $$d_{0}$$は、仮説を採択するという決定
    * $$d_{1}$$は、仮説を棄却するという決定
* $$S_{0}, S_{1}$$,
    * $X$の値域の分割
    * $$S_{0}$$の時採択となるようにとる
    * $$S_{1}$$の時棄却となるようにとる
    * $$S_{1}$$はcritical regionともいわれる。
    * $$S_{i} := \{X(\omega) \mid \omega \in \Omega,\ \delta(X(\omega)) = d_{i} \}$$,

検定の2つのえらー。

1. 仮説が正しいのに、棄却する
    * Error of the first kind
    * True Negativeとも
2. 仮説が間違っているのに、採択する
    * Error of the second kind
    * False Positiveとも


病気の有無の検定を考える。
病気であるという仮説をたてる。

1. 病気であるのに、病気でないという 
    * 病気の場合は治療が必要なので、命に関わる病気であれば、このミスは減らす必要がある
2. 病気でないのに、病気であるという 
    * 病気の場合は治療が必要なので、このミスが増えると、無駄な治療費がかかる

どちらを減らすかは、問題によって考える必要がある。
一般にどちらのミスを減らすような両立はできないことが知られている。

そのため、間違って仮説$H$を棄却する確率$\alpha \in [0, 1]$を使って、以下のような条件をつける。

$$
\begin{equation}
    P_{\theta}(\delta(X) = d_{1})
    =
    P_{\theta}(X \in S_{1})
    \le
    \alpha
    \quad
    \theta \in \Theta_{H}
    \label{chap03_3_1_level_of_significance}
\end{equation}
$$

仮説が正しい（つまり、parameterが$\theta \in \Theta{H}$)の時の、棄却するという決定$d_{1}$を取る確率が$\alpha$以下であるとする。
この条件のもと、仮説が間違っている（つまり、parameterが$\theta \in \Theta_{K}$)ときの、採択する確率を最小にするようにする。
つまり、以下の最適化問題を解く。

$$
\begin{align}
    \min_{\theta \in \Theta_{K}}
    & & &
        P_{\theta}(\delta(X) = d_{0})
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        P_{\theta}(\delta(X) = d_{1})
        \le
        \alpha
        \quad
        \theta \in \Theta_{H}
    \nonumber
\end{align}
$$

これは、以下と同値である。

$$
\begin{align}
    \min_{\theta \in \Theta_{K}}
    & & &
        P_{\theta}(X = S_{0})
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        P_{\theta}(X = S_{1})
        \le
        \alpha
        \quad
        \theta \in \Theta_{H}
    \nonumber
\end{align}
$$

* 目的関数は、Error of the second kindの最小化
* 制約は、Error of the first kindの確率が$\alpha$以下となる。

多くの場合、目的関数の最小化によって、制約は等号で達成されることが期待される。
つまり、

$$
\begin{equation}
    \sup_{\theta \in \Theta_{H}} P_{\theta}(X \in S_{1})
    =
    \alpha
    \label{chap03_3_3_size}
\end{equation}
$$

$$\eqref{chap03_3_3_size}$$の左辺は、size of the testと呼ばれるものである。
また、Error of the second kindに当たる、以下の式をpower of the testという。

$$
\begin{equation}
    P_{\theta}(\delta(X) = d_{1})
    =
    P_{\theta}(X \in S_{1})
    \label{chap03_3_2_power}
\end{equation}
$$

また、Error of the second kindを$\Theta$全体で定義された関数とみなした$\beta: \Theta \rightarrow [0, 1]$をpower function of the testという。

$$
    \theta \in \Theta,
    \
    \beta(\theta)
    :=
    P_{\theta}(\delta(X) = d_{1})
$$

* $\alpha$はError of the first kindの上限
* Error of the second kindは最小化

Error of the first kindの値については問題ごとに設定するしかない。
$\alpha$の値は0.05や0.01が使われることが多い。

level of siginifanceは小さい値をとることが多いが、本来であればpower of the testを考慮して決めるべきものである。

理想的には、significance levelとpowerの両方に対して適当な値をえらうためには、sample sizeは十分大きく取る必要があることが知られている。
Cohen(1962), Freiman et al. (1978)など。
powerと両立した$\alpha$の選び方については、Lehmann (1958), Arrow(1960), Sanathanan (1974)などがある。
また、Bayesianの観点から Savage(1962 pp 62-66)、Rosenthal and Rubin (1958)などがある。

また、significance levelを決める別の指針は、仮定に対する確信度である。
仮定が成り立つとかんがえられる時は、十分significance levelを小さくする。

次に、randomized testについて述べる。
* $0 \le \phi(x) \le 1$をcritical functionという

* $X$
* $P_{\theta}$

randomized testのrejectionの確率は

$$
    \beta_{\phi}(\theta)
    :=
    E_{\theta}
    \left[
        \phi(X)
    \right]
    =
    \int
        \phi(x)
    \ d P_{\theta}(x)
$$

で定義する。
また、powerは

$$
    \forall \theta \in \Theta_{K},
    \
    \beta_{\phi}(\theta)
$$

で定義する。
$\phi$は、Error of the first kindとError of the second kindを減らすように選ぶべきである。
よって、

$$
\begin{equation}
    \theta \in \Theta_{K},
    \
    \beta_{\theta}(\phi)
    \label{chap03_3_4}
\end{equation}
$$

の最大化を

$$
\begin{equation}
    \theta \in \Theta_{H},
    \
    \mathrm{E}_{\theta}(\phi(X))
    \le
    \alpha,
    \label{chap03_3_5}
\end{equation}
$$

の下に行いたい。
もし、$$\Theta_{K} := \{\theta_{K}\}$$が1点集合であれば、適当な$\phi$のクラス$A$から

$$
\begin{align}
    \max_{\phi \in A}
    & & &
        \beta_{\phi}(\theta_{K})
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \mathrm{E}_{\theta}(\phi(X))
        \le
        \alpha,
        \
        \forall \theta \in \Theta_{H}
    \nonumber
\end{align}
$$

を解けば良い。
一般に$\Theta_{K}$が1点でない場合は、Uniformly most powerful (UMP) testというクラスが重要となる。
これについては、Section 3.4, Section 3.7で議論する。

検定の場合は、次の2つのloss function$$L_{1},L_{2}$$を考えることができる。

$$
\begin{eqnarray}
    L_{1}(\theta, d_{1})
    & := &
        \begin{cases}	
            1 & \theta \in \Theta_{H} \\
            0 & \theta \in \Theta_{K} 
        \end{cases}
    \nonumber
    \\
    L_{1}(\theta, d_{0})
    & := &
        0
        \
        \forall \theta
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    L_{2}(\theta, d_{0})
    & := &
        \begin{cases}	
            0 & \theta \in \Theta_{H} \\
            1 & \theta \in \Theta_{K} 
        \end{cases}
    \nonumber
    \\
    L_{2}(\theta, d_{1})
    & := &
        0
        \
        \forall \theta
    \nonumber
\end{eqnarray}
$$

### Remark
以下が成り立つ。

$$
    \arg\inf_{\theta \in \Theta_{K}}
        P(X \in S_{0})
    =
    \arg\sup_{\theta \in \Theta_{K}}
        P(X \in S_{1})
$$

実際

$$
\begin{eqnarray}
    \inf_{\theta \in \Theta_{K}} P_{\theta}(X \in S_{0})
    & = &
        \inf_{\theta \in \Theta_{K}}
            (P_{\theta}(X \in (S_{0} \cup S_{1})) - P_{\theta}(X \in S_{1}))
    \nonumber
    \\
    & = &
        1
        +
        \inf_{\theta \in \Theta_{K}}-P_{\theta}(X \in S_{1})
    \nonumber
    \\
    & = &
        1
        -
        \sup_{\theta \in \Theta_{K}}P_{\theta}(X \in S_{1})
    \nonumber
\end{eqnarray}
$$

<div style="text-align: right">■</div>

## 3.2 THe Neyman-Pearson Fundamental Lemma
分布の族が、simpleとは族がただ1つからなる場合を指す。
そうでない場合をcompositeと呼ぶ。

$H, K$がsimpleの場合を考える。
対応する分布をそれぞれ、$$P_{0}, P_{1}$$とする。
$X$は離散値とする。
Criticial Reagionが$S$とすると、$$P(X \in S) = \sum_{x \in S}P(X = x)$$より、 最適化問題は以下のようにかける。

$$
\begin{align}
    \min
    & & &
        \sum_{x \notin S}
            P_{1}(X = x)
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \sum_{x \in S}
            P_{0}(X = x)
        \le
        \alpha,
        \label{chap03_3_6}
\end{align}
$$

$$
    r(x)
    :=
    \frac{
        P_{0}(X = x)
    }{
        P_{1}(X = x)
    }
$$

$$
    P_{0}(X \in S)
    =
    \sum_{x:r(x) > c}
        P(X = x)
    = \alpha
$$

### Theorem 3.2.1
* $P_{0}, P_{1}$
    * $X$の分布
* $p_{0}, p_{1}$
    * $P_{i}$の$\mu$に対する密度関数
* $\mu$
    * measure

このとき、hypothesis $$H = {P_{0}}$$, alternatives $K = {P_{0}}$とすると、$\exists k, r \in \mathbb{R}$

$$
\begin{equation}
    \mathrm{E}_{0}
    \left[
        \phi(X)
    \right]
    =
    \alpha
\end{equation}
$$

$$
\begin{equation}
    \phi(x)
    =
    \begin{cases}	
        1
            &
            p_{1}(x) > kp_{0}(x)
            \\
        0
            & 
            p_{1}(x) < kp_{0}(x)
            \\
        r
            & 
            p_{1}(x) = kp_{0}(x)
    \end{cases}
\end{equation}
$$

### proof.

$$
\begin{eqnarray}
    \alpha(c)
    & := &
        P_{0}(p_{1}(X) > c p_{0}(X))
    \nonumber
    \\
    & = &
        P_{0}
        \left(
            \frac{
                p_{1}(X)
            }{
                p_{0}(X)
            }
            >
            c
        \right)
    \nonumber
\end{eqnarray}
$$

とすると、$F(c) := 1 - \alpha(c)$は$p_{1}(X)/p_{0}(X)$の分布関数となる。
$F(c)$が単調増加で、右連続である。
よって、$\alpha(c)$は右連続で、単調減少である。

$$
    r
    :=
    \frac{
        \alpha - \alpha(c_{0})
    }{
        \alpha(c_{0} - 0) - \alpha(c_{0})
    }
$$


<div class="QED" style="text-align: right">$\Box$</div>

## 3.3. $p$-values


