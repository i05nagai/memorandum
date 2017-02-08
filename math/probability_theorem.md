---
title: Theorems related to probability
---

# Theorems related to probabilty

## Bayse' rule
$Q \sim P$が同値な確率測度とする。
このdensity processを

$$
    D(t) :=
        \left. 
            \frac{d Q}{d P}
        \right|_{\mathcal{F}_{t}}
        =
        \mathrm{E}
        \left[
        \left.
            \frac{d Q}{d P}
        \right|
            \mathcal{F}_{t}
        \right],
$$

と定義する。
$X$を$\mathcal{F}_{T}$-measurableな確率変数で、$\mathrm{E^{Q}}^{|X|} < \infty$とする。
このとき、

1. 以下のBayse' ruleが成り立つ

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        F_{t}
    \right]
        = \frac{
            \mathrm{E}
            \left[
            \left.
                XD(T)
            \right|
                \mathcal{F}_{t}
            \right]
        }{
            \mathcal{F}_{t}
        },
        \quad
        t \ge T.
$$

2. $M$が適合過程で、$Q$-martingaleあることと、$DM$が$P$-martingaleであることは同値

## proof
まず、1について示す。

$$
    
$$
