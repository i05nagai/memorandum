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

### Calculation of numerator

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

$g, \alpha, \tilde{\chi}$の微分は[Appendix](#appendix)で計算している。

### linear TSR model + cap
$\alpha$がlinear annuity mapping functionで、$g$がcapの場合を考える。

$$
\begin{eqnarray}
    g_{\mathrm{cap}}^{\prime\prime}(s; K)\alpha(s)\tilde{\chi}(s) 
        & = &
            \delta(s - K)\alpha(s)\tilde{\chi}(s),
    \\
    g_{\mathrm{cap}}(s; K)\alpha^{\prime\prime}(s)\tilde{\chi}(s) 
        & = & 0,
    \\
    g_{\mathrm{cap}}(s; K)\alpha(s)\tilde{\chi}^{\prime\prime}(s)
        & = &
        (s - K)^{+}  
        (\alpha_{1}s + \alpha_{2})
        \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
               h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right),
    \\
	2g_{\mathrm{cap}}^{\prime}(s; K)\alpha^{\prime}(s)\tilde{\chi}(s)
        & = & 2 1_{[K, \infty)}(s) \alpha_{1} 
            \exp 
            \left(
                \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right),
    \\
    2g_{\mathrm{cap}}^{\prime}(s; K)\alpha(s)\tilde{\chi}^{\prime}(s)
        & = & 2 1_{[K, \infty)}(s) 
            (\alpha_{1}s + \alpha_{2})
            \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
    \\ 
    2g_{\mathrm{cap}}(s; K)\alpha^{\prime}(s)\tilde{\chi}^{\prime}(s)
        & = & 
            2(s - K)^{+} \alpha_{1}
                \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
\end{eqnarray}
$$

より、

$$
\begin{eqnarray}
    \int_{-\infty}^{S(0)} p(0, S(0); k, T)w(k) \ dk
        & = & 
            p(0, S(0); K, T) \alpha(K) \tilde{\chi}(K) 1_{(-\infty, S(0)]}(K)
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
第一項は、積分範囲が行使価格$K$を含んでいれば1となる。

更に、$S(T)$が非負過程(BSなど)とすると、$k < 0$では、$p(0, S(0); k, T) = 0$である。
よって、その場合は

$$
\begin{eqnarray}
    \int_{-\infty}^{S(0)} p(0, S(0); k, T)w(k) \ dk
        & = & 
            p(0, S(0); K, T) \alpha(K) \tilde{\chi}(K)1_{(0, S(0)]}(K)
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
            c(0, S(0); K, T) \alpha(K) \tilde{\chi}(K) 1_{[S(0), \infty)}(K)
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

第一項は、積分範囲が行使価格$K$を含んでいれば1となる。

#### linear TSR model + floor
linear TSR modelにおいて、payoffがfloor(put)型のstochastic weightの計算をする。

$$
\begin{eqnarray*}
    g_{\mathrm{floor}}^{\prime\prime}(s; K)\alpha(s)\tilde{\chi}(s) 
        & = &
            \delta(s - K)\alpha(s)\tilde{\chi}(s),
    \\
    g_{\mathrm{floor}}(s; K)\alpha^{\prime\prime}(s)\tilde{\chi}(s) 
        & = & 0,
    \\
    g_{\mathrm{floor}}(s; K)\alpha(s)\tilde{\chi}^{\prime\prime}(s)
        & = &
        (s - K)^{+}  
        (\alpha_{1}s + \alpha_{2})
        \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
               h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right),
    \\
	2g_{\mathrm{floor}}^{\prime}(s; K)\alpha^{\prime}(s)\tilde{\chi}(s)
        & = & 2 1_{[K, \infty)}(s) \alpha_{1} 
            \exp 
            \left(
                \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right),
    \\
    2g_{\mathrm{floor}}^{\prime}(s; K)\alpha(s)\tilde{\chi}^{\prime}(s)
        & = & 2 1_{[K, \infty)}(s) 
            (\alpha_{1}s + \alpha_{2})
            \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
    \\ 
    2g_{\mathrm{floor}}(s; K)\alpha^{\prime}(s)\tilde{\chi}^{\prime}(s)
        & = & 
            2(s - K)^{+} \alpha_{1}
                \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
