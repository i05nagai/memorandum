---
title: t tests
---

## t-tests
* the population is normally distributed
* the sample size is large enogh (e.g. $n \le 15$),
* do not use this test if there are outlier or the population is very skewed
    * skewness can be ignored if $n \le 40$
* the population standard deviation $\sigma$ is unkown

## Note
* An estimator is a r.v.
    * 推定量といった場合は確率変数
* Variable without subscption such as $X$, $Y$ denote true desitribution
    * 基本的に添え字なしの$X$, $Y$などは真の分布を表すのに使用する

## Definition
* $$X, X_{1}, \ldots, X_{N}$$,
    * r.v.
* $$Y, Y_{1}, \ldots, Y_{M}$$,
    * r.v.
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
    * sample mean
    * 平均の不偏推定量
* $$
    \displaystyle
    V_{N}(X_{1}, \ldots, X_{N})
    :=
    \frac{
        \sum_{i=1}^{N} (X_{i} - \bar{X}_{N})^{2}
    }{
        N - 1
    }
    \label{def_sample_variance}
$$,
    * unbiased estimator of variance
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

## one sample t-tests for population mean
正規分布に従う確率変数の平均値の検定。

* True distribution: $X \sim \mathrm{N}(\mu, \sigma)$
* The value of $\sigma$ is unkown
* the sample size is large enough that the mean is normally distributed
    * $n \ge 15$,
* skew can be ignored if $n \ge 40$,
* the population standard deviation $\sigma$ is unkown
* If $n \ge 30$, $t$ distribution can be approximated with the normal distribution
* In practice, $\sigma$ is rarely known

### Example
* $\mu_{0} \in \mathbb{R}$
    * mean for null hypothesis
* $n \in \mathbb{N}$,
    * sample size
* $x_{i} := X_{i}(\omega)$,
* $\alpha \in (0, 1)$,
    * significance level
    * 0.05, 0.01 are commonly used

$$
\begin{eqnarray}
    \bar{x}
    & := &
        \bar{X}_{n}(\omega)
    \nonumber
    \\
    s
    & := &
        \sqrt{V_{n}(X_{1}, \ldots, X_{n})(\omega)}
    \nonumber
\end{eqnarray}
$$

The steps for one-sample t-test for population mean are as follows;

* (1) State the hypotheses:
    * null hypothesis
        * $H_{0}$: $\mu = \mu_{0}$,
    * alternative hypothesis
        * (a) $H_{A}$: $\mu \neq \mu_{0}$,
        * (b) $H_{A}$: $\mu > \mu_{0}$,
        * (c) $H_{A}$: $\mu < \mu_{0}$,
* (2) Compute the test statistics
    * $\bar{x}$
        * the sample mean
    * $s$
        * the sample standard deviation

$$
\begin{eqnarray}
    t
    & = &
        \frac{
            \bar{x} - \mu_{0}
        }{
            \frac{s}{\sqrt{n}}
        }
\end{eqnarray}
$$

* (3) Compute the $p$ value
    * $T$ t distribution with $n - 1$ degree of freedom
    * (a) $$
p := P(T \le - |t| \cup T \ge - |t|)$$,
    * (b) $p := P(T > t)$,
    * (c) $p := P(T < t)$,
* (4)
    * If $p < \alpha$, reject $H_{0}$,
    * otherwise, fail to reject $H_{0}$,

### Lemma 5

$$
    \sum_{i=1}^{N} (X_{i} - \bar{X}_{N}) = 0
$$

### proof.
Easy to check.

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 19
* $X \sim \mathrm{N}(\mu, \sigma)$,
* $$X_{1}, \ldots, X_{N}$$,
    * $X$のi. i. d

$$
    \frac{
        (N - 1)V_{N}(X_{1}, \ldots, X_{N})
    }{
        \sigma^{2}
    }
    \sim
    \chi^{2}(N-1)
$$

が成立。

### proof.
まず、

$$
    \frac{
        (N - 1)V_{N}(X_{1}, \ldots, X_{N})
    }{
        \sigma^{2}
    }
    \sim
    \chi^{2}(N-1)
    =
    \frac{ 1 }{ \sigma^{2} }
    \sum_{i=1}^{N}
        (X_{i} - \bar{X}_{N})^{2}
$$

となるから、右辺の分布を求めれば良い。
天下り的に以下を計算する。

