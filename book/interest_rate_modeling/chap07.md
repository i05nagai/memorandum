---
layout: math
title: Interest Rate Modeling 1
---

# 7

### 7.1.2. Volatility  Smile and Implied Density

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