\end{eqnarray*}
$$

#### linear TSR model + bull spread

$$
\begin{eqnarray*}
    g_{\mathrm{bullspread}}^{\prime\prime}(s; K_{f}, K_{c})\alpha(s)\tilde{\chi}(s) 
        & = &
            \left(
                \delta(s - K_{f}) + \delta(K_{c} - s)
            \right)
            \alpha(s)\tilde{\chi}(s),
    \\
    g_{\mathrm{bullspread}}(s; K_{f}, K_{c})\alpha^{\prime\prime}(s)\tilde{\chi}(s) 
        & = & 0,
    \\
    g_{\mathrm{bullspread}}(s; K_{f}, K_{c})\alpha(s)\tilde{\chi}^{\prime\prime}(s)
        & = &
        g_{\mathrm{bullspread}}(s; K_{f}, K_{c})
        (\alpha_{1}s + \alpha_{2})
        \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
               h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right),
    \\
	2g_{\mathrm{bullspread}}^{\prime}(s; K_{f}, K_{c})\alpha^{\prime}(s)\tilde{\chi}(s)
        & = & 2 1_{[K_{f}, K_{c}]}(s) \alpha_{1} 
            \exp 
            \left(
                \rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right),
    \\
    2g_{\mathrm{bullspread}}^{\prime}(s; K_{f}, K_{c})\alpha(s)\tilde{\chi}^{\prime}(s)
        & = & 2 1_{[K_{f}, K_{c}]}(s) 
            (\alpha_{1}s + \alpha_{2})
            \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
    \\ 
    2g_{\mathrm{bullspread}}(s; K_{f}, K_{c})\alpha^{\prime}(s)\tilde{\chi}^{\prime}(s)
        & = & 
            2 g_{\mathrm{bullspread}}(s; K_{f}, K_{c}) 
                \alpha_{1}
                \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
\end{eqnarray*}
$$

### Calculation of denominator
分母を計算する。

$$
    \mathrm{E}^{A,d}
    \left[
        \alpha(S(T)) \tilde{\chi}(S(T))
    \right]
        = \alpha(S(0)) \tilde{\chi}(S(0))
        + \int_{-\infty}^{S(0)} p(0, S(0); k, T) w(k) \ dk
        + \int_{S(0)}^{\infty} c(0, S(0); k, T) w(k) \ dk
$$

ここで、

$$
\begin{eqnarray*}
    w(s) 
        & := & 
            \frac{d^{2} }{d s^{2}} (\alpha(s) \tilde{\chi}(s))
        \\
        & = &
            \alpha^{\prime\prime}(s)\tilde{\chi}(s)
                + \alpha(s)\tilde{\chi}^{\prime\prime}(s)
                + 2\alpha^{\prime}(s)\tilde{\chi}^{\prime}(s)
\end{eqnarray*}
$$

$\alpha, \tilde{\chi}$の微分は[Appendix](#appendix)で計算している。
以下では、$\alpha$はTSR modelとして何を選択するのかに依存するので、$\alpha$で分けて計算する。

#### linear TSR model
linear TSR modelの場合を考える。

$$
\begin{eqnarray}
    \alpha^{\prime\prime}(s)\tilde{\chi}(s)
        & = & 0
        \\
    \alpha(s)\tilde{\chi}^{\prime\prime}(s)
        & = &
        (\alpha_{1}s + \alpha_{2})
        \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
               h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right),
        \\
    2\alpha^{\prime}(s)\tilde{\chi}^{\prime}(s)
        & = &
            2\alpha_{1}
            \rho_{XS}\sigma_{X}\sqrt{T}h^{\prime}(s)\tilde{\chi}(s),
\end{eqnarray}
$$

#### swap yield TSR model
TBD.

### Appendix
ここでは、$g, \alpha, \tilde{\chi}$の微分を計算する。

#### payoff $g$の微分
各payoff $g$の微分を考える。

##### cap option
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

