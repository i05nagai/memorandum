---
title: Chapter3-05. Conditional expectation
book_title: Mathematical statistics
book_chapter: 3
book_section: 5-20
---

### Problem 3.20
* $X_{i} \sim N(\mu, \sigma) \ (i = 1, \ldots, n)$
    * i.i.d.

$$
\begin{eqnarray}
    T_{1}
    & := &
        \sum_{j=1}^{n}
            (X_{i} - \mu)
    \nonumber
    \\
    T_{2}
    & := &
        \sum_{j=1}^{n}
            (X_{i} - \mu)^{2}
    \nonumber
\end{eqnarray}
$$

Then the followings hold:

* (1) $T_{1}$ and $T_{2}$ are independet,

* (2) $T_{1}$ is normal distribution $N(0, n\sigma^{2})$, that is, p.d.f. $f_{T_{1}}$ of $T_{1}$ is given by

$$
    f_{T_{1}}(t_{1})
    =
    \frac{
        1
    }{
        (2 \pi n \sigma^{2})^{1/2}
    }
    \exp
    \left(
        \frac{1}{2 n \sigma^{2}}
        t^{2}
    \right)
$$

* (3) $T_{2}$ is $\xi^{2}$ distribution with $n$ degree of freedom, that is, p.d.f. $f_{T_{2}}$ of $T_{2}$ is given by

$$
    f_{T_{1}}(t_{1})
    =
    \frac{
        1
    }{
        (2 \pi n \sigma^{2})^{1/2}
    }
    \exp
    \left(
        \frac{1}{2 n \sigma^{2}}
        t^{2}
    \right)
$$


### proof

$$
\begin{eqnarray}
    \bar{X}
    & := &
        \frac{1}{n}
        \sum_{j=1}^{n}
            X_{j}
        \sim
        \mathrm{N}(\mu, \sigma^{2})
    \nonumber
    \\
    S
    & := &
        \frac{1}{n}
        \sum_{j=1}^{n}
            (X_{j} - \bar{X})^{2}
    \nonumber
    \\
    Y
    & := &
        \frac{
            nS
        }{
            \sigma^{2}(n - 1)
        }
        \sim
        \chi^{2}(n - 1)
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    p_{\bar{X}, Y}(\bar{x}, y)
    & := &
        p_{\bar{X}}(\bar{x})
        p_{Y}(y)
    \nonumber
    \\
    & = &
        \frac{1}{(2\pi\sigma^{2})^{1/2}}
        \exp
        \left(
            -
            \frac{1}{2\sigma^{2}}
            (\bar{x} - \mu)^{2}
        \right)
        \frac{1}{\Gamma((n - 1)/2)}
            (\frac{1}{2})^{(n - 1)/2} y^{\frac{(n - 1) - 2}{2}} e^{-\frac{y}{2}}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    T_{1}
    & = &
        \sum_{j=1}^{n}
            X_{j}
        -
        n\mu
    \nonumber
    \\
    & = &
        n
        \frac{1}{n}
        \sum_{j=1}^{n}
            X_{j}
        -
        n \mu
    \nonumber
    \\
    & = &
        n
        \bar{X}
        -
        n \mu
    \nonumber
    \\
    T_{2}
    & = &
        \sum_{j=1}^{n}
            X_{j}^{2}
        -
        2\mu
        \sum_{j=1}^{n}
            X_{j}
        +
        n
        \mu^{2}
    \nonumber
    \\
    & = &
        \sum_{j=1}^{n}
            X_{j}^{2}
        -
        2\mu
        n
        \frac{1}{n}
        \sum_{j=1}^{n}
            X_{j}
        +
        n
        \mu^{2}
    \nonumber
    \\
    & = &
        \sum_{j=1}^{n}
            X_{j}^{2}
        +
        2\bar{X}
        \sum_{j=1}^{n}
            X_{j}
        -
        2\bar{X}
        \sum_{j=1}^{n}
            X_{j}
        +
        n
        \bar{X}^{2}
        -
        n
        \bar{X}^{2}
        -
        2\mu
        n
        \bar{X}
        +
        n
        \mu^{2}
    \nonumber
    \\
    & = &
        \sum_{j=1}^{n}
            (X_{j} - \bar{X})^{2}
        +
        2\bar{X}
        \sum_{j=1}^{n}
            X_{j}
        -
        n
        \bar{X}^{2}
        -
        2\mu
        n
        \bar{X}
        +
        n
        \mu^{2}
    \nonumber
    \\
    & = &
        n
        S
        +
        2\bar{X}^{2}
        n
        -
        n
        \bar{X}^{2}
        -
        2\mu
        n
        \bar{X}
        +
        n
        \mu^{2}
    \nonumber
    \\
    & = &
        n
        S
        +
        \bar{X}^{2}
        n
        -
        2\mu
        n
        \bar{X}
        +
        n
        \mu^{2}
