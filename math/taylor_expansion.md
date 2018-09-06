---
title: Taylor Expansion
---

## Taylor Expansion


#### Thereom
* $I := [a, b] \subseteq \mathbb{R}$,
* $f: I \rightarrow \mathbb{R}$,
* $k \in \mathbb{N}$,

For all $x \in (a, b)$,

$$
\begin{eqnarray}
    f(x)
   & = &
        f(a)
        +
        f^{\prime}(a)
        (x - a)
        +
        \frac{1}{2!}
        f^{\prime\prime}(a)
        (x - a)^{2}
        +
        \cdots
        +
        \frac{1}{k!}
        f^{(k)}(a)
        (x - a)^{k}
        +
        h_{k}(x)
        (x - a)^{k}
    \nonumber
    \\
    & = &
        f(a)
        +
        \sum_{i=1}^{k}
        \frac{1}{k!}
        f^{(k)}(a)
        (x - a)^{k}
        +
        R_{k}(x)
    \nonumber
    .
\end{eqnarray}
$$

$R_{k}(x)$ has many forms

(1) If $f$ is $C^{k+1}((a, b))$ and $f^{(k)}$ is continuous on $I$, then

$$
\begin{eqnarray}
    R_{k}(x)
    & = &
        \frac{
            f^{(k + 1)}(z)
        }{
            (k + 1)!
        }
        (x - a)^{k + 1}
    \nonumber
\end{eqnarray}
$$

#### proof
(1)

Let $x \in \mathbb{R}$ be fixed.
Let $G: I \rightarrow \mathbb{R}$ be continuous on $I$ and diffierentiable between $(a, x)$.

$$
    F(t)
    :=
    f(t)
    +
    f^{\prime}(t)(x - t)
    +
    \frac{1}{2!}
    f^{\prime\prime}(t)(x - t)^{2}
    +
    \cdots
    +
    \frac{1}{k!}
    f^{(k)}(t)(x - t)^{k}
    .
$$

$$
\begin{eqnarray}
    F^{\prime}(t)
    & = &
        f^{\prime}(t)
        +
        \left(
            f^{\prime\prime}(t)(x - t)
            -
            f^{\prime}(t)
        \right)
        +
        \left(
            \frac{
                f^{(3)}(t)
            }{
                2!
            }
            (x - t)^{2}
            -
            \frac{
                f^{(2)}(t)
            }{
                1!
            }
            (x - t)
        \right)
        +
        \cdots
        \left(
            \frac{
                f^{(k+1)}(t)
            }{
                k!
            }
            (x - t)^{k}
            -
            \frac{
                f^{(k)}(t)
            }{
                (k - 1)!
            }
            (x - t)^{k - 1}
        \right)
    \nonumber
    \\
    & = &
        \frac{
            f^{(k+1)}(t)
        }{
            k!
        }
        (x - t)^{k}
    \nonumber
\end{eqnarray}
$$

By mean-value theorem, for some $z \in (a, x)$,

$$
\begin{eqnarray}
    & &
        \frac{
            F^{\prime}(z)
        }{
            G^{\prime}(z)
        }
        =
        \frac{
            F(x)
            -
            F(a)
        }{
            G(a)
            -
            G(a)
        }
    \nonumber
    \\
    & \Leftrightarrow &
        F(x)
        -
        F(a)
        =
        F^{\prime}(z)
        \frac{
            G(x)
            -
            G(a)
        }{
            G^{\prime}(z)
        }
    .
    \nonumber
\end{eqnarray}
$$

Note that $R_{k}(x) = F(a) - F(x)$.
Suppose that $G(t) := (t - x)^{k+1}$.

$$
\begin{eqnarray}
    F(x)
    -
    F(a)
    & = &
        \frac{
            f^{(k+1)}(z)
        }{
            k!
        }
        (x - z)^{k}
        \frac{
            G(x)
            -
            G(a)
        }{
            G^{\prime}(z)
        }
    \nonumber
    \\
    & = &
        \frac{
            f^{(k+1)}(z)
        }{
            k!
        }
        (x - z)^{k}
        \frac{
            -
            (a - x)^{k+1}
        }{
            (k + 1)
            (z - x)^{k}
        }
    \nonumber
    \\
    & = &
        \frac{
            f^{(k+1)}(z)
        }{
            (k + 1)!
        }
        (a - x)^{k+1}
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Thereom multiple variables
* $I \subseteq \mathbb{R}^{n}$,
    * open
    * convex
* $f: I \rightarrow \mathbb{R}$,
* $k \in \mathbb{N}$,

For all $x, a \in I$,

$$
\begin{eqnarray}
   f(x)
   & = &
        f(a)
        +
        \sum_{\abs{\alpha} \le k}
            \left(
                D^{\alpha}
                f(a)
            \right)
            \prod_{j=1}^{n}
                (x - a)^{\alpha_{j}}
        +
        \sum_{\abs{\alpha} = k}
            h_{\alpha}(x)
            \prod_{j=1}^{n}
                (x - a)^{\alpha_{j}}
    \nonumber
    .
\end{eqnarray}
$$

$R_{\alpha}(x)$ has many forms

(1) If $f$ is $C^{k+1}(I)$ and $D^{\alpha}f$ is continuous on $I$, then

$$
\begin{eqnarray}
    R_{\alpha}(x)
    & = &
        \sum_{\abs{\alpha} = k + 1}
            \frac{
                D^{\alpha}f(x + c(x - a))
            }{
                (k + 1)!
            }
            \prod_{j=1}^{n}
                (x - a)^{\alpha_{j}}
    \nonumber
\end{eqnarray}
$$

where $c \in [0, 1]$.

#### proof
(1)

Let $x, a \in \mathbb{R}$ be fixed.

$$
    g(t)
    :=
    f(a + t(x - a))
    .
$$

$$
\begin{eqnarray}
    g(1)
    & = &
        g(0)
        +
        \sum_{i=1}^{k}
            \frac{1}{k!}
            g^{(k)}(0)
        +
        \frac{
            g^{(k + 1)}(c)
        }{
            (k + 1)!
        }
\end{eqnarray}
$$

Let $G: I \rightarrow \mathbb{R}$ be continuous on $I$ and diffierentiable between $I$.

$$
    F(t)
    :=
    f(
    \sum_{\abs{\alpha} = k + 1}
        \frac{
            D^{\alpha}f(x + c(x - a))
        }{
            (k + 1)!
        }
        \prod_{j=1}^{n}
            (x - a)^{\alpha_{j}}
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Taylor's theorem \- Wikipedia](https://en.wikipedia.org/wiki/Taylor%27s_theorem)
