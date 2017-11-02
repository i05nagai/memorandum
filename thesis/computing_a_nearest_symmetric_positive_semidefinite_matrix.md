---
title: Computing a nearest symmetric positive semidefinite matrix
---

## Computing a nearest symmetric positive semidefinite matrix
* $A \in \mathbb{R}^{n \times n}$
* $$\mathcal{S}^{n}$$,
    * symmetric positve semidefinite

spectra radius $\rho: \mathbb{R}^{n\times n} \rightarrow \mathbb{R}$

$$
    \rho(A)
    :=
    \max
    \{
        |\lambda|
        \mid
        \mathrm{det}(A - \lambda I) = 0
    \}
$$

The 2-norm

$$
    \|A\|_{2}
    :=
    \rho(A^{\mathrm{T}}A)^{1/2}
$$

The Frobenius norm

$$
    \|A\|_{F}
    :=
    \left(
        \sum_{i=1}^{n}
            \sum_{j=1}^{n}
                (a_{i}^{j})^{2}
    \right)^{1/2}
$$

We denote positive semidefinite matrix $A$ by $$A \geqslant 0$$.

The distance in the norm $$\| \cdot \|_{2}$$ is denoted by

$$
    \delta_{2}(A)
    :=
    \min_{X \in \mathcal{S}} \| A - X\|_{2}
$$

Positive semidefinite matrix $X$ satisfying $$\|A - X\| = \delta_{2}(A)$$ is termed a positve approximant of $A$.
For a positive semidefinite matrix $A$, $$A^{1/2}$$ denotes $X \in \mathcal{S}$ which satisfies

$$
    X^{2}
    =
    A
    .
$$

## 2. The Frobenius norm Positive Approximant

## Theorem 2.1.
* $$A \in \mathcal{A}^{n \times n}$$,
* $$B = (A + A^{\mathrm{T}}) / 2$$,
    * symmetric matrix
* $$C = (A - A^{\mathrm{T}}) / 2$$,
    * skew-symmetric matrix
* $$B = UH$$,
    * $U$ is a unitary matrix,
    * $H \in \mathcal{S}$.

Then $$ X_{F} := (B + H)/2 $$ is unique positive approximant of $A$ in the frobenius norm.

$$
    \min_{X \in \mathcal{S}}\|A - X\|_{F}^{2}
    =
    \sum_{\lambda_{i}(B) < 0}
        \lambda_{i}(B)^{2}
    +
    \|C\|_{F}^{2}
$$

where $$\lambda_{i}(B)$$ is $i$-th largest eigenvalue of $B$.
Moreover,

$$
\begin{eqnarray}
    X^{*}
    & := &
        Z \mathrm{diag}(d_{1}, \ldots, d_{n}) Z^{\mathrm{T}}
    \nonumber
    \\
    & = &
        \arg \min_{X \in \mathcal{S}} \|A - X\|_{F}^{2}
\end{eqnarray}
$$

where $Z \in \mathbb{R}^{n \times n }$ is unitary matrix satisfying $$B = Z \mathrm{diag}(\lambda_{1}(B), \ldots, \lambda_{n}(B))Z^{\mathrm{T}}$$ and

$$
    d_{i}
    :=
    \begin{cases}
        \lambda_{i}
        &
            \lambda_{i} \ge 0
        \\
        0
        &
            \lambda_{i} < 0
    \end{cases}
    .
$$

## proof.
Let $X$ be positive semidefnite.
$B$ is symmetric and $C$ is skew-symmetric so that by <a href="{{ site.baseurl }}/math/matrix_norm.html#proposition5">proposition</a> we have

$$
\begin{eqnarray}
    \|A - X \|_{F}^{2}
    & = &
        \|B + C - X \|_{F}^{2}
    \nonumber
    \\
    & = &
        \|B - X\|_{F}
        +
        \|C\|_{F}^{2}
    \nonumber
    .
\end{eqnarray}
$$

The problem reduces to that of approximating $B$.
Since $B$ is symmetric, by eigenvalue decomposition there exists unitary marix $Z$ and diagonal matrix $$\Lambda := \mathrm{diag}(\lambda_{1}, \ldots, \lambda_{n})$$ such that $$B = Z \Lambda Z^{\mathrm{T}}$$.
Let $$Y := (y_{j}^{i})_{i,j = 1, \ldots, n} := Z^{\mathrm{T}}XZ$$.
By <a href="{{ site.baseurl }}/math/positive_definite_matrix.html#theorem7">theorem</a>, $Y$ is positive semidefinite.
Then

$$
\begin{eqnarray}
    \|B - X\|_{F}^{2}
    & = &
        \|Z \Lambda Z^{\mathrm{T}} - X\|_{F}^{2}
    \nonumber
    \\
    & = &
        \|Z (\Lambda  - Z^{\mathrm{T}}XZ )Z^{\mathrm{T}}\|_{F}^{2}
    \nonumber
    \\
    & = &
        \|\Lambda  - Y\|_{F}^{2}
        \quad
        (\because Z \text{ is unitary})
    \nonumber
    \\
    & = &
        \sum_{i \neq j}
            (y_{j}^{i})^{2}
        +
        \sum_{i = 1}^{n}
            (\lambda_{i} - y_{i}^{i})^{2}
    \nonumber
    \\
    & \ge &
        \sum_{i = 1}^{n}
            (\lambda_{i} - y_{i}^{i})^{2}
    \nonumber
    \\
    & \ge &
        \sum_{i: \lambda_{i} < 0}
            (\lambda_{i} - y_{i}^{i})^{2}
        \quad
        (\because Y \text{ is positive semi-definite so that } y_{i}^{i} \ge 0)
    \nonumber
    \\
    & \ge &
        \sum_{i: \lambda_{i} < 0}
            (\lambda_{i})^{2}
    \nonumber
\end{eqnarray}
$$

The lower bound is attaind uniquly by $$Y := \mathrm{diag}(d_{1}, \ldots, d_{n})$$, where

$$
    d_{i}
    :=
    \begin{cases}
        \lambda_{i}
        &
            \lambda_{i} \ge 0
        \\
        0
        &
            \lambda_{i} < 0
    \end{cases}
    .
$$

Hence

$$
    X^{*}
    :=
    Z \mathrm{diag}(d_{1}, \ldots, d_{n}) Z^{\mathrm{T}}
$$

is the minimizer.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
