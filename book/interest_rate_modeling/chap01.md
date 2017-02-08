---
layout: slate_page
title: Interest Rate Modeling 1
book_title: Interest Rate Modeling
book_chapter: 1
---

# 1. Introduction to Arbitrage Pricing Theory

## 1.3 Equivalent Martingale Measures and Arbitrage

### Theorem 1.3.1 (Radon-Nikodym Theorem)
$P$, $\hat{P}$は確率測度$(\Omega, \mathcal{F})$上の同値な測度とする。
このとき、ある非負確率変数$R$が存在して、$\mathrm{E}^{P}(R) = 1$で、

$$
    \hat{P}(A) = \mathrm{E}^{P}
    \left[
        R 1_{\{A\}}
    \right],
    \forall A \in \mathcal{A}
$$

を満たす。
$R$は確率$1$で一意である。
また、Radon-Nikodym　derivativeとよび

$$
    \frac{d\hat{P}}{d P} 
        := R,
$$

とも書く。

### sketch of proof
Billingsley [1995]による。

任意の確率測度$\hat{P}$について、以下のdensity processを定義できる。

$$
\begin{equation}
    \zeta(t)
        := \mathrm{E}_{t}^{P}
        \left[
            \frac{d \hat{P}}{dP}
        \right],
        \forall t \in [0, T].
    \label{chap1_12_def_density_process}
\end{equation}
$$

明らかに$\zeta(t)$は$P$-マルチンゲールで、$\zeta(0) = 1$で、$\zeta(t) = \mathrm{E}_{t}^{P}(\zeta(T))$を満たす。

