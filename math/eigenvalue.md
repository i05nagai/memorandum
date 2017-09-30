---
title: Eigenvalue
---

## Eigenvalue

## Definition1. Eigenvector and Eigenvalues
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

## Remark2
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

## Theorem3. Diagolization
* $$A \in \mathbb{C}^{n \times n}$$,
* $$x_{1}, \ldots, x_{m} \in \mathbb{C}^{n}$$,
* $$X := (x_{1}, \ldots, x_{m})$$,

$$x_{1}, \ldots, x_{m}$$ are eigenvectors are there exsists a diagonal matrix $$D := \mathrm{diag}(d_{1}, \ldots, d_{m})$$ such that

$$
    AX
    =
    XD
    .
$$

In this case, $$d_{i}$$ is a eigenvector of $$x_{i}$$.

## proof.
To show only if part,

$$
\begin{eqnarray}
    AX
    & = &
        (Ax_{1} \cdots Ax_{m})
    \nonumber
    \\
    & = &
        (\lambda_{1} x_{1} \cdots \lambda_{m} x_{m})
    \nonumber
    \\
    & = &
        (x_{1} \cdots x_{m})
        \mathrm{diag}(\lambda_{1}, \ldots, \lambda_{m})
    .
    \nonumber
\end{eqnarray}
$$

To show if part, the equation is equivalent to following equations

$$
\begin{eqnarray}
    \forall i = 1, \ldots, m,
    \
    Ax_{i}
    =
    \lambda_{i}
    x_{i}
    .
\end{eqnarray}
$$

This is the definition of eigenvectors.

<div class="end-of-statement" style="text-align: right">■</div>

## Corollary4.
Eigenvectors $$x_{1}, \ldots, x_{m}$$ are linearly independent.
Then There exists a diagonal matrix D such that

$$
    X^{-1}AX
    =
    D
$$

## proof.
By the asusmption, $X$ is nonsingular so that $X^{-1}$ exists.
<div class="QED" style="text-align: right">$\Box$</div>

## Theorem5. Linear indepence of eigenvectors
* $$A \in \mathbb{C}^{n \times n}$$,
* $$k$$,
    * number of distinct eigenvalues.
* $$\lambda_{i}\ (i= 1, \ldots, k)$$,
    * distinct eigenvalues
* $$x_{i}^{1}, \ldots, x_{i}^{m_{i}} \ (i = 1, \ldots, k)$$,
    * linearly independent eieigenvectors corresponding to eigenvalue $$\lambda_{i}$$

Then $$x_{1}^{1}, \ldots, x_{1}^{m_{1}}, \ldots, x_{k}^{1}, \ldots, x_{k}^{m_{k}}$$ are linearly independent.

## proof.
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

## Corollary6.
* $$A \in \mathbb{C}^{n \times n}$$,

Then $A$ is diagonalizable.

## proof.
By combining corollary4 and theorem5.

<div class="end-of-statement" style="text-align: right">■</div>

## Thereom7.
* $$A \in \mathbb{C}^{n \times n}$$,

Then

* There exists a nonsingular matrix $$Q := (q_{1} \ldots q_{n})$$ and $$D := \mathrm{diag}(d_{1}, \ldots, d_{n})$$ such that
    * $$Q^{-1}AQ = D$$,
* $\mathrm{rank}(A)$ equals the number of nonzero diagonal elements of $D$
* $$\mathrm{det}(A) = d_{1} \cdots d_{n}$$,
* $$\mathrm{tr}(A) = d_{1} + \cdots + d_{n}$$,
* The characteristic polynomial of $A$ is

$$
    p(\lambda)
    =
    (-1)^{n}
        (\lambda - d_{1})
        \cdots
        (\lambda - d_{n})
$$

## proof.

<div class="QED" style="text-align: right">$\Box$</div>

## Theorem 8. Orthogonal diagonalization
* $A \in \mathbb{C}^{n \times n}$
    * symmetric matrix

$A$ is orthogonally idagonalizable.

## proof.

$$
    A^{\mathrm{T}}
    =
    (
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
