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
