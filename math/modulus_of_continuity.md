---
title: Modulus of Continuity
---

## Modulus of Continuity


#### Definition 1
* $f \in C[0, \infty)$,

$$
\begin{eqnarray}
    m^{T}(f, \delta)
    & := &
        \sup
        \{
            \abs{
                f(x) - f(y)
            }
            \mid
            \abs{x - y}
            <
            \delta,
            x, y \in [0, T]
        \}
    \nonumber
    \\
    B(\delta)
    & := &
        \{
            (x, y)
            \in
            [0, T]^{2}
            \mid
            \abs{x - y} < \delta
        \}
    \nonumber
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 2


* (1) If $\delta_{1} \le \delta_{2}$, $$m^{T}(f, \delta_{1}) \le m^{T}(f, \delta_{2})$$,
* (2) If $$m^{T}(f, \delta_{1} + \delta_{2}) \le m^{T}(f, \delta_{1}) + m^{T}(f, \delta_{2})$$,
* (3) $f$ is uniformly continuous if and only if $\lim_{\delta \searrow 0} m^{T}(f, r) = 0$,
* (4) If $\lambda > 0$, $m^{T}(f, \lambda \delta) < (1 + \lambda) m^{T}(f, \delta)$,
* (5)

$$
\begin{eqnarray}
    \abs{
        m^{T}(f, \delta)
        -
        m^{T}(g, \delta)
    }
    & \le &
        2 \sup
        \{
            \abs{f(x) - g(x)}
            \mid
            x
            \in
            [0, T]
        \}
        =:
        2
        \norm{
            f - g
        }_{\infty, [0,T]}
    .
    \nonumber
\end{eqnarray}
$$

(6) $m^{T}(f, \delta)$ is continuous in $f \in C[0, T]$ for fixed $\delta$.

#### proof

**proof of (1)**

Since $B(\delta_{1}) \subseteq B(\delta_{2})$,

$$
\begin{eqnarray}
    \sup
    \{
        \abs{f(x) - f(y)}
        \mid
        (x, y) \in B(\delta_{1})
    \}
    \le
    \sup
    \{
        \abs{f(x) - f(y)}
        \mid
        (x, y) \in B(\delta_{2})
    \}
    \nonumber
\end{eqnarray}
$$


**proof of (3)**

(only if)

Let $\epsilon > 0$ be fixed.
Since $f$ is uniformly continuous, there exists $\delta > 0$ such that

$$
    \abs{
        x - y
    }
    < \delta
    \Rightarrow
    \abs{
        f(x)
        -
        f(y)
    }
    <
    \frac{\epsilon}{2}
    .
$$

Thus,

$$
\begin{eqnarray}
    \sup
    \{
        \abs{
            f(x) - f(y)
        }
        \mid
        \abs{
            x - y
        }
        < \delta
    \}
    & \le &
        \frac{\epsilon}{2}
    \nonumber
    \\
    & < &
        \epsilon
    \nonumber
\end{eqnarray}
$$

Since $\epsilon$ was chosen arbitrary, the proof completed.

(if)

Let $\epsilon > 0$ be fixed.
By assumption,



**proof of (4)**


**proof of (5)**

By triangle inequality,

$$
\begin{eqnarray}
    \forall x, y \in [0, T],
    \
    \abs{x - y} < \delta,
    \
    \abs{f(x) - f(y)}
    & \le &
        \abs{f(x) - g(y)}
        +
        \abs{g(y) - g(x)}
        +
        \abs{g(x) - f(y)}
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \forall x, y \in [0, T],
    \
    \abs{x - y} < \delta,
    \
    \abs{f(x) - f(y)}
    & \le &
        \abs{f(x) - g(y)}
        +
        m^{T}(g, \delta)
        +
        \abs{g(x) - f(y)}
    \nonumber
    \\
    & \le &
        \abs{f(x) - g(y)}
        +
        m^{T}(g, \delta)
        +
        \norm{
            f - g
        }_{\infty, [0, T]}
    \nonumber
    \\
    & \le &
        \norm{
            f - g
        }_{\infty, [0, T]}
        +
        m^{T}(g, \delta)
        +
        \norm{
            f - g
        }_{\infty, [0, T]}
    \nonumber
    \\
    & \le &
        2
        \norm{
            f - g
        }_{\infty, [0, T]}
        +
        m^{T}(g, \delta)
    .
    \nonumber
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    & &
        m^{T}(f, \delta)
        \le
        2
        \norm{
            f - g
        }_{\infty, [0, T]}
        +
        m^{T}(g, \delta)
    \nonumber
    \\
    & \Leftrightarrow &
        m^{T}(f, \delta)
        -
        m^{T}(g, \delta)
        \le
        2
        \norm{
            f - g
        }_{\infty, [0, T]}
\end{eqnarray}
    .
$$

Similary,

$$
\begin{eqnarray}
    & &
        m^{T}(g, \delta)
        \le
        2
        \norm{
            f - g
        }_{\infty, [0, T]}
        +
        m^{T}(f, \delta)
    \nonumber
    \\
    & \Leftrightarrow &
        m^{T}(g, \delta)
        -
        m^{T}(f, \delta)
        \le
        2
        \norm{
            f - g
        }_{\infty, [0, T]}
    .
    \nonumber
\end{eqnarray}
$$

Therefore, the proof of (5) completes.

(6)

Let $(f_{n}) \in C[0, \infty]$ be a sequence such that

$$
    \norm{
        f_{n} - f
    }_{\infty, [0, T]}
    \rightarrow
    0
    .
$$

By (5),

$$
    \abs{
        m^{T}(f_{n}, \delta)
        -
        m^{T}(f, \delta)
    }
    \le
    2
    \norm{
        f_{n} - f
    }_{\infty, [0, T]}
    \rightarrow
    0
    .
