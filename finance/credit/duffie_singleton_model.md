---
title: Duffie-Singleton model
---

## Duffie-Singleton model


#### Definition Recovery Rate according to Jarrow and Turnbull

* $r(t)$,
    * risk-free rate
* $Z_{0}(t, T)$,
    * the price of risk-free discount bond at maturity $T$
* $L(t, T)$,
    * the price of risk-free discount bond if 
* $\delta_{t}^{JT} \in [0, 1]$
    * recovery rate

$$
    \delta_{t}^{JT}
    :=
    \frac{
        L(t, T)
    }{
        L(t, T)
    }
    .
$$

$$
\begin{eqnarray}
    Z_{0}(t, T)
    & := &
        \exp
        \left(
            -
            \int_{t}^{R}
                r(s)
            \ ds
        \right)
    \nonumber
    \\
    L(t, T)
    & = &
        \delta_{t}^{JT}
        \exp
        \left(
            -
            \int_{t}^{R}
                r(s)
            \ ds
        \right)
    \nonumber
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Duffie-Singleton according to Jarrow and Turnbull
* $(\tau-)$,
    * the time immdediately before the default time
* $v(\tau-, T)$,
    * the price of the bond at $t$ whose maturity is $T$ immediately before default,
* $v(\tau, T)$,
    * the price of the bond at $t$ whose maturity is $T$ immediately after default,
* $\delta_{\tau}^{DS} \in [0, 1]$
    * recovery rate at $\tau$,

$$
    \delta_{\tau}^{DS}
    :=
    \frac{
        v(\tau, T)
    }{
        v(\tau-, T)
    }
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

$$
\begin{eqnarray}
    Z(t, T)
    & := &
        \mathrm{E}
        \left[
            \exp
            \left(
                -
                \int_{t}^{T}
                    R(s)
                \ ds
            \right)
            \mid
            \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \exp
            \left(
                -
                \int_{t}^{T}
                    r(s)
                \ ds
            \right)
            \mid
            \mathcal{F}_{t}
        \right]
        \mathrm{E}
        \left[
            \exp
            \left(
                -
                \int_{t}^{T}
                    (1 - \delta)
                    h(s)
                \ ds
            \right)
            \mid
            \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        Z_{0}(t, T)
        \mathrm{E}
        \left[
            \exp
            \left(
                -
                \int_{t}^{T}
                    (1 - \delta)
                    h(s)
                \ ds
            \right)
            \mid
            \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    R(s)
    & := &
        r(s)
        +
        (1 - \delta)h(s)
    \nonumber
    \\
    h(t)
    & := &
        \frac{
            -
            \frac{\partial }{\partial s} 
            P(\tau \ge s)
        }{
            P(\tau \ge t)
        }
    \nonumber
    \\
    & = &
        \lim_{u \rightarrow 0}
            \frac{1}{u}
            P(t < \tau \le \tau + u \mid  \tau > t)
    \nonumber
    \\
    Z_{0}(t, T)
    & := &
        \mathrm{E}
        \left[
            \exp
            \left(
                -
                \int_{t}^{T}
                    r(s)
                \ ds
            \right)
            \mid
            \mathcal{F}_{t}
        \right]
    \nonumber
\end{eqnarray}
$$

* $S(t)$,
    * the probability that a company survive until $t$,

$$
    S(t)
    :=
    P(\tau \ge t)
    .
$$

$$
\begin{eqnarray}
    h(t)
    =
    \frac{
        \frac{d S(t)}{d t}
    }{
        S(t)
    }
    \nonumber
\end{eqnarray}
$$

## Reference
