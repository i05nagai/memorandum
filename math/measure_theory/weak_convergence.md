---
title: Weak Convergence
---

## Weak Convergence

* $C_{b}(S)$,
    * the set of boubded continuous functions on $S$.

#### Definition 1 Weak convergence
* $(S, \rho)$,
    * metric space with Borel $\sigma$-algebra $\mathcal{B}(S))$,
* $$\{P_{n}\}_{n \in \mathbb{N}}$$,
    * a sequence of probability measure on $(S, \mathcal{B}(S))$,
* $P$
    * a measure on $(S, \mathcal{B}(S))$

$$\{P_{n}\}$$ is said to converge wealkly to $P$ if

$$
    \forall f \in C_{b}(S),
    \
    \lim_{n \rightarrow \infty}
        \int_{S}
            f(s)
        \ P_{n}(ds)
    =
    \int_{S}
        f(s)
    \ P(ds)
    .
$$

We write $P_{n} \overset{w}{\rightarrow} P$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 1

* $(S, \rho)$,
* $\mathcal{O}$,
    * all open sets in $S$,

(1)

If $P_{n} \overset{w}{\rightarrow} P$, $P_{n} \overset{w}{\rightarrow} P^{\prime}$, then $P = P^{\prime}$.

(2) Let $F$ be closed set.

$$
\begin{eqnarray}
    f(x)
    & := &
        (1 - \rho(x, F)/\epsilon)^{+}
\end{eqnarray}
$$

(2-1) $f$ is bounded.

(2-2) $f$ is uniformly continuous

(2-3)

$$
\begin{eqnarray}
    I_{F}(x)
    \le
    f(x)
    \le
    I_{F^{\epsilon}}(x)
    .
\end{eqnarray}
$$

#### proof

**proof of (1)**

$$
\begin{eqnarray}
    \forall O \in \mathcal{O},
    \
    P(O)
    & = &
        \int_{S}
            1_{O}(x)
        \ P(dx)
    \nonumber
    \\
    & = &
    \lim_{n \rightarrow \infty}
        \int_{S}
            1_{O}(x)
        \ P_{n}(dx)
    \nonumber
    \\
    & = &
        \int_{S}
            1_{O}(x)
        \ P^{\prime}(dx)
    \nonumber
    \\
    & = &
        P^{\prime}(O)
    \nonumber
\end{eqnarray}
$$

**proof of (2)**

Since $0 \le f_{\epsilon} \le 1$, (2-1) holds.

As to (2-2), 

$$
\begin{eqnarray}
    \abs{
        f_{\epsilon}(x) - f_{\epsilon}(x)
    }
    \le
\end{eqnarray}
$$



<div class="QED" style="text-align: right">$\Box$</div>

#### Definition 3

* $(S, \rho)$,
    * metric space
* $$\{(\Omega_{n}, \mathcal{F}_{n}, P_{n})\}_{n \in \mathbb{N}}$$,
    * a sequence of probability spaces
* $X_{n}: \Omega \rightarrow S$,
    * random variable over $$(\Omega_{n}, \mathcal{F}_{n}, P_{n})$$,
* $(\Omega, \mathcal{F}, P)$,
    * probability space
    * random variable on $$(\Omega_{n}, \mathcal{F}_{n}, P_{n})$$,
* $X: \Omega \rightarrow S$,
    * random variable over $(\Omega, \mathcal{F}, P)$,

$$\{X_{n}\}$$ is said to converge to $X$ in distribution if

$$
\begin{eqnarray}
    & &
        P_{n}X_{n}^{-1}
        \overset{w}{\rightarrow}
        PX^{-1}
    \nonumber
    \\
    & \Leftrightarrow &
        \forall f \in C_{b}(S),
        \
        \lim_{n \rightarrow \infty}
            \int_{S}
                f(s)
            \ (P_{n}X_{n}^{-1})(ds)
        =
        \int_{S}
            f(s)
        \ (PX^{-1})(ds)
        .
\end{eqnarray}
    .
$$

We write $X_{n} \overset{d}{\rightarrow} X$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 4

(1)

$X_{n} \overset{d}{\rightarrow} X$ if and only if

$$
    \forall f \in C_{b}(S),
    \
    \lim_{n \rightarrow \infty}
        \int_{S_{n}}
            f(X_{n}(\omega))
        \ P_{n}(d \omega)
    =
    \int_{S}
        f(X(\omega))
    \ P(d \omega)
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Definition 5
* $(S, \rho)$,
    * metric space
* $A \in \mathcal{B}(S)$

$A$ is said to be $P$-continuity set if

$$
    P(\partial A)
    =
    0
$$

where $\partial A$ is boundary of $A$.
Note that $\partial A$ is closed.

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 6 The Portmanteau Theorem
* $(S, \rho)$,
    * metric space
* $\mathcal{O}$,
    * all open sets
* $\mathcal{F}$,
    * all closed sets

These five conditions are equivalent:

* (i) $P_{n} \overset{w}{\rightarrow} P$,
* (ii) $P_{n} f \rightarrow Pf$ for all bounded, uniformly continuous $f$,
* (iii) $\lim\sup_{n} P_{n}F \le PF$ for all $F \in \mathcal{F}$
* (iv) $\lim\inf_{n} P_{n}G \ge PG$ for all $G \in \mathcal{O}$
* (v) $P_{n}A \rightarrow PA$ for all $P$ continuity sets $A$
 
