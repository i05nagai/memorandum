---
title: Lesat Common Multiple
---

## Lesat Common Multiple

#### Definition Common Multiple
- $a_{1}, \ldots, a_{n} \in \mathbb{Z}$
    - $a_{i} \neq 0$ for all $i$

$$
    \mathrm{CM}(a_{1}, \ldots, a_{n})
    :=
    \{
        a \in \mathbb{Z}
        \mid
        \exists (k_{1}, \ldots, k_{n}) \in \mathbb{Z}^{n}
        \text{ s.t. }
        a = a_{i} k_{i}
    \}
    .
$$

We define positve common multiples

$$
    \mathrm{CM}_{+}(a_{1}, \ldots, a_{n})
    :=
    \mathrm{CM}(a_{1}, \ldots, a_{n})
    \cap
    \mathbb{N}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Definition LCM
- $a_{1}, \ldots, a_{n} \in \mathbb{Z}$
    - $a_{i} \neq 0$ for all $i$

$$
    \mathrm{lcm}(a_{1}, \ldots, a_{n})
    :=
    \min \mathrm{CM}_{+}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### proposition
- $a_{1}, \ldots, a_{n} \in \mathbb{Z}$
    - $a_{i} \neq 0$ for all $i$

Let $l := \mathrm{lcm}(a_{1}, \ldots, a_{n})$.
If $m$ is a common multiple, $l \mid m$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### propositoin
- $n \ge 7$,

$$
    \mathrm{lcm}(1, \ldots, n)
    \ge
    2^{n}
    .
$$

#### proof
Let $1 \le m \le n$ and $l_{n} := \mathrm{lcm}(1, \ldots, m)$
By integration by parts,

$$
\begin{eqnarray}
    I_{n, m}
    & := &
        \int_{0}^{1}
            x^{m - 1}(1 - x)^{n - m}
        \ dx
    \nonumber
    \\
    & = &
        \left[
            \frac{
                x^{m}(1 - x)^{n - m}
            }{
                m
            }
        \right]_{0}^{1}
        +
        \frac{(n - m)}{m}
        \int_{0}^{1}
            x^{m}(1 - x)^{n - m - 1}
        \ dx
    \nonumber
    \\
    & = &
        \frac{(n - m)}{m}
        \left[
            \frac{
                x^{m + 1}(1 - x)^{n - m - 1}
            }{
                m + 1
            }
        \right]_{0}^{1}
        +
        \frac{(n - m)}{m}
        \frac{(n - m - 1)}{m + 1}
        \int_{0}^{1}
            x^{m + 1}(1 - x)^{n - m - 2}
        \ dx
    \nonumber
    \\
    & = &
        \frac{(n - m)}{m}
        \frac{(n - m - 1)}{m + 1}
        \int_{0}^{1}
            x^{m + 1}(1 - x)^{n - m - 2}
        \ dx
    \nonumber
    \\
    & = &
        \frac{
            (n - m) (n - m - 1) \cdots 1
        }{
            m (m + 1) \cdots n
        }
    \nonumber
    \\
    & = &
        \frac{
            (n - m)! (m + 1)!
        }{
            n!
        }
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            m
            \left(
                \begin{array}{c}
                    n \\
                    m
                \end{array}
            \right)
        }
        \label{i_n_m_integration_by_parts}
    .
\end{eqnarray}
$$

On the other hand, by binominal theorem,


$$
\begin{eqnarray}
    I_{n, m}
    & = &
        \int_{0}^{1}
            x^{m - 1}(1 - x)^{n - m}
        \ dx
    \nonumber
    \\
    & = &
        \int_{0}^{1}
            x^{m - 1}
            \sum_{r=0}^{n - m}
                \left(
                    \begin{array}{c}
                        n - m \\
                        r
                    \end{array}
                \right)
                (-1)^{r}
                x^{n - m - r}
        \ dx
    \nonumber
    \\
    & = &
        \int_{0}^{1}
            \sum_{r=0}^{n - m}
                \left(
                    \begin{array}{c}
                        n - m \\
                        r
                    \end{array}
                \right)
                (-1)^{r}
                x^{n - r - 1}
        \ dx
    \nonumber
    \\
    & = &
        \sum_{r=0}^{n - m}
            \left[
                \left(
                    \begin{array}{c}
                        n - m \\
                        r
                    \end{array}
                \right)
                (-1)^{r}
                \frac{1}{n - r}
                x^{n - r}
            \right]_{0}^{1}
    \nonumber
    \\
    & = &
        \sum_{r=0}^{n - m}
            \left(
                \begin{array}{c}
                    n - m \\
                    r
                \end{array}
            \right)
            (-1)^{r}
            \frac{1}{n - r}
    .
    \nonumber
