---
title: Notation
book_title: Theory and method of Bayes Statistics
book_chapter: 0
book_section: 0
---

## 0.0. Notation

#### Definition Little O
$$
\begin{eqnarray}
    & &
        f(x)
        =
        o(\abs{x - a}^{b})
    \nonumber
    \\
    & \Leftrightarrow &
        \lim_{x \rightarrow a}
            \frac{
                f(x)
            }{
                \abs{x - a}^{b}
            }
        =
        0
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Big O

$$
\begin{eqnarray}
    & &
        f(x)
        =
        O(\abs{x - a}^{b})
    \nonumber
    \\
    & \Leftrightarrow &
        \exists M > 0
        \text{ s.t. }
        \limsup_{x \rightarrow a}
            \frac{
                f(x)
            }{
                \abs{x - a}^{b}
            }
        <
        M
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Little O in probablity
$$
\begin{eqnarray}
    & &
        X_{n}
        =
        o_{p}(\frac{1}{n^{\alpha}})
        \quad
        (n \rightarrow \infty)
    \nonumber
    \\
    & \Leftrightarrow &
        \lim_{n \rightarrow \infty}
            P
            \left(
                X_{n}
                <
            \right)
            \frac{
                f(x)
            }{
                \abs{x - a}^{b}
            }
        =
        0
    .
\end{eqnarray}
$$

This definition is equivalent to $\abs{n^{\alpha} X_{n}} \overset{p}{\rightarrow} 0$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Big O in probablity

$$
\begin{eqnarray}
    & &
        X_{n}
        =
        O_{p}(\frac{1}{n^{\alpha}})
    \nonumber
    \\
    & \Leftrightarrow &
        \exists M > 0
        \text{ s.t. }
        \limsup_{n \rightarrow \infty}
            P(\abs{n^{\alpha} X_{n}} < \epsilon)
        <
        M
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

$$
\begin{eqnarray}
    \mathrm{E}_{X}
    \left[
        X
    \right]
    & = &
        \int
            x
            q(x)
        \ dx
\end{eqnarray}
$$

posterior distribution

$$
\begin{eqnarray}
    p(w \mid X^{n})
    & = &
        \frac{1}{Z_{n}(\beta)}
        \phi(w)
        \prod_{i=1}^{n}
            p(X_{i} \mid w)^{\beta}
    \nonumber
    \\
    Z_{n}(\beta)
    & := &
        \int_{W}
            \phi(w)
            \prod_{i=1}^{n}
                p(X_{i} \mid w)^{\beta}
        \ dw
    .
\end{eqnarray}
$$

Predictive distritbuion.

$$
\begin{eqnarray}
    p(X^{n})
    :=
    \int_{}
        \phi(w)
        \prod_{i=1}^{n}
            p(X_{i} \mid w)
    \ dw
    .
\end{eqnarray}
$$


$$
\begin{eqnarray}
    L(w)
    :=
    -
    \mathrm{E}_{X}
    \left[
        \log p(X \mid w)
    \right]
    .
\end{eqnarray}
$$


$$
\begin{eqnarray}
    L_{n}(w)
    :=
    -
    \frac{1}{n}
    \sum_{i=1}^{n}
        \log p(X_{i} \mid w)
    .
\end{eqnarray}
$$

Free energy.

$$
\begin{eqnarray}
    F_{n}(\beta)
    & := &
        - \frac{1}{\beta}
        \log Z_{n}(\beta)
    \nonumber
    \\
    F_{n}^{0}(\beta)
    & := &
        - \frac{1}{\beta}
        \log
            \int 
                \exp
                \left(
                    - n \beta K_{n}(w)
                \right)
                \phi(w)
            \ dw
    \nonumber
    .
\end{eqnarray}
$$

Generalization error

$$
\begin{eqnarray}
    G_{n}
    & := &
        \mathrm{E}_{X}
        \left[
            \log
                \mathrm{E}_{w}
                \left[
                    p(X \mid w)
                \right]
        \right]
    \nonumber
    \\
    G_{n}^{(0)}
    & := &
        -
        \mathrm{E}_{X}
        \left[
            \log
                \mathrm{E}_{w}
                \left[
                    \exp
                    \left(
                        - f(X, w)
                    \right)
                \right]
        \right]
    \nonumber
    .
\end{eqnarray}
$$

Emprical error

