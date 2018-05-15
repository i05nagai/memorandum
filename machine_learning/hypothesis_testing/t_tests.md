---
title: t tests
---

## t-tests

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
    V_{N}(X_{1}, \ldots, X_{N})
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

## one sample t-tests for population mean
正規分布に従う確率変数差の平均値の検定。

* 真の分布$X \sim \mathrm{N}(\mu, \sigma)$
* $\sigma$の値は不明だが、一致していることは事前に知っている

### Lemma 5

$$
    \sum_{i=1}^{N} (X_{i} - \bar{X}_{N}) = 0
$$

### proof.
計算すればよい。

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

* 真の分布$X \sim \mathrm{N}(\mu_{X}, \sigma)$
* 真の分布$Y \sim \mathrm{N}(\mu_{Y}, \sigma)$
* $\sigma$の値は不明だが、一致していることは事前に知っている


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
分散が等しい場合の正規分布に従う2つの確率変数の平均値の検定

* 真の分布$X \sim \mathrm{N}(\mu_{X}, \sigma)$が正規分布に従う
* 真の分布$Y \sim \mathrm{N}(\mu_{Y}, \sigma)$が$X$と分散の等しい正規分布に従う
* $\sigma$の値は不明だが、一致していることは事前に知っている必要がある

### Lemma 6
$$\{ X_{i} \}_{i=1}^{N}$$と$$\{ Y_{i}\}_{i=1}^{M}$$が独立とする。

* $$X_{i} \sim \mathrm{N}(\mu_{X}, \sigma^{2})$$,
* $$Y_{i} \sim \mathrm{N}(\mu_{Y}, \sigma^{2})$$,

とする。
このとき、

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
Lemma3より

$$
\begin{eqnarray}
    \bar{X}_{N}
    & \sim &
        \mathrm{N}(\mu_{X}, \frac{\sigma^{2}}{N}),
    \nonumber
    \\
    \bar{Y}_{N}
    & \sim &
        \mathrm{N}(\mu_{Y}, \frac{\sigma^{2}}{M}),
\end{eqnarray}
$$

となる。
また、2つの正規分布に従う確率変数の和はまた、正規分布に従うので、

$$
\begin{eqnarray}
    \bar{X}_{N} - \bar{Y}_{M}
    & = &
        \bar{X}_{N} + (-1)\bar{Y}_{M}
    \nonumber
    \\
    & \sim &
       \mathrm{N}(\mu_{X} - \mu_{Y},
           \frac{ \sigma^{2} }{ N }
           +
           (-1)^{2}
           \frac{ \sigma^{2} }{ M }
       )
    \nonumber
\end{eqnarray}
$$

となる。

<div class="QED" style="text-align: right">$\Box$</div>

### Lemma 7
* $$X \sim \mathrm{N}(\mu_{X}, \sigma^{2})$$,
* $$Y \sim \mathrm{N}(\mu_{Y}, \sigma^{2})$$,
* $$X_{1}, \ldots, X_{N}$$,
    * $X$と同分布
* $$Y_{1}, \ldots, Y_{M}$$,
    * $Y$と同分布
* $$\{X_{i} \}$$と$$\{Y_{i}\}$$が独立

このとき、

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
前Lemmaより、

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
$$

なので、平均を引いて標準偏差で割ったものを考えれば良い。

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 22
* $$X \sim \mathrm{N}(\mu_{X}, \sigma)$$,
* $$Y \sim \mathrm{N}(\mu_{Y}, \sigma)$$,
* $$X_{1}, \ldots, X_{N}$$,
    * $X$と同分布
* $$Y_{1}, \ldots, Y_{M}$$,
    * $Y$と同分布
* $$\{X_{i} \}$$と$$\{Y_{i}\}$$が独立

このとき、

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

である。
ただし、

$$
\begin{eqnarray}
    V^{P}
    & := &
        \frac{
            (N-1)V_{N}(X_{1}, \ldots, X_{N}) + (M - 1)V_{M}(Y_{1}, \ldots, Y_{M})
        }{
            N + M - 2
        }
    \nonumber
\end{eqnarray}
$$

である。

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

* 真の分布$X \sim \mathrm{N}(\mu_{X}, \sigma_{X}^{2})$が正規分布に従う
* 真の分布$Y \sim \mathrm{N}(\mu_{Y}, \sigma_{Y}^{2})$が正規分布に従う
* $\sigma$の値は不明だが、一致していないことは事前に知っている必要がある
* $\mu_{X} \neq \mu_{Y}$が帰無仮説

### Lemma 8
* $$X \sim \mathrm{N}(\mu, \sigma)$$,
* $$X_{1} ,\ldots, X_{N}$$,
    * $X$と同分布

このとき、

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

### proof.
Theorem 19 より、

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

である。
よって、

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
$$

である。
一方

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

である。
よって、

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

### Theorem 23

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

### proof.

<div class="QED" style="text-align: right">$\Box$</div>


### Theorem 24
* $X \sim \mathrm{N}(\mu_{X}, \sigma_{X}^{2})$,
* $Y \sim \mathrm{N}(\mu_{Y}, \sigma_{Y}^{2})$,
* $$X_{1}, \ldots, X_{N}$$,
    * $X$と同分布
* $$Y_{1}, \ldots, Y_{M}$$,
    * $Y$と同分布

このとき、

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

### proof.
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

