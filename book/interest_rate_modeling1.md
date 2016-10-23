---
layout: math
title: Interest Rate Modeling 3
---

# Interest Rate Modeling 1

## Symbols

## 7.1.2. Volatility  Smile and Implied Density

$$
\begin{equation}
    c(t, S(t); T, K) 
        = E_{t}
        \left(
            (S(T)) - K)^{+}
        \right)
\end{equation}
$$

である。
strikeと密度関数の関係について以下が知られている。

$$
    P(S(T) \in dK) 
        = 
            \left.
                \frac{\partial^{2} c(t, S(t); T, K}{\partial K^{2}} 
            \right|_{K=\bar{K}} d\bar{K}
        = E_{t}(\delta(S(T) - \bar{K})) d \bar{K}
$$

Heuristicに計算すると以下のようになる。

$$
\begin{eqnarray*}
    \int f(\tilde{K}) 
        \left. 
            \frac{\partial^{2} c(0, S(0); T, K)}{\partial K^{2}}  
        \right|_{K=\tilde{K}}\ d\tilde{K} 
        & = & \int f(\tilde{K}) 
            \left. 
                \frac{\partial^{2} E_{t}[(S(T) - K)^{+}]}{\partial K^{2}}  
            \right|_{K=\tilde{K}}\ d\tilde{K} \\
        & = & E_{t}
            \left[
                \int f(\tilde{K}) 
                    \left. 
                        \frac{\partial^{2} (S(T) - K)^{+}}{\partial K^{2}}  
                    \right|_{K=\tilde{K}}\ d\tilde{K} 
            \right] \\
       & = &  E_{t}
            \left[
                \int f(\tilde{K}) \delta(S(T) - \tilde{K})\ d\tilde{K}
            \right] \\
       & = & E_{t}[f(S(T))]
\end{eqnarray*}
$$

## 8.4.5 Fourier Integration for Arbitrary European Payoffs
$f$をpayoffとすると、

$$
    E(f(S(T))) 
        = \int f(K)\ P(S(T) \in dK)
$$

これは、更に(7.5)より

$$
\begin{equation}
    E(f(S(T))) 
        = \int f(K) \frac{\partial^{2} c(0, S(0); T, K)}{\partial K^{2}}  \ P(S(T) \in dK
    \label{chap8_expectation_with_pdf}
\end{equation}
$$



### Proposition 8.4.13. 
$f(x) \in C^{2}$とする。
満期$T$、payoffが$f$のeuropean optionの価値は、callとputの積分で表現できる。
つまり、以下が$\forall K$について成立。
$$
\begin{equation}
    E(f(S(T))) 
        = f(K*)
            + f'(K*)(S(0) - K)
            + \int_{-\infty}^{K*} p(0, S(0),; T, K) f''(K)\ dK
            + \int_{K*}^{\infty} c(0, S(0); T, K) f''(K)\ dK
\end{equation}
$$

#### proof of skecth
$\eqref{chap8_expectation_with_pdf}$を部分積分する。

$$
\begin{eqnarray*}
    \int f(K) \frac{\partial^{2} c(0, S(0);T, K)}{\partial K^{2}} \ dK
        & = &
            f(K^{*}) \frac{\partial c(0, S(0);T, K)}{\partial K} 
                + \int f'(K) \frac{\partial c(0, S(0);T, K)}{\partial K} \ d K
\end{eqnarray*}
$$