$$
\begin{eqnarray}
    \frac{1}{\sigma^{2}}
        \sum_{i=1}^{N}
            (X_{i} - \mu)^{2}
    & = &
        \frac{1}{\sigma^{2}}
        \sum_{i=1}^{N}
            \left(
                (X_{i} - \bar{X}_{N})
                +
                (\bar{X}_{N} - \mu)
            \right)^{2}
    \nonumber
    \\
    & = &
        \frac{1}{\sigma^{2}}
        \sum_{i=1}^{N}
            \left(
                (X_{i} - \bar{X}_{N})^{2}
                +
                2
                (X_{i} - \bar{X}_{N})
                (\bar{X}_{N} - \mu)
                +
                (\bar{X}_{N} - \mu)^{2}
            \right)
    \nonumber
    \\
    & = &
        \frac{1}{\sigma^{2}}
        \sum_{i=1}^{N}
            (X_{i} - \bar{X}_{N})^{2}
        +
        2
        \frac{1}{\sigma^{2}}
        (\bar{X}_{N} - \mu)
        \sum_{i=1}^{N}
            (X_{i} - \bar{X}_{N})
        +
        \frac{1}{\sigma^{2}}
        \sum_{i=1}^{N}
            (\bar{X}_{N} - \mu)^{2}
    \nonumber
    \\
    & = &
        \frac{1}{\sigma^{2}}
        \sum_{i=1}^{N}
            (X_{i} - \bar{X}_{N})^{2}
        +
        \frac{1}{\sigma^{2}}
        \sum_{i=1}^{N}
            (\bar{X}_{N} - \mu)^{2}
    \nonumber
    \\
    & = &
        \frac{(N-1)}{\sigma^{2}}
        V_{N}(X_{1}, \ldots, X_{N})
        +
        \frac{N}{\sigma^{2}}
        (\bar{X}_{N} - \mu)^{2}
    \nonumber
    \\
    & = &
        \frac{(N-1)}{\sigma^{2}}
        V_{N}(X_{1}, \ldots, X_{N})
        +
        \left(
            \frac{
                \bar{X}_{N} - \mu
            }{
                \frac{
                    \sigma
                }{
                    \sqrt{N}
                }
            }
        \right)^{2}
    \nonumber
\end{eqnarray}
$$

4つめの等式はLemma 5による。
ここで、

$$
\begin{eqnarray}
    U
    & := &
        \frac{1}{\sigma^{2}}
            \sum_{i=1}^{N}
                (X_{i} - \mu)^{2},
    \nonumber
    \\
    W
    & := &
        \frac{1}{\sigma^{2}}
        V_{N}(X_{1}, \ldots, X_{N})
    \nonumber
    \\
    V
    & := &
        \left(
            \frac{
                \bar{X}_{N} - \mu
            }{
                \frac{
                    \sigma
                }{
                    \sqrt{N}
                }
            }
        \right)^{2}
\end{eqnarray}
$$

とおくと、$W = U + V$である。

まず、$W$の分布を求める。

$$
    Z_{i}
    :=
    \frac{
        X_{i} - \bar{X}_{N}
    }{
        \sigma
    }
$$

とおくと、$$Z_{i} \sim \mathrm{N}(0, 1)$$で、各$Z_{i}$は独立である。
よって、

$$
\begin{eqnarray}
    \frac{
        (N - 1)V_{N}(X_{1}, \ldots, X_{N})
    }{
        \sigma^{2}
    }
    & = &
        \frac{
            (N - 1)
        }{
            \sigma^{2}
        }
        \frac{
            \sum_{i=1}^{N} (X_{i} - \bar{X}_{N})^{2}
        }{
            N - 1
        }
    \nonumber
    \\
    & = &
        \frac{
            \sum_{i=1}^{N} (X_{i} - \bar{X}_{N})^{2}
        }{
            \sigma^{2}
        }
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \left(
                \frac{
                     (X_{i} - \bar{X}_{N})
                }{
                    \sigma
                }
            \right)^{2}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            Z_{i}^{2}
\end{eqnarray}
$$

となって、$W \sim \chi^{2}(N)$である。
定理より、$\sqrt{V} \sim \mathrm{N}(0, 1)$で、特に$V \sim \chi^{2}(1)$である。
また、$W - V = U$であるから、両辺のMoment generating functionを計算すると

$$
\begin{eqnarray}
    M_{U}(t)
    & = &
        \frac{
            M_{W}(t)
        }{
            M_{V}(t)
        }
    \nonumber
    \\
    & = &
        \frac{
            (1 - 2t)^{-N/2}
        }{
            (1 - 2t)^{-1/2}
        }
    \nonumber
    \\
    & = &
        (1 - 2t)^{-(n-1)/2}
