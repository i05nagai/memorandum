---
layout: math
title: Black Scholes
---

# Black Scholes

$$
\begin{equation}
    S(t) = S_{0}
        + \int_{0}^{t} \mu S(s)\ ds 
        + \int_{0}^{t} \sigma S(s)\ dW_{s}
    \label{black_scholes_model_integral_form}
\end{equation}
$$

微分形でかくと

$$
\begin{equation}
    d S(t) = \mu S(t) dt + \sigma S(t) dW_{t},
    \quad
    S(0) = S_{0}
    \label{black_scholes_model_differential_form}
\end{equation}
$$

である。
ここで、$S(t)$は原資産で、$\mu, \sigma, S(0)$は定数で、$S(0), \sigma(0) > 0$とする。
$S(t)$は解析的にとけて、以下の解を持つ。

$$
    S(t) = S_{0} \exp
        \left(
            \left(
                \mu - \frac{\sigma^{2}}{2}
            \right) t
            + \sigma W_{t}
        \right)
$$

## call option

$$
\begin{eqnarray}
    c_{BS}(0; S_{0}, K, r, T, \sigma)
        & :=  &
            \mathrm{E}^{Q}
            \left[
                e^{-rT}(S(T) - K)^{+}
            \right]
        \nonumber
        \\
        & = &
            S(0)N(d_{1}) - e^{-rT}KN(d_{2})
\end{eqnarray}
$$

ここで、$N$は標準正規分布関数で、

$$
\begin{eqnarray}
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
\end{eqnarray}
$$

である。
また、

