---
title: Kolmogorov Extension Theorem
---

## Kolmogorov Extension Theorem
* $\mathfrak{S}_{n}$,
    * symmetric group with order $n$

$$
\begin{eqnarray}
    \mathcal{T}^{n}
    & := &
        \{\tilde{t} := (t_{1}, \ldots, t_{n}) \mid t_{i} \neq t_{j}\}
    \nonumber
    \\
    \tilde{t} := (t_{1}, \ldots, t_{n}) \in \mathcal{T}^{n},
    \
    \tau \in \mathfrak{S}_{n},
    \
    \tau(\tilde{t})
    & := &
        (t_{\tau(1)}, \ldots, t_{\tau(n)})
        \in
        \mathcal{T}^{n}
    \nonumber
    \\
    \mathcal{T}
    & := &
        \bigcup_{n \in \mathbb{N}}
            \mathcal{T}^{n}
    \nonumber
    \\
    \mathcal{T}^{\infty}
    & := &
        \{
            (t_{1}, t_{2}, \ldots) \in \mathbb{R}^{\mathbb{N}}
            \mid
            t_{1} < t_{2} < \ldots
        \}
    .
    \nonumber
    \\
    \tilde{t} \in \mathcal{T}^{n},
    \
    \abs{\tilde{t}}
    & := &
        n
    \nonumber
    \\
    \tilde{t}_{1} := (t_{1}, \ldots, t_{n}), \tilde{t}_{2} := (s_{1}, \ldots, s_{m})\in \mathrm{T},
    \
    (\tilde{t}_{1}, \tilde{t}_{2})
    & := &
        (t_{1}, \ldots, t_{n}, s_{1}, \ldots, s_{m})
        \in
        \mathrm{T}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \tau \in \mathfrak{S}_{n},
    \
    A \in \mathcal{B}(\mathbb{R}^{n}),
    \
    \tau(A)
    :=
    \{
        (a_{\tau(1)}, \ldots, a_{\tau(n)})
        \mid
        (a_{1}, \ldots, a_{n}) \in A
    \}
    \nonumber
\end{eqnarray}
$$

With this notation, it is easy to confirm that

$$
\begin{eqnarray}
    \tau \in \mathfrak{S}_{n},
    \
    A_{i} \in \mathcal{B}(\mathbb{R}),
    \
    \tau(A_{1} \times \cdots \times A_{n})
    =
    A_{\tau(1)} \times \cdots \times A_{\tau(n)}
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \Omega
    & := &
        \mathbb{R}^{[0, \infty)}
    \nonumber
    \\
    \tilde{t} \in \mathcal{T},
    \
    \omega(\tilde{t})
    & := &
        (\omega(t_{1}), \ldots, \omega(t_{n}))
        \in
        \mathbb{R}^{n}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \tilde{t} \in \mathcal{T}^{n},
    \
    A \in \mathcal{B}(\mathbb{R}^{n}),
    \
    C(A, \tilde{t})
    & := &
        \{
            \omega \in \Omega
            \mid
            \omega(\tilde{t})
            \in A
        \},
    \nonumber
    \\
    \mathcal{C}
    & := &
        \{
            C(A, \tilde{t})
            \mid
            n \in \mathbb{N},
            \
            A \in \mathcal{B}(\mathbb{R}^{n}),
            \
            \tilde{t} \in \mathcal{T}^{n}
        \},
    \nonumber
    \\
    \mathcal{B}(\mathbb{R}^{[0, \infty)})
    & := &
        \sigma(\mathcal{C})
    \nonumber
\end{eqnarray}
$$

#### Proposition 1
(1) $\mathcal{C}$ is $\pi$-system.

(2) $\mathcal{C}$ is an algebra on $\Omega$.

(3) If $$C(A_{1}, \tilde{t}_{1}) = C(A_{2}, \tilde{t}_{2})$$,