\end{eqnarray}
$$

となる。
よって、$U \sim \chi^{2}(N-1)$である。

<div class="QED" style="text-align: right">$\Box$</div>


### Thereom 20
$$X_{1}, \ldots, X_{N}$$が独立な確率変数とする。
$$X_{i} \sim \mathrm{N}(\mu, \sigma^{2})$$とする。
このとき、

$$
    \frac{
        \bar{X}_{N} - \mu
    }{
        \sqrt{
            \frac{
                V_{N}(X_{1}, \dots, X_{N})
            }{
                N
            }
        }
    }
    \sim
    t(N-1)
$$

である。

### proof.
まず、

$$
\begin{eqnarray}
    U
    & := &
        \frac{
            (N-1) V_{N}(X_{1}, \dots, X_{N})
        }{
            \sigma^{2}
        }
    \nonumber
    \\
    Z
    & := &
        \frac{
            \bar{X}_{N} - \mu
        }{
            \sqrt{
                \frac{
                    \sigma^{2}
                }{
                    N
                }
            }
        }
    \nonumber
\end{eqnarray}
$$

とおくと、定理より$Z \sim \mathrm{N}(0, 1)$かつ$U \sim \chi^{2}(N-1)$である。

$$
\begin{eqnarray}
    \frac{
        \bar{X}_{N} - \mu
    }{
        \sqrt{
            \frac{
                V_{N}(X_{1}, \ldots, X_{N})
            }{
                N
            }
        }
    }
    & = &
        \frac{1}{V_{N}(X_{1}, \ldots, X_{N})}
        \frac{
            \bar{X}_{N} - \mu
        }{
            \frac{
                1
            }{
                \sqrt{N}
            }
        }
        \sqrt{
            \frac{
                \sigma^{2}
            }{
                \sigma^{2}
            }
        }
    \nonumber
    \\
    & = &
        \sqrt{
            \frac{\sigma^{2}}{V_{N}}
        }
        \frac{
            \bar{X}_{N} - \mu
        }{
            \frac{
                \sigma^{2}
            }{
                \sqrt{N}
            }
        }
    \nonumber
    \\
    & = &
        \sqrt{
            \frac{(N-1)\sigma^{2}}{(N-1)V_{N}(X_{1}, \ldots, X_{N})}
        }
        Z
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            \sqrt{
                \frac{
                    (N-1)V_{N}(X_{1}, \ldots, X_{N})
                }{
                    (N-1)\sigma^{2}
                }
            }
        }
        Z
    \nonumber
    \\
    & = &
        \frac{
            Z
        }{
            \sqrt{
                \frac{
                    U
                }{
                    (N-1)
                }
            }
        }
    \nonumber
\end{eqnarray}
$$

となる。

<div class="QED" style="text-align: right">$\Box$</div>

## paired samples t-test for the population mean of paired samples
正規分布に従う確率変数差の平均値の検定。

* True distribution: $X \sim \mathrm{N}(\mu_{X}, \sigma)$
* True distribution: $Y \sim \mathrm{N}(\mu_{Y}, \sigma)$
* two samples are paired
    * Here paired means that $X$ and $Y$ has same sample size $n$
* The value of $\sigma$ is uknown but $X$ and $Y$ has same $\sigma$
* both normal distribution
* both simze sizes are large enough
    * $n \ge 15$,


### Example
* $D \in \mathbb{R}$,
    * the difference mean
* $n \in \mathbb{N}$,
    * the sample size
* $X_{1}, \ldots, X_{n}$,
    * i.i.d. of $X$
* $Y_{1}, \ldots, Y_{n}$,
    * i.i.d. of $Y$
* $D_{1} := X_{1} - Y_{1}, \ldots, D_{n} := X_{n} - Y_{n}$,
    * i.i.d. of $D := X - Y$,
* $$s_{d} := \mathrm{Var}_{n}(D_{1}, \ldots, D_{N})(\omega)$$,
    * sample standard deviation of $D$
* $\alpha \in (0, 1)$,
    * significance level



* (1) State the hypothesis
    * null hypothesis
        * $H_{0}:\mu_{D} = D $
    * alternative hypothesis
        * (a) $H_{0}:\mu_{D} \neq D $
        * (b) $H_{0}:\mu_{D} > D $
        * (c) $H_{0}:\mu_{D} < D $
* (2) compute the test statistic


$$
\begin{eqnarray}
    t
    =
    \frac{
        \bar{d}
        -
        D
    }{
        \frac{s_{d}}{\sqrt{n}}
    }
