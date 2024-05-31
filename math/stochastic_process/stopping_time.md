---
title: Stopping Time
---

## Stopping Time


#### Definition Stopping Time
- $$(\Omega, \mathcal{F}, P, \{\mathcal{F}_{t}\}_{0 \le t})$$,
    - probablility space with a filtration
- $T: \Omega \rightarrow [0, \infty)$,
    - r.v.

$T$ is said to be a stopping time of the filtration if

$$
    \{T \le t\} \in \mathcal{F}_{t}
$$

for every $t \in [0, \infty)$.

$T$ is said to be a optional time of the filtration if

$$
    \{T < t\} \in \mathcal{F}_{t}
$$

for every $t \in [0, \infty)$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition hitting time

- $X: [0, \infty) \times \omega \rightarrow \mathbb{R}$
    - stochastic process
- $A \subseteq \mathbb{R}$,

A stopping time

$$
    \tau_{A}(\omega)
    :=
    \inf
    \{
        t \in T \mid X_{t}(\omega) \in A
    \}
$$

is called a hitting time.

<div class="end-of-statement" style="text-align: right">■</div>


#### Lemmna 
- $T, S: \Omega \rightarrow [0, \infty)$,
    - stopping time

The followings are also stopping time;

- $A := \min(T, S)$,
- $B := \max(T, S)$,
- $C := T + S$,

#### proof

$$
\begin{eqnarray}
    \{\min(T, S) \le t\}
    & = &
        \{T \le t\}
        \cup
        \{S \le t\}
    \nonumber
    \\
    \{\max(T, S) \le t\}
    & = &
        \{T \le t\}
        \cap
        \{S \le t\}
    \nonumber
\end{eqnarray}
$$

All of sets are $\mathcal{F}_{t}$ measurable sets.

<div class="QED" style="text-align: right">$\Box$</div>


#### Definition
- $T$,
    - stopping time of the filtration $$\{\mathcal{F}_{t}\}$$,

The $\sigma$-field $\mathcal{F}_{T}$ of events determined prior to the stotping time $T$ is defined 

$$
    \mathcal{F}_{T}
    :=
    \{
        A \in \mathcal{F}
        \mid
        A \cap \{T \le t\} \in \mathcal{F}_{t},
        \
        t \ge 0
    \}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem Wald's equation
- $\tau$,
    - discrete stopping time
- $X_{n}$
    - i.i.d. discrete stochastic process with expectation $E[X_{n}]$.

If $E[\tau] < \infty$ and $E[\abs{X}] < \infty$,

$$
    \mathrm{E}
    \left[
        \sum_{n=1}^{\tau}
            X_{n}
    \right]
    =
    E[\tau]
    E[X]
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
- https://www.columbia.edu/~ks20/stochastic-I/stochastic-I-ST.pdf
