---
layout: math
title: Quanto CMS
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
    * $\Psi^{A}(K) = 1 + \frac{\partial }{\partial K} c(0, S(0); K, T)$
* $\psi^{A}$
    * $S(T)$の密度関数
    * $\psi^{A}(K) = \frac{\partial^{2} }{\partial K^{2}} c(0, S(0); K, T)$


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
        = g(S(0)) \alpha(S(0)) \tilde{\chi}(S(0))
        + \int_{-\infty}^{S(0)} p(0, S(0); k, T) w(k) \ dk
        + \int_{S(0)}^{\infty} c(0, S(0); k, T) w(k) \ dk
$$

ここで、

$$
\begin{eqnarray*}
    w(s) 
        & := & 
            \frac{d^{2} }{d s^{2}} (g(s) \alpha(s) \tilde{\chi}(s))
        \\
        & = &
            g^{\prime\prime}(s)\alpha(s)\tilde{\chi}(s) 
                + g(s)\alpha^{\prime\prime}(s)\tilde{\chi}(s)
                + g(s)\alpha(s)\tilde{\chi}^{\prime\prime}(s)
                + 2g^{\prime}(s)\alpha^{\prime}(s)\tilde{\chi}(s)
                + 2g^{\prime}(s)\alpha(s)\tilde{\chi}^{\prime}(s)
                + 2g(s)\alpha^{\prime}(s)\tilde{\chi}^{\prime}(s)
\end{eqnarray*}
$$


### linear TSR model

linear TSR modelの場合、$\alpha$の微分を考える。

$$
\begin{eqnarray}
    \alpha(s) & := & \alpha_{1}s + \alpha_{2}
    \\
    \alpha^{\prime}(s) & = &\alpha_{1}
    \\
    \alpha^{\prime\prime}(s) & = & 0
\end{eqnarray}
$$

#### call option

$$
\begin{eqnarray*}
    g^{\prime\prime}(s; K)\alpha(s)\tilde{\chi}(s) 
        & = &
            \delta(s - K)\alpha(s)\tilde{\chi}(s),
    \\
    g(s)\alpha^{\prime\prime}(s)\tilde{\chi}(s) 
        & = & 0,
    \\
    g(s)\alpha(s)\tilde{\chi}^{\prime\prime}(s)
        & = &
        (s - K)^{+}  
        (\alpha_{1}s + \alpha_{2})
        \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
               h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right),
    \\
	2g^{\prime}(s)\alpha^{\prime}(s)\tilde{\chi}(s)
        & = & 2 1_{[K, \infty)}(s) \alpha_{1} 
            \exp 
            \left(
                \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right),
    \\
    2g^{\prime}(s)\alpha(s)\tilde{\chi}^{\prime}(s)
        & = & 2 1_{[K, \infty)}(s) 
            (\alpha_{1}s + \alpha_{2})
            \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
    \\ 
    2g(s)\alpha^{\prime}(s)\tilde{\chi}^{\prime}(s)
        & = & 
            2(s - K)^{+} \alpha_{1}
                \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
\end{eqnarray*}
$$

より、

$$
\begin{eqnarray}
    \int_{-\infty}^{S(0)} p(0, S(0); k, T)w(k) \ dk
        & = & 
            p(0, S(0); K, T) \alpha(K) \tilde{\chi}(K)
            \nonumber
            \\
        & &  + 0
            \nonumber
            \\
        & &  + \int_{-\infty}^{S(0)} 
                p(0, S(0); k, T) 
                (k - K)^{+}  
                (\alpha_{1}k + \alpha_{2})
                \rho_{XS}\sigma_{X}\sqrt{T}
                \left(
                    h^{\prime\prime}(k)\tilde{\chi}(k)
                    + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(k)^{2} \tilde{\chi}(k)
                \right)
                \ dk
            \nonumber
            \\
        & &  + \int_{-\infty}^{S(0)} 
                2 \alpha_{1}
                p(0, S(0); k, T) 
                1_{[K, \infty)}(k)
                \exp 
                \left(
                    \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(k))
                        + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
                \right)
                \ dk
            \nonumber
        \\
        & & + \int_{-\infty}^{S(0)} 
                2 (\alpha_{1}k + \alpha_{2})
                p(0, S(0); k, T) 
                1_{[K, \infty)}(k)
                \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(k)\tilde{\chi}(k)
                \ dk
        \nonumber
        \\
        & & + \int_{-\infty}^{S(0)} 
                2(k - K)^{+} \alpha_{1}
                p(0, S(0); k, T) 
                    \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(k)\tilde{\chi}(k)
                \ dk
        \nonumber
