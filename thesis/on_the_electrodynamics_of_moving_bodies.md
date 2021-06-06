---
title: On the electrodynamics of moving bodies
---

## On the electrodynamics of moving bodies


### 3. Theory of the Transformation of Co-ordinates and Times from a Stationary Sytem to another System in Uniform Motion of Translation Relatively to the Former

* $(x, y, z)$, $t$,
    * stationary system
* $(\xi , \eta, \zeta)$, $\tau$,
    * moving system


Assumptions

(1)

There exists $f$ such that

$$
    \tau
    =
    f(x, y, z, t)
$$


(2)

$f$ is linear


$$
    \tau
    =

$$


(3)

$$
    x^{\prime}
    :=
    x - vt
    .
$$


$$
    \tau_{1} - \tau_{0}
    :=
    \tau_{2} - \tau_{1}
    .
$$

$$
    \tau
    =
    a
    \left(
        t
        -
        \frac{
            v
        }{
            c^{2} - v^{2}
        }x^{\prime}
    \right)
$$

where $a$ is a function $\phi(v)$.
For brevity, we assume that $\tau = 0$ at $(0, 0, 0)$ in $k$, when $t = 0$.

For a ray of light emitted from the origin of the moving sytem $k$ at the time $\tau = 0$ in the direction of the increasing $\xi$,

$$
\begin{eqnarray}
    \xi
    & = &
        c \tau
    \nonumber
    \\
    & = &
        ac
        \left(
            t
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }x^{\prime}
        \right)
    .
    \nonumber
\end{eqnarray}
$$

When it is measured in the stationary system,

$$
    \frac{
        x^{\prime}
    }{
        c - v
    }
    =
    t.
$$

If we insert the value of $t$,

$$
\begin{eqnarray}
    \xi
    & = &
        ac
        \left(
            t
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }x^{\prime}
        \right)
    \nonumber 
    \\
    & = &
        ac
        \left(
            \frac{
                x^{\prime}
            }{
                c - v
            }x^{\prime}
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }x^{\prime}
        \right)
    \nonumber 
    \\
    & = &
        ac
        \left(
            \frac{
                1
            }{
                c - v
            }
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }
        \right)
        x^{\prime}
    \nonumber 
    \\
    & = &
        ac
        \left(
            \frac{
                c
            }{
                c^{2} - v^{2}
            }
        \right)
        x^{\prime}
    .
    \nonumber
\end{eqnarray}
$$

In an analogous manner by considering rays moing along the two other axes,
when

$$
    \frac{
        y
    }{
        \sqrt{
            c^{2} - v^{2}
        }
    }
    =
    t,
    \
    x^{\prime}
    =
    0,
$$

then

$$
\begin{eqnarray}
    \eta
    & = &
        c \tau
    \nonumber
    \\
    & = &
        ac
        \left(
            t -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }
            x^{\prime}
        \right)
    \nonumber
\end{eqnarray}
$$

Hence,

$$
\begin{eqnarray}
    \eta
    & = &
        ac t
    \nonumber
    \\
    & = &
        ac
        \frac{
            y
        }{
            \sqrt{
                c^{2} - v^{2}
            }
        }
    \nonumber
    .
\end{eqnarray}
$$

Similary,

$$
\begin{eqnarray}
    \zeta
    & = &
        ac
        \frac{
            z
        }{
            \sqrt{
                c^{2} - v^{2}
            }
        }
    \nonumber
    .
\end{eqnarray}
$$

Substituting for $x^{\prime} = x - vt$,

$$
\begin{eqnarray}
    \beta
    & := &
        \frac{
            1
        }{
            \sqrt{
                1 - v^{2} / c^{2}
            }
        }
    \nonumber
    \\
    & = &
        \frac{
            c
        }{
            \sqrt{
                c^{2} - v^{2}
            }
        }
    \nonumber
    \\
    \phi(v)
    & := &
        a \beta,
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \tau
    & = &
        a
        \left(
            t
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }
            x^{\prime}
        \right)
    \nonumber
    \\
    & = &
        a
        \left(
            t
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }
            (x - vt)
        \right)
    \nonumber
    \\
    & = &
        a
        \left(
            t
            +
            \frac{
                v^{2}
            }{
                c^{2} - v^{2}
            }
            t
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }
            x
        \right)
    \nonumber
    \\
    & = &
        a
        \left(
            \beta^{2}t
            -
            \frac{
                v
            }{
                c^{2} - v^{2}
            }
            x
        \right)
    \nonumber
    \\
    & = &
        a
        \left(
            \beta^{2}t
            -
            v \beta^{2}
            \frac{1}{c^{2}}
            x
        \right)
    \nonumber
    \\
    & = &
        \phi(v)
        \beta
        \left(
            t
            -
            \frac{v}{c^{2}}
            x
        \right)
    \label{equation_relation_tau}
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \xi
    & = &
        a
        \frac{
            c^{2}
        }{
            c^{2} - v^{2}
        }
        x^{\prime}
    \nonumber
    \\
    & = &
        a
        \beta^{2}
        (x - vt)
    \nonumber
    \\
    & = &
        \phi(v)
        \beta
        (x - vt)
    .
    \label{equation_relation_xi}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \eta
    & = &
        \frac{
            a c
        }{
            \sqrt{c^{2} - v^{2}}
        }y
    \nonumber
    \\
    & = &
        a \beta y
    \nonumber
    \\
    & = &
        \phi(v) y
    .
    \label{equation_relation_eta}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \zeta
    & = &
        \phi(v) z
    .
    \label{equation_relation_zeta}
