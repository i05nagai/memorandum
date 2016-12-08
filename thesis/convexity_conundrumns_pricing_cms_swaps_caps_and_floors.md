---
layout: math
title: "Convexity Conundrums: Pricing CMS Swaps, Caps, and Floors"
---


# Convexity Conundrums: Pricing CMS Swaps, Caps, and Floors

## 1. Introduction

* $P(t, T)$
    * 満期$T$のZero Coupon Bondの$t$での価値
* $D(T) := P(0, T)$
* $\mathrm{cvg}(t_{\mathrm{st}}, t_{\mathrm{end}}, \mathrm{dcb})$
    * day count conventionがdcbの区間$[t_{\mathrm{st}}, t_{\mathrm{end}}]$のday count fraction

### 1.1 Deal definition
* $t_{0}, \ldots, t_{m}$
    * CMS のCash Flowの日付
* $R_{j}$
    * $N$年のswap rate

CMS capsは各$t_{j} (j = 1, \ldots, m)$で以下の支払いを持つ。

$$
    \delta_{j}(R_{j} - K)^{+},
$$

CMS floorsは各$t_{j} (j = 1, \ldots, m)$で以下の支払いを持つ。

$$
    \delta_{j}(K - R_{j})^{+}
$$

### 1.2. Reference swap
CMS swap, cap. floorの価値は、各$t_{j}$での支払いの期待値の和である。
各時点でのpayoffを計算すれば良いから、以下を$t_{p}$で以下の支払いを持つ取引のみを考える。

$$
\begin{eqnarray}
    g(R) 
        & := & R,
    \\
    g_{\mathrm{cap}}(R) 
        & := & (R - K)^{+},
    \\
    g_{\mathrm{floor}}(R) 
        & := & (K - R)^{+},
\end{eqnarray}
$$

swap rateの$t$での価値はo

$$
    V_{\mathrm{swap}}(t)
        := P(t, s_{0}) - P(t, s_{n}) - R_{\mathrm{fix}} \sum_{j=1}^{n} \alpha_{j}P(t, s_{j})
$$

PV01, DV01, annuityを以下で定義する。

$$
    A(t) := \sum_{j=1}^{n} \alpha_{j}P(t, s_{j})
$$

annuityは1ドルをswapの支払い期間ずつ$N$年間受け取る取引の現在価値である。

$$
\begin{equation}
    V_{\mathrm{swap}}(t) = \frac{S(t) - R_{\mathrm{fix}}}{A(t)}
    \label{1_9_a_value_of_forward_swap_rate}
\end{equation}
$$

ここで、

$$
\begin{equation}
    S(t) = \frac{P(t, s_{0}) - P(t, s_{n})}{A(t)}
    \label{1_9_b_forward_swap_rate}
\end{equation}
$$

$$
\begin{equation}
    A_{0} := A(0)
        = \sum_{j=1}^{n} \alpha_{j} D_{j}
        = \sum_{j=1}^{n} \alpha_{j} P(0, s_{j})
        \label{1_10_a_today_annuity}
\end{equation}
$$

$t=0$での(forward) swap rateは以下でかける。

$$
\begin{equation}
    S(0) = \frac{D_{0} - D_{n}}{A(0)}
    \label{1_10_b_today_swap_rate}
\end{equation}
$$

## 2. Valuation
annuity measureの下での価値は以下のようになる。

$$
\begin{equation}
    V(t)
        := A(t) \mathrm{E}^{A}
        \left[
        \left.
            \frac{V(T)}{A(T)}
        \right|
            \mathcal{F}_{t}
        \right],
    \quad
    \forall T > t,
    \label{2_1_martingale_formula}
\end{equation}
$$

である。
plain vanilla swaptionの価値、特に参照しているswap rateのstandard european optionについて考える。
行使日は、参照しているswapのfixing date$t_{\mathrm{fix}}$で、start date$s_{0}$のspot-lag営業日前である。

