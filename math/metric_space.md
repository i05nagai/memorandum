---
title: Metric space
---

## Metric space


#### Completion
- $(X, d)$,
    - metric space

There is a metric space $(\bar{X}, \bar{d})$ and $\phi: X \rightarrow \bar{X}$ which satisfies

- (1) $(\bar{X}, \bar{d})$ is a complete
- (2) $\phi$ is metric preserving
- (3) $\phi(X)$ is dense in $\bar{X}$.

Moreover, such $((\bar{X}, \bar{d}), \phi)$ is unique.

#### Proof

(1)

Let $C(X)$ be a set of all cauchy squence.
We define a equivalence relation $R$ on $C(X)$ as

$$
    (x_{n}) R (y_{n})
    \Leftrightarrow
    \lim_{n}d(x_{n}, y_{n}) = 0
    .
$$

$R$ is a equivalence relation.
It is reflextive and symetric.
Transivity is prooved by triangle inequality.

Let $\bar{X} := C(S) / R$ and

$$
    \bar{d}([(x_{n})], [(y_{n})])
    :=
    \lim_{n} d(x_{n}, y_{n})
    .
$$

$\bar{d}$ is well-defined and metric in $\bar{X}$.
Indeed, if $$(x_{n})R(x^{\prime}_{n})$$ and $(y_{n})R(y_{n}^{\prime})$,
$\lim_{n}d(x_{n}, x_{n}^{\prime} = 0$ and $\lim_{n}d(y_{n}, y_{n}^{\prime}) = 0$.
Hence

$$
    d(x_{n}, y_{n})
    \le
    d(x_{n}, x_{n}^{\prime})
    +
    d(x_{n}^{\prime}, y_{n}^{\prime})
    +
    d(y_{n}^{\prime}, y_{n})
    .
$$

By taking limit of both sides, we obtain

$$
    \lim_{n} d(x_{n}, y_{n})
    \le
    \lim_{n} d(x_{n}^{\prime}, y_{n}^{\prime})
    .
$$

Similary, we obtain

$$
    \lim_{n} d(x_{n}^{\prime}, y_{n}^{\prime})
    \le
    \lim_{n} d(x_{n}, y_{n})
    .
$$

By definition of $\bar{d}$, identity of indiscernibles holds.
Symmetry, and triangle inequality can be derived from properties of $d$.
Thus, $(\bar{X}, \bar{d})$ is a metric space.

Let $x \in X$ and $(x_{n})$ where $x_{n} := x$ for all $n \in \mathbb{N}$.
$(x_{n})$ is a Cauchy sequence so we define

$$
    \phi(x)
    :=
    [(x_{n})]
    .
$$

$\phi$ is injective.
If $\phi(x) = \phi(y)$, $\lim_{n}d(x, y) = 0$. Hence $x = $.

$\phi$ is a metric preservering.
For $x, y \in X$,

$$
    \bar{d}(\phi(x), \phi(y))
    =
    \bar{d}([(x_{n})], [(y_{n})])
    =
    d((x, y)
    .
$$

(3) $X$ is dense in $\bar{X}$.
Let $[(x_{n})] \in \bar{X}$.
The sequence $$(\phi(x_{n}))_{n}$$ converges to $[(x_{n})]$.

$$
\begin{eqnarray}
    \bar{d}([(x_{i})], \phi(x_{n}))
    & = &
        \lim_{i} d(x_{i}, x_{n})
    \nonumber
\end{eqnarray}
$$

$(x_{n})$ is a Cauchy sequence in $X$ so

$$
    \lim_{n} \bar{d}([(x_{i})], \phi(x_{n}))
    =
    0
    .
$$

We will show that it is complete.
Let $$([(x_{n}^{i})_{n}])_{i}$$ be a Cauchy sequence.
$\phi(X)$ is dense in $X$.
For all $i \in \mathbb{N}$, there exists $x_{i} \in X$

$$
    \bar{d}([(x_{n}^{i})_{n}], \phi(x_{i}))
    =
    \frac{ 1 }{ i }
    .
$$

$(x_{i})_{i}$ is a Cauchy sequence in $X$.
Indeed,

$$
\begin{eqnarray}
    \bar{d}(\phi(x_{i}), \phi(x_{j}))
    \le
    \bar{d}(\phi(x_{i}), [(x_{k}^{i})_{k}])
    +
    \bar{d}([(x_{k}^{i})_{k}], [(x_{k}^{j})_{k}])
    +
    \bar{d}([(x_{k}^{j})_{k}], \phi(x_{j}))
    \nonumber
    .
\end{eqnarray}
$$

For any $\epsilon > 0$, there exists $n_{0} \in \mathbb{N}$ such that $i > n_{0}, j > n_{0}$,

$$
    d(x_{i}, (x_{j})
    =
    \bar{d}(\phi(x_{i}), \phi(x_{j}))
    <
    \epsilon
    .
$$

Thus, $[(x_{i})] \in \bar{X}$.

$$
\begin{eqnarray}
    \bar{d}([(x_{n}^{i})_{n}], [(x_{i})_{i}])
    \le
    \bar{d}([(x_{n}^{i})_{n}], \phi(x_{i}))
    +
    \bar{d}([(x_{n}^{i})_{n}], \phi(x_{i}))
\end{eqnarray}
$$

RHS converges to 0 as $i \rightarrow \infty$.
Therefore, $(\bar{X}, \bar{d})$ is complete.

(Uniquness)



<div class="QED" style="text-align: right">$\Box$</div>


## Reference
