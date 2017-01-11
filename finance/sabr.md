---
layout: math
title: SABR model
---

# Intoroduction
以下のSDEをもつものをSABR modelと呼ぶ。

$$
\begin{eqnarray}
    S(t) 
        & = & S(0) + \int_{0}^{t} \alpha(s) S(s)^{\beta} dW_{1}(s),
    \\
    \alpha(t) 
        & = & \alpha(0) + \int_{0}^{t} \nu\alpha(s) dW_{2}(s),
    \\
    \langle W_{1}(\cdot), W_{2}(\cdot) \rangle(t)
        & = & \rho t
\end{eqnarray}
$$

微分形で書くと以下のようになる。　

$$
\begin{eqnarray}
    d S(t) 
        & = & \alpha(t)S(t)^{\beta} dW_{1}(t),
    \quad
    S(0) = S_{0},
    \\
    d\alpha(t) 
        & = & \nu \alpha(t) dW_{2}(t),
    \quad
    \alpha(0) = \alpha_{0},
    \\
    dW_{1}(t)dW_{2}(t) 
        & = & \rho dt,
\end{eqnarray}
$$

measure変換した結果マルチンゲールとなる商品について考えることが殆どであるため、drift項は考慮しない。
SABRの名はStochastic Alpha Beta Rhoに由来する。

# Pricing
において、以下の2つが示されている。

* sigular purtabation theoryによるSABR modelのimplied volatility function
* implied volatilityによるcall option（及びput option）の評価

## implied volatility
Haganは、SABR modelのimplied volatilityを以下のように近似して求めた。

$$
\begin{eqnarray}
	\sigma_{B}(K, S; T)
		& \approx &
        \frac{
            \alpha
        }{
            (SK)^{(1-\beta)/2}
            \left(
                1
                + \frac{(1 - \beta)^{2}}{24}
                    \log^{2}\frac{S}{K}
                + \frac{(1 - \beta)^{4}}{1920}
                    \log^{4}\frac{S}{K}
            \right)
        }
        \left(
            \frac{z}{x(z)}
        \right)
        \left[
            1
            +
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{(SK)^{1-\beta}}
                + \frac{1}{4}
                    \frac{\rho\beta\nu\alpha}{(SK)^{(1-\beta)/2}}
                + \frac{2 - 3\rho^{2}}{24}\nu^{2}
            \right) T
        \right],
    \\
    z 
        & := &
        \frac{\nu}{\alpha}
            (SK)^{(1-\beta)/2}
            \log\left( \frac{S}{K} \right),
    \\
    x(z) 
        & := &
            \log
            \left(
                \frac{
                    \sqrt{1 - 2\rho z + z^{2}} + z - \rho
                }{
                    1 - \rho
                }
            \right)
\end{eqnarray}
$$

更にATM($S = K$)の場合には以下のようにかける。

$$
	\sigma_{ATM}(S; T)
		:= \sigma_{B}(S, S; T)
        \approx
        \frac{\alpha}{S^{(1-\beta)}}
        \left[
            1
            + 
            \left(
                \frac{(1-\beta)^{2}}{24}
                    \frac{\alpha^{2}}{S^{2 - 2\beta}}
                + \frac{1}{4}
                    \frac{\rho \beta \alpha \nu}{S^{1-\beta}}
                + \frac{2 - 3\rho^{2}}{24} \nu^{2}
            \right) T
        \right]
$$

## European Option
European call optionの価格は以下であたえられる。

$$
\begin{eqnarray}
    V_{\mathrm{SABR}}(S, K, r, T)
        & := &
        V_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
    \nonumber
    \\
        & = &
        S \Phi(d_{1})
            - Ke^{-rT} \Phi(d_{2})
    \nonumber
    \\
    d_{1}
        & = &
            \frac{
                \ln\left(\frac{S}{K} \right) 
                    + (r + \frac{1}{2}\sigma_{B}(K, S; T)^{2}))T
            }{
                \sigma_{B}(K, S; T) \sqrt{T}
            },
    \nonumber
    \\
    d_{2}
        & := & 
            \frac{
                \ln\left(\frac{S}{K} \right)
                    + (r - \frac{1}{2}\sigma_{B}(K, S; T)^{2})T
            }{
                \sigma_{B}(K, S; T) \sqrt{T}
            }
    \nonumber