##### floor option
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


##### cap-floor (bull spread) option
cap floor optionのとき、$g_{\mathrm{capfloor}}$の微分を考える。

$$
\begin{eqnarray}
    g_{\mathrm{capfloor}}(s; K_{f}, K_{c})
        & := &
            \min(\max(s - K_{f}, 0), K_{c}),
        & = &
            \min((s - K_{f})^{+}, K_{c}),
    \label{def_payoff_cap_floor}
    \\
    g_{\mathrm{capfloor}}^{\prime}(s; K_{f}, K_{c})
        & = &
            1_{[K_{f}, K_{c}]}(s),
    \label{derivaitve_payoff_cap_floor_by_strike}
    \\
    g_{\mathrm{capfloor}}^{\prime\prime}(s; K_{f}, K_{c}) 
        & = &
            \delta(s - K_{f}) + \delta(K_{c} - s),
    \label{derivaitve2_payoff_cap_floor_by_strike}
\end{eqnarray}
$$

#### annuity mapping funciton $\alpha$の微分
annuity mapping function $\alpha$の各modelごとの微分を考える

##### linear TSR model

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

##### swap yield model
TBD.

#### $\chi$の微分

$\tilde{\chi}$の微分を考える。
まず、$h(s) := \Phi^{-1}(\Psi^{A}(s))$とおくと

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
        & = &
            \exp 
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

更に、$\Psi^{A}(s)$の計算をする為に、$S(T)$の分布を考える。

