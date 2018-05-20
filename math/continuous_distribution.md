---
title: Continuous Distributions
---

## Continuous Distributions
The list of continuous distributions.

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
* $\alpha > 0$,
* $\nu > 0$,

$\eqref{gamma_distribution_pdf}$の密度関数を持つ確率変数をガンマ分布に従う確率変数という。

p.d.f. of gamma distribution

$$
\begin{equation}
    f_{G}(x; \alpha, \nu)
    :=
    \begin{cases}
        \frac{1}{\Gamma(\nu)}
        \alpha^{\nu}
        x^{\nu - 1}
        e^{-\alpha x}
        &
            (x > 0)
            \\
        0
            &
            (x \ge 0)
    \end{cases}
    \label{gamma_distribution_pdf}
\end{equation}
$$

where $\Gamma(\nu)$ is the gamma function.

### 2-1. Exponential distribution $\mathrm{Exp}(\lambda)$
* $\lambda > 0$

指数分布はガンマ分布の特別な場合である。
$G(\lambda, 1)$をパラメータ$\lambda$の指数分布といい、$\mathrm{Exp}(\lambda)$とかく。

p.d.f of exponential distribution

### 2-2. noncentral chi-squared distribution
* $k \in \mathbb{N}$,
* $\mu \in \mathbb{R}$,
* $X_{1} \sim N(\mu, 1)$,
* $X_{j} \sim N(0, 1) \ (j = 2, \ldots, k)$,
* $X_{1}, \ldots, X_{k}$,
    * independent

The distribution of r.v. $Y := \sum_{j=1}^{k} X_{j}$ is said to be chi-suqre distribution with $k$ degree of freedom and noncentrality parameter $\mu^{2}$.
The p.d.f of $Y$ is given by

$$
\begin{eqnarray}
    f_{\chi}(x; k, \mu^{2})
    & = &
        e^{-\frac{\mu^{2}}{2}}
        \sum_{r=0}^{\infty}
            \frac{1}{r!}
            \left(
                \frac{\mu^{2}}{2}
            \right)^{r}
            f_{G}(x; \frac{1}{2}, r + \frac{k}{2})
    & &
        (x > 0)
    \nonumber
    \\
    & = &
        e^{-\frac{\mu^{2}}{2}}
        \sum_{r=0}^{\infty}
            \frac{1}{r!}
            \left(
                \frac{\mu^{2}}{2}
            \right)^{r}
            \frac{1}{\Gamma(r + \frac{k}{2})}
            \frac{1}{2^{r + \frac{k}{2}}}
            x^{r + \frac{k}{2} - 1}
            e^{-\frac{1}{2} x}
    & &
        (x > 0)
    \nonumber
    \\
    & = &
        e^{-\frac{\mu^{2}}{2}}
        e^{-\frac{1}{2} x}
        x^{\frac{k}{2} - 1}
        \frac{1}{2^{\frac{k}{2}}}
        \sum_{r=0}^{\infty}
            \frac{1}{r!}
            \left(
                \frac{\mu^{2}}{2}
            \right)^{r}
            \frac{1}{\Gamma(r + \frac{k}{2})}
            \frac{1}{2^{r}}
            x^{r}
    & &
        (x > 0)
\end{eqnarray}
$$

where $g(x; \alpha, \nu)$ is the p.d.f. of gamma distribution with $\alpha, \nu$.
We denote $\chi^{2}(k ,\mu^{2})$ by chi-suqre distribution with $k$ degree of freedom and noncentrality parameter $\mu^{2}$.
In particular, chi-square distribution with $k$ degree of freedom and denote $\chi^{2}(k) := \chi^{2}(k, \mu^{2})$ when $\mu = 0$.
In this case, the p.d.f. of $\chi^{2}(k)$ is given by

$$
\begin{eqnarray}
    f_{\chi}(x; k)
    & = &
        e^{-\frac{0}{2}}
        \sum_{r=0}^{\infty}
            \frac{1}{r!}
            \left(
                \frac{0}{2}
            \right)^{r}
            f_{G}(x; \frac{1}{2}, r + \frac{k}{2})
    \nonumber
    \\
    & = &
        f_{G}(x; \frac{1}{2}, \frac{k}{2})
    \nonumber
    \\
    & = &
        \begin{cases}
            \frac{1}{\Gamma(k/2)}
                (\frac{1}{2})^{k/2} x^{\frac{k - 2}{2}} e^{-\frac{x}{2}}
            &
                (x > 0)
            \\
            0
                & (x \le 0)
        \end{cases}
    \nonumber
\end{eqnarray}
$$

Chi-distribution with $k$ degree of freedom is a special case of gamma distribution.

## 10. t distribution
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

p.d.f of t distribution.

$$
\begin{eqnarray}
    t(n; \delta)(x)
    & := &
        \frac{
            1
        }{
            \sqrt{\pi n}
        }
        e^{-\frac{\delta^{2}}{2}}
        \sum_{r=0}^{\infty}
            \frac{
                2^{r/2}
            }{
                r!
            }
            \frac{
                \Gamma((n + r + 1) / 2)
            }{
                \Gamma(n/2)
            }
            \left(
                \frac{
                    \delta x
                }{
                    \sqrt{n}
                }
            \right)^{r}
            \left(
                1
                +
                \frac{
                    x^{2}
                }{
                    n
                }
            \right)^{
                -(n + r + 1)/2
            }
    \nonumber
    \\
    t(n)(x)
    & := &
        t(n; 0)(x)
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            \sqrt{\pi n}
        }
        \frac{
            \Gamma((n + 1) / 2)
        }{
            \Gamma(n/2)
        }
        \left(
            1
            +
            \frac{
                x^{2}
            }{
                n
            }
        \right)^{
            -(n + 1)/2
        }
    \nonumber
\end{eqnarray}

$$

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

## Reference
* [F-distribution - Wikipedia](https://en.wikipedia.org/wiki/F-distribution)
* [Student's t-test - Wikipedia](https://en.wikipedia.org/wiki/Student%27s_t-test)