$$
    V_{\mathrm{opt}}(t_{\mathrm{fix}}) = (S(t_{\mathrm{fix}}) - R_{\mathrm{fix}})^{+}A(t_{\mathrm{fix}})
$$

martingale formula $\eqref{2_1_martingale_formula}$ より、

$$
\begin{equation}
    V_{\mathrm{opt}}(t)
        = A(t) \mathrm{E}^{A}
            \left[
            \left.
                \frac{V_{\mathrm{opt}}(t_{\mathrm{fix}})}{A(t_{\mathrm{fix}})}
            \right|
                \mathcal{F}_{t}
            \right]
        = A(t) \mathrm{E}^{A}
        \left[
        \left.
            (S(t_{\mathrm{fix}}) - R_{\mathrm{fix}})^{+}
        \right|
            \mathcal{F}_{t}
        \right]
    \label{2_3_value_of_swaption}
\end{equation}
$$

特に、0でのswaptionの価値は

$$
\begin{equation}
    V_{\mathrm{opt}}(0)
        = A(0) \mathrm{E}^{A}
        \left[
        \left.
            (S(t_{\mathrm{fix}}) - R_{\mathrm{fix}})^{+}
        \right|
            \mathcal{F}_{0}
        \right]
        \label{2_4_a_value_of_today_swaption}
\end{equation}
$$

annuity measureの下forward swap rateはマルチンゲールなので

$$
\begin{equation}
    \mathrm{E}^{A}
    \left[
    \left.
        S(t_{\mathrm{fix}})
    \right|
        \mathcal{F}_{0}
    \right]
        = S(0) =: S_{0}
    \label{2_4_b_swap_rate_}
\end{equation}
$$

実際にpricingする為に、forward swap rate$S(t_{\mathrm{fix}})$のmodel(e.g. Black's model, Heston's model, SABR model)を考える。


### 2.1 CMS caplets
$t_{p}$で以下のpayoffを支払うCMS capletを考える。

$$
\begin{equation}
    (S(t_{\mathrm{fix}}) - K)^{+},
    \label{2_6_caplet_payoff}
\end{equation}
$$

$$
\begin{equation}
    V_{\mathrm{CMScap}}(t) 
        = A(t) \mathrm{E}^{A}
        \left[
        \left.
            \frac{
                (S(t_{\mathrm{fix}}) - K)^{+}P(t_{\mathrm{fix}}, t_{p})
            }{
                A(t_{\mathrm{fix}})
            }
        \right|
            \mathcal{F}_{t}
        \right],
    \label{2_7_a_value_of_cms_cap}
\end{equation}
$$

とくに、todayの場合は、

$$
\begin{equation}
    V_{\mathrm{CMScap}}(0) 
        = A(0) \mathrm{E}^{A}
        \left[
        \left.
            \frac{
                (S(t_{\mathrm{fix}}) - K)^{+}P(t_{\mathrm{fix}}, t_{p})
            }{
                A(t_{\mathrm{fix}})
            }
        \right|
            \mathcal{F}_{0}
        \right],
    \label{2_7_b_value_of_today_cms_cap}
\end{equation}
$$

である。
$P(t, t_{p}) / A(t_{\mathrm{fix}})$はマルチンゲールであるから

$$
\begin{eqnarray}
    & &
        \mathrm{E}^{A}
        \left[
        \left.
            \frac{P(t_{\mathrm{fix}}, t_{p})}{A(t_{\mathrm{fix}})}
        \right|
            \mathcal{F}_{0}
        \right]
        = \frac{P(0, t_{p})}{A(0)}
    \label{2_8_annuity}
    \\
    & \iff & 
        \mathrm{E}^{A}
        \left[
        \left.
            \frac{
                \frac{P(t_{\mathrm{fix}}, t_{p})}{A(t_{\mathrm{fix}})}
            }{
                \frac{P(0, t_{p})}{A(0)}      
            }
        \right|
            \mathcal{F}_{0}
        \right]
        = 1
    \nonumber
\end{eqnarray}
$$

である。


