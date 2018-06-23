---
title: Hypothesis Test
---

## Hypothesis Test

## Definition
推定量といった場合は確率変数。
基本的に添え字なしの$X$, $Y$などは真の分布を表すのに使用する。

* $$X, X_{1}, \ldots, X_{N}$$,
    * 確率変数
* $$Y, Y_{1}, \ldots, Y_{M}$$,
    * 確率変数
* $$
    \displaystyle
    \bar{X}_{N}
    :=
    \sum_{i=1}^{N}
        \frac{
            X_{i}
        }{
            N
        }
$$,
    * 標本の平均
    * 平均の不偏推定量
* $$
    \displaystyle
    V_{N}
    := 
    \frac{
        \sum_{i=1}^{N} (X_{i} - \bar{X}_{N})^{2}
    }{
        N - 1
    }
    \label{def_sample_variance}
$$,
    * 分散の不偏推定量
* $$
    \displaystyle
    V_{N}^{S}
    := 
    \frac{
        \sum_{i=1}^{N} (X_{i} - \bar{X}_{N})^{2}
    }{
        N
    }
$$,
    * 標本の分散(標本分散）

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

### Definition ($\chi^{2}$ distribution)
$$X_{i} \sim \mathrm{N}(\mu, \sigma^{2})$$とする。
このとき、

$$
    V := \sum_{i=1}^{N} X_{i}^{2}
    
$$

で定義される$V$を自由度$N$の$\chi_{N}^{2}$分布(chi-squared distribution)という。
つまり、$\chi_{N}^{2}$分布は、正規乱数の$N$個の二乗和である。

### Definition (t distribution)
$Z \sim \mathrm{N}(0, 1)$、$U \sim \chi_{N}^{2}$とする。

## Statistics

### one sample t検定
one sample t testsは、平均値が$\mu_{0}$と等しいかどうかの検定。

### paired sample (two sample) t-test for the population mean of paired samples
$X$, $Y$という2つの確率変数が独立で、正規分布に従っているとする。

### $\chi^{2}$検定
TBD.


よって、$Z$検定の仮定のもと$\mu$の取る確率を計算できる。




## Reference
* [Z検定 - Wikipedia](https://ja.wikipedia.org/wiki/Z%E6%A4%9C%E5%AE%9A)
* [Statistical hypothesis testing - Wikipedia](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
* [Lecture Notes \| Statistics for Applications \| Mathematics \| MIT OpenCourseWare](https://ocw.mit.edu/courses/mathematics/18-443-statistics-for-applications-fall-2006/lecture-notes/)
