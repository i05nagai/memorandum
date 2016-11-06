---
layout: math
title: Interest Rate Modeling 2
---

# 10 One-Factor Short Rate Model I

## 10.1 The One-Factor Gaussian Short Rate Model

### 10.1.1 Notation

### 10.1.2 The Mean-Reverting 

#### 10.1.2.2 The General One-Factor GSR Model
1-factorのGSR odelの一般形は以下で与えられる。

$$
\begin{equation}
    dr(t)
        = \varkappa (\vartheta(t) - r(t)) dt + \sigma_{r}(t) dW(t),
    \label{chap10_general_one_factor_short_rate_model}
\end{equation}
$$

Section 4.5.2で示したように、HJMのもとでのshort rateのdynamicsは以下のようなseparableな形となる。

$$
\begin{eqnarray}
    df(t, T)
        & = & \sigma_{f}(t, T)
            \left(
                \int_{t}^{T} \sigma_{f}(t, u)\ du
            \right)
            dt
            + \sigma_{f}(t, T) dW(t),
    \label{chap10_instantaneous_forward_rate_of_general_one_factor_short_rate_model}
    \\
    \sigma_{f}(t, T)
        & = & \sigma_{r}(t) \exp
            \left(
                - \int_{t}^{T} \varkappa(u) \ du
            \right).
    \nonumber
\end{eqnarray}
$$

##### Proposition 10.1.6

##### Proposition 10.1.7 
$$
    x(t) := r(t) - f(0, t).
$$

このとき、$\eqref{chap10_general_one_factor_short_rate_model}$と$\eqref{chap10_instantaneous_forward_rate_of_general_one_factor_short_rate_model}$は

$$
\begin{equation}
    d x(t) 
        = (y(t) - \varkappa(t) x(t)) dt
            + \sigma_{r}(t) dW(t),
    \quad
    x(0) = 0
\end{equation}
$$

とかける。
ここで、

$$
\begin{equation}
    y(t) := \int_{0}^{t} e^{-2 \int_{u}^{t} \varkappa(s)\ ds} \sigma_{r}(u)^{2} \ du
\end{equation}
$$

である。
また、discount bondは以下のようにかける。

$$
\begin{eqnarray}
    P(t, T)
        & = & \frac{P(0, T)}{P(0, t)} \exp
            \left(
                -x(t) G(t, T) - \frac{1}{2} y(t) G(t, T)^{2}
            \right),
    \\
    G(t, T) 
        & := & \int_{t}^{T} e^{- \int_{t}^{u} \varkappa(s)\ ds}\ du.
    \nonumber
\end{eqnarray}
$$