$$
\begin{eqnarray}
    V_{\mathrm{CMScap}}(0)
        & = & A(0) \mathrm{E}^{A}
            \left[
            \left.
                \frac{
                    (S(t_{\mathrm{fix}}) - K)^{+}P(t_{\mathrm{fix}}, t_{p})
                }{
                    A(t_{\mathrm{fix}})
                }
            \right|
                \mathcal{F}_{0}
            \right]
        \nonumber
        \\
        & = & P(0, t_{p})
            \mathrm{E}^{A}
            \left[
            \left.
                (S(t_{\mathrm{fix}}) - K)^{+}
                \frac{
                    \frac{P(t_{\mathrm{fix}}, t_{p})}{A(t_{\mathrm{fix}})}
                }{
                    \frac{P(0, t_{p})}{A(0)}
                }
            \right|
                \mathcal{F}_{0}
            \right]
    \label{2_9_value_of_cms_caplet}
    \\
        & = & 
            P(0, t_{p})
            \mathrm{E}^{A}
            \left[
            \left.
                (S(t_{\mathrm{fix}}) - K)^{+}
            \right|
                \mathcal{F}_{0}
            \right]
            - 
            P(0, t_{p})
            \mathrm{E}^{A}
            \left[
            \left.
                (S(t_{\mathrm{fix}}) - K)^{+}
            \right|
                \mathcal{F}_{0}
            \right]
            +
            P(0, t_{p})
            \mathrm{E}^{A}
            \left[
            \left.
                (S(t_{\mathrm{fix}}) - K)^{+}
                \frac{
                    \frac{P(t_{\mathrm{fix}}, t_{p})}{A(t_{\mathrm{fix}})}
                }{
                    \frac{P(0, t_{p})}{A(0)}
                }
            \right|
                \mathcal{F}_{0}
            \right]
    \nonumber
    \\
        & = & 
            P(0, t_{p})
            \mathrm{E}^{A}
            \left[
            \left.
                (S(t_{\mathrm{fix}}) - K)^{+}
            \right|
                \mathcal{F}_{0}
            \right]
            +
            P(0, t_{p})
            \mathrm{E}^{A}
            \left[
            \left.
                (S(t_{\mathrm{fix}}) - K)^{+}
                \left(
                    \frac{
                        \frac{P(t_{\mathrm{fix}}, t_{p})}{A(t_{\mathrm{fix}})}
                    }{
                        \frac{P(0, t_{p})}{A(0)}
                    }
                    - 1
                \right)
            \right|
                \mathcal{F}_{0}
            \right]
        \label{2_10_value_of_today_cms_cap}
\end{eqnarray}
$$

最初の項は、european swaptionの価格である。
第二項はconvexity correctionとよばれる項である。
$\eqref{2_8_annuity}$より、第二項の期待値は0である。

ここで、$P$と$A$の比を$S$の関数として以下のようにmodel化することを考える。

$$
\begin{eqnarray}
    G(S(t_{\mathrm{fix}})) 
        & := & \frac{P(t_{\mathrm{fix}}, t_{p})}{A(t_{\mathrm{fix}})},
   \label{2_11_a_def_annuity_mapping_function} 
   \\
    G(S(0)) 
        & := & \frac{P(0, t_{p})}{A(0)},
   \label{2_11_b_def_annuity_mapping_function} 
\end{eqnarray}
$$

$G$を使うとconvexity correctionは以下で定義できる。

$$
\begin{equation}
    cc := 
        P(0, t_{p})
        \mathrm{E}^{A}
        \left[
        \left.
            (S(t_{\mathrm{fix}}) - K)^{+}
            \left(
                \frac{G(S(t_{\mathrm{fix}}))}{ G(S(0)) } - 1
            \right)
        \right|
            \mathcal{F}_{0}
        \right]
        \label{2_12_der_convexity_correction}
\end{equation}
$$

$G$のstreet-standard modelとして、以下の関数形が知られている。