\end{eqnarray}
$$

# Greeks
簡単のため、Black Scholes call option formulaのGreeksを以下のようにかく。

$$
\begin{eqnarray}
    \Delta_{\mathrm{BScall}}(S, K, r, T, \sigma)
        & := &
            \frac{\partial}{\partial S}
            V_{\mathrm{BScall}}(S, K, r, T, \sigma)
    \nonumber
    \\
    \Gamma_{\mathrm{BScall}}(S, K, r, T, \sigma)
        & = &
            \frac{\partial^{2}}{\partial S^{2}}
            V_{\mathrm{BScall}}(S, K, r, T, \sigma)
    \nonumber
    \\
    \Theta_{\mathrm{BScall}}(S, K, r, T, \sigma)
        & = &
            \frac{\partial}{\partial T}
            V_{\mathrm{BScall}}(S, K, r, T, \sigma)
    \nonumber
    \\
    \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma)
        & = &
            \frac{\partial}{\partial \sigma}
            V_{\mathrm{BScall}}(S, K, r, T, \sigma)
    \nonumber
    \\
    \mathrm{Volga}_{\mathrm{BScall}}(S, K, r, T, \sigma)
        & = &
            \frac{\partial^{2}}{\partial \sigma^{2}}
            V_{\mathrm{BScall}}(S, K, r, T, \sigma)
    \nonumber
    \\
    \mathrm{Vanna}_{\mathrm{BScall}}(S, K, r, T, \sigma)
        & = &
            \frac{\partial^{2}}{\partial \sigma \partial S}
            V_{\mathrm{BScall}}(S, K, r, T, \sigma)
\end{eqnarray}
$$

以下で見るように、SABR modelの微分はBSのGreeksとimplied volatilityの微分で表現できる。

合成関数の微分より、

$$
\begin{eqnarray}
    \frac{\partial}{\partial S}
    V_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
        & = &
            \left.
                \frac{\partial}{\partial S}
                V_{\mathrm{BScall}}(S, K, r, T, \sigma)
            \right|_{\sigma = \sigma_{B}(K, S; T)}
            + 
            \left.
                \frac{\partial}{\partial \sigma}
                V_{\mathrm{BScall}}(S, K, r, T, \sigma)
            \right|_{\sigma = \sigma_{B}(K, S; T)}
            \frac{\partial}{\partial S}
            \sigma_{B}(K, S; T)
    \nonumber
    \\
        & = &
            \Delta_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            \frac{\partial}{\partial S}
            \sigma_{B}(K, S; T)
\end{eqnarray}
$$

## Delta

$$
\begin{eqnarray}
    \frac{\partial}{\partial S}
    V_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
        & = &
            \Delta_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            \frac{\partial}{\partial S}
            \sigma_{B}(K, S; T)
\end{eqnarray}
$$

## Gamma

$$
\begin{eqnarray}
    \frac{\partial^{2}}{\partial S^{2}}
    V_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
        & = &
            \Gamma_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
    \nonumber
    \\
        & &
            +
            \mathrm{Vanna}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial}{\partial S}
                \sigma_{B}(K, S; T)
    \nonumber
    \\
        & &
            + 
            \left(
                \mathrm{Vanna}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                + 
                \mathrm{Volga}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                    \frac{\partial}{\partial S}
                    \sigma_{B}(K, S; T)
            \right)
                \frac{\partial}{\partial S}
                \sigma_{B}(K, S; T)
    \nonumber
    \\
        & &
            +
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial^{2}}{\partial S^{2}}
                \sigma_{B}(K, S; T)
    \nonumber
    \\
        & = &
            \Gamma_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
    \nonumber
    \\
        & &
            +
            2\mathrm{Vanna}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial}{\partial S}
                \sigma_{B}(K, S; T)
    \nonumber
    \\
        & &
            + 
            \mathrm{Volga}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \left(
                    \frac{\partial}{\partial S}
                    \sigma_{B}(K, S; T)
                \right)^{2}
    \nonumber
    \\
        & &
            +
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial^{2}}{\partial S^{2}}
                \sigma_{B}(K, S; T)