$$
\begin{eqnarray}
    d_{1}
        & = & 
            \frac{
                \ln\left(\frac{S(0)}{K} \right) + (r + \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            }
        \nonumber
        \\
        & = &
            \frac{
                \ln\left(\frac{S(0)}{K} \right) + (r - \frac{1}{2}\sigma^{2} + \sigma^{2})T
            }{
                \sigma \sqrt{T}
            }
        \nonumber
        \\
        & = &
            d_{2} + \sigma \sqrt{T}
        \label{d1_d2_relation}
\end{eqnarray}
$$

が成り立つ。

### case1: strike is negative, underlying is positive
$K < 0, S_{0} > 0$とすると、$S(T) > 0$より

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

### case2: strike is positive, underlying is negative
$K > 0, S_{0} < 0$とすると、$S(T) < 0$より

$$
    c_{BS}(0; S_{0}, K, r, T, \sigma)
        = 0
$$

### case3: strike is negative, underlying is negative
$K < 0, S_{0} < 0$とすると、put-call parityより

$$
    (S(T) - K)^{+}
        = (S(T) - K) + (-(S(T) - K))^{+}
$$

である。
よって、

$$
\begin{eqnarray}
    c_{BS}(0; S_{0}, K, r, T, \sigma)
        & = &
            \mathrm{E}^{Q}
            \left[
                e^{-rT}
                \left(
                    (S(T) - K)
                        + (-(S(T) - K))^{+}
                \right)
            \right]
        \nonumber
        \\
        & = &
            (S_{0} - e^{-rT}K)
            + 
            \mathrm{E}^{Q}
            \left[
                e^{-rT} (-(S(T) - K))^{+}
            \right]
\end{eqnarray}
$$

となって、第二項はunderlying, strikeが正のcall optionの価格と等しくなる。
put optionをput-call parityで計算する場合は、実装上の循環呼び出しを避けるため重要となる。

### case4: option is expired
$T < 0$のときは、optionがexpiryしていると考えると以下の定義が妥当。

$$
    c_{BS}(0; S_{0}, K, r, T, \sigma)
        := 0
$$

### case5: negative volatility
$\sigma < 0$のときは、未定義が妥当。
volatilityは一般には負にはならない。

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
\begin{eqnarray}
    d_{1}(S, r, T, \sigma)
        & := & 
            \frac{
                \ln\left(\frac{S}{K} \right) + (r + \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            },
        \label{def_d1}
        \\
    d_{2}(S, r, T, \sigma)
        & := & 
            \frac{
                \ln\left(\frac{S}{K} \right) + (r - \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            }
        \label{def_d2}
\end{eqnarray}
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

また、以下が成り立つ。

$$
\begin{eqnarray}
    S\phi(d_{1})
        & = &
            S \frac{1}{\sqrt{2\pi}}
            \exp
            \left(
                -\frac{ d_{1}^{2} }{2} 
            \right)
        \nonumber
        \\
        & = &
            S \frac{1}{\sqrt{2\pi}}
            \exp
            \left(
                -\frac{ (d_{2} + \sigma\sqrt{T})^{2} }{2}
            \right)
        \nonumber
        \\
        & = &
            S \frac{1}{\sqrt{2\pi}}
            \exp
            \left(
                -\frac{ (d_{2}^{2} 
                + 2d_{2}\sigma\sqrt{T}
                + \sigma^{2}T) }{2}
            \right)
        \nonumber
        \\
        & = &
            S \frac{1}{\sqrt{2\pi}}
            e^{-\frac{d_{2}^{2} }{2} }
            \exp
            \left(
                -\frac{ 
                2(\ln(S/K) + (r - \frac{1}{2}\sigma^{2})T)
                + \sigma^{2}T) }{2}
            \right)
        \nonumber
        \\
        & = &
            S
            \phi(d_{2})
            \exp
            \left(
                -
                \left(
                    \ln(S/K) + (r - \frac{1}{2}\sigma^{2})T
                    + \frac{1}{2}\sigma^{2}T)
                \right)
            \right)
        \nonumber
        \\
        & = &
            S
            \phi(d_{2})
            \exp
            \left(
                -
                \left(
                    \ln(S/K) + rT
                \right)
            \right)
        \nonumber
        \\
        & = &
            S
            \phi(d_{2})
            \exp
            \left(
                - \ln(S/K)
            \right)
            e^{-rT}
        \nonumber
        \\
        & = &
            S
            \phi(d_{2})
            \frac{K}{S}
            e^{-rT}
        \nonumber
        \\
        & = &
            \phi(d_{2})
            K e^{-rT}
        \label{d1_d2_density_relation}
\end{eqnarray}
$$


## Delta
deltaは原資産による微分である。
簡単のため、$d_{1}, d_{2}, c$を$S$の関数として書く。
まず、$d_{1}, d_{2}$の微分を考える。

$$
\begin{eqnarray}
    \frac{\partial}{\partial S} d_{1}(S)
        & = &
        \frac{\partial}{\partial S}
            \left(
                \frac{
                    \left(\ln(S) - \ln(K) \right) + (r + \frac{1}{2}\sigma^{2})T
                }{
                    \sigma \sqrt{T}
                }
            \right)
        \nonumber
        \\
        & = & \frac{1}{S} \frac{1}{ \sigma \sqrt{T} }
    \\
    \frac{\partial}{\partial S} d_{2}(S)
        & = & \frac{1}{S} \frac{1}{ \sigma \sqrt{T} }
\end{eqnarray}
$$

以上と$$\eqref{d1_d2_density_relation}$$より

$$
\begin{eqnarray}
    \frac{\partial}{\partial S} c(S)
        & = & 
            \Phi(d_{1}(S))
                + S\phi(d_{1}(S)) \frac{\partial}{\partial S} d_{1}(S)
                - e^{-rT}K\phi(d_{2}(S)) \frac{\partial}{\partial S} d_{2}(S)
        \nonumber
        \\
        & = &
            \Phi(d_{1}(S))
            + 
            \frac{1}{S} \frac{1}{ \sigma \sqrt{T} }
            \left(
                S\phi(d_{1}(S)) - e^{-rT}K\phi(d_{2}(S)) 
            \right)
        \nonumber
        \\
        & = &
            \Phi(d_{1}(S))
\end{eqnarray}
$$

となる。

## Gamma
Gammaは原資産による2階微分である。
簡単のため、$d_{1}, d_{2}, c$を$S$の関数として書く。
まず、$d_{1}, d_{2}$の2階微分を考える。

$$
\begin{eqnarray}
    \frac{\partial^{2}}{\partial S^{2}} d_{1}(S)
        & = & -\frac{1}{S^{2}} \frac{1}{ \sigma \sqrt{T} }
    \\
    \frac{\partial^{2}}{\partial S^{2}} d_{2}(S)
        & = & -\frac{1}{S^{2}} \frac{1}{ \sigma \sqrt{T} }
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{\partial^{2}}{\partial S^{2}} c(S)
        & = & 
            \frac{\partial}{\partial S} 
                \Phi(d_{1}(S))
            \nonumber
        \\
        & = & 
            \phi(d_{1}(S))d_{1}^{\prime}(S)
\end{eqnarray}
$$

## Vega
vegaはvolatility $\sigma$による微分である。
簡単のため、$d_{1}, d_{2}, c$を$\sigma$の関数として書く。
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
                 (r + \frac{1}{2}\sigma^{2})\sqrt{T}
                     - \sigma \sigma\sqrt{T}
            }{
                \sigma^{2}
            }
        \nonumber
        \\
        & = &
            \frac{
                 (r - \frac{1}{2}\sigma^{2})\sqrt{T}
            }{
                \sigma^{2}
            }
        \\
    \frac{\partial}{\partial \sigma} d_{2}(\sigma)
        & = &
            \frac{\partial}{\partial \sigma}
            \frac{
                 (r - \frac{1}{2}\sigma^{2})\sqrt{T}
            }{
                \sigma^{2}
            }
        \nonumber
        \\
        & = &
            \frac{
                 (r - \frac{1}{2}\sigma^{2})\sqrt{T}
                    + \sigma \sigma\sqrt{T}
            }{
                \sigma^{2}
            }
        \nonumber
        \\
        & = &
            \frac{
                 (r + \frac{1}{2}\sigma^{2})\sqrt{T}
            }{
                \sigma^{2}
            }
