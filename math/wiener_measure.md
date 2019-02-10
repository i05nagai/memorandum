---
title: Wiener Measure
---

## Wiener Measure

#### Lemma 1
* $\Omega_{n} := C_{0}([0, n])$,
    * continuous funcitons
* $$(\omega_{k})_{k \in \mathbb{N}}$$,
    * $\omega_{k} \in \Omega_{n}$,

Suppose

$$
    \max_{t \in [0, n]}
    \left(
        \abs{
            \omega_{k}(t)
            -
            \omega_{m}(t)
        }
    \right)
    \rightarrow
    0
    \quad
    (k, m \rightarrow \infty)
    .
$$

Then

$$
\begin{equation}
    \exists \omega \in \Omega_{n},
    \text{ s.t. }
    \max_{t \in [0, n]}
    \left(
        \abs{
            \omega_{k}(t)
            -
            \omega(t)
        }
    \right)
    \rightarrow
    0
    \
    (k \rightarrow \infty)
    \label{lemma_01_existence}
\end{equation}
    .
$$

In other words, continuous functions is complete metric space with sup norm.

Moreover, if

$$
\begin{eqnarray}
    \max_{t \in [0, n]}
    \left(
        \omega_{k}(t)
        -
        \omega(t)
    \right)
    & \rightarrow &
        0
    \nonumber
    \\
    \max_{t \in [0, n]}
    \left(
        \omega_{k}(t)
        -
        \omega^{\prime}(t)
    \right)
    & \rightarrow &
        0,
    \nonumber
\end{eqnarray}
$$

then $\omega = \omega^{\prime}$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 2
* $\Omega := C_{0}([0, \infty))$,
    * continuous funcitons

$$
\begin{eqnarray}
    \omega_{1}, \omega_{2} \in \Omega,
    \
    \rho(\omega_{1}, \omega_{2})
    :=
    \sum_{n \in \mathbb{N}}
        \frac{1}{2^{n}}
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{1}(t)
                -
                \omega_{2}(t)
            }
            \wedge
            1
        \right)
    \label{wiener_measure_def_metric}
\end{eqnarray}
$$

(1) $\rho$ is a metric on $\Omega$.

(2) $(\Omega, \rho)$ is a separable

(3) $(\Omega, \rho)$ is a complete


#### proof
proof of (1)

We will show

* (1-1) $\rho(\omega_{1}, \omega_{2}) \ge 0$,
* (1-2) $\rho(\omega_{1}, \omega_{2}) = \rho(\omega_{2}, \omega_{1})$,
* (1-3) $\rho(\omega_{1}, \omega_{2}) = 0 \Leftrightarrow \omega_{2} = \omega_{1}$,
* (1-4) $\rho(\omega_{1}, \omega_{2}) \le \rho(\omega_{1}, \omega_{3}) + \rho(\omega_{3}, \omega_{2})$.

(1-1) and (1-2) is obvious because of properties of modulus.
Regarding (1-3),

$$
\begin{eqnarray}
    & &
        \rho(\omega_{1}, \omega_{2}) = 0
    \nonumber
    \\
    & \Leftrightarrow &
        \forall n \in \mathbb{N},
        \
        \forall t \in [0, n],
        \
        \frac{1}{2^{n}}
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{1}(t)
                -
                \omega_{2}(t)
            }
            \wedge
            1
        \right)
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \forall n \in \mathbb{N},
        \
        \forall t \in [0, n],
        \
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{1}(t)
                -
                \omega_{2}(t)
            }
        \right)
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \forall n \in \mathbb{N},
        \
        \forall t \in [0, n],
        \
        \abs{
            \omega_{1}(t)
            -
            \omega_{2}(t)
        }
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \forall n \in \mathbb{N},
        \
        \forall t \in [0, n],
        \
        \omega_{1}(t)
        =
        \omega_{2}(t)
    \nonumber
    \\
    & \Leftrightarrow &
        \forall t \in [0, \infty),
        \
        \omega_{1}(t)
        =
        \omega_{2}(t)
    .
    \nonumber
\end{eqnarray}
$$

Lastly, we will show (1-4).
It is easy to show the following inequality in both cases:

