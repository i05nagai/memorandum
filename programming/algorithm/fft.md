---
title: FFT
---

## FFT


## Discrete Fourier Transform
- $f(x)$
    - function

$$
    \mathcal{F}(f)(t)
    :=
    \sum_{j=0}^{n-1}
        f(e^{\frac{2 \pi ij }{n}})
        t^{j}
    .
$$

## Inverse Fourier Transform
- $\hat{f}(x)$
    - function

$$
    \mathcal{\hat{F}}(\hat{f})(x)
    :=
    \frac{1}{n}
    \sum_{j=0}^{n-1}
        \hat{f}(e^{\frac{-2 \pi ij }{n}})
        x^{j}
    .
$$


#### Lemma 1
- $k \in \mathbb{Z}$,

$$
    \sum_{j=0}^{n-1}
        e^{\frac{2\pi i j k}{n}}
    =
    \begin{cases}
        n
        &
            (k = 0 (\mathrm{mod}\ n))
        \\
        0
        &
            (\text{otherwise})
    \end{cases}
    .
$$

#### proof
Let us assume that $k = n k^{\prime}$ for some $k^{\prime} \in \mathbb{Z}$.

$$
    e^{\frac{2\pi i j k}{n}}
    =
    e^{2\pi i j k^{\prime}}
    =
    1
    \quad
    \forall j
    .
$$

Hence the sum is $n$.

$$\{e^{\frac{2\pi i j k}{n}}\}_{j=0}^{n-1}$$ is the $n$-th root of the unity.

$$
    z^{n} - 1
    =
    (z - 1)
    (z - e^{\frac{2 \pi i k}{n}})
    \cdots
    (z - e^{\frac{2 \pi i k(n - 1)}{n}})
    .
$$

This implies that the term of $z^{n-1}$ in the RHS is 0.
That is,

$$
\begin{eqnarray}
    \sum_{j=0}^{n-1}
        e^{\frac{2 \pi i k j}{n}}
    & = &
        0
    .
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Example 1
- $$f(x) = \sum_{j=0}^{n-1}a_{j}x^{j}$$,

$$
\begin{eqnarray}
    \mathcal{F}(f)(t)
    & = &
        \sum_{j=0}^{n-1}
            \left(
                \sum_{k=0}^{n-1}
                    a_{k}
                    (e^{\frac{2 \pi ij}{n}})^{k}
            \right)
            t^{j}
    \nonumber
    \\
    & = &
        \sum_{k=0}^{n-1}
            a_{k}
            \sum_{j=0}^{n-1}
                e^{\frac{2 \pi i(jk)}{n}}
                t^{j}
    \nonumber
\end{eqnarray}
$$

When $t = e^{\frac{-2 \pi l}{n}}$,

$$
\begin{eqnarray}
    \hat{f}(e^{\frac{-2 \pi l i}{n}})
    :=
    \mathcal{F}(f)(e^{\frac{-2 \pi l i}{n}})
    & = &
        \sum_{k=0}^{n-1}
            a_{k}
            \sum_{j=0}^{n-1}
                e^{\frac{2 \pi i (jk)}{n}}
                e^{\frac{2 \pi i (-jl)}{n}}
    \nonumber
    \\
    & = &
        \sum_{k=0}^{n-1}
            a_{k}
            \sum_{j=0}^{n-1}
                e^{\frac{2 \pi i j (k - l)}{n}}
    \nonumber
    \\
    & = &
        a_{k^{\prime}}
        n
    \nonumber
\end{eqnarray}
$$

where $k^{\prime} = l (\mathrm{mod}\ n)$.

The inverse transformation is

$$
\begin{eqnarray}
    \mathcal{\hat{F}}(\hat{f})(x)
    & = &
        \frac{1}{n}
        \sum_{l=0}^{n-1}
            \hat{f}(e^{\frac{-2 \pi i l}{n}})
            x^{l}
    \nonumber
    \\
    & = &
        \frac{1}{n}
        n
        \sum_{l=0}^{n-1}
            a_{l}
            x^{l}
    \nonumber
    \\
    & = &
        \sum_{l=0}^{n-1}
            a_{l}
            x^{l}
    \nonumber
\end{eqnarray}
$$


## Reference
- https://www.kylem.net/math/roots_unity.html
- https://cp-algorithms.com/algebra/fft.html
