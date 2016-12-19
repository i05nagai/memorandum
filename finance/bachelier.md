---
layout: math
title: Bachelier
---

# Introduction
Bachelier modelまたはNormal modelとして知られるモデルである。
Black Scholes modelにおいて、増分がlog-normalの分布を持つのに対して、bachelier modelでは増分がnormalの分布を持つ。
積分形で書くと以下で定義される。

$$
\begin{equation}
    S(t) = S_{0}
        + \int_{0}^{t} \mu \ ds 
        + \int_{0}^{t} \sigma \ dW_{s}
    \label{bachelier_model_integral_form}
\end{equation}
$$

微分形でかくと

$$
\begin{equation}
    d S(t) = \mu dt + \sigma dW_{t},
    \quad
    S(0) = S_{0}
    \label{bacelier_model_differential_form}
\end{equation}
$$

である。
ここで、$S(t)$は原資産で、$\mu, \sigma, S(0)$は定数で、$S(0), \sigma(0) > 0$とする。
$S(t)$は解析的にとけて、以下の解を持つ。

$$
    S(t) = 
        S_{0} + \mu t + \sigma W_{t}
$$
