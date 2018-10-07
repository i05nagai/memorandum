---
title: Lanczos Approximation
---

## Lanczos Approximation
A method of approximating gamma function.

$$
\begin{eqnarray}
    \Gamma(z + 1)
    & = &
        (z + r + \frac{1}{2})^{z + \frac{1}{2}}
        \exp
        \left(
            -
            \left(
                z + r + \frac{1}{2}
            \right)
        \right)
        \sqrt{2}
        \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}
            \cos^{2z}\theta
            \left(
                \frac{
                    a_{0}(r)
                }{
                    2
                }
                +
                \sum_{k=0}^{\infty}
                    a_{k}(r)
                    \cos(2k\theta)
            \right)
        \ d\theta
    .
\end{eqnarray}

$$


#### Lemma 1

$$
    z \in \mathbb{C},
    \
    \mathrm{Re}(z) > -1,
    \
    \Gamma(z + 1)
    =
    \alpha^{z + 1}
    \int_{0}^{\infty}
        t^{z}e^{-\alpha t}
    \ dt
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Lanczos approximation \- Wikipedia](https://en.wikipedia.org/wiki/Lanczos_approximation)
* Pugh, G. R. (1999). An Analysis of the Lanczos Gamma a Thesis Submitted in Partial Fulfillment of, (November 2004).
