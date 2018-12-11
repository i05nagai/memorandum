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

Additionally, we assume 

* $g_{k}^{t}$ is $\mathcal{F}_{t}$ measurable
* $Q_{k}^{t}$ is $\mathcal{F}_{t-1}$ measurable
* $g_{k}^{t}$ is independent of $\mathcal{F}_{t-1}$.

* $m \in \mathbb{N}$
    * the number of constraints
* $\mathcal{X}_{0}$,
    * convex set

#### Algorithm 1
* $V, \alpha > 0$,
* $x^{1} \in \mathcal{X}_{0}$,
* $Q_{k}^{1} := 0 \ (k = [1:m])$,

Step1. For $t = 1, \ldots, T$,

Step2. Play $x^{t}$

Step3. Observe a cost function $f^{t}$ and constraints $g_{k}^{t}$.
$f^{t}$ and $g_{k}^{t}$ is $\mathcal{F}_{t + 1}$ measurable.

Step4. Update

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

#### Remark

* $g_{k}^{t}$ is known at the begining of the round $t$, so we can assume $g_{k}^{t}$ is $\mathcal{F}_{t-1}$ measurable.
* $Q_{k}^{t}$ is not known at the begining of the round $t$, so we can assume $Q_{k}^{t}$ is $\mathcal{F}_{t}$ measurable.

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
    & &
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
    \nonumber
    \\
    & \le &
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
    \nonumber
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
        }^{2},
        \quad
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
If $\norm{x^{t + 1} - x^{1}} = 0$, it is easy to confirm the inequality holds.
Suppose that $\norm{x^{t + 1} - x^{1}} = 0$.
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
            m
            D{2}^{2}
            \norm{
                x^{t + 1} - x^{t}
            }^{2}
        }
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
        \sqrt{m}
        D_{2}
        \norm{
            x^{t + 1} - x^{t}
        }
    \nonumber
\end{eqnarray}
$$

Dividing both sides by $\norm{x^{t+1} - x^{t}}2\alpha$, we obtain

$$
\begin{eqnarray}
    \norm{x^{t+1} - x^{t}}
    & \le 
        \frac{
            V D_{1}
        }{
            2 \alpha
        }
        +
        \frac{
            \sqrt{m} D_{2}
        }{
            2 \alpha
        }
        \norm{Q^{t}}
    .
    \nonumber
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

If we choose $V = \sqrt{T}$, $\alpha = T$ in Alogrithm 1, 

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
        -
        1_{\{Z(t) \ge \theta\}}
        t_{0} \zeta
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
By lemma 10,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        e^{r Z(t)}
    \right]
    & \le &
        \frac{
            e^{r t_{0} \delta_{\mathrm{max}} }
        }{
            1 - \rho
        }
        e^{r\theta}
        +
        \rho^{\lceil \frac{t}{t_{0}} \rceil}
    \nonumber
    \\
    & \le &
        \frac{
            e^{r t_{0} \delta_{\mathrm{max}} }
        }{
            1 - \rho
        }
        e^{r\theta}
        +
        1
        \quad
        (\because 0 < \rho < 1)
    \nonumber
    \\
    & \le &
        \frac{
            e^{r t_{0} \delta_{\mathrm{max}}}
        }{
            1 - \rho
        }
        e^{r\theta}
        +
        e^{r\theta}
        \quad
        (\because 0 < r, 0 < \theta)
    \nonumber
    \\
    & = &
        e^{r\theta}
        \left(
            \frac{
                e^{r t_{0} \delta_{\mathrm{max}} }
            }{
                1 - \rho
            }
            +
            1
        \right)
        \label{equation_26}
\end{eqnarray}
$$

Proof of (1)

