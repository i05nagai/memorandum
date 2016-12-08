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
Haganは、SABR modelのimplied volatilityを近似して求めた。

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



# Reference