\end{eqnarray}
$$

* (3) Compute $p$ value
    * $T \sim \mathrm{t}(n-1)$,
    * (a) $$
    p := P(T \le |t| \cup T \ge |t|)$$
    * (b) $p := P(T > t)$
    * (c) $p := P(T < t)$
* (4)
    * If $p < \alpha$, reject $H_{0}$,
    * otherwise, fail to reject $H_{0}$,

### Theorem21
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

### proof.
$D_{i}$は正規分布に従うから、前定理の結果をそのままあてはめれば良い。


<div class="QED" style="text-align: right">$\Box$</div>

## Two sample t-test for population means (equal variances)
Test for means of two random variables with normal distribution whose variances are equal.

* True distribution: $X \sim \mathrm{N}(\mu_{X}, \sigma)$
* True distribution: $Y \sim \mathrm{N}(\mu_{Y}, \sigma)$
* $X$, $Y$ are independent
* $n$ is the sample size of $X$
* $m$ is the sample size of $Y$
* Two sample means that the sample size can be different
* $\sigma$ are unkown but euqal to the other
    * weired situation

In practical, $D = 0$.

## Example
* $D \in \mathbb{R}$,
    * the difference of means to be tested
* $n \in \mathbb{N}$,
    * the sample size of $X$
* $m \in \mathbb{N}$,
    * the sample size of $Y$
* $X_{1}, \ldots, X_{N}$,
    * i.i.d. of $X$
* $Y_{1}, \ldots, Y_{M}$,
    * i.i.d. of $Y$
* $\bar{X}_{N}$,
    * estimator of mean of $X$,
* $\bar{Y}_{M}$,
    * estimator of mean of $Y$,
* $\mu_{X} := \bar{X}_{N}(\omega)$,
* $\mu_{Y} := \bar{Y}_{M}(\omega)$,
* $$S_{X} := \mathrm{Var}_{N}(X_{1}, \ldots, X_{N})$$,
    * sample standard deviation of $X$
* $$S_{Y} := \mathrm{Var}_{M}(Y_{1}, \ldots, Y_{M})$$,
    * sample standard deviation of $Y$
* $$s_{X} := S_{X}(\omega)$$,
* $$s_{Y} := S_{Y}(\omega)$$,
* $\alpha \in (0, 1)$,
    * significance level

The steps for two-sample t-tests for population mean are as follows;

* (1) State the hypothesis
    * null hypothesis
        * $H_{0}:\mu_{X} - \mu_{Y} = D$,
    * alternative hypothesis
        * (a) $H_{A}:\mu_{X} - \mu_{Y} \neq D $
        * (b) $H_{A}:\mu_{X} - \mu_{Y} > D $
        * (c) $H_{A}:\mu_{X} - \mu_{Y} < D $
* (2) compute the test statistic


$$
\begin{eqnarray}
    t
    & = &
    \frac{
        (\mu_{X} - \mu_{Y})
        -
        D
    }{
        \sqrt{
            s_{P}^{2}
            \left(
                \frac{1}{N}
                +
                \frac{1}{M}
            \right)
        }
    }
    \nonumber
    \\
    s_{P}^{2}
    & := &
        \frac{
            (N - 1)^{2}s_{X}^{2}
            +
            (M - 1)^{2}s_{Y}^{2}
        }{
            N + M - 2
        }
    \nonumber
\end{eqnarray}
$$

* (3) Compute $p$ value
    * $T \sim \mathrm{t}(n m - 2)$,
    * (a) $$
    p := P(T \le |t| \cup T \ge |t|)$$
    * (b) $p := P(T > t)$
    * (c) $p := P(T < t)$
* (4)
    * If $p < \alpha$, reject $H_{0}$,
    * otherwise, fail to reject $H_{0}$,

### Lemma 6
Suppose that $$\{ X_{i} \}_{i=1}^{N}$$ and $$\{ Y_{i}\}_{i=1}^{M}$$ are independent.

* $$X_{i} \sim \mathrm{N}(\mu_{X}, \sigma^{2})$$,
    * i.i.d.
* $$Y_{i} \sim \mathrm{N}(\mu_{Y}, \sigma^{2})$$,
    * i.i.d.

Then

$$
    \bar{X}_{N} - \bar{Y}_{M}
    \sim
    \mathrm{N}
        \left(
            \mu_{X} - \mu_{Y},
            \sigma^{2}
                \left(
                    \frac{1}{N}
                    +
                    \frac{1}{M}
                \right)
        \right).
$$

### proof.
By Lemma3, it follows that

