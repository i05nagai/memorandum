---
title: Chi-square tests
---

## Chi-square tests


## Chi-Square test for the Population Variance

* True ditribution: $X \sim \mathrm{N}(\mu, \sigma^{2})$,
* $X_{1}, \ldots, X_{N}$,
    * i.i.d. of $X$
* $\mu$ is unknown

### Example
* $\sigma_{0} \in \mathbb{R}_{>0}$
    * std deviation for null hypothesis
* $N \in \mathbb{N}$,
    * sample size
* $x_{i} := X_{i}(\omega)$,
* $\alpha \in (0, 1)$,
    * significance level
    * 0.05, 0.01 are commonly used

$$
\begin{eqnarray}
    \bar{x}
    & := &
        \bar{X}_{N}(\omega)
    \nonumber
    \\
    s
    & := &
        \sqrt{V_{n}(X_{1}, \ldots, X_{N})(\omega)}
    \nonumber
\end{eqnarray}
$$

The steps for chi-square test for population variance are as follos;

* (1) State the hypotheses:
    * null hypothesis
        * $H_{0}$: $\sigma^{2} = \sigma_{0}^{2}$,
    * alternative hypothesis
        * (a) $H_{A}$: $\sigma^{2} \neq \sigma_{0}^{2}$,
        * (b) $H_{A}$: $\sigma^{2} > \sigma_{0}^{2}$,
        * (c) $H_{A}$: $\sigma^{2} < \sigma_{0}^{2}$,
* (2) Compute the test statistics
    * $\bar{x}$
        * the sample mean
    * $s$
        * the sample standard deviation

$$
\begin{eqnarray}
    y
    & = &
        \frac{
            (N - 1)s^{2}
        }{
            \sigma_{0}^{2}
        }
\end{eqnarray}
$$

* (3) Compute the $p$ value
    * $Y$: $\chi^{2}$ distribution with $N - 1$ degree of freedom
    * (a) 
        * If $y$ is less than the median, $$p := 2P(Y \le y)$$,
        * If $y$ is greater than the median, $$p := 2P(Y \ge y)$$,
    * (b) $p := P(Y > y)$,
    * (c) $p := P(Y < y)$,
* (4)
    * If $p < \alpha$, reject $H_{0}$,
    * otherwise, fail to reject $H_{0}$,

### Theory

#### Corollary 9.
* $X \sim \mathrm{N}(\mu, \sigma^{2})$,
* $X_{1}, \ldots, X_{N}$,
    * i.i.d. of $X$

Then

$$
\begin{eqnarray}
    \frac{
        (N - 1) V_{N}(X_{1}, \ldots, X_{N})
    }{
        \sigma^{2}
    }
    & \sim &
        \chi(N - 1)
    \nonumber
\end{eqnarray}
$$

#### proof.
By Theorem 19.

<div class="QED" style="text-align: right">$\Box$</div>


## Chi-square test for goodness of fit
The test is also known as Pearson's chi-squared test.
This approximation known as Peason's approximation.

* True ditribution: $X \sim f(p_{1}, \ldots, p_{m})$,
    * multinomial distribution
    * $f$: p.d.f. of multinomial distribution
    * $\sum_{j=1}^{m} p_{j} = 1$,
    * $$X \in \{1, \ldots, m\}$$,
* $N \in \mathbb{N}$,
    * sample size
* $X_{1}, \ldots, X_{n}$,
    * $X$のi.i.d
* $x_{i} := X_{i}(\omega)$,
* All expected values are at least 5

### Example
The steps for chi-square test for goodness of fit are as follows;

* (1) State the hypothesis
    * null hypothesis
        * $H_{0}:$ The data fits the proposed distribution
    * alternative hypothesis
        * $H_{A}:$ The data doesn't fit the proposed distribution
* (2) compute the test statistic


$$
\begin{eqnarray}
    j \in \{1, \ldots, m\},
    \
    u_{j}
    & = &
        \sum_{i :x_{i} = j}
            x_{i}
    \nonumber
    \\
    w
    & = &
        \sum_{i=1}^{m}
            \frac{
                (u_{j} - n p_{j})^{2}
            }{
                Np_{j}
            }
    \nonumber
\end{eqnarray}
$$

* (3) Compute $p$ value
    * $T \sim \mathrm{t}(N-1)$,
    * (a) $$
    p := P(T \le |t| \cup T \ge |t|)$$
    * (b) $p := P(T > t)$
    * (c) $p := P(T < t)$
* (4)
    * If $p < \alpha$, reject $H_{0}$,
    * otherwise, fail to reject $H_{0}$,

### Theory

#### Theorem21
$$X_{1}, \ldots, X_{N}$$, $$Y_{1}, \ldots, Y_{N}$$が正規分布に従っているとする。
また、$X_{i}$と$Y_{i}$が各$i$について独立とする。
このとき、

$$
    Z
    :=
    \frac{
        \bar{D}_{N} - \delta
    }{
        \sqrt{
            \frac{
                V_{N}(D_{1}, \ldots, D_{N})
            }{
                N
            }
        }
    }
    \sim
    t(N - 1)
$$

は、
ここで、

* $$D_{i} := X_{i} - Y_{i}$$,
* $$\bar{D}_{N} := \frac{\sum_{i=1}^{N} D_{i}}{N}$$,
* $$
    \displaystyle
    V_{N}(D_{1}, \ldots, D_{N})
    :=
    \frac{
        \sum_{i=1}^{N}
        (D_{i} - \bar{D}_{N})^{2}
    }{
        N - 1
    }
$$,

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>


#### Proposition 3
* $X \sim f(p_{1}, \ldots, p_{m})$,
    * $f$ is multinomial distribution
    * $\sum_{j=1}^{m}p_{j} = 1$,
    * $$X \in \{1, \ldots, m\}$$,
* $X_{1}, \ldots, X_{n}$,
    * I.I.D. of $X$
* $n \in \mathbb{N}$,
    * sample size
* $x_{j} := X_{j}(\omega)$

$$
\begin{eqnarray}
    j = 1, \ldots, m,
    \
    \bar{p}_{j}
    & := &
        \sum_{i:x_{i}=j} 
            \frac{
                1
            }{
                n
            }
    \nonumber
    \\
    W
    & := &
        \sum_{i=1}^{n}
            \frac{
                (X_{i} - n \bar{p}_{i})^{2}
            }{
                n \bar{p}_{i}
            }
    \nonumber
\end{eqnarray}
$$

Then $W$ has an approximate $\chi^{2}$ distribution with

* $r - m$ degree of freedom

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

## Chi square tests for Independence


## Chi square tests for Homegenity

## Reference
* [Pearson's chi\-squared test \- Wikipedia](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test)