$$
\begin{eqnarray}
    \mathrm{E}^{\hat{P}}
    \left[
        Y(T) | \mathcal{F}_{t}
    \right]
    & = & \frac{1}{ \mathrm{E}^{P}( R | \mathcal{F}_{t}) }
        \mathrm{E}^{P}
        \left[
            R Y(T) | \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        \frac{1}{\zeta(t)} \mathrm{E}^{P}
        \left[
            \mathrm{E}^{P}
            \left[
                R | \mathcal{F}_{T}
            \right]
            Y(T)
            | \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}^{P}
        \left[
        \left.
            Y(T) \frac{\zeta(T)}{\zeta(t)}
        \right|
            \mathcal{F}_{t}
        \right]
\end{eqnarray}
$$

## 1.5 Girsanov's Teorem
Equivalent Martingale Measure(EMM)の存在と一意性と無裁定の関係を見てきた。
ここでは、以下について議論する。

1. 資産価格が許容するequivalent martingale measureの条件
2. measure変換による資産過程への影響

以下では、２つの確率測度の間でのBMの変換を扱う。
$P$, $P(\theta)$の2つのmeasureを扱う。
確率密度として、$\zeta^{\theta} := \mathrm{E}^{P}_{t}(dP(\theta)/dP)$を持つとする。
ここで、$\zeta^{\theta}$はexponential martingaleと呼ばれる以下を満たすIto過程である。

$$
    \frac{d \zeta^{\theta}(t)}{\zeta^{\theta}(t)}
        = -\theta(t)^{\mathrm{T}} dW(t),
$$

ここで$W(t)$は$d$次元の$P$-BMである。
$d$次元の確率過程$\theta$はmarket price of riskとして知られている。
Itoの補題より、

$$
\begin{eqnarray}
    \zeta^{\theta}
        & = & \exp
            \left(
                - \int_{0}^{t} \theta(s)^{\mathrm{T}} \ dW(s)
                - \frac{1}{2} \int_{0}^{t} \theta(s)^{\mathrm{T}}\theta(s) \ ds
            \right)
            \nonumber
        \\
        & =: & \mathcal{E}
            \left(
                - \int_{0}^{t} \theta(s)^{\mathrm{T}}\ dW(s)
            \right)
        \label{chap1_16_exponential_martingale}
\end{eqnarray}
$$

ここで、$\mathcal{E}$はDoleans exponentialと呼ばれる。

### Theorem 1.5.1 (Girsanov's Theorem)
$$\eqref{chap1_16_exponential_martingale}$$で$\zeta^{\theta}(t)$が定義されているとする。
また、$\theta(t)$はマルチンゲールであるとする。
このとき、$t \in [0, T]$について、

$$
    W^{\theta}(t)
        := W(t) + \int_{0}^{t} \theta(s)\ ds
$$

は$P(\theta)$の下でBMである。

### Remark
Girsanovの定理において、$\theta(t)$はマルチンゲールである必要がある。
確率過程がマルチンゲールとなるためには、いくつかの条件が知られているが、以下はNovikov conditionとして知られているものである。

$$
\begin{equation}
    \mathrm{E}^{P}
    \left[
        \exp
            \left(
                \frac{1}{2} \int_{0}^{t} \theta(s)^{\mathrm{T}}\theta(s)\ ds
            \right)
    \right]
    < \infty
    \label{chap1_17_novikov_condition}
\end{equation}
$$

Novikov conditionを満たせば、$\theta(t)$がマルチンゲールとなる。
実務的な応用では、この条件を示すことが難しい場合が多い。

## 1.8 Kolmogorov's Equation and the Feynman-Kac Theorem
これまで、derivativeの価格は、ある確率測度の下での期待値ないしPDEの解として表現できることを見てきた。
これは、期待値とPDEに関係があることを示唆している。
後のmodelのCalibrationのために、推移確率密度に関する幾つかの結果をここで述べておく。

以下のMarkov vector SDEを扱う。

$$
\begin{equation}
    dX(t) = \mu(t, X(t)) dt + \sigma(t, X(t)) dW(t),
    \quad
    X(0) = X_{0},
    \label{chap1_29_markov_vector_sde}
\end{equation}
$$

Therem 1.6.1の解の一意性を満たすように係数に条件をつけておく。
ここで、$g:\mathbb{R}^{d} \rightarrow \mathbb{R}$.

$$
    u(t, x) := \mathrm{E}^{P}
    \left[
        g(X(T))
        | X(t) = x
    \right],
$$

$u(t, X(t))$を$u(t)$と書く。

$$
    du(t)
        = u_{t}(t) dt
            + \sum_{i=1}^{p} u_{x_{i}}(t)\mu_{i}(t) dt
            + \frac{1}{2} \sum_{i=1}^{p} \sum_{j=1}^{p} u_{x_{i}x_{j}}(t)\Sigma_{i,j}(t) dt 
            + O(dW(t)).
$$

ここで、$\Sigma_{i,j} := \sigma\sigma^{\mathrm{T}}_{i,j}$である。
また、$u(t, X(t))$はマルチンゲールであるから、$dt$の項はゼロである。
よって、

$$
    \mathcal{A}
        := \sum_{i=1}^{p} \mu_{i}(t, x) \frac{\partial}{\partial x_{i}} 
            + \frac{1}{2} \sum_{i=1}^{p} \sum_{j=1}^{p} \Sigma_{i,j}(t, x) \frac{\partial^{2}}{\partial x_{i} \partial x_{j}}.
$$

とおくと、

$$
\begin{equation}
    \frac{\partial u(t,x)}{\partial t} + \mathcal{A} u(t, x) = 0,
    \label{chap1_30_kolmogorov_backward_equation}
\end{equation}
$$


Kolmogorov backward equationの有用な拡張である、Feyman-Kacに述べてこの節を終える。

$$
\begin{equation}
    \frac{\partial u(t, x)}{\partial t} + \mathcal{A}u(t,x) + h(t, x) 
        = r(t, x)u(t,x),
    \label{chap1_34_feyman_kac_pde}
\end{equation}
$$

ここで、$h, r:[0, T] \times \mathbb{R}^{p} \rightarrow \mathbb{R}$である。
また、境界条件は$u(T, x) = g(x)$である。
このPDEの解は以下で与えられる。

$$
\begin{equation}
    u(t, x) 
        = \mathrm{E}^{p}
        \left[
            \psi(t, T) g(X(T))
                + \int_{t}^{T} \psi(t, s)h(s, X(s)) \ ds
            |
            X(t) = x
        \right]
        \label{chap1_35_feyman_kac_solution}
\end{equation}
$$

ここで、

$$
    \psi(t, T)
        = \exp
            \left(
                - \int_{t}^{T} r(s, X(s))\ ds
            \right),
    \quad
    t \in [0, T].
$$
