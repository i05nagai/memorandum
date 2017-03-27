---
title: F-tests
---

## F-tests

## Definition
* $$U_{1} \sim \chi_{N}$$,
* $$U_{2} \sim \chi_{M}$$,
* $$U_{1}, U_{2}$$が独立

$$
    F
    :=
    \frac{
        U_{1}/N
    }{
        U_{2}/M
    }
$$

の従う分布を自由度$N, M$の$F$分布といい、$F(N, M)$とかく。

## Two sample F test for population variances
* $X \sim \mathrm{N}(\mu_{X}, \sigma^{2})$,
* $Y \sim \mathrm{N}(\mu_{Y}, \sigma^{2})$,

### Theorem 25
* $X \sim \mathrm{N}(\mu_{X}, \sigma^{2})$,
* $Y \sim \mathrm{N}(\mu_{Y}, \sigma^{2})$,
* $$X_{1}, \ldots, X_{N}$$,
    * $X$のi.i.d
* $$Y_{1}, \ldots, Y_{M}$$,
    * $Y$のi.i.d

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
$$

である。

### proof.
まず、

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
        },
\end{eqnarray}
$$

とすると、$$U_{X} \sim \chi^{2}(N-1)$$, $$U_{Y} \sim \chi^{2}(M-1)$$となる。
よって、

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

となってこれは、$F(N - 1, M - 1)$に従う。

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
