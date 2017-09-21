---
title: Singular Value Decomposition
---

## Singular Value Decomposition
* $m \ge n$
* $$A \in \mathbb{C}^{m \times n}$$,

SVD of $A$ is 

$$
\begin{equation}
    A
    =
    U \Sigma V^{*}
\end{equation}
$$

where 

* $U$
    * $m \times m$ unitary matrix
* $V$
    * $n \times n$ unitary matrix
* $$\Sigma = \mathrm{diag}(\sigma_{1}, \ldots, \sigam_{n})$$,
    * $m \times n$ matrix
    * $$\sigma_{1} \ge \ldots \ge \sigma_{n} \ge 0$$,

### Definition. Hermitian matrix
* $$A = (a_{j}^{i})_{i = 1, \ldots, m, j = 1, \ldots, n} \in \mathbb{C}^{m \times n}$$,
    * matrix

$A$ is a hermitian matrix iff $$A^{*} = A$$ where

$$
    A^{*} := \bar{A^{\mathrm{T}}}.
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. Singluar Value
* $m \ge n$
* $$A \in \mathbb{C}^{m \times n}$$,
    * Hermitian matrix

Singlua values $$\{\sigma_{1}, \ldots, \sigma_{k}\}$$ of $A$ are square root of non negative eigenvalues of $$AA^{*}$$.
i.e. Let $$\lambda_{1}, \ldots, \lambda_{n}$$ be eigenvalues of $$AA^{*}$$.

$$
    \{\sigma_{i}\}_{i}
    =
    \{\sqrt{\lambda_{i}} \mid \lambda_{i} \ge 0\}_{i}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Theorem 1
* $$A \in \mathbb{C}^{m \times n}$$,
* $$\sigma_{i}$$,
    * singular value of $A$,

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [lecture3.pdf](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-fall-2004/lecture-notes/lecture3.pdf)

