---
title: Closed Newton-Cotes
---

## Closed Newton-Cotes
* integrate approximated function which is made by interpolating representative points of the integrand
* useful if the value of the integrand at equally spaced points is given

## Theory
For simplicity, we only consider one-dimentional integrand.

* $a, b \in \mathbb{R}$,
    * $a < b$

We define $N$ paritition of interval $[a, b]$, denoted $\pi(N; a, b)$,

$$
\begin{eqnarray}
    \pi(N; a, b)
    & := &
        \{
            x_{0}, \ldots, x_{N + 1}
        \}
    \nonumber
    \\
    x_{0}
    & := &
        a
    \nonumber
    \\
    x_{k}
    & := &
        \frac{
            x_{k} - x_{k - 1}
        }{
            N
        }
        \quad
        (k = 1, \ldots, N)
    \nonumber
    \\
    x_{N+1}
    & := &
        b
    .
    \nonumber
\end{eqnarray}
$$

The interpolation polynomial in the Lagrange form is given by

$$
\begin{eqnarray}
    l_{j}(x; \pi(N; a, b))
    & := &
        \prod_{m \in \{0, \ldots, N + 1\}, m \neq j}
            \frac{
                x - x_{m}
            }{
                x_{j} - x_{m}
            }
    \nonumber
    \\
    L(x; \pi(N, a, b))
    & := &
        \sum_{j=0}^{N+1}
            f(x_{j})
            l_{j}(x)
    \nonumber
\end{eqnarray}
$$

$L(x)$ interpolates points $$(x_{i}, f(x_{i}))$$ by Lagrange Polynomial.


$$
\begin{eqnarray}
    \int_{x_{1}}^{x_{2}}
        L(x; \pi(1; x_{1}, x_{2}))
    \ dx
    & = &
        \int_{x_{1}}^{x_{2}}
            L(x)
        \ dx
\end{eqnarray}
$$


## Reference
* [Newton–Cotes formulas \- Wikipedia](https://en.wikipedia.org/wiki/Newton%E2%80%93Cotes_formulas)
* [Lagrange polynomial \- Wikipedia](https://en.wikipedia.org/wiki/Lagrange_polynomial)