\end{eqnarray}
$$

以上と$$\eqref{d1_d2_density_relation}$$より、

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
            S\phi(d_{1}(\sigma)) \frac{\partial}{\partial \sigma} d_{1}(\sigma)
                - e^{-rT}K\phi(d_{2}(\sigma)) \frac{\partial}{\partial \sigma} d_{2}(\sigma)
        \nonumber
        \\
        & = &
            S\phi(d_{1}(\sigma)) \frac{\partial}{\partial \sigma} d_{1}(\sigma)
                - S\phi(d_{1}(\sigma)) \frac{\partial}{\partial \sigma} d_{2}(\sigma)
        \nonumber
        \\
        & = &
            S\phi(d_{1}(\sigma)) 
            \left(
                \frac{\partial}{\partial \sigma} d_{1}(\sigma)
                    - \frac{\partial}{\partial \sigma} d_{2}(\sigma)
            \right)
        \nonumber
        \\
        & = &
            S\phi(d_{1}(\sigma)) 
            \left(
                \frac{
                     (r - \frac{1}{2}\sigma^{2})\sqrt{T}
                }{
                    \sigma^{2}
                }
                - 
                \frac{
                     (r + \frac{1}{2}\sigma^{2})\sqrt{T}
                }{
                    \sigma^{2}
                }
            \right)
        \nonumber
        \\
        & = &
             - \sqrt{T} S\phi(d_{1}(\sigma)) 
\end{eqnarray}
$$

## Theta
Thetaは現在時刻$t$による微分である。
簡単のため、$d_{1}, d_{2}, c$を$t$の関数として書く。
まず、$d_{1}, d_{2}$の微分を考える。

$$
\begin{eqnarray}
    \frac{\partial}{\partial t} d_{1}(t)
        & = &
            \frac{\partial}{\partial t}
            \left(
                \frac{
                    \ln\left(\frac{S}{K} \right) + (r + \frac{1}{2}\sigma^{2})(T - t)
                }{
                    \sigma \sqrt{T - t}
                }
            \right)
        \nonumber
        \\
        & = &
            \frac{\partial}{\partial t}
            \left(
                \frac{
                    (r + \frac{1}{2}\sigma^{2})
                }{
                    \sigma
                }
                \sqrt{T - t}
            \right)
        \nonumber
        \\
        & = &
            -
            \frac{
                (r + \frac{1}{2}\sigma^{2})
            }{
                2\sigma\sqrt{T - t}
            }
        \\
    \frac{\partial}{\partial t} d_{2}(t)
        & = &
            -
            \frac{
                (r - \frac{1}{2}\sigma^{2})
            }{
                2\sigma\sqrt{T - t}
            }
\end{eqnarray}
$$

以上と$$\eqref{d1_d2_density_relation}$$より