$$
\begin{eqnarray}
    \exp
    \left(
        r
        \mathrm{E}
        \left[
            Z(t)
        \right]
    \right)
    & \le &
        \mathrm{E}
        \left[
            e^{r Z(t)}
        \right]
        \quad
        (\because \text{Jensen's inequalith})
    \nonumber
    \\
    & \le &
        e^{r\theta}
        \left(
            \frac{
                e^{r t_{0} \delta_{\mathrm{max}}} 
            }{
                1 - \rho
            }
            +
            1
        \right)
        (\because \eqref{equation_26})
    .
\end{eqnarray}
$$

By taking logarithm on both side and dividing by $r$, we obtain

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        Z(t)
    \right]
    & \le &
        \theta
        +
        \frac{1}{r}
        \log
        \left(
            \frac{
                e^{r t_{0} \delta_{\mathrm{max}}}
            }{
                1 - \rho
            }
            +
            1
        \right)
    \nonumber
    \\
    & = &
        \theta
        +
        \frac{
            4 t_{0} \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log
        \left(
            \frac{
                \exp
                \left(
                    \frac{
                        \zeta
                        t_{0}
                        \delta_{\mathrm{max}}
                    }{
                        4 t_{0} \delta_{\mathrm{max}}^{2}
                    }
                \right)
            }{
                \zeta^{2}
            }
            8 \delta_{\mathrm{max}}^{2}
            +
            1
        \right)
    \nonumber
    \\
    & = &
        \theta
        +
        \frac{
            4 t_{0} \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log C_{1}
    \nonumber
    \\
    C_{1}
    & := &
        \frac{
            \exp
            \left(
                \frac{
                    \zeta
                }{
                    4 \delta_{\mathrm{max}}
                }
            \right)
        }{
            \zeta^{2}
        }
        8 \delta_{\mathrm{max}}^{2}
        +
        1
\end{eqnarray}
$$

Proof of (2)

For all $z \in \mathbb{R}$,

$$
\begin{eqnarray}
    P(Z(t) > z)
    & = &
        P(e^{r Z(t)} > e^{r z})
    \nonumber
    \\
    & \le &
        \frac{
            \mathrm{E}
            \left[
                e^{r Z(t)}
            \right]
        }{
            e^{rz}
        }
        \quad
        (\because \text{Markov's inequality})
    \nonumber
    \\
    & \le &
        e^{-rz}
        e^{r\theta}
        \left(
            \frac{
                e^{r t_{0} \delta_{\mathrm{max}} }
            }{
                1 - \rho
            }
            +
            1
        \right)
        \quad
        (\because \eqref{equation_26})
    \nonumber
    \\
    & = &
        \exp
        \left(
            \frac{
                \zeta
            }{
                4 t_{0} \delta_{\mathrm{max}}^{2}
            }
            (\theta - z)
        \right)
        C_{1}
        \label{equation_28}
\end{eqnarray}
$$

Let $\mu$ be RHS of $$\eqref{equation_28}$$.

$$
\begin{eqnarray}
    & &
        \log \mu
        =
        \frac{
            \zeta
        }{
            4 t_{0} \delta_{\mathrm{max}}^{2}
        }
        (\theta - z)
        +
        \log C_{1}
    \nonumber
    \\
    & \Leftrightarrow &
        z
        =
        \theta
        +
        \frac{
            4 t_{0} \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log C_{1}
        -
        \frac{
            4 t_{0} \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        \log \mu
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 6
* $x^{*} \in \mathcal{X}_{0}$,

$$
    \tilde{g}(x^{*})
    :=
    \mathrm{E}
    \left[
        g(x^{*}; \cdot)
    \right]
    \le
    0
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
        \norm{Q^{t}}
        \mid
        \mathcal{F}_{t-1}
    \right]
    & \le &
        1_{\{\norm{Q^{t}} < \theta(t_{0})\}}
        t_{0}
        \delta_{\mathrm{max}}
        -
        1_{\{\norm{Q^{t}} \ge \theta(t_{0})\}}
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
Note that the definition of $\theta(t_{0})$ in the original paper is wrong.

#### proof
By $$\eqref{lemma12_statement}$$ in lemma 12,

$$
\begin{eqnarray}
    \norm{Q^{t}}
    -
    \norm{Q^{t+1}}
    & \le &
        G + \sqrt{m}D_{2}R
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \norm{Q^{t}}
    -
    \norm{Q^{t+t_{0}}}
    & \le &
        \sum_{s=t}^{t_{0}-1}
            \left(
                \norm{Q^{s}}
                -
                \norm{Q^{s+1}}
            \right)
    \nonumber
    \\
    & \le &
        (t_{0} - 1 - t)
        (G + \sqrt{m}D_{2} R)
    \nonumber
    \\
    & \le &
        t_{0}
        (G + \sqrt{m}D_{2} R)
    \nonumber
\end{eqnarray}
$$

Suppose that  $\hat{x} \in \mathcal{X}_{0}$ and $\epsilon > 0$ satisfies the slater condition.

Fix $\tau \in \mathbb{N}$.
By lemma 4,

$$
\begin{eqnarray}
    & &
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            x^{\tau +1} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            \langle
                \nabla g_{k}^{\tau}(x^{t}),
                x^{\tau +1} - x^{\tau}
            \rangle
        +
        \alpha
        \norm{x^{\tau+1} - x^{\tau}}^{2}
    \nonumber
    \\
    & \le &
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            \hat{x} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            \langle
                \nabla g_{k}^{\tau}(x^{\tau}),
                \hat{x} - x^{\tau}
            \rangle
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
    \nonumber
    \\
    & = &
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            \hat{x} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            \left(
                g_{k}^{\tau}(x^{\tau})
                -
                g_{k}^{\tau}(x^{\tau})
                +
                \langle
                    \nabla g_{k}^{\tau}(x^{\tau}),
                    \hat{x} - x^{\tau}
                \rangle
            \right)
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
    \nonumber
    \\
    & \le &
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            \hat{x} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            \left(
                g_{k}^{\tau}(\hat{x})
                -
                g_{k}^{\tau}(x^{\tau})
            \right)
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
        \quad
        (\because \text{convexity})
    .
\end{eqnarray}
$$

By adding a term, we obtain

$$
\begin{eqnarray}
    & & 
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            x^{\tau +1} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            \left(
                g_{k}^{\tau}(x^{\tau})
                +
                \langle
                    \nabla g_{k}^{\tau}(x^{t}),
                    x^{\tau +1} - x^{\tau}
                \rangle
            \right)
        +
        \alpha
        \norm{x^{\tau+1} - x^{\tau}}^{2}
    \nonumber
    \\
    & \le &
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            \hat{x} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            g_{k}^{\tau}(\hat{x})
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
    .
    \nonumber
\end{eqnarray}
$$

Rearrangin terms yields

$$
\begin{eqnarray}
    & & 
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            \left(
                g_{k}^{\tau}(x^{\tau})
                +
                \langle
                    \nabla g_{k}^{\tau}(x^{t}),
                    x^{\tau +1} - x^{\tau}
                \rangle
            \right)
    \nonumber
    \\
    & \le &
        -
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            x^{\tau +1} - x^{\tau}
        \rangle
        -
        \alpha
        \norm{x^{\tau+1} - x^{\tau}}^{2}
        +
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            \hat{x} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            g_{k}^{\tau}(\hat{x})
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
    \nonumber
    \\
    & \le &
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha
        }
        +
        V
        \langle
            \nabla f^{\tau}(x^{\tau}),
            \hat{x} - x^{\tau}
        \rangle
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            g_{k}^{\tau}(\hat{x})
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
        \quad
        (\because \text{lemma 8-1})
    \nonumber
    \\
    & \le &
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha
        }
        +
        V
        \norm{
            \nabla f^{\tau}(x^{\tau})
        }
        \norm{
            \hat{x} - x^{\tau}
        }
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            g_{k}^{\tau}(\hat{x})
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
        \quad
        (\because \text{Cauchy-Schwarz})
    \nonumber
    \\
    & \le &
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha
        }
        +
        V D_{1} R
        +
        \sum_{k=1}^{m}
            Q_{k}^{\tau}
            g_{k}^{\tau}(\hat{x})
        +
        \alpha
        \norm{\hat{x} - x^{\tau}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{\tau + 1}}^{2}
    \label{lemma07_equation_01}
\end{eqnarray}
$$

It easy to confirm that

$$
\begin{eqnarray}
    \sum_{\tau=t}^{t + t_{0} - 1}
        \left(
            \alpha
            \norm{\hat{x} - x^{\tau}}^{2}
            -
            \alpha
            \norm{\hat{x} - x^{\tau + 1}}^{2}
        \right)
    & = &
        \alpha
        \norm{\hat{x} - x^{t}}^{2}
        -
        \alpha
        \norm{\hat{x} - x^{t + t_{0}}}^{2}
    \nonumber
    \\
    & \le &
        \alpha R^{2}
        \label{lemma07_equation_02}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \sum_{\tau=t}^{t + t_{0} - 1}
        \mathrm{E}
        \left[
        \left.
            \sum_{k=1}^{m}
                Q_{k}^{\tau}
                g_{k}^{\tau}(\hat{x})
        \right|
            \mathcal{F}_{t-1}
        \right]
    & \le &
        -
        \epsilon
        \sum_{\tau=t}^{t + t_{0} - 1}
            \mathrm{E}
            \left[
            \left.
                \norm{
                    Q^{\tau}
                }
            \right|
                \mathcal{F}_{t-1}
            \right]
        \quad
        (\because \text{lemma 11})
    \nonumber
    \\
    & \le &
        -
        \epsilon
        \sum_{\tau=t}^{t + t_{0} - 1}
            \mathrm{E}
            \left[
            \left.
                \norm{
                    Q^{t}
                }
                +
                (\tau - t)
                (G + \sqrt{m}D_{2}R)
            \right|
                \mathcal{F}_{t-1}
            \right]
        \quad
        (\because \text{lemma 12})
    \nonumber
    \\
    & = &
        -
        \epsilon
        \sum_{\tau=1}^{t_{0}}
            \mathrm{E}
            \left[
            \left.
                \norm{
                    Q^{t}
                }
                +
                (\tau - 1)
                (G + \sqrt{m}D_{2}R)
            \right|
                \mathcal{F}_{t-1}
            \right]
    \nonumber
    \\
    & = &
        -
        \epsilon
        \sum_{\tau=1}^{t_{0}}
            \norm{
                Q^{t}
            }
        +
        \epsilon
        \sum_{\tau=1}^{t_{0}}
            (\tau - 1)
            (G + \sqrt{m}D_{2}R)
        \quad
        (\because \text{our assumption})
    \nonumber
    \\
    & \le &
        -
        \epsilon
        t_{0}
        \norm{
            Q^{t}
        }
        +
        \epsilon
        t_{0}(t_{0} - 1)
        (G + \sqrt{m}D_{2}R)
    \nonumber
    \\
    & \le &
        -
        \epsilon
        t_{0}
        \norm{
            Q^{t}
        }
        +
        \epsilon
        t_{0}^{2}
        (G + \sqrt{m}D_{2}R)
    \nonumber
    \\
    & = &
        -
        \epsilon
        t_{0}
        \norm{
            Q^{t}
        }
        +
        \epsilon
        t_{0}^{2}
        \delta_{\mathrm{max}}
    \label{lemma07_equation_03}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        \mathrm{E}
        \left[
        \left.
            \norm{Q^{t+t_{0}}}^{2}
            -
            \norm{Q^{t}}^{2}
        \right|
            \mathcal{F}_{t-1}
        \right]
    \nonumber
    \\
    & = &
        2
        \mathrm{E}
        \left[
        \left.
            \sum_{\tau=t}^{t + t_{0} - 1}
                \Delta^{\tau}
        \right|
            \mathcal{F}_{t-1}
        \right]
    \nonumber
    \\
    & \le &
        2
        \mathrm{E}
        \left[
        \left.
            \sum_{\tau=t}^{t + t_{0} - 1}
            \left(
                \sum_{k=1}^{m}
                    Q_{k}^{\tau}
                    \left(
                        g_{k}^{\tau}(x^{\tau})
                        +
                        \langle
                            \nabla g_{k}^{\tau}(x^{t}),
                            x^{\tau +1} - x^{\tau}
                        \rangle
                    \right)
                +
                \frac{1}{2}
                \delta_{\mathrm{max}}
            \right)
        \right|
            \mathcal{F}_{t-1}
        \right]
        \quad
        (\because \text{lemma 2})
    \nonumber
    \\
    & \le &
        2
        \mathrm{E}
        \left[
        \left.
            \sum_{\tau=t}^{t + t_{0} - 1}
            \left(
                \frac{
                    V^{2}D_{1}^{2}
                }{
                    4 \alpha
                }
                +
                V D_{1} R
                +
                \sum_{k=1}^{m}
                    Q_{k}^{\tau}
                    g_{k}^{\tau}(\hat{x})
                +
                \alpha
                \norm{\hat{x} - x^{\tau}}^{2}
                -
                \alpha
                \norm{\hat{x} - x^{\tau + 1}}^{2}
                +
                \frac{1}{2}
                \delta_{\mathrm{max}}^{2}
            \right)
        \right|
            \mathcal{F}_{t-1}
        \right]
        \quad
        (\because \eqref{lemma07_equation_01})
    \nonumber
    \\
    & \le &
        2
        \mathrm{E}
        \left[
        \left.
            \sum_{\tau=t}^{t + t_{0} - 1}
            \left(
                \sum_{k=1}^{m}
                    Q_{k}^{\tau}
                    g_{k}^{\tau}(\hat{x})
            \right)
        \right|
            \mathcal{F}_{t-1}
        \right]
        +
        \frac{
            V^{2}D_{1}^{2}
            (t_{0} - 1)
        }{
            2 \alpha
        }
        +
        2
        V D_{1} R
        (t_{0} - 1)
        +
        (t_{0} - 1)
        \delta_{\mathrm{max}}^{2}
        +
        2 \alpha R^{2}
        \quad
        (\because \eqref{lemma07_equation_02})
    \nonumber
    \\
    & \le &
        -2
        \epsilon t_{0} \norm{Q^{t}}
        +
        2 \epsilon t_{0}^{2} \delta_{\mathrm{max}}
        +
        \frac{
            V^{2}D_{1}^{2}
            (t_{0} - 1)
        }{
            2 \alpha
        }
        +
        2
        V D_{1} R
        (t_{0} - 1)
        +
        (t_{0} - 1)
        \delta_{\mathrm{max}}^{2}
        +
        2 \alpha R^{2}
        \quad
        (\because \eqref{lemma07_equation_03})
    \nonumber
    \\
    & \le &
        -
        2\epsilon t_{0} \norm{Q^{t}}
        +
        2 \epsilon t_{0}^{2} \delta_{\mathrm{max}}
        +
        \frac{
            V^{2}D_{1}^{2}
            t_{0}
        }{
            2 \alpha
        }
        +
        2
        V D_{1} R
        t_{0}
        +
        t_{0}
        \delta_{\mathrm{max}}^{2}
        +
        2 \alpha R^{2}
    \nonumber
    \\
    & = &
        -
        2\epsilon t_{0} \norm{Q^{t}}
        +
        \frac{
            V^{2}D_{1}^{2}
            t_{0}
        }{
            2 \alpha
        }
        +
        2 \epsilon t_{0}^{2}
        \delta_{\mathrm{max}}
        +
        2
        V D_{1} R
        t_{0}
        +
        t_{0}
        \delta_{\mathrm{max}}^{2}
        +
        2 \alpha R^{2}
    \nonumber
    \\
    & = &
        -
        2\epsilon t_{0} \norm{Q^{t}}
        +
        t_{0} \epsilon
        \left(
            \frac{
                V^{2}D_{1}^{2}
            }{
                2 \alpha
                \epsilon
            }
            +
            2 t_{0}
            \delta_{\mathrm{max}}
            +
            \frac{
                2
                V D_{1} R
            }{
                \epsilon
            }
            +
            \frac{
                \delta_{\mathrm{max}}^{2}
            }{
                \epsilon
            }
            +
            \frac{
                2 \alpha R^{2}
            }{
                \epsilon t_{0}
            }
        \right)
    \nonumber
\end{eqnarray}
$$

Contunuing

Letting

$$
\begin{eqnarray}
    \theta(t_{0})
    :=
    \left(
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha \zeta
        }
        +
        2 t_{0}
        \delta_{\mathrm{max}}
        +
        \frac{
            V D_{1} R
        }{
            \zeta
        }
        +
        \frac{
            2
            \delta_{\mathrm{max}}^{2}
        }{
            \zeta
        }
        +
        \frac{
            \alpha R^{2}
        }{
            \zeta t_{0}
        }
    \right)
    +
    \frac{\epsilon}{2}
    t_{0}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        -
        2\epsilon t_{0} \norm{Q^{t}}
        +
        t_{0} \epsilon
        \theta(t_{0})
        -
        \frac{\epsilon^{2}}{2}
        t_{0}^{2}
    \nonumber
    \\
    & \le &
        -
        \epsilon t_{0} \norm{Q^{t}}
        -
        \epsilon t_{0} \theta(t_{0})
        +
        t_{0} \epsilon
        \theta(t_{0})
        -
        \frac{\epsilon^{2}}{2}
        t_{0}^{2}
    \nonumber
    \\
    & = &
        -
        \epsilon t_{0} \norm{Q^{t}}
        -
        \frac{\epsilon^{2}}{2}
        t_{0}^{2}
    \nonumber
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        \norm{Q^{t+t_{0}}}^{2}
    \right|
        \mathcal{F}_{t-1}
    \right]
    & \le &
        \norm{Q^{t}}^{2}
        -
        \epsilon t_{0} \norm{Q^{t}}
        -
        \frac{\epsilon^{2}}{2}
        t_{0}^{2}
    \nonumber
    \\
    & \le &
        \left(
            \norm{Q^{t}}
            -
            t_{0}
            \frac{\epsilon}{2}
        \right)^{2}
        -
        t_{0}^{2}
        \frac{\epsilon^{2}}{4}
        -
        \frac{\epsilon^{2}}{2}
        t_{0}^{2}
    \nonumber
    \\
    & \le &
        \left(
            \norm{Q^{t}}
            -
            t_{0}
            \frac{\epsilon}{2}
        \right)^{2}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \norm{Q^{t}}
    -
    t_{0}
    \zeta
    & \ge &
        \sqrt{
            \mathrm{E}
            \left[
            \left.
                \norm{Q^{t+t_{0}}}^{2}
            \right|
                \mathcal{F}_{t-1}
            \right]
        }
    \nonumber
    \\
    & \ge &
        \mathrm{E}
        \left[
        \left.
            \norm{Q^{t+t_{0}}}
        \right|
            \mathcal{F}_{t-1}
        \right]
        \quad
        (\because \text{Jensen's inequality})
\end{eqnarray}
$$

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

#### Lemma 8-1
* $z \in \mathcal{X}_{0}$,
* $T \ge 1$,

Then Algorithm 1 guarantees

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
    & \le &
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha
        }
        \label{lemma8_1_statement}
\end{eqnarray}
$$

#### proof

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
    & &
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
    \nonumber
    \\
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
    \label{equation_18}
\end{eqnarray}
$$

By lemma 8-1,

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
    & \le &
        \frac{
            V^{2}D_{1}^{2}
        }{
            4 \alpha
        }
    .
        \label{lemma8_equation_01}
\end{eqnarray}
$$

Moreover,

$$
\begin{eqnarray}
    -
    \sum_{t=1}^{T}
        \Delta^{t}
    & = &
        L(1) - L(T + 1)
    \nonumber
    \\
    & = &
        \frac{1}{2}
        \norm{Q^{1}}^{2}
        -
        \frac{1}{2}
        \norm{Q^{T+1}}^{2}
    \nonumber
    \\
    & = &
        -
        \frac{1}{2}
        \norm{Q^{T+1}}^{2}
    \nonumber
    \\
    & \le &
        0
        \label{lemma8_equation_02}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
        \left(
            \alpha
            \norm{z - x^{t}}^{2}
            -
            \alpha
            \norm{z - x^{t + 1}}^{2}
        \right)
    & = &
        \alpha
        \norm{z - x^{1}}^{2}
        -
        \alpha
        \norm{z - x^{T+1}}^{2}
    \nonumber
    \\
    & \le &
        \alpha R^{2}
        -
        \alpha
        \norm{z - x^{T+1}}^{2}
    \nonumber
    \\
    & \le &
        \alpha R
        \label{lemma8_equation_03}
\end{eqnarray}
$$

Combining the inequalities $$\eqref{lemma8_equation_01}$$, $$\eqref{lemma8_equation_02}$$, $$\eqref{lemma8_equation_03}$$, summing up $$\eqref{equation_18}$$ yields

$$
\begin{eqnarray}
    & &
        \sum_{t=1}^{T}
        \left(
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
            \Delta^{t}
            +
            \frac{1}{2}
            \left(
                G + \sqrt{m}D_{2}R
            \right)^{2}
            -
            V
            \langle
                \nabla f^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
            -
            \alpha
            \norm{x^{t+1} - x^{t}}^{2}
        \right)
    \nonumber
    \\
    & \le &
        \sum_{t=1}^{T}
            Vf^{t}(z)
        +
        \sum_{t=1}^{T}
            \sum_{k=1}^{m}
                Q_{k}^{t}
                g_{k}^{t}(z)
        +
        \alpha
        R^{2}
        +
        \frac{1}{2}
        \left(
            G + \sqrt{m}D_{2}R
        \right)^{2}
        T
        +
        \frac{
            V^{2} D_{1}^{2} T
        }{
            4 \alpha
        }
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 2 Expected Regret Bound
* $V := \sqrt{T}$,
* $\alpha := T$,
* $x^{*} \in \mathcal{X}_{0}$,

$$
    \mathrm{E}
    \left[
        g(x^{*})
    \right]
    \le
    0
    .
$$

Algorithm 1 guarantees for all $T \in \mathbb{N}$,

$$
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            f^{t}(x^{t})
    \right]
    \le
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            f^{t}(x^{*})
    \right]
    +
    O(\sqrt{T})
    .
