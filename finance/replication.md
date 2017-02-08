---
title: Replication
---

# Overview
replication methodは

$$
    \mathrm{E}
    \left[
        f(S(T)) 
    \right]
    =
        f(S)
        + \int_{-\infty}^{S}
            \mathrm{E}
            \left[
                (k - S(T))^{+}
            \right]
            f^{\prime\prime}(k)\ d k
        + \int_{S}^{\infty}
            \left[
                (S(T) - k)^{+}
            \right]
            f^{\prime\prime}(k)\ d k
$$

として、右辺を計算する計算手法である。
特に、black scholes式でeuropean optionの価格がかける場合は

$$
    \mathrm{E}
    \left[
        f(S(T)) 
    \right]
    =
        f(S)
        + \int_{-\infty}^{S}
            p(0; S, k, r, T, \sigma)
            f^{\prime\prime}(k)\ d k
        + \int_{S}^{\infty}
            c(0; S, k, r, T, \sigma)
            f^{\prime\prime}(k)\ d k
$$

となる。
ここで、$p$, $c$はputとcallに対するBlack scholes formulaである。
$S(T)$がswap rateの場合は

$$
    \mathrm{E}^{A}
    \left[
        f(S(T)) 
    \right]
    =
        f(S)
        + \int_{-\infty}^{S}
            p(0; S, k, 1, T, \sigma)
            f^{\prime\prime}(k)\ d k
        + \int_{S}^{\infty}
            c(0; S, k, 1, T, \sigma)
            f^{\prime\prime}(k)\ d k
$$

ここで、$p$, $c$はreceiver'sとpayer'sのblack swaption formulaである。
第三項はswapのannuityである。

# 例

## 例1
通常の$f(s)$がstrike $K$のcall optionの場合は、$T$-forward measureでの期待値に直し、期待値の中身がnumeraireに依存しないようにする。
$f(s; K) := (s - K)^{+}$とかくと

$$
\begin{eqnarray}
    c(0; S, K, r, T, \sigma)
        & = &
            P(0, T) 
            \mathrm{E}^{T}
            \left[
                (S(T) - K)^{+}
            \right]
    \nonumber
    \\
        & = &
            P(0, T)
            \left(
                (S - K)^{+}
                + 
                \int_{-\infty}^{S}
                    p(0; S, k, 1, T, \sigma)
                    \delta_{S - k}
                \ d k
                + 
                \int_{S}^{\infty}
                    c(0; S, k, 1, T, \sigma)
                    \delta_{S - k}
                \ d k
            \right)
    \nonumber
    \\
        & = &
            \begin{cases}	
                P(0, T)
                \left(
                    (S - K)^{+} + p(0; S, K, 1, T, \sigma)    
                \right)
                = P(0, T)c(0; S, K, 1, T, \sigma)
                & S \ge K \\
                0 + c(0; S, K, 1, T, \sigma) & S < K 
            \end{cases}
\end{eqnarray}

$$


## 例2
$f(s)$がstrike $K$のswap rateに対するcallの場合、$f(s; K) := (s - K)^{+}$とかくと

$$
\begin{eqnarray}
    c(0; S, K, 1, T, \sigma)
        & = &
            \mathrm{E}^{A}
            \left[
                (S(T) - K)^{+}
            \right]
    \nonumber
    \\
        & = &
            (S - K)^{+}
            + 
            \int_{-\infty}^{S}
                p(0; S, k, 1, T, \sigma)
                \delta_{k - K}
            \ d k
            + 
            \int_{S}^{\infty}
                c(0; S, k, 1, T, \sigma)
                \delta_{k - K}
            \ d k
    \nonumber
    \\
        & = &
            \begin{cases}	
                (S - K) + p(0; S, K, 1, T, \sigma) = c(0; S, K, 1, T, \sigma) & S \ge K \\
                0 + c(0; S, K, 1, T, \sigma) & S < K 
            \end{cases}
\end{eqnarray}
$$

## 例3
$f(s)$がstrike $K$のswap rateに対するputの場合、$f(s; K) := (K - s)^{+}$とかくと

$$
\begin{eqnarray}
    p(0; S, K, 1, T, \sigma)
        & = &
            \mathrm{E}^{A}
            \left[
                (K - S(T))^{+}
            \right]
    \nonumber
    \\
        & = &
            (K - S)^{+}
            + 
            \int_{-\infty}^{S}
                p(0; S, k, 1, T, \sigma)
                \delta_{K - k}
            \ d k
            + 
            \int_{S}^{\infty}
                c(0; S, k, 1, T, \sigma)
                \delta_{K - k}
            \ d k
    \nonumber
    \\
        & = &
            \begin{cases}	
                0 + p(0; S, K, 1, T, \sigma) = p(0; S, K, 1, T, \sigma) & S \ge K \\
                (K - S) + c(0; S, K, 1, T, \sigma) = p(0; S, K, 1, T, \sigma) & S < K 
            \end{cases}