\end{eqnarray}
$$

Let $g: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$ be

$$
\begin{eqnarray}
    (g^{-1}(\bar{x}, y))_{1}
    & := &
        n \bar{x} - n \mu
    \nonumber
    \\
    (g^{-1}(\bar{x}, y))_{2}
    & := &
        \sigma^{2}(n - 1) y
        +
        n \bar{x}^{2}
        -
        2 n \mu \bar{x}
        +
        n \mu^{2}
    \nonumber
    \\
    (g(t_{1}, t_{2}))_{1}
    & = &
        \frac{t_{1}}{n}
        +
        \mu
    \nonumber
    \\
    (g(t_{1}, t_{2}))_{2}
    & = &
        \frac{
            t_{2}
            -
            n \mu^{2}
            +
            2 n\mu
                (\frac{t_{1}}{n} + \mu)
            -
            n
            \left(
                \frac{t_{1}}{n}
                +
                \mu
            \right)^{2}
        }{
            \sigma^{2} (n - 1)
        }
    \nonumber
    \\
    & = &
        \frac{
            t_{2}
            -
            n \mu^{2}
            +
            2 \mu t_{1}
            +
            2 n\mu^{2}
            -
            \left(
                \frac{t_{1}^{2}}{n}
                +
                2 \mu t_{1}
                +
                n \mu^{2}
            \right)
        }{
            \sigma^{2} (n - 1)
        }
    \nonumber
    \\
    & = &
        \frac{
            t_{2}
            -
            2
            n \mu^{2}
            +
            2 \mu t_{1}
            +
            2n \mu^{2}
            -
            \frac{t_{1}^{2}}{n}
            -
            2 \mu t_{1}
        }{
            \sigma^{2} (n - 1)
        }
    \nonumber
    \\
    & = &
        \frac{
            t_{2}
            -
            \frac{t_{1}^{2}}{n}
        }{
            \sigma^{2} (n - 1)
        }
    \nonumber
    \\
    & = &
        \frac{
            n t_{2}
            -
            t_{1}^{2}
        }{
            n \sigma^{2} (n - 1)
        }
\end{eqnarray}
$$

Then we have

$$
\begin{eqnarray}
    g^{-1}(\bar{X}, Y)
    & = &
        (T_{1}, T_{2})
    \nonumber
    \\
    g(T_{1}, T_{2})
    & = &
        (\bar{X}, Y)
    .
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    p_{T_{1}, T_{2}}(t_{1}, t_{2})
    =
    p_{\bar{X}, Y}(g(t_{1}, t_{2}))
    |J_{g}(t_{1}, t_{2})|
    \nonumber
\end{eqnarray}
$$

where $$J_{g}(t_{1}, t_{2})$$ is Jacobian matrix of $g$ at $$(t_{1}, t_{2})$$.

$$
\begin{eqnarray}
    \frac{\partial g_{1}}{\partial t_{1}}
    & = &
        \frac{1}{n}
    \nonumber
    \\
    \frac{\partial g_{1}}{\partial t_{2}}
    & = &
        0
    \nonumber
    \\
    \frac{\partial g_{2}}{\partial t_{1}}
    & = &
        \frac{-2 t_{1}}{\sigma^{2} (n - 1) n}
    \nonumber
    \\
    \frac{\partial g_{2}}{\partial t_{2}}
    & = &
        \frac{1}{\sigma^{2} (n - 1)}
    \nonumber
    \\
    J_{g}(t_{1}, t_{2})
    & = &
        \left(
            \begin{array}{cc}
                \frac{1}{n}
                &
                    0
                \\
                \frac{-2 t_{1}}{\sigma^{2} (n - 1) n}
                &
                    \frac{1}{\sigma^{2} (n - 1)}
            \end{array}
        \right)
    \nonumber
    \\
    |J_{g}(t_{1}, t_{2})|
    & = &
        \frac{
            1
        }{
            \sigma^{2}(n - 1)n
        }
    \nonumber
