---
layout: math
title: Quant CMS
---


# Calculation methods of quanto cms

## Symbols
* $P_{d}(t, T)$
    * value of domestic currency $T$ maturity zero coupon bond at time $t$.
* $P_{f}(t, T)$
    * value of foreign currency $T$ maturity zero coupon bond at time $t$.
* $S(t)$
    * domestic forward swap rate at time $t$.
* $X(t)$
    * FX rate [DOM/FOR] at time $t$.
    * domestic currency per unit of foreign currency.
* $X_{T}(t)$
    * $T$ forward FX rate at time $t$.
* $T_{p}$
    * payment date of quanto CMS
* $\Phi$
    * standard gaussian c.d.f.
* $\phi$
    * standard gaussian p.d.f.
* $c(t, S(t); K, T)$
    * strike $K$, Maturity $T$のcall optionの$t$での価格
* $p(t, S(t); K, T)$
    * strike $K$, Maturity $T$のput optionの$t$での価格
* $\Psi^{A}(K)$
    * $S(T)$の分布
    * $\Phi^{A}(K) = 1 + \frac{\partial }{\partial K} c(0, S(0); K, T)$
* $\psi^{A}$
    * $S(T)$の密度関数
    * $\phi^{A}(K) = \frac{\partial^{2} }{\partial K^{2}} c(0, S(0); K, T)$


## Simple case
volatility $\sigma_{X}$は$T$満期のFX rateのATM optionにキャリブレーションして求める。
$X_{T_{p}}$が$Q^{A,d}$の下でlog-normalであるとする。

$$
\begin{equation}
    X_{T_{p}}(T) = X(0) e^{\sigma_{X}\sqrt{T}\xi_{1} + m_{X}T},
\end{equation}
$$

ここで、$\xi_{1}$は標準正規乱数で、$\sigma_{X}$はvolatility、$m_{X}$は定数である。

$S(T)$と$X_{T_{p}}$の同時分布を表現する為に、copula methodを使う。
Chapter 17でcopula methodについて詳しく述べるが、ここでは次のように$S(T)$を定義する。
$\xi_{2}$が標準正規乱数とすると、

$$
    S(T) := (\Psi^{A})^{-1}(\Phi(\xi_{2})),
$$

ここで、$\Phi(\cdot)$は標準正規分布のc.d.f.である。
$S(T)$と$X_{T_{p}}(T)$の相関は$\xi_{1}$と$\xi_{2}$の相関$\rho_{XS}$で表現される。

$$
\begin{eqnarray*}
    X_{T_{p}}(T)
        & = & X(0) e^{\sigma_{X} \sqrt{T} \xi_{1} + m_{X}T},
        \\
    S(T) 
        & = & (\Psi^{A})^{-1}(\Phi(\xi_{2})),
        \\
    Corr(\xi_{1}, \xi_{2}) 
        & = & \rho_{XS}.
\end{eqnarray*}
$$

$$
    \chi(s) = X(0) e^{m_{X}T} \hat{\chi}(s),
$$

ここで、

$$
    \tilde{\chi}(s)
        := \exp 
            \left(
                \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right).
$$

である。
annuity mapping function $\alpha(\cdot)$は条件付き期待値で定義されているとする。

$$
\begin{equation}
    V_{\mathrm{QuantoCMS}}(0)
        \approx
            P_{f}(0, T_{p})
            \frac{\mathrm{E}^{A,d}
            \left[
                g(S(T)) \alpha(S(T)) \tilde{\chi}(S(T))
            \right]
            }{\mathrm{E}^{A,d}
            \left[
                \alpha(S(T)) \tilde{\chi}(S(T))
            \right]
            }
\end{equation}
$$

### Calculation

$$
    \mathrm{E}^{A,d}
    \left[
        g(S(T)) \alpha(S(T)) \tilde{\chi}(S(T))
    \right]
        = S(0) \alpha(S(0)) \tilde{\chi}(S(0))
        + \int_{-\infty}^{S(0)} c(0, S(0); K, T) w(K) \ dK
        + \int_{S(0)}^{\infty} c(0, S(0); K, T) w(K) \ dK
$$

ここで、

$$
    w(k) := \frac{d^{2} }{d k^{2}} (g(k) \alpha(k) \tilde{\chi}(k))
$$

$\tilde{\chi}$の微分を考える。
$h(s) := \Phi^{-1}(\Psi^{A}(s))$とおくと

$$
    \frac{d}{d s} h(s) 
        = \frac{1}{\phi(\Phi^{-1}(\Psi^{A}(s)))} \psi^{A}(s)
        = \frac{1}{\phi(h(s))} \psi^{A}(s),
$$

