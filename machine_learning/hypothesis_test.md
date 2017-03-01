---
title: Hypothesis Test
---

## Hypothesis Test

## Definition
* $$X_{1}, \ldots, X_{N}$$,
    * 確率変数
* $$Y_{1}, \ldots, Y_{M}$$,
    * 確率変数
* $$
    \displaystyle
    \bar{X}_{N} := \sum_{i=1}^{N} X_{i} / N
$$,
* $$
    \displaystyle
    S_{N} := \sum_{i=1}^{N} (X_{i} - \bar{X}_{N}) / (N - 1)
$$,

$X_{1}, \ldots, X_{N}$が$X$のi.i.dとすれば、以下が成立する。
$N$をsample sizeという。

$$
\begin{eqnarray}
    \mathrm{E}(\bar{X}_{N})
    &= &
        \mathrm{E}(X),
    \nonumber
    \\
    \mathrm{Var}(\bar{X}_{N})
    & = &
        \frac{
            \mathrm{Var}(X)
        }{
            N
        },
    \nonumber
\end{eqnarray}
$$

sample sizeが増えれば標本分散は減る。

## Statistics

### Z - tests
Z検定は、正規分布性を仮定して、標本の平均が真の平均とどの程度乖離しているかを統計的に調べる方法。
以下を仮定する。

1. 標本が正規分布
2. 真の分布の標準偏差は既知ないし、仮定

2の仮定は現実的ではない、
真の分布の平均を知りたい場合は、t検定を用いるのが一般的。

### t検定
TBD.

### $\chi^{2}$検定
TBD.


## Theory

## Proposition 1
$$X_{i} \sim \mathrm{N}(\mu, \sigma)\ \forall i = 1,\ldots, N$$とする。
このとき、

$$
    \frac{
        \bar{X}_{N} - \mu
    }{
        \frac{\sigma}{\sqrt{N}}
    }
    \sim
    \mathrm{N}(0, 1)
$$

## proof

<div class="QED" style="text-align: right">$\Box$</div>

よって、$Z$検定の仮定のもと$\mu$の取る確率を計算できる。

## Proposition 2
$X_{i} \forall i = 1, \ldots, N$, $Y_{i} \forall j = 1, \ldots, N$が正規分布に従うとする。
$$\forall i = 1, \ldots, N$$について、$$X_{i}, \{Y_{i}\}$$が独立とする。
このとき、

$$
    Z
    :=
    \frac{
        \bar{D}_{N} - \delta
    }{
        \frac{
            \sigma_{D}
        }{
            \sqrt{N}
        }
    }
    \sim
    \mathrm{N}(0, 1)
$$

ここで、

$$
\begin{eqnarray}
    D_{i}
    & := &
    (X_{i} - Y_{i}),
    \nonumber
    \\
    \bar{D}_{N}
    & := &
        \frac{
            \sum_{i=1}^{N} (X_{i} - Y_{i})
        }{
            N
        },
    \nonumber
    \\
    \mu_{D} 
    & := &
        \mathrm{E}(D_{N}),
    \nonumber
    \\
    \sigma_{D}
    & = &
        \sqrt{\mathrm{Var}(\bar{D}_{N})}
\end{eqnarray}
$$

### proof.
$X_{i} - Y_{i}$が正規分布に従うことに注意すれば良い。

<div class="QED" style="text-align: right">$\Box$</div>

よって、$Z$検定の仮定を用いれば$\mu_{D}$の取る確率を次の通り計算できる。
独立性は各$i$について独立であることに注意する。

### Lemman 3
$$\{X_{i}\}$$, $$\{Y_{i}\}$$が独立とする。
また、$$\forall i = 1, \ldots, N, X_{i} \sim \mathrm{N}(\mu_{X}, \sigma_{X}^{2})$$かつ$$\forall i = 1, \ldots, M$$, $$Y_{i} \sim \mathrm{N}(\mu_{Y}, \sigma_{Y}^{2})$$とする。
このとき、

$$
    \bar{X}_{N} - \bar{Y}_{M}
    \sim
    \mathrm{N}(\mu_{X} - \mu_{Y}, \frac{\sigma_{X}^{2}}{N} + \frac{\sigma_{Y}^{2}}{M})
$$

### proof.
独立な正規乱数の和はまた正規乱数であることに注意すれば、

$$
\begin{eqnarray}
    \bar{X}_{N}
    & \sim &
        \mathrm{N}(\mu_{X}, \frac{\sigma_{X}^{2}}{N}),
    \nonumber
    \\
    \bar{Y}_{N}
    & = &
        \mathrm{N}(\mu_{Y}, \frac{\sigma_{Y}^{2}}{M}),
    \nonumber
    \\
    \bar{X}_{N} - \bar{Y}_{M}
    & = &
        \bar{X}_{N} + (-\bar{Y}_{M}),
    \nonumber
    \\
    & \sim &
        \mathrm{N}
        (
            \mu_{X} - \mu_{Y},
            \frac{\sigma_{X}^{2}}{N} + (-1)^{2}\frac{\sigma_{Y}^{2}}{M}
        ),
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 4
$$\{ X_{i} \}_{i=1}^{N}$$, $$\{ Y_{i} \}_{i=1}^{M}$$が独立とする。
$$\forall i = 1, \ldots, N, X_{i} \sim \mathrm{N}(\mu_{X}, \sigma_{X}^{2})$$かつ$$\forall i = 1, \ldots, M, Y_{i} \sim \mathrm{N}(\mu_{Y}, \sigma_{Y}^{2})$$とする。
このとき、

$$
    Z
    :=
    \frac{
        (\bar{X}_{N} - \bar{Y}_{M}) - (\mu_{X} - \mu_{Y})
    }{
        \sqrt{
            \frac{\sigma_{X}^{2}}{N}
            +
            \frac{\sigma_{Y}^{2}}{M}
        }
    }
    \sim
    \mathrm{N}(0, 1)
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

独立性は族の間の独立性である。
この場合も、各々の標準偏差が既知であれば、$\mu_{X} - \mu_{Y}$の確率を計算できる。

### Lemma

$$
    \sum_{i=1}^{N} (X_{i} - \bar{X}_{N}) = 0
$$

### proof.
計算すればよい。

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem

$$
    \frac{
        (N - 1)S^{2}
    }{
        \sigma^{2}
    }
$$

は自由度$n-1$の$\chi^{2}$分布に従う。

### proof.

$$
\begin{eqnarray}
    S^{2}
    & = &
        \frac{
            \left(
                \sum_{i=1}^{N} (X_{i} - \bar{X}_{N})
            \right)^{2}
        }{
            (N - 1)^{2}
        },
    \nonumber
    \\
    & = &
        \frac{
            \sum_{i=1}^{N}
                 (X_{i} - \bar{X}_{N})^{2}
            +
            \sum_{i \neq j}
                 (X_{i} - \bar{X}_{N})
                 (X_{j} - \bar{X}_{N})
        }{
            (N - 1)^{2}
        },
\end{eqnarray}
$$

## Reference
1. [Z検定 - Wikipedia](https://ja.wikipedia.org/wiki/Z%E6%A4%9C%E5%AE%9A)

