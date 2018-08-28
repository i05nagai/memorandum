---
title: Inverse Transform Method
---

## Inverse Transform Method
Inverse transform method is also known as inversion method.
The method generates random vairable with cumulative distribution $F$ from an uniformly distributed random variable.

### One-dimensional case
* $$(\Omega, \mathcal{F}, P)$$,
    * probability space
* $$F: \mathbb{R} \rightarrow [0, 1]$$,
    * 1-dim c.d.f.

$$
    F^{-1}(u)
    :=
    \inf
    \{
        x \in \mathbb{R} \mid F(x) \ge u
    \}
$$

$F$ is monotonically increasing so that this definition is well-defined.

### Proposition1.
$$
\begin{eqnarray}
    F^{-1}(u) \le y
    & \Leftrightarrow &
        u \le F(y),
\end{eqnarray}
$$

### proof.
($\Rightarrow$)
There is a sequence $$y_{n}$$ such that $$y_{n} \searrow y^{*} := F^{-1}(y)$$, $$F(y_{n}) \ge u$$.
Since $F$ is right continuous, $$F(y^{*}) \ge u$$.
$$F$$ is monotone so that $$F(y^{*}) \le F(y)$$.

($\Leftarrow$)
$$u \le F(y)$$ implies $$y \in \{x \in \mathbb{R} \mid F(x) \ge u\}$$.
Hence by definition of $$F^{-1}$$, $$F^{-1}(u) \le y$$.

<div class="QED" style="text-align: right">$\Box$</div>

### Thereom2. Inversion method
Let $U$ be uniformly distributed random variable on $(0, 1)$ (i.e. $$U:\Omega \rightarrow [0, 1]$$).
Then $F^{-1}(U)$ is a random variable with distribution $F$.

### proof.
$$
\begin{eqnarray}
    P(\{\omega \mid F^{-1}(U(\omega)) \le x\})
    & = &
        P(\{\omega \mid U(\omega) \le F(x)\})
    \nonumber
    & = &
        F(x)
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Multi-dimensional case
* $$(\Omega, \mathcal{F}, P)$$,
    * probability space
* $$X: \Omega \rightarrow \mathbb{R}^{n}$$,
    * $n$-dim r.v.
* $$\mathcal{B}(\mathbb{R}^{n})$$,
    * borel sets
* $$\mathcal{I}_{n}$$,

$$
    \mathcal{I}_{n}
    :=
    \{
        (-\infty, x_{1}] \times \cdots \times (-\infty, x_{n}]
        \mid
        x := (x_{1}, \ldots, x_{n}) \in \mathbb{R}^{n}
    \}
    \cup
    \{\mathbb{R}^{n}\}
$$

* $$J_{n}: \mathbb{R}^{n} \rightarrow \mathcal{I}_{n}$$,
    * $$J_{n}(x) := (-\infty, x_{1}] \times \cdots \times (-\infty, x_{n}]$$,

Cumulative distribution function of $X$ is defined as

$$
    x \in \mathbb{R}^{n},
    \
    F(x) := P(X^{-1}(J_{n}(x)))
    .
$$

$$\mathcal{I}_{n}$$ is a $\pi$-system so that the RHS of the above equation uniquly determines probability measure over $$(\mathbb{R}^{n}, \mathcal{B}(\mathbb{R}^{n}))$$.
$F$ is monotonically increasing so that we can define

$$
\begin{eqnarray}
    \mathcal{A}
    & := &
        \{
            I
            \in \mathcal{J}_{n}
            \mid
            \exists
            x \in \mathbb{R}^{n},
            \
            I = J_{n}(x),
            \
            F(x) \ge u
        \}
    \\
    F^{-1}(u)
    & := &
        \inf_{I \in \mathcal{A}}
            I
    \nonumber
    \\
    & = &
        \bigcap_{I \in \mathcal{A}}
            I
    .
    \nonumber
\end{eqnarray}
$$