\end{eqnarray}
$$

## 例4
$f(s)$がstrike $K$のswap rateに対するbull-spreadの場合、$f(s; K_{L}, K_{U}) := \min((s - K_{L})^{+}, K_{U})$とかくと$f(s; K_{L}, K_{U}) = (S - K_{L})^{+} - (S - K_{U})^{+}$に注意すると

$$
\begin{eqnarray}
    c(0; S, K_{L}, 1, T, \sigma)
        - c(0; S, K_{U}, 1, T, \sigma)
        & = &
            \mathrm{E}^{A}
            \left[
                (S(T) - K_{L})^{+}
                    - (S(T) - K_{U})^{+}
            \right]
    \nonumber
    \\
        & = &
            \mathrm{E}^{A}
            \left[
                \min((S(T) - K_{L}), K_{U})
            \right]
    \nonumber
    \\
        & = &
            (S(0) - K_{L})^{+} - (S(0) - K_{U})^{+}
            + 
            \int_{-\infty}^{S}
                p(0; S, k, 1, T, \sigma)
                (
                    \delta_{k - K_{L}}
                    -
                    \delta_{k - K_{U}}
                )
            \ d k
            + 
            \int_{S}^{\infty}
                c(0; S, k, 1, T, \sigma)
                (
                \delta_{k - K_{L}}
                -
                \delta_{k - K_{U}}
                )
            \ d k
    \nonumber
\end{eqnarray}
$$

ここで、$0 < K_{L} < K_{U} < S$とすると

$$
\begin{eqnarray}
    & = &
        (S(0) - K_{L})^{+} - (S(0) - K_{U})^{+}
            + p(0; S, K_{L}, 1, T, \sigma)
            - p(0; S, K_{U}, 1, T, \sigma)
            + 0
    \nonumber
    \\
        & = &
        (S(0) - K_{L})^{+} - (S(0) - K_{U})^{+}
            + c(0; S, K_{L}, 1, T, \sigma) - (S(0) - K_{L})
            - (c(0; S, K_{U}, 1, T, \sigma) - (S(0) - K_{U}))
    \nonumber
    \\
        & = &
        (K_{L} - S(0))^{+} - (K_{U} - S(0))^{+}
            + c(0; S, K_{L}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
    \nonumber
    \\
        & = &
            c(0; S, K_{L}, 1, T, \sigma) - c(0; S, K_{U}, 1, T, \sigma)
\end{eqnarray}
$$

となる。
ここで、$0 < K_{L} < K_{U} = S$とすると

$$
\begin{eqnarray}
    & = &
        (S(0) - K_{L})^{+} - (S(0) - K_{U})^{+}
            + p(0; S, K_{L}, 1, T, \sigma)
            - p(0; S, K_{U}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
    \nonumber
    \\
        & = &
        (S(0) - K_{L})^{+} - (S(0) - K_{U})^{+}
            + c(0; S, K_{L}, 1, T, \sigma) - (S(0) - K_{L})
            - (c(0; S, K_{U}, 1, T, \sigma) - (S(0) - K_{U}))
            - c(0; S, K_{U}, 1, T, \sigma)
    \nonumber
    \\
        & = &
        (K_{L} - S(0))^{+} - (K_{U} - S(0))^{+}
            + c(0; S, K_{L}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
    \nonumber
    \\
        & = &
            c(0; S, K_{L}, 1, T, \sigma) - c(0; S, K_{U}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
\end{eqnarray}
$$

となるから、call optionとput optionの積分の$\delta_{K_{U} - k}$はどちらか一方0でなければならない。
ここで、$0 = K_{L} < K_{U} = S(0)$とすると

$$
\begin{eqnarray}
    & = &
        (S(0) - K_{L})^{+} - (S(0) - K_{U})^{+}
            + p(0; S, K_{L}, 1, T, \sigma)
            - p(0; S, K_{U}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
    \nonumber
    \\
        & = &
        S(0) - 
            + c(0; S, K_{L}, 1, T, \sigma) - S(0)
            - c(0; S, K_{U}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
    \nonumber
    \\
        & = &
            + c(0; S, K_{L}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
            - c(0; S, K_{U}, 1, T, \sigma)
\end{eqnarray}
$$

となるから、call optionとput optionの積分の$\delta_{K_{U} - k}$はどちらか一方0でなければならない。
以上から積分の端点のdelta関数はどちらか一方の関数に含まれる必要がある。