$$

Therefore, the proof (6) completes.

<div class="QED" style="text-align: right">$\Box$</div>


#### Theorem Arzela-Ascoli
* $A \subseteq C[0, \infty)$,
* $\bar{A}$,
    * closure of $A$,


The following conditions are euqivalent;

(1) $\bar{A}$ is compact

(2) 

$$
\begin{eqnarray}
    \sup_{\omega \in A}
        \abs{\omega(0)}
    & < &
        \infty
    \label{arzela_ascoli_theorem_condition_01}
    \\
    \forall T > 0,
    \
    \lim_{\delta \rightarrow 0}
    \sup_{\omega \in A}
        m^{T}(\omega, \delta) = 0
    \label{arzela_ascoli_theorem_condition_02}
\end{eqnarray}
$$

#### proof

(1) $\Rightarrow$ (2)

$$
\begin{eqnarray}
    G_{n}
    & := &
        \{
            \omega \in C[0, \infty)
            \mid
            \abs{\omega(0)}
            <
            n
        \}
    \nonumber
    \\
    \bar{A}
    & \subseteq &
        \bigcup_{n \in \mathbb{N}}
            G_{n}
    .
    \nonumber
\end{eqnarray}
$$

Since $\bar{A}$ is compact, there exists $n \in \mathbb{N}$ such that $\bar{A} \subseteq G_{n}$.
Let $\epsilon > 0$ be fixed.
Let

$$
    \delta > 0,
    \
    K_{\delta}
    :=
    \{
        \omega \in \bar{A}
        \mid
        m^{T}(\omega, \delta)
        \ge
        \epsilon
    \}
    .
$$

Since $\omega^{T}(\omega, \delta)$ is continuous in $\omega \in \Omega$, $K_{\delta}$ is closed and $$K_{\delta} \subseteq \bar{A}$$.
A closed subset of compact set is also compact.
It follows that $K_{\delta}$ is compact.
By proposition, $$\lim_{\delta \rightarrow 0} m^{T}(\omega, \delta) = 0$$.
It follows that

$$
    \bigcap_{\delta > 0}
        K_{\delta}
    =
    \emptyset
    .
$$

Thus, there exists $\delta_{\epsilon} > 0$ such that $K_{\delta_{\epsilon}} = \emptyset$.
This proves $(\Rightarrow)$ part.

(1) $\Leftarrow$ (2)

Since $C[0, \infty)$ is a metric space, we will show that every sequence $$\{\omega_{n}\}_{n=1}^{\infty} \subseteq A$$ has a convergent subsequence.
Let $$\{\omega_{n}\}_{n \in \mathbb{N}} \subseteq A$$ be fixed.
By $$\eqref{arzela_ascoli_theorem_condition_01}$$, there exists $\delta_{1} > 0$ such that

$$
    \sup_{\omega \in A}
        m^{T}(\omega, \delta_{1})
    <
    1
    .
$$

It follows that for $m \in \mathbb{N}$ and $t (0, T]$ with $(m - 1) \delta_{1} < t \le ((m \delta_{1}) \wedge T)$,

$$
\begin{eqnarray}
    \abs{\omega(t)}
    & \le &
        \abs{\omega(0)}
        +
        \sum_{k=1}^{m-1}
            \abs{
                \omega(k\delta_{1})
                -
                \omega((k - 1)\delta_{1})
            }
        +
        \abs{
            \omega(t) - \omega((m - 1) \delta_{1})
        }
    \nonumber
    \\
    & \le &
        \abs{\omega(0)}
        +
        \sum_{k=1}^{m-1}
            m^{T}(\omega, \delta_{1})
        +
        m^{T}(\omega, \delta_{1})
    \nonumber
    \\
    & \le &
        \abs{\omega(0)}
        +
        m
    \nonumber
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \forall r \in \mathbb{Q}_{\ge 0},
    \
    \omega_{n}(r)
    & \le &
        \abs{\omega_{n}(0)}
        +
        m
    & \le &
        \sup_{\omega \in A}
            \abs{\omega(0)}
        +
        m
    \nonumber
\end{eqnarray}
$$

Hence $$\{\omega_{n}(r)\}$$ is bounded for each $$r \in \mathbb{Q}_{\ge 0}$$.
Let $$\{r_{0}, r_{1}, \ldots\}$$ be an enumeration of $$\mathbb{Q}_{\ge 0}$$.
Since $$\{\omega_{n}(r_{0})\}$$ is bounded, there exists a subsequence $$\{\omega_{n}^{(0)}\}_{n \in \mathbb{N}}$$ converging to a limit denoted $$\omega(r_{0})$$.
From $$\{\omega_{n}^{(k-1)}\}$$, we recursively define a subsequence $$\{\omega_{n}^{(k)}\}$$ converging to a limit denoted $$\omega(r_{k})$$.
As a consequence of this process, we can define diagonal sequence


$$
    \{
        \bar{\omega}_{n}
    \}_{n \in \mathbb{N}}
    :=
    \{
        \omega_{n}^{(n)}
    \}_{n \in \mathbb{N}}
$$

such that

$$
    \forall r \in \mathbb{Q}_{\ge 0},
    \
    \omega_{n}(r)
    \rightarrow
    \omega(r)
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Modulus of continuity \- Wikipedia](https://en.wikipedia.org/wiki/Modulus_of_continuity)
* [real analysis \- Modulus of continuity properties and uniform continuity\. \- Mathematics Stack Exchange](https://math.stackexchange.com/questions/928260/modulus-of-continuity-properties-and-uniform-continuity)
* [853\.pdf](http://pefmath2.etf.rs/files/117/853.pdf)