$$

#### proof
Let $T \in \mathbb{N}$ be fixed.
Taking $z = x^{*}$ in Lemma 8 yields

$$
\begin{eqnarray}
    \frac{1}{V}
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
        \sum_{k=1}^{m}
            Q_{k}^{t}
            g_{k}^{t}(x^{*})
    \right]
    & \le &
        0
        \quad
        (\because \eqref{equation_13})
    \label{theorem2_equation_01}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            f^{t}(x^{t})
    \right]
    & \le &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                f^{t}(x^{*})
        \right]
        +
        \alpha
        R^{2}
        \frac{1}{V}
        +
        \frac{1}{2V}
        \left(
            G + \sqrt{m}D_{2}R
        \right)^{2}
        T
        +
        \frac{
            V D_{1}^{2} T
        }{
            4 \alpha
        }
        \quad
        (\because \eqref{theorem2_equation_01})
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                f^{t}(x^{*})
        \right]
        +
        T
        R^{2}
        \frac{1}{\sqrt{T}}
        +
        \frac{1}{2\sqrt{T}}
        \left(
            G + \sqrt{m}D_{2}R
        \right)^{2}
        T
        +
        \frac{
            \sqrt{T} D_{1}^{2} T
        }{
            4 T
        }
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                f^{t}(x^{*})
        \right]
        +
        \sqrt{T}
        \left(
            R^{2}
            +
            \frac{1}{2}
            \left(
                G + \sqrt{m}D_{2}R
            \right)^{2}
            +
            \frac{
                D_{1}^{2}
            }{
                4
            }
        \right)
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 10

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 11
* $\hat{x} \in \mathcal{X}_{0}$,
    * satisfies the slater condition