\end{eqnarray}
$$

である。
更に、$S(T)$が非負過程(BSなど)とすると、$k < 0$では、$p(0, S(0); k, T) = 0$である。
よって、その場合は


$$
\begin{eqnarray}
    \int_{-\infty}^{S(0)} p(0, S(0); k, T)w(k) \ dk
        & = & 
            p(0, S(0); K, T) \alpha(K) \tilde{\chi}(K)
            \nonumber
            \\
        & &  + 0
            \nonumber
            \\
        & &  + \int_{0}^{S(0)} 
                p(0, S(0); k, T) 
                (k - K)^{+}  
                (\alpha_{1}k + \alpha_{2})
                \rho_{XS}\sigma_{X}\sqrt{T}
                \left(
                    h^{\prime\prime}(k)\tilde{\chi}(k)
                    + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(k)^{2} \tilde{\chi}(k)
                \right)
                \ dk
            \nonumber
            \\
        & &  + \int_{0}^{S(0)} 
                2 \alpha_{1}
                p(0, S(0); k, T) 
                1_{[K, \infty)}(k)
                \exp 
                \left(
                    \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(k))
                        + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
                \right)
                \ dk
            \nonumber
        \\
        & & + \int_{0}^{S(0)} 
                2 (\alpha_{1}k + \alpha_{2})
                p(0, S(0); k, T) 
                1_{[K, \infty)}(k)
                \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(k)\tilde{\chi}(k)
                \ dk
        \nonumber
        \\
        & & + \int_{0}^{S(0)} 
                2(k - K)^{+} \alpha_{1}
                p(0, S(0); k, T) 
                    \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(k)\tilde{\chi}(k)
                \ dk
        \nonumber
\end{eqnarray}
$$

となる。
第三項も同様に計算すると、

$$
\begin{eqnarray}
    \int_{-\infty}^{S(0)} c(0, S(0); k, T)w(k) \ dk
        & = & 
            c(0, S(0); K, T) \alpha(K) \tilde{\chi}(K)
            \nonumber
            \\
        & &  + 0
            \nonumber
            \\
        & &  + \int_{S(0)}^{\infty} 
                c(0, S(0); k, T) 
                (k - K)^{+}  
                (\alpha_{1}k + \alpha_{2})
                \rho_{XS}\sigma_{X}\sqrt{T}
                \left(
                    h^{\prime\prime}(k)\tilde{\chi}(k)
                    + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(k)^{2} \tilde{\chi}(k)
                \right)
                \ dk
            \nonumber
            \\
        & &  + \int_{S(0)}^{\infty} 
                2 \alpha_{1}
                c(0, S(0); k, T) 
                1_{[K, \infty)}(k)
                \exp 
                \left(
                    \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(k))
                        + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
                \right)
                \ dk
            \nonumber
        \\
        & & + \int_{S(0)}^{\infty} 
                2 (\alpha_{1}k + \alpha_{2})
                c(0, S(0); k, T) 
                1_{[K, \infty)}(k)
                \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(k)\tilde{\chi}(k)
                \ dk
        \nonumber
        \\
        & & + \int_{S(0)}^{\infty} 
                2(k - K)^{+} \alpha_{1}
                c(0, S(0); k, T) 
                    \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(k)\tilde{\chi}(k)
                \ dk,
        \nonumber
