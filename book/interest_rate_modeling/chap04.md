---
layout: math
title: Interest Rate Modeling 1
---

# 4

## 4.2 Fixed Income Probability Measures

### 4.2.1 Risk Neutral Measure

### 4.2.2 $T$-Forward Measure

### 4.2.3 Spot Measure

### 4.2.4 Terminal and Hybrid Measures

### 4.2.5 Swap Measures

## 4.3 Multi-Currency Markets


### 4.3.1 Notations and FX Forwards
* $P_{d}(t, T)$
    * domestic economyでの$t$のzero coupon bond 
* $P_{f}(t, T)$
    * foreign economyでの$t$のzero coupon bond 
* $X(t)$
    * foreign exchange rate
    * $t$に外国通貨1単位に対する国内通貨

外国のzero coupon bondを$\tilde{P}_{d}(t, T)$

$$
    \tilde{P}_{d}(t, T) := X(t)P_{f}(t, t).
$$

$$
    X_{T}(t) 
        := \frac{\tilde{P}_{d}(t, T)}{P_{d}(t, T)} 
        = X(t) \frac{P_{f}(t, T)}{P_{d}(t, T)}
$$

$X_{T}(t)$はforwrad FX rateという。
forward FX rateの由来は以下の裁定取引による。

* 時刻$t$で
    1. 国内通貨で$\tilde{P}_{d}(t, T)$だけ外国のzero-coupon bondを買う
        * 資金
            * $-\tilde{P}_{d}(t, T)$
        * 資産
            * 額面$\tilde{P}_{d}(t, T) / (X(t) P_{f}(t, T))$の外国のzero-coupon bond
    2. 額面$\tilde{P}_{d}(t, T) / P_{d}(t, T)$で、国内のzero-coupon bondを売る
        * 資金
            * $(\tilde{P}_{d}(t, T) / P_{d}(t, T)) P_{d}(t, T) = \tilde{P}_{d}(t, T)$
        * 資産
            * 額面$\tilde{P}_{d}(t, T) / P_{d}(t, T)$国内のzero-coupon bondを空売り
* 時刻$T$で
    1. $\tilde{P}_{d}(t, T) / (X(t) P_{f}(t, T)$を外国通貨で得る
    2. $\tilde{P}_{d}(t, T) / P_{d}(t, T)$を国内通貨で払う
    * netすると国内通貨で以下を得る

$$
    \frac{\tilde{P}_{d}(t, T)}{X(t)P_{f}(t, T)}X(T) - \frac{\tilde{P}_{d}(t, T)}{P_{d}(t, T)} 
        = X(T) - X_{T}(t)
$$

よって、無裁定の下では$X(T) = X_{T}(t)$で、$X_{T}(t)$が$T$で外国通貨1単位得るのに必要な国内通貨になる。


### 4.3.2 Risk Neutral Measures
* $\beta_{d}(t)$
    * 国内のmoney market account
* $Q^{d}$
    * 国内のrisk-neutral measure
* $\beta_{f}(t)$
    * 外国のmoney market account
* $Q^{f}$
    * 外国のrisk-neutral measure

$g(\cdot)$が$T$でforeign currencyでのpayoffとすると、foreign measureの下

$$
\begin{equation}
    V_{f}(t) 
        =  \beta_{f}(t) \mathrm{E}_{t}^{f}
        \left[
            \frac{g(T)}{\beta_{f}(T)}
        \right],
    \label{chap4_27_value_under_foreign_risk_neutral_measure}
\end{equation}
$$

である。
一方、domestic risk-neutral measureの下では、

$$
\begin{equation}
    V_{d}(t) 
        =  \beta_{d}(t) \mathrm{E}_{t}^{d}
        \left[
            \frac{g(T)X(T)}{\beta_{d}(T)}
        \right]
    \label{chap4_28_value_under_domestic_risk_neutral_measure}
\end{equation}
$$

である。
無裁定のででは

$$
\begin{eqnarray}
    V_{d}(t) 
        & = & X(t)V_{f}(t)
    \nonumber
    \\
    \iff
    \beta_{f}(t)\mathrm{E}_{t}^{d}
    \left[
        \frac{g(T)X(T)}{\beta_{d}(T)}
    \right]
        & = & X(t) \beta_{f}(t) \mathrm{E}_{t}^{f}
        \left[
            \frac{g(T)}{\beta_{f}(T)}
        \right]
    \label{chap4_29_equation}
\end{eqnarray}
$$

である。

#### Lemma 4.3.1

$$
    \mathrm{E}^{d}
    \left[
        \frac{d Q^{f}}{d Q^{d}}
    \right]
        = \frac{\beta_{f}(t) X(t)}{\beta_{d}(t) X(0)},
    \quad
    t \ge 0
$$

#### sketch of proof
$\mathcal{F}_{t}$-measurable variable $Y(T) := g(T) X(T) / \beta_{d}(T)$とおくと、$\eqref{chap4_29_equation}$は


$$
    \mathrm{E}_{t}^{d}
    \left[
        Y(T)
    \right]
        = X(t) \frac{\beta_{f}(t)}{\beta_{d}(t)}
            \mathrm{E}_{t}^{f}
            \left[
                \frac{Y(T)}{X(T)} \frac{\beta_{d}(T)}{\beta_{f}(T)}
            \right],
$$

TODO

### 4.3.3 Other Measures

## 4.4 The HJM Analysis

### 4.4.1 Bond Price Dynamics

### 4.4.2 Forward Rate Dynamics

### 4.4.3 Short Rate Process

## 4.5 Examples of HJM Models

### 4.5.1 The Gaussian Models

### 4.5.2 Gaussian HJM Models

### 4.5.3 Log-Normal HJM Models