$$
    \forall t_{2} \le t_{1} - 1,
    \
    \mathrm{E}
    \left[
    \left.
        \sum_{k=1}^{m}
            Q_{k}^{t_{1}}
            g_{k}^{t_{1}}(\hat{x})
    \right|
        \mathcal{F}_{t_{2}}
    \right]
    \le
    -\epsilon
    \mathrm{E}
    \left[
    \left.
        \norm{Q^{t_{1}}}
    \right|
        \mathcal{F}_{t_{2}}
    \right]
$$

where $\epsilon > 0$.

#### proof
Let $t_{2} \le t_{1} - 1$ be fixed.

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        Q_{k}^{t_{1}}
        g_{k}^{t_{1}}(\hat{x})
    \right|
        \mathcal{F}_{t_{2}}
    \right]
    & = &
        \mathrm{E}
        \left[
        \left.
            Q_{k}^{t_{1}}
            \mathrm{E}
            \left[
            \left.
                g_{k}^{t_{1}}(\hat{x})
            \right|
                \mathcal{F}_{t_{1} - 1}
            \right]
        \right|
            \mathcal{F}_{t_{2}}
        \right]
        \quad
        (\because \text{By assumption})
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
        \left.
            Q_{k}^{t_{1}}
            \mathrm{E}
            \left[
                g_{k}^{t_{1}}(\hat{x})
            \right]
        \right|
            \mathcal{F}_{t_{2}}
        \right]
        \quad
        (\because \text{By assumption})
    \nonumber
    \\
    & = &
        -\epsilon
        \mathrm{E}
        \left[
        \left.
            Q_{k}^{t_{1}}
        \right|
            \mathcal{F}_{t_{2}}
        \right]
        \quad
        \text{-a.s.}
        \quad
        (\because \text{By the Slater condition})
