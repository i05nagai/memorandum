---
title: Methods for constructing a Yield Curve
---

# Methods for constructing a Yield Curve

## Symbol
* $r(t) := r(0, t)$は,時刻0の満期$t$のrisk free rate
* $Z(0, t)$は時刻0の満期$t$での割引債の価格
* $C(0, t)$は$Z(0, t)$の逆数
* $Z(0; t_{1}, t_{2})$は時刻0での$t_{1}, t_{2}$の間のforward discount factor
* $f(0; t_{1}, t_{2})$は時刻0での$t_{1}, t_{2}$の間のforward rate
* $f(t) := f(0, t)$は時刻0でのinstantaneous forward rate

$$
\begin{eqnarray}
    C(0, t) 
        & = & \exp(r(0, t)t) \\
    Z(0, t) 
        & = &\exp(-r(0, t)t) \\
    r(t) & = & - \frac{1}{t}\ln Z(0, t)
    \label{risk_free_rate_discount_factor}
\end{eqnarray}
$$

forward discoutn factorは以下で定義される。

$$
    Z(0, t_{1}) Z(0; t_{1}, t_{2}) = Z(0, t_{2})
$$

また、fowward rateは以下で定義する。

$$
    \exp(-f(0; t_{1}, t_{2})(t_{2} - t_{1})) = Z(0; t_{1}, t_{2})
$$

$$
\begin{eqnarray}
    f(0; t_{1}, t_{2}) 
        & = & - \frac{\ln(Z(0, t_{2})) - \ln(Z(0, t_{1}))}{t_{2} - t_{1}} 
            \label{forward_rate_discount_factor} \\
        & = & \frac{r(t_{2})t_{2} - r(t_{1}) t_{1}}{t_{2} - t_{1}}
\end{eqnarray}
$$

instantaneous forward rateを以下で定義する。

$$
    f(0, t) := \lim_{\epsilon \rightarrow 0}f(0; t, t+\epsilon) 
$$

また、forward rateの定義より以下が成り立つ。

$$
\begin{eqnarray}
    f(0, t) 
        & = & - \frac{d}{dt} \ln(Z(0, t)) \\
        & = & \frac{d}{dt}r(t)t
        \label{instantaneous_forward_rate_risk_free_rate}
\end{eqnarray}
$$

よって、instantaneous forward rateは$f(0, t) = r(t) + r'(t)t$とかける。
また、上式を両辺積分すると

$$
\begin{eqnarray}
    r(t) t
        & = & \int_{0}^{t} f(0, s)\ ds \\
    Z(0, t)
        & = & \exp \left( - \int_{0}^{t} f(0, s) \ ds \right)
    \label{discount_factor_instantaneous_forward_rate}
\end{eqnarray}
$$

また、$\eqref{discount_factor_instantaneous_forward_rate}$と$\eqref{forward_rate_discount_factor}$から

$$
\begin{eqnarray}
    f(0; t_{1}, t_{2}) 
        & = & - \frac{\ln(Z(0, t_{2})) - \ln(Z(0, t_{1}))}{t_{2} - t_{1}} \\
        & = & -\frac{1}{t_{2} - t_{1}} \int_{t_{1}}^{t_{2}} f(0, s) \ ds
\end{eqnarray}
$$

更に

$$
\begin{equation}
    f(0; t_{i - 1}, t_{i}) 
        = \frac{r(t_{i}) t_{i} - r(t_{i - 1}) t_{i - 1}}{t_{i} - t_{i - 1}} 
        = -\frac{1}{t_{i} - t_{i-1}} \int_{t_{i-1}}^{t_{i}} f(0, s) \ ds
\end{equation}
$$

となる。ここで、$t_{i} = t$とおけば

$$
\begin{equation}
    r(t) t = r(t_{i-1}) t_{i-1} + \int_{t_{i-1}}^{t} f(0, s) \ ds,\ t \in [t_{i - 1}, t_{i}]
    \label{rt_instantaneous_forward_rate}
\end{equation}
$$

となる。
よって、risk free rateはforward rateを与えれば(instantaneous forward rateが求まり）求まる。

## 2. Interpolation And Bootstrap Of Yield Curves - Not Two Separate Processes

## 3. How to Compare Yield Curve Interpolation Methodologies

* forward rateの形状
    * 連続性はfoward rateの安定性のために重要
    * 不連続なfoward curveは将来のshort-term interest rateの期待値を
    * forwardのsmoothnessは必要だが、他の要素との兼ね合い
* 補間方法がlocalかどうか
    * 変化のあった入力値の近傍の補間の値だけ変わる
    * ある点の補間方法が入力値全体に依存しない方が望ましい
* forward rateが安定しているか
    * 入力値の一つが数basis point動いた時にか０部全体がどの程度動くか
    * 

## Linear Methods

### Linear on rates
risk free rateの線形補間。
つまり、

$$
    r(t) = \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} r(t_{i}) + \frac{t_{i} - t}{t_{i} - t_{i-1}} r(t_{i-1})
$$

となる。
instantaneous forward rateは$\eqref{instantaneous_forward_rate_risk_free_rate}$より