$$
\begin{equation}
    G(S) 
        := \frac{S(t_{\mathrm{fix}})}{(1 + \frac{S}{q})^{\Delta}}
        \frac{
            1
        }{
            1 - \frac{S(t_{\mathrm{fix}})}{(1 + \frac{S}{q})^{n}}
        }
    \label{2_13_a_annuity_mapping_function}
\end{equation}
$$

ここで、$q$は参照しているswapの1年での支払い回数である。
例えば、swapの支払いがsemi-annualであれば$q=2$で、quarterlyであれば$q=4$である。
$\Delta$は

$$
\begin{equation}
    \Delta := \frac{t_{p} - s_{0}}{s_{1} - s_{0}}
    \label{2_13_b_ratio_of_date}
\end{equation}
$$

として定義する。
$\Delta$は、支払日とstart日が等しいset-in-arreasであれば$\Delta=0$で、end日に支払いをするset-in-advanceであれば、swapの支払い期間に応じてきまる。

$f$をなめらかな関数とすると、$\forall S$について

$$
\begin{eqnarray*}
    f(S) 
        & = & f(K) + \int_{K}^{S} f^{\prime}(x) \ dx
        \\
        & = & f(K) + \int_{K}^{\infty} 1_{(-\infty, S]}(x)f^{\prime}(x) \ dx
        \\
        & = & f(K) 
            - \left[
                (S - x)^{+}f^{\prime}(x) 
            \right]_{K}^{\infty}
            + \int_{K}^{\infty} (S - x)^{+} f^{\prime\prime}(x) \ dx
        \\
        & = & f(K) 
            + (S - K)^{+}f^{\prime}(K) 
            + \int_{K}^{\infty} (S - x)^{+} f^{\prime\prime}(x) \ dx.
\end{eqnarray*}
$$

である。
特に、$S < K$の場合は、第二項、第三項は0になることに注意する。
よって、 $f(K) = 0$を満たすとすると、

$$
\begin{equation}
    (S - K)^{+}f^{\prime}(K) 
    + \int_{K}^{\infty} (S - x)^{+} f^{\prime\prime}(x) \ dx
    = 
       \begin{cases}	
           f(S) & (S > K) \\
           0 & (S < K) 
       \end{cases},
\end{equation}
$$

となる。
ここで、

$$
\begin{eqnarray}
    g_{\mathrm{cap}}(x) 
        & := & (x - K)^{+}
        \left(
            \frac{G(x)}{G(S(0))} - 1
        \right),
    \label{2_15_def_of_payoff}
    \\
    g_{\mathrm{cap}}^{\prime}(x)
        & = &
            1_{[K, \infty)}(x)
            \left(
                \frac{G(x)}{G(S(0))} - 1
            \right)
            + (x - K)^{+}
            \left(
                \frac{G(x)}{G(S(0))} - 1
            \right)^{\prime}
\end{eqnarray}
$$

とおくと、$\eqref{2_12_der_convexity_correction}$に代入すると

$$
\begin{eqnarray}
    cc 
        & = & P(0, t_{p})
            \mathrm{E}
            \left[
            \left.
                g_{\mathrm{cap}}(S(t_{\mathrm{fix}}))
            \right|
                \mathcal{F}_{0}
            \right]
    \nonumber
    \\
        & = & P(0, t_{p})
            \mathrm{E}
            \left[
            \left.
                g_{\mathrm{cap}}^{\prime}(K)(S(t_{\mathrm{fix}}) - K)^{+}
                + \int_{K}^{\infty} (S(t_{\mathrm{fix}}) - x)^{+}g_{\mathrm{cap}}^{\prime\prime}(x)\ dx
            \right|
                \mathcal{F}_{0}
            \right]
    \nonumber
    \\
        & = & P(0, t_{p})
            \left(
                g_{\mathrm{cap}}^{\prime}(K)
                \mathrm{E}
                \left[
                \left.
                    (S(t_{\mathrm{fix}}) - K)^{+}
                \right|
                    \mathcal{F}_{0}
                \right]
                + \int_{K}^{\infty} 
                    \mathrm{E}
                    \left[
                    \left.
                        (S(t_{\mathrm{fix}}) - x)^{+}\ 
                    \right|
                        \mathcal{F}_{0}
                    \right]
                    g_{\mathrm{cap}}^{\prime\prime}(x)
                dx
            \right)
    \label{2_16_convexity_correction}