\end{eqnarray}
$$

## Theta

$$
\begin{eqnarray}
    \frac{\partial}{\partial T}
    V_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
        & = &
            \Theta_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            \frac{\partial}{\partial T}
            \sigma_{B}(K, S; T)
\end{eqnarray}
$$

## Vega

$$
\begin{eqnarray}
    \frac{\partial}{\partial \sigma}
    V_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
        & = &
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            \frac{\partial}{\partial \sigma}
            \sigma_{B}(K, S; T)
\end{eqnarray}
$$

## Volga


# Distribution of underlying
call option価格の1階微分及び2階微分はそれぞれ原資産の分布と密度を与える。

$$
    \mathrm{E}
    \left[
        (S(T) - K)^{+}
    \right]
        =
            V_{\mathrm{SABRcall}}(S, K, 1, T)
$$

より、

$$
\begin{eqnarray}
    \Phi_{\mathrm{SABR}}(s) 
        & = &
            1
            +
            \left.
                \frac{\partial}{\partial K}
                V_{\mathrm{SABRcall}}(S, K, 1, T)
            \right|_{K=s}
    \\
    \phi_{\mathrm{SABR}}(s) 
        & = &
            \left.
                \frac{\partial^{2}}{\partial K^{2}}
                V_{\mathrm{SABRcall}}(S, K, 1, T)
            \right|_{K=s}
\end{eqnarray}
$$

を計算すれば良い。
以下では、BS modelでの分布と密度関数を$\Phi_{\mathrm{BS}}(\cdot)$, $\phi_{\mathrm{BS}}(\cdot)$とおく。

$$
\begin{eqnarray}
    \Phi_{\mathrm{BS}}(s; S, T, \sigma)
    & = &
        1
        +
        \left.
            \frac{\partial}{\partial K}
            V_{\mathrm{BScall}}(S, K, 1, T, \sigma)
        \right|_{K=s}
    \nonumber
    \\
    \phi_{\mathrm{BS}}(s; S, T, \sigma)
        & = &
            \left.
                \frac{\partial^{2}}{\partial K^{2}}
                V_{\mathrm{BScall}}(S, K, 1, T, \sigma)
            \right|_{K=s}
\end{eqnarray}
$$

## Distribution
SABR modelの分布を考える。

$$
\begin{eqnarray}
    \frac{\partial}{\partial K}
    V_{\mathrm{SABRcall}}(S, K, 1, T)
        & = &
            \frac{\partial}{\partial K}
            V_{\mathrm{BScall}}(S, K, 1, T, \sigma_{B}(K, S; T))
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial}{\partial K}
                \sigma_{B}(K, S; T)
\end{eqnarray}
$$

より、

$$
\begin{eqnarray}
    \Phi_{\mathrm{SABR}}(s; S, T) 
        & = &
            1
            +
            \left.
                \frac{\partial}{\partial K}
                V_{\mathrm{SABRcall}}(S, K, 1, T)
            \right|_{K=s}
    \nonumber
    \\
        & = &
            \Phi_{\mathrm{BS}}(s; S, T, \sigma_{B}(K, S; T)) 
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, s, r, T, \sigma_{B}(s, S; T))
                \left.
                    \frac{\partial}{\partial K}
                    \sigma_{B}(K, S; T)
                \right|_{K=s}
\end{eqnarray}
$$

また、密度関数は

