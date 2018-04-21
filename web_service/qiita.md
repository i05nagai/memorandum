---
title: Qiita
---

## Qiita

## 数式

### 集合

* `$$`
    `$$\\\{a \in \mathbb{R} \mid a > 0 \\\}$$`,

$$
    \\\{a \in \mathbb{R} \mid a > 0 \\\}
$$


* `math`
    * `$\\\{a \in \mathbb{R} \mid a > 0 \\\}$`,

```math
    \\\{a \in \mathbb{R} \mid a > 0 \\\}
```


```
$$
\begin{eqnarray}
    \\\{a \in \mathbb{R} \mid a > 0 \\\}
    & = &
        a_{1}
    \tag{a1}
    \\\\
    \\\{a \in \mathbb{R} \mid a > 0 \\\}
    & = &
        a_{1}
    \tag{a2}
\end{eqnarray}
$$
```

* tagにunderbarは２つ以上使えない

$$
\begin{eqnarray}
    \\\{a \in \mathbb{R} \mid a > 0 \\\}
    & = &
        a_{1}
    \tag{a1_b1}
    \\\\
    \\\{a \in \mathbb{R} \mid a > 0 \\\}
    & = &
        a_{2}
    \tag{a2_b2_c2}
\end{eqnarray}
$$

cases

$$
\begin{eqnarray}
    \phi(x)
    & = &
    \begin{cases}
        1 & (p_{1}(x) > kp_{0}(x))
        \\\\
        \gamma & (p_{1}(x) = kp_{0}(x))
        \\\\
        0 & p_{1}(x) < kp_{0}(x)
    \end{cases}
    \\\\
\end{eqnarray}
$$

eqnarray

$$
\begin{eqnarray}
    \exists \phi: \text{ test},
    \
    \exists k, \gamma \in \mathbb{R}
    \
    \text{ s.t. }
    \
    \mathrm{E}_{0}
    \left[
        \phi
    \right]
    & = &
        \alpha
    \tag{chap03-03-07}
    \\\\
    \phi(x)
    & = &
    \begin{cases}
        1
        &
        (p\_{1}(x) > kp\_{0}(x))
        \\\\
        \gamma
        &
            (p\_{1}(x) = kp\_{0}(x))
        \\\\
        0
        &
            p\_{1}(x) < kp\_{0}(x)
    \end{cases}
    \\\\
    & = &
        1\_{\\\{p\_{1} > kp\_{0}\\\}}(x)
        +
        \gamma
        1\_{\\\{p\_{1} = kp\_{0}\\\}}(x)
        \quad
        \mu
        \text{-a.e. } x
    \tag{chap03-03-08}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    F(z)
    & := &
        P_{0}
        \left(
            \left\\\{
                x \in \mathcal{X}
                \mid
                p\_{1}(x) \le z p\_{0}(x)
            \right\\\}
        \right)
    \\\\
    & = &
        \int_{\mathcal{X}}
            1\_{\{\frac{p\_{1}}{p\_{0}} \le z\}}(x)
            p\_{0}(x)
        \ \mu(dx)
    \tag{theorem-fundamental-neyman-peason-lemma-02-def-of-cdf}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \mu(
        \\\{
            x \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}}
            \mid
            p\_{\theta\_{0}}(x)
            \neq
            0,
            \
            T(x) \ge c
        \\\}
    )
    & = &
        \mu(
            \\\{
                x \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}}
                \mid
                T(x) \ge c
            \\\}
        )
    \\\\
    & > &
        0
\end{eqnarray}
$$

$$
\begin{eqnarray}
    F^{t^{\*}}(z)
    & := &
        \int\_{(-\infty, z]}
        \ P\_{\vartheta\_{0}}(t^{\*}, dt\_{1})
    \\\\
    U\_{1}^{t^{\*}}(p)
    & := &
        \inf
        \\\{
            z \in \mathbb{R}
            \mid
            F^{t^{\*}}(z)
            \ge
            p
        \\\}
    \\\\
    U\_{2}^{t^{\*}}(p)
    & := &
        \inf
        \\\{
            z \in \mathbb{R}
            \mid
            F^{t^{\*}}(z)
            \ge
            1 - \alpha + p
        \\\}
    \\\\
    \Gamma\_{1}^{t^{\*}}(p)
    & := &
        (p - F^{t^{\*}}(U\_{1}^{t^{\*}}(p)-))
        (F^{t^{\*}}(U\_{1}^{t^{\*}}(p)) -  F^{t^{\*}}(U\_{1}^{t^{\*}}(p)-))^{-}
    \\\\
    \Gamma\_{2}^{t^{\*}}(p)
    & := &
        (F^{t^{\*}}(U\_{2}^{t^{\*}}(p)) - (1 - \alpha) - p)
        (F^{t^{\*}}(U\_{2}^{t^{\*}}(p)) -  F^{t^{\*}}(U\_{2}^{t^{\*}}(p)-))^{-}
    \\\\
    \Psi^{t^{\*}}(t\_{1}, p)
    & := &
        1\_{(-\infty, U\_{1}^{t^{\*}}(p))}(t)
        +
        \Gamma\_{1}^{t^{\*}}(p)
        1\_{U\_{1}^{t^{\*}}(p)}(t)
        +
        \Gamma\_{2}^{t^{\*}}(p)
        1\_{U\_{2}^{t^{\*}}(p)}(t)
        +
        1\_{(U\_{2}^{t^{\*}}(p)), \infty)}(t)
    \\\\
    S^{t^{\*}}(p)
    & := &
        \int\_{\mathbb{R}}
            t
            \Psi^{t^{\*}}(t\_{1}, p)
        \ P\_{\vartheta\_{0}}(t^{\*}, dt\_{1})
\end{eqnarray}
$$
