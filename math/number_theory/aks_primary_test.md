---
title: AKS Primary Test
---

## AKS Primary Test

#### Definition

$$
    o_{r}(n)
    := 
    \min
    \{
        e
        \mid
        n^{e}
         \equiv
        1
        (\mathrm{mod}\ r)
    \}
    .
$$

$$
    (X + a)^{n}
    \equiv
    X^{n} + a
    (\mathrm{mod}\ X^{r} - 1, n)
    \overset{\mathrm{def}}{\Leftrightarrow}
    \exists f, g
    \text{ s.t. }
    (X + a)^{n}
    -
    X^{n} + a
    =
    (X^{r} - 1)g
    +
    nf
$$

## Algorithm
$n > 1$.

- Step 1. If $n = a^{b}$ for some $a \in \mathbb{N}$ and $b \in \mathbb{N}, b > 1$, output COMPOSITE
- Step 2. Find

$$
    r :=
    \min
    \{
        r^{\prime}
        \mid
        o_{r^{\prime}}(n) > (\log n)^{2}
    \}
    .
$$

- Step 3. If $1 < (a, n) < n$ for some $a \ge $, output COMPISITE
- Step 4. If $n \ge r$, output PRIME
- Step 5. For $a = 1$ to $\lfloor \sqrt{\phi(r)} \log n \rfloor$ do
    - if $(X + a)^{n} \neq X^{n} + a (\mathrm{mod}\ X^{r} - 1, n)$, output COMPSITE
- Step 6. Output PRIME

#### Lemma 2.1
- $a \in \mathbb{Z}$,
- $n \in \mathbb{N}$,
    - $n \ge 2$,
- $(a, n) = 1$,

$n$ is prime if and only if

$$
    (X + a)^{n} \equiv X^{n} + a (\mathrm{mod}\ n)
$$

#### proof

$$
\begin{eqnarray}
    (X + a)^{n}
    -
    (X^{n} + a)
    & = &
        \sum_{r=0}^{n}
            \left(
                \begin{array}{c}
                    n \\
                    r
                \end{array}
            \right)
            X^{r}
            a^{n - r}
        - X^{n}
        - a
    \nonumber
    \\
    & = &
        \sum_{r=1}^{n-1}
            \left(
                \begin{array}{c}
                    n \\
                    r
                \end{array}
            \right)
            X^{r}
            a^{n - r}
    \label{lemma_02_01_01}
\end{eqnarray}
$$

(only if part)
If $n$ is prime, for $1 \ge r \ge n$,

$$
    \left(
        \begin{array}{c}
            n \\
            r
        \end{array}
    \right)
    \equiv
    \frac{
        n!
    }{
        (n - r)!r!
    }
    \equiv
    0
    (\mathrm{mod}\ n)
    .
$$

So $$\eqref{lemma_02_01_01}$$ holds.

(if part)

If $n$ is composite, there is a prime $q \in \mathbb{N}$ and integer $k \mathbb{N}$ such that $n = q^{k}d$.
$q^{k}$ does not divide $${n \choose q}$$.
Indeed, 

$$
\begin{eqnarray}
    \left(
        \begin{array}{c}
            n \\
            q
        \end{array}
    \right)
    & = &
        \frac{
            n!
        }{
            q! (n - q)!
        }
    \nonumber
    \\
    & = &
        \frac{
            q^{k - 1}d (n - 1) \cdots (n - q + 1)
        }{
            (q - 1)!
        }.
\end{eqnarray}
$$

Since there is no multiple of $q$ between $(n-1)$ and $(n - q + 1)$, $q^{k}$ cannot divide the factors in the numerator.
Also, $(a^{n - q}, q^{k}) = 1$.
Indeed, if $(a^{n-q}, q^{k}) \neq 1$, there is a common divisor $$d_{1}$$.
Since $q$ is a prime, $d_{1} = q^{l}$ for some $1 \le l \le k$.
Hence $q$ is a common divisor as well.
However, if $q \mid a^{n - q}$, $q | a$.
This contradicts to $(a, n) = 1$.
Therefore, the coefficient of $X^{q}$ is not zero (mod $n$).

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 4.1
The algorithm returns PRIME if and only if $n$ is prime.

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma 4.2
If $n$ is prime, the algorithm returns PRIME.

#### proof
If $n$ is prime, Step 1 and Step 3 do not return COMPIOSITE.
At Step 5, by lemma 2.1, 


<div class="end-of-statement" style="text-align: right">■</div>


## Reference
- https://en.wikipedia.org/wiki/AKS_primality_test