$$
\begin{eqnarray}
    \frac{\partial^{2}}{\partial K^{2}}
    V_{\mathrm{SABRcall}}(S, K, 1, T)
        & = &
            \frac{\partial^{2}}{\partial K^{2}}
            V_{\mathrm{BScall}}(S, K, 1, T, \sigma_{B}(K, S; T))
    \\
        & &
            +
            \frac{\partial}{\partial K}
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial}{\partial K}
                \sigma_{B}(K, S; T)
    \\
        & &
            + 
            \left(
                \frac{\partial}{\partial K}
                \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                +
                \mathrm{Volga}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                    \frac{\partial}{\partial K}
                    \sigma_{B}(K, S; T)
            \right)
                \frac{\partial}{\partial K}
                \sigma_{B}(K, S; T)
    \\
        & &
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial^{2}}{\partial K^{2}}
                \sigma_{B}(K, S; T)
    \nonumber
    \\
        & = &
            \frac{\partial^{2}}{\partial K^{2}}
            V_{\mathrm{BScall}}(S, K, 1, T, \sigma_{B}(K, S; T))
    \\
        & &
            +
            2
            \frac{\partial}{\partial K}
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial}{\partial K}
                \sigma_{B}(K, S; T)
    \\
        & &
            + 
            \mathrm{Volga}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \left(
                    \frac{\partial}{\partial K}
                    \sigma_{B}(K, S; T)
                \right)^{2}
    \\
        & &
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
                \frac{\partial^{2}}{\partial K^{2}}
                \sigma_{B}(K, S; T)
\end{eqnarray}
$$

以上より、

$$
\begin{eqnarray}
    \phi_{\mathrm{SABR}}(s; S, T) 
        & = &
            \phi_{\mathrm{BS}}(s; S, T, \sigma_{B}(s, S; T)) 
    \\
        & &
            +
            2
            \left.
                \frac{\partial}{\partial K}
                \mathrm{Vega}_{\mathrm{BScall}}(S, K, r, T, \sigma_{B}(K, S; T))
            \right|_{K=s}
            \left.
                    \frac{\partial}{\partial K}
                    \sigma_{B}(K, S; T)
            \right|_{K=s}
    \\
        & &
            + 
            \mathrm{Volga}_{\mathrm{BScall}}(S, s, r, T, \sigma_{B}(s, S; T))
                \left(
                    \left.
                        \frac{\partial}{\partial K}
                        \sigma_{B}(K, S; T)
                    \right|_{K=s}
                \right)^{2}
    \\
        & &
            + 
            \mathrm{Vega}_{\mathrm{BScall}}(S, s, r, T, \sigma_{B}(s, S; T))
                \left.
                    \frac{\partial^{2}}{\partial K^{2}}
                    \sigma_{B}(K, S; T)
                \right|_{K=s}
\end{eqnarray}
$$

# derivative of implied volatility
分布やGreeksの計算でimplied volatilityの微分が必要となる。
以下では、implied volatilityの微分を考える。

## with respect to underlying

## with respect to strike
strikeによる微分を考える。
まず、以下のようにおく。

$$
\begin{eqnarray}
    A_{1}(K, S; T)
        & := &
            (SK)^{(1-\beta)/2}
            \left(
                1
                + \frac{(1 - \beta)^{2}}{24}
                    \log^{2}\frac{S}{K}
                + \frac{(1 - \beta)^{4}}{1920}
                    \log^{4}\frac{S}{K}
            \right)
    \nonumber
    \\
    A_{2}(K, S; T)
        & := &
            z
    \nonumber
    \\
        & = &
        \frac{\nu}{\alpha}
            (SK)^{(1-\beta)/2}
            \log\left( \frac{S}{K} \right),
    \nonumber
    \\
    A_{3}(K, S; T)
        & := &
            x(z)
    \nonumber
    \\
        & = &
            \log
            \left(
                \frac{
                    \sqrt{1 - 2\rho z + z^{2}} + z - \rho
                }{
                    1 - \rho
                }
            \right)
    \nonumber
    \\
    A_{4}(K, S; T)
        & := &
            1
            +
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{(SK)^{1-\beta}}
                + \frac{1}{4}
                    \frac{\rho\beta\nu\alpha}{(SK)^{(1-\beta)/2}}
                + \frac{2 - 3\rho^{2}}{24}\nu^{2}
            \right) T
    \nonumber
    \\
	\sigma_{B}(K, S; T)
        & \approx &
            \frac{
                \alpha
            }{
                A_{1}(K, S; T)
            }
            \frac{A_{2}(K, S; T)}{A_{3}(K, S; T)}
            A_{4}(K, S; T)
