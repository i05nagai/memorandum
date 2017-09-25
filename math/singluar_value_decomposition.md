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
    \\
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
    \\
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
    \\
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

## Theorem.
* $$A \in \mathbb{C}^{n \times n}$$,
* $$k$$,
    * number of distinct eigenvalues.
* $$\lambda_{i}\ (i= 1, \ldots, k)$$,
    * distinct eigenvalues
* $$x_{i}^{1}, \ldots, x_{i}^{m_{i}} \ (i = 1, \ldots, k)$$,
    * linearly independent eieigenvectors corresponding to eigenvalue $$\lambda_{i}$$

Then $$x_{1}^{1}, \ldots, x_{1}^{m_{1}}, \ldots, x_{k}^{1}, \ldots, x_{k}^{m_{k}}$$ are linearly independent.

## Proof.
We prove by mathematical induction with respect to the number of eigenvalues.
$$x_{1}^{1}, \ldots, x_{1}^{m_{1}}$$ are linearlY independent by definition.
Suppose that the set of first $$\sum_{i=1}^{s}m_{i}$$ eigenvectors $$x_{1}^{1}, \ldots, x_{1}^{m_{1}}, \ldots, x_{s}^{1}, \ldots, x_{s}^{m_{s}}$$ are linear independent for $s \le k - 1$.
It suffices to show that the set first $$\sum_{i=1}^{s+1} m_{i}$$ eigenvectors is linearly independent.

We prove this by contradiction.
Let us assume that the set of eigenvectors is not linearly independent.
Then there is a set of scalars $$c_{1}^{1}, \ldots, c_{1}^{m_{1}}, \ldots, c_{s+1}^{1}, \ldots, c_{s+1}^{m_{s+1}}$$ such that

$$
\begin{equation}
    \sum_{i=1}^{s + 1}
        \sum_{j=1}^{m_{i}}
            c_{i}^{j}x_{i}^{j}
    =
    0.
    \label{04_01_proof}
\end{equation}
$$

and for some $i^{\prime}$ such that $$c_{i^{\prime}} \neq 0$$.
We observe that

$$
    \forall j = 1, \ldots, m_{s+1}
    \
    (A - \lambda_{s+1}I)x_{s+1}^{j}
    =
    0
$$

and

$$
\begin{eqnarray}
    \forall i = 1, \ldots, s,
    \
    \forall j = 1, \ldots, m_{i},
    \
    (A - \lambda_{s+1}I)x_{i}^{j}
    & = &
        (A - \lambda_{i}I + \lambda_{i}I - \lambda_{s+1}I)x_{i}^{j}
    \nonumber
    \\
    & = &
        (\lambda_{i}I - \lambda_{s+1}I)x_{i}^{j}
    \nonumber
    \\
    & = &
        (\lambda_{i} - \lambda_{s+1})x_{i}^{j}
\end{eqnarray}
$$

Multiplying both sides of $$A - \lambda_{s+1}$$

$$
\begin{eqnarray}
    (A - \lambda_{s+1})
    \sum_{i=1}^{s}
        \sum_{j=1}^{m_{i+1}}
            c_{i}^{j}x_{i}^{j}
    & = &
        0
    \nonumber
    \\
    \sum_{i=1}^{s+1}
        (\lambda_{i} - \lambda_{s+1})
        \left(
            \sum_{j=1}^{m_{i+1}}
                c_{i}^{j}x_{i}^{j}
        \right)
    & = &
        0
    \nonumber
    \\
    \sum_{i=1}^{s}
        (\lambda_{i} - \lambda_{s+1})
        \left(
            \sum_{j=1}^{m_{i+1}}
                c_{i}^{j}x_{i}^{j}
        \right)
    & = &
        0
    .
\end{eqnarray}
$$

Since eigenvalues are distinct and by assumption of the mathematical induction $$x_{1}^{1}, \ldots, x_{1}^{m_{1}}, \ldots, x_{s}^{1}, \ldots, x_{s}^{m_{s}}$$ are linearly induction, it follows that

$$
    \forall i = 1, \ldots, s,
    \
    \forall j = 1, \ldots, m_{s},
    \
    c_{i}^{j}
    =
    0
    .
$$

Substitutiong the above into equality into the equation, we find that

$$
    \sum_{j=1}^{m_{s+1}}
        c_{s+1}^{j}x_{s+1}^{j}
    =
    0
    .
$$

Since $$x_{s+1}^{1}, \ldots, x_{s+1}^{m_{s+1}}$$ are lineraly independent by definition, $$c_{s+1}^{1}, \ldots, c_{s+1}^{m_{s+1}} = 0$$.
This is contradiction.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [lecture3.pdf](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-fall-2004/lecture-notes/lecture3.pdf)

