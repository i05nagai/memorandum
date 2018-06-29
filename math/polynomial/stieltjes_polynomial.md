---
title: Stieltjes Polynomial
---

## Stieltjes Polynomial

## Definition

Let $P_{n}$ be Legendre polynomial defined by

$$
\begin{eqnarray}
    \int_{-1}^{-1}
        P_{n}(x)x^{k}
    \ dx
    & = &
        0
        \quad
        k = 0, 1, \ldots, n - 1,
    \nonumber
    \\
    P_{n}(1)
    & = &
        1
    \nonumber
    .
\end{eqnarray}
$$

For $n \ge 0$, Stieltjes polynomial $E_{n+1}$ is defined by

$$
\begin{eqnarray}
    \int_{-1}^{1}
        P_{n}(x)
        E_{n+1}(x)
        x^{k}
    \ dx
    & = &
        0
        \label{stieltjes_polynomial_constraint_01}
    \\
    E_{n+1}(x)
    & = &
        \frac{
            2^{n}
        }{
            \gamma_{n}
        }
        x^{n+1}
        +
        p(x)
        \label{stieltjes_polynomial_constraint_02}
    \\
    \gamma_{n}
    & = &
        \frac{
            2^{2n}
            (n!)^{2}
        }{
            (2n + 1)!
        }
    \nonumber
    \\
    \Pi_{n}
    & := &
        \left\{
            \sum_{i=0}^{n}
                a_{i}x^{i}
            \mid
            a_{i} \in \mathbb{R}
        \right\}
    \nonumber
    \\
    p
    & \in &
        \Pi_{n}
    \nonumber
\end{eqnarray}
$$

Stieltjes polynomial is othogonal to $P_{n}$ by weigthing $x^{k}$.
Up to a multiplicative constant, the polynomial $E_{n+1}$ is defined uniquely by $$\eqref{stieltjes_polynomial_constraint_01}$$.


<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Stieltjes polynomials \- Encyclopedia of Mathematics](https://www.encyclopediaofmath.org/index.php/Stieltjes_polynomials)
* Ehrich, S. (1995). Asymptoticproperties of stieltjes polynomials and gauss-kronrod quadrature formulas. Journal of Approximation Theory, 82(2), 287–303. https://doi.org/10.1006/jath.1995.1079