* $$\abs{\omega_{1}(t) - \omega_{3}} + \abs{\omega_{2}(t) - \omega_{3}} \le 1$$,
* $$\abs{\omega_{1}(t) - \omega_{3}} + \abs{\omega_{2}(t) - \omega_{3}} > 1$$.

$$
\begin{eqnarray}
    & &
        \forall n \in \mathbb{N},
        \
        \max_{t \in [0, n]}
        \left(
            \left(
                \abs{
                    \omega_{1}(t)
                    -
                    \omega_{3}(t)
                }
                +
                \abs{
                    \omega_{2}(t)
                    -
                    \omega_{3}(t)
                }
            \right)
            \wedge
            1
        \right)
    \nonumber
    \\
    & \le &
        \forall n \in \mathbb{N},
        \
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{1}(t)
                -
                \omega_{3}(t)
            }
            \wedge
            1
        \right)
        +
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{2}(t)
                -
                \omega_{3}(t)
            }
            \wedge
            1
        \right)
    .
    \nonumber
\end{eqnarray}
$$

Since $\rho$ always converge absolutely, we have

$$
\begin{eqnarray}
    & &
        \rho(\omega_{1}, \omega_{2})
    \nonumber
    \\
    & \le &
        \sum_{n \in \mathbb{N}}
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \left(
                    \abs{
                        \omega_{1}(t)
                        -
                        \omega_{3}(t)
                    }
                    +
                    \abs{
                        \omega_{3}(t)
                        -
                        \omega_{2}(t)
                    }
                \right)
                \wedge
                1
            \right)
    \nonumber
    \\
    & \le &
        \sum_{n \in \mathbb{N}}
        \left(
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    \omega_{1}(t)
                    -
                    \omega_{3}(t)
                }
                \wedge
                1
            \right)
            +
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    \omega_{3}(t)
                    -
                    \omega_{2}(t)
                }
                \wedge
                1
            \right)
        \right)
    \nonumber
    \\
    & = &
        \rho(\omega_{1}, \omega_{3})
        +
        \rho(\omega_{3}, \omega_{2})
    .
    \nonumber
\end{eqnarray}
$$

**proof of (2)**

By <a href="{{ site.baseurl }}/math/stone_weierstrass_theorem.html#corollary-2">the Weierstrass approximation theorem</a>, $C([0, n])$ is separable for all $n \in \mathbb{N}$.

Let $\mathcal{P}_{n}$ be the set of countable polynomial functions which is dense in $C([0, n])$.
Since polynomials can be defined over $\mathbb{R}$, we extend the domain of the polynomials to $C([0, \infty))$.
Let

$$
    \mathcal{P}
    :=
    \bigcup_{n \in \mathbb{N}}
        \mathcal{P}_{n}
    .
$$

$\mathcal{P}$ is countable.
Let $B(\omega^{\prime}, r)$ be open ball in $(\Omega, \rho)$.
That is,

$$
    r > 0,
    \
    \omega^{\prime} \in \Omega,
    \
    B(\omega^{\prime}, r)
    :=
    \{
        \omega
        \mid
        \rho(\omega, \omega^{\prime})
        <
        r
    \}
    .
$$

Taking $n_{0} \in \mathbb{N}$ and $\epsilon > 0$ such that

$$
    \frac{1}{2^{n_{0}-1}}
    <
    \epsilon
    <
    r
    .
$$

By the Weierstrass approximation theorem, there exists $p \in \mathcal{P}$ such that

$$
    \frac{1}{2^{n_{0}}}
    \max_{t \in [0, n_{0}]}
        \abs{
            p(t)
            -
            \omega^{\prime}(t)
        }
    <
    \frac{\epsilon}{2}
    \frac{\epsilon}{2^{n_{0}}}
    .
$$

Note that