$$
\begin{eqnarray}
    T_{n}
    & := &
        - \frac{1}{n}
        \sum_{i=1}^{n}
            \log
                \mathrm{E}_{w}
                \left[
                    p(X_{i} \mid w)
                \right]
    \nonumber
    \\
    T_{n}^{(0)}
    & := &
        - \frac{1}{n}
        \sum_{i=1}^{n}
            \log
                \mathrm{E}_{w}
                \left[
                    \exp
                    \left(
                        - f(X_{i}, w)
                    \right)
                \right]
    \nonumber
    .
\end{eqnarray}
$$

Cumulant

$$
\begin{eqnarray}
    \mathcal{G}_{n}(\alpha)
    & := &
        \mathrm{E}_{X}
        \left[
            \log
                \mathrm{E}_{w}
                \left[
                    p(X \mid w)^{\alpha}
                \right]
        \right]
    \nonumber
    \\
    \mathcal{T}_{n}(\alpha)
    & := &
        \frac{1}{n}
        \sum_{i=1}^{n}
            \log
                \mathrm{E}_{w}
                \left[
                    p(X_{i} \mid w)^{\alpha}
                \right]
    \nonumber
\end{eqnarray}
$$

Entropy

$$
\begin{eqnarray}
    S
    =
    -
    \int
        q(x) \log q(x)
    \ dx
    .
\end{eqnarray}
$$


$$
\begin{eqnarray}
    f(x, w)
    :=
    \log
        \frac{
            p(x \mid w_{0})
        }{
            p(x \mid w)
        }
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    K(w)
    & := &
        \mathrm{E}_{X}
        \left[
            f(X, w)
        \right]
    \nonumber
    \\
    K_{n}(w)
    & := &
        \frac{1}{n}
        \sum_{i=1}^{n}
            f(X_{i}, w)
    \nonumber
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    J_{i,j} 
    :=
    \left(
        \frac{\partial L}{\partial w_{i} \partial w_{j}} (w_{0})
    \right)
\end{eqnarray}
$$

Stochastic process $\eta_{n}(w)$

$$
\begin{eqnarray}
    \eta_{n}(w)
    & := &
        \frac{1}{\sqrt{n}}
        \sum_{i=1}^{n}
            \left(
                K(w)
                -
                f(X_{i}, w)
            \right)
    \nonumber
    \\
    \xi_{n}
    & := &
        J^{-1/2}\nabla \eta_{n}(w_{0})
    \nonumber
    \\
    \hat{\xi}_{n}
    & := &
        J^{-1}\nabla \eta_{n}(w_{0})
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    I(w)
    :=
    \mathrm{E}_{X}
    \left[
        \nabla f(X, w)
        (\nabla f(X, w))^{\mathrm{T}}
    \right]
    -
    \nabla K(w)
    (\nabla K(w))^{\mathrm{T}}
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    Z_{n}^{(0)}(\beta)
    & := &
        \int
            \exp
            \left(
                - n \beta K_{n}(w)
            \right)
            \phi(w)
        \ dw
    \nonumber
    \\
    & = &
        \int
            \exp
            \left(
                - \beta
                \sum_{i=1}^{n}
                    \log
                        \frac{
                            p(X_{i} \mid  w_{0})
                        }{
                            p(X_{i} \mid  w)
                        }
            \right)
            \phi(w)
        \ dw
    \nonumber
    \\
    & = &
        \int
            \exp
            \left(
                - \beta
                \sum_{i=1}^{n}
                    \log
                        \frac{
                            p(X_{i} \mid  w_{0})
                        }{
                            p(X_{i} \mid  w)
                        }
            \right)
            \phi(w)
        \ dw
    \nonumber
    \\
    & = &
        \int
            \prod_{i=1}^{n}
                    \frac{
                        p(X_{i} \mid  w)^{\beta}
                    }{
                        p(X_{i} \mid  w_{0})^{\beta}
                    }
            \phi(w)
        \ dw
    \nonumber
    \\
    & = &
        Z_{n}(\beta)
        \frac{
            1
        }{
            \prod_{i=1}^{n}
            p(X_{i} \mid  w_{0})^{\beta}
        }
    \nonumber
    \\
    Z_{n}^{(1)}(\beta)
    & := &
        \int_{K(w) < \epsilon}
            \exp
            \left(
                - n \beta K_{n}(w)
            \right)
            \phi(w)
        \ mu(dx)
    \nonumber
    \\
    Z_{n}^{(2)}(\beta)
    & := &
        \int_{K(w) \ge \epsilon}
            \exp
            \left(
                - n \beta K_{n}(w)
            \right)
            \phi(w)
        \ mu(dx)
    .
    \nonumber
\end{eqnarray}
$$