\end{eqnarray}
$$

また、$\eqref{2_10_value_of_today_cms_cap}$に代入すると、swaptionの価値は$\eqref{2_4_a_value_of_today_swaption}$なので、

$$
\begin{eqnarray}
    V_{\mathrm{CMScap}}(0)
        & = & 
            P(0, t_{p}) \mathrm{E}^{A}
            \left[
            \left.
                (S(t_{\mathrm{fix}}) - K)^{+}
            \right|
                \mathcal{F}_{0}
            \right]
            + P(0, t_{p})
            \left(
                g_{\mathrm{cap}}^{\prime}(K)
                \mathrm{E}^{A}
                \left[
                \left.
                    (S(t_{\mathrm{fix}}) - K)^{+}
                \right|
                    \mathcal{F}_{0}
                \right]
                + \int_{K}^{\infty} 
                    \mathrm{E}^{A}
                    \left[
                    \left.
                        (S(t_{\mathrm{fix}}) - x)^{+}\ 
                    \right|
                        \mathcal{F}_{0}
                    \right]
                    g_{\mathrm{cap}}^{\prime\prime}(x)
                dx
            \right)
        \nonumber
        \\
        & = &
            P(0, t_{p}) 
            \frac{A(0)}{A(0)}
            \left(
                \mathrm{E}^{A}
                \left[
                \left.
                    (S(t_{\mathrm{fix}}) - K)^{+}
                \right|
                    \mathcal{F}_{0}
                \right]
                + g_{\mathrm{cap}}^{\prime}(K)
                \mathrm{E}^{A}
                \left[
                \left.
                    (S(t_{\mathrm{fix}}) - K)^{+}
                \right|
                    \mathcal{F}_{0}
                \right]
                + \int_{K}^{\infty} 
                    \mathrm{E}^{A}
                    \left[
                    \left.
                        (S(t_{\mathrm{fix}}) - x)^{+}\ 
                    \right|
                        \mathcal{F}_{0}
                    \right]
                    g_{\mathrm{cap}}^{\prime\prime}(x)
                dx
            \right)
    \nonumber
    \\
        & = &
            \frac{P(0, t_{p})}{A(0)}
            \left(
                C(K)(1 + g_{\mathrm{cap}}^{\prime}(K))
                + \int_{K}^{\infty} C(x) g_{\mathrm{cap}}^{\prime\prime}(x) dx
            \right)
\end{eqnarray}
$$

$$
    C(x)
        := A(0) \mathrm{E}
        \left[
        \left.
            (S(t_{\mathrm{fix}}) - x)^{+}
        \right|
            \mathcal{F}_{0}
        \right]
$$

とおく。

よって、european swaptionの異なるstirkeで積分したもので表現できる。
* replication methodは、CMS legを正確に表現する手法

### 2.2 CMS floorlets and swaplets

$$
\begin{equation*}
    g_{\mathrm{floor}}(x) := (K - x)^{+}
        \left(
            \frac{G(x)}{G(S(0))} - 1
        \right),
\end{equation*}
$$

$$
    g_{\mathrm{floor}}^{\prime}(x) 
        = 1_{(-\infty, K]}(x)
        \left(
            \frac{G(x)}{G(S(0))} - 1
        \right)
        + (K - x)^{+}
        \left(
            \frac{G(x)}{G(S(0))} - 1
        \right)^{\prime}
$$

同様に、$f$がなめらかな関数とすると

