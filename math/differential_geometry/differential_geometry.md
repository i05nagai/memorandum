---
title: Differential Geometry
---

## Differential Geometry


#### Definition

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition
* $M$,
    * manifold
* $N$,
    * manifold
* $T_{p}M$,
    * tangent space at $p$
* $v \in T_{p}M$,
    * tanvent vector at $p$
    * $v:C^{\infty}(M) \rightarrow \mathbb{R}$,
        * linear map
* $T_{p}^{*}M$,
    * cotangent space at $p$
* $\omega \in T_{p}^{*}M$,
    * cotangent vector at $p$
    * $\omega:T_{p}M \rightarrow \mathbb{R}$,
        * linear map
* $TM$,
    * tangent bundle

$$
\begin{eqnarray}
    TM
    & := &
        \sqcup_{p \in M}T_{p}M
    \nonumber
    \\
    & = &
        \sqcup_{p \in M}
        \{p\}
        \times
        T_{p}M
    \\
    & \cong &
        \sqcup_{p \in M}
        \{p\}
        \times
        \mathbb{R}^{n}
\end{eqnarray}
    .
$$

* $T^{*}M$,
    * cotangent bundle

$$
\begin{eqnarray}
    T^{*}M
    & := &
        \sqcup_{p \in M}T_{p}^{*}M
    \nonumber
    \\
    & = &
        \sqcup_{p \in M}
        \{p\}
        \times
        T_{p}^{*}M
\end{eqnarray}
    .
$$

* $(p, v) \in TM$,
    * $p \in M$, $v \in T_{p}M$,

* $(p, \omega) \in T^{*}M$,
    * $p \in M$, $\omega \in T_{p}^{*}M$,

* $F: M \rightarrow N$,
    * smooth map
* $dF_{p}: T_{p}M \rightarrow T_{F(p)}{N}$
    * differential of $F$ at $p$

$$
    f \in C^{\infty}(N),
    \
    dF_{p}(v)(f)
    :=
    v(f \circ F)
    .
$$

* $X: M \rightarrow TM$,
    * vector field
    * $p \in M \mapto X_{p} TM$,

$$
\begin{eqnarray}
    X_{p}
    & = &
        X^{i}(p)
        \left.
            \frac{\partial}{\partial x^{i}} 
        \right|_{p}
    \nonumber
    \\
    \pi \circ X
    & = &
        \mathrm{Id}_{M}
    \nonumber
    .
\end{eqnarray}
$$

* vector bundle
* coframe
* frame

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition

$$
\begin{eqnarray}
    \left.
        \frac{\partial}{\partial x^{1}} 
    \right|_{\phi(p)},
    \ldots,
    \left.
        \frac{\partial}{\partial x^{n}} 
    \right|_{\phi(p)},
\end{eqnarray}
$$

form a basis for $T_{\phi(p)} \mathbb{R}^{n}$.

Let

$$
\begin{eqnarray}
    \left.
        \frac{\partial}{\partial x^{i}} 
    \right|_{p}
    & := &
        (d \phi_{p})^{-1}
        \left(
            \left.
                \frac{\partial}{\partial x^{n}} 
            \right|_{\phi(p)}
        \right)
    \nonumber
    \\
    & = &
        d(\phi^{-1})_{\phi(p)}
        \left(
            \left.
                \frac{\partial}{\partial x^{n}} 
            \right|_{\phi(p)}
        \right)
    \nonumber
\end{eqnarray}
$$

form a basis for $T_{p}M$.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
