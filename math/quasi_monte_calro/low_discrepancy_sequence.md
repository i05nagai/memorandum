---
title: Low Discrepancy Sequence
---

## Low Discrepancy Sequence

* $N \in \mathbb{N}$,
    * the number of points,
* $\mathcal{P} := \{x_{1}, x_{2}, \ldots\} \subset [0, 1)^{s}$,
    * point set
* $1_{A}$,
    * indicator function of a subset $A$,
* $s \in \mathbb{N}$,
    * dimension of integrand
* $f:[0, 1]^{s} \rightarrow \mathbb{R}$,
    * integrand

### Definition. local discrepancy
* $\mathcal{P}$,
* $\mathbf{t}=(t_{1}, \ldots, t_{s}) \in [0, 1)^{s}$,

Local discrepancy function $\Delta_{\mathcal{P}}^{N}(\mathbf{t})$ is defined by

$$
\begin{equation}
    \Delta_{\mathcal{P}}^{N}(\mathbf{t})
    :=
    \frac{1}{N}
    \sum_{n=1}^{N}
    1_{[\mathbf{0},\mathbf{t})}(x_{n})
    -
    \prod_{i=1}^{s}t_{i}
\end{equation}
$$

where $[\mathbf{0}, \mathbf{t}):=\prod_{i=1}^{s}[0,t_{i})$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. discrepancy

$$
\begin{equation}
    D_{N}(\mathcal{P})
    :=
    \sup_{
        \mathbf{y},\mathbf{z} \in [0, 1)^{s};
        \mathbf{y} < \mathbf{z}
    }
        \left|
            \frac{1}{N}
            \sum_{n=1}^{N}
                1_{[\mathbf{y},\mathbf{z})}(x_{n}) - \prod_{i=1}^{s}(z_{i} - y_{i})
        \right|.
\end{equation}
$$

is called $N$-points discrepnacy of point set $\mathcal{P}$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. $L_{p}$-discrepancy
$$
\begin{equation}
    L_{p}^{N}(\mathcal{P})
    :=
    \|\Delta_{\mathcal{P}}^{N}\|_{L_{p}}
    =
    \left(
        \int_{[0,1]^{s}}
            |
                \Delta_{\mathcal{P}}^{N}(\mathbf{t})
            | ^{p}
        \ d \mathbf{t}
    \right)^{1/p}.
\end{equation}
$$

is called $N$-points $L_{p}$-discrepancy $L_{p}^{N}(\mathcal{P})$ of point set $\mathcal{P}$.
In particular, if $p=\infty$, we say star-discrepancy, denoted by $D_{N}^{*}(\mathcal{P})$.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. low-discrepancy sequence
$\mathcal{P}$ is said to be low-discrepancy sequence if

$$
\begin{equation}
    D_{N}^{*}(\mathcal{P})
    \le
    O
    \left(
        \frac{(\log N)^{s}}{N}
    \right)
    \quad
    (\forall N \in \mathbb{N}).
\end{equation}
$$

<div class="end-of-statement" style="text-align: right">■</div>

The following theorem [1] show the relation between Low-discrepancy sequence $\mathcal{P}$ and numerical error of integration.

### Theorem. Koksma-Hlawska inequality
* $f:[0, 1]^{s} \rightarrow \mathbb{R}$,

If $f$ Hardy-Krause varidation is bounded (i.e. $V(f) < \infty$),
then for every $N \in \mathbb{N}$,

$$
\begin{equation}
    \left|
        \frac{1}{N}
        \sum_{n=1}^{N}
            f(x_{n})
        -
        \int_{[0,1]^{s}}
            f(u)
        \ d u
    \right|
    \le
    V(f) D_{N}^{*}(\mathcal{P})
    .
\end{equation}
$$

<div class="end-of-statement" style="text-align: right">■</div>

Below is immidate consequence of the Koksma-Hlawska inequality.

### Corollary.
* $\mathcal{P}$
    * low-discrepancy sequence

Then $\forall N \in \mathbb{N}$

$$
\begin{equation}
    \left|
        \frac{1}{N}
        \sum_{n=1}^{N}
            f(x_{n})
        -
        \int_{[0,1]^{s}}
            f(u)
        \ d u
    \right|
    =
    O
    \left(
        \frac{(\log N)^{s}}{N}
    \right)
    .
\end{equation}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Remark.
In QMC, The range of integration must be within $[0, 1]^{s}$.
If integrand is not within the range, integration by substitution is need to be applied.
In QMC, it is emprically well-known that the lower dimension $s$ of the integrand is, the faster convergence is achieved.

<div class="end-of-statement" style="text-align: right">■</div>

The theorem [1] below imply the relation of discrepancy and star-discrepancy.

### Theorem.
* $\mathcal{P}$
    * low-discrepancy sequence

Then for every $N \in \mathbb{N}$,

$$
\begin{equation}
    D_{N}^{*}(\mathcal{P})
    \le
    D_{N}(\mathcal{P})
    \le
    2^{s}D_{N}^{*}(\mathcal{P})
    .
\end{equation}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [1] H. Niederreiter, Random number generation and quasi-Monte Carlo methods, Vol. 63. Philadelphia: Society for Industrial and Applied mathematics, 1992.