\end{eqnarray}
$$

Thus, by summing up from $m \in [1:m]$ yields

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
    \left.
        \sum_{k=1}^{m}
            Q_{k}^{t_{1}}
            g_{k}^{t_{1}}(\hat{x})
    \right|
        \mathcal{F}_{t_{2}}
    \right]
    & \le &
        -\epsilon
        \mathrm{E}
        \left[
        \left.
            \sum_{k=1}^{m}
                Q_{k}^{t_{1}}
        \right|
            \mathcal{F}_{t_{2}}
        \right]
    \nonumber
    \\
    & \le &
        -\epsilon
        \mathrm{E}
        \left[
        \left.
            \sqrt{
                \sum_{k=1}^{m}
                    (Q_{k}^{t_{1}})^{2}
            }
        \right|
            \mathcal{F}_{t_{2}}
        \right]
    \nonumber
    \\
    & = &
        -\epsilon
        \mathrm{E}
        \left[
        \left.
            \norm{Q^{t_{1}}}
        \right|
            \mathcal{F}_{t_{2}}
        \right]
    .
    \nonumber
\end{eqnarray}
$$

The last inequality follows from $$\sum_{k=1}^{m} a_{k} \ge \sqrt{\sum_{k=1}^{m}a_{k}^{2}}$$ when $a_{k} \ge 0$.
The proof completed.

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma 12

