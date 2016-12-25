---
layout: math
title: "A note on a simple, accurate formula to compute implied standard deviations"
---

# Citation
Corrado, C. J., & Miller, T. W. (1996). A note on a simple, accurate formula to compute implied standard deviations. Journal of Banking & Finance, 20(1996), 595–603. https://doi.org/10.1016/0378-4266(95)00014-3

# Summary
black formulaのimplied volatilityの近似について述べている。
QuantLibではimplied volatilityを求める際の初期値として用いている。

# Abstraction

# 1. Introduction

$$
\begin{eqnarray}
    c(S, r, T, \sigma; K)
        & := & S\Phi(d_{1}) - e^{-rT}K\Phi(d_{2}),
    \\
    d_{1} 
        & := &
            \frac{
                \ln\left(\frac{S}{K} \right) + (r + \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            },
    \\
    d_{2}
        & := & 
            \frac{
                \ln\left(\frac{S}{K} \right) + (r - \frac{1}{2}\sigma^{2})T
            }{
                \sigma \sqrt{T}
            }
\end{eqnarray}
$$

Brenner and Subrahmanyam (1988) では、株式市場において以下の式で近似を与えた。　
Feinstein (1989)も独立に同様の結果を得ている。

$$
\begin{equation}
    \sigma \sqrt{T}
        = \sqrt{2} \pi
            \frac{C}{S}.
    \label{brenner_subrahmanyam_formula}
\end{equation}
$$

ここで、$C$はオプションの価格で、$S$は割り引かれた原資産価格である。

* comoditiy
    * $S := Me^(b - r)T$
* futures
    * $S := F e^{-rT}$

上記の近似は、ATMという仮定をおいた近似である。
この論文では、一般にATMでない場合のimplied volatilityの近似を与える。
また今回与える近似式は、ATMの場合に近似式がBrenner and Subrahmanyam (1988)の式と一致する。

# 2. Quadratic approximations

$$
\begin{equation}
    \Phi(z)
        := 
            \frac{1}{2}
                + \frac{1}{\sqrt{2\pi}}
                    \left(
                        z
                            - \frac{z^{3}}{6}
                            + \frac{z^{5}}{40}
                            + \ldots
                    \right).
    \label{03_approximation_normal_distribution}
\end{equation}
$$

$d_{1}, d_{2}$を代入し、black formulaに適用し、3次とそれ以降の項を無視すると以下を得る。

$$
\begin{equation}
    C \approx S
        \left(
            \frac{1}{2}
                + \frac{d}{\sqrt{2 \pi}}
        \right)
        - X
        \left(
            \frac{1}{2}
                + \frac{d_{2}}{\sqrt{2\pi}}
        \right).
    \label{04_approximate_black_scholes_formula}
\end{equation}
$$

ここで、簡単のため$X := K e^{-rT}$とおいた。
$d_{2} = d_{1} - \sigma \sqrt{T}$に注意し、式を整理すると$\sigma$についての以下の2次方程式を得る。

$$
\begin{equation}
    \sigma^{2} T(S + X)
        - \sigma \sqrt{T} \sqrt{8\pi}
            \left(
                C - \frac{S - X}{2}
            \right)
        + 2(S - X) \ln( \frac{S}{X} ) 
        = 0
    \label{05_implied_vol_quadratic_equation}
\end{equation}
$$

$$\eqref{05_implied_vol_quadratic_equation}$$の解は全て非負である。
解の最大値は以下で与えられる。

$$
\begin{eqnarray}
    \sigma \sqrt{T}
        & = &
            \sqrt{2 \pi}
                \left(
                    \frac{
                        C - \frac{S - X}{2}
                    }{
                        S + X
                    }
                \right)
        \nonumber
        \\
        &  &
            + \sqrt{
                2 \pi
                \left(
                    \frac{
                        C - \frac{S - X}{2}
                    }{
                        S + X
                    }
                \right)^{2}
                -
                \frac{
                    2(S - X)\ln(S/X)
                }{
                    S + X
                }
            }.
    \label{06_largest_solution_of_quadratic_equation}
\end{eqnarray}
$$

$$\eqref{06_largest_solution_of_quadratic_equation}$$は、ATMのときBrenner-Subrahmanyamの公式に一致する解である。
しかし、もう一方の解は一致しない。
よって、経済的に正しい解は$$\eqref{06_largest_solution_of_quadratic_equation}$$である。

$$\eqref{06_largest_solution_of_quadratic_equation}$$の精度は次で述べるように凹性をを減らすことで、改善することができる。
議論を簡単にする為に、$\ln(S/X) \approx 2 (S- X) / (S + X)$とし、代入する。
また、第二項の平方根に含まれる2番目の項に現れる定数4を$\alpha$としパラメータとする。

$$
\begin{eqnarray}
    \sigma \sqrt{T}
        & = &
            \sqrt{2 \pi}
                \left(
                    \frac{
                        C - \frac{S - X}{2}
                    }{
                        S + X
                    }
                \right)
        \nonumber
        \\
        &  &
            + \sqrt{
                2 \pi
                \left(
                    \frac{
                        C - \frac{S - X}{2}
                    }{
                        S + X
                    }
                \right)^{2}
                -
                \alpha
                \left(
                    \frac{ S - X }{ S + X }
                \right)^{2}
            }.
    \label{07_largest_solution_of_quadratic_equation_parametric_form}
\end{eqnarray}
$$

$$\eqref{07_largest_solution_of_quadratic_equation_parametric_form}$$は、ATMのとき$\alpha$に無関係にBrenner-Subrahmanyamの式に一致する。
よって、$\alpha$をATMでの精度に影響を与えることのない、凹性を減らすためのパラメータとして利用する。
$\alpha$をATMの近傍で線形に近似するような値として選ぶ。
$C$を原資産の関数とし、ATMで$$\eqref{07_largest_solution_of_quadratic_equation_parametric_form}$$を原資産価格$S$について2階微分する。
2階微分を0とおき、$\alpha$について解くと以下を得る。

$$
\begin{equation}
    \alpha =
        \frac{ 4 \pi C }{ \sigma \sqrt{T} S }
            \phi( \frac{ \sigma \sqrt{T} }{2})
            + \pi( \Phi( \frac{ \sigma \sqrt{T}}{2} ) - \frac{1}{2})^{2}
\end{equation}
$$

ここで、$\phi(\cdot)$は標準正規分布の密度関数である。
$$\eqref{brenner_subrahmanyam_formula}$$を代入すると、以下を得る。

$$
\begin{equation}
    \alpha =
        \sqrt{8 \pi} \phi( \frac{ \sigma \sqrt{T} }{2})
            + \pi( \Phi( \frac{ \sigma \sqrt{T}}{2} ) - \frac{1}{2})^{2}
    \label{09_equation_alpha_simple}
\end{equation}
$$

$$\eqref{09_equation_alpha_simple}$$が現実に近い値をとる場合を考える。
例えば、$\sigma \le 1$, $T \le 1$,とすると、$\alpha \approx 1.88$と2近い値をとる。
簡単のため、$\alpha = 2$としてとり(1.88ではなく）、$$\eqref{09_equation_alpha_simple}$$に当てはめると、以下の2次近似式を得る。

$$
\begin{equation}
    \sigma \sqrt{T}
        =
            \frac{
                \sqrt{2 \pi}
            }{
                S + X
            }
            \left(
                C - \frac{S - X}{2}
                + \sqrt{
                    \left(
                        C - \frac{S - X}{2}
                    \right)^{2}
                    -
                    \frac{(S - X)^{2}}{\pi}
                }
            \right)
    \label{10_implied_volatility_quadratic_formula}
\end{equation}
$$

よくわからんが、$\alpha$は2階微分に現実に近いパラメータを入れて、値を出せば良いということ？

$$\eqref{10_implied_volatility_quadratic_formula}$$が求める近似式となる。




# Reference