\end{eqnarray}
$$

#### put option

#### cap floor

### Swap-Yield Model

#### call option

#### put option

#### cap floor

### fundamental calculation

$\tilde{\chi}$の微分を考える。
$h(s) := \Phi^{-1}(\Psi^{A}(s))$とおくと

$$
\begin{eqnarray}
    h(s) & := & \Phi^{-1}(\Psi^{A}(s)),
    \label{def_h}
    \\
    h^{\prime}(s) 
        & = & \frac{1}{\phi(\Phi^{-1}(\Psi^{A}(s)))} \psi^{A}(s)
        = \frac{1}{\phi(h(s))} \psi^{A}(s),
    \label{derivaitve_h}
    \\
    h^{\prime\prime}(s) 
        & = & \frac{
            (\psi^{A})^{\prime}(s) \phi(h(s)) - \psi^{A}(s) \phi^{\prime}(h(s)) h^{\prime}(s)
        }{
            \phi(h(s))^{2}
        } 
    \label{derivaitve2_h}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \tilde{\chi}(s)
        & = & \exp 
            \left(
                \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right),
    \label{forward_fx_diffusion}
    \\
    \tilde{\chi}^{\prime}(s)
        & = & \rho_{XS}\sigma_{X}\sqrt{T}h'(s) \tilde{\chi}(s)
    \label{derivative_forward_fx_diffusion}
    \\
    \tilde{\chi}^{\prime\prime}(s)
        & = & \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
               h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right)
    \label{derivative2_forward_fx_diffusion}
\end{eqnarray}
$$

call optionのとき、$g_{\mathrm{cap}}$の微分を考える。

$$
\begin{eqnarray}
    g_{\mathrm{cap}}(s;K) & := & (s - K)^{+} = \max(s - K, 0),
    \label{def_payoff_cap}
    \\
    g_{\mathrm{cap}}^{\prime}(s; K) & = & 1_{[K, \infty)}(s),
    \label{derivative_payoff_cap_by_strike}
    \\
    g_{\mathrm{cap}}^{\prime\prime}(s; K) & = & \delta(s - K),
    \label{derivative2_payoff_cap_by_strike}
\end{eqnarray}
$$

put(floor) optionのとき、$g_{\mathrm{floor}}$の微分を考える。

$$
\begin{eqnarray}
    g_{\mathrm{floor}}(s; K) 
        & := & (K - s)^{+} = \max(K - s, 0)
    \label{def_payoff_floor}
    \\
    g_{\mathrm{floor}}^{\prime}(s; K) 
        & = & -1_{(-\infty, K]}(s),
    \label{derivative_payoff_floor_by_strike}
    \\
    g_{\mathrm{floor}}^{\prime\prime}(s; K) 
        & = & -\delta(s - K),
    \label{derivative2_payoff_floor_by_strike}
\end{eqnarray}
$$

cap floor optionのとき、$g_{\mathrm{capfloor}}$の微分を考える。

$$
\begin{eqnarray}
    g_{\mathrm{capfloor}}(s; K_{f}, K_{c}) & := & \min(\max(s - K_{f}, 0), K_{c}),
    \label{def_payoff_cap_floor}
    \\
    g_{\mathrm{capfloor}}^{\prime}(s; K_{f}, K_{c}) & = & 1_{[K_{f}, K_{c}]}(s),
    \label{derivaitve_payoff_cap_floor_by_strike}
    \\
    g_{\mathrm{capfloor}}^{\prime\prime}(s; K_{f}, K_{c}) 
        & = & \delta(s - K_{f}) + \delta(K_{c} - s),
    \label{derivaitve2_payoff_cap_floor_by_strike}
\end{eqnarray}
$$

Black Scholesのcall optionの微分を考えるために、$d_{1}$の微分を考える。

