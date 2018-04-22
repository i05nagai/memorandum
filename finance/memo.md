# memo

## Girsanovの定理

$$
    d\zeta^{\theta}(t) = \zeta^{\theta}(t)\theta(t)^{T} dW(t)
$$

のSDEの解、

$$
    \zeta^{\theta}(t)
        := \mathcal{E}
        \left(
            \int_{0}^{t} \theta(s)^{T}\ dW(s)
        \right)
        :=
        \exp
        \left( 
            \int_{0}^{t}\theta(s)^{T}\ dW(s) - \frac{1}{2} \int_{0}^{t}\theta(s)^{T}\theta(s)\ ds
        \right)
$$

が$P$のもとでマルチンゲールとする。
このとき、

$$
    W^{\theta}(t) := W(t) + \int_{0}^{t} \theta(s)\ ds
$$

は$P(\theta)$の元でBMとなる。

### Remark
$P$のもとでの以下のSDEを考える。

$$
    S(t) = S(0) + \int_{0}^{t} \mu(s, S(s))\ ds + \int_{0}^{t} \sigma(s, S(s))\ dW(s)
$$

このとき、以下の$W^{\theta}(t)$を考えると

$$
    W^{\theta}(t) :=  W(t) +  \int_{0}^{t} -\sigma^{-1}(t, x) \mu(t, x)  \ ds
$$

SDEが$W^{\theta}(t)$の元では、マルチンゲールになる。

$$
    S(t) = S(0) + \int_{0}^{t} \sigma(s, S(s))\ dW^{\theta}(s)
$$

financeでは、マルチンゲールになるような測度を探すことがよくある。