$$
    \frac{d^{2}}{d s^{2}} h(s) 
        = \frac{
            (\psi^{A})^{\prime}(s) \phi(h(s)) - \psi^{A}(s) \phi^{\prime}(h(s)) h^{\prime}(s)
        }{
            \phi(h(s))^{2}
        } 
$$

$$
    \tilde{\chi}(s)
        = \exp 
            \left(
                \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right).
$$

$$
    \tilde{\chi}'(s)
        = \rho_{XS}\sigma_{X}\sqrt{T}h'(s) \tilde{\chi}(s)
$$

$$
    \tilde{\chi}''(s)
        = \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
               h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right)
        
$$

linear TSR modelの場合、$\alpha$の微分を考える。

$$
    \alpha(s) := \alpha_{1}s + \alpha_{2}
$$

$$
    \alpha'(s) = \alpha_{1}
$$

$$
    \alpha''(s) = 0
$$

$g(k) := (S - k)^{+} = \max(S -k, 0)$のcall optionのとき、$g$の微分を考える。

$$
    g^{\prime}(k) = -1_{(-\infty, S]}(k),
$$

$$
    g^{\prime\prime}(k) = -\delta(S - k),
$$

$g(k) := (k - S)^{+} = \max(k - S, 0)$のput optionのとき、$g$の微分を考える。

$$
    g^{\prime}(k) = 1_{[S, \infty)}(k),
$$

$$
    g^{\prime\prime}(k) = \delta(S - k),
$$

$g(k) := \min(\max(S - k, 0), c)$のcap call optionのとき、$g$の微分を考える。

$$
    g^{\prime}(k) = -1_{[S - c, S]}(k),
$$

$$
    g^{\prime\prime}(k) = \delta(S - k)+\delta(S - c - k),
$$

Black Scholesのcall optionの微分を考えるために、$d_{1}$の微分を考える。

$$
    d_{1}(K)
        := \frac{
           \frac{S}{K} + (r + \sigma^{2}/2)T
        }{
            \sqrt{T}\sigma
        }
$$

$$
\begin{eqnarray*}
    d_{1}(K)^{2}
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right) + (r + \sigma^{2}/2)T
            \right)^{2}
        \\
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right)^{2}
                    + 2\ln\left( \frac{S}{K} \right) (r + \sigma^{2}/2)T
                    + ((r + \sigma^{2}/2)T)^{2}
            \right)
\end{eqnarray*}
$$

$$
    d_{1}^{\prime}(K)
        = \frac{1}{\sqrt{T}\sigma} \frac{K}{S}
$$

$$
    d_{1}^{\prime\prime}(K)
        = \frac{1}{\sqrt{T}\sigma S}
$$

$$
\begin{eqnarray*}
    \phi(d_{1}(K))
        & = &
            \frac{1}{\sqrt{T}\sigma} e^{-\frac{1}{2}d_{2}(K)^{2}}
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \exp
            \left(
                -\frac{1}{2T\sigma^{2}}
                \left(
                    \ln\left( \frac{S}{K} \right)^{2}
                        + 2\ln\left( \frac{S}{K} \right) (r + \sigma^{2}/2)T
                        + ((r + \sigma^{2}/2)T)^{2}
                \right)
            \right)
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \exp
                    \left[
                        \ln\left( \frac{S}{K} \right)
                    \right]
                \right)^{ -\frac{1}{2T\sigma^{2}} \ln\left( \frac{S}{K} \right)}
                \left(
                    \exp
                    \left[
                        \ln\left( \frac{S}{K} \right) 
                    \right]
                \right)^{-\frac{1}{T\sigma^{2}} (r + \sigma^{2}/2)T}
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2)^{2}T
                \right]
            \right)
            \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{ -\frac{1}{2T\sigma^{2}} \ln\left( \frac{S}{K} \right)}
                \left(
                    \frac{S}{K}
                \right)^{-\frac{1}{T\sigma^{2}} (r + \sigma^{2}/2)T}
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2)^{2}T
                \right]
            \right)
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} \ln\left( \frac{S}{K} \right)
                    -\frac{1}{T\sigma^{2}} (r + \sigma^{2}/2)T
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2)^{2}T
                \right]
            \right)
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} 
                    \left(
                        \ln\left( \frac{S}{K} \right)
                        + 2(r + \sigma^{2}/2)T
                    \right)
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2)^{2}T
                \right]
            \right)
\end{eqnarray*}
$$

$d_{2}$の微分を考える。

$$
    d_{2}(K)
        := \frac{
           \frac{S}{K} - (r + \sigma^{2}/2)T
        }{
            \sqrt{T}\sigma
        }
$$

