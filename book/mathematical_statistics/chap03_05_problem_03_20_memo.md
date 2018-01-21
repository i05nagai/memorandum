---
title: Chapter3-05. Conditional expectation memo for calculation
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
    \phi_{(T_{1}, T_{2})}(u)
    & = &
        \mathrm{E}
        \left[
            \exp
            \left(
                i
                u_{1}
                \sum_{j=1}^{n}
                    (x_{j} - \mu)
                +
                i
                u_{2}
                \sum_{j=1}^{n}
                    (x_{j} - \mu)^{2}
            \right)
        \right]
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}^{n}}
            \exp
            \left(
                i
                u_{1}
                \sum_{j=1}^{n}
                    (x_{j} - \mu)
                +
                i
                u_{2}
                \sum_{j=1}^{n}
                    (x_{j} - \mu)^{2}
            \right)
            \frac{
                1
            }{
                (2 \pi \sigma^{2})^{n/2}
            }
            \exp
            \left(
                \frac{
                    -1
                }{
                    2 \sigma^{2}
                }
                \sum_{j=1}^{n}
                    \left(
                        x_{j}
                        -
                        \mu
                    \right)^{2}
            \right)
        \ dx
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}^{n}}
            \frac{
                1
            }{
                (2 \pi \sigma^{2})^{n/2}
            }
            \exp
            \left(
                i
                u_{1}
                \sum_{j=1}^{n}
                    (x_{j} - \mu)
                +
                i
                u_{2}
                \sum_{j=1}^{n}
                    (x_{j} - \mu)^{2}
                -
                \frac{
                    1
                }{
                    2 \sigma^{2}
                }
                \sum_{j=1}^{n}
                    \left(
                        x_{j}
                        -
                        \mu
                    \right)^{2}
            \right)
        \ dx
    \nonumber
    \\
    & = &
        \prod_{j=1}^{n}
            \frac{
                1
            }{
                (2 \pi \sigma^{2})^{1/2}
            }
            \int_{\mathbb{R}}
                \exp
                \left(
                    i
                        u_{1}
                        (x_{j} - \mu)
                    +
                    i
                        u_{2}
                        (x_{j} - \mu)^{2}
                    -
                    \frac{
                        1
                    }{
                        2 \sigma^{2}
                    }
                        \left(
                            x_{j}
                            -
                            \mu
                        \right)^{2}
                \right)
            \ dx_{j}
    \nonumber
\end{eqnarray}
$$

$(x_{j} - \mu) = y_{j}$, $dy_{j}/x_{j} = 1$,

$$
\begin{eqnarray}
    \prod_{j=1}^{n}
        \frac{
            1
        }{
            (2 \pi \sigma^{2})^{1/2}
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                i
                    u_{1}
                    y_{j}
                +
                i
                    u_{2}
                    y_{j}^{2}
                -
                \frac{
                    1
                }{
                    2 \sigma^{2}
                }
                    y_{j}^{2}
            \right)
        \ dy_{j}
    & = &
        \prod_{j=1}^{n}
            \frac{
                1
            }{
                (2 \pi \sigma^{2})^{1/2}
            }
            \int_{\mathbb{R}}
                \exp
                \left(
                    i
                        u_{1}
                        y_{j}
                    +
                    \left(
                        \frac{
                            i
                            2 \sigma^{2}
                            u_{2}
                            -
                            1
                        }{
                            2 \sigma^{2}
                        }
                    \right)
                        y_{j}^{2}
                \right)
            \ dy_{j}
    \nonumber
    \\
    & = &
        \prod_{j=1}^{n}
            \frac{
                1
            }{
                (2 \pi \sigma^{2})^{1/2}
            }
            \int_{\mathbb{R}}
                \exp
                \left(
                    i
                        u_{1}
                        y_{j}
                    -
                    \frac{1}{2}
                    \left(
                        \frac{
                            1
                            -
                            i
                            2 \sigma^{2}
                            u_{2}
                        }{
                            \sigma^{2}
                        }
                    \right)
                        y_{j}^{2}
                \right)
            \ dy_{j}
\end{eqnarray}
$$

$$
    \frac{(1 - 2 i \sigma^{2} u_{2})^{1/2}}{\sigma}y_{j}
    =
    z_{j}
$$,
$$
    d z_{j} / dy_{j}
    =
    \frac{(1 - 2 \sigma^{2} u_{2})^{1/2}}{\sigma}
$$,