$$
\begin{eqnarray}
    \bar{X}_{N}
    & \sim &
        \mathrm{N}(\mu_{X}, \frac{\sigma^{2}}{N}),
    \nonumber
    \\
    \bar{Y}_{M}
    & \sim &
        \mathrm{N}(\mu_{Y}, \frac{\sigma^{2}}{M}),
    \nonumber
\end{eqnarray}
.
$$

Since the sum of the independet normally distributed r.v.s follows normal distribution, we have

$$
\begin{eqnarray}
    \bar{X}_{N} - \bar{Y}_{M}
    & = &
        \bar{X}_{N} + (-1)\bar{Y}_{M}
    \nonumber
    \\
    & \sim &
        \mathrm{N}
        \left(
           \mu_{X} - \mu_{Y},
           \frac{ \sigma^{2} }{ N }
           +
           (-1)^{2}
           \frac{ \sigma^{2} }{ M }
        \right)
    \nonumber
\end{eqnarray}
.
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Lemma 7
* $$X \sim \mathrm{N}(\mu_{X}, \sigma^{2})$$,
* $$Y \sim \mathrm{N}(\mu_{Y}, \sigma^{2})$$,
* $$X_{1}, \ldots, X_{N}$$,
    * i.i.d. of $X$
* $$Y_{1}, \ldots, Y_{M}$$,
    * i.i.d. of $Y$
* $$\{X_{i} \}$$ and $$\{Y_{i}\}$$ are independent

Then

$$
    \frac{
        \bar{X}_{N} - \bar{Y}_{M}
        -
        (\mu_{X} - \mu_{Y})
    }{
        \sigma
        \sqrt{
            \frac{
                \frac{ 1 }{ N }
            }{
                \frac{1}{M}
            }
        }
    }
    \sim
    \mathrm{N}(0, 1)
$$

### proof.
By lemma6, it follows that

$$
    \bar{X}_{N}
    -
    \bar{X}_{M}
    \sim
    \mathrm{N}
        \left(
            \mu_{X} - \mu_{Y},
            \sigma^{2}
                \left(
                    \frac{1}{N}
                    +
                    \frac{1}{M}
                \right)
        \right)
    .
$$

Thus, the statement holds.

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 22
* $$X \sim \mathrm{N}(\mu_{X}, \sigma)$$,
* $$Y \sim \mathrm{N}(\mu_{Y}, \sigma)$$,
* $$X_{1}, \ldots, X_{N}$$,
    * i.i.d. of $X$
* $$Y_{1}, \ldots, Y_{M}$$,
    * i.i.d. of $Y$
* $$\{X_{i} \}$$ and $$\{Y_{i}\}$$ are independent

Then

$$
    T
    :=
    \frac{
        (\bar{X}_{N} - \bar{Y}_{M})
        -
        (\mu_{X} - \mu_{Y})
    }{
        \sqrt{
            V_{N}^{P}
            \left(
                \frac{1}{N}
                +
                \frac{1}{M}
            \right)
        }
    }
    \sim
    t(N + M - 2)
$$

where

$$
\begin{eqnarray}
    V^{P}
    & := &
        \frac{
            (N-1)V_{N}(X_{1}, \ldots, X_{N}) + (M - 1)V_{M}(Y_{1}, \ldots, Y_{M})
        }{
            N + M - 2
        }
    .
    \nonumber
\end{eqnarray}
$$

### proof.
まず、 前定理より

$$
\begin{eqnarray}
    Z
    & := &
        \frac{
            (\bar{X}_{N} - \bar{Y}_{M})
            -
            (\mu_{X} - \mu_{Y})
        }{
            \sigma
            \sqrt{
                \frac{1}{N}
                +
                \frac{1}{M}
            }
        },
    \nonumber
    \\
    & \sim &
        \mathrm{N}(0, 1)
    \nonumber
    \\
    U_{1}
    & := &
        \frac{
            (N - 1) V_{N}(X_{1}, \ldots, X_{N})
        }{
            \sigma^{2}
        }
    \nonumber
    \\
    & \sim &
        \chi^{2}(N - 1)
    \nonumber
    \\
    U_{2}
    & := &
        \frac{
            (M-1) V_{M}(Y_{1}, \ldots, Y_{M})
        }{
            \sigma^{2}
        }
    \nonumber
    \\
    & \sim &
        \chi^{2}(M - 1)
    \nonumber
    \\
    U
    & := &
        U_{1} + U_{2}
    \nonumber
    \\
    & \sim &
        \chi^{2}(N + M - 2)
    \nonumber
