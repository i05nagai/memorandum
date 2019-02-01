---
title: Tightness
---

## Tightness

#### Definiton 1
* $(S, \rho)$,
    * metric space
* $\Pi$,
    * a family of probability measures on $(S, \mathcal{B}(\mathbb{R}^{n}))$,

$\Pi$ is said to be relatively compact if

$$
    \forall \{P_{n}\}_{n \in \mathbb{N}} \subseteq \Pi,
    \
    \exists \{P_{i_{n}}\}_{n \in \mathbb{N}} \subseteq \{P_{n}\}_{n},
    \
    \exists P
    \
    \text{ s.t. }
    P_{i_{n}}
    \overset{w}{\rightarrow}
    P
    .
$$

$\Pi$ is said to be tight if

$$
    \forall \epsilon > 0,
    \
    \exists K \subseteq S
    \
    \text{ s.t. }
    K \text{ is compact and }
    P(K) \ge 1 - \epsilon
    \
    (\forall P \in \Pi)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition 2

* $$(\Omega_{a}, \mathcal{F}_{a}, P_{a})$$,
    * probabilty spaces
* $$\{X^{a}\}_{a \in \Lambda}$$,
    * a family of $S$-valued r.v.s on $(\Omega_{a}, \mathcal{F}_{a}, P_{a})$

$$\{X^{a}\}_{a \in \Lambda}$$ is said to be relatively compact if $$\{P(X^{a})^{-1}\}$$ is relatively compact.

$$\{X^{a}\}_{a \in \Lambda}$$ is said to be tight if $$\{P(X^{a})^{-1}\}$$ is tight.

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem 3 Prohorov Theorem
* $(S, \rho)$,
    * a compelte, separable metric space
* $\Pi$,
    * a family of probability measures on $S$,

Then the following statements are equivalent;

(1) $\Pi$ is tight

(2) $\Pi$ is realatively compact.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Definiton 4
* $T > 0$,
* $\delta > 0$,
* $\omega \in C[0, \infty)$,

$$
\begin{eqnarray}
    m^{T}(\omega, \delta)
    & := &
        \max_{\abs{s - t} \le \delta, 0 \le s, t \le T}
        \abs{
            \omega(s)
            -
            \omega(t)
        }
    \nonumber
\end{eqnarray}
$$

is caleld the modulus of continuity on $[0, T]$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 5

* (1) $m^{T}$ is continuous in $\omega \in C[0, \infty)$ under the metric $\rho$ defined in <a href="{{ site.baseurl }}/math/wiener_measure.html#proposition-2">here</a>.
* (2) $m^{T}$ is non-decreasing in $\delta$
* (3) for each $\omega \in C[0, \infty)$, $\lim_{\delta \searrow 0} m^{T}(\omega, \delta) = 0$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