\end{eqnarray}
$$

$A_{1}$の微分を考える。
まず、$B_{11} := (SK)^{(1-\beta)/2}$とおく。

$$
\begin{eqnarray}
    \frac{\partial}{\partial K}
        B_{11}
        & = &
            \frac{1 - \beta}{2} S^{(1 - \beta)/2}K^{(-1 - \beta)/2}
    \nonumber
    \\
    \frac{\partial^{2}}{\partial K^{2}}
        B_{11}
        & = &
            \frac{1 - \beta}{2}
                S^{(1 - \beta)/2}
                \frac{-1 - \beta}{2}
                K^{(-3 - \beta)/2}
    \nonumber
    \\
        & = &
            -\frac{1 - \beta^{2}}{4}
                S^{(1 - \beta)/2}
                K^{(-3 - \beta)/2}
    \nonumber
\end{eqnarray}
$$

また、

$$
\begin{eqnarray}
    B_{12}
        & := &
        \left(
            1
            + \frac{(1 - \beta)^{2}}{24}
                \log^{2}\frac{S}{K}
            + \frac{(1 - \beta)^{4}}{1920}
                \log^{4}\frac{S}{K}
        \right)
    \\
    \frac{\partial}{\partial K}
        B_{12}
        & = &
            \frac{(1 - \beta)^{2}}{12}
                \log\left( \frac{S}{K} \right)
                \frac{K}{S}
                (- \frac{S}{K^{2}})
            + \frac{(1 - \beta)^{4}}{480}
                \log^{3}\left( \frac{S}{K} \right)
                \frac{K}{S}
                (- \frac{S}{K^{2}})
    \nonumber
    \\
        & = &
            -\frac{(1 - \beta)^{2}}{12K}
                \log \left( \frac{S}{K} \right)
            - \frac{(1 - \beta)^{4}}{480K}
                \log^{3}\left( \frac{S}{K} \right)
    \nonumber
    \\
    \frac{\partial^{2}}{\partial K^{2}}
        B_{12}
        & = &
            -\frac{(1 - \beta)^{2}}{12K}
                (-\frac{1}{K})
            - \frac{(1 - \beta)^{4}}{480K}
                3
                \log^{2}\left( \frac{S}{K} \right)
                (-\frac{1}{K})
    \nonumber
    \\
        & = &
            \frac{(1 - \beta)^{2}}{12K^{2}}
            + \frac{(1 - \beta)^{4}}{160K^{2}}
                \log^{2}\left( \frac{S}{K} \right)
    \nonumber
\end{eqnarray}
$$

以上より、

$$
\begin{eqnarray}
    \frac{\partial}{\partial K}
        A_{1}(K, S; T) 
        & = &
            A_{11}
                A_{12}^{\prime}
            +
            A_{11}^{\prime}
                A_{12}
    \nonumber
    \\
    \frac{\partial^{2}}{\partial K^{2}}
        A_{1}(K, S; T) 
        & = &
            A_{11}
                A_{12}^{\prime\prime}
            +
            2 A_{11}^{\prime}
                A_{12}^{\prime}
            +
            A_{11}^{\prime\prime}
                A_{12}
\end{eqnarray}
$$

となる。
$A_{2}$の微分を考える。

