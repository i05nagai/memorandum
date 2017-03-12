---
title: Asymptotic notations
---

## Asymptotic notation

### Def

asymptotically tight bound

$$
    f(n) \in \Theta(g(n)) 
    \Leftrightarrow
    \exists c_{1} > 0,
    \
    \exists c_{2} > 0,
    \
    \exists n_{0} > 0,
    \
    \forall n \ge n_{0},
    \
    0 \le c_{1} \le f(n) \le c_{2} g(n)
$$

asymptotic upper bound

$$
    f(n) \in O(g(n)) 
    \Leftrightarrow
    \exists c > 0,
    \
    \exists n_{0} > 0,
    \
    \forall n \ge n_{0},
    \
    0 \le f(n) \le c g(n)
$$

asymptotic lower bound

$$
    f(n) \in \Omega(g(n)) 
    \Leftrightarrow
    \exists c > 0,
    \
    \exists n_{0} > 0,
    \
    \forall n \ge n_{0},
    \
    0 \le cg(n) \le f(n)
$$

upper bound but asymptotically not tight.

$$
    f(n) \in o(g(n)) 
    \Leftrightarrow
    \forall c > 0,
    \
    \exists n_{0} > 0,
    \
    \forall n \ge n_{0},
    \
    0 \le f(n) < cg(n) 
$$

lower bound but asymptotically not tight

$$
    f(n) \in \omega(g(n)) 
    \Leftrightarrow
    \forall c > 0,
    \
    \exists n_{0} > 0,
    \
    \forall n \ge n_{0},
    \
    0 \le cg(n) < f(n)
$$

### Example
* $2n^{2} \in O(n^{2})$
* $2n^{2} \in o(n^{3})$
* $2n^{2} \in \Omega(n^{2})$
* $2n^{2} \in \omega(n)$

### Proposition(Equivalence Definitions)

$$
    f(n) \in \Theta(g(n))
    \Leftrightarrow
    f(n) \in O(g(n)),
    \
    f(n) \in \Omega(g(n)),
$$

$$
    f(n) \in O(g(n))
    \Leftrightarrow
    \limsup_{n \rightarrow \infty}
        \frac{
            f(n)
        }{
            g(n)
        }
    <
    \infty
$$

$$
    f(n) \in \Omega(g(n))
    \Leftrightarrow
    \limsup_{n \rightarrow \infty}
        \frac{
            g(n)
        }{
            f(n)
        }
    <
    \infty
$$

$$
    f(n) \in o(g(n))
    \Leftrightarrow
    \limsup_{n \rightarrow \infty}
        \frac{
            f(n)
        }{
            g(n)
        }
    =
    0
$$

$$
    f(n) \in \omega(g(n))
    \Leftrightarrow
    \limsup_{n \rightarrow \infty}
        \frac{
            g(n)
        }{
            f(n)
        }
    =
    0
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition(Transivity)

$$
\begin{eqnarray}
    f(n) \in \Theta(g(n)),
    \
    g(n) \in \Theta(h(n))
    & \Rightarrow &
        f(n) \in \Theta(h(n)),
    \nonumber
    \\
    f(n) \in O(g(n)),
    \
    g(n) \in O(h(n))
    & \Rightarrow &
        f(n) \in O(h(n)),
    \nonumber
    \\
    f(n) \in o(g(n)),
    \
    g(n) \in o(h(n))
    & \Rightarrow &
        f(n) \in o(h(n)),
    \nonumber
    \\
    f(n) \in \Omega(g(n)),
    \
    g(n) \in \Omega(h(n))
    & \Rightarrow &
        f(n) \in \Omega(h(n)),
    \nonumber
    \\
    f(n) \in \omega(g(n)),
    \
    g(n) \in \omega(h(n))
    & \Rightarrow &
        f(n) \in \omega(h(n)),
    \nonumber
\end{eqnarray}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition(Reflexivity)

$$
\begin{eqnarray}
    f(n) \in \Theta(f(n)),
    \nonumber
    \\
    f(n) \in O(f(n)),
    \nonumber
    \\
    f(n) \in \Omega(f(n)),
    \nonumber
\end{eqnarray}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition(Symmetry)

$$
\begin{eqnarray}
    f(n) \in \Theta(g(n)),
    \Leftrightarrow
    g(n) \in \Theta(f(n)),
    \nonumber
\end{eqnarray}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition(Transpose symmetry)

$$
\begin{eqnarray}
    f(n) \in O(g(n)),
    & \Leftrightarrow &
        g(n) \in \Omega(f(n)),
    \nonumber
    \\
    f(n) \in o(g(n)),
    & \Leftrightarrow &
        g(n) \in \omega(f(n)),
\end{eqnarray}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>