\end{eqnarray}
$$

Therefore we can explicitly write the joint p.d.f. as follows:

$$
\begin{eqnarray}
    p_{T_{1}, T_{2}}(t_{1}, t_{2})
    & = &
        p_{\bar{X}}(
            \frac{t_{1}}{n} + \mu
        )
        p_{Y}
        \left(
            \frac{
                n t_{2}
                -
                t_{1}^{2}
            }{
                n \sigma^{2} (n - 1)
            }
        \right)
        \frac{
            1
        }{
            \sigma^{2}(n - 1)n
        }
    \nonumber
    \\
    & = &
        \frac{1}{(2\pi\sigma^{2})^{1/2}}
        \exp
        \left(
            -
            \frac{1}{2\sigma^{2}}
            (\frac{t_{1}}{n})^{2}
        \right)
        \frac{1}{\Gamma((n - 1)/2)}
            (\frac{1}{2})^{(n - 1)/2}
            \left(
                \frac{
                    n t_{2}
                    -
                    t_{1}^{2}
                }{
                    n \sigma^{2} (n - 1)
                }
            \right)^{\frac{n - 3}{2}}
            \exp
            \left(
                -\frac{
                    \frac{
                        n t_{2}
                        -
                        t_{1}^{2}
                    }{
                        n \sigma^{2} (n - 1)
                    }
                }{
                    2
                }
            \right)
        \frac{
            1
        }{
            \sigma^{2}(n - 1)n
        }
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            (2\pi\sigma^{2}n^{2})^{1/2}
            \sigma^{2}(n - 1)
        }
        \exp
        \left(
            -
            \frac{1}{2\sigma^{2}n^{2}}
            t_{1}^{2}
            -
            \frac{
                n t_{2}
                -
                t_{1}^{2}
            }{
                2
                n \sigma^{2} (n - 1)
            }
        \right)
        \frac{1}{\Gamma((n - 1)/2)}
            (\frac{1}{2})^{(n - 1)/2}
            \left(
                \frac{
                    n t_{2}
                    -
                    t_{1}^{2}
                }{
                    n \sigma^{2} (n - 1)
                }
            \right)^{\frac{n - 3}{2}}
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            (2\pi\sigma^{2}n^{2})^{1/2}
            \sigma^{2}(n - 1)
            2^{(n - 1)/2}
            \Gamma(\frac{n - 1}{2})
            (n \sigma^{2} (n - 1))^{\frac{n - 3}{2}}
        }
        \exp
        \left(
            \frac{
                -(n - 1)
                    t_{1}^{2}
                +
                t_{1}^{2}n
            }{
                2\sigma^{2}n^{2}
                (n - 1)
            }
            -
            \frac{
                t_{2}
            }{
                2
                \sigma^{2} (n - 1)
            }
        \right)
        \left(
            n t_{2}
            -
            t_{1}^{2}
        \right)^{\frac{n - 3}{2}}
    \nonumber
    \\
    & = &
        K
        \exp
        \left(
            \frac{
                t_{1}^{2}
            }{
                2\sigma^{2}n^{2}
                (n - 1)
            }
            -
            \frac{
                t_{2}
            }{
                2
                \sigma^{2} (n - 1)
            }
        \right)
        \left(
            n t_{2}
            -
            t_{1}^{2}
        \right)^{\frac{n - 3}{2}}
    \nonumber
    \\
    & = &
        K
        \exp
        \left(
            \frac{
                -
                \left(
                    t_{1}n\mu(n - 1)
                    -
                    t_{1}
                \right)^{2}
                -
                t_{1}^{2}
                    n^{2}
                    \mu^{2}
                    (n - 1)^{2}
                (
                    +
                    (n - 1)
                    2t_{1}n\mu
                    +
                    (n - 1)
                    n^{2}\mu^{2}
                )
            }{
                2\sigma^{2}n^{2}
                (n - 1)
            }
            -
            \frac{
                t_{2}
            }{
                2
                \sigma^{2} (n - 1)
            }
        \right)
        \left(
            n t_{2}
            -
            t_{1}^{2}
        \right)^{\frac{n - 3}{2}}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