\end{eqnarray}
$$

That implies $l_{n} I_{n, m} \in \mathbb{Z}$.
Combining $$\eqref{i_n_m_integration_by_parts}$$, we have

$$
    m
    \left(
        \begin{array}{c}
            n \\
            m
        \end{array}
    \right)
    \mid
    l_{n}
    .
$$

$$
    n
    \left(
        \begin{array}{c}
            2n \\
            n
        \end{array}
    \right)
    \mid
    l_{2n}
$$

and

$$
    (n + 1)
    \left(
        \begin{array}{c}
            2n + 1\\
            n + 1
        \end{array}
    \right)
    =
    (2n + 1)
    \left(
        \begin{array}{c}
            2n\\
            n
        \end{array}
    \right)
    \mid
    l_{2n + 1}
$$

hold.

Since by definition, $$l_{2n} \mid l_{2n+1}$$,
There is $k_{1}, k_{2}, k_{3} \in \mathbb{Z}$ such that

$$
\begin{eqnarray}
    l_{2n + 1}
    & = &
        k_{1}
        l_{2n}
    \nonumber
    \\
    & = &
        k_{1}
        k_{2}
        n
        \left(
            \begin{array}{c}
                2n\\
                n
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        k_{3}
        (2n + 1)
        \left(
            \begin{array}{c}
                2n\\
                n
            \end{array}
        \right)
    .
    \nonumber
\end{eqnarray}
$$

Since $k_{1}k_{2} n = k_{3} (2n + 1)$,

$$
    n \mid k_{3}.
$$

We obtain

$$
    n (2n + 1)
    \left(
        \begin{array}{c}
            2n \\
            n
        \end{array}
    \right)
    \mid
    l_{2n+1}
    .
$$

Now

$$
\begin{eqnarray}
    (1 + x)^{2n}
    & = &
        \sum_{r=0}^{2n}
            \left(
                \begin{array}{c}
                    2n \\
                    r
                \end{array}
            \right)
            x^{2n - r}
    \nonumber
    \\
    & \le &
        \left(
            \begin{array}{c}
                2n \\
                n
            \end{array}
        \right)
        \sum_{r=0}^{2n}
            x^{2n - r}
    \nonumber
    .
\end{eqnarray}
$$

Taking $x = 1$,

$$
\begin{eqnarray}
    2^{2n}
    & \le &
        \left(
            \begin{array}{c}
                2n \\
                n
            \end{array}
        \right)
        (2n + 1)
        \label{binominal_ineaulity_01}
\end{eqnarray}
$$

Since $n \ge 4$,

$$
\begin{eqnarray}
    l_{2n + 1}
    & \ge &
        n (2n + 1)
        \left(
            \begin{array}{c}
                2n \\
                n
            \end{array}
        \right)
    \nonumber
    \\
    & \ge &
        n 4^{n}
        \quad
        (\because \eqref{binominal_ineaulity_01})
    \nonumber
    \\
    & = &
        n 2^{2n}
    \nonumber
    \\
    & \ge &
        4 2^{2n}
    \nonumber
    \\
    & = &
        2^{2n + 2}
    \nonumber
    \\
    & = &
        2^{2n + 1}
    .
    \nonumber
\end{eqnarray}
$$

Hence for $n \ge 9$

$$
    l_{n}
    \ge
    2^{n}
    .
$$

Since $l_{7} = 420$, $l_{8} = 840$, $2^{7} = 128$, and $2^{8} = 256$,

$$
    l_{n}
    \ge
    2^{n}
$$

for $n \ge 7$.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
- https://math.stackexchange.com/questions/851328/textlcm1-2-3-ldots-n-geq-2n-for-n-geq-7
- https://www.jstor.org/stable/2320934
- https://en.wikipedia.org/wiki/Least_common_multiple