where inf is taken as infimum of family of sets.
The proposition1 is easily exntend to multi dimensional case.

### Proposition3.

$$
    F^{-1}(u) \subseteq J_{n}(y)
    \Leftrightarrow
    u \le F(y)
$$

### proof.
($\Rightarrow$)
We can construct a sequence of sets converging to $$F^{-1}(u)$$.
Let $$\phi_{i}(J_{n}(x)) := x_{i}$$ and

$$
    z_{i}
    :=
    \inf
    \{
        \phi_{i}(I) \in \mathbb{R}
        \mid
        I \in \mathcal{A}
    \}
    .
$$

We define $$z := (z_{1}, \ldots, z_{n})$$.
Then we observe 

$$
    F^{-1}(u)
    =
    J_{n}(z)
    .
$$

Indeed, $\subseteq$ is obvious so that we will show $\supseteq$.
To show that, it suffices to prove

$$
    \forall I \in \mathcal{A},
    \
    J_{n}(z) \subseteq I.
$$

Suppose that $$ \exists I \in \mathcal{A}$$ such that

$$
    \exists z^{\prime} := (z_{1}^{\prime}, \ldots, z_{n}^{\prime}) \in J_{n}(z),
    \
    z^{\prime} \notin I
    .
$$

This implies that $$\exists z^{\prime}_{i} \in \mathbb{R}$$ s.t. $$\phi_{i}(I) < z_{i}^{\prime} \le z_{i}$$.

($\Leftarrow$)
$u \le F(y)$ implies $$J_{n}(y) \in \mathcal{A}$$. That is $$F^{-1}(u) \subseteq J_{n}(y)$$.

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem4. Inversion Method
Let $U$ be uniformly distributed random variable on $(0,1)$ (i.e. $$U:\Omega \rightarrow (0,1)$$).
Then $$F^{-1}(U)$$ is a random variable with distribution $F$.

### proof.
Let $X := F^{-1}(U)$.
Then by proposition3,

$$
\begin{eqnarray}
    P(X^{-1}(J_{n}(x)))
    & = &
        P(\{\omega \mid F^{-1}(U(\omega)) \subseteq J_{n}(x) \})
    \nonumber
    \\
    & = &
        P(\{\omega \mid U(\omega) \le F(x) \})
    \nonumber
    \\
    & = &
        F(x)
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


### Example1 uniform distribution over unit ball

$$
\begin{eqnarray}
    h: (-1, 1) \rightarrow \mathbb{R},
    \quad
    h(x)
    & := &
        \mathrm{tanh}^{-1}(x)
    \nonumber
    \\
    C_{a, b}
    & := &
        (a, b)^{n}
        \subseteq
        \mathbb{R}^{n}
    \nonumber
\end{eqnarray}
    .
$$

$$
\begin{eqnarray}
    \phi_{0}: C_{0, 1} \rightarrow C_{-1, 1},
    \quad
    \phi_{0}(x)
    & := &
        2x - 1
    \nonumber
    \\
    \phi_{1}: C_{-1, 1} \rightarrow \mathbb{R},
    \quad
    \phi_{1}(x_{1}, \ldots, x_{n})
    & := &
        (
            h(x_{1}),
            \cdots
            h(x_{n})
        )
    \nonumber
    \\
    \phi_{2}: \mathbb{R} \rightarrow B_{0, 1},
    \quad
    \phi_{2}(x)
    & := &
        \frac{
            x
        }{
            \sqrt{
                1
                +
                |x|^{2}
            }
        }
    \nonumber
    \\
    \phi: C_{0, 1} \rightarrow B_{0, 1},
    \quad
    \phi(x_{1}, \ldots, x_{n})
    & := &
        \phi_{2}(\phi_{1}(\phi_{0}(x_{1}, \ldots, x_{n})))
    .
    .
\end{eqnarray}
    .
$$

$\phi$ is bijection.
$\phi^{-1}: real$ is continuous.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