\end{eqnarray}
$$

We have to prove that the principle of the constancy of the velocity of light iscompatible iwth the principle of relativity.

Let a spherical wave be emitted at $t = \tau = 0$ with the velocity $c$ in stationary system $K$.
$(x, y, z)$ is a point attained by this wave.

$$
\begin{eqnarray}
        \sqrt{x^{2} + y^{2} + z^{2}}
        =
        ct
        \nonumber
    & \Leftrightarrow &
        x^{2} + y^{2} + z^{2} 
        =
        c^{2} t^{2}
        \nonumber
        .
\end{eqnarray}
$$

From the equations above,

$$
\begin{eqnarray}
    v \tau + \xi
    & = &
        \phi(v) \beta
        \left(
            vt - \frac{v^{2}}{c^{2}}x
            +x - vt
        \right)
    \nonumber
    \\
    & = &
        \phi(v) \beta
        x
        \left(
            1
            - \frac{v^{2}}{c^{2}}
        \right)
    \nonumber
    \\
    & = &
        \phi(v) \beta
        x
        \frac{1}{\beta^{2}}
    \nonumber
    \\
    \Leftrightarrow
    \quad
    x
    & = &
        \frac{\beta}{\phi(x)}
        \left(
            v \tau + \xi
        \right)
    \nonumber
\end{eqnarray}
$$

Similary,

$$
\begin{eqnarray}
    \tau + \frac{v}{c^{2}}\xi
    & = &
        \phi(v) \beta
        \left(
            t - \frac{v}{c^{2}}x
            + \frac{v}{c^{2}}x
            - t \frac{v^{2}}{c^{2}}
        \right)
    \nonumber
    \\
    & = &
        \phi(v) \beta t
        \left(
            1
            - \frac{v^{2}}{c^{2}}
        \right)
    \nonumber
    \\
    & = &
        \phi(v) \beta
        t
        \frac{1}{\beta^{2}}
    \nonumber
    \\
    \Leftrightarrow
    \quad
    t
    & = &
        \frac{\beta}{\phi(x)}
        \left(
            \tau + \frac{v}{c^{2}}\xi
        \right)
    \nonumber
\end{eqnarray}
$$

Other equations are as follows.

$$
\begin{eqnarray}
    y
    & = & \frac{y}{\phi(v)},
    \nonumber
    \\
    \zeta
    & = & \frac{z}{\phi(v)}.
    \nonumber
\end{eqnarray}
$$

Substituting the equations into the above equation,

$$
\begin{eqnarray}
    & &
        x^{2}
        +y^{2}
        +z^{2}
        =
        c^{2} t^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \frac{\beta^{2}}{\phi^{2}(v)}
        \left(
            v \tau + \xi
        \right)^{2}
        +
        \frac{\eta^{2}}{\phi^{2}(v)}
        + 
        \frac{\zeta^{2}}{\phi^{2}(v)}
        =
        c^{2}
        \beta^{2}
        \frac{\beta^{2}}{\phi^{2}(v)}
        \left(
            \tau
            +
            \frac{v}{c^{2}} \xi
        \right)^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \beta^{2}
        \left(
            v \tau + \xi
        \right)^{2}
        -
        c^{2}
        \beta^{2}
        \left(
            \tau
            +
            \frac{v}{c^{2}} \xi
        \right)^{2}
        +
        \eta^{2}
        +
        \zeta^{2}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \beta^{2}
        \left(
            v \tau + \xi
            +
            c
            \left(
                \tau
                +
                \frac{v}{c^{2}} \xi
            \right)
        \right)
        \left(
            v \tau + \xi
            -
            c
            \left(
                \tau
                +
                \frac{v}{c^{2}} \xi
            \right)
        \right)
        + \eta^{2}
        + \zeta^{2}
        = 0
    \nonumber
\end{eqnarray}
    .
$$

Arraging the first term further, we will obtain

