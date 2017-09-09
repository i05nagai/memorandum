---
title: Hilbert Space
---

## Hilbert Space


### Proposition 1
* $H$
    * hilbert space
* $$\alpha_{1}, \alpha_{2}, \beta_{1}, \beta_{2} \in H$$,

$$
    \langle
        \alpha_{1},
        \beta_{1}
    \rangle
    \pm
    \langle
        \alpha_{2},
        \beta_{2}
    \rangle
    =
    \langle
        \alpha_{1},
        \beta_{1} \pm \beta_{2}
    \rangle
    \pm
    \langle
        \alpha_{2} - \alpha_{1},
        \beta_{2}
    \rangle
$$

### proof.

$$
\begin{eqnarray}
    \langle
        \alpha_{1},
        \beta_{1}
    \rangle
    \pm
    \langle
        \alpha_{2},
        \beta_{2}
    \rangle
    & = &
        \langle
            \alpha_{1},
            \beta_{1}
        \rangle
        \pm
        \langle
            \alpha_{1}
            -
            \alpha_{1}
            +
            \alpha_{2},
            \beta_{2}
        \rangle
    \nonumber
    \\
    & = &
        \langle
            \alpha_{1},
            \beta_{1} \pm \beta_{2}
        \rangle
        \pm
        \langle
            \alpha_{2} - \alpha_{1},
            \beta_{2}
        \rangle
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 2
* $X$
    * Hilbert sp.
* $L$
    * closed subsp.

Then $\forall x \in X$, $$\exists ! (y, z)$$, s.t. $$y \in L$$, $$z \in L^{\perp}$$,

$$
\begin{equation}
    x = y + z
    \label{hilbert_space_orthogonal_projection}
\end{equation}
$$

### proof.
For uniquness, suppose that both $$y_{1}, z_{1}$$ and $$y_{2}, z_{2}$$ satisfy $$\eqref{hilbert_space_orthogonal_projection}$$.

$$
\begin{eqnarray}
    & &
        y_{1} - z_{1}
        =
        y_{2} - z_{2}
    \\
    & \Leftrightarrow &
        y_{1} - y_{2}
        =
        z_{1} - z_{2}
\end{eqnarray}
$$

Hence $$y_{1} - y_{2} \in L$$, and $$z_{2} - z_{2} \in L^{\perp}$$.
$$L \cap L^{\perp} = \{0\}$$ so that $$y_{1} - y_{2} = z_{1} - z_{2} = 0$$.

For existence, Let $\delta$ be

$$
\begin{equation}
    \delta
    :=
    \mathrm{dist}(x, L)
    =
    \inf_{h \in L} \| x - h\|.
    \label{inf}
\end{equation}
$$

There is a sequence $$\{h_{n}\}_{n \in \mathbb{N}} \subset L$$ such that

$$
    \|x - h_{n}\|
    \rightarrow
    \delta
    \
    (n \rightarrow \infty).
$$

By parallelogram law, 

$$
\begin{eqnarray}
    & &
        \|(x - h_{n}) + (x - h_{m})\|^{2}
        +
        \|(x - h_{n}) - (x - h_{m})\|^{2}
        =
        2 \|x -h_{n}\|^{2}
        +
        2 \|x -h_{m}\|^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \|2x - (h_{n} + h_{m})\|^{2}
        +
        \|h_{m} - h_{n}\|^{2}
        =
        2 \|x -h_{n}\|^{2}
        +
        2 \|x -h_{m}\|^{2}.
    \label{inequality_from_parallelogram_law}
\end{eqnarray}
$$

Since

$$
    \frac{
        h_{n} + h_{m}
    }{
        2
    }
    \in
    L,
$$

$$2\|x - (h_{n} + h_{m})/2\| \ge 2 \delta$$.
From $$\eqref{inequality_from_parallelogram_law}$$,

$$
\begin{eqnarray}
    0
    & \le &
        \|h_{m} - h_{n}\|^{2}
    \nonumber
    \\
    & = &
        2 \|x -h_{n}\|^{2}
        +
        2 \|x -h_{m}\|^{2}
        -
        \|2x - (h_{n} + h_{m})\|^{2}
    \nonumber
    \\
    & \le &
        2 \|x -h_{n}\|^{2}
        +
        2 \|x -h_{m}\|^{2}
        -
        4 \delta^{2}
    \nonumber
\end{eqnarray}
$$

$$h_{n}$$ is cauchy sequence.
Since $H$ is complete, the sequence converges to a point, say

