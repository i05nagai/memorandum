---
title: Online Convex Optimization with Stochastic Constraints
---

## Online Convex Optimization with Stochastic Constraints


* $\mathcal{F}$,
    * loss functions
* $\mathcal{G}$,
    * constraint functions

#### Basic Assumptions
(1) Bounded gradient of loss functions;

$$
    \forall f \in \mathcal{F},
    \
    \exists D_{1} > 0,
    \text{ s.t. }
    \forall x \in \mathcal{X}_{0},
    \
    \norm{
        \nabla f(x)
    }
    \le
    D_{1}
    .
$$

(2) Bounded gradient of constraint functions;

$$
    \forall g \in \mathcal{G},
    \
    \exists D_{2} > 0,
    \text{ s.t. }
    \forall x \in \mathcal{X}_{0},
    \
    \omega \in \Omega,
    \
    \norm{
        \nabla g(x; \omega)
    }
    \le
    D_{2}
    .
$$

(3) Bounded constraint functions

$$
    \forall g \in \mathcal{G},
    \
    \exists G > 0
    \text{ s.t. }
    \forall x \in \mathcal{X}_{0},
    \
    \forall \omega \in \Omega,
    \
    \norm{g(x; \omega)}
    \le
    G
    .
$$

(4)

$$
    \exists R > 0
    \text{ s.t. }
    \forall x, y \in \mathcal{X}_{0},
    \
    \norm{x - y}
    \le
    R
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Assumption The slater condition

$$
    \exists \epsilon > 0,
    \
    x \in \mathcal{X}_{0}
    \text{ s.t. }
    g(x)
    :=
    \mathrm{E}
    \left[
        g(x; \cdot)
    \right]
    \le
    -\epsilon
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

* $m \in \mathbb{N}$
    * the number of constraints
* $\mathcal{X}_{0}$,
    * convex set

#### Algorithm 1
* $V, \alpha > 0$,
* $x^{1} \in \mathcal{X}_{0}$,
* $Q_{k}^{1} := 0 \ (k = [1:m])$,

$$
\begin{eqnarray}
    x^{t + 1}
    :=
    \arg\min_{x \in \mathcal{X}_{0}}
    \left(
        V
        \left(
            \nabla f^{t}(x^{t})
        \right)^{\mathrm{T}}
        \left(
            x - x^{t}
        \right)
        +
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \left(
                \nabla g_{k}^{t}(x^{t})
            \right)^{\mathrm{T}}
            \left(
                x - x_{t}
            \right)
            +
            \alpha
            \norm{
                x - x^{t}
            }^{2}
    \right)
    \label{equation_02}
\end{eqnarray}
    .
$$

$$
\begin{eqnarray}
    Q_{k}^{t + 1}
    :=
    \max
    \left(
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        +
        \left(
            \nabla g_{k}^{t}(x^{t})
        \right)^{\mathrm{T}}
        \left(
            x^{t + 1} - x^{t}
        \right),
        0
    \right)
    \label{equation_03}
\end{eqnarray}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Lemma 1
* $x^{t + 1}$,

$$
\begin{eqnarray}
    x^{t + 1}
    & = &
        \mathcal{P}_{\mathcal{X}_{0}}
        \left(
            x^{t}
            -
            \frac{1}{2 \alpha}
            d^{t}
        \right)
\end{eqnarray}
$$

where

$$
\begin{eqnarray}
    d^{t}
    :=
    V \nabla f^{t}(x^{t})
    +
    \sum_{k=1}^{m}
        Q_{k}^{t}
        \nabla g_{k}^{t}(x^{t})
    \nonumber
\end{eqnarray}
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

$$
\begin{eqnarray}
    Q^{t}
    & := &
        (Q_{1}^{t}, \ldots, Q_{m}^{t})^{\mathrm{T}}
    \nonumber
    \\
    L^{t}
    & := &
        \frac{1}{2}
        \norm{Q^{t}}^{2}
    \nonumber
    \\
    \Delta^{t}
    & := &
        L^{t + 1}
        -
        L^{t}
    \nonumber
    \\
    & = &
        \frac{1}{2}
        \left(
            \norm{Q^{t + 1}}^{2}
            -
            \norm{Q^{t}}^{2}
        \right)
    \label{equation_05}
\end{eqnarray}
$$


#### Lemma 2

