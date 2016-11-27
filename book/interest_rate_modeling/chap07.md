---
layout: math
title: Interest Rate Modeling 1
---

# 7 Vanilla Models with Local Volatility

## 7.1 General Framework

### 7.1.1 Model Dynamics

$$
\begin{equation}
    dS(t) 
        = \lambda \phi(S(t)) dW(t),
    \label{chap7_1_general_local_volatility}
\end{equation}
$$

$\lambda$は正の定数で、$\phi: \mathbb{R} \rightarrow \mathbb{R}$はTheorem 1.6.1のような条件を満たすとする。
$S(t)$が非負になる為には、以下の条件を満たす必要がある。

$$
\begin{equation}
    \phi(0) = 1.
    \label{chap7_2_non_negative_condition}
\end{equation}
$$

modelの解析のために、必要に応じて$\eqref{chap7_2_non_negative_condition}$を無視する。
$P$をpropability measureとし、$\mathrm{E}^{P}$を$\mathrm{E}$と書く。


### 7.1.2. Volatility  Smile and Implied Density

$$
\begin{equation}
    c(t, S(t); T, K) 
        = E_{t}
        \left(
            (S(T)) - K)^{+}
        \right)
    \label{chap07_3}
\end{equation}
$$

である。
strikeと密度関数の関係について以下が知られている。

$$
\begin{eqnarray}
    P(S(T) \in dK) 
        & = &
            \left.
                \frac{\partial^{2} c(t, S(t); T, K}{\partial K^{2})}
            \right|_{K=\bar{K}} d\bar{K}
            \label{chap07_5_pdf_by_second_derivative_of_call_option}
        \\
        & = & E_{t}(\delta(S(T) - \bar{K})) d \bar{K}
            \label{chap07_4}
\end{eqnarray}
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

この結果は、BreedenとLitzenberger[1978]による。
$S(T)$の周辺分布が$T$満期のcall optionの$K$に対する連続性から得られることを述べている。
option marketでは、call optionとput optionのstrikeへの依存関係ををimplied volatilitesで表現することが一般的である。
具体的には、strike $K$の満期$T$のoption price$c$に対して、$t$でのimplied volatility function $\sigma_{B}(t, S; TK)$を以下の解として定義する。

$$
\begin{equation}
    c(t, S; T, K)
        = S\Phi(d_{+}) - K\Phi(d_{-})
    \label{chap07_6_call_option}
\end{equation}
$$

$$
    d_{\pm} 
        := \frac{
            \ln \frac{S}{K} \pm \\frac{1}{2}\sigma-{B}(t, S; T, K)^{2}(T - T)
        }{
            \sigma_{B}(t, S; T, K) \sqrt{T - t}
        }
$$

$\eqref{chap07_6_call_option}$の右辺は$\sigma_{B}(t, S; T, K)$を定数volatilityとしたBlack-Scholes-Merton formulaである。
写像$K \mapsto \sgima_{B}(t, S; T, K)$は$T$-maturity volatility smileとして知られている。
金利のmarketでは、volatility smileは大抵downward-slopingである。
しかし、十分大きな$K$についてvolatilityが増加する傾向も一般的である。
smileが単調に増加、減少し、Uの形状でない場合volatility skewという。
よって、skewをsmileのslopeの意味で用いる。


実際のmarketでは、call optionやput optionの場合はある決まった$\{K_{1}, \ldots, K_{N_{K}}\}$のstrikeと満期$\{T_{1}, \ldots, T_{N_{T}}\}$に対してvolatilityがquoteされている。

### 7.1.3 Choice of $\phi$



