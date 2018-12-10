---
title: Kolmogorov Inequality
---

## Kolmogorov Inequality

* $$[m:n] := \{m, m+1, \ldots, n\}$$,
    * $m \le n$,

#### Theorem Kolmogorov Inequality
* $X_{1}, \ldots, X_{n}$,
    * independent variables
    * $\mathrm{E}[X_{i}] = 0$,
    * $\mathrm{V}[X_{i}] < \infty $,

Then for $\lambda > 0$<

$$
\begin{eqnarray}
    P
    \left(
        \max_{k \in [1:n]}
            \abs{S_{k}}
        \ge
    \right)
    & \le &
        \frac{1}{\lambda^{2}}
        \mathrm{Var}
        \left[
            S_{n}
        \right]
    \nonumber
    \\
    & = &
        \frac{1}{\lambda^{2}}
        \sum_{k=1}^{n}
            \mathrm{E}
            \left[
                X_{k}^{2}
            \right]
\end{eqnarray}

$$

where

$$
\begin{eqnarray}
    S_{k}
    & := &
        \sum_{i=1}^{k}
            X_{i}
    \nonumber
\end{eqnarray}
$$

#### proof

$$
\begin{eqnarray}
    S_{i} - S_{i-1}
    & = &
        X_{i}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        - 2(S_{n} - S_{k})S_{k}
    \right]
    & = &
        \sum_{i=1}^{n}
            2
            \mathrm{E}
            \left[
                \sum_{i=k+1}^{n}
                    X_{i}
            \right]
            \mathrm{E}
            \left[
                S_{i-1}
            \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            S_{n}^{2} - S_{i-1}^{2}
        \right]
        -
        \mathrm{E}
        \left[
            S_{0}^{2}
        \right]
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    A_{k}
    & := &
        \{
            S_{k}
            \ge
            \lambda,
            \
            \forall j < k,
            \
            S_{j} < \alpha
        \}
    \nonumber
\end{eqnarray}
$$

Note that

$$
\begin{eqnarray}
    \bigcup_{k \in [1:n]}
        A_{k}
    =
    \left\{
        \max_{k \in [1:n]}
            \abs{S_{k}}
        \ge
        \alpha
    \right\}
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        S_{n}^{2}
    \right]
    & = &
        \int_{\sum_{k=1}^{n} A_{k}}
            S_{n}^{2}(\omega)
        \ P(d\omega)
    \nonumber
    \\
    & = &
        \sum_{k=1}^{n}
            \int_{A_{k}}
                (S_{n}(\omega) - S_{k}(\omega))^{2}
                -
                S_{k}^{2}(\omega)
                +
                2
                S_{k}(\omega)
                S_{n}(\omega)
            \ P(d\omega)
    \nonumber
    \\
    & = &
        \sum_{k=1}^{n}
            \int_{A_{k}}
                (S_{n}(\omega) - S_{k}(\omega))^{2}
                +
                S_{k}^{2}(\omega)
                -
                2
                S_{k}^{2}(\omega)
                +
                2
                S_{k}(\omega)
                S_{n}(\omega)
            \ P(d\omega)
    \nonumber
    \\
    & = &
        \sum_{k=1}^{n}
            \int_{A_{k}}
                (S_{n}(\omega) - S_{k}(\omega))^{2}
                +
                S_{k}^{2}(\omega)
                +
                2
                S_{k}(\omega)
                \left(
                    S_{n}(\omega)
                    -
                    S_{k}^{2}(\omega)
                \right)
            \ P(d\omega)
    \nonumber
    \\
    & \ge &
        \sum_{k=1}^{n}
            \int_{A_{k}}
                S_{k}^{2}(\omega)
                +
                2
                S_{k}(\omega)
                (S_{n}(\omega) - S_{k}(\omega))
            \ P(d\omega)
    \nonumber
    \\
    & = &
        \sum_{k=1}^{n}
            \int_{A_{k}}
                S_{k}^{2}(\omega)
            \ P(d\omega)
    \nonumber
    \\
    & \ge &
        \sum_{k=1}^{n}
            \alpha^{2}
            P(A_{k})
    \nonumber
    \\
    & = &
        \alpha^{2}
        P(\max_{k \in [1:n]}\abs{S_{k}} \ge \alpha)
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Kolmogorov's inequality \- Wikipedia](https://en.wikipedia.org/wiki/Kolmogorov%27s_inequality)