$$
\begin{eqnarray}
    \frac{\partial}{\partial t} c(t)
        & = &
            \frac{\partial}{\partial t} 
            \left(
                S\Phi(d_{1}(t)) - e^{-r(T - t)}K\Phi(d_{2}(t))
            \right)
        \nonumber
        \\
        & = &
            S\phi(d_{1}(t))
                \frac{\partial}{\partial t} d_{1}(t) 
            - re^{-r(T - t)}K\Phi(d_{2}(t))
            - e^{-r(T - t)}K\phi(d_{2}(t))
                \frac{\partial}{\partial t} d_{2}(t) 
        \nonumber
        \\
        & = &
            S\phi(d_{1}(t))
                \frac{\partial}{\partial t} d_{1}(t) 
            - S\phi(d_{1}(t))
                \frac{\partial}{\partial t} d_{2}(t) 
            - re^{-r(T - t)}K\Phi(d_{2}(t))
        \nonumber
        \\
        & = &
            S\phi(d_{1}(t))
            \left(
                \frac{\partial}{\partial t} d_{1}(t) 
                - \frac{\partial}{\partial t} d_{2}(t) 
            \right)
            - re^{-r(T - t)}K\Phi(d_{2}(t))
        \nonumber
        \\
        & = &
            S\phi(d_{1}(t))
            \left(
                -
                \frac{
                    (r + \frac{1}{2}\sigma^{2})
                }{
                    2\sigma\sqrt{T - t}
                }
                + \frac{
                    (r - \frac{1}{2}\sigma^{2})
                }{
                    2\sigma\sqrt{T - t}
                }
            \right)
            - re^{-r(T - t)}K\Phi(d_{2}(t))
        \nonumber
        \\
        & = &
            - S\phi(d_{1}(t))
            \left(
                \frac{
                    \sigma
                }{
                    2\sqrt{T - t}
                }
            \right)
            - re^{-r(T - t)}K\Phi(d_{2}(t))
\end{eqnarray}
$$


## Rho
Rhoは金利$r$による微分である。
簡単のため、$d_{1}, d_{2}, c$を$r$の関数として書く。
まず、$d_{1}, d_{2}$の微分を考える。

$$
\begin{eqnarray}
    \frac{\partial}{\partial r} d_{1}(r)
        & = &
            \frac{\partial}{\partial r}
            \left(
                \frac{
                    \ln\left(\frac{S}{K} \right) + (r + \frac{1}{2}\sigma^{2})(T - t)
                }{
                    \sigma \sqrt{T - t}
                }
            \right)
        \nonumber
        \\
        & = &
            \frac{\partial}{\partial t}
            \left(
                \frac{
                    \sqrt{T - t}
                }{
                    \sigma
                } r
            \right)
        \nonumber
        \\
        & = &
            \frac{
                \sqrt{T - t}
            }{
                \sigma
            }
        \\
    \frac{\partial}{\partial t} d_{2}(t)
        & = &
            \frac{
                \sqrt{T - t}
            }{
                \sigma
            }
\end{eqnarray}
$$

以上と$$\eqref{d1_d2_density_relation}$$より

$$
\begin{eqnarray}
    \frac{\partial}{\partial r} c(r)
        & = &
            \frac{\partial}{\partial r} 
            \left(
                S\Phi(d_{1}(r)) - e^{-r(T - t)}K\Phi(d_{2}(r))
            \right)
        \nonumber
        \\
        & = &
            S\phi(d_{1}(r))
                \frac{\partial}{\partial r} d_{1}(r) 
            + (T - t)e^{-r(T - t)}K\Phi(d_{2}(r))
            - e^{-r(T - t)}K\phi(d_{2}(r))
                \frac{\partial}{\partial r} d_{2}(r) 
        \nonumber
        \\
        & = &
            S\phi(d_{1}(r))
                \frac{\partial}{\partial r} d_{1}(r) 
            - S\phi(d_{1}(r))
                \frac{\partial}{\partial r} d_{2}(r) 
            + (T - t)e^{-r(T - t)}K\Phi(d_{2}(r))
        \nonumber
        \\
        & = &
            S\phi(d_{1}(r))
            \left(
                \frac{\partial}{\partial r} d_{1}(r) 
                - \frac{\partial}{\partial r} d_{2}(r) 
            \right)
            + (T - t)e^{-r(T - t)}K\Phi(d_{2}(r))
        \nonumber
        \\
        & = &
            (T - t)e^{-r(T - t)}K\Phi(d_{2}(r))
\end{eqnarray}
$$
