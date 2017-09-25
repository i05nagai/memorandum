---
title: Eigenvalue
---

## Eigenvalue

## Definition. Eigenvector and Eigenvalues
* $$A \in \mathbb{C}^{n \times n}$$,

$$\lambda \in \mathbb{C}$$ is an eigenvalue of $A$ if and only if there is a vector $x \in \mathbb{C}^{n}$ such that

$$
    (A - \lambda I)x
    =
    0
    .
$$

$x$ is said to be an eigenvector with respect to $\lambda$.

<div class="end-of-statement" style="text-align: right">■</div>

## Remark
Eigenvector corresponding to an eigenvalue is not unique.
The number of eigenvectors with respect to an eigenvalue is determined by the rank of $$A - \lambda I$$.
Suppose that $\lambda$ is a eigenvalue of $A$.
By dimension theorem, we obtain

$$
    \dim \mathrm{Ker}(A - \lambda I)
    =
    n - \mathrm{rank}(A - \lambda I)
    .
$$

Hence the number of eigenvectors equals to $$\dim \mathrm{Ker}(A - \lambda I)$$.
So we can take linearly independent eigenvectors corresponding to eigenvalue $\lambda$.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
