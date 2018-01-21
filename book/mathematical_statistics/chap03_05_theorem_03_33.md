---
title: Theorem 3.33
---

## Theorem 3.33

$$
\begin{eqnarray}
    U_{1}^{t^{*}}(0)
    & = &
        \inf
        \{
            z \in \mathbb{R}
            \mid
            F^{t^{*}}(z)
            \ge
            0
        \}
    \nonumber
    \\
    & = &
        -\infty
    \nonumber
    \\
    U_{2}^{t^{*}}(0)
    & = &
        \inf
        \{
            z \in \mathbb{R}
            \mid
            F^{t^{*}}(z)
            \ge
            1 - \alpha
        \}
    \nonumber
\end{eqnarray}
$$

By proposition 3.19, $$P_{\bar{\theta}}(\cdot \mid t^{*})$$ is a regular conditional probability of $T_{1}$ given $$T^{*} = t^{*}$$ with respect to $P_{\bar{\theta}}$.
For all level $\alpha$ unabiased test $\phi$,

$$
\begin{eqnarray}
    \int_{\mathbb{R}}
        \phi(t_{1}, t^{*})
    \ P_{(b, b^{*})}(d t_{1} \mid t^{*})
    & = &
        \int_{\mathbb{R}}
            \alpha
        \ P_{(b, b^{*})}(d t_{1} \mid t^{*})
    \nonumber
    \\
    & = &
        \alpha
        \quad
        P_{(b, b^{*})}^{T^{*}}\text{-a.s.}
    \label{chap03_03_36}
\end{eqnarray}
$$