#### proof

(i) $\Rightarrow$ (ii)

(ii) $\Rightarrow$ (iii)

(iii) $\Leftrightarrow$ (iv)


(iii) $\Rightarrow$ (v)


(v) $\Rightarrow$ (i)

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 7
* $(\Omega, \mathcal{F}, P)$,
* $X:\Omega \rightarrow C[0, \infty)$,
    * $\mathcal{F}/\mathcal{B}(C[0, \infty))$-measurable
* $$(\Omega_{n}, \mathcal{F}_{n}, P_{n})$$,
    * probability spaces
* $X^{n}:\Omega_{n} \rightarrow C[0, \infty)$,
    * $\mathcal{F}_{n}/\mathcal{B}(C[0, \infty))$-measurable

If

$$
    X^{n} \overset{d}{\rightarrow} X,
$$

then for all $\tilde{t} := (t_{1}, \ldots, t_{d}) \in \mathcal{T}$,

$$
    (X_{t_{1}}^{n}, \ldots, X_{t_{d}}^{n})
    \overset{d}{\rightarrow}
    (X_{t_{1}}, \ldots, X_{t_{d}})
    .
$$

#### proof
Let us define $\pi_{\tilde{t}}: C[0, \infty) \rightarrow \mathbb{R}^{d}$ as

$$
    \pi_{\tilde{t}}(X(\omega))
    :=
    X_{\tilde{t}}(\omega)
    =
    (X_{t_{1}}(\omega), \ldots, X_{t_{d}}(\omega))
    .
$$

Note that $\pi_{\tilde{t}}$ is $\mathcal{B}(C[0, \infty))/\mathcal{B}(\mathbb{R}^{d})$ measurable.
Let $f \in C_{b}(\mathbb{R}^{d})$ be fixed.
$f \circ \pi_{\tilde{t}}$ is bounded function from $C[0, \infty)$ to $\mathbb{R}^{d}$.

$$
\begin{eqnarray}
    \lim_{n \rightarrow \infty}
        \int_{\Omega^{n}}
            f(X_{\tilde{t}}^{n}(\omega))
        \ P_{n}(d \omega)
    & = &
        \lim_{n \rightarrow \infty}
            \int_{\Omega^{n}}
                f(\pi_{\tilde{t}}(X^{n}(\omega)))
            \ P_{n}(d \omega)
    \nonumber
    \\
    & = &
        \lim_{n \rightarrow \infty}
            \int_{\Omega^{n}}
                (f \circ \pi_{\tilde{t}})(X^{n}(\omega)))
            \ P_{n}(d \omega)
    \nonumber
    \\
    & = &
        \int_{\Omega}
            (f \circ \pi_{\tilde{t}})(X(\omega)))
        \ P(d \omega)
    \nonumber
    \\
    & = &
        \int_{\Omega}
            f(X_{\tilde{t}}(\omega))
        \ P(d \omega)
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem
* $(\Omega, \mathcal{F}, P)$,
* $$\{X^{n}\}_{n \in \mathbb{N}}$$,
    * $X^{n}:\Omega_{n} \rightarrow C[0, \infty)$,
    * $$\mathcal{F}_{n}/\mathcal{B}(C[0, \infty))$$-measurable
    * tight sequence

$$
    \tilde{t} \in \mathcal{T},
    \
    (X_{d_{1}}^{n}, \ldots, X_{t_{d}}^{n})
    \overset{D}{\rightarrow}
    (X_{d_{1}}, \ldots, X_{t_{d}})
    .
$$

If

$$
    X^{n} \overset{d}{\rightarrow} X,
$$

then for all $\tilde{t} := (t_{1}, \ldots, t_{d}) \in \mathcal{T}$,

$$
    (X_{t_{1}}^{n}, \ldots, X_{t_{d}}^{n})
    \overset{d}{\rightarrow}
    (X_{t_{1}}, \ldots, X_{t_{d}})
    .
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem
* $(\Omega, \mathcal{F}, P)$,
* $$\{X^{n}\}_{n \in \mathbb{N}}$$,
    * $X^{n}:\Omega_{n} \rightarrow C[0, \infty)$,
    * $\mathcal{F}_{n}/\mathcal{B}(C[0, \infty))$-measurable
    * tight sequence

$$
    \forall \tilde{t} \in \mathcal{T},
    \
    X_{\tilde{t}}^{n}
    \rightarrow
    X_{\tilde{t}}
    .
$$

Let

$$
\begin{eqnarray}
    P^{n}
    & := &
        P \circ (X^{n})^{-1}: \mathcal{B}(C[0, \infty)) \rightarrow [0, 1]
    \nonumber
    \\
    W_{t}(\omega)
    & := &
        \omega(t)
    \nonumber
\end{eqnarray}
    .
$$

Then there exists measure $P$ on $$(C[0, \infty), \mathcal{B}(C[0, \infty)))$$ such that

$$
    \tilde{t} \in \mathcal{T},
    \
    X_{\tilde{t}}^{n}
    \rightarrow
    W_{\tilde{t}}
    .
$$

#### proof
By definition of tightness, every subsequence of tight sequence is also tight.
Let $\bar{P} := P \circ X^{-1}$.
By Prohorov theorme, $$\{P_{n}\}$$ contains a weakly convergent subsequence.
every subsequence of $$\{P^{n}\}$$ converges weakly to a probability measure $\bar{P}$.

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