$$
\begin{eqnarray}
    \forall t \ge 0,
    \
    \norm{Q^{t}}
    -
    G
    -
    \sqrt{m}D_{2} R
    & \le &
        \norm{Q^{t+1}}
    \nonumber
    \\
    & \le &
        \norm{Q^{t}} + G
    \label{lemma12_statement}
\end{eqnarray}
$$

#### proof
**Proof of the first inequality.**

Since $Q_{k}^{t} \ge 0$, 
Suppose that $$g_{k}^{t}(x^{t}) + \langle \nabla g_{k}^{t}(x^{t}), x^{t+1} - x^{t} \rangle \ge -Q_{k}^{t}$$, 

$$
\begin{eqnarray}
    \abs{
        \max\{
            Q_{k}^{t}
            +
            g_{k}^{t}(x^{t})
            +
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle,
            0
        \}
        -
        Q_{k}^{t}
    }
    & = &
        \abs{
            Q_{k}^{t}
            +
            g_{k}^{t}(x^{t})
            +
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
            -
            Q_{k}^{t}
        }
    \nonumber
    \\
    & = &
        \abs{
            g_{k}^{t}(x^{t})
            +
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
        }
    \nonumber
\end{eqnarray}
$$

Suppose that $$g_{k}^{t}(x^{t}) + \langle \nabla g_{k}^{t}(x^{t}), x^{t+1} - x^{t} \rangle < -Q_{k}^{t}$$, 