$$
\begin{eqnarray*}
    d_{2}(K)^{2}
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right) + (r - \sigma^{2}/2)T
            \right)^{2}
        \\
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right)^{2}
                    + 2\ln\left( \frac{S}{K} \right) (r - \sigma^{2}/2)T
                    + ((r - \sigma^{2}/2)T)^{2}
            \right)
\end{eqnarray*}
$$

$$
    d_{2}^{\prime}(K)
        = \frac{1}{\sqrt{T}\sigma} \frac{K}{S}
$$

$$
    d_{2}^{\prime\prime}(K)
        = \frac{1}{\sqrt{T}\sigma S}
$$


$$
\begin{eqnarray*}
    \phi(d_{2}(K))
        & = &
            \frac{1}{\sqrt{T}\sigma} e^{-\frac{1}{2}d_{2}(K)^{2}}
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \exp
            \left(
                -\frac{1}{2T\sigma^{2}}
                \left(
                    \ln\left( \frac{S}{K} \right)^{2}
                        + 2\ln\left( \frac{S}{K} \right) (r - \sigma^{2}/2)T
                        + ((r - \sigma^{2}/2)T)^{2}
                \right)
            \right)
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \exp
                    \left[
                        \ln\left( \frac{S}{K} \right)
                    \right]
                \right)^{ -\frac{1}{2T\sigma^{2}} \ln\left( \frac{S}{K} \right)}
                \left(
                    \exp
                    \left[
                        \ln\left( \frac{S}{K} \right) 
                    \right]
                \right)^{-\frac{1}{\sigma^{2}} (r - \sigma^{2}/2)}
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
                \right]
            \right)
            \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{ -\frac{1}{2T\sigma^{2}} \ln\left( \frac{S}{K} \right)}
                \left(
                    \frac{S}{K}
                \right)^{-\frac{1}{T\sigma^{2}} (r - \sigma^{2}/2)T}
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
                \right]
            \right)
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} \ln\left( \frac{S}{K} \right)
                    -\frac{1}{T\sigma^{2}} (r - \sigma^{2}/2)T
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
                \right]
            \right)
        \\
        & = &
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} 
                    \left(
                        \ln\left( \frac{S}{K} \right)
                        + 2(r - \sigma^{2}/2)T
                    \right)
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
                \right]
            \right)
\end{eqnarray*}
$$

$$
\begin{eqnarray*}
    \phi^{\prime}(x)
        & = & 
\end{eqnarray*}
$$


$$
    \Phi(x) := 
        \frac{1}{\sqrt{2\pi}}
            \int_{-\infty}^{x} e^{-x^{2}/2}\ dx
$$

$$
\begin{eqnarray*}
    \frac{d}{d K} \Phi(d_{1}(K))
        & = & \phi(d_{1}(K)) d_{1}^{\prime}(K)
        \\
        & = & 
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} 
                    \left(
                        \ln\left( \frac{S}{K} \right)
                        + 2(r + \sigma^{2}/2)T
                    \right)
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2))^{2}T
                \right]
            \right)
            \frac{1}{\sqrt{T}\sigma} \left(\frac{K}{S}\right)
        \\
        & = &
            \frac{1}{T\sigma^{2}} \left(\frac{S}{K} \right)^{-1}
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} 
                    \left(
                        \ln\left( \frac{S}{K} \right)
                        + 2(r + \sigma^{2}/2)T
                    \right)
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2))^{2}T
                \right]
            \right)
        \\
        & = &
            \frac{1}{T\sigma^{2}} 
            \left(
                \frac{S}{K}
            \right)^{
                -\frac{1}{2T\sigma^{2}} 
                \left(
                    \ln\left( \frac{S}{K} \right)
                    + 2(r + \sigma^{2}/2)T
                    +2T\sigma^{2}
                \right)
            }
            \exp
            \left[
                -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2))^{2}T
            \right]
\end{eqnarray*}
$$


$$
    \Phi(d_{2}(K)) = 
        \frac{1}{\sqrt{2\pi}}
            \int_{-\infty}^{d_{2}(K)} e^{-x^{2}/2}\ dx
$$

