---
title: Duality in Nonconvex Optimization
---

## Duality in Nonconvex Optimization


### 1.2 Preliminaries
* $\bar{\mathbb{R}}$,
    * extended real number
* $V, V^{*}$,
    * real vector space
* $\langle , \rangle: V \times V^{*} \rightarrow \mathbb{R}$,
    * bilinear form


### Definition Separating
$V$ and $V^{*}$ is said to be vector spaces put in duality if there exists bilinear form $\langle , \rangle$.

Duality $\langle , \rangle$ is said to be separating if

$$
    u \neq 0 \in V,
    \
    \exists u^{*} \in V^{*},
    \text{ s.t. }
    \langle u, u^{*} \rangle \neq 0,
$$

and

$$
    u^{*} \neq 0 \in V^{*},
    \
    \exists u \in V,
    \text{ s.t. }
    \langle u, u^{*} \rangle \neq 0.
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition Weak topology
* $(\mathbb{R}, \mathcal{O})$,
    * standard topogical sp.
* $f_{u^{*}}: V \rightarrow \mathbb{R}$,
    * $$f_{u^{*}}(u) := \langle u, u^{*} \rangle$$,

We denote the weak topology on $V$ by $\sigma(V, V^{*})$.

$$
    \sigma(V, V^{*})
    :=
    \mathfrak{M}
    \{
        f_{u^{*}}^{-1}(O)
        \mid
        u^{*} \in V^{*},
        \
        O \in \mathcal{O}
    \}
    .
$$

Analogousy we define

$$
    \sigma(V, V^{*})
    :=
    \mathfrak{M}
    \{
        f_{u}^{-1}(O)
        \mid
        u \in V,
        \
        O \in \mathcal{O}
    \},
$$

where $$f_{u}(u^{*}) := \langle u, u^{*} \rangle$$ and $\mathfrak{M}(\mathcal{A})$ is the smallest topology containing $\mathcal{A} \subseteq 2^{\mathbb{R}}$.

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition Equivalent condition for Hausdorff
The following statements are equivalent:

* (a) $\sigma(V, V^{*})$ is Hausdorff,
* (b) $\sigma(V^{*}, V)$ is Hausdorff,
* (c) the duality between $V$ and $V^{*}$ is separating.

### proof
(a) $\Rightarrow$ (b)

(b) $\Rightarrow$ (c)



<div class="QED" style="text-align: right">$\Box$</div>

We shall consider the spaces $V$ and $V^{*}$ in separating duality endowed with the topologies $$\sigma(V, V^{*})$$ and $$\sigma(V^{*}, V)$$.
All statements concerning continuity, lower semicontinuity, convergence, closure, etc. will refer to continuity, lower semicontinuity, convergence, closure etc. in these topology.

### Definition lower semicontinuity
* $F: V \rightarrow \bar{\mathbb{R}}$,
    * functional

$F$ is said to be lower semicontinuity (l.s.c.) if 

$$
    \forall u \in V,
    \
    u_{n} \rightarrow u,
    \
    F(u) \le \lim \inf F(u_{n})
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition convex
* $F: V \rightarrow \bar{\mathbb{R}}$,
    * functional

$F$ is said to be convex if 

$$
    \forall w, u \in V,
    \
    F(\lambda u + (1 - \lambda) w)
    \le
    \lambda F(u)
    +
    (1 - \lambda))
    F(w)
    \quad
    \lambda \in (0, 1)
    .
$$

$F$ is said to be strictly convex if the above inequality is strict inequality for all $u \neq w$.

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition
* $F:V \rightarrow \bar{\mathbb{R}}$,
    * convex, l.s.c.

$$
    \exists u^{\prime} \in V,
    \
    F(u^{\prime}) = - \infty
    .
$$

Then

$$
    \forall u \in V,
    \
    F(u) = -\infty
    .
$$

### proof

<div class="QED" style="text-align: right">$\Box$</div>

### Definition affine continuous
* $f: V \rightarrow \bar{\mathbb{R}}$,
    * function

$f$ is said to be affine continuous on $V$ if there exists continuous linear functional $l:V \rightarrow \mathbb{R}$ and $\alpha \in \mathbb{R}$ such that

$$
    f(u) = l(u) + \alpha
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition
* $V$, $V^{*}$
    * in separating duality

If $f$ is affine continuous functions on $V$, then

$$
    \exists u^{*} \in V^{*},
    \text{ s.t. }
    f(u)
    =
    \langle u, u^{*} \rangle
    +
    \alpha
    .
$$

### proof

<div class="QED" style="text-align: right">$\Box$</div>

We shall denote by $\Gamma(V)$

$$
    \Gamma(V)
    :=
    \left\{
        f(u)
        :=
        \sup_{ i \in \Lambda }
            f_{i}(u)
        \mid
            \{
                f_{i}
            \}_{i \in \Lambda}
            \text{ a set of affine continuous funcitons on } V
    \right\}
$$


## Reference
* Toland, J. F. (1978). Duality in nonconvex optimization. Journal of Mathematical Analysis and Applications. https://doi.org/10.1016/0022-247X(78)90243-3