$$
\begin{eqnarray}
    \frac{\partial }{\partial K}
    A_{2}(K, S; T)
        & = &
        \frac{\nu}{\alpha}
        \left(
            S^{(1-\beta)/2} K^{(-1-\beta)/2} 
            \log\left( \frac{S}{K} \right)
            +
            (SK)^{(1-\beta)/2} 
            \frac{K}{S}
            (-\frac{S}{K^{2}})
        \right)
    \nonumber
    \\
        & = &
        \frac{\nu}{\alpha}
        \left(
            S^{(1-\beta)/2} K^{(-1-\beta)/2} 
            \log\left( \frac{S}{K} \right)
            -
            S^{(1-\beta)/2} 
                K^{(-1-\beta)/2} 
        \right)
    \nonumber
    \\
        & = &
        \frac{\nu}{\alpha}
            S^{(1-\beta)/2}
        \left(
            K^{(-1-\beta)/2} 
                \log\left( \frac{S}{K} \right)
            -
            K^{(-1-\beta)/2} 
        \right)
    \nonumber
    \\
        & = &
        \frac{\nu}{\alpha}
            S^{(1-\beta)/2}
            K^{(-1-\beta)/2} 
        \left(
            \log\left( \frac{S}{K} \right)
            -
            1
        \right)
    \nonumber
    \\
    \frac{\partial^{2} }{\partial K^{2}}
    A_{2}(K, S; T)
        & = &
        \frac{\nu}{\alpha}
            S^{(1-\beta)/2}
        \left(
            \frac{-1-\beta}{2}
                K^{(-3-\beta)/2} 
                \log\left( \frac{S}{K} \right)
            +
            K^{(-1-\beta)/2} 
                (-\frac{1}{K})
            -
            \frac{-1-\beta}{2}
                K^{(-3-\beta)/2} 
        \right)
    \nonumber
    \\
        & = &
        \frac{\nu}{\alpha}
            S^{(1-\beta)/2}
            K^{(-3-\beta)/2} 
            \left(
                \frac{-1-\beta}{2}
                    \log\left( \frac{S}{K} \right)
                - 1
                -
                \frac{-1-\beta}{2}
            \right)
    \nonumber
    \\
        & = &
        \frac{\nu}{\alpha}
            S^{(1-\beta)/2}
            K^{(-3-\beta)/2} 
            \left(
                \frac{-1-\beta}{2}
                    \log\left( \frac{S}{K} \right)
                +
                \frac{-1+\beta}{2}
            \right)
\end{eqnarray}
$$

次に、$A_{3}$の部分を考える。
簡単のため、$A_{3}(K) := A_{3}(K, S; T)$, $A_{2}(K) := A(K, S; T)$と書く。
$A_{2}(K)$の$K$での微分を$A_{2}^{\prime}(K)$とかく。
$A_{2}(K) = z$に注意すると、

$$
\begin{eqnarray}
    A_{31}
        & := &
            \sqrt{1 - 2\rho z + z^{2}} + z - \rho
    \nonumber
    \\
    \frac{\partial }{\partial K}
        A_{31}
        & = &
            \frac{1}{2}
            \frac{
                (-2\rho A_{2}^{\prime}(K) + 2zA_{2}^{\prime}(K))
            }{
                \sqrt{1 - 2\rho z + z^{2}}
            }
            + 1
    \nonumber
    \\
        & = &
            \frac{
                (-\rho A_{2}^{\prime}(K) + zA_{2}^{\prime}(K))
            }{
                \sqrt{1 - 2\rho z + z^{2}}
            }
            + 1
    \nonumber
    \\
    \frac{\partial^{2} }{\partial K^{2}}
        A_{31}
        & = &
            \frac{
                (-\rho A_{2}^{\prime\prime}(K)
                    + A_{2}^{\prime}(K)^{2}
                    + zA_{2}^{\prime\prime}(K))
                    \sqrt{1 - 2\rho z + z^{2}}
                +
                (-\rho A_{2}^{\prime}(K)
                    + zA_{2}^{\prime}(K))
                    \frac{1}{2}
                    (1 - 2\rho z + z^{2})^{-1/2}
                    (-2 \rho A_{2}^{\prime}(K)
                        + 2 z A_{2}^{\prime}(K))
            }{
                1 - 2\rho z + z^{2}
            }
    \nonumber
    \\
        & = &
            \frac{
                (-\rho A_{2}^{\prime\prime}(K)
                    + A_{2}^{\prime}(K)^{2}
                    + zA_{2}^{\prime\prime}(K))
                    (1 - 2\rho z + z^{2})
                +
                (-\rho A_{2}^{\prime}(K)
                    + zA_{2}^{\prime}(K))^{2}
            }{
                (1 - 2\rho z + z^{2})^{3/2}
            }
