---
title: Notation
book_title: Theory and method of Bayes Statistics
book_chapter: 0
book_section: 0
---

## 0.0. Notation

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
        \frac{1}{Z_{n} \phi(w)}
        \phi(w)
        \prod_{i=1}^{n}
            p(X_{i} \mid w)^{\beta}
    \nonumber
    \\
    Z_{n}(\beta)
    & = &
        \int_{W}
            \phi(w)
            \prod_{i=1}^{n}
                p(X_{i} \mid w)^{\beta}
        \ dw
    .
\end{eqnarray}
$$

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