$$
\begin{eqnarray}
    & &
        \prod_{j=1}^{n}
            \frac{
                1
            }{
                (2 \pi \sigma^{2})^{1/2}
            }
            \int_{\mathbb{R}}
                \exp
                \left(
                    i
                        u_{1}
                        \frac{
                            \sigma
                        }{
                            (1 - 2i \sigma^{2}u_{2})^{1/2}
                        }
                        z_{j}
                    -
                    \frac{1}{2}
                    z_{j}^{2}
                \right)
                \frac{
                    \sigma
                }{
                    (1 - 2i \sigma^{2}u_{2})^{1/2}
                }
            \ dz_{j}
    \nonumber
    \\
    & = &
        \prod_{j=1}^{n}
            \frac{
                1
            }{
                (2 \pi)^{1/2}
                (1 - 2i \sigma^{2}u_{2})^{1/2}
            }
            \int_{\mathbb{R}}
                \exp
                \left(
                    -
                    \frac{1}{2}
                    \left(
                        z_{j}^{2}
                        -
                        i
                        u_{1}
                        \frac{
                            \sigma
                        }{
                            (1 - 2i \sigma^{2}u_{2})^{1/2}
                        }
                    \right)^{2}
                    -
                    \frac{
                        u_{1}^{2}
                        \sigma^{2}
                    }{
                        2
                        (1 - 2i \sigma^{2}u_{2})
                    }
                \right)
            \ dz_{j}
    \nonumber
    \\
    & = &
        \prod_{j=1}^{n}
            \frac{
                1
            }{
                (1 - 2i \sigma^{2}u_{2})^{1/2}
            }
            \exp
            \left(
                -
                \frac{
                    u_{1}^{2}
                    \sigma^{2}
                }{
                    2
                    (1 - 2i \sigma^{2}u_{2})
                }
            \right)
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            (1 - 2i \sigma^{2}u_{2})^{n/2}
        }
        \exp
        \left(
            -
            \frac{
                n
                u_{1}^{2}
                \sigma^{2}
            }{
                2
                (1 - 2i \sigma^{2}u_{2})
            }
        \right)
\end{eqnarray}
$$

$$
\begin{eqnarray}
    f(t_{1}, t_{2})
    & = &
        \frac{1}{(2\pi)^{2}}
        \int_{\mathbb{R}}
        \int_{\mathbb{R}}
            \exp
            \left(
                -i t_{1} u_{1}
                -i t_{2} u_{2}
            \right)
            \frac{
                1
            }{
                (1 - 2i \sigma^{2}u_{2})^{n/2}
            }
            \exp
            \left(
                -
                \frac{
                    n
                    u_{1}^{2}
                    \sigma^{2}
                }{
                    2
                    (1 - 2i \sigma^{2}u_{2})
                }
            \right)
        \ du_{1}
        \ du_{2}
    \nonumber
    \\
    & = &
        \frac{1}{(2\pi)^{2}}
        \frac{
            1
        }{
            (1 - 2i \sigma^{2}u_{2})^{n/2}
        }
        \int_{\mathbb{R}}
        \int_{\mathbb{R}}
            \exp
            \left(
                -i t_{1} u_{1}
                -i t_{2} u_{2}
                -
                \frac{ 1 }{ 2 }
                \frac{
                    n
                    u_{1}^{2}
                    \sigma^{2}
                }{
                    (1 - 2i \sigma^{2}u_{2})
                }
            \right)
        \ du_{1}
        \ du_{2}
\end{eqnarray}
$$

$$
    v_{1} = \frac{\sqrt{n}\sigma}{(1 - 2i\sigma^{2}u_{2})^{1/2}}u_{1}
$$,
$$
    dv_{1}/du_{1}
    =
    \frac{
        \sqrt{n}\sigma
    }{
        (1 - 2i\sigma^{2}u_{2})^{1/2}
    }
$$,