$$
\begin{eqnarray}
    P(S(T) \le x) 
        & = &
            P((\Psi^{A})^{-1}(\Phi(\xi_{2})) \le x)
        \nonumber
        \\
        & = &
            P(\xi_{2} \le \Phi^{-1}((\Psi^{A}(x)))
        \nonumber
        \\
        & = &
            \Phi(\Phi^{-1}(\Psi^{A}(x)))
        \nonumber
        \\
        & = &
            \Psi^{A}(x)
        \nonumber
        \\
        & = &
            1 +
            \frac{1}{A(t)}
            \frac{\partial}{\partial K} V_{\mathrm{payer}}(t; S(t), K, A(t), T, \sigma)
\end{eqnarray}
$$

である。
payer's swaptionの[first derivative]({{ site.baseurl }}/finance/black_scholes#mjx-eqn-first_derivative_of_payers_swaption_with_respect_to_strike), [second derivative]({{ site.baseurl }}/finance/black_scholes#mjx-eqn-second_derivative_of_payers_swaption_with_respect_to_strike), [third derivative]({{ site.baseurl }}/finance/black_scholes#mjx-eqn-third_derivative_of_payers_swaption_with_respect_to_strike)より

$$
\begin{eqnarray}
    V_{\mathrm{payer}}(t; S, K, 1, T, \sigma)
        & = &
            \mathrm{E}^{A}
            \left[
                (S(T) - K)^{+}
            \right],
    \nonumber
    \\
    \Psi^{A}(\tilde{K})
        & = &
            1 + 
            \left.
                \frac{\partial}{\partial K} 
                V_{\mathrm{payer}}(t; S, K, 1, T, \sigma)
            \right|_{K=\tilde{K}}
    \nonumber
    \\
        & = &
            1 - \Phi(d_{2}(\tilde{K})),
    \nonumber
    \\
    \psi^{A}(\tilde{K})
        & = &
            \left.
                \frac{\partial^{2}}{\partial K^{2}}
                V_{\mathrm{payer}}(t; S, K, 1, T, \sigma)
            \right|_{K=\tilde{K}}
    \nonumber
    \\
        & = &
            -\phi(d_{2}(\tilde{K})) d_{2}^{\prime}(\tilde{K}),
    \nonumber
    \\
    (\psi^{A})^{\prime}(\tilde{K})
        & = &
            \left.
                \frac{\partial^{3}}{\partial K^{3}}
                V_{\mathrm{payer}}(t; S, K, 1, T, \sigma)
            \right|_{K=\tilde{K}}
    \nonumber
    \\
    & = &
            -\left(
                \phi^{\prime}(d_{2}(\tilde{K})) (d^{\prime}(\tilde{K}))^{2}
                    + \phi(d_{2}(\tilde{K})) d^{\prime\prime}(\tilde{K})
            \right),
\end{eqnarray}
$$


### Tips
replicationの積分範囲の決め方。
以下はQuantLibの実装より引用。

* 自分で指定する
* atm swaptionのvegaが1%以下になるようなvanilla swaptionのstrike
* 割り引かれていないpayer、reciever swaptionの価格が与えられたしきい値以下になるようなStrike
* ATM volatilityを持つBlack scholes process

### Examples of simple case
ドルCMSを参照する$T$での円払いのQuanto CMSを考える。

* $S^{\$}(T)$
    * ドルのswap rate
* $\beta_{\$}(T)$
    * ドルのrisk neutral measureの下でのnumeraire
* $\beta_{\yen}(T)$
    * 円のrisk neutral measureの下でのnumeraire
* $T_{p}$
    * Quanto CMSのpayment date
* $T$
    * $S(T)$のfixing date
* $Q^{\$}$
    * ドルのrisk neutral measure
* $Q^{\yen}$
    * 円のrisk neutral measure
* $X(t)$
    * 時刻$t$でのDOM=円、FOR=ドル、ドル円のtoday FX[DOM/FOR]
* $X_{T}(t)$
    * 時刻$t$での$T$のドル円のforward FX[DOM/FOR]
* $g(\cdot)$
    * payoff関数
* $A^{\$}$
    * ドルのannuity measure
* $P_{\$}(t, T)$
    * ドルのZero Coupon Bond
* $P_{\yen}(t, T)$
    * 円のZero Coupon Bond

$$
\begin{eqnarray}
    V_{\mathrm{QuantoCMS}}(0)
        := 
        \mathrm{E}_{t}^{\yen}
        \left[
            \frac{\beta_{\yen}(t)}{\beta_{\yen}(T_{p})}
            g(S^{\$}(T))
        \right]
\end{eqnarray}
$$

ここで、

$$
\begin{eqnarray}
    \mathrm{E}_{t}^{\yen}
    \left[
        \frac{dQ^{\$}}{dQ^{\yen}}
    \right]
        & = &
            \frac{
                \frac{\beta_{\yen}(0)}{\beta_{\yen}(t)}
            }{
                \frac{\beta_{\$}(0) X(0)}{\beta_{\$}(t) X(t)}
            }
    \nonumber
    \\
        & = &
            \frac{
                \beta_{\$}(t) X(t)
            }{
                \beta_{\yen}(t) X(0)
            }
\end{eqnarray}
$$

となる。

$$
\begin{eqnarray}
    V_{\mathrm{QuantoCMS}}(t)
        & = &
            \mathrm{E}_{t}^{\yen}
            \left[
                \frac{\beta_{\yen}(t)}{\beta_{\yen}(T_{p})}
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            \mathrm{E}_{t}^{\yen}
            \left[
                \frac{\beta_{\yen}(t)}{\beta_{\yen}(T_{p})}
                \mathrm{E}_{T_{p}}^{\yen}
                \left[
                    \frac{dQ^{\$}}{dQ^{\yen}}
                \right]
                \frac{
                    \beta_{\yen}(T_{p}) X(0)
                }{
                    \beta_{\$}(T_{p}) X(T_{p})
                }
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            \mathrm{E}_{t}^{\yen}
            \left[
                \frac{
                    X(0) \beta_{\yen}(t)
                }{
                    \beta_{\$}(T_{p}) X(T_{p})
                }
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            \mathrm{E}_{t}^{\$}
            \left[
                \frac{
                    X(0) \beta_{\yen}(t) P^{\$}(T_{p}, T_{p})
                }{
                    \beta_{\$}(T_{p}) X_{T_{p}}(T_{p}) P^{\yen}(T_{p}, T_{p})
                }
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            \mathrm{E}_{t}^{\$}
            \left[
                \frac{
                    X(0) \beta_{\yen}(t)
                }{
                    \beta_{\$}(T)
                }
                \mathrm{E}_{T}^{\$}
                \left[
                    \beta_{\$}(T)
                    \frac{
                         P^{\$}(T_{p}, T_{p})
                    }{
                        \beta_{\$}(T_{p}) X_{T_{p}}(T_{p})
                    }
                \right]
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            \mathrm{E}_{t}^{\$}
            \left[
                \frac{
                    X(0) \beta_{\yen}(t)
                }{
                    \beta_{\$}(T)
                }
                \beta_{\$}(T)
                \frac{
                     P^{\$}(T, T_{p})
                }{
                    \beta_{\$}(T) X_{T_{p}}(T)
                }
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            \mathrm{E}_{t}^{\$}
            \left[
                \frac{
                    X(0) \beta_{\yen}(t)
                }{
                    \beta_{\$}(T)
                }
                \frac{
                     P^{\$}(T, T_{p})
                }{
                    X_{T_{p}}(T)
                }
                g(S^{\$}(T))
            \right]
\end{eqnarray}
$$

となる。
更にannuity measureの下では

$$
\begin{eqnarray}
    V_{\mathrm{QuantoCMS}}(t)
        & = &
            \mathrm{E}_{t}^{A^{\$}}
            \left[
                \frac{
                    X(0) \beta_{\yen}(t) A^{\$}(t)
                }{
                    \beta_{\$}(t) A^{\$}(T)
                }
                \frac{
                     P^{\$}(T, T_{p})
                }{
                    X_{T_{p}}(T)
                }
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            \frac{
                X(0) \beta_{\yen}(t) A^{\$}(t)
            }{
                \beta_{\$}(t)
            }
            \mathrm{E}_{t}^{A^{\$}}
            \left[
                \frac{
                     P^{\$}(T, T_{p})
                }{
                    A^{\$}(T)
                }
                \frac{ 1 }{ X_{T_{p}}(T) }
                g(S^{\$}(T))
            \right]
\end{eqnarray}
$$

となる。
特に時刻$t=0$では

$$
\begin{eqnarray}
    V_{\mathrm{QuantoCMS}}(0)
        & = &
            X(0) A^{\$}(0)
            \mathrm{E}^{A^{\$}}
            \left[
                \frac{
                     P^{\$}(T, T_{p})
                }{
                    A^{\$}(T)
                }
                \frac{ 1 }{ X_{T_{p}}(T) }
                g(S^{\$}(T))
            \right]
\end{eqnarray}
$$

となる。
[Andersen and Piterbarg]({{ site.baseurl }}/book/interest_rate_modeling/chap16)と同様の議論で

$$
\begin{eqnarray}
    V_{\mathrm{QuantoCMS}}(0)
        & \approx &
            X(0) A^{\$}(0)
            \mathrm{E}^{A^{\$}}
            \left[
                \alpha(S^{\$}(T))
                \chi(S^{\$}(T))
                g(S^{\$}(T))
            \right]
    \label{dollar_yen_quanto_cms_approx_value_by_replication}
\end{eqnarray}
$$

と近似する。
ここで、

$$
\begin{eqnarray}
    \chi(S^{\$}(T))
        & := &
            \mathrm{E}^{A^{\$}}
            \left[
            \left.
                \frac{1}{X_{T_{p}}(T)}
            \right|
                S^{\$}(T) = s
            \right]
\end{eqnarray}
$$


以下では具体的なモデルを考える。
$X_{T}(t)$が以下で与えられていると

$$
\begin{equation}
    X_{T_{p}}(T) 
        = X(0) e^{\sigma_{X}\sqrt{T}\xi_{1} + m_{X}T},
\end{equation}
$$

その逆数は

$$
\begin{equation}
    \frac{1}{X_{T_{p}}(T)}
        = \frac{1}{X(0)}
            e^{-\sigma_{X}\sqrt{T}\xi_{1} - m_{X}T},
\end{equation}
$$

となる。
上記の下、$chi(\cdot)$を計算すると

$$
\begin{eqnarray*}
    \chi(s)
        & = & 
            \frac{1}{X(0)}
            e^{-m_{X}T} \mathrm{E}^{A,d}
            \left[
                e^{-\sigma_{X}\sqrt{T}\xi_{1}} | \xi_{2} = \Psi^{-1}(\Phi^{A}(s))
            \right]
            \nonumber
            \\
        & = &
            \frac{1}{X(0)}
            e^{-m_{X}T} \hat{\chi}(s),
\end{eqnarray*}
$$

ここで、最後の等式は以下による。

$$
\begin{eqnarray*}
    \mathrm{E}^{A,d}
        \left[
            e^{-\sigma_{X}\sqrt{T}\xi_{1}} | \xi_{2} = x_{2}
        \right]
    & = &
        \frac{1}{\sqrt{2 \pi (1 - \rho^{2})}}
        \int_{-\infty}^{\infty} 
            \exp
            \left(
                \frac{-2 \sigma_{X} \sqrt{T} x_{1}(1 - \rho^{2})}{2(1 - \rho^{2})}
                -
                \frac{
                    (x_{1} - x_{2}\rho)^{2}
                }{
                    2(1 - \rho^{2})
                }
            \right)
        \ dx_{1}
    \\
    & = &
        \frac{1}{\sqrt{2 \pi (1 - \rho^{2})}}
        \int_{-\infty}^{\infty} 
            \exp
            \left(
                \frac{
                    -2 \sigma_{X} \sqrt{T} x_{1}(1 - \rho^{2}) 
                        - x_{1}^{2} 
                        + 2x_{1}x_{2}\rho 
                        - x_{2}^{2}\rho^{2}
                }{
                    2(1 - \rho^{2})
                }
            \right)
        \ dx_{1}
        \\
    & = &
        \frac{1}{\sqrt{2 \pi (1 - \rho^{2})}}
        \int_{-\infty}^{\infty} 
            \exp
            \left(
                \frac{
                    -x_{1}^{2} 
                        - 2 x_{1}(\sigma_{X} \sqrt{T}(1 - \rho^{2}) + x_{2}\rho) 
                        -x_{2}^{2}\rho^{2}
                }{
                    2(1 - \rho^{2})
                }
            \right)
        \ dx_{1}
    \\
    & = &
        \frac{1}{\sqrt{2 \pi (1 - \rho^{2})}}
        \int_{-\infty}^{\infty} 
            \exp
            \left(
                \frac{
                    -(x_{1} - (-\sigma_{X} \sqrt{T}(1 - \rho^{2}) + x_{2}\rho))^{2}
                    +(-\sigma_{X} \sqrt{T}(1 - \rho^{2}) + x_{2}\rho)^{2}
                    -x_{2}^{2}\rho^{2}
                }{
                    2(1 - \rho^{2})
                }
            \right)
        \ dx_{1}
    \\
    & = &
        \frac{1}{\sqrt{2 \pi (1 - \rho^{2})}}
        \int_{-\infty}^{\infty} 
            \exp
            \left(
                \frac{
                    -(x_{1} - (-\sigma_{X} \sqrt{T}(1 - \rho^{2}) + x_{2}\rho))^{2}
                    \sigma_{X}^{2} T(1 - \rho^{2})^{2} 
                    - 2\sigma_{X} \sqrt{T} (1 - \rho^{2})x_{2}\rho
                    + x_{2}^{2}\rho^{2}
                    -x_{2}^{2}\rho^{2}
                }{
                    2(1 - \rho^{2})
                }
            \right)
        \ dx_{1}
    \\
    & = &
        \frac{1}{\sqrt{2 \pi (1 - \rho^{2})}}
        \int_{-\infty}^{\infty} 
            \exp
            \left(
                \frac{1}{2} \sigma_{X}^{2} T(1 - \rho^{2})
                - \sigma_{X} \sqrt{T} x_{2}\rho
            \right)
            \exp
            \left(
                \frac{
                    -(x_{1} - (\sigma_{X} \sqrt{T}(1 - \rho^{2}) + x_{2}\rho))^{2}
                }{
                    2(1 - \rho^{2})
                }
            \right)
        \ dx_{1}
    \\
    & = &
        \exp
        \left(
            \frac{1}{2} \sigma_{X}^{2} T(1 - \rho^{2})
            - \sigma_{X} \sqrt{T} x_{2}\rho
        \right).
\end{eqnarray*}
$$

ここで、

$$
\begin{eqnarray}
    \frac{1}{X_{T_{p}}(0)}
        & = &
            \mathrm{E}^{T_{p},d}
            \left[
                \frac{1}{X_{T_{p}}(T)}
            \right]
        \nonumber
        \\
        & = &
            \frac{A^{\$}(0)}{P_{\$}(0,T_{p})}
            \mathrm{E}^{A^{\$}}
            \left[
                \frac{P_{\$}(T, T_{p})}{A^{\$}(T)}
                \frac{1}{X_{T_{p}}(T)}
            \right]
        \nonumber
        \\
        & = &
            \frac{A^{\$}(0)}{P_{\$}(0,T_{p})}
            \mathrm{E}^{A^{\$}}
            \left[
                \alpha(S^{\$}(T))
                \chi(S^{\$}(T))
            \right]
        \nonumber
        \\
        & = &
            \frac{A^{\$}(0)}{P_{\$}(0,T_{p})}
            \frac{1}{X(0)}
            e^{-m_{X}T}
            \mathrm{E}^{A^{\$}}
            \left[
                \alpha(S^{\$}(T))
                \hat{\chi}(S^{\$}(T))
            \right].
\end{eqnarray}
$$

よって、

$$
\begin{eqnarray}
    e^{-m_{X}T}
        & = &
            \frac{P_{\$}(0,T_{p})}{A^{\$}(0)}
            \frac{X(0)}{X_{T_{p}}(0)}
            \frac{
                1
            }{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \hat{\chi}(S^{\$}(T))
                \right]
            }
    \label{dollar_yen_quanto_cms_forward_fx}
\end{eqnarray}
$$

$$\eqref{dollar_yen_quanto_cms_forward_fx}$$と$$\eqref{dollar_yen_quanto_cms_approx_value_by_replication}$$と

$$
\begin{eqnarray}
    V_{\mathrm{QuantoCMS}}(0)
        & \approx &
            X(0) A^{\$}(0)
            \frac{1}{X(0)}
            e^{-m_{X}T} 
            \mathrm{E}^{A^{\$}}
            \left[
                \alpha(S^{\$}(T))
                \hat{\chi}(S^{\$}(T))
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            A^{\$}(0)
            \frac{P_{\$}(0,T_{p})}{A^{\$}(0)}
            \frac{X(0)}{X_{T_{p}}(0)}
            \frac{
                1
            }{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \hat{\chi}(S^{\$}(T))
                \right]
            }
            \mathrm{E}^{A^{\$}}
            \left[
                \alpha(S^{\$}(T))
                \hat{\chi}(S^{\$}(T))
                g(S^{\$}(T))
            \right]
    \nonumber
    \\
        & = &
            P_{\$}(0,T_{p})
            \frac{X(0)}{X_{T_{p}}(0)}
            \frac{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \hat{\chi}(S^{\$}(T))
                    g(S^{\$}(T))
                \right]
            }{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \hat{\chi}(S^{\$}(T))
                \right]
            }
    \nonumber
    \\
        & = &
            P_{\yen}(0,T_{p})
            \frac{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \hat{\chi}(S^{\$}(T))
                    g(S^{\$}(T))
                \right]
            }{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \hat{\chi}(S^{\$}(T))
                \right]
            }
\end{eqnarray}
$$

また、$\chi(\cdot)$の微分を計算すると、

$$
\begin{eqnarray}
    \tilde{\chi}(s)
        & = & \exp 
            \left(
                -\rho_{XS}\sigma_{X}\sqrt{T}\Phi^{-1}(\Psi^{A}(s))
                    + \frac{\sigma_{X}^{2}T}{2}(1 - \rho_{XS}^{2})
            \right),
    \label{dollar_yen_quanto_cms_forward_fx_diffusion}
    \\
    \tilde{\chi}^{\prime}(s)
        & = & 
        -\rho_{XS}\sigma_{X}\sqrt{T}h'(s) \tilde{\chi}(s)
    \label{dollar_yen_quanto_cms_derivative_forward_fx_diffusion}
    \\
    \tilde{\chi}^{\prime\prime}(s)
        & = &
        \rho_{XS}\sigma_{X}\sqrt{T}
        \left(
            -h^{\prime\prime}(s)\tilde{\chi}(s)
            + \rho_{XS}\sigma_{X}\sqrt{T} h^{\prime}(s)^{2} \tilde{\chi}(s)
        \right)
    \label{dollar_yen_quanto_cms_derivative2_forward_fx_diffusion}
\end{eqnarray}
$$

となる。

### Analysis
linear TSR modelで$\alpha_{0} = 0$かつ$\rho=0$の特別な場合を考える。

$$
\begin{eqnarray}
    V_{\mathrm{QuantoCMS}}(0)
        & \approx &
            P_{\yen}(0,T_{p})
            \frac{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \exp
                    \left(
                        \frac{1}{2} \sigma_{X}^{2}T
                    \right)
                    g(S^{\$}(T))
                \right]
            }{
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha(S^{\$}(T))
                    \exp
                    \left(
                        \frac{1}{2} \sigma_{X}^{2}T
                    \right)
                \right]
            }
    \nonumber
    \\
        & = &
            P_{\yen}(0,T_{p})
            \frac{
                \alpha_{0}
                \mathrm{E}^{A^{\$}}
                \left[
                    S^{\$}(T)
                    g(S^{\$}(T))
                \right]
                +
                \mathrm{E}^{A^{\$}}
                \left[
                    \alpha_{1}
                    g(S^{\$}(T))
                \right]
            }{
                \alpha_{0}S^{\$}(0)
                + \alpha_{1}
            }
    \nonumber
    \\
        & = &
            P_{\yen}(0,T_{p})
            \mathrm{E}^{A^{\$}}
            \left[
                g(S^{\$}(T))
            \right]
\end{eqnarray}
$$

となる。
replication methodで計算される2階微分を考えると

$$
\begin{eqnarray}
    \alpha^{\prime\prime}(S^{\$}(T)) g(S^{\$}(T))
        & = &
            0
    \nonumber
    \\
    2\alpha^{\prime}(S^{\$}(T)) g^{\prime}(S^{\$}(T))
        & = &
            \alpha_{0} g^{\prime}(S^{\$}(T))
    \nonumber
    \\
    \alpha(S^{\$}(T)) g^{\prime\prime}(S^{\$}(T))
        & = &
            \alpha(S^{\$}(T)) g^{\prime\prime}(S^{\$}(T))
\end{eqnarray}
$$

更にpayoff関数がstrike $K$のcall optionの場合は、

$$
\begin{eqnarray}
    2\alpha^{\prime}(S^{\$}(T)) g^{\prime}(S^{\$}(T))
        & = &
            \alpha_{0} 1_{[K, \infty)}(S^{\$}(T))
    \nonumber
    \\
    \alpha(S^{\$}(T)) g^{\prime\prime}(S^{\$}(T))
        & = &
            \alpha(S^{\$}(T)) \delta(S^{\$}(T) - K)
\end{eqnarray}
$$

となり、payoff関数が$K_{\mathrm{lower}}, K_{\mathrm{upper}}$をstrikeとするbull-spreadの場合は

$$
\begin{eqnarray}
    2\alpha^{\prime}(S^{\$}(T)) g^{\prime}(S^{\$}(T))
        & = &
            \alpha_{0} 1_{[K_{\mathrm{lower}}, K_{\mathrm{upper}})}(S^{\$}(T))
    \nonumber
    \\
    \alpha(S^{\$}(T)) g^{\prime\prime}(S^{\$}(T))
        & = &{
            \alpha(S^{\$}(T))(\delta(S^{\$}(T) - K_{\mathrm{lower} - \delta{})
\end{eqnarray}
$$

となる。
