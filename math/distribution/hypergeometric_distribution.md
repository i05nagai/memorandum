---
title: Hypergeometric Distribution
---

## Hypergeometric Distribution

* $(\Omega, \mathcal{F}, P)$,
* $N \in \mathbb{N}$,
* $$K \in \{0, 1, \ldots, N\}$$,
* $$n \in \{1, \ldots, N\}$$,
* $$X: \Omega \rightarrow \{0, \ldots, N\}$$,

p.d.f. of hypergeometric function is defined by

$$
\begin{eqnarray}
    k \in \{0, 1, \ldots, N\},
    \
    \mathrm{Hyper}(k; N, K, n)
    & := &
        \frac{
            \left(
                \begin{array}{c}
                    K \\
                    k
                \end{array}
            \right)
            \left(
                \begin{array}{c}
                    N - K \\
                    n - k
                \end{array}
            \right)
        }{
            \left(
                \begin{array}{c}
                    N \\
                    n
                \end{array}
            \right)
        }
\end{eqnarray}
$$

* $k$,
    * is the number of observed succsess
* $n$,
    * is the number of trials

## c.d.f.
$$
\begin{eqnarray}
    F_{\mathrm{Hyper}}(k; N, K, n)
    & := &
        \sum_{i=0}^{k}
            \mathrm{Hyper}(i; N, K, n)
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \sum_{i=k + 1}^{N}
        \mathrm{Hyper}(i; N, K, n)
    & = &
        1 - F_{\mathrm{Hyper}}(k; N, K, n)
\end{eqnarray}
$$


## Example
* $N$,
    * the number of total groups
* $K$,
    * the number of people in YES condition
* $n$,
    * the number of people in treatment group

| Condition | treatment group | control group  | total   |
|-----------|-----------------|----------------|---------|
| YES       | $k$             | $K − k$        | $K$     |
| NO        | $n − k$         | $N + k − n − K$ | $N − K$ |
|-----------|-----------------|----------------|---------|
| total     | $n$             | $N − n$        | $N$     |


Suppose that $k$ is given by a value of some r.v. $X$.
Then p.d.f of $X$ follows $\mathrm{Hyper}(k; N, K, n)$.
Indeed, there are ${K \choose k}$ patterns to become YES state,
${N - K \choose n - k }$ patterns to become NO state
and $\{ N \choose n}$ total patterns to be in treatment group from $N$.

#### Proposition

$$
    \forall k \in \{0, 1, \ldots, N\},
    \
    \max(0, n + K - N)
    \le
    k
    \le
    \min(K, n)
    \Rightarrow
    \mathrm{Hyper}(k; N, K, n)
    \ge
    0
    .
$$

#### proof

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Hypergeometric distribution \- Wikipedia](https://en.wikipedia.org/wiki/Hypergeometric_distribution)