$$
\begin{eqnarray}
    \forall n \in [1:n_{0}],
    \
    \frac{1}{2^{n}}
        \left(
            \max_{t \in [0, n]}
                \abs{
                    p(t)
                    -
                    \omega^{\prime}(t)
                }
            \wedge
            1
        \right)
    & \le &
        \frac{1}{2^{n}}
        \max_{t \in [0, n_{0}]}
        \left(
            \abs{
                p(t)
                -
                \omega^{\prime}(t)
            }
            \wedge
            1
        \right)
    \nonumber
    \\
    & = &
        2^{n_{0}-n}
        \frac{1}{2^{n_{0}}}
        \max_{t \in [0, n_{0}]}
        \left(
            \abs{
                p(t)
                -
                \omega^{\prime}(t)
            }
            \wedge
            1
        \right)
    \nonumber
    \\
    & < &
        2^{n_{0}-n}
        \frac{\epsilon}{2}
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & = &
        \frac{\epsilon}{2}
        \frac{1}{2^{n}}
    .
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \sum_{n \in \mathbb{N}}
        \frac{1}{2^{n}}
        \max_{t \in [0, n]}
        \left(
            \abs{
                p(t)
                -
                \omega^{\prime}(t)
            }
            \wedge
            1
        \right)
    & = &
        \sum_{n = 1}^{n_{0}}
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    p(t)
                    -
                    \omega^{\prime}(t)
                }
                \wedge
                1
            \right)
        +
        \sum_{n = n_{0} + 1}^{\infty}
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    p(t)
                    -
                    \omega^{\prime}(t)
                }
                \wedge
                1
            \right)
    \nonumber
    \\
    & \le &
        \sum_{n = 1}^{n_{0}}
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    p(t)
                    -
                    \omega^{\prime}(t)
                }
                \wedge
                1
            \right)
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & \le &
        \sum_{n = 1}^{n_{0}}
            \frac{\epsilon}{2}
            \frac{1}{2^{n}}
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & = &
        \frac{\epsilon}{2}
        \frac{
            \frac{1}{2}
            \left(
                1
                -
                \frac{1}{2^{n_{0}}}
            \right)
        }{
            1
            -
            \frac{1}{2}
        }
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & = &
        \frac{\epsilon}{2}
        \left(
            1
            -
            \frac{1}{2^{n_{0}}}
        \right)
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & \le &
        \frac{\epsilon}{2}
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & < &
        \frac{\epsilon}{2}
        +
        \frac{\epsilon}{2}
    \nonumber
    \\
    & = &
        \epsilon
    \nonumber
    \\
    & < &
        r
    \nonumber
\end{eqnarray}
$$

Thus, $p \in B(\omega^{\prime}, r)$.
Therefore, the proof completed.

**proof of (3)**

Supopse that $$(\omega_{k})_{k \in \mathbb{N}} \subseteq \Omega$$ and

$$
    \rho(\omega_{k}, \omega_{m}) \rightarrow 0
    \quad
    (k, m \rightarrow \infty)
    .
$$

we will show

$$
    \exists \omega \in \Omega,
    \
    \text{ s.t. }
    \rho(\omega_{k}, \omega) \rightarrow 0
    \quad
    (k \rightarrow \infty)
    .
$$

From our assumption, we claim

$$
\begin{equation}
    \forall n \in \mathbb{N},
    \
    \max_{t \in [0, n]}
    \left(
        \abs{
            \omega_{m}(t)
            -
            \omega_{k}(t)
        }
    \right)
    \rightarrow
    0
    \quad
    (k, m \rightarrow \infty)
    \label{proposition_02_cauchy_sequence_01}
    .
\end{equation}
$$

Indeed, Let $\epsilon \in (0, 1)$  and $n \in \mathbb{N}$ be fixed.
there exsits $n_{0} \in \mathbb{N}$ such that

$$
    \forall m, k \ge n_{0},
    \
    \rho(\omega_{m}, \omega_{k})
    =
    \sum_{l \in \mathbb{N}}
        \frac{1}{2^{l}}
        \max_{t \in [0, l]}
        \left(
            \abs{
                \omega_{k}(t)
                -
                \omega_{m}(t)
            }
            \wedge
            1
        \right)
    <
    \frac{\epsilon}{2^{n}}
    .
$$

Thus,