$$
\begin{eqnarray}
    \Delta^{t}
    \le
    \sum_{k=1}^{m}
        Q_{k}^{t}
        \left(
            g_{k}^{t}(x^{t}))
            +
            \left(
                \nabla
                g_{k}^{t}(x^{t}))
            \right)^{\mathrm{T}}
            \left(
                x^{t + 1}
                -
                x^{t}
            \right)
        \right)
        +
        \frac{1}{2}
        \left(
            G + \sqrt{m}D_{2}R
        \right)^{2}
    \label{equation_07}
\end{eqnarray}
$$

#### proof

$$
\begin{eqnarray}
    \frac{1}{2}
    \left(
        Q_{k}^{t+1}
    \right)^{2}
    & \le &
        \frac{1}{2}
        \left(
            Q_{k}^{t}
            +
            g_{k}^{t}(x^{t})
            +
            (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
            (x^{t + 1} - x^{t})
        \right)^{2}
    \nonumber
    \\
    & = &
        \frac{1}{2}
        (Q_{k}^{t})^{2}
        +
        (Q_{k}^{t})^{2}
        \left(
            g_{k}^{t}(x^{t})
            +
            (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
            (x^{t + 1} - x^{t})
        \right)
        +
        \frac{1}{2}
        \left(
            g_{k}^{t}(x^{t})
            +
            (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
            (x^{t + 1} - x^{t})
        \right)^{2}
    \nonumber
    \\
    & = &
        \frac{1}{2}
        (Q_{k}^{t})^{2}
        +
        (Q_{k}^{t})^{2}
        \left(
            g_{k}^{t}(x^{t})
            +
            (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
            (x^{t + 1} - x^{t})
        \right)
        +
        \frac{1}{2}
        \left(
            h_{k}^{t}(x^{t})
        \right)^{2}
    \nonumber
    \\
    h_{k}^{t}(x^{t})
    & := &
        g_{k}^{t}(x^{t})
        +
        (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
        (x^{t + 1} - x^{t})
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    s^{t}
    & := &
        (s_{1}^{t}, \ldots, s_{m}^{t})
    \nonumber
    \\
    s_{k}^{t}
    & := &
        (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
        (x^{t + 1} - x^{t})
    \nonumber
    \\
    h^{t}
    & := &
        (h_{1}^{t}, \ldots, h_{m}^{t})
    \nonumber
    \\
    \norm{h^{t}}
    & \le &
        \norm{g^{t}(x^{t})}
        +
        \norm{s^{t}}
    \nonumber
    \\
    & \le &
        G
        +
        \sqrt{
            \sum_{k=1}^{m}
                (D_{2}R)^{2}
        }
    \nonumber
    \\
    & = &
        G
        +
        \sqrt{m}
        D_{2}R
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 3
* $T \ge 1$,

Algorithm1 guarantees

$$
    \forall k \in [1:m],
    \
    \sum_{t=1}^{T}
        g_{k}^{t}(x^{t})
    \le
    \norm{Q^{T+1}}
    +
    D_{2}
    \sum_{t=1}^{T}
        \norm{
            x^{t+1} - x^{t}
        }
    .
$$

#### proof

$$
\begin{eqnarray}
    Q_{k}^{t+1}
    & = &
        \max
        \left(
            Q_{k}^{t}
            +
            g_{k}^{t}(x^{t})
            +
            (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
            (x^{t+1} - x^{t}),
            0
        \right)
    \nonumber
    \\
    & \ge &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        +
        (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
        (x^{t+1} - x^{t})
    \nonumber
    \\
    & = &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        +
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
\end{eqnarray}
$$

Suppose that

$$
\begin{eqnarray}
    \langle
        \nabla g_{k}^{t}(x^{t}),
        x^{t+1} - x^{t}
    \rangle
    \ge
    0
    .
\end{eqnarray}
$$

Then

$$
\begin{eqnarray}
    Q_{k}^{t}
    +
    g_{k}^{t}(x^{t})
    +
    \langle
        \nabla g_{k}^{t}(x^{t}),
        x^{t+1} - x^{t}
    \rangle
    & \ge &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        +
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
        -
        2
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
    \nonumber
    \\
    & = &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        -
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
    \nonumber
    \\
    & \ge &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        -
        \norm{
            \nabla g_{k}^{t}(x^{t})
        }
        \norm{
            x^{t+1} - x^{t}
        }
    \nonumber
\end{eqnarray}
$$

Suppose that

$$
\begin{eqnarray}
    \langle
        \nabla g_{k}^{t}(x^{t}),
        x^{t+1} - x^{t}
    \rangle
    <
    0
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    Q_{k}^{t}
    +
    g_{k}^{t}(x^{t})
    +
    \langle
        \nabla g_{k}^{t}(x^{t}),
        x^{t+1} - x^{t}
    \rangle
    & \ge &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        +
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
        2
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
    \nonumber
    \\
    & = &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        -
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
    \nonumber
    \\
    & \ge &
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t})
        -
        \norm{
            \nabla g_{k}^{t}(x^{t})
        }
        \norm{
            x^{t+1} - x^{t}
        }
    \nonumber
\end{eqnarray}
$$

TODO: complete proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 4
* $z \in \mathcal{X}_{0}$,
* $t \ge 1$,

Algorithm 1 guarantees

$$
\begin{eqnarray}
    V(\nabla f^{t}(x^{t}))^{\mathrm{T}}
    (x^{t + 1} - x^{t})
    +
    \sum_{k=1}^{m}
        Q_{k}^{t}
        (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
        (x^{t + 1} - x^{t})
    +
    \alpha
    \norm{x^{t+1} - x^{t}}^{2}
    \le
    V(\nabla f^{t}(x^{t}))^{\mathrm{T}}
    (z - x^{t})
    +
    \sum_{k=1}^{m}
        Q_{k}^{t}
        (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
        (z - x^{t})
    +
    \alpha
    \norm{z - x^{t}}^{2}
    -
    \alpha
    \norm{x^{t+1} - z}^{2}
\end{eqnarray}
$$

#### proof
In $$\eqref{equation_03}$$,

$$
    h(x)
    :=
    V
    \left(
        \nabla f^{t}(x^{t})
    \right)^{\mathrm{T}}
    \left(
        x - x^{t}
    \right)
    +
    \sum_{k=1}^{m}
        Q_{k}^{t}
        \left(
            \nabla g_{k}^{t}(x^{t})
        \right)^{\mathrm{T}}
        \left(
            x - x_{t}
        \right)
    +
    \alpha
    \norm{
        x - x^{t}
    }^{2}
$$

is strongly convex with modulus $2 \alpha$.
It is easy to see

$$
    \phi(x)
    :=
    V
    \left(
        \nabla f^{t}(x^{t})
    \right)^{\mathrm{T}}
    \left(
        x - x^{t}
    \right)
    +
    \sum_{k=1}^{m}
        Q_{k}^{t}
        \left(
            \nabla g_{k}^{t}(x^{t})
        \right)^{\mathrm{T}}
        \left(
            x - x_{t}
        \right)
$$

is convex.
Thus,

$$
    h(x)
    =
    \phi(x)
    +
    \alpha
    \norm{
        x - x^{t}
    }^{2}
$$

is strongly convex with modulus $2 \alpha$.
We know for strongly convex function $h$ with module $c$

$$
\begin{eqnarray}
    x^{*}
    & := &
        \arg\min_{x \in \mathcal{X}_{0}} h(x)
    \nonumber
    \\
    h(x^{*})
    & \le &
        h(x)
        -
        \frac{c}{2}
        \norm{
            x - x^{*}
        }^{2}
        \
        \forall x \in \mathcal{X}_{0}
    .
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary 1
* $z \in \mathcal{X}_{0}$,
* $t \ge 1$,

Algorithm 1 guarantees

$$
    \norm{x^{t + 1} - x^{t}}
    \le
    \frac{
        VD_{1}
    }{
        2\alpha
    }
    +
    \frac{
        \sqrt{m}
        D_{2}
    }{
        2\alpha
    }
    \norm{Q^{t}}
    .
$$

#### proof
In lemma4, by taking $z = x^{t}$, we obtain

$$
\begin{eqnarray}
    V(\nabla f^{t}(x^{t}))^{\mathrm{T}}
    (x^{t + 1} - x^{t})
    +
    \sum_{k=1}^{m}
        Q_{k}^{t}
        (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
        (x^{t + 1} - x^{t})
    +
    \alpha
    \norm{x^{t+1} - x^{t}}^{2}
    \le
    -
    \alpha
    \norm{x^{t} - x^{t+1}}^{2}
    .
\end{eqnarray}
$$

Rearranging terms

$$
\begin{eqnarray}
    2\alpha
    \norm{x^{t+1} - x^{t}}^{2}
    & \le &
        -
        V(\nabla f^{t}(x^{t}))^{\mathrm{T}}
        (x^{t + 1} - x^{t})
        -
        \sum_{k=1}^{m}
            Q_{k}^{t}
            (\nabla g_{k}^{t}(x^{t}))^{\mathrm{T}}
            (x^{t + 1} - x^{t})
    \nonumber
    \\
    & = &
        -
        V
        \langle
            \nabla f^{t}(x^{t}),
            x^{t + 1} - x^{t}
        \rangle
        -
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t + 1} - x^{t}
            \rangle
    \nonumber
    \\
    & = &
        -
        \left(
            V
            \langle
                \nabla f^{t}(x^{t}),
                x^{t + 1} - x^{t}
            \rangle
            +
            \langle
                Q^{t},
                \langle
                    \nabla g_{k}^{t}(x^{t}),
                    x^{t + 1} - x^{t}
                \rangle
            \rangle
        \right)
    \nonumber
    \\
    & = &
        \abs{
            -
            \left(
                V
                \langle
                    \nabla f^{t}(x^{t}),
                    x^{t + 1} - x^{t}
                \rangle
                +
                \langle
                    Q^{t},
                    \langle
                        \nabla g_{k}^{t}(x^{t}),
                        x^{t + 1} - x^{t}
                    \rangle
                \rangle
            \right)
        }
        \quad
        (\because \text{LHS} \ge 0)
    \nonumber
    \\
    & = &
        \abs{
            V
            \langle
                \nabla f^{t}(x^{t}),
                x^{t + 1} - x^{t}
            \rangle
            +
            \langle
                Q^{t},
                \langle
                    \nabla g_{k}^{t}(x^{t}),
                    x^{t + 1} - x^{t}
                \rangle
            \rangle
        }
    \nonumber
    \\
    & \le &
        V
        \abs{
            \langle
                \nabla f^{t}(x^{t}),
                x^{t + 1} - x^{t}
            \rangle
        }
        +
        \abs{
            \langle
                Q^{t},
                \langle
                    \nabla g_{k}^{t}(x^{t}),
                    x^{t + 1} - x^{t}
                \rangle
            \rangle
        }
        \quad
        (\because \text{triangle inequality})
    \nonumber
    \\
    & \le &
        V
        \norm{
            \nabla f^{t}(x^{t})
        }
        \norm{
            x^{t + 1} - x^{t}
        }
        +
        \norm{
            Q^{t}
        }
        \sqrt{
            \sum_{k=1}^{m}
                \left(
                    \langle
                        \nabla g_{k}^{t}(x^{t}),
                        x^{t + 1} - x^{t}
                    \rangle
                \right)^{2}
        }
        \quad
        (\because \text{Cauchy-Schwarz})
    \nonumber
    \\
    & \le &
        V
        \norm{
            \nabla f^{t}(x^{t})
        }
        \norm{
            x^{t + 1} - x^{t}
        }
        +
        \norm{
            Q^{t}
        }
        \sqrt{
            \sum_{k=1}^{m}
                \norm{
                    \nabla g_{k}^{t}(x^{t})
                }^{2}
                \norm{
                    x^{t + 1} - x^{t}
                }^{2}
        }
        \quad
        (\because \text{Cauchy-Schwarz})
    \nonumber
    \\
    & \le &
        V D_{1}
        \norm{
            x^{t + 1} - x^{t}
        }
        +
        \norm{
            Q^{t}
        }
        \sqrt{
            \sum_{k=1}^{m}
                \norm{
                    \nabla g_{k}^{t}(x^{t})
                }^{2}
                \norm{
                    x^{t + 1} - x^{t}
                }^{2}
        }
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary 2
* $T \ge 1$,

Algorithm 1 guarantees

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        g_{k}^{t}(x^{t})
    & \le &
        \norm{Q^{T+1}}
        +
        \frac{
            V T D_{1} D_{2}
        }{
            2 \alpha
        }
        +
        \frac{
            \sqrt{m} D_{2}^{2}
        }{
            2\alpha
        }
        \sum_{t=1}^{T}
            \norm{Q^{t}}
        \quad
        \forall k \in [1:m]
    \nonumber
\end{eqnarray}
$$

#### proof

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        g_{k}^{t}(x^{t})
    & \le &
        \norm{Q^{T+1}}
        +
        D_{2}
        \sum_{t=1}^{T}
            \norm{
                x^{t+1} - x^{t}
            }
        \quad
        (\because \text{lemma 3})
    \nonumber
    \\
    & \le &
        \norm{Q^{T+1}}
        +
        D_{2}
        \sum_{t=1}^{T}
            \left(
                \frac{
                    V D_{1}
                }{
                    2 \alpha
                }
                +
                \frac{
                    \sqrt{m} D_{2}
                }{
                    2\alpha
                }
                \norm{Q^{t}}
            \right)
        \quad
        (\because \text{Corollary 1})
    \nonumber
    \\
    & \le &
        \norm{Q^{T+1}}
        +
        \frac{
            V T D_{1} D_{2}
        }{
            2 \alpha
        }
        +
        \frac{
            \sqrt{m} D_{2}^{2}
        }{
            2\alpha
        }
        \sum_{t=1}^{T}
            \norm{Q^{t}}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

If we choose $V = \sqrt{T}$, $\alpha = $T$ in Alogrithm 1, 

* expected regret: $O(\sqrt{T})$,
* expected constraint violation: $O(\sqrt{T})$.

#### Lemma 5
* $$(\Omega, \mathcal{F}, P, \{\mathcal{F}_{t}\}_{t \in \mathbb{Z}_{\ge 0}})$$,
* $$\{Z_{t}\}_{t \in \mathbb{Z}_{\ge 0}}$$,
    * adapted process
* $t_{0} \in \mathbb{N}$,
* $\theta \in \mathbb{R}$,
* $\delta_{\mathrm{max}} > 0$,
* $\delta_{\mathrm{max}} > \zeta > 0$,

$$
\begin{eqnarray}
    \abs{
        Z(t + 1) - Z(t)
    }
    & \le &
        \delta_{\mathrm{max}}
    \label{equation_11}
    \\
    \mathrm{E}
    \left[
    \left.
        Z(t + t_{0}) - Z(t)
    \right|
        \mathcal{F}_{t}
    \right]
    & \le &
        1_{\{Z(t) < \theta\}}
        t_{0} \delta_{\mathrm{max}}
        +
        1_{\{Z(t) \ge \theta\}}
        -t_{0} \zeta
    \label{equation_12}
\end{eqnarray}
$$

Then

(1)

$$
    \forall t \in \mathbb{N},
    \
    \mathrm{E}
    \left[
        Z(t)
    \right]
    \le
    \theta
    +
    t_{0}
    \frac{
        4 \delta_{\mathrm{max}}^{2}
    }{
        \zeta
    }
    \log
        \left(
            1
            +
            \frac{
                8
                \delta_{\mathrm{max}}^{2}
            }{
                \zeta^{2}
            }
            \exp
            \left(
                \frac{\zeta}{4 \delta_{\mathrm{max}}}
            \right)
        \right)
    .
$$

(2) For any constant $0 < \mu < 1$,

$$
\begin{eqnarray}
    P(Z(t) \ge z(\mu))
    & \le &
        \mu
    \nonumber
    \\
    z(\mu)
    & := &
        \theta
        +
        t_{0}
        \frac{
            4 \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log
        \left(
            1
            +
            \frac{
                8 \delta_{\mathrm{max}}^{2}
            }{
                \zeta
            }
            \exp
            \left(
                \frac{\zeta}{4 \delta_{\mathrm{max}}}
            \right)
        \right)
        +
        t_{0}
        \frac{
            4 \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log
        \left(
            \frac{1}{\mu})
        \right)
    \nonumber
\end{eqnarray}
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 6
* $x^{*} \in \mathcal{X}_{0}$,

$$
    \tilde{g}(x^{*})
    :=
    \le
    \mathrm{E}
    \left[
        g(x^{*}; \cdot)
    \right]
    \le
    0.
$$

Then Algorithm 1 guarantees

$$
\begin{equation}
    \forall k \in [1:m],
    \
    t \in \mathbb{N},
    \
    \mathrm{E}
    \left[
        Q_{k}^{t}
        g_{k}^{t}(x^{*})
    \right]
    \le
    0
    \label{equation_13}
\end{equation}
$$

#### proof
Fix $k \in [1:m]$ and $t \in \mathbb{N}$.

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        Q_{k}^{t}
        g_{k}^{t}(x^{*})
    \right]
    & = &
        \mathrm{E}
        \left[
            Q_{k}^{t}
        \right]
        \mathrm{E}
        \left[
            g_{k}^{t}(x^{*})
        \right]
        \quad
        (\because \text{independence})
    \nonumber
    \\
    & \le &
        0
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 7
* $t_{0} \in \mathbb{N}$,
* $t \in \mathbb{N}$,

Then in Algorithm 1, the following holds

$$
\begin{eqnarray}
    \abs{
        \norm{Q^{t+1}}
        -
        \norm{Q^{t}}
    }
    & \le &
        \delta_{\mathrm{max}}
    \nonumber
    \\
    \mathrm{E}
    \left[
        \norm{Q^{t + t_{0}}}
        -
        \norm{Q^{t + t_{0}}}
        \mid
        \mathcal{F}_{t-1}
    \right]
    & \le &
        1_{\{\norm{Q^{t}} < \theta\}}
        t_{0}
        \delta_{\mathrm{max}}
        -
        1_{\{\norm{Q^{t}} \ge \theta\}}
        t_{0} \zeta
    \nonumber
\end{eqnarray}
$$

where

$$
\begin{eqnarray}
    \theta(t_{0})
    & := &
        \zeta
        t_{0}
        +
        \delta_{\mathrm{max}}
        t_{0}
        +
        \frac{
            \alpha R^{2}
        }{
            \zeta
            t_{0}
        }
        +
        \frac{
            V D_{1} R
            +
            \frac{1}{2}
            \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
    \nonumber
    \\
    \zeta
    & := &
        \frac{\epsilon}{2}
    \nonumber
    \\
    \delta_{\mathrm{max}}
    & := &
        G + \sqrt{m}D_{2} R
    \nonumber
\end{eqnarray}
$$

and $\epsilon$ is defined in Algorithm 2.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 1 Expected Constraint Violation Bound
* $V := \sqrt{T}$,
* $\alpha := T$,

Then for all $T \ge 1$,

$$
\begin{equation}
    \forall k \in [1:m],
    \
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            g_{k}^{t}(x^{t})
    \right]
    \le
    O(\sqrt{T})
    \label{equation_14}
\end{equation}
$$

#### proof
Let $Z^{t} := \norm{Q^{t}}$.
By lemma 7, $Z^{t}$ satisfies the conditions in Lemma 5.
By lemma 5, we have

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \norm{Q^{t}}
    \right]
    & \le &
        \theta
        +
        t_{0}
        \frac{
            4 \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log
            \left(
                1
                +
                \frac{
                    8
                    \delta_{\mathrm{max}}^{2}
                }{
                    \zeta^{2}
                }
                \exp
                \left(
                    \frac{\zeta}{4 \delta_{\mathrm{max}}}
                \right)
            \right)
    \nonumber
    \\
    & = &
        \theta(t_{0})
        +
        t_{0}
        B
    \nonumber
    \\
    & = &
        \zeta
        t_{0}
        +
        \delta_{\mathrm{max}}
        t_{0}
        +
        \frac{
            \alpha R^{2}
        }{
            \zeta
            t_{0}
        }
        +
        \frac{
            V D_{1} R
            +
            \frac{1}{2}
            \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        +
        t_{0}
        B
    \nonumber
    \\
    & = &
        \zeta
        \sqrt{T}
        +
        \delta_{\mathrm{max}}
        \sqrt{T}
        +
        \frac{
            T R^{2}
        }{
            \zeta
            \sqrt{T}
        }
        +
        \frac{
            \sqrt{T} D_{1} R
            +
            \frac{1}{2}
            \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        +
        \sqrt{T}
        B
    \nonumber
    \\
    & = &
        (
            \zeta
            +
            \delta_{\mathrm{max}}
            +
            B
        )
        \sqrt{T}
        +
        \frac{
            \sqrt{T} R^{2}
        }{
            \zeta
        }
        +
        \frac{
            \sqrt{T} D_{1} R
            +
            \frac{1}{2}
            \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
    \nonumber
    \\
    & = &
        (
            \zeta
            +
            \delta_{\mathrm{max}}
            +
            B
            +
            \frac{
                R^{2}
                +
                 D_{1} R
            }{
                \zeta
            }
        )
        \sqrt{T}
        +
        \frac{
            \delta_{\mathrm{max}}^{2}
        }{
            2
            \zeta
        }
    \nonumber
    \\
    & = &
        C_{1}
        \sqrt{T}
        +
        C_{2}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    B
    & := &
        \frac{
            4 \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log
            \left(
                1
                +
                \frac{
                    8
                    \delta_{\mathrm{max}}^{2}
                }{
                    \zeta^{2}
                }
                \exp
                \left(
                    \frac{\zeta}{4 \delta_{\mathrm{max}}}
                \right)
            \right)
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            g_{k}^{t}(x^{t})
    \right]
    & \le &
        \mathrm{E}
        \left[
            \norm{Q^{T+1}}
            +
            \frac{
                \sqrt{T} D_{1} D_{2}
            }{
                2
            }
            +
            \frac{
                \sqrt{m} D_{2}^{2}
            }{
                2T
            }
            \sum_{t=1}^{T}
                \norm{Q^{t}}
        \right]
        \quad
        (\because \text{Corollary 2})
    \nonumber
    \\
    & \le &
        C_{1} \sqrt{T + 1}
        +
        C_{2}
        +
        \frac{
            \sqrt{T} D_{1} D_{2}
        }{
            2
        }
        +
        \frac{
            \sqrt{m} D_{2}^{2}
        }{
            2T
        }
        \sum_{t=1}^{T}
            \left(
                C_{1} \sqrt{t}
                +
                C_{2}
            \right)
    \nonumber
    \\
    & \le &
        C_{1} \sqrt{T + 1}
        +
        C_{2}
        +
        \frac{
            \sqrt{T} D_{1} D_{2}
        }{
            2
        }
        +
        \frac{
            \sqrt{m} D_{2}^{2}
        }{
            2T
        }
        \sum_{t=1}^{T}
                C_{1} \sqrt{T}
        +
        \frac{
            \sqrt{m} D_{2}^{2}
            C_{2}
        }{
            2
        }
    \nonumber
    \\
    & = &
        \left(
            C_{1}
            \sqrt{T + 1}
            +
            \frac{
                D_{1} D_{2}
            }{
                2
            }
            \sqrt{T}
            +
            \frac{
                \sqrt{m} D_{2}^{2}
                C_{1}
                \sqrt{T}
            }{
                2
            }
        \right)
        +
        C_{2}
        +
        \frac{
            \sqrt{m} D_{2}^{2}
            C_{2}
        }{
            2
        }
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 8
* $z \in \mathcal{X}_{0}$,
* $T \ge 1$,

Then Algorithm 1 guarantees

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        f^{t}(x^{t})
    & \le &
        \sum_{t=1}^{T}
            f^{t}(z)
        +
        \frac{\alpha}{V}
        R^{2}
        +
        \frac{V D_{1}^{2}}{4 \alpha}
        T
        +
        \frac{1}{2}
        \left(
            G
            +
            \sqrt{m} D_{2} R
        \right)^{2}
        \frac{T}{V}
        +
        \frac{1}{V}
        \sum_{t=1}^{T}
        \left(
            \sum_{k=1}^{m}
                Q_{k}^{t}
                g_{k}^{t}(z)
        \right)
    \label{equation_15}
\end{eqnarray}
$$

#### proof
Fix $t \in \mathbb{N}$.
By lemma 4,

$$
\begin{eqnarray}
    V
    \langle
        \nabla f^{t}(x^{t}),
        x^{t+1} - x^{t}
    \rangle
    +
    \sum_{k=1}^{m}
        Q_{k}^{t}
        \langle
            \nabla g_{k}^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
    +
    \alpha
    \norm{x^{t+1} - x^{t}}^{2}
    & \le &
        V
        \langle
            \nabla f^{t}(x^{t}),
            z - x^{t}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \langle
                \nabla g_{k}^{t}(x^{t}),
                z - x^{t}
            \rangle
        +
        \alpha
        \norm{z - x^{t}}^{2}
        -
        \alpha
        \norm{z - x^{t + 1}}^{2}
    \nonumber
    \\
    & = &
        Vf^{t}(x^{t})
        -
        Vf^{t}(x^{t})
        +
        V
        \langle
            \nabla f^{t}(x^{t}),
            z - x^{t}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \left(
                g_{k}^{t}(x^{t})
                -
                g_{k}^{t}(x^{t})
                +
                \langle
                    \nabla g_{k}^{t}(x^{t}),
                    z - x^{t}
                \rangle
            \right)
        +
        \alpha
        \norm{z - x^{t}}^{2}
        -
        \alpha
        \norm{z - x^{t + 1}}^{2}
    \nonumber
    \\
    & \le &
        Vf^{t}(z)
        -
        Vf^{t}(x^{t})
        +
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \left(
                g_{k}^{t}(z)
                -
                g_{k}^{t}(x^{t})
            \right)
        +
        \alpha
        \norm{z - x^{t}}^{2}
        -
        \alpha
        \norm{z - x^{t + 1}}^{2}
        \quad
        (\because \text{convexity})
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        Vf^{t}(x^{t})
    \nonumber
    \\
    & \le &
        Vf^{t}(z)
        +
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \left(
                g_{k}^{t}(z)
                -
                g_{k}^{t}(x^{t})
            \right)
        +
        \alpha
        \norm{z - x^{t}}^{2}
        -
        \alpha
        \norm{z - x^{t + 1}}^{2}
        -
        V
        \langle
            \nabla f^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
        -
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
        -
        \alpha
        \norm{x^{t+1} - x^{t}}^{2}
    \nonumber
    \\
    & = &
        Vf^{t}(z)
        +
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \left(
                g_{k}^{t}(z)
                -
                g_{k}^{t}(x^{t})
            \right)
        +
        \alpha
        \norm{z - x^{t}}^{2}
        -
        \alpha
        \norm{z - x^{t + 1}}^{2}
        -
        V
        \langle
            \nabla f^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
        -
        \sum_{k=1}^{m}
            Q_{k}^{t}
            \left(
                g_{k}^{t}(x^{t})
                -
                g_{k}^{t}(x^{t})
                +
                \langle
                    \nabla g_{k}^{t}(x^{t}),
                    x^{t+1} - x^{t}
                \rangle
            \right)
        -
        \alpha
        \norm{x^{t+1} - x^{t}}^{2}
    \nonumber
    \\
    & \le &
        Vf^{t}(z)
        +
        \sum_{k=1}^{m}
            Q_{k}^{t}
            g_{k}^{t}(z)
        +
        \alpha
        \norm{z - x^{t}}^{2}
        -
        \alpha
        \norm{z - x^{t + 1}}^{2}
        -
        V
        \langle
            \nabla f^{t}(x^{t}),
            x^{t+1} - x^{t}
        \rangle
        -
        \Delta^{t}
        +
        \frac{1}{2}
        \left(
            G + \sqrt{m}D_{2}R
        \right)^{2}
        -
        \alpha
        \norm{x^{t+1} - x^{t}}^{2}
        \quad
        (\because \text{in lemma 2, }\eqref{equation_07})
\end{eqnarray}
$$

$$
\begin{eqnarray}
    -
    V
    \langle
        \nabla f^{t}(x^{t}),
        x^{t+1} - x^{t}
    \rangle
    -
    \alpha
    \norm{x^{t+1} - x^{t}}^{2}
    & = &
        \abs{
            V
            \langle
                \nabla f^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
        }
        -
        \alpha
        \norm{x^{t+1} - x^{t}}^{2}
    \nonumber
    \\
    & \le &
        V
        \norm{
            \nabla f^{t}(x^{t})
        }
        \norm{
            x^{t+1} - x^{t}
        }
        -
        \alpha
        \norm{x^{t+1} - x^{t}}^{2}
        \quad
        (\because \text{Cauchy-Schwarz})
    \nonumber
    \\
    & \le &
        V
        D_{1}
        \norm{
            x^{t+1} - x^{t}
        }
        -
        \alpha
        \norm{x^{t+1} - x^{t}}^{2}
    \nonumber
    \\
    & = &
        -
        \alpha
        \left(
            \norm{x^{t+1} - x^{t}}
            -
            \frac{
                V D_{1}
            }{
                2 \alpha
            }
        \right)^{2}
        +
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha
        }
    \nonumber
    \\
    & \le &
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha
        }
    \nonumber
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>

## Reference
