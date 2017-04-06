---
title: Continuous Distributions
---

## Continuous Distributions
連続分布の一覧

1. Uniform distribution(一様分布)
2. Gamma distribution(Gamma分布)
    * Exponential distribution(指数分布)
    * Chi-squared distribution(Chi2乗分布)
3. Normal distribution(正規分布)
4. Log-normal distribution(対数正規分布)
5. Beta(Beta分布)
6. Cauchy distribution(Cauchy分布)
7. Weibull distribution(Weibull分布)
8. Logistic distribution(Logistic分布)
9. Pareto distribution(Pareto分布)
10. t distribution
11. F distribution

## 1. Uniform distribution $U(a, b)$


## 2. Gamma distribution $G(\alpha, \nu)$
$\alpha > 0$, $\nu > 0$とする。
$\eqref{gamma_distribution_pdf}$の密度関数を持つ確率変数をガンマ分布に従う確率変数という。

### p.d.f.

$$
\begin{equation}
    f(x)
    :=
    \begin{cases}	
        \frac{1}{\Gamma(\nu)} \alpha^{\nu} x^{nu - 1} e^{-\alpha x} & (x > 0) \\
        0 & (x \ge 0)  
    \end{cases}
    \label{gamma_distribution_pdf}
\end{equation}
$$

ここで、$\Gamma(\nu)$はガンマ関数である。

### c.d.f.

### Exponential distribution $\mathrm{Exp}(\lambda)$
指数分布はガンマ分布の特別な場合である。
$\lambda > 0$とする。
$G(\lambda, 1)$をパラメータ$\lambda$の指数分布といい、$\mathrm{Exp}(\lambda)$とかく。

#### p.d.f

#### c.d.f

### Chi-squared distribution $\chi^{2}(k)$
カイ2乗分布もガンマ分布の特別な場合である。
$k \in \mathbb{N}$とする。
$G(1/2, k /2)$を自由度$k$のカイ二乗分布といい、$\chi^{2}$とかく。

#### p.d.f

$$
\begin{equation}
    f(x)
    :=
    \begin{cases}	
        \frac{1}{\Gamma(k/2)} (\frac{1}{2})^{k/2} x^{\frac{k - 2}{2}} e^{-\frac{x}{2}} & (x < 0) \\
        0 & (x \ge 0)  
    \end{cases}
\end{equation}
$$

#### c.d.f

## 10. t distribution $t(n, \delta)$
$Y$が自由度$n$のカイ2乗分布$\chi(n)$に従い、$Z$が正規分布$\mathrm{N}(\delta, 1)$に従い、$Y,Z$が独立とする。

$$
    X
    :=
    \frac{
        Z
    }{
        \sqrt{Y/n}
    }
$$

の分布を自由度$n$、非心度$\delta$の非心t分布(noncentral t-distritbuion)といい、$t(n, \delta)$とかく。
特に$\delta = 0$のとくt分布といい$t(n)$とかく。

### p.d.f

### c.d.f

## 11. F distribution $F(m, n, \delta)$
$Y_{1}$が$\chi^{2}(m, \delta)$に$$Y_{2}$$が$$\chi^{2}(n)$$に従い、$$Y_{1}, Y_{2}$$が独立であるとする。
このとき、

$$
    X
    :=
    \frac{
        Y_{1}/m
    }{
        Y_{2}/n
    }
$$

の分布を自由度$m,n$、非心度$\delta$の非心F分布(noncentral F-distribution)といいい、$F(m, n, \delta)$とかく。
特に$\delta=0$のとき、自由度$m, n$のF分布といい、$F(m, n)$とかく。

### p.d.f
非心F分布の確率密度関数は$\forall x \in (0, \infty)$に対して、

$$
\begin{equation}
    p_{X}(x; m, n, \delta)
    :=
    \sum_{r=0}^{\infty}
        e^{-\frac{1}{2} \delta}
        \left(
            \frac{\delta}{2}
        \right)
        \frac{
            (m/n)^{m/2 + r}
        }{
            r!
            B(m/2 + r, n/2)
        }
        \frac{
            x^{m/2 + r -1}
        }{
            (1 + m x / n)^{(m+n)/2 + r}
        }
    \label{noncentral_f_distribution_pdf}
\end{equation}
$$

である。
特に、$\delta=0$の場合は$r=0$の項のみ残り、

$$
\begin{eqnarray}
    p_{X}(x; m, n)
    & := &
        p_{X}(x; m, n, 0)
    \nonumber
    \\
    & = &
        e^{-\frac{1}{2} \delta}
        \left(
            \frac{\delta}{2}
        \right)
        \frac{
            (m/n)^{m/2}
        }{
            B(m/2, n/2)
        }
        \frac{
            x^{m/2 -1}
        }{
            (1 + m x / n)^{(m+n)/2}
        }
    \label{f_distribution_pdf}
\end{eqnarray}
$$

となる。
これが$F$分布の密度関数である。

### c.d.f

## Reference
* [F-distribution - Wikipedia](https://en.wikipedia.org/wiki/F-distribution)
* [Student's t-test - Wikipedia](https://en.wikipedia.org/wiki/Student%27s_t-test)

