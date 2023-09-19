---
title: Bloom Filter
---

$$
\newcommand{\OR}{\mathop{\rm OR}\nolimits}
$$

## Bloom Filter

- $m \in \mathbb{N}$,
    - bit length
- $U = \mathbb{F}_{2}^{m}$,
- $(\Omega, \mathcal{F}, P)$,
    - probability space

#### Definition OR operator
- $a, b \in U$,

We define $a \OR b$ as

$$
    c := a \OR b,
    \quad
    c_{i} := \begin{cases}
        0
        &
            (a_{i} = b_{i} = 0)
        \\
        1
        &
            (\text{otherwise})
    \end{cases}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition comparator
For $a, b \in U$,

$$
\begin{eqnarray}
    a \ll b
    \overset{\mathrm{def}}{\Leftrightarrow}
    \forall i \in \mathbb{N},
    \quad
    a_{i} = 1 \Rightarrow b_{i} = 1
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

- $$S := \{x_{1}, \ldots, x_{n}\} \subseteq U$$,
- $B \in \mathbb{F}_{2}^{m}$
    - $m$-bit vector
- $$e_{i} = (0, \ldots, 0, 1, 0, \ldots, 0)$$,
    - $m$-bit vector with only its $i$-th bit set to 1.
- $$E := \{e_{1}, \ldots, e_{m}\}$$,
- $k \in \mathbb{N}$,
    - number of random hash
- $$h_{1}, \ldots, h_{k}: U \times \Omega \rightarrow E$$,
    - random variable

$$
    h: U \times \Omega \rightarrow \mathbb{F}_{2}^{m},
    \quad
    h(x, \omega)
    :=
    h_{1}(x, \omega) \OR \cdots \OR h_{k}(x, \omega)
    .
$$

$h$ maps to a vector with at most $k$ bits are set to 1.

Update $B$

$$
    B
    :=
    h(x_{1}) \OR \cdots \OR h(x_{n})
    .
$$

Query whether $y \in U$ belongs to $S$

- (1) If $h(y) \ll B$, answer yes.
- (2) Otherwise, answer no.

## Algorithm

- Define random hash function $h_{1}, \ldots, h_{m}$,
- Define $$S := \{x_{1}, \ldots, x_{n}\}$$

Step 1. Define the filter $B$

$$
    B
    :=
    h(x_{1})
    \OR
    \cdots
    \OR
    h(x_{n})
    .
$$

Step 2-a. Query. Calculate the $h(y)$. If $h(y) \ll B$, return yes. Otherwise, retur no.

Step 2-b. Add $x_{n+1}$ to $S$.

$$
    B \leftarrow B \OR h(x_{n+1})
    .
$$


Computational compelxity

- Query: $O(k + m)$,
- Update: $O(k)$,


#### Probability of False positive


#### Choice of hash functions


## Reference
- https://en.wikipedia.org/wiki/Bloom_filter
- https://ayushgupta2959.medium.com/understanding-bloom-filters-part-2-a-space-time-trade-off-in-hash-coding-a502751c35a4
- https://www.enjoyalgorithms.com/blog/bloom-filter