\end{eqnarray}
$$

以上より、

$$
\begin{eqnarray}
    \frac{\partial }{\partial K}
    A_{3}(K, S; T)
        & = &
            \frac{
                1 - \rho
            }{
                A_{31}
            }
            \frac{\partial}{\partial K}
            \left(
                \frac{
                    A_{31}
                }{
                    1 - \rho
                }
            \right)
    \nonumber
    \\
        & = &
            \frac{ 1 }{ A_{31} }
            \frac{\partial}{\partial K}
            A_{31}
    \nonumber
    \\
    \frac{\partial^{2} }{\partial K^{2}}
    A_{3}(K, S; T)
        & = &
            -A_{31}^{-2}
                \frac{\partial}{\partial K}
                A_{31}
                \frac{\partial}{\partial K}
                A_{31}
            +
            A_{31}^{-1}
                \frac{\partial^{2}}{\partial K^{2}}
                A_{31}
    \nonumber
    \\
        & = &
            -A_{31}^{-2}
            \left(
                \frac{\partial}{\partial K}
                A_{31}
            \right)^{2}
            +
            A_{31}^{-1}
                \frac{\partial^{2}}{\partial K^{2}}
                A_{31}
\end{eqnarray}
$$

となる。
次に、$A_{4}(K, S; T)$の微分を考える。

$$
\begin{eqnarray}
    \frac{\partial}{\partial K}
    A_{4}(K, S; T)
        & = &
            \frac{\partial}{\partial K}
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{S^{1-\beta}}
                    K^{-(1-\beta)}
                + \frac{1}{4}
                    \frac{\rho\beta\nu\alpha}{S^{(1-\beta)/2}}
                    K^{-(1-\beta)/2}
            \right) T
    \nonumber
    \\
        & = &
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{S^{1-\beta}}
                    (\beta - 1)
                    K^{\beta - 2}
                + \frac{1}{4}
                    \frac{\rho\beta\nu\alpha}{S^{(1-\beta)/2}}
                    \frac{(\beta - 1)}{2}
                    K^{(\beta-3)/2}
            \right) T
    \nonumber
    \\
        & = &
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{S^{1-\beta}}
                    K^{\beta - 2}
                + \frac{1}{8}
                    \frac{\rho\beta\nu\alpha}{S^{(1-\beta)/2}}
                    K^{(\beta-3)/2}
            \right) T (\beta - 1)
    \nonumber
    \\
    \frac{\partial^{2}}{\partial K^{2}}
    A_{4}(K, S; T)
        & = &
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{S^{1-\beta}}
                    (\beta - 2)
                    K^{\beta - 3}
                + \frac{1}{8}
                    \frac{\rho\beta\nu\alpha}{S^{(1-\beta)/2}}
                    \frac{\beta - 3}{2}
                    K^{(\beta-5)/2}
            \right) T (\beta - 1)
    \nonumber
    \\
        & = &
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{S^{1-\beta}}
                    (\beta - 2)
                    K^{\beta - 3}
                + \frac{1}{16}
                    \frac{\rho\beta\nu\alpha}{S^{(1-\beta)/2}}
                    (\beta - 3)
                    K^{(\beta-5)/2}
            \right) T (\beta - 1)
\end{eqnarray}
$$

以上より、以下を計算すれば良い。
簡単のため、$A_{i}(K) := A_{i}(K, S; T)$とおく。

