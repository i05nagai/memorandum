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

#### Softmax function
$j$ -th softmax

$$
\begin{eqnarray}
    f(x; j)
    & := &
        \frac{
            \exp
            \left(
                x^{\mathrm{T}}
                w_{j}
            \right)
        }{
            \sum_{i=1}^{n}
                \exp
                \left(
                    x^{\mathrm{T}}
                    w_{i}
                \right)
        }
    \nonumber
    \\
    P(Y=j \mid X = x)
    & := &
        \frac{
            \exp
            \left(
                x_{j}^{\mathrm{T}}
                w_{j}
            \right)
        }{
            \sum_{i=1}^{n}
                \exp
                \left(
                    x_{i}^{\mathrm{T}}
                    w_{i}
                \right)
        }
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Binary Logistic function
* Other names
    * Binary logistic probability function.
    * softmax function
        * Special case of softmax function
    * Binary logistic regression function

$$
\begin{eqnarray}
    f(x; 1)
    & := &
        \frac{
            \exp
            \left(
                x^{\mathrm{T}}
                w_{1}
            \right)
        }{
            \exp
            \left(
                x^{\mathrm{T}}
                w_{1}
            \right)
                +
            \exp
            \left(
                x^{\mathrm{T}}
                w_{2}
            \right)
        }
    \nonumber
    \\
    & = &
        \frac{
            \exp
            \left(
                x^{\mathrm{T}}
                (w_{1} - w_{2})
            \right)
        }{
            \exp
            \left(
                x^{\mathrm{T}}
                (w_{1} - w_{2})
            \right)
                +
            1
        }
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            1
            +
            \exp
            \left(
                x^{\mathrm{T}}
                (w_{2} - w_{1})
            \right)
        }
    \nonumber
    \\
    P(Y=1 \mid X = x)
    & := &
        f(x; 1)
    \nonumber
    \\
    P(Y=2 \mid X = x)
    & := &
        1 - f(x; 1)
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Cross entropy - Wikipedia](https://en.wikipedia.org/wiki/Cross_entropy)
* [Softmax function \- Wikipedia](https://en.wikipedia.org/wiki/Softmax_function)