$$
\begin{eqnarray}
    & &
        \forall m, k \ge n_{0},
        \
        \frac{1}{2^{n}}
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{k}(t)
                -
                \omega_{m}(t)
            }
            \wedge
            1
        \right)
        <
        \frac{\epsilon}{2^{n}}
    \nonumber
    \\
    & \Leftrightarrow &
        \forall m, k \ge n_{0},
        \
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{k}(t)
                -
                \omega_{m}(t)
            }
            \wedge
            1
        \right)
        <
        \epsilon
    \nonumber
    \\
    & \Leftrightarrow &
        \forall m, k \ge n_{0},
        \
        \max_{t \in [0, n]}
        \abs{
            \omega_{k}(t)
            -
            \omega_{m}(t)
        }
        <
        \epsilon
        \quad
        (\because \epsilon < 1)
\end{eqnarray}
$$

Since $\epsilon$ is arbitrary, our claim proved.

Let $n^{\prime} \in \mathbb{N}$ be fixed.
Define $$\omega^{n^{\prime}} := \omega_{\restriction_{[0, n^{\prime}]}}$$ and $$\omega_{k}^{n^{\prime}} := \omega_{k \restriction_{[0, n^{\prime}]}}$$.
By $$\eqref{proposition_02_cauchy_sequence_01}$$,

$$
\begin{eqnarray}
    \max_{t \in [0, n^{\prime}]}
    \left(
        \abs{
            \omega_{m}^{n^{\prime}}(t)
            -
            \omega_{k}^{n^{\prime}}(t)
        }
    \right)
    \rightarrow
    0
    \quad
    (k, m \rightarrow \infty)
    .
\end{eqnarray}
$$

By $$\eqref{lemma_01_existence}$$, there exists contunous function $\omega^{n^{\prime}}$ on $[0, n^{\prime}]$ such that

$$
\begin{eqnarray}
    \max_{t \in [0, n^{\prime}]}
    \left(
        \abs{
            \omega_{k}^{n^{\prime}}(t)
            -
            \omega^{n^{\prime}}(t)
        }
    \right)
    \rightarrow
    0
    \quad
    (k \rightarrow \infty)
    \nonumber
    .
\end{eqnarray}
$$

Since $n^{\prime}$ is arbitrary, we obtain the sequence $$(\omega^{n})_{n \in \mathbb{N}}$$ of continuous functions.
It is easy to confirm that for all $n > m$,

$$
\begin{eqnarray}
    \max_{t \in [0, m]}
    \left(
        \abs{
            \omega_{k}^{m}(t)
            -
            \omega^{n}(t)
        }
    \right)
    & = &
        \max_{t \in [0, m]}
        \left(
            \abs{
                \omega_{k}^{n}(t)
                -
                \omega^{n}(t)
            }
        \right)
    \nonumber
    \\
    & \le &
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega_{k}^{n}(t)
                -
                \omega^{n}(t)
            }
        \right)
        \rightarrow
        0
        \quad
        (k \rightarrow \infty)
    \nonumber
\end{eqnarray}
$$

By lemma 1,

$$
\begin{equation}
    \forall t \in [0, m],
    \
    \omega^{m}(t)
    =
    \omega^{n}(t)
    \label{proposition_02_uniqueness}
\end{equation}
    .
$$

Now we can define

$$
    \omega(t)
    :=
    \sum_{n \in \mathbb{N}}
        1_{[n-1, n)}(t)
        \omega^{n}(t)
    .
$$

From $$\eqref{proposition_02_uniqueness}$$, $\omega$ is well defined.
Moreover, $\omega \in \Omega$.
To see this, if $t \in \mathbb{N}$, $\omega$ is left-continuous and right continuous.
Continuity at point $t \notin \mathbb{N}$ is obvious from continuity of $\omega^{\lceil t \rceil}$,
Thus, $\omega \in \Omega$.

Finally, we will show

$$
    \rho(\omega, \omega_{k})
    \rightarrow
    0
    .
$$

Let $\epsilon \in (0, 1)$ be fixed.
There exists $n_{0} \in \mathbb{N}$ such that

$$
    \frac{1}{2^{n_{0} - 1}}
    <
    \epsilon
    .
$$

Since the definition of $\omega$ and $$\eqref{proposition_02_uniqueness}$$, 