$$
    y
    :=
    \lim_{n \rightarrow \infty} h_{n}.
$$

$$h_{n} \in L$$ and $L$ is closed so that $y \in L$.
By $$\eqref{inf}$$,

$$
\begin{equation}
    \delta
    =
    \|x - y\|
    =
    \min_{h \in L}
        \|x - h\|.
    \label{minumum_value}
\end{equation}
$$

Finally we will show $$z := x - y \perp L$$.
Suppose $\theta \in \mathbb{R}$, then we define for all $h \in L$

$$
    \eta(\theta)
    :=
    \|x - y - \theta h\|^{2}
    =
    \| x - (y + \theta h)\|^{2}.
$$

From $$\eqref{minumum_value}$$, it is easy to show that $\eta$ takes minimum value $\delta^{2}$ when $\theta = 0$.
Therefore $$\eta^{\prime}(0) = 0$$.
On the other hand,

$$
    \eta(\theta)
    =
    \|x - y\|^{2}
    -
    2\theta \mathrm{Re}(x - y, h)
    +
    \theta^{2} \|h\|^{2}
$$

$$\eta^{\prime}(0) = -2 \mathrm{Re}(x - y, h)$$.
Hence

$$
\begin{equation}
    \mathrm{Re}(x - y, h)
    =
    0.
    \label{equation_perp_for_real_part}
\end{equation}
$$

Substituting $ih$ into $$\eqref{equation_perp_for_real_part}$$ instead of $h$, 

$$
    0
    =
    \mathrm{Re}(x - y, ih)
    =
    \mathrm{Re}(-i(x - y, h))
    =
    \mathrm{Im}(x - y, h).
$$

By $$\eqref{equation_perp_for_real_part}$$, we obtain

$$
    (x - y, h)
    =
    0
    \
    \forall h \in L.
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 3
* $X$
    * Hilbert sp.
* $K$
    * closed convex set.

Then $\forall x \in X$, $$\exists ! y \in K$$, s.t.

$$
\begin{equation}
    \|x - y\|
    =
    \min_{h \in K}
    \|x - h\|.
    \label{projection_to_closed_convex_set}
\end{equation}
$$

Moreover, it is equivalent to existence of $y \in K$ satisfying

$$
\begin{equation}
    \forall v \in K,
    \
    \mathrm{Re}(x - y, v - y)
    \le
    0
    \label{projection_to_closed_convex_set_equivalent_condition}
\end{equation}
$$

### proof.
To prove existence of $y$ satisfying $$\eqref{projection_to_closed_convex_set}$$, we only need to replace $L$ with $K$ in the above proof.

Now we prove $$\eqref{projection_to_closed_convex_set} \Leftrightarrow \eqref{projection_to_closed_convex_set_equivalent_condition}$$.

($\Rightarrow$)

Suppose $v \in K$ and $$0 \le \theta \le 1$$,

$$
    y + \theta(v - y)
    =
    (1 - \theta)y
    +
    \theta v
    \in
    K.
$$

Hence by taking $h := v - y$ we can define

$$
    \eta(\theta)
    :=
    \|x - y - \theta h\|^{2}
    =
    \|x - (y + \theta h)\|^{2}.
$$

$\eta$ takes the minimum value when $\theta = 0$.

$$
    \eta(\theta)
    =
    \|x - y\|^{2}
    +
    2 \theta \mathrm{Re}(x - y, h)
    +
    \theta^{2} \|h\|^{2}.
$$

$$
\begin{eqnarray}
    & &
        \eta^{\prime}(0) = 0
    \nonumber
    \\
    & \Leftrightarrow &
        \mathrm{Re}(x - y, h) = 0.
    \nonumber
\end{eqnarray}
$$

($$\Leftarrow$$)

Suppose $$y_{1}, y_{2} \in K$$ satisfying $$\eqref{projection_to_closed_convex_set_equivalent_condition}$$.
Then

$$
\begin{eqnarray}
    \mathrm{Re}(x - y_{1}, y_{2} - y_{1})
    & \le &
        0,
    \nonumber
    \\
    \mathrm{Re}(x - y_{2}, y_{1} - y_{2})
    & \le &
        0.
    \nonumber
\end{eqnarray}
$$

By adding equations,

$$
    \mathrm{Re}(y_{2} - y_{1}, y_{2} - y_{1})
    =
    \| y_{2} - y_{1} \|^{2}
    \le
    0.
$$

Therefore $$y_{1} = y_{2}$$.


<div class="QED" style="text-align: right">$\Box$</div>



## Reference
