---
title: F-tests
---

## F-tests

## Definition

### F-distribution
* $N, M \in \mathbb{N}$,
* $U_{1} \sim \chi^{2}(N)$,
* $U_{2} \sim \chi^{2}(M)$,
* $U_{1}, U_{2}$ are independant

$$
    F
    :=
    \frac{
        U_{1}/N
    }{
        U_{2}/M
    }
    .
$$

Distribution of $F$ is said to be $F$-distribution with $N, M$ degree of freedom.
We denote $F(N, M)$.

## Two sample F test for population variances
$F$検定では、真の分布が正規分布の2つの分散が一致するか検定する。
$F$分布は$N$及び$M$によってのみ決まる。
つまり、正規分布の平均によらず、分散の検定ができる。

* $X \sim \mathrm{N}(\mu_{X}, \sigma_{X}^{2})$,
* $Y \sim \mathrm{N}(\mu_{Y}, \sigma_{Y}^{2})$,
* null hypothesis is that variances of $X$ and $Y$ are equal
* $X$, $Y$ are independent
* $\sigma_{X}$, $\sigma_{Y}$ are unkown

### Example
* $n \in \mathbb{N}$,
    * the sample size for $X$
* $m \in \mathbb{N}$,
    * the sample size for $Y$
* $\alpha \in (0, 1)$,
    * significance level
* $s_{X}^{2}$,
    * sample variance of $X$
* $s_{Y}^{2}$,
    * sample variance of $Y$


* (1) State the hypothesis
    * null hypothesis
        * $H_{0}:\sigma_{X} = \sigma_{Y} $
    * alternative hypothesis
        * (a) $H_{0}:\sigma_{X} \neq \sigma_{Y}$
        * (b) $H_{0}:\sigma_{X} > \sigma_{Y}$
        * (c) $H_{0}:\sigma_{X} < \sigma_{Y}$
* (2) compute the test statistic


$$
\begin{eqnarray}
    f
    =
    \frac{
        s_{X}^{2}
    }{
        s_{Y}^{2}
    }
\end{eqnarray}
$$

* (3) Compute $p$ value
    * $F \sim \mathrm{F}(n - 1, m - 1)$,
    * (a) $$
    p := 2P(F \ge f)$$
    * (b) $p := P(F \ge f)$
    * (c) $p := P(F \ge f)$
* (4)
    * If $p < \alpha$, reject $H_{0}$,
    * otherwise, fail to reject $H_{0}$,

### Theorem 25
* $X \sim \mathrm{N}(\mu_{X}, \sigma^{2})$,
* $Y \sim \mathrm{N}(\mu_{Y}, \sigma^{2})$,
* $$X_{1}, \ldots, X_{N}$$,
    * $X$のi.i.d
* $$Y_{1}, \ldots, Y_{M}$$,
    * $Y$のi.i.d

Then

$$
    F
    :=
    \frac{
        V_{N}(X_{1}, \ldots, X_{N})
    }{
        V_{M}(Y_{1}, \ldots, Y_{M})
    }
    \sim
    F(N - 1, M - 1)
    .
$$


### proof.
Let

$$
\begin{eqnarray}
    U_{X}
    & := &
        \frac{
            (N-1)
            V_{N}(X_{1}, \ldots, X_{N})
        }{
            \sigma^{2}
        },
    \nonumber
    \\
    U_{Y}
    & := &
        \frac{
            (M-1)
            V_{M}(Y_{1}, \ldots, Y_{N})
        }{
            \sigma^{2}
        }
    .
\end{eqnarray}
$$

$$U_{X} \sim \chi^{2}(N-1)$$, $$U_{Y} \sim \chi^{2}(M-1)$$.
Thus,

$$
\begin{eqnarray}
    F
    & = &
        \frac{
            V_{N}(X_{1}, \ldots, X_{N})
        }{
            V_{M}(Y_{1}, \ldots, Y_{M})
        }
    \nonumber
    \\
    & = &
        \frac{
            V_{N}(X_{1}, \ldots, X_{N})
        }{
            V_{M}(Y_{1}, \ldots, Y_{M})
        }
        \frac{
            \frac{
                1
            }{
                \sigma^{2}
            }
        }{
            \frac{
                1
            }{
                \sigma^{2}
            }
        }
        \frac{
            \frac{
                (N - 1)
            }{
                (N - 1)
            }
        }{
            \frac{
                (M - 1)
            }{
                (M - 1)
            }
        }
    \nonumber
    \\
    & = &
        \frac{
            \frac{
                (N - 1)
                V_{N}(X_{1}, \ldots, X_{N})
            }{
                \sigma^{2}
            }
        }{
            \frac{
                (M - 1)
                V_{M}(Y_{1}, \ldots, Y_{M})
            }{
                \sigma^{2}
            }
        }
        \frac{
            \frac{
                1
            }{
                (N - 1)
            }
        }{
            \frac{
            }{
                (M - 1)
            }
        }
    \nonumber
    \\
    & = &
        \frac{
            \frac{
                U_{X}
            }{
                (N - 1)
            }
        }{
            \frac{
                U_{Y}
            }{
                (M - 1)
            }
        }
    \nonumber
\end{eqnarray}
$$

The distribution of $F$ is $F(N - 1, M - 1)$.

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