$$
\begin{eqnarray}
    \abs{
        \max\{
            Q_{k}^{t}
            +
            g_{k}^{t}(x^{t})
            +
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle,
            0
        \}
        -
        Q_{k}^{t}
    }
    & = &
        \abs{
            -
            Q_{k}^{t}
        }
    \nonumber
    \\
    & \le &
        \abs{
            g_{k}^{t}(x^{t})
            +
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
        }
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \norm{
        Q_{k}^{t+1}
        -
        Q_{k}^{t}
    }
    & \le &
        \norm{
            g^{t}(x^{t})
            +
            \langle
                \nabla g^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
        }
    \nonumber
    \\
    & \le &
        \norm{
            g^{t}(x^{t})
        }
        +
        \norm{
            \langle
                \nabla g^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle
        }
    \nonumber
    \\
    & \le &
        G
        +
        \sqrt{
            \sum_{k=1}^{m}
                \left(
                    \langle
                        \nabla g^{t}(x^{t}),
                        x^{t+1} - x^{t}
                    \rangle
                \right)^{2}
        }
    \nonumber
    \\
    & \le &
        G
        +
        \sqrt{
            \sum_{k=1}^{m}
                \norm{
                    \nabla g^{t}(x^{t})
                }^{2}
                \norm{
                    x^{t+1} - x^{t}
                }^{2}
        }
    \nonumber
    \\
    & \le &
        G
        +
        \sqrt{
            m
            G^{2}
            D_{2}^{2}
        }
    \nonumber
    \\
    & = &
        G
        +
        \sqrt{
            m
        }
        G
        D_{2}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    G
    +
    \sqrt{
        m
    }
    G
    D_{2}
    & \ge &
        \norm{
            Q^{t+1}
            -
            Q^{t}
        }
    \nonumber
    \\
    & \ge &
        \norm{
            Q^{t}
        }
        -
        \norm{
            Q^{t+1}
        }
        \quad
        (\because \text{triangle inequality})
    \nonumber
\end{eqnarray}
$$

The proof of the first inequality completed.

Proof of the second inequality.

$$
\begin{eqnarray}
    Q_{k}^{t+1}
    & = &
        \max\{
            Q_{k}^{t}
            +
            g_{k}^{t}(x^{t})
            +
            \langle
                \nabla g_{k}^{t}(x^{t}),
                x^{t+1} - x^{t}
            \rangle,
            0
        \}
    \nonumber
    \\
    & \le &
        \max\{
            Q_{k}^{t}
            +
            g_{k}^{t}(x^{t+1}),
            0
        \}
        \quad
        (\because \text{Convexity})
    \nonumber
\end{eqnarray}
$$

Recall that $0 \le a \le \max(b,0)$, then $a^{2} \le b^{2}$.
Applying this to the above, we obtain

$$
    \abs{Q_{k}^{t+1}}^{2}
    \le
    \left(
        Q_{k}^{t}
        +
        g_{k}^{t}(x^{t+1})
    \right)^{2}
    .
$$

Summing over $k \in [1:m]$,

$$
\begin{eqnarray}
    \norm{Q^{t+1}}^{2}
    & \le &
        \norm{
            Q^{t}
            +
            g^{t}(x^{t+1})
        }^{2}
    \nonumber
\end{eqnarray}
$$


$$
\begin{eqnarray}
    \norm{Q^{t+1}}
    & \le &
        \norm{
            Q^{t}
            +
            g^{t}(x^{t+1})
        }
    \nonumber
    \\
    & \le &
        \norm{
            Q^{t}
        }
        +
        \norm{
            g^{t}(x^{t+1})
        }
    \nonumber
    \\
    & \le &
        \norm{
            Q^{t}
        }
        +
        G
    .
    \nonumber
\end{eqnarray}
$$

The proof of the second inequality completed.

<div class="QED" style="text-align: right">$\Box$</div>

#### Application
* $$(\Omega, \mathcal{F}, P, \{\mathcal{F}_{t}\}_{t \in \mathbb{N}})$$,
    * probability space with filtration
* $T \in \mathbb{N}$,
* $N \in \mathbb{N}$,
    * the number of ads
* $M \in \mathbb{N}$,
    * the number of display ads
* $(Y_{d, a}^{s})_{s \in [0:T]} \ (d \in [1:M], a \in [1:N])$,
    * the number of clicks of advertimesement $a$ at dispaly $d$,
    * $Y_{d, a}^{0}$ is an initial value
    * adapted
* $(Z_{d, a}^{s})_{s \in [0:T]} \ (d \in [1:M], a \in [1:N])$,
    * the number of conversions of advertimesement $a$ at dispaly $d$,
    * $Z_{d, a}^{0}$ is an initial value
    * adapted
* $B_{a} \in \mathbb{R}_{\ge 0}$,

$$
\begin{eqnarray}
    \Delta Y_{d, a}^{t}
    & := &
        Y_{d, a}^{t+1}
        -
        Y_{d, a}^{t}
    \nonumber
    \\
    \Delta Z_{d, a}^{t}
    & := &
        Z_{d, a}^{t+1}
        -
        Z_{d, a}^{t}
    \nonumber
    \\
    S_{d, a}^{t}
    & := &
        \sum_{s=0}^{t-1}
        \mathrm{tCPA}_{a}
        \frac{
            Z_{d, a}^{s}
        }{
            Y_{d, a}^{s}
        }
        \Delta
        Y_{d, a}^{s}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
    & := &
        \mathrm{tCPA}_{a}
        \frac{
            Z_{d, a}^{t}
        }{
            Y_{d, a}^{t}
        }
    \nonumber
    \\
    \mathrm{CPA}_{d, a}^{t}(Y_{d, a}^{t}, Z_{d, a}^{t})
    & := &
        \frac{
            \sum_{s=0}^{t-1}
                \mathrm{CPC}_{d, a}(Y_{d, a}^{s}, Z_{d, a}^{s})
                \Delta Y_{d, a}^{s}
        }{
            Z_{d, a}^{t}
        }
    \nonumber
