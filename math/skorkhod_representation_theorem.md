---
title: Skorokhod Representation Theorem
---

## Skorokhod Representation Theorem
* $(\Omega, \mathcal{F}, P) := ([0, 1], \mathcal{B}([0, 1]), P)$,
    * $\mathcal{B}([0, 1])$ borrel sigma algebra over $[0, 1]$,
    * $P$ is Lebesgue measure over $[0, 1]$
    * the triplet is probability space
* $F: \mathbb{R} \rightarrow [0, 1]$
    * non decreasing
    * $\lim_{x \rightarrow \infty}F(x) = 1$,
    * $\lim_{x \rightarrow -\infty}F(x) = 0$,
    * right continuous

* (a)

$$
\begin{eqnarray}
    \omega \in \Omega,
    \quad
    A^{+}(\omega)
    & := &
        \{
            z \in \mathbb{R}
            \mid
            F(z)
            >
            \omega
        \}
    \nonumber
    \\
    \omega \in \Omega,
    \quad
    X^{+}(\omega)
    & := &
        \inf
            A(\omega)
    \nonumber
    \\
    & = &
        \sup\{
            y \in \mathbb{R}
            \mid
            F(y)
            \le
            \omega
        \}
    \nonumber
    \\
    \omega \in \Omega,
    \quad
    A^{-}(\omega)
    & := &
        \{
            z \in \mathbb{R}
            \mid
            F(z)
            \ge
            \omega
        \}
    \nonumber
    \\
    \omega \in \Omega,
    \quad
    X^{-}(\omega)
    & := &
        \inf
            A^{-}(\omega)
    \nonumber
    \\
    & = &
        \sup\{
            y \in \mathbb{R}
            \mid
            F(y)
            <
            \omega
        \}
    \nonumber
\end{eqnarray}
$$

* (b) $X^{-1}$ has distribution function $F$,
* (c) $X^{+}$ has distribution function $F$, and

$$
    P(X^{+} = X^{-1})
    =
    1
$$

## proof
(a)

We first remember that

$$
\begin{eqnarray}
    (z > X^{-}(\omega))
    & \Rightarrow &
        (F(z) \ge \omega)
    .
    \nonumber
\end{eqnarray}
$$

Indeed, suppose that $F(z) < \omega$ for some $\omega$.
There exists $z^{\prime} \in A^{-}(\omega)$ such that $X^{-}(\omega) < z^{\prime} < z$.
By monotoncity, we have $F(X^{-}(\omega)) \le F(z^{\prime}) \le F(z) < \omega$.
However $z^{\prime} \in A^{-}(\omega)$ contradicts $F(z^{\prime}) < \omega$.

We can take a sequence $$\{z_{n}\}_{n \in \mathbb{N}} \subset A^{-}(\omega)$$ which converges to $X^{-}(\omega)$.
By $F(z^{n}) \ge \omega$ and right continuity of $F$, we have

$$
\begin{eqnarray}
    F(X^{-}(\omega))
    \ge
    \omega
    .
    \nonumber
\end{eqnarray}
$$

Combining above, we have

$$
    (X^{-}(\omega) \le c)
    \Rightarrow
    (
        \omega
        \le
        F(X^{-}(\omega))
        \le
        F(c)
    )
    .
$$

Thus,

$$
    (\omega \le F(c))
    \Leftrightarrow
    (X^{-}(\omega) \le c)
$$

so that

$$
    P(X^{-} \le c)
    =
    F(c)
    .
$$



<div class="QED" style="text-align: right">$\Box$</div>


## Reference