$$
\begin{eqnarray}
    \max_{t \in [0, n_{1}]}
    \abs{
        \omega(t)
        -
        \omega_{n}(t)
    }
    =
    \max_{t \in [0, n_{1}]}
    \abs{
        \omega^{n_{1}}(t)
        -
        \omega_{n}(t)
    }
    \nonumber
\end{eqnarray}
$$

Thus, for all $n_{1} \in [1:n_{0}]$, there exists $n_{2, n_{1}} \in \mathbb{N}$ such that

$$
\begin{eqnarray}
    \forall n \ge n_{2, n_{1}},
    \
    \frac{1}{2^{n_{1}}}
    \max_{t \in [0, n_{1}]}
    \left(
        \abs{
            \omega(t)
            -
            \omega_{n}(t)
        }
        \wedge
        1
    \right)
    <
    \frac{\epsilon}{2}
    \frac{1}{2^{n_{1}}}
    .
    \nonumber
\end{eqnarray}
$$

Now, we define $n_{3} := \max_{n_{1} \in [1:n_{0}]} n_{2, n_{1}}$.
We have

$$
\begin{eqnarray}
    \forall n \ge n_{3},
    \
    \forall n_{1} \in [1:n_{0}],
    \
    \frac{1}{2^{n_{1}}}
    \max_{t \in [0, n_{1}]}
    \left(
        \abs{
            \omega(t)
            -
            \omega_{n}(t)
        }
        \wedge
        1
    \right)
    <
    \frac{\epsilon}{2}
    \frac{1}{2^{n_{1}}}
    .
    \nonumber
\end{eqnarray}
$$

Thus, for all $k \ge n_{3}$,

$$
\begin{eqnarray}
    \sum_{n \in \mathbb{N}}
        \frac{1}{2^{n}}
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega(t)
                -
                \omega_{k}(t)
            }
            \wedge
            1
        \right)
    & = &
        \sum_{n = 1}^{n_{0}}
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    \omega(t)
                    -
                    \omega_{k}(t)
                }
                \wedge
                1
            \right)
        +
        \sum_{n = n_{0} + 1}^{\infty}
        \frac{1}{2^{n}}
        \max_{t \in [0, n]}
        \left(
            \abs{
                \omega(t)
                -
                \omega_{k}(t)
            }
            \wedge
            1
        \right)
    \nonumber
    \\
    & \le &
        \sum_{n = 1}^{n_{0}}
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    \omega(t)
                    -
                    \omega_{k}(t)
                }
                \wedge
                1
            \right)
        +
        \sum_{n = n_{0} + 1}^{\infty}
            \frac{1}{2^{n}}
    \nonumber
    \\
    & \le &
        \sum_{n = 1}^{n_{0}}
            \frac{1}{2^{n}}
            \max_{t \in [0, n]}
            \left(
                \abs{
                    \omega(t)
                    -
                    \omega_{k}(t)
                }
                \wedge
                1
            \right)
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & < &
        \frac{\epsilon}{2}
        \sum_{n = 1}^{n_{0}}
            \frac{\epsilon}{2^{n}}
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & = &
        \frac{\epsilon}{2}
        \sum_{n = 1}^{n_{0}}
            \frac{1}{2^{n}}
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & = &
        \frac{\epsilon}{2}
        \frac{
            \frac{1}{2}
            \left(
                1
                -
                \frac{1}{2^{n_{0}}}
            \right)
        }{
            1
            -
            \frac{1}{2}
        }
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & = &
        \frac{\epsilon}{2}
        \left(
            1
            -
            \frac{1}{2^{n_{0}}}
        \right)
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & \le &
        \frac{\epsilon}{2}
        +
        \frac{1}{2^{n_{0}}}
    \nonumber
    \\
    & \le &
        \frac{\epsilon}{2}
        +
        \frac{\epsilon}{2}
    \nonumber
    \\
    & = &
        \epsilon
    \nonumber
    .
\end{eqnarray}
$$

Proof of (3) completes.

<div class="QED" style="text-align: right">$\Box$</div>

#### Definition 3