$$
    \exists n \in \mathbb{N},
    \
    \exists A \in \mathcal{B}(\mathbb{R}^{n}),
    \
    \exists \tilde{t} \in \mathcal{B}(\mathbb{R}^{n}),
    \
    \text{ s.t. }
    C(A, \tilde{t}) = C(A_{i}, \tilde{t}_{i})
    \quad
    (i = 1, 2)
    .
$$

(4) Suppose $$C(A, \tilde{t}) \in \mathcal{C}$$. Then

$$
    \forall \tilde{s} \in \mathcal{T},
    \
    n := \abs{\tilde{s}},
    \
    \tilde{u} := (\tilde{t}, \tilde{s}),
    \
    \tilde{u}^{\prime} := (\tilde{s}, \tilde{t}),
    \
    C(A \times \mathbb{R}^{n}, \tilde{u})
    =
    C(A, \tilde{t})
    =
    C(\mathbb{R}^{n} \times A, \tilde{u}^{\prime})
    .
$$

(5)

Let $$C(A_{i}, \tilde{t}_{i}) \in \mathcal{C}$$. Then

$$
    C(A_{1} \times A_{2}, \tilde{t})
    =
    C(A_{1} \times \mathbb{R}^{n_{2}}, \tilde{t})
    \cap
    C(\mathbb{R}^{n_{1}} \times A_{2}, \tilde{t})
    .
$$

#### proof
(1)

(2)

(3)

Let

$$
\begin{eqnarray}
    i = 1, 2,
    \
    n_{i}
    & := &
        \abs{\tilde{t}_{i}}
    \nonumber
    \\
    n
    & := &
        n_{1} + n_{2}
    \nonumber
    \\
    A
    & := &
        A_{1} \times A_{2}
    \nonumber
    \\
    \tilde{t}
    & := &
        (\tilde{t}_{1}, \tilde{t}_{2})
    .
    \nonumber
\end{eqnarray}
$$

Let $$\omega \in C(A_{1}, \tilde{t}_{1})$$ be fixed.
Since $\omega \in C(A_{2}, \tilde{t}_{2})$,

$$
\begin{eqnarray}
    \omega(\tilde{t}_{1})
    & \in &
        A_{1},
    \nonumber
    \\
    \omega(\tilde{t}_{2})
    & \in &
        A_{2}
    .
    \nonumber
\end{eqnarray}
$$

Hence

$$
    \omega(\tilde{t})
    =
    (\omega(\tilde{t}_{1}), \omega(\tilde{t}_{1}))
    \in
    A_{1} \times A_{2}
    .
$$

Therefore, $$C(A_{1}, \tilde{t}_{1}) \subseteq C(A, \tilde{t})$$
The opposite inclusion is obvious from the above discussion.

(4)

Let $\tilde{s} \in \mathcal{T}$ be fixed.
We will show that the equality holds.
Let $\omega \in C(A, \tilde{t})$ be fixed.

$$
    \omega(\tilde{t}) \in A
    \Rightarrow
    \omega(\tilde{u})
    =
    (\omega(\tilde{t}), \omega(\tilde{s})) \in A \times \mathbb{R}^{n},
    \
    \omega(\tilde{u}^{\prime})
    =
    (\omega(\tilde{s}), \omega(\tilde{t})) \in \mathbb{R}^{n} \times A
    .
$$

Hence $C(A, \tilde{t}) \subseteq C(A\times \mathbb{R}^{n}, \tilde{u})$ and $C(A, \tilde{t}) \subseteq C(\mathbb{R}^{n} \times A, \tilde{u}^{\prime})$.
Similarly, we can prove the opposite inclusion from the above discussion.

(5)

<div class="QED" style="text-align: right">$\Box$</div>

Note that (3) can be shown from (4) and (5).