$$
\begin{eqnarray}
    f(0, t) 
        & = & r(t) + r'(t)t \\
        & = & \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} r(t_{i}) + \frac{t_{i} - t}{t_{i} - t_{i-1}} r(t_{i-1}) 
            + \frac{t}{t_{i} - t_{i-1}} r(t_{i}) + \frac{- t}{t_{i} - t_{i-1}} r(t_{i-1})  \\
        & = & \frac{2t - t_{i-1}}{t_{i} - t_{i-1}} r(t_{i}) + \frac{t_{i} - 2t}{t_{i} - t_{i-1}}r(t_{i-1})
\end{eqnarray}
$$

となる。

### Linear on the log of rates
risk free rateのlogをとったものを線形補間。
risk free rateのlog linear補間。
この補間方法ではrisk free rateは常に正になる。

$$
    \ln(r(t)) = \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} \ln(r(t_{i})) + \frac{t_{i} - t}{t_{i} - t_{i-1}} \ln(r(t_{i-1}))
$$

これは以下のようにかける。

$$
    r(t) = r(t_{i})^{\frac{t -  t_{i-1}}{t_{i} - t_{i-1}}}r(t_{i-1})^\frac{t_{i} - t}{t_{i} - t_{i-1}}
$$

また、forward rateは

$$
    r'(t) = \ln(r(t_{i})) r(t_{i})^{\frac{t -  t_{i-1}}{t_{i} - t_{i-1}}} \ln(r(t_{i-1}) r(t_{i-1})^\frac{t_{i} - t}{t_{i} - t_{i-1}} 
$$

を代入すれば求まる。

### Linear on discount factors
discount factorの線形補間

$$
    Z(0, t) = \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} Z(0, t_{i}) + \frac{t_{i} - t}{t_{i} - t_{i-1}} Z(0, t_{i-1})
$$

このとき、risk free rateは$\eqref{risk_free_rate_discount_factor}$より

$$
\begin{eqnarray}
    r(t) 
        & = & - \frac{1}{t}\ln Z(0, t) \\
        & = & - \frac{1}{t} \ln 
            \left( 
               \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} e^{-r(t_{i})t_{i}} 
                   + \frac{t_{i} - t}{t_{i} - t_{i-1}} e^{-r(t_{i-1}) t_{i-1}}
            \right) 
\end{eqnarray}
$$

となる。
またforward rateは、

$$
\begin{eqnarray}
    r'(t) 
        & = & t^{-2} \ln 
            \left( 
               \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} e^{-r(t_{i})t_{i}} 
                   + \frac{t_{i} - t}{t_{i} - t_{i-1}} e^{-r(t_{i-1}) t_{i-1}}
            \right) 
            +
            t^{-1} \frac{1}{ \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} e^{-r(t_{i})t_{i}} + \frac{t_{i} - t}{t_{i} - t_{i-1}} e^{-r(t_{i-1}) t_{i-1}}}
            \left(
                \frac{1}{t_{i} - t_{i-1}} e^{-r(t_{i})t_{i}} 
                    - \frac{1}{t_{i} - t_{i-1}} e^{-r(t_{i-1}) t_{i-1}}
            \right) \\
        & = &
            t^{-2} \ln 
            \left( 
               \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} e^{-r(t_{i})t_{i}} 
                   + \frac{t_{i} - t}{t_{i} - t_{i-1}} e^{-r(t_{i-1}) t_{i-1}}
            \right) 
            +
            t^{-1} \frac{1}{(t -  t_{i-1})e^{-r(t_{i})t_{i}} 
                + (t_{i} - t)e^{-r(t_{i-1}) t_{i-1}}}
            \left(
                e^{-r(t_{i})t_{i}} - e^{-r(t_{i-1}) t_{i-1}}
            \right) 
\end{eqnarray}
$$

より、

$$
\begin{eqnarray}
    f(0, t) 
        & = & r(t) + r'(t)t \\ 
        & = &
            \frac{1}{(t -  t_{i-1})e^{-r(t_{i})t_{i}} 
                + (t_{i} - t)e^{-r(t_{i-1}) t_{i-1}}}
            \left(
                e^{-r(t_{i})t_{i}} - e^{-r(t_{i-1}) t_{i-1}}
            \right) 
\end{eqnarray}
$$

となる。

### Raw interpolation (linear on the log of discount factors)
とても安定している方法で、実装が楽。
instantaneous forward rateをpiecewise constantとする。
disocunt factorのlog linear補間。
また、$rt$のlinear補間とも見ることができる。

instantaneous forward rateが区分定数とすると、$\eqref{rt_instantaneous_forward_rate}$より

$$
\begin{eqnarray*}
    r(t) t 
        & = & r(t_{i-1}) t_{i-1} + \int_{t_{i-1}}^{t} f(s) \ ds,\ t \in [t_{i - 1}, t_{i}] \\
        & = & r(t_{i-1}) t_{i-1} + (r(t)t - r(t_{i-1})t_{i-1}) ds,
\end{eqnarray*}
$$

また、disocunt factorのlog linear補間と思うと

$$
    \ln(Z(0, t)) = \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} \ln(Z(0, t_{i})) + \frac{t_{i} - t}{t_{i} - t_{i-1}} \ln(Z(0, t_{i-1}))
$$

$Z(0, t) = \exp(-r(t)t)$より、

$$
    r(t)t = \frac{t -  t_{i-1}}{t_{i} - t_{i-1}} r(t_{i})t_{i} + \frac{t_{i} - t}{t_{i} - t_{i-1}}r(t_{i-1})t_{i-1}
$$

である。

### Piecewise linear forward

## 5.Splines

### Quadratic splines

### Cubic splines

## 6. Monotone Convex