\end{eqnarray}
$$

となる。
$Z$は前定理より、$U$は$\chi^{2}$分布に従う確率変数の和はまた、$\chi^{2}$分布に従うことによる。

$$
\begin{eqnarray}
    T
    & = &
        \frac{
            (\bar{X}_{N} - \bar{Y}_{M})
            -
            (\mu_{X} - \mu_{Y})
        }{
            \sqrt{
                \frac{
                    (N-1)V_{N}(X_{1}, \ldots, X_{N}) + (M - 1)V_{M}(Y_{1}, \ldots, Y_{M})
                }{
                    N + M - 2
                }
                \left(
                    \frac{1}{N}
                    +
                    \frac{1}{M}
                \right)
            }
        }
        \frac{ \sigma }{ \sigma }
    \nonumber
    \\
    & = &
        \frac{
            (\bar{X}_{N} - \bar{Y}_{M})
            -
            (\mu_{X} - \mu_{Y})
        }{
            \sigma
            \sqrt{
                \left(
                    \frac{1}{N}
                    +
                    \frac{1}{M}
                \right)
            }
        }
        \frac{
            \sigma
        }{
            \sqrt{
                \frac{
                    (N-1)V_{N}(X_{1}, \ldots, X_{N}) + (M - 1)V_{M}(Y_{1}, \ldots, Y_{M})
                }{
                    N + M - 2
                }
            }
        }
    \nonumber
    \\
    & = &
        Z
        \sqrt{
            \frac{
                1
            }{
                \frac{
                    \frac{
                        (N-1)V_{N}(X_{1}, \ldots, X_{N})
                    }{
                        \sigma^{2}
                    }
                    + 
                    \frac{
                        (M - 1)V_{M}(Y_{1}, \ldots, Y_{M})
                    }{
                        \sigma^{2}
                    }
                }{
                    N + M - 2
                }
            }
        }
    \nonumber
    \\
    & = &
        \frac{
            Z
        }{
            \sqrt{
                \frac{
                    U
                }{
                    N + M - 2
                }
            }
        }
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Two sample t-test for population means (unequal variances)
分散が等しくない場合の正規分布に従う2つの確率変数の平均値の検定。
検定において、分布を近似しているので、この近似の意味で検定が成り立つことに注意する。

* True distribution: $X \sim \mathrm{N}(\mu_{X}, \sigma_{X}^{2})$
* True distribution: $Y \sim \mathrm{N}(\mu_{Y}, \sigma_{Y}^{2})$
* $N$ is the sample size of $X$
* $M$ is the sample size of $Y$
* Two sample means that the sample size can be different
* $\sigma_{X}$ and $\sigma_{Y}$ are unkown but are not equal.
* $\mu_{X} - \mu_{Y} = D$ is null hypothesis 

### Example
* $D \in \mathbb{R}$,
    * the difference of means
* $N \in \mathbb{N}$,
    * the sample size of $X$,
* $M \in \mathbb{N}$,
    * the sample size of $Y$,
* $X_{1}, \ldots, X_{N}$,
    * i.i.d. of $X$
* $Y_{1}, \ldots, Y_{M}$,
    * i.i.d. of $Y$
* $$\bar{x}_{N} := \bar{X}_{N}(\omega)$$,
* $$\bar{y}_{M} := \bar{Y}_{M}(\omega)$$,
* $$S_{X} := \mathrm{Var}_{n}(X_{1}, \ldots, X_{N})$$,
    * sample standard deviation of $X$
* $$S_{Y} := \mathrm{Var}_{m}(Y_{1}, \ldots, Y_{M})$$,
    * sample standard deviation of $Y$
* $$s_{X} := S_{X}(\omega)$$,
* $$s_{Y} := S_{Y}(\omega)$$,
* $\alpha \in (0, 1)$,
    * significance level

The steps for two sample t-tests are as follows;

* (1) State the hypothesis
    * null hypothesis
        * $$H_{0}:\bar{x}_{N} - \bar{y}_{M} = D$$,
    * alternative hypothesis
        * (a) $$H_{A}:\bar{x}_{N} - \bar{y}_{M} \neq D$$,
        * (b) $$H_{A}:\bar{x}_{N} - \bar{y}_{M} > D $$,
        * (c) $$H_{A}:\bar{x}_{N} - \bar{y}_{M} < D $$,
* (2) compute the test statistic