#### Definition consistensy
* $$\{Q_{\tilde{t}}\}_{\tilde{t} \in \mathcal{T}}$$,
    * $Q_{\tilde{t}}$ is a probability measure on $$(\mathbb{R}^{\abs{\tilde{t}}}, \mathcal{B}(\mathbb{R}^{\abs{\tilde{t}}})$$,

$$\{Q_{\tilde{t}}\}$$ is said to be consistent if

(a)

$$
    n := \abs{\tilde{t}},
    \
    \forall A_{i} \in \mathcal{B}(\mathbb{R}),
    \
    Q_{\tilde{t}}(A_{1}\times \cdots \times A_{n})
    =
    Q_{\tilde{t}}(\tau(A_{1}\times \cdots \times A_{n}))
    .
$$

(b) If $\tilde{t} := (t_{1}, \ldots, t_{n}) \in \mathcal{T}^{n}$ and $\tilde{s} := (t_{1}, \ldots, t_{n-1}) \in \mathcal{T}^{n-1}$,

$$
    \forall A \in \mathcal{B}(\mathbb{R}^{n-1}),
    \
    Q_{\tilde{t}}(A \times \mathbb{R})
    =
    Q_{\tilde{s}}(A)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 2
* $$\{Q_{\tilde{t}}\}_{\tilde{t} \in \mathcal{T}}$$,
    * consistent finite-dimentional distributions

(1)

$$
    \forall n \in \mathbb{N},
    \
    \forall \tilde{t} \in \mathcal{T}^{n},
    \
    \forall A \in \mathcal{B}(\mathbb{R}^{n}),
    \
    \forall \tau \in \mathfrak{S}_{n},
    \
    Q_{\tilde{t}}(A)
    =
    Q_{\tau(\tilde{t})}(\tau(A))
    .
$$

(2) Suppose that

$$
\begin{eqnarray}
    \tilde{t}
    & := &
        (t_{1} ,\ldots, t_{n}) \in \mathcal{T}^{n}
    \nonumber
    \\
    n_{1}, n_{2} \in \mathbb{N},
    \
    n_{1} + n_{2} + 1
    & = &
        n
    \nonumber
    \\
    \tilde{s}
    & := &
        (t_{1}, \ldots, t_{n_{1}}, t_{n_{2}}, \ldots, t_{n_{1} + n_{2}}).
    \nonumber
\end{eqnarray}
$$

Then

$$
    \forall A \in \mathcal{B}(\mathbb{R}^{n_{1}}),
    \
    \forall B \in \mathcal{B}(\mathbb{R}^{n_{2}}),
    \
    Q_{\tilde{t}}(A \times \mathbb{R} \times B)
    =
    Q_{\tilde{s}}(A \times B)
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem Kolmogorov Extension Theorem
* $$\{Q_{\tilde{t}}\}_{\tilde{t} \in \mathcal{T}}$$,
    * consistensy finite dimensional distributions

#### proof

$$
    Q(C(A, \tilde{t}))
    :=
    Q_{\tilde{t}}(A)
    .
$$

Claim: $Q$ is well-defined.

Suppose that $$C(A_{1}, \tilde{t}_{1}) = C(A_{2}, \tilde{t}_{2})$$.
Let $$n_{i} := \abs{\tilde{t}_{i}}$$ and $$\tilde{t} := (\tilde{t}_{1}, \tilde{t}_{2})$$.
By proposition,

$$
\begin{eqnarray}
    C(A_{1}, \tilde{t}_{1})
    & = &
        C(A_{1} \times \mathbb{R}^{n}, \tilde{t})
    \nonumber
    \\
    C(A_{2}, \tilde{t}_{2})
    & = &
        C(\mathbb{R}^{n} \times A_{2}, \tilde{t})
    .
    \nonumber
\end{eqnarray}
$$

Hence,

$$
\begin{eqnarray}
    Q(C(A_{1} \times \mathbb{R}^{n}, \tilde{t}))
    & = &
        Q_{\tilde{t}}(A_{1} \times \mathbb{R}^{n})
    \nonumber
    \\
    & = &
        Q_{\tilde{t}_{1}}(A_{1})
    \nonumber
    \\
    & = &
        Q(C(A_{1}, \tilde{t}_{1}))
    \nonumber
    \\
    Q(C(\mathbb{R}^{n} \times A_{2}, \tilde{t}))
    & = &
        Q_{\tilde{t}}(\mathbb{R}^{n} \times A_{2})
    \nonumber
    \\
    & = &
        Q_{\tilde{t}_{2}}(A_{2})
    \nonumber
    \\
    & = &
        Q(C(A_{2}, \tilde{t}_{2}))
    .
    \nonumber
\end{eqnarray}
$$

On the other hand,

$$
\begin{eqnarray}
    Q_{\tilde{t}}(A_{1} \times \mathbb{R}^{n_{2}})
    -
    Q_{\tilde{t}}(\mathbb{R}^{n_{1}} \times A_{2})
    & = &
        Q_{\tilde{t}}(A_{1} \times \mathbb{R}^{n_{2}} \setminus \mathbb{R}^{n_{1}} \times A_{2})
    \nonumber
    \\
    & = &
        Q_{\tilde{t}}
        (
            A_{1} \times \mathbb{R}^{n_{2}}
            \cap
            \left(
                \mathbb{R}^{n_{1}} \times A_{2}
            \right)^{c}
        )
    \nonumber
    \\
    & = &
        Q_{\tilde{t}}(\emptyset)
    \nonumber
    \\
    & = &
        0
    .
    \nonumber
\end{eqnarray}
$$

Combining the above equations,

$$
\begin{eqnarray}
    Q(C(A_{1}, \tilde{t}_{1}))
    & = &
        Q(C(A_{1} \times \mathbb{R}^{n}, \tilde{t}))
    \nonumber
    \\
    & = &
        Q(C(\mathbb{R}^{n} \times A_{2}, \tilde{t}))
    \nonumber
    \\
    & = &
        Q(C(A_{2}, \tilde{t}_{2}))
    .
    \nonumber
\end{eqnarray}
$$

The claim proved.

Claim: $Q(\Omega) = 1$.

$$
    Q(C(\mathbb{R}, 0))
    =
    Q_{0}(\mathbb{R})
    =
    1
    .
$$

The claim proved.

Claim: $Q$ is finitely additive on $\mathcal{C}$.

Let $$C(A_{1}, \tilde{t}_{1}), C(A_{2}, \tilde{t}_{2}) \in \mathcal{C}$$.
Suppose that $$C(A_{1}, \tilde{t}_{1}) \cap C(A_{2}, \tilde{t}_{2}) = \emptyset$$.
By proposition, letting $$\tilde{t} := (\tilde{t}_{1}, \tilde{t}_{2})$$.

$$
\begin{eqnarray}
    C(A_{1} \times A_{2}, \tilde{t})
    =
    C(A_{1} \times \mathbb{R}^{n_{2}}, \tilde{t})
    \cap
    C(\mathbb{R}^{n_{1}} \times A_{2}, \tilde{t})
    .
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    Q_{\tilde{t}}(A_{1} \times A_{2})
    & = &
        Q_{\tilde{t}}(A_{1} \times \mathbb{R}^{n_{2}} \cap \mathbb{R}^{n_{2}} \times A_{1})
    \nonumber
    \\
    & = &
        Q_{\tilde{t}}(A_{1} \times \mathbb{R}^{n_{2}})
        +
        Q_{\tilde{t}}(\mathbb{R}^{n_{2}} \times A_{1})
    \nonumber
    \\
    & = &
        Q_{\tilde{t}_{1}}(A_{1})
        +
        Q_{\tilde{t}_{2}}(A_{2})
    \nonumber
\end{eqnarray}
$$

This implies additivity of $Q$.
The claim proved.


<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Kolmogorov extension theorem \- Wikipedia](https://en.wikipedia.org/wiki/Kolmogorov_extension_theorem)

