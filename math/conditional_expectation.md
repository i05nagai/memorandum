---
title: Conditional Expectation
---

## Conditional Expectation
Conditional expectation is defined in many different ways and written in various notations.
We summarize the definitions and nottations about conditional expectations.

#### Definition. conditional probability given sigma algebra
* $$(\Omega, \mathcal{F}, P)$$,
    * prob. sp.
* $$X: \Omega \rightarrow \mathbb{R}$$,
    * r.v.
* $\mathcal{G} \subset \mathcal{F}$
    * $\sigma$-algebra
* $Z: \Omega \rightarrow \mathbb{R}$,
    * measurable function

$Z$ is said to be conditional expectation given $\mathcal{G}$ if

$$
    A \in \mathcal{G},
    \
    \int_{A}
        X(\omega)
    \ dP(\omega)
    =
    \int_{A}
        Z(\omega)
    \ dP(\omega)
$$

We write $Z$ by

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G}
    \right]
    (\omega)
    :=
    Z(\omega)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. conditional probability given r.v.
* $$(\Omega, \mathcal{F}, P)$$,
    * prob. sp.
* $$X: \Omega \rightarrow \mathbb{R}$$,
    * r.v.
* $$Y: \Omega \rightarrow \mathbb{R}$$,
    * r.v.

$$\mathrm{E} \left[ X \mid \sigma(Y) \right]$$ is called be conditional expectation given $Y$.
We write

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        Y
    \right]
    (\omega)
    :=
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \sigma(Y)
    \right]
    (\omega)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. conditional probability over Y=y
* $$(\Omega, \mathcal{F}, P)$$,
    * prob. sp.
* $$X: \Omega \rightarrow \mathbb{R}$$,
    * r.v.
* $$Y: \Omega \rightarrow \mathbb{R}$$,
    * r.v.
* $g: \mathbb{R} \rightarrow \mathbb{R}$
    * $\mathcal{B}(\mathbb{R})$ measurable

$g$ is said to be conditional expectation of $X$ given $Y = y$ if

$$
    \forall B \in \mathcal{B}(\mathbb{R}),
    \
    \int_{Y^{-1}(B)}
        X(\omega)
    \ dP(\omega)
    =
    \int_{B}
        g(y)
    \ dP^{Y}(y)
    .
$$

We denote $g$ by

$$
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        Y = y
    \right]
    :=
    g(y)
    \quad
    (y \in \mathbb{R})
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
Since $$\sigma(Y) = \{Y^{-1}(B) \mid B \in \mathcal{B}(\mathbb{R})\}$$, the following equation holds.

$$
\begin{eqnarray}
    \forall B \in \mathcal{B}(\mathbb{R}),
    \
    \int_{B}
        \mathrm{E}
        \left[
        \left.
            X
        \right|
            Y = y
        \right]
    \ dP^{Y}(y)
    & = &
        \int_{Y^{-1}(B)}
            X(\omega)
        \ dP(\omega)
    \nonumber
    \\
    & = &
        \int_{Y^{-1}(B)}
            \mathrm{E}
            \left[
            \left.
                X
            \right|
                Y
            \right](\omega)
        \ dP(\omega)
    \nonumber
\end{eqnarray}
$$

Hence the difference between conditional expectation of $X$ given $Y$ and conditional expectation of $X$ of given $Y=y$ is just the domain of conditional expecation.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition
* $X: \Omega \rightarrow \mathbb{R}$,
    * r.v.
* $\mathcal{B} \subset \mathcal{F}$
    * $\sigma$-algebra
* $f: \mathbb{R} \rightarrow \mathbb{R}$
    * $\mathcal{B}$ measurable

If $X$ and $\mathcal{B}$ is independent, $$\mathrm{E}( \abs{f(X)} ) < \infty$$,

$$
    \mathrm{E}
    \left[
        f(X)
        \mid
        \mathcal{B}
    \right]
    =
    \mathrm{E}
    \left[
        f(X)
    \right]
    \mathrm{a.s.}
$$

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition
* $X: \Omega \rightarrow \mathbb{R}$,
    * r.v.
* $Y: \Omega \rightarrow \mathbb{R}$,
    * r.v.
* $\mathcal{B} \subset \mathcal{F}$
    * $\sigma$-algebra
* $f_{(X, Y)}: \mathbb{R} \rightarrow \mathbb{R}$
    * joint p.d.f. of $(X, Y)$
    * $\mathcal{B}$ measurable

(1)

$$
\begin{eqnarray}
    A
    & := &
        \{(x, y) \mid f_{X}(x) = 0\}
    \nonumber
    \\
    P((X, Y) \in A)
    & = &
        0
    \nonumber
\end{eqnarray}
$$

(2)

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        Y
    \right|
        X = a
    \right]
    =
    \int_{\mathbb{R}}
        y
        \frac{
            f_{(X, Y)}(a, y)
        }{
            f_{X}(a)
        }
    \ dy
\end{eqnarray}
$$

