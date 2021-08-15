---
title: Lebesgue Integral
---

## Lebesgue Integral


#### Definition

$$
    \mathbb{M}(S \rightarrow \mathbb{C})
    :=
    \{
        f: S \rightarrow \mathbb{C}
        \mid
        f \text{ is measurable}
    \}
    .
$$

$$
    L^{1}(\mu)
    :=
    \{
        f \in \mathbb{M}(S \rightarrow \mathbb{C})
        \mid
        \abs{f} \text{ is integrable}
    \}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem
* $(S, \mathcal{A}, \mu)$,
    * measure space
* $I := (a, b) \subseteq \mathbb{R}$,
* $$\{f_{t}\} \subseteq \mathbb{M}(S \rightarrow \mathbb{C}) \cap L^{1}(\mu)$$,

$$
\begin{eqnarray}
    F(t)
    & := &
        \int
            f
        \ d \mu
    \nonumber
\end{eqnarray}
$$

For all $(x, t) \in S \times I$, $ \frac{\partial f_{t}}{\partial t}(x)$ exists.
If there exists an open interval $J \subseteq I$ and $g \in L^{1}(\mu)$ such that

$$
    \sup_{t \in J}
    \abs{
        \frac{\partial f_{t}}{\partial t} 
    }
    \le
    g
    \quad
    \mu
    \text{-a.e.}
$$

Then $F$ is differentiable over $J$ and for all $t \in J$

$$
    F^{\prime}(t)
    =
    \int
        \frac{\partial f_{t}}{\partial t} 
    \ d \mu
    .
$$

#### proof
It is sufficnet that $f$ 

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
