---
title: Double Exponential
---

## Double Exponential


## Quadrature Formula

#### (-1, 1)

$$
\begin{eqnarray}
    \frac{\pi}{2} h
    \sum_{i=-n}^{n}
        \frac{
            f(\tanh(\pi \sinh(h * i) / 2))
            \cosh(i h)
        }{
            \cosh^{2}(\pi h / 2 \sinh(h * i))
        }
\end{eqnarray}
$$

#### (0, \infty)

$$
\begin{eqnarray}
    \frac{\pi}{2} h
    \sum_{i=-n}^{n}
        f(\exp(\pi \sinh(h * i) / 2))
        \cosh(i h)
        \exp(\pi \sinh(h * i) / 2)
\end{eqnarray}
$$

#### (-\infty, \infty)

$$
\begin{eqnarray}
    \frac{\pi}{2} h
    \sum_{i=-n}^{n}
        f(\sinh(\pi \sinh(h * i) / 2))
        \cosh(i h)
        \cosh(\pi \sinh(h * i) / 2)
\end{eqnarray}
$$

#### Converting finite interval to (-1, 1)

$$
\begin{eqnarray}
    \int_{a}^{b}
        f(x)
    \ dx
    & = &
        \int_{-1}^{1}
            f
            \left(
                \frac{
                    b - a
                }{
                    2
                }
                \left(
                    t
                    +
                    \frac{
                        b + a
                    }{
                        b - a
                    }
                \right)
            \right)
        \ dt
\end{eqnarray}
$$

## Reference
- Takahasi, H., & Mori, M. (1974). Double exponential formulas for numerical integration. Publications of the Research Institute for Mathematical Sciences, 9(3), 721–741. https://doi.org/10.2977/prims/1195192451