$$
\begin{eqnarray*}
    f(S) 
        & = & f(K) + \int_{K}^{S} f^{\prime}(x) \ dx
        \\
        & = & f(K) - \int_{S}^{K} f^{\prime}(x) \ dx
        \\
        & = & f(K) - \int_{-\infty}^{K} 1_{[S, \infty)}(x)f^{\prime}(x) \ dx
        \\
        & = & f(K) 
            - \left[
                (x - S)^{+}f^{\prime}(x) 
            \right]_{-\infty}^{K}
            + \int_{-\infty}^{K} (x - S)^{+} f^{\prime\prime}(x) \ dx
        \\
        & = & f(K) 
            - (K - S)^{+}f^{\prime}(K) 
            + \int_{-\infty}^{K} (x - S)^{+} f^{\prime\prime}(x) \ dx.
\end{eqnarray*}
$$

より

$$
\begin{eqnarray*}
    cc 
        & = & P(0, t_{p})
            \mathrm{E}
            \left[
            \left.
                g_{\mathrm{floor}}(S(t_{\mathrm{fix}}))
            \right|
                \mathcal{F}_{0}
            \right]
    \\
        & = & P(0, t_{p})
            \mathrm{E}
            \left[
            \left.
                -g_{\mathrm{floor}}^{\prime}(K)(K - S(t_{\mathrm{fix}}))^{+}
                + \int_{-\infty}^{K} (x - (t_{\mathrm{fix}}))^{+}g_{\mathrm{floor}}^{\prime\prime}(x)\ dx
            \right|
                \mathcal{F}_{0}
            \right]
    \\
        & = & P(0, t_{p})
            \left(
                - g_{\mathrm{floor}}^{\prime}(K)
                \mathrm{E}
                \left[
                \left.
                    (K - S(t_{\mathrm{fix}}))^{+}
                \right|
                    \mathcal{F}_{0}
                \right]
                + \int_{-\infty}^{K} 
                    \mathrm{E}
                    \left[
                    \left.
                        (x - S(t_{\mathrm{fix}}))^{+}\ 
                    \right|
                        \mathcal{F}_{0}
                    \right]
                    g_{\mathrm{floor}}^{\prime\prime}(x)
                dx
            \right)
\end{eqnarray*}
$$

$$
\begin{eqnarray}
    V_{\mathrm{CMSfloor}}(0)
        & = & 
            P(0, t_{p}) \mathrm{E}^{A}
            \left[
            \left.
                (x - S(t_{\mathrm{fix}}))^{+} 
            \right|
                \mathcal{F}_{0}
            \right]
            + P(0, t_{p})
            \left(
                - g_{\mathrm{floor}}^{\prime}(K)
                \mathrm{E}^{A}
                \left[
                \left.
                    (x - S(t_{\mathrm{fix}}))^{+} 
                \right|
                    \mathcal{F}_{0}
                \right]
                + \int_{-\infty}^{K} 
                    \mathrm{E}^{A}
                    \left[
                    \left.
                        (x - S(t_{\mathrm{fix}}))^{+} 
                    \right|
                        \mathcal{F}_{0}
                    \right]
                    g_{\mathrm{floor}}^{\prime\prime}(x)
                dx
            \right)
        \nonumber
        \\
        & = &
            P(0, t_{p}) 
            \frac{A(0)}{A(0)}
            \left(
                \mathrm{E}^{A}
                \left[
                \left.
                    (x - S(t_{\mathrm{fix}}))^{+} 
                \right|
                    \mathcal{F}_{0}
                \right]
                - g_{\mathrm{floor}}^{\prime}(K)
                \mathrm{E}^{A}
                \left[
                \left.
                    (x - S(t_{\mathrm{fix}}))^{+} 
                \right|
                    \mathcal{F}_{0}
                \right]
                + \int_{-\infty}^{K} 
                    \mathrm{E}^{A}
                    \left[
                    \left.
                        (x - S(t_{\mathrm{fix}}))^{+} 
                    \right|
                        \mathcal{F}_{0}
                    \right]
                    g_{\mathrm{floor}}^{\prime\prime}(x)
                dx
            \right)
    \nonumber
    \\
        & = &
            \frac{P(0, t_{p})}{A(0)}
            \left(
                P(K)(1 - g_{\mathrm{floor}}^{\prime}(K))
                + \int_{-\infty}^{K} P(x) g_{\mathrm{floor}}^{\prime\prime}(x) dx
            \right)