$$
\begin{eqnarray}
    \mathcal{T}_{s}
    & := &
        \{
            \tilde{t} := (t_{1}, \ldots, t_{n})
            \mid
            t_{i} \in [0, s],
            \
            t_{i} \neq t_{j},
            \
            n \in \mathbb{N}
        \}
    \nonumber
    \\
    \mathcal{T}
    & := &
        \{
            \tilde{t} := (t_{1}, \ldots, t_{n})
            \mid
            t_{i} \in [0, \infty),
            \
            t_{i} \neq t_{j},
            \
            n \in \mathbb{N}
        \}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \tilde{t} \in \mathcal{T},
    \
    C(A, \tilde{t})
    & := &
        \{
            \omega \in \Omega
            \mid
            \omega(\tilde{t}) \in A
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
            \tilde{t} \in \mathcal{T}^{n},
            \
            A \in \mathcal{B}(\mathbb{R}^{n})
        \}
    \nonumber
    \\
    \mathcal{G}
    & := &
        \sigma(\mathcal{C})
    \nonumber
    \\
    \tilde{t} \in \mathcal{T}_{s},
    \
    C_{s}(A, \tilde{t})
    & := &
        \{
            \omega \in \Omega
            \mid
            \omega(\tilde{t}) \in A
        \},
    \nonumber
    \\
    \mathcal{C}_{s}
    & := &
        \{
            C_{s}(A, \tilde{t})
            \mid
            n \in \mathbb{N},
            \
            \tilde{t} \in \mathcal{T}^{n},
            \
            A \in \mathcal{B}(\mathbb{R}^{n})
        \}
    \nonumber
    \\
    \mathcal{G}_{s}
    & := &
        \sigma(\mathcal{C}_{s})
    \nonumber
    \\
    B(\omega^{\prime}, r)
    & := &
        \{
            \omega
            \mid
            \rho(\omega, \omega^{\prime})
            <
            r
        \}
        .
    \nonumber
    \\
    \mathcal{O}
    & := &
        \{
            B(\omega, r)
            \mid
            \omega \in \Omega,
            \
            r > 0
        \}
    \nonumber
    \\
    \mathcal{B}(\Omega)
    & := &
        \sigma(\mathcal{O})
    \nonumber
        .
\end{eqnarray}
$$

$\phi_{t}: C[0, \infty) \rightarrow C[0, \infty)$ is the mamping

$$
    (\phi_{t}\omega)(s)
    :=
    \omega(t \wedge s)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark

$$
\begin{eqnarray}
    \mathcal{B}(\mathbb{R}^{n})
    & = &
        \sigma
        \left(
            \{
                A_{1} \times \cdots \times A_{n}
                \mid
                A_{i} \mathcal{B}(\mathbb{R})
            \}
        \right)
    \nonumber
    \\
    & = &
        \sigma
        \left(
            \{
                (a_{1}, b_{1}) \times \cdots \times (a_{n}, b_{n})
                \mid
                a_{i} < b_{i}
            \}
        \right)
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 4
(1)

$$
    \mathcal{G}
    =
    \mathcal{B}(\Omega)
    .
$$

(2)

$$
    \mathcal{G}_{t}
    =
    \phi_{t}^{-1}(\mathcal{B}(\Omega))
    .
$$

#### proof

**proof of (1)**

We claim that $\mathcal{C} \subseteq \sigma(\mathcal{O})$.

Let $C(\tilde{t}, A) \in \mathcal{C}$ where $\tilde{t} \in \mathcal{T}^{n}$ and $A \in \mathcal{B}(\mathbb{R}^{n})$ be fixed.

$$
\begin{eqnarray}
    \bigcup_{i \in \mathbb{N}}
        C(\tilde{t}, A_{i})
    & = &
        C
        \left(
            \tilde{t},
            \bigcup_{i \in \mathbb{N}}
                A_{i}
        \right)
    \nonumber
    \\
    \bigcap_{i \in \mathbb{N}}
        C(\tilde{t}, A_{i})
    & = &
        C
        \left(
            \tilde{t},
            \bigcap_{i \in \mathbb{N}}
                A_{i}
        \right)
    \nonumber
\end{eqnarray}
    .
$$

Let $$(\pi_{\tilde{t}})^{-1}(A) \in \mathcal{C}_{T}$$ be fixed.

$$

$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