$$
\begin{eqnarray*}
    \frac{d}{d K} \Phi(d_{2}(K))
        & = & \phi(d_{2}(K)) d_{2}^{\prime}(K)
        \\
        & = & 
            \frac{1}{\sqrt{T}\sigma} 
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} 
                    \left(
                        \ln\left( \frac{S}{K} \right)
                        + 2(r - \sigma^{2}/2)T
                    \right)
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
                \right]
            \right)
            \frac{1}{\sqrt{T}\sigma} \left(\frac{K}{S}\right)
        \\
        & = &
            \frac{1}{T\sigma^{2}} \left(\frac{S}{K} \right)^{-1}
            \left(
                \left(
                    \frac{S}{K}
                \right)^{
                    -\frac{1}{2T\sigma^{2}} 
                    \left(
                        \ln\left( \frac{S}{K} \right)
                        + 2(r - \sigma^{2}/2)T
                    \right)
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
                \right]
            \right)
        \\
        & = &
            \frac{1}{T\sigma^{2}} 
            \left(
                \frac{S}{K}
            \right)^{
                -\frac{1}{2T\sigma^{2}} 
                \left(
                    \ln\left( \frac{S}{K} \right)
                    + 2(r - \sigma^{2}/2)T
                    +2T\sigma^{2}
                \right)
            }
            \exp
            \left[
                -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
            \right]
\end{eqnarray*}
$$

call option $c(0, S(0); T, K)$の微分を考える。
$S := S(0)$とおく。 

$$
    c(0, S; T, K)
        = S\Phi(d_{1}(K)) - K\Phi(d_{2}(K))
$$

$$
\begin{eqnarray*}
    \frac{\partial}{\partial K} c(0, S; T, K)
        & = & 
            S\phi(d_{1}(K))d_{1}^{\prime}(K) - \Phi(d_{2}(K)) - K\phi(d_{2}(K))d_{2}^{\prime}(K)
        \\
        & = &
            S \frac{1}{T\sigma^{2}} 
            \left(
                \frac{S}{K}
            \right)^{
                -\frac{1}{2T\sigma^{2}} 
                \left(
                    \ln\left( \frac{S}{K} \right)
                    + 2(r + \sigma^{2}/2)T
                    +2T\sigma^{2}
                \right)
            }
            \exp
            \left[
                -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2))^{2}T
            \right]
        \\
        & & 
            - K \frac{1}{T\sigma^{2}} 
            \left(
                \frac{S}{K}
            \right)^{
                -\frac{1}{2T\sigma^{2}} 
                \left(
                    \ln\left( \frac{S}{K} \right)
                    + 2(r - \sigma^{2}/2)T
                    +2T\sigma^{2}
                \right)
            }
            \exp
            \left[
                -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
            \right]
            - \Phi(d_{2}(K))
        \\
        & = &
            \frac{1}{T\sigma^{2}} 
            \left(
                \frac{S}{K}
            \right)^{
                -\frac{1}{2T\sigma^{2}} 
                \left(
                    \ln\left( \frac{S}{K} \right)
                    +2T\sigma^{2}
                \right)
            }
            \left(
                S \left(
                    \frac{S}{K}
                \right)^{
                    2(r + \sigma^{2}/2)T
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r + \sigma^{2}/2)^{2}T
                \right]
                - K \left(
                    \frac{S}{K}
                \right)^{
                    2(r - \sigma^{2}/2)T
                }
                \exp
                \left[
                    -\frac{1}{2\sigma^{2}} (r - \sigma^{2}/2)^{2}T
                \right]
            \right)
            - \Phi(d_{2}(K))
\end{eqnarray*}
$$

$d^{\prime}(K) := d_{1}^{\prime}(K) = d_{2}^{\prime}(K)$と$d^{\prime\prime} := d_{2}^{\prime\prime}(K) = d_{2}^{\prime\prime}(K)$とする。

$$
\begin{eqnarray*}
    \frac{\partial^{2}}{\partial K^{2}} c(0, S; T, K)
        & = & 
            S\phi^{\prime}(d_{1}(K))(d_{1}^{\prime}(K))^{2} 
                + S\phi(d_{1}(K))d_{1}^{\prime\prime}(K)
                - \phi(d_{2}(K))d_{2}^{\prime}(K)
                - \phi(d_{2}(K))d_{2}^{\prime}(K)
                - K\phi^{\prime}(d_{2}(K))(d_{2}^{\prime}(K))^{2}
                - K\phi(d_{2}(K))d_{2}^{\prime\prime}(K))
        \\
        & = & 
            S\phi^{\prime}(d_{1}(K))(d^{\prime}(K))^{2} 
                + S\phi(d_{1}(K))d^{\prime\prime}
                - 2\phi(d_{2}(K))d^{\prime}(K)
                - K\phi^{\prime}(d_{2}(K))(d^{\prime}(K))^{2}
                - K\phi(d_{2}(K))d^{\prime\prime}
        \\
        & = & 
            (d^{\prime}(K))^{2} 
                (S\phi^{\prime}(d_{1}(K)) - K\phi^{\prime}(d_{2}(K)))
            + d^{\prime\prime}
                (S\phi(d_{1}(K)) - K\phi(d_{2}(K)))
            - 2\phi(d_{2}(K))d^{\prime}(K)
\end{eqnarray*}
$$