(3)

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        Y
    \right|
        X
    \right](\omega)
    =
    \int_{\mathbb{R}}
        y
        \frac{
            f_{(X, Y)}(X(\omega), y)
        }{
            f_{X}(X(\omega))
        }
    \ dy
    \nonumber
\end{eqnarray}
$$

#### proof
(1)

$$
\begin{eqnarray}
    P((X, Y) \in A)
    & = &
        \int_{A}
            f_{(X, Y)}(x, y)
        \ dx
        dy
    \nonumber
    \\
    & = &
        \int_{\{x \mid f_{X}(x) = 0\}}
        \int_{\mathbb{R}}
                f_{(X, Y)}(x, y)
        \ dy
        dx
    \nonumber
    \\
    & = &
        \int_{\{x \mid f_{X}(x) = 0\}}
                f_{(X, Y)}(x, y)
        \ dx
    \nonumber
    \\
    & = &
        0
    \nonumber
\end{eqnarray}
$$

(2)


(3)

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \mathrm{E}
        \left[
        \left.
            Y
        \right|
            X
        \right]
    \right]
    & = &
        \mathrm{E}
        \left[
            \int_{\mathbb{R}}
                y
                \frac{
                    f_{(X, Y)}(X, y)
                }{
                    f_{X}(X)
                }
            \ dy
        \right]
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}}
            \int_{\mathbb{R}}
                y
                \frac{
                    f_{(X, Y)}(x, y)
                }{
                    f_{X}(x)
                }
            \ dy
            f_{X}(x)
        \ dx
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}}
            \int_{\mathbb{R}}
                y
                f_{(X, Y)}(x, y)
            \ dx
        \ dy
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}}
            y
            f_{Y}(x, y)
        \ dy
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            Y
        \right]
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Remark
If the joint p.d.f. of $(X, Y)$ exists, the p.d.f. of $$\mathrm{E}\left[ Y \mid X \right]$$ is

$$
    p_{Y \mid X}(y)
    :=
    \frac{
        f_{(X, Y)}(X, y)
    }{
        f_{X}(X)
    }
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 1
* $(\Omega, \mathcal{F}, P)$,
* $\mathcal{G} \subseteq \mathcal{F}$,
    * sub $\sigma$-algebra
* $\mathcal{H} \subseteq \mathcal{G}$,
    * sub $\sigma$-algebra
* $X, Y$,
    * r.v.
* $(X_{n \in \mathbb{N}})$,
    * r.v.s


(1)

$$
\begin{equation}
    \mathrm{E}
    \left[
        \mathrm{E}
        \left[
        \left.
            X
        \right|
            \mathcal{G}
        \right]
    \right]
    =
    \mathrm{E}
    \left[
        X
    \right]
\end{equation}
$$

(2)

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        aX
        +
        bY
    \right|
        \mathcal{G}
    \right]
    =
    a
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G}
    \right]
    +
    b
    \mathrm{E}
    \left[
    \left.
        Y
    \right|
        \mathcal{G}
    \right]
\end{eqnarray}
$$

(3)

$$
\begin{eqnarray}
    X \ge 0,
    \
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G}
    \right]
    \ge
    0
\end{eqnarray}
$$

(4) If $0 \le X_{n}$, $X_{n} \nearrow X (n \rightarrow \infty)$, then

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        X_{n}
    \right|
        \mathcal{G}
    \right]
    \nearrow
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G}
    \right]
    \text{-a.s.}
\end{eqnarray}
$$

(5) If $X_{n} \ge 0$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        \liminf_{n \rightarrow \infty} X_{n}
    \right|
        \mathcal{G}
    \right]
    \le
    \liminf_{n \rightarrow \infty}
    \mathrm{E}
    \left[
    \left.
         X_{n}
    \right|
        \mathcal{G}
    \right]
    \text{-a.s.}
\end{eqnarray}
$$

(6) If $c: \mathbb{R} \rightarrow \mathbb{R}$ is a convex function,

$$
\begin{equation}
    c
    \left(
        \mathrm{E}
        \left[
        \left.
            X
        \right|
            \mathcal{G}
        \right]
    \right)
    \le
    \mathrm{E}
    \left[
    \left.
        c(X)
    \right|
        \mathcal{G}
    \right]
    \text{-a.s.}
\end{equation}
$$

(7)

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        \mathrm{E}
        \left[
        \left.
            X
        \right|
            \mathcal{G}
        \right]
    \right|
        \mathcal{H}
    \right]
    =
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{H}
    \right]
    \text{-a.s.}
\end{eqnarray}
$$

(8) If $Z$ is $\mathcal{G}$ measurable,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        Z
        X
    \right|
        \mathcal{G}
    \right]
    =
    Z
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G}
    \right]
    \text{-a.s.}
\end{eqnarray}
$$

(9) If $\mathcal{H}$ is independent on $\sigma(X) \vee \mathcal{G}$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G} \vee \mathcal{H}
    \right]
    =
    \mathrm{E}
    \left[
    \left.
        X
    \right|
        \mathcal{G}
    \right]
    \text{-a.s.}
\end{eqnarray}
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
