---
title: loss function
---

## loss function


### Cross entropy
* $$(\Omega, \mathcal{F})$$,
    * measurable space
* $X: \Omega \rightarrow \mathbb{R}$
    * r.v.
* $Y: \Omega \rightarrow \mathbb{R}$
    * r.v.
* $$P^{X}: \mathcal{F} \rightarrow [0, 1]$$,
    * absolutely continuous to $\mu$
    * distribution of $X$
* $$P^{Y}: \mathcal{F} \rightarrow [0, 1]$$,
    * absolutely continuous to $\mu$
    * distribution of $Y$

$$
\begin{eqnarray}
    H(P^{X}, P^{Y})
    & := &
        -
        \int_{\Omega}
            \log
            \frac{
                d P^{Y}
            }{
                d P^{X}
            }
            (x)
        \ P(dx)
    \nonumber
    \\
    & = &
        -
        \mathrm{E}_{P^{X}}
        \left[
            -
            \log
            \frac{
                d P^{Y}
            }{
                d P^{X}
            }
        \right]
\end{eqnarray}
$$


### binary crossentropy

$$
\begin{eqnarray}
    p \log(q)
    +
    (1 - p) \log(1 - q)
\end{eqnarray}
$$

### categorical crossentropy
* $$(\Omega, \mathcal{F})$$,
    * $\mathrm{card}(\Omega) < \infty$
* $$P^{X}$$,
* $$P^{Y}$$,

$$
\begin{eqnarray}
    H(P^{X} , P^{Y})
    & := &
        \mathrm{E}_{P^{X}}
        \left[
            -
            \log
            \frac{d P^{X}}{d P^{Y}}
        \right]
    \nonumber
    \\
    & = &
        -
        \sum_{\omega \in \Omega}
            \left(
                P^{X}(\{ \omega \})
                \log P^{Y}(\{ \omega \})
            \right)
\end{eqnarray}

$$

### Softmax
$j$ -th softmax

$$
    (f(x))_{j}
    :=
    \frac{
        \exp
        \left(
            z_{j}
        \right)
    }{
        \sum_{i=1}^{n}
            \exp
            \left(
                z_{i}
            \right)
    }
$$

## Reference
* [Cross entropy - Wikipedia](https://en.wikipedia.org/wiki/Cross_entropy)