$$
\begin{eqnarray}
    t
    & = &
        \frac{
            (\bar{x}_{N} - \bar{y}_{M})
            -
            D
        }{
            \sqrt{
                \frac{s_{X}^{2}}{N}
                +
                \frac{s_{Y}^{2}}{M}
            }
        }
    \nonumber
    \\
    df
    & := &
        \frac{
            \left(
                \frac{s_{X}^{2}}{N}
                +
                \frac{s_{y}^{2}}{M}
            \right)^{2}
        }{
            \frac{
                s_{X}^{4}
            }{
                N^{2}(N - 1)
            }
            +
            \frac{
                s_{Y}^{4}
            }{
                M^{2}(M - 1)
            }
        }
    \nonumber
\end{eqnarray}
$$

* (3) Compute $p$ value
    * $T \sim \mathrm{t}(df)$,
    * (a) $$
    p := P(T \le |t| \cup T \ge |t|)$$
    * (b) $p := P(T > t)$
    * (c) $p := P(T < t)$
* (4)
    * If $p < \alpha$, reject $H_{0}$,
    * otherwise, fail to reject $H_{0}$,

### Theory

#### Lemma 8
* $$X \sim \mathrm{N}(\mu, \sigma)$$,
* $$X_{1} ,\ldots, X_{N}$$,
    * i.i.d. of $X$

Then

$$
\begin{equation}
    \mathrm{Var}
    \left[
        V_{N}(X_{1}, \ldots, X_{N})
    \right]
    =
    \frac{
        2 \sigma^{4}
    }{
        N - 1
    }
\end{equation}
$$

#### proof.
By Theorem 19, it follows that

$$
\begin{equation}
    \frac{
        (N - 1) V_{N}(X_{1} ,\ldots, X_{N})
    }{
        \sigma^{2}
    }
    \sim
    \chi_{N-1}^{2}
\end{equation}
$$

Hence

$$
    \mathrm{Var}
    \left[
        \frac{
            (N - 1) V_{N}(X_{1} ,\ldots, X_{N})
        }{
            \sigma^{2}
        }
    \right]
    =
    2 (N - 1)
    .
$$

On the other hand,

$$
\begin{eqnarray}
    \mathrm{Var}
    \left[
        \frac{
            (N - 1) V_{N}(X_{1} ,\ldots, X_{N})
        }{
            \sigma^{2}
        }
    \right]
    & = &
        \frac{
            (N - 1)^{2}
        }{
            \sigma^{4}
        }
        \mathrm{Var}
        \left[
            V_{N}(X_{1} ,\ldots, X_{N})
        \right]
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    & &
        \frac{
            (N - 1)^{2}
        }{
            \sigma^{4}
        }
        \mathrm{Var}
        \left[
            V_{N}(X_{1} ,\ldots, X_{N})
        \right]
        =
        2 (N - 1)
    \nonumber
    \\
    & \Leftrightarrow &
        \mathrm{Var}
        \left[
            V_{N}(X_{1} ,\ldots, X_{N})
        \right]
        =
        \frac{
            2 \sigma^{4}
        }{
            (N - 1)
        }
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 23

$$
    \hat{\beta}
    \frac{
        \frac{
            V_{N}(X_{1}, \ldots, X_{N})
        }{
            N
        }
        +
        \frac{
            V_{M}(Y_{1}, \ldots, Y_{M})
        }{
            M
        }
    }{
        \frac{
            \sigma^{2}_{X}
        }{
            N
        }
       +
       \frac{
           \sigma_{Y}^{2}
       }{
           M
       }
    }
    \overset{\mathrm{approx}}{\sim}
    \chi_{\hat{\beta}}^{2},
$$

ここで、

$$
\begin{equation}
    \hat{\beta}
    :=
    \frac{
        \left(
            \frac{
                V_{N}(X_{1}, \ldots, X_{N})
            }{
                N
            }
            +
            \frac{
                V_{M}(Y_{1}, \ldots, Y_{M})
            }{
                M
            }
        \right)^{2}
    }{
        \frac{
            V_{N}(X_{1}, \ldots, X_{N})^{2}
        }{
            N(N-1)
        }
        +
        \frac{
            V_{M}(Y_{1}, \ldots, Y_{N})^{2}
        }{
            M(M-1)
        }
    }
\end{equation}
$$

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>


#### Theorem 24
* $X \sim \mathrm{N}(\mu_{X}, \sigma_{X}^{2})$,
* $Y \sim \mathrm{N}(\mu_{Y}, \sigma_{Y}^{2})$,
* $$X_{1}, \ldots, X_{N}$$,
    * i.i.d. of $X$
* $$Y_{1}, \ldots, Y_{M}$$,
    * i.i.d. of $y$