\end{eqnarray}
$$

For $t \in [0:T-1]$,

$$
\begin{eqnarray}
    & &
        g_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [0:t+1]}, (Z_{d, a}^{s})_{s \in [0:t+1]})
    \nonumber
    \\
    & := &
        \mathrm{E}
        \left[
        \left.
            \sum_{d=1}^{M}
                \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \frac{
                    Z_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
                1_{\{I_{t} = a\}}
            -
            \mathrm{tCPA}_{a}
            +
            1_{\{I_{t} = a\}}
            \left(
                \frac{
                    \sum_{d=1}^{M}
                        \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                        \Delta Y_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
            \right)
        \right|
            \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
        \left.
            \sum_{d=1}^{M}
                \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \frac{
                    Z_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
                \mathrm{E}
                \left[
                \left.
                    1_{\{I_{t} = a\}}
                \right|
                    \mathcal{F}_{t} \vee I_{t}
                \right]
            -
            \mathrm{tCPA}_{a}
            +
            \mathrm{E}
            \left[
            \left.
                1_{\{I_{t} = a\}}
            \right|
                \mathcal{F}_{t} \vee I_{t}
            \right]
            \left(
                \frac{
                    \sum_{d=1}^{M}
                        \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                        \Delta Y_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
            \right)
        \right|
            \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
        \left.
            \sum_{d=1}^{M}
                \mathrm{CPA}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \frac{
                    Z_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
                x_{a}
            -
            \mathrm{tCPA}_{a}
            +
            x_{a}
            \left(
                \frac{
                    \sum_{d=1}^{M}
                        \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                        \Delta Y_{d, a}^{t}
                }{
                    Z_{d, a}^{t+1}
                }
            \right)
        \right|
            \mathcal{F}_{t}
        \right]
\end{eqnarray}
$$

For $t \in [0:T-1]$,

$$
\begin{eqnarray}
    & &
        h_{a}^{t}(x; (Y_{d, a}^{s})_{s \in [0:t+1]}, (Z_{d, a}^{s})_{s \in [0:t+1]})
    \nonumber
    \\
    & := &
        \mathrm{E}
        \left[
        \left.
            \sum_{s=0}^{t}
            \sum_{d=1}^{M}
                \frac{
                    Y_{d, a}^{s}
                }{
                    Z_{d, a}^{s}
                }
                \mathrm{CPA}_{d, a}^{s}(Y_{d, a}^{s}, Z_{d, a}^{s})
            -
            B_{a}
            +
            1_{\{I_{t} = a\}}
            \left(
                \sum_{d=1}^{M}
                    \frac{
                        Y_{d, a}^{t+1}
                    }{
                        Z_{d, a}^{t+1}
                    }
                    \mathrm{CPA}_{d, a}^{t+1}(Y_{d, a}^{t+1}, Z_{d, a}^{t+1})
            \right)
        \right|
            \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
        \left.
            \sum_{s=0}^{t}
            \sum_{d=1}^{M}
                \frac{
                    Y_{d, a}^{s}
                }{
                    Z_{d, a}^{s}
                }
                \mathrm{CPA}_{d, a}^{s}(Y_{d, a}^{s}, Z_{d, a}^{s})
            -
            B_{a}
            +
            x_{a}
            \left(
                \sum_{d=1}^{M}
                    \frac{
                        Y_{d, a}^{t+1}
                    }{
                        Z_{d, a}^{t+1}
                    }
                    \mathrm{CPA}_{d, a}^{t+1}(Y_{d, a}^{t+1}, Z_{d, a}^{t+1})
            \right)
        \right|
            \mathcal{F}_{t}
        \right]
\end{eqnarray}
$$

The loss function at $t \in [0:T-1]$ is given by

$$
\begin{eqnarray}
    & &
        f^{t}(x; (Y_{d, a}^{s})_{s \in [t:t+1]}, (Z_{d, a}^{s})_{s \in [t:t+1]})
    \nonumber
    \\
    & := &
        -
        \mathrm{E}
        \left[
        \left.
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, I_{t}}(Y_{d, I_{t}}^{t}, Z_{d, I_{t}}^{t})
                \Delta Y_{d, I_{t}}^{t}
        \right|
            \mathcal{F}_{t}
        \right]
    \nonumber
    \\
    & = &
        -
        \mathrm{E}
        \left[
        \left.
            \sum_{a=1}^{N}
            \sum_{d=1}^{M}
                \mathrm{CPC}_{d, a}(Y_{d, a}^{t}, Z_{d, a}^{t})
                \Delta Y_{d, a}^{t}
                x_{a}
        \right|
            \mathcal{F}_{t}
        \right]
\end{eqnarray}
$$


## Reference
* Yu, H., Neely, M. J., & Wei, X. (2017). Online Convex Optimization with Stochastic Constraints, 1–23. Retrieved from http://arxiv.org/abs/1708.03741