\end{eqnarray}
$$

ここで、$P$はreciever's swaptionの現在価値である。

$$
\begin{eqnarray*}
    V_{\mathrm{CMSswap}}(0)
        & := & A(0)
            \mathrm{E}
            \left[
            \left.
                \frac{
                    (S(t_{\mathrm{fix}}) - K)P(t_{\mathrm{fix}}, t_{p})
                }{
                    A(t_{\mathrm{fix}})
                }
            \right|
                \mathcal{F}_{0}
            \right]
        \\
        & = & A(0)
            \mathrm{E}
            \left[
            \left.
                \frac{
                    (S(t_{\mathrm{fix}}) - K)P(t_{\mathrm{fix}}, t_{p})
                }{
                    A(t_{\mathrm{fix}})
                }
            \right|
                \mathcal{F}_{0}
            \right]
        \\
        & = & A(0)
            \mathrm{E}
            \left[
            \left.
                \frac{
                    (S(t_{\mathrm{fix}}) - K)^{+}P(t_{\mathrm{fix}}, t_{p})
                }{
                    A(t_{\mathrm{fix}})
                }
                -
                \frac{
                    (K - S(t_{\mathrm{fix}}))^{+}P(t_{\mathrm{fix}}, t_{p})
                }{
                    A(t_{\mathrm{fix}})
                }
            \right|
                \mathcal{F}_{0}
            \right]
        \\
        & = &
            V_{\mathrm{CMScap}}(0) - V_{\mathrm{CMSfloor}}(0)
\end{eqnarray*}
$$

また、

$$
\begin{eqnarray*}
    C(K) - P(K)
        & = & A(0)
            \left(
               \mathrm{E}^{A}
               \left[
                \left.
                   S(t_{\mathrm{fix}}) - K
                \right|
                    \mathcal{F}_{0}
               \right]
            \right)
        \\
        & = & A(0)(S(0) - K),
\end{eqnarray*}
$$

をあわせて、

$$
\begin{eqnarray}
    V_{\mathrm{CMSswap}}(0)
        & = &
            \frac{P(0, t_{p})}{A(0)}
            \left(
                C(K)(1 + g_{\mathrm{cap}}^{\prime}(K)) 
                    + \int_{K}^{\infty} C(x)g_{\mathrm{cap}}^{\prime\prime}(x)\ dx 
            \right)
            -
            \frac{P(0, t_{p})}{A(0)}
            \left(
                P(K)(1 + g_{\mathrm{floor}}^{\prime}(K))
                    - \int_{-\infty}^{K} P(x)g_{\mathrm{floor}}^{\prime\prime}(x)\ dx
            \right)
        \nonumber
        \\
        & = &
            \frac{P(0, t_{p})}{A(0)}
            \left(
                (C(K) - P(K) + C(K)g_{\mathrm{cap}}^{\prime}(K) - P(K)g_{\mathrm{floor}}^{\prime}(K))
                    + \int_{-\infty}^{K} P(x)g_{\mathrm{floor}}^{\prime\prime}(x)\ dx
                    + \int_{K}^{\infty} C(x)g_{\mathrm{cap}}^{\prime\prime}(x)\ dx
            \right)
        \nonumber
        \\
        & = &
            P(0, t_{p})
            \frac{(S - K)}{A(0)}
                (1 + f^{\prime}(K))
            \frac{P(0, t_{p})}{A(0)}
            \left(
                    + \int_{-\infty}^{K} P(x)f^{\prime\prime}(x)\ dx
                    + \int_{K}^{\infty} C(x)f^{\prime\prime}(x)\ dx
            \right)
        \label{2_19_a_value_of_cms_swap}
\end{eqnarray}
$$