$$
\begin{eqnarray}
    &  &
        \beta^{2}
        \left(
            v \tau + \xi
            +
            c
            \tau
            +
            \frac{v}{c} \xi
        \right)
        \left(
            v \tau + \xi
            -
            c \tau
            -
            \frac{v}{c} \xi
        \right)
    \nonumber
    \\
    & = &
        \beta^{2}
        \left(
            (v + c) \tau 
            +
            \left(
                1
                +
                \frac{v}{c}
            \right)
            \xi
        \right)
        \left(
            (v - c)\tau
            +
            \left(
                1
                -
                \frac{v}{c}
            \right)
            \xi
        \right)
    \nonumber
    \\
    & = &
        \beta^{2}
        \left(
            (v + c)(v - c) \tau ^{2}
            +
            (v + c)
            \left(
                1
                -
                \frac{v}{c}
            \right)
            \tau
            \xi
            +
            (v - c)
            \left(
                1
                +
                \frac{v}{c}
            \right)
            \xi
            \tau
            +
            \left(
                1
                +
                \frac{v}{c}
            \right)
            \left(
                1
                -
                \frac{v}{c}
            \right)
            \xi^{2}
        \right)
    \nonumber
    \\
    & = &
        \beta^{2}
        \left(
            (v^{2} - c^{2}) \tau ^{2}
            +
            \left(
                v + c
                -
                \frac{v^{2}}{c}
                -
                v
            \right)
            \tau
            \xi
            +
            \left(
                v - c
                +
                \frac{v^{2}}{c}
                -
                v
            \right)
            \xi
            \tau
            +
            \left(
                1
                -
                \frac{v^{2}}{c^{2}}
            \right)
            \xi^{2}
        \right)
    \nonumber
    \\
    & = &
        \beta^{2}
        \frac{c^{2}}{\beta^{2}}
        \tau ^{2}
        +
        \beta^{2}
        \left(
            \left(
                c
                -
                \frac{v^{2}}{c}
            \right)
            \tau
            \xi
            +
            \left(
                \frac{v^{2}}{c}
                - c
            \right)
            \xi
            \tau
        \right)
        +
        \beta^{2}
        \frac{1}{\beta^{2}}
        \xi^{2}
    \nonumber
    \\
    & = &
        c^{2}
        \tau ^{2}
        +
        \xi^{2}
    \nonumber
\end{eqnarray}
$$

Combining the results,

$$
\begin{eqnarray}
    x^{2} + y^{2} + z^{2}
    =
    c^{2} t^{2}
    \Leftrightarrow
    \xi^{2} + \eta^{2} + \zeta^{2}
    =
    c^{2} \tau^{2}
    .
    \nonumber
\end{eqnarray}
$$


Now we will determine an unkown function $\phi$ of $v$.

- $K^{\prime}$ be a third system of co-ordinates
    - coordinates in $K^{\prime}$ is $(\Xi, H, Z)$,
    - relatively to the moving system $k$ is in a state of parallel translatory motion parallel to the axis of $\Xi$
    - moves with velocity $-v$
    - $x^{\prime}, y^{\prime}, z^{\prime}$,

By using $$\eqref{equation_relation_tau}$$,

$$
\begin{eqnarray}
    t^{\prime}
    & = &
        \phi(-v) \beta(-v)
        (\tau + v \frac{\xi}{c^{2}})
    \nonumber
    \\
    & = &
        \phi(-v) \beta(-v)
        \left(
            \phi(v)
            \beta(v)
            \left(
                t
                -
                \frac{v}{c^{2}}x
            \right)
            +
            \frac{v}{c^{2}}
            \left(
                \phi(v) \beta(v)
                (x - vt)
            \right)
        \right)
    \nonumber
    \\
    & = &
        \phi(-v) \phi(v) \beta^{2}
        \left(
            t
            -
            \frac{v}{c^{2}}x
            +
            \frac{v}{c^{2}}
            x
            -
            \frac{v^{2}}{c^{2}}
            t
        \right)
    \nonumber
    \\
    & = &
        \phi(-v) \phi(v) \beta^{2}
        t
        \frac{1}{\beta^{2}}
    \nonumber
    \\
    & = &
        \phi(-v)
        \phi(v)
        t
    .
\end{eqnarray}
$$

By using $$\eqref{equation_relation_xi}$$ and $$\eqref{equation_relation_tau}$$,

