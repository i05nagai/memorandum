---
title: Box Muller's method
---

## Box Muller's method

* $$(\Omega, \mathcal{F}, P)$$,
    * probability space
* $$U_{i}: \Omega \rightarrow (0, 1),\ (i = 1, 2)$$,
    * uniformly distributed random variable
    * $$U_{1}, U_{2}$$ are independent

## Theorem1.

$$
\begin{eqnarray}
    X_{1}
    & := &
        \sqrt{-2 \ln(U_{1})}\cos (2 \pi U_{2})
    \nonumber
    \\
    X_{2}
    & := &
        \sqrt{-2 \ln(U_{1})}\sin (2 \pi U_{2})
    \nonumber
\end{eqnarray}
$$

Then $$X_{1}$$, $$X_{2}$$ are independent one-dimentional normal distribution.

## proof.
We show that the characteristic function of $X_{1}$ is equal to a normal distribution.

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        e^{i\xi X_{1}}
    \right]
    & = &
        \int_{(0, 1)}
            \int_{(0, 1)}
                \exp
                \left(
                    i \xi \sqrt{-2 \ln(u_{1})} \cos (2 \pi u_{2})
                \right)
            \ d u_{1}
        \ d u_{2}
    \nonumber
\end{eqnarray}
$$

We substitute

$$
\begin{eqnarray}
    &  &
        u_{1}
        =
        \exp(- r^{2}/2)
    \nonumber
    \\
    & \Leftrightarrow &
        \sqrt{-2 \ln(u_{1})}
        =
        r
        ,
    \nonumber
    \\
    & &
        u_{2}
        =
        \theta/(2\pi)
    \nonumber
    \\
    & \Leftrightarrow &
        2\pi u_{2}
        =
        \theta
        ,
    \nonumber
\end{eqnarray}
$$

into the above equation.
Then corresponding jacobian matrix and jacobian are given by

$$
\begin{eqnarray}
    J
    & := &
        \left(
            \begin{array}{cc}
                \frac{\partial u_{1}}{\partial r}
                &
                    \frac{\partial u_{1}}{\partial \theta}
                \\
                \frac{\partial u_{2}}{\partial r}
                &
                    \frac{\partial u_{2}}{\partial \theta}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                -r \exp(- r^{2} / 2)
                &
                    0
                \\
                0
                &
                    1 / (2\pi)
            \end{array}
        \right)
    \nonumber
    \\
    | \mathrm{det}J|
    & = &
        \frac{r}{2\pi}
        \exp(-r^{2}/2)
    \nonumber
\end{eqnarray}
$$

Substituting $$r$$ and $$\theta$$,

$$
\begin{eqnarray}
    \int_{(0, 1)}
        \int_{(0, 1)}
            \exp
            \left(
                i \xi \sqrt{-2 \ln(u_{1})} \cos (2 \pi u_{2})
            \right)
        \ d u_{1}
    \ d u_{2}
    & = &
        \int_{(0, 2\pi)}
            \int_{(0, \infty)}
                \exp
                \left(
                    i \xi r \cos (\theta)
                \right)
                |\mathrm{det}J|
            \ d r
        \ d \theta
    \nonumber
    \\
    & = &
        \int_{(0, 2\pi)}
            \int_{(0, \infty)}
                \exp
                \left(
                    i \xi r \cos (\theta)
                \right)
                \frac{r}{2\pi}
                \exp
                \left(
                    \frac{-r^{2}}{2}
                \right)
            \ d r
        \ d \theta
    \nonumber
    \\
    & = &
        \int_{(0, 2\pi)}
            \int_{(0, \infty)}
                \frac{r}{2\pi}
                \exp
                \left(
                    i \xi r \cos (\theta)
                    -
                    \frac{r^{2}}{2}
                \right)
            \ d r
        \ d \theta
\end{eqnarray}
$$

Additionaly we substitute

$$
\begin{eqnarray}
    &  &
        y_{1}
        =
        r \cos \theta
    \nonumber
    \\
    & &
        y_{2}
        =
        r \sin \theta
    \nonumber
\end{eqnarray}
$$

Then corresponding jacobian matrix and jacobian are given by

