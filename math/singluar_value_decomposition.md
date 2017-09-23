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
* $$\Sigma = \mathrm{diag}(\sigma_{1}, \ldots, \sigma_{n})$$,
    * $m \times n$ matrix
    * $$\sigma_{1} \ge \ldots \ge \sigma_{n} \ge 0$$,

### Definition. Hermitian matrix
* $$A = (a_{j}^{i})_{i = 1, \ldots, m, j = 1, \ldots, n} \in \mathbb{C}^{m \times n}$$,
    * matrix

$A$ is a hermitian matrix iff $$A^{*} = A$$ where

$$
    A^{*} := \bar{A}^{\mathrm{T}}.
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
    * rank $r$
* $$\sigma_{i}$$,
    * singular value of $A$,
* $$Q_{1} \in \mathbb{C}^{n \times r}$$,
* $$Q_{2} \in \mathbb{C}^{n \times (n - r)}$$,
* $$Q := (Q_{1}, Q_{2}) \in \mathbb{C}^{n \times n}$$,
    * orthogonal matrix
* $$P_{1} := AQ_{1}D_{1}^{-1} \in \mathbb{C}^{m \times r}$$,
* $$P_{2} \in \mathbb{C}^{m \times (m - r)}$$,
* $$P := (P_{1}, P_{2}) \in \mathbb{C}^{m times m}$$,
* $$D_{1} \in \mathbb{C}^{r \times r}$$,

Suppose $A$ satisfies

$$
\begin{equation}
    Q^{\mathrm{T}}A^{\mathrm{T}}AQ
    =
    \left(
        \begin{array}{cc}
            D_{1}^{2}
            &
                0
            \\
            0
            &
                0
        \end{array}
    \right).
    \label{singular_value_decomposition_condition}
\end{equation}
$$

If there is $$P_{2}$$ such that

$$
    P_{1}^{\mathrm{T}}P_{2}
    =
    0.
$$

Then

$$
    P^{\mathrm{T}}AQ
    =
    \left(
        \begin{array}{cc}
            D_{1} & 0
            \\
            0 & 0
        \end{array}
    \right).
$$

### proof.
Since

$$
\begin{eqnarray}
    Q^{\mathrm{T}}A^{\mathrm{T}}Q
    & = &
        \left(
            \begin{array}{c}
                Q_{1}^{\mathrm{T}}
                \\
                Q_{2}^{\mathrm{T}}
            \end{array}
        \right)
        A^{\mathrm{T}}
        \left(
            \begin{array}{cc}
                Q_{1} & Q_{2}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                Q_{1}^{\mathrm{T}}A^{\mathrm{T}}AQ_{1}
                &
                    Q_{1}^{\mathrm{T}}A^{\mathrm{T}}AQ_{2}
                \\
                Q_{2}^{\mathrm{T}}A^{\mathrm{T}}AQ_{1}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                Q_{1}^{\mathrm{T}}A^{\mathrm{T}}AQ_{1}
                &
                    Q_{1}^{\mathrm{T}}A^{\mathrm{T}}AQ_{2}
                \\
                Q_{2}^{\mathrm{T}}A^{\mathrm{T}}AQ_{1}
            \end{array}
        \right),
\end{eqnarray}
$$

we have that

$$
\begin{eqnarray}
    Q_{1}^{\mathrm{T}}A^{\mathrm{T}}AQ_{1}
    & = &
        D_{1}^{2}
    \nonumber
    \\
    (AQ_{2})^{\mathrm{T}}AQ_{2}
    & = &
        0
    \nonumber
\end{eqnarray}
$$

by comparing with $$\eqref{singular_value_decomposition_condition}$$.
In light of Corollary 5.3.2, we have obtained $$AQ_{2} = 0$$.

$$
\begin{eqnarray}
    P^{\mathrm{T}}AQ
    & = &
        \left(
            \begin{array}{c}
                P_{1}^{\mathrm{T}}
                \\
                P_{2}^{\mathrm{T}}
            \end{array}
        \right)
        A
        (Q_{1}, Q_{2})
    \nonumber
    & = &
        \left(
            \begin{array}{cc}
                P_{1}^{\mathrm{T}}AQ_{1}
                &
                    P_{1}^{\mathrm{T}}AQ_{2}
                \\
                P_{2}^{\mathrm{T}}AQ_{1}
                &
                    P_{2}^{\mathrm{T}}AQ_{2}
            \end{array}
        \right)
    \nonumber
    & = &
        \left(
            \begin{array}{cc}
                D_{1}^{-1}Q_{1}^{\mathrm{T}}A^{\mathrm{T}}AQ_{1}
                &
                    0
                \\
                P_{2}^{\mathrm{T}}P_{1}D_{1}
                &
                    0
            \end{array}
        \right)
    \nonumber
    & = &
        \left(
            \begin{array}{cc}
                D_{1}^{-1}D_{1}^{2}
                &
                    0
                \\
                (P_{1}P_{2})^{\mathrm{T}}D_{1}
                &
                    0
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                D_{1}
                &
                    0
                \\
                0
                &
                    0
            \end{array}
        \right)
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [lecture3.pdf](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-fall-2004/lecture-notes/lecture3.pdf)