$$
\begin{eqnarray}
    x^{\prime}
    & = &
        \phi(-v) \beta(-v)
        (\xi + v \tau)
    \nonumber
    \\
    & = &
        \phi(-v) \beta(-v)
        \left(
            \phi(v)\beta(v)
            (x - vt)
            +
            v
            \phi(v)\beta(v)
            \left(
                t
                -
                \frac{v}{c^{2}}x
            \right)
        \right)
    \nonumber
    \\
    & = &
        \phi(-v) \phi(v) \beta^{2}
        \left(
            x
            - vt
            +
            v t
            -
            \frac{v^{2}}{c^{2}}x
        \right)
    \nonumber
    \\
    & = &
        \phi(-v) \phi(v) \beta^{2}
        x
        \frac{1}{\beta^{2}}
    \nonumber
    \\
    & = &
        \phi(-v)
        \phi(v)
        x
    .
    \nonumber
\end{eqnarray}
$$

By using $$\eqref{equation_relation_eta}$$ and $$\eqref{equation_relation_zeta}$$,
,

$$
\begin{eqnarray}
    y^{\prime}
    & = &
        \phi(-v) \eta
    \nonumber
    \\
    & = &
        \phi(-v)
        \phi(v)
        y
    \nonumber
    \\
    z^{\prime}
    & = &
        \phi(-v) \zeta
    \nonumber
    \\
    & = &
        \phi(-v)
        \phi(v)
        z
    \nonumber
    .
\end{eqnarray}
$$

Since the relations between $x^{\prime}, y^{\prime}, z^{\prime}$ and $x, y, z$ do not contain the time $t$, it is clear that the transformation from $K$ to $K^{\prime}$ must be the identical transformation.

Thus,

$$
\begin{equation}
    \phi(v)\phi(-v)
    =
    1
    \label{equation_relation_phi_1}
\end{equation}
    .
$$

Let $l$ be the length of a rigid rod.
To determine $\phi(v)$, we will consider a ridid rod moving parallel to $x$ axis with velocity $v$ relatively to stationary system $K$ lying between $(\xi, \eta, \zeta) = (0, 0, 0)$ and $(\xi, \eta, \zeta) = (0, l, 0)$.
The coordinates of the end of the rod in $K$ is $(x_{1}, y_{1}, z_{1})$

By using $$\eqref{equation_relation_xi}$$, $$\eqref{equation_relation_eta}$$, $$\eqref{equation_relation_zeta}$$, the coordinates of moving system $k$ can be transformed into $K$ by the following relations.

$$
\begin{eqnarray}
    & &
        \xi
        =
        \phi(v) \beta
        (x - vt)
    \nonumber
    \\
    & \Leftrightarrow &
        x
        =
        \frac{
            \xi
        }{
            \phi(v) \beta
        }
        + vt
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        \eta
        =
        \phi(v) y
    \nonumber
    \\
    & \Leftrightarrow &
        y
        =
        \frac{
            \eta
        }{
            \phi(v)
        }
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        \zeta
        =
        \phi(v) z
    \nonumber
    \\
    & \Leftrightarrow &
        z
        =
        \frac{
            \zeta
        }{
            \phi(v)
        }
    .
    \nonumber
\end{eqnarray}
$$

Using the relations, we can determine the coordinates of the rods in stationary system $K$.
For $(\xi, \eta, \zeta) = (0, l, 0)$,

$$
\begin{eqnarray}
    x_{1}
    & = &
        vt,
    \nonumber
    \\
    y_{1}
    & = &
        \frac{l}{\phi(v)}
    \nonumber
    \\
    z_{1}
    & = &
        0.
    \nonumber
\end{eqnarray}
$$

For $(\xi, \eta, \zeta) = (0, 0, 0)$,

$$
\begin{eqnarray}
    x_{2}
    & = &
        vt,
    \nonumber
    \\
    y_{2}
    & = &
        0
    \nonumber
    \\
    z_{2}
    & = &
        0
    .
    \nonumber
\end{eqnarray}
$$

The lenght of the lod in stationary system $K$ is $l / \phi(v)$.
From reasons of symmetry, the length of the moving rod measured in the stationary ssytem $K$ does not change if $v$ and $-v$ are interchanged.

$$
\begin{eqnarray}
    & &
        \frac{l}{\phi(v)}
        =
        \frac{l}{\phi(-v)}
    \nonumber
    \\
    & \Leftrightarrow &
        \phi(v)
        =
        \phi(-v)
    .
    \label{equation_relation_phi_2}
\end{eqnarray}
$$

It follows that $\phi(v) = 1$ from $$\eqref{equation_relation_phi_1}$$ and $$\eqref{equation_relation_phi_2}$$.
Therefore,

$$
\begin{eqnarray}
    \tau
    & = &
        \beta (t - vx / c^{2}),
    \\
    \xi
    & = &
        \beta (x - vt)
    \\
    \eta
    & = &
        y
    \\
    \zeta
    & = &
        z
    .
\end{eqnarray}
$$


#### 4. Physial Meaning of the Equations Obtained in Respect to Moving Rigid Bodies and Moving Clocks



$$

$$


## Reference
