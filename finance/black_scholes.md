---
layout: math
title: Black Scholes
---

# Black Scholes

$$
\begin{equation}
    S(t) = S(0) 
        + \int_{0}^{t} \mu S(s)\ ds 
        + \int_{0}^{t} \sigma S(s)\ dW_{s}
    \label{black_scholes_model_integral_form}
\end{equation}
$$

微分形でかくと

$$
\begin{equation}
    d S(t) = \mu S(t) dt + \sigma S(t) dW_{t}
    \label{black_scholes_model_differential_form}
\end{equation}
$$

である。
ここで、$S(t)$は原資産で、$\mu, \sigma, S(0)$は定数で、$S(0), \sigma(0) > 0$とする。
$S(t)$は解析的にとけて、以下の解を持つ。

$$
    S(t) = S(0) \exp
        \left(
            \left(
                \mu - \frac{\sigma^{2}}{2}
            \right) t
            + \sigma W_{t}
        \right)
$$

## call option

$$
    \mathrm{E}^{Q}
    \left[
        e^{-rT}(S(T) - K)^{+}
    \right]
    = S(0)N(d_{1}) - e^{-rT}KN(d_{2})
$$

ここで、$N$は標準正規分布関数で、

$$
\begin{eqnarray*}
    d_{1}
        & := & 
            \frac{
                \ln\left(\frac{S(0)}{K} \right) + (r + \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            },
        \\
    d_{2}
        & := & 
            \frac{
                \ln\left(\frac{S(0)}{K} \right) + (r - \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            }
\end{eqnarray*}
$$

である。
$K < 0 $とすると、$S(T) > 0$より

$$
\begin{eqnarray*}
    \mathrm{E}^{Q}
    \left[
        e^{-rT}(S(T) - K)
    \right]
        & = & S(0) - e^{-rT}K,
\end{eqnarray*}
$$

でforwardとなる。

## put option

$$
    \mathrm{E}^{Q}
    \left[
        e^{-rT}(K - S(T))^{+}
    \right]
    = -S(0)N(-d_{1}) - e^{-rT}KN(-d_{2})
$$

$K < 0 $とすると、$S(T) > 0$より

$$
\begin{eqnarray*}
    \mathrm{E}^{Q}
    \left[
        e^{-rT}(S(T) - K)
    \right]
        & = & 0
\end{eqnarray*}
$$

となる。


# Shifted black scholes model
Shifted Black model, Shifted lognormal model or displaced diffusionともいう。

$$
    S_{\theta}(t) = (S(0) - \theta)
        + \int_{0}^{t} \sigma (S_{\theta}(s) - \theta)\ dW_{s}^{Q}
$$

微分形でかくと

$$
    d S_{\theta}(t) = \sigma (S_{\theta}(t) - \theta) dW_{t}^{Q},
    \quad
    S(0) = S(0) - \theta

$$

である。

$S_{\theta}(t)$は解析的にとけて、以下の解を持つ。

$$
    S_{\theta}(t) =  \theta
        + (S(0) - \theta)\exp
        \left(
            - \frac{\sigma^{2}}{2} t
            + \sigma W_{t}
k        \right)
$$

## call option

$$
    C(S(0), T; K, r)
        := 
        \mathrm{E}^{Q}
        \left[
            e^{-rT}((S(T) - \theta) - (K - \theta))^{+}
        \right]
$$


# swaption pricing
swap rate $S(T)$をBlack-scholes modelとしてswaptionのPricingをする。
swap rateが$$\eqref{black_scholes_model_integral_form}$$で定義されているとする。
$S(T)$どの測度の下で定義されているかは、以下の議論においてはさほど重要ではない。
$S(T)$がannuity measureの下でマルチンゲールであるため、annuity measureの下では以下の形でかける。

$$
    S(t) = S(0) 
        + \int_{0}^{t} \sigma S(s)\ dW_{s}^{A}
$$

ここで、$W^{A}(t)$はannuity measureの下でのBrown運動である。
以下の議論ではこの事実を利用し、swaptionに対するblack formulaを導出する。
payer's swaptionのpayoffとreciever's swaptionを以下のように

$$
    V_{\mathrm{swap}}(t) 
        := P(t, T_{0}) - P(t, T_{N}) - K \sum_{i=1}^{N} \delta_{i} P(t, T_{i})
        = P(t, T_{0}) - P(t, T_{N}) - K A(t)
        = (S(t) - K)A(t)
$$

physical settled swaptionは、swaptionの固定レートを$K$とすると、満期日$T$とすると、満期日にswapの価値が正であれば、payer's swaptionの持ちては権利を行使する。
よって、payer's swaptionの価値は

$$
    V_{\mathrm{payersswap}}(t)
    = 
    \mathrm{E}_{t}^{Q}
    \left[
        \frac{D(T)}{D(t)}
        \left(
            (S(T) - K)A(T)
        \right)^{+}
    \right]
    =
    \mathrm{E}_{t}^{Q}
    \left[
        D(T) (S(T) - K)^{+} A(T)
    \right]
    =
    A(t)
    \mathrm{E}_{t}^{A}
    \left[
        (S(T) - K)^{+}
    \right]
$$

となる。
$S(T)$が$Q^{A}$の下マルチンゲールなので、black scholes call option formulaより、

$$
    V_{\mathrm{payerswapion}}(t)
    =
    A(t)(S(t)N(d_{1}) - KN(d_{2}))
$$

$$
\begin{eqnarray*}
    d_{1}
        & = & 
            \frac{
                \ln\left(\frac{S(0)}{K} \right) + \frac{1}{2}\sigma^{2}(T - t)
            }{
                \sigma \sqrt{T - t}
            },
        \\
    d_{2}
        & = & 
            \frac{
                \ln\left(\frac{S(0)}{K} \right) - \frac{1}{2}\sigma^{2}(T - t)
            }{
                \sigma \sqrt{T - t}
            }
\end{eqnarray*}
$$

# Greeks
black scholes modelのvanilla optionは解析的に求まる。
よって、Greeksも解析的に計算可能。
以下では

$$
    c(S, r, T, \sigma; K)
        := S(0)\Phi(d_{1}) - e^{-rT}K\Phi(d_{2})
$$

とし、

$$
\begin{eqnarray*}
    d_{1}(S, r, T, \sigma)
        & := & 
            \frac{
                \ln\left(\frac{S}{K} \right) + (r + \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            },
        \\
    d_{2}(S, r, T, \sigma)
        & := & 
            \frac{
                \ln\left(\frac{S}{K} \right) + (r - \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            }
\end{eqnarray*}
$$

とおく。
また、標準正規分布の分布関数$\Phi(x)$と密度関数$\phi(x)$の微分も計算しておく。
密度関数$\phi(x)$の微分を考える。

$$
    \phi(x) := \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{x^{2}}{2} \right)
$$

$$
\begin{eqnarray}
    \phi^{\prime}(x)
        & = & 
            -x \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{x^{2}}{2} \right)
        \nonumber
        \\
        & = &
            -x \phi(x)
        \label{phi_derivative}
        \\
    \phi^{\prime\prime}(x)
        & = &
            -\phi(x) - x\phi^{\prime}(x)
        \nonumber
        \\
        & = &
            -\phi(x) + x^{2}\phi(x)
\end{eqnarray}
$$

分布関数の微分は（存在すれば）密度関数に一致するので、$\Phi(x)$の微分は明らか。

$$
    \Phi(x) := 
        \frac{1}{\sqrt{2\pi}}
            \int_{-\infty}^{x} e^{-x^{2}/2}\ dx
$$

$$
    \Phi^{\prime}(x) = \phi(x)
$$


## Delta
deltaは原資産による微分である。
簡単のため、$d_{1}, d_{2}, c$を$S$の関数として書く。
まず、$d_{1}, d_{2}$の微分を考える。

$$
    \frac{\partial}{\partial S} d_{1}(S)
        = \frac{K}{S} \frac{1}{ \sigma \sqrt{T} }
$$

$$
    \frac{\partial}{\partial S} d_{2}(S)
        = \frac{K}{S} \frac{1}{ \sigma \sqrt{T} }
$$

$$
\begin{eqnarray}
    \frac{\partial}{\partial S} c(S)
        & = & 
        \Phi(d_{1}(S))
        + S\phi(d_{1}(S)) \frac{\partial}{\partial S} d_{1}(S)
        - K\phi(d_{2}(S)) \frac{\partial}{\partial S} d_{2}(S)
        \nonumber
        \\
        & = &
        \Phi(d_{1}(S))
        + 
        \frac{K}{S} \frac{1}{ \sigma \sqrt{T} }
        \left(
            S\phi(d_{1}(S)) - K\phi(d_{2}(S)) 
        \right)
\end{eqnarray}
$$


## Gamma
Gammaは原資産による2階微分である。
簡単のため、$d_{1}, d_{2}, c$を$S$の関数として書く。
まず、$d_{1}, d_{2}$の2階微分を考える。

$$
    \frac{\partial^{2}}{\partial S^{2}} d_{1}(S)
        = - \frac{K}{S^{2}} \frac{1}{ \sigma \sqrt{T} }
$$

$$
    \frac{\partial^{2}}{\partial S^{2}} d_{2}(S)
        = -\frac{K}{S^{2}} \frac{1}{ \sigma \sqrt{T} }
$$

$$
\begin{eqnarray}
    \frac{\partial^{2}}{\partial S^{2}} c(S)
        & = & 
            \frac{\partial}{\partial S} 
            \left(
                \Phi(d_{1}(S))
                + \frac{K}{S} \frac{1}{ \sigma \sqrt{T} }
                \left(
                    S\phi(d_{1}(S)) - K\phi(d_{2}(S)) 
                \right)
            \right)
            \nonumber
        \\
        & = & 
            \phi(d_{1}(S))d_{1}^{\prime}(S)
            + d_{1}^{\prime\prime}(S)
            \left(
                \phi(d_{1}(S)) 
                + S\phi^{\prime}(d_{1}(S)) 
                - K\phi^{\prime}(d_{2}(S)) d_{2}^{\prime}(S)
            \right)
        \nonumber
        \\
        & = &
            \phi(d_{1}(S))d_{1}^{\prime}(S)
            + d_{1}^{\prime\prime}(S)
            \left(
                \phi(d_{1}(S)) 
                - Sd_{1}(S)\phi(d_{1}(S)) 
                + Kd_{2}(S)\phi(d_{2}(S)) d_{2}^{\prime}(S)
            \right)
\end{eqnarray}
$$

## Vega
vegaはvolatility $\sigma$による微分である。
簡単のため、$d_{1}, d_{2}, c$を$S$の関数として書く。
まず、$d_{1}, d_{2}$の微分を考える。

$$
\begin{eqnarray}
    \frac{\partial}{\partial \sigma} d_{1}(\sigma)
        & = &
            \frac{\partial}{\partial \sigma}
            \frac{
                 (r + \frac{1}{2}\sigma^{2})\sqrt{T}
            }{
                \sigma 
            }
            \nonumber
        \\
        & = &
            \frac{
                 \sigma\sqrt{T}
                 - (r + \frac{1}{2}\sigma^{2})\sqrt{T}
            }{
                \sigma^{2}
            }
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{\partial}{\partial \sigma} d_{2}(\sigma)
        & = &
            \frac{\partial}{\partial \sigma}
            \frac{
                 (r - \frac{1}{2}\sigma^{2})\sqrt{T}
            }{
                \sigma 
            }
            \nonumber
        \\
        & = &
            \frac{
                 \sigma\sqrt{T}
                 - (r - \frac{1}{2}\sigma^{2})\sqrt{T}
            }{
                \sigma^{2}
            }
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{\partial}{\partial \sigma} c(\sigma)
        & = &
            \frac{\partial}{\partial \sigma} 
            \left(
                S\Phi(d_{1}(\sigma)) - e^{-rT}K\Phi(d_{2}(\sigma))
            \right)
        \nonumber
        \\
        & = &
            \left(
                S\phi(d_{1}(\sigma)) \frac{\partial}{\partial \sigma} d_{1}(\sigma)
                - e^{-rT}K\phi(d_{2}(\sigma)) \frac{\partial}{\partial \sigma} d_{2}(\sigma)
            \right)
        \nonumber
        \\
\end{eqnarray}
$$

## Theta

## Rho