$$
\begin{eqnarray}
    & &
        \frac{1}{(2\pi)^{2}}
        \frac{
            1
        }{
            (1 - 2i \sigma^{2}u_{2})^{n/2}
        }
        \int_{\mathbb{R}}
        \int_{\mathbb{R}}
            \exp
            \left(
                -i t_{1}
                \frac{
                    (1 - 2i\sigma^{2}u_{2})^{1/2}
                }{
                    \sqrt{n}\sigma
                }
                v_{1}
                -i t_{2} u_{2}
                -
                \frac{ 1 }{ 2 }
                v_{1}^{2}
            \right)
            \frac{
                (1 - 2i\sigma^{2}u_{2})^{1/2}
            }{
                \sqrt{n}\sigma
            }
        \ dv_{1}
        \ du_{2}
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            (2\pi)^{2}
            (1 - 2i \sigma^{2}u_{2})^{(n-1)/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
        \int_{\mathbb{R}}
            \exp
            \left(
                -i t_{1}
                \frac{
                    (1 - 2i\sigma^{2}u_{2})^{1/2}
                }{
                    \sqrt{n}\sigma
                }
                v_{1}
                -i t_{2} u_{2}
                -
                \frac{ 1 }{ 2 }
                v_{1}^{2}
            \right)
        \ dv_{1}
        \ du_{2}
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            (2\pi)^{2}
            (1 - 2i \sigma^{2}u_{2})^{(n-1)/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
        \int_{\mathbb{R}}
            \exp
            \left(
                -i t_{2} u_{2}
                -
                \frac{ 1 }{ 2 }
                \left(
                    v_{1}
                    +
                    i t_{1}
                    \frac{
                        (1 - 2i\sigma^{2}u_{2})^{1/2}
                    }{
                        \sqrt{n}\sigma
                    }
                \right)^{2}
                -
                t_{1}^{2}
                \frac{
                    (1 - 2i\sigma^{2}u_{2})
                }{
                    2
                    n\sigma^{2}
                }
            \right)
        \ dv_{1}
        \ du_{2}
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            (2\pi)^{3/2}
            (1 - 2i \sigma^{2}u_{2})^{(n-1)/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                -i t_{2} u_{2}
                -
                t_{1}^{2}
                \frac{
                    (1 - 2i\sigma^{2}u_{2})
                }{
                    2
                    n\sigma^{2}
                }
            \right)
        \ du_{2}
\end{eqnarray}
$$

$$
    v_{2}
    =
    1 - 2i\sigma^{2}u_{2}
$$,
$$
    \frac{
        (v_{2} - 1)i
    }{
        2\sigma^{2}
    }
    =
    u_{2}
$$,
$$
    dv_{2}/ du_{2}
    =
    -2i\sigma^{2}
$$,

$$
\begin{eqnarray}
    & &
        \frac{
            1
        }{
            (2\pi)^{3/2}
            v_{2}^{(n-1)/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                -i t_{2}
                \frac{
                    (v_{2} - 1)i
                }{
                    2\sigma^{2}
                }
                -
                t_{1}^{2}
                \frac{
                    v_{2}
                }{
                    2
                    n\sigma^{2}
                }
            \right)
            \frac{
                i
            }{
                2\sigma^{2}
            }
        \ dv_{2}
    \nonumber
    \\
    & = &
        \frac{
            v_{2}^{-(n-1)/2}
        }{
            (2\pi)^{3/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                t_{2}
                \frac{
                    (v_{2} - 1)
                }{
                    2\sigma^{2}
                }
                -
                t_{1}^{2}
                \frac{
                    v_{2}
                }{
                    2
                    n\sigma^{2}
                }
            \right)
            \frac{
                i
            }{
                2\sigma^{2}
            }
        \ dv_{2}
    \nonumber
    \\
    & = &
        \frac{
            v_{2}^{-(n-1)/2}
        }{
            (2\pi)^{3/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                \frac{
                    t_{2}
                    v_{2}
                }{
                    2\sigma^{2}
                }
                -
                \frac{
                    t_{2}
                }{
                    2\sigma^{2}
                }
                -
                t_{1}^{2}
                \frac{
                    v_{2}
                }{
                    2
                    n\sigma^{2}
                }
            \right)
            \frac{
                i
            }{
                2\sigma^{2}
            }
        \ dv_{2}
    \nonumber
    \\
    & = &
        \frac{
            v_{2}^{-(n-1)/2}
        }{
            (2\pi)^{3/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                v_{2}
                \frac{
                    t_{2}
                    n
                    -
                    t_{1}^{2}
                }{
                    2
                    n\sigma^{2}
                }
                -
                \frac{
                    t_{2}
                }{
                    2\sigma^{2}
                }
            \right)
            \frac{
                i
            }{
                2\sigma^{2}
            }
        \ dv_{2}
\end{eqnarray}
$$

$$
    w_{2}
    =
    \frac{
        t_{2}
        n
        -
        t_{1}^{2}
    }{
        2
        n\sigma^{2}
    }
    v_{2}
$$,
$$
    dw_{2}/dv_{2}
    =
    \frac{
        t_{2}
        n
        -
        t_{1}^{2}
    }{
        2
        n\sigma^{2}
    }
$$,

$$
\begin{eqnarray}
    & &
        \left(
            \frac{
                2
                n\sigma^{2}
            }{
                t_{2}
                n
                -
                t_{1}^{2}
            }
        \right)^{-(n - 1)/2}
        \frac{
            w_{2}^{-(n-1)/2}
        }{
            (2\pi)^{3/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                w_{2}
                -
                \frac{
                    t_{2}
                }{
                    2\sigma^{2}
                }
            \right)
            \frac{
                i
            }{
                2\sigma^{2}
            }
            \frac{
                2
                n\sigma^{2}
            }{
                t_{2}
                n
                -
                t_{1}^{2}
            }
        \ dw_{2}
    \nonumber
    \\
    & &
        \left(
            \frac{
                2
                n\sigma^{2}
            }{
                t_{2}
                n
                -
                t_{1}^{2}
            }
        \right)^{-(n - 1)/2}
        \frac{
            w_{2}^{-(n-1)/2}
        }{
            (2\pi)^{3/2}
            \sqrt{n}\sigma
        }
        \int_{\mathbb{R}}
            \exp
            \left(
                w_{2}
                -
                \frac{
                    t_{2}
                }{
                    2\sigma^{2}
                }
            \right)
            \frac{
                i
            }{
                2\sigma^{2}
            }
            \frac{
                2
                n\sigma^{2}
            }{
                t_{2}
                n
                -
                t_{1}^{2}
            }
        \ dw_{2}
\end{eqnarray}
$$

