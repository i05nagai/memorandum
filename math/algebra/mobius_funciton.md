---
title: Mobius Function
---

## Mobius Function

#### Definitioin Mobius Function

Let $$\mu: \mathbb{N} \rightarrow \{-1, 0, 1\}$$

$$
\begin{eqnarray}
    \mu(1) := 1,
    \nonumber
    \\
    \mu(n) := 0 \quad (\exists p: \text{ prime s.t. } p^{2} | n)
    \nonumber
    \\
    \mu(n) := (-1)^{k} \quad (n = p_{1}^{\alpha_{1}} \cdots p_{k}^{\alpha_{k}})
    .
    \nonumber
\end{eqnarray}
$$


<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem
- $n > 1$

$$
    \sum_{d | n}
        \mu(d)
    =
    0.
$$

#### proof
Let $n = p_{1}^{\alpha_{1}} \cdots p_{k}^{\alpha_{k}}$ be the prime factorization.
If the power of primes in $d$ is higher than 1, $\mu(d) = 0$.
We only need to consider divisors that the power of primes is at most 1.

$$
\begin{eqnarray}
    \sum_{d | n}
        \mu(d)
    & = &
        1
        -
        \left(
            \begin{array}{c}
                k \\
                1
            \end{array}
        \right)
        +
        \left(
            \begin{array}{c}
                k \\
                2
            \end{array}
        \right)
        -
        \cdots
        +
        (-1)^{r}
        \left(
            \begin{array}{c}
                k \\
                r
            \end{array}
        \right)
        +
        \cdots
    \nonumber
    \\
    & = &
        (1 - 1)^{k}
    \nonumber
    \\
    & = & 
        0
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


#### Theorem
- $F: \mathbb{N} \rightarrow \mathbb{C}$.

$$
    G(n)
    :=
    \sum_{d | n}
        F(d)
$$

Then

$$
    F(n)
    =
    \sum_{d|n}
        \mu(d) G(\frac{n}{d})
    .
$$

#### proof

$$
\begin{eqnarray}
    F(n)
    & = &
        \sum_{d|n}
            \mu(d) G(\frac{n}{d})
    \nonumber
    \\
    & = &
        \sum_{d|n}
            \mu(d)
            \sum_{d^{\prime} | \frac{n}{d}}
                F(d^{\prime})
    \nonumber
    \\
    & = &
        \sum_{d|n}
            \left(
                \sum_{d^{\prime} | \frac{n}{d}}
                    F(d^{\prime})
            \right)
            \mu(d)
    \nonumber
\end{eqnarray}
$$

Since

$$
\begin{eqnarray}
    \{
        (d^{\prime}, d)
        \mid
        d^{\prime} | \frac{n}{d},
        \
        d | n
    \}
    & = &
        \{
            (d^{\prime}, d)
            \mid
            d | \frac{n}{d^{\prime}},
            \
            d^{\prime} | n
        \}
        \quad
        (\because d^{\prime} | \frac{n}{d}, d | n \Leftrightarrow d | \frac{n}{d^{\prime}}, d^{\prime} | n ),
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \sum_{d|n}
        \left(
            \sum_{d^{\prime} | \frac{n}{d}}
                F(d^{\prime})
        \right)
        \mu(d)
    & = &
    \sum_{d^{\prime}|n}
        \left(
            \sum_{d | \frac{n}{d^{\prime}}}
                F(d^{\prime})
        \right)
        \mu(d)
    \nonumber
    \\
    & = &
        \sum_{d^{\prime}|n}
            \left(
                \sum_{d | \frac{n}{d^{\prime}}}
                    \mu(d)
            \right)
            F(d^{\prime})
    \nonumber
    \\
    & = &
        \mu(1)
        F(n)
    \nonumber
    \\
    & = &
        F(n)
    .
    \nonumber
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>

## Reference
