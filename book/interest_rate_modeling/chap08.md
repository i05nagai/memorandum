---
layout: math
title: Interest Rate Modeling 1
---

# 8 

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
        = \int f(K) \frac{\partial^{2} c(0, S(0); T, K)}{\partial K^{2}}  \ P(S(T) \in dK
    \label{chap8_expectation_with_pdf}
\end{equation}
$$



#### Proposition 8.4.13. 
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

#### skecth of proof
$\eqref{chap8_expectation_with_pdf}$を部分積分する。

$$
\begin{eqnarray*}
    \int f(K) \frac{\partial^{2} c(0, S(0);T, K)}{\partial K^{2}} \ dK
        & = &
            f(K^{*}) \frac{\partial c(0, S(0);T, K)}{\partial K} 
                + \int f'(K) \frac{\partial c(0, S(0);T, K)}{\partial K} \ d K
\end{eqnarray*}
$$

TODO
<div class="QED" style="text-align: right">$\Box$</div>