$$
\begin{eqnarray}
    \frac{\partial}{\partial K} 
    \alpha
    A_{1}(K)^{-1}
        & = &
            -\alpha
            A_{1}(K)^{-2}
            A_{1}^{\prime}(K)
    \nonumber
    \\
    \frac{\partial^{2}}{\partial K^{2}} 
    \alpha
    A_{1}(K)^{-1}
        & = &
            -\alpha
            (-2
                A_{1}(K)^{-3}
                A_{1}^{\prime}(K)
                A_{1}^{\prime}(K)
            +
            A_{1}(K)^{-2}
                A_{1}^{\prime\prime}(K)
            )
    \nonumber
    \\
    \frac{\partial}{\partial K}
    \frac{A_{2}(K)}{A_{3}(K)}
        & = &
            A_{2}^{\prime}(K)
                A_{3}(K)^{-1}
            -
            A_{2}(K)
                A_{3}^{\prime}(K)
                A_{3}(K)^{-2}
    \nonumber
    \\
    \frac{\partial^{2}}{\partial K^{2}}
    \frac{A_{2}(K)}{A_{3}(K)}
        & = &
            A_{2}^{\prime\prime}(K)
                A_{3}(K)^{-1}
            +
            2
            A_{2}^{\prime}(K)
                (-
                A_{3}(K)^{-2}
                A_{3}^{\prime}(K)
                )
            -
            A_{2}(K)
                (
                A_{3}^{\prime\prime}(K)
                    A_{3}(K)^{-2}
                +
                A_{3}^{\prime}(K)
                    (-2
                    A_{3}(K)^{-3}
                    A_{3}^{\prime}(K)
                    )
                )
    \nonumber
    \\
        & = &
            A_{2}^{\prime\prime}(K)
                A_{3}(K)^{-1}
            -
            2
            A_{2}^{\prime}(K)
                A_{3}(K)^{-2}
                A_{3}^{\prime}(K)
            -
            A_{2}(K)
                (
                A_{3}^{\prime\prime}(K)
                    A_{3}(K)^{-2}
                -2
                A_{3}^{\prime}(K)^{2}
                    A_{3}(K)^{-3}
                )
\end{eqnarray}
$$

以上より、
        
$$
\begin{eqnarray}
    \frac{\partial}{\partial K}
	\sigma_{B}(K, S; T)
    & \approx &
        \alpha
            \frac{\partial}{\partial K}
            A_{1}(K)^{-1}
            A_{2}(K)A_{3}(K)^{-1}
            A_{4}(K)
        +
        \alpha
            A_{1}(K)^{-1}
            \frac{\partial}{\partial K}
            A_{2}(K)A_{3}(K)^{-1}
            A_{4}(K)
        +
        \alpha
            A_{1}(K)^{-1}
            A_{2}(K)A_{3}(K)^{-1}
            \frac{\partial}{\partial K}
            A_{4}(K)
    \\
    \frac{\partial^{2}}{\partial K^{2}}
    \sigma_{B}(K, S; T)
    & \approx &
        \alpha
            \frac{\partial^{2}}{\partial K^{2}}
            A_{1}(K)^{-1}
            A_{2}(K)A_{3}(K)^{-1}
            A_{4}(K)
        +
        \alpha
            A_{1}(K)^{-1}
            \frac{\partial^{2}}{\partial K^{2}}
            A_{2}(K)A_{3}(K)^{-1}
            A_{4}(K)
        +
        \alpha
            A_{1}(K)^{-1}
            A_{2}(K)A_{3}(K)^{-1}
            \frac{\partial^{2}}{\partial K^{2}}
            A_{4}(K)
    \nonumber
    \\
        &  &
        +
        2 \alpha
            \frac{\partial}{\partial K}
            A_{1}(K)^{-1}
            \frac{\partial}{\partial K}
            A_{2}(K)A_{3}(K)^{-1}
            A_{4}(K)
        +
        2 \alpha
            \frac{\partial}{\partial K}
            A_{1}(K)^{-1}
            A_{2}(K)A_{3}(K)^{-1}
            \frac{\partial}{\partial K}
            A_{4}(K)
        +
        2 \alpha
            A_{1}(K)^{-1}
            \frac{\partial}{\partial K}
            A_{2}(K)A_{3}(K)^{-1}
            \frac{\partial}{\partial K}
            A_{4}(K)
\end{eqnarray}
$$

を計算すれば良い。



# Reference

