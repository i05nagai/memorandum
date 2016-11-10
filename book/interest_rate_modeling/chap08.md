---
layout: math
title: Interest Rate Modeling 1
---

# 8 Vanilla Models with Stochastic Volatility I

## 8.1 Model Definition

## 8.2 Model Parameters

## 8.3 Basic Properties

## 8.4 Fourier Integration
SV modelの精度の良い計算について議論する。
ここでの議論は、Fourier integration methodの応用である。
Lewis[2000], Carr and Madan [1999], Lipton[2002] and Lee[2004]などによる。

### 8.4.1 General Theory

### 8.4.3 numerical Implementation

### 8.4.4 Refinements of Numeriacal Implementation


### 8.4.5 Fourier Integration for Arbitrary European Payoffs
$f$をpayoffとすると、

$$
    E(f(S(T))) 
        = \int f(K)\ P(S(T) \in dK)
$$

これは、更に(7.5)より

$$
\begin{equation}
    E(f(S(T))) 
        = \int_{-\infty}^{\infty} f(K) \frac{\partial^{2} c(0, S(0); T, K)}{\partial K^{2}}  \ dK,
    \label{chap8_34_expectation_with_pdf}
\end{equation}
$$

#### Proposition 8.4.13. 
$f(x) \in C^{2}$とする。
満期$T$、payoffが$f$のeuropean optionの価値は、callとputの積分で表現できる。
つまり、以下が$\forall K^{*}$について成立。
$$
\begin{equation}
    E(f(S(T))) 
        = f(K^{*})
            + f'(K^{*})(S(0) - K^{*})
            + \int_{-\infty}^{K*} p(0, S(0); T, K) f''(K)\ dK
            + \int_{K*}^{\infty} c(0, S(0); T, K) f''(K)\ dK
    \label{chap8_35_replication_formula}
\end{equation}
$$

#### skecth of proof
$\eqref{chap8_34_expectation_with_pdf}$を部分積分する。
$F(K) := \frac{\partial c(0, S(0); T, K)}{\partial K}$は$S(T)$の分布関数であるから、

$$
  \lim_{K \rightarrow \infty} F(K) = 1,
  \quad
  \lim_{K \rightarrow -\infty} F(K) = 0,
$$

である。

$$
\begin{eqnarray*}
    \int_{-\infty}^{\infty} f(K) \frac{\partial^{2} c(0, S(0);T, K)}{\partial K^{2}} \ dK
        & = &
            \int_{-\infty}^{K^{*}} f(K) \frac{\partial^{2} c(0, S(0);T, K)}{\partial K^{2}} \ dK
            + \int_{K^{*}}^{\infty} f(K) \frac{\partial^{2} c(0, S(0);T, K)}{\partial K^{2}} \ dK
        \\
        & = &
            \left[
                f(K) \frac{\partial c(0, S(0);T, K)}{\partial K} 
            \right]_{-\infty}^{K^{*}}
            +
            \left[
                f(K) \frac{\partial c(0, S(0);T, K)}{\partial K} 
            \right]_{K^{*}}^{\infty}
                + \int_{-\infty}^{\infty} f'(K) \frac{\partial c(0, S(0);T, K)}{\partial K} \ d K
        \\
        & = &
            f(
                + \int_{-\infty}^{\infty} f'(K) \frac{\partial c(0, S(0);T, K)}{\partial K} \ d K
        \\
        & = &
            + f'(K) c(0, S(0);T, K)
            + \int_{-\infty}^{\infty} f''(K) c(0, S(0);T, K) \ d K
            
\end{eqnarray*}
$$

<div class="QED" style="text-align: right">$\Box$</div>