$$
\begin{eqnarray}
    J
    & := &
        \left(
            \begin{array}{cc}
                \frac{\partial y_{1}}{\partial r}
                &
                    \frac{\partial y_{1}}{\partial \theta}
                \\
                \frac{\partial y_{2}}{\partial r}
                &
                    \frac{\partial y_{2}}{\partial \theta}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                \cos \theta
                &
                    -r \sin \theta
                \\
                \sin \theta
                &
                    r \cos \theta
            \end{array}
        \right)
    \nonumber
    \\
    | \mathrm{det}J |
    & = &
        r\cos^{2} \theta
        +
        r\sin^{2} \theta
    \nonumber
    \\
    & = &
        r
    \nonumber
    \\
    dy_{1} dy_{2}
    & = &
        |J| dr d\theta
    \nonumber
\end{eqnarray}
$$

Substituting $$y_{1}$$ and $$y_{2}$$,

$$
\begin{eqnarray}
    \int_{(0, 2\pi)}
        \int_{(0, \infty)}
            \frac{r}{2\pi}
            \exp
            \left(
                i \xi r \cos (\theta)
                -
                \frac{r^{2}}{2}
            \right)
        \ d r
    \ d \theta
    & = &
        \int_{(-\infty, \infty)}
            \int_{(-\infty, \infty)}
                \frac{1}{2\pi}
                \exp
                \left(
                    i \xi y_{1}
                    -
                    \frac{y_{1}^{2} + y_{2}^{2}}{2}
                \right)
            \ d y_{1}
        \ d y_{2}
    \nonumber
    \\
    & = &
        \frac{1}{2\pi}
        \int_{(-\infty, \infty)}
            \int_{(-\infty, \infty)}
                \exp
                \left(
                    i \xi y_{1}
                    -
                    \frac{y_{1}^{2}}{2}
                    -
                    \frac{y_{2}^{2}}{2}
                    -
                    \frac{(y_{1} - i\xi)^{2}}{2}
                    +
                    \frac{(y_{1} - i\xi)^{2}}{2}
                \right)
            \ d y_{1}
        \ d y_{2}
    \nonumber
    \\
    & = &
        \frac{1}{2\pi}
        \int_{(-\infty, \infty)}
            \int_{(-\infty, \infty)}
                \exp
                \left(
                    -
                    \frac{y_{2}^{2}}{2}
                    -
                    \frac{(y_{1} - i\xi)^{2}}{2}
                    -
                    \frac{\xi^{2}}{2}
                \right)
            \ d y_{1}
        \ d y_{2}
    \nonumber
    \\
    & = &
        \frac{1}{2\pi}
        \exp
        \left(
            -
            \frac{\xi^{2}}{2}
        \right)
        \int_{(-\infty, \infty)}
            \int_{(-\infty, \infty)}
                \exp
                \left(
                    -
                    \frac{y_{2}^{2}}{2}
                    -
                    \frac{(y_{1} - i\xi)^{2}}{2}
                \right)
            \ d y_{1}
        \ d y_{2}
    \nonumber
    \\
    & = &
        \exp
        \left(
            -
            \frac{\xi^{2}}{2}
        \right)
        \frac{1}{\sqrt{2\pi}}
        \int_{(-\infty, \infty)}
            \exp
            \left(
                -
                \frac{y_{2}^{2}}{2}
            \right)
        \ d y_{2}
        \frac{1}{\sqrt{2\pi}}
        \int_{(-\infty, \infty)}
            \exp
            \left(
                -
                \frac{(y_{1} - i\xi)^{2}}{2}
            \right)
        \ d y_{1}
    \nonumber
    \\
    & = &
        \exp
        \left(
            -
            \frac{\xi^{2}}{2}
        \right)
        \frac{1}{\sqrt{2\pi}}
        \int_{(-\infty, \infty)}
            \exp
            \left(
                -
                \frac{(y_{1} - i\xi)^{2}}{2}
            \right)
        \ d y_{1}
    \nonumber
    \\
    & = &
        \exp
        \left(
            -
            \frac{\xi^{2}}{2}
        \right)
\end{eqnarray}
$$

This is characteristic function of normal distribution.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [ボックス＝ミュラー法 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%9C%E3%83%83%E3%82%AF%E3%82%B9%EF%BC%9D%E3%83%9F%E3%83%A5%E3%83%A9%E3%83%BC%E6%B3%95)