Then

$$
    T
    :=
    \frac{
        (\bar{X}_{N} - \bar{Y}_{M})
        -
        (\mu_{X} - \mu_{Y})
    }{
        \sqrt{
            \frac{
                V_{N}(X_{1}, \ldots, X_{N})
            }{
                N
            }
            +
            \frac{
                V_{M}(Y_{1}, \ldots, Y_{M})
            }{
                M
            }
        }
    }
    \overset{\mathrm{approx}}{\sim}
    t(v)
$$

ここで、

$$
    v
    :=
    \frac{
        \left(
            \frac{
                V_{N}(X_{1}, \ldots, X_{N})
            }{
                N
            }
            +
            \frac{
                V_{M}(Y_{1}, \ldots, Y_{M})
            }{
                M
            }
        \right)^{2}
    }{
        \frac{
            V_{N}(X_{1}, \ldots, X_{N})^{2}
        }{
            N^{2}(N - 1)
        }
        +
        \frac{
            V_{M}(Y_{1}, \ldots, Y_{M})^{2}
        }{
            M^{2}(M - 1)
        }
    }
$$

である。

#### proof.
まず、

$$
    Z
    :=
    \frac{
        (\bar{X}_{N} - \bar{Y}_{M})
        -
        (\mu_{X} - \mu_{Y})
    }{
        \sqrt{
            \frac{
                \sigma_{X}^{2}
            }{
                N
            }
            +
            \frac{
                \sigma_{Y}^{2}
            }{
                M
            }
        }
    }
$$

とおくと、$Z \sim \mathrm{N}(0, 1)$となる。
また、前定理より、

$$
    V
    :=
    \hat{\beta}
    \frac{
        \frac{
            V_{N}(X_{1}, \ldots, X_{N})
        }{
            N
        }
        +
        \frac{
            V_{M}(Y_{1}, \ldots, Y_{M})
        }{
            M
        }
    }{
        \frac{
            \sigma_{X}^{2}
        }{
            N
        }
        +
        \frac{
            \sigma_{Y}^{2}
        }{
            M
        }
    }
$$

とすると、$$V \overset{\mathrm{approx}}{\sim} \chi_{\hat{\beta}}^{2}$$である。
以上をふまえ、

$$
\begin{eqnarray}
    T
    & = &
        \frac{
            (\bar{X}_{N} - \bar{Y}_{M})
            -
            (\mu_{X} - \mu_{Y})
        }{
            \sqrt{
                \frac{
                    V_{N}(X_{1}, \ldots, X_{N})
                }{
                    N
                }
                +
                \frac{
                    V_{M}(Y_{1}, \ldots, Y_{M})
                }{
                    M
                }
            }
        }
        \frac{
            \hat{\beta}
            \sqrt{
                \frac{
                    \sigma_{X}^{2}
                }{
                    N
                }
                +
                \frac{
                    \sigma_{Y}^{2}
                }{
                    M
                }
            }
        }{
            \hat{\beta}
            \sqrt{
                \frac{
                    \sigma_{X}^{2}
                }{
                    N
                }
                +
                \frac{
                    \sigma_{Y}^{2}
                }{
                    M
                }
            }
        }
    \nonumber
    \\
    & = &
        \frac{
            (\bar{X}_{N} - \bar{Y}_{M})
            -
            (\mu_{X} - \mu_{Y})
        }{
            \sqrt{
                \frac{
                    \sigma_{X}^{2}
                }{
                    N
                }
                +
                \frac{
                    \sigma_{Y}^{2}
                }{
                    M
                }
            }
        }
        \left(
            \frac{
                \hat{\beta}
                \sqrt{
                    \frac{
                        V_{N}(X_{1}, \ldots, X_{N})
                    }{
                        N
                    }
                    +
                    \frac{
                        V_{M}(Y_{1}, \ldots, Y_{M})
                    }{
                        M
                    }
            }
            }{
                \hat{\beta}
                \sqrt{
                    \frac{
                        \sigma_{X}^{2}
                    }{
                        N
                    }
                    +
                    \frac{
                        \sigma_{Y}^{2}
                    }{
                        M
                    }
                }
            }
        \right)^{-1}
    \nonumber
    \\
    & = &
        \hat{\beta}
        \frac{
            Z
        }{
            \sqrt{
                \frac{
                    V
                }{
                    \hat{\beta}
                }
            }
        }
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Student's t\-test \- Wikipedia](https://en.wikipedia.org/wiki/Student%27s_t-test#Slope_of_a_regression_line)