$$
\begin{eqnarray}
    d_{1}(K)
        & := & \frac{
           \ln\left(\frac{S}{K}\right) + (r + \sigma^{2}/2)T
        }{
            \sqrt{T}\sigma
        },
    \label{def_d1}
    \\
    d_{1}(K)^{2}
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right) + (r + \sigma^{2}/2)T
            \right)^{2}
        \nonumber
        \\
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right)^{2}
                    + 2\ln\left( \frac{S}{K} \right) (r + \sigma^{2}/2)T
                    + ((r + \sigma^{2}/2)T)^{2}
            \right),
        \label{square_d1}
    \\
    d_{1}^{\prime}(K)
        & = & \frac{1}{\sqrt{T}\sigma} \frac{K}{S},
    \label{derivative_d1}
    \\
    d_{1}^{\prime\prime}(K)
        & = & \frac{1}{\sqrt{T}\sigma S},
    \label{derivative2_d1}
\end{eqnarray}
$$

$d_{2}$の微分を考える。

$$
\begin{eqnarray}
    d_{2}(K)
        & := & \frac{
           \ln\left(\frac{S}{K}\right) - (r + \sigma^{2}/2)T
        }{
            \sqrt{T}\sigma
        },
    \label{def_d2}
    \\
    d_{2}(K)^{2}
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right) + (r - \sigma^{2}/2)T
            \right)^{2}
        \nonumber
        \\
        & = & \frac{1}{T\sigma^{2}} 
            \left(
                \ln\left( \frac{S}{K} \right)^{2}
                    + 2\ln\left( \frac{S}{K} \right) (r - \sigma^{2}/2)T
                    + ((r - \sigma^{2}/2)T)^{2}
            \right),
        \label{square_d2}
    \\
    d_{2}^{\prime}(K)
        & = & \frac{1}{\sqrt{T}\sigma} \frac{K}{S},
    \label{derivative_d2}
    \\
    d_{2}^{\prime\prime}(K)
        & = & \frac{1}{\sqrt{T}\sigma S},
    \label{derivative2_d2}
\end{eqnarray}
$$

$\phi(x)$の微分を考える。

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
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \phi(d_{1}(K))
        & = &
            \frac{1}{\sqrt{T}\sigma} e^{-\frac{1}{2}d_{2}(K)^{2}}
        \nonumber
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
        \nonumber
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
        \nonumber
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
        \nonumber
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
        \nonumber
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
        \label{phi_d1}
\end{eqnarray}
$$


$$
\begin{eqnarray}
    \phi(d_{2}(K))
        & = &
            \frac{1}{\sqrt{T}\sigma} e^{-\frac{1}{2}d_{2}(K)^{2}}
        \nonumber
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
        \nonumber
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
        \nonumber
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
        \nonumber
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
        \nonumber
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
        \label{phi_d2}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \phi^{\prime}(d_{1}(K))
        & = & 
            -d_{1}(K) \phi(d_{1}(K))
        \nonumber
        \\
        & = &
            -
            \frac{
               \ln\left(\frac{S}{K}\right) + (r + \sigma^{2}/2)T
            }{
                \sqrt{T}\sigma
            }
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
        \nonumber
        \\
        & = &
            -
            \frac{
               \ln\left(\frac{S}{K}\right) + (r + \sigma^{2}/2)T
            }{
                T\sigma^{2}
            }
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
        \label{phi_derivative_d1}
\end{eqnarray}
$$

次に$\Phi(x)$の微分を考える。

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
$S(T)$の分布を考える。

$$
    P(S(T) \le x) 
        = P((\Psi^{A})^{-1}(\Phi(\xi_{2})) \le x)
        = P(\xi_{2} \le \Phi^{-1}((\Psi^{A}(x)))
        = \Phi(\Phi^{-1}(\Psi^{A}(x)))
        = \Psi^{A}(x)
$$

$$
    c(0, S; T, K)
        = \mathrm{E}^{A}
        \left[
            (S - K)^{+}
        \right]
        =
        S\Phi(d_{1}(K)) - K\Phi(d_{2}(K))
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
