---
title: Eigenvalue
---

## Eigenvalue

#### Definition1. Eigenvector and Eigenvalues
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

#### Remark2
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

#### Theorem3. Diagolization
* $$A \in \mathbb{C}^{n \times n}$$,
* $$x_{1}, \ldots, x_{m} \in \mathbb{C}^{n}$$,
* $$X := (x_{1}, \ldots, x_{m})$$,

$$x_{1}, \ldots, x_{m}$$ are eigenvectors.
There exsists a diagonal matrix $$D := \mathrm{diag}(d_{1}, \ldots, d_{m})$$ such that

$$
    AX
    =
    XD
    .
$$

In this case, $$d_{i}$$ is a eigenvector of $$x_{i}$$.

#### proof.
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

#### Corollary4.
Eigenvectors $$x_{1}, \ldots, x_{m}$$ are linearly independent.
Then There exists a diagonal matrix D such that

$$
    X^{-1}AX
    =
    D
$$

#### proof.
By the asusmption, $X$ is nonsingular so that $X^{-1}$ exists.
<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem5. Linear indepence of eigenvectors
* $$A \in \mathbb{C}^{n \times n}$$,
* $$k$$,
    * number of distinct eigenvalues.
* $$\lambda_{i}\ (i= 1, \ldots, k)$$,
    * distinct eigenvalues
* $$x_{i}^{1}, \ldots, x_{i}^{m_{i}} \ (i = 1, \ldots, k)$$,
    * linearly independent eieigenvectors corresponding to eigenvalue $$\lambda_{i}$$

Then $$x_{1}^{1}, \ldots, x_{1}^{m_{1}}, \ldots, x_{k}^{1}, \ldots, x_{k}^{m_{k}}$$ are linearly independent.

#### proof.
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

Substitutiong the above equality into the equation, we find that

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

#### Corollary6.
* $$A \in \mathbb{C}^{n \times n}$$,

Then $A$ is diagonalizable.

#### proof.
By combining corollary4 and theorem5.

<div class="end-of-statement" style="text-align: right">■</div>

#### Thereom7.
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

#### proof.
From THereom 21.5.1 in Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.



<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem8.
* $A \in \mathbb{C}^{n \times n}$

Then $$\exists x_{1}, x_{2}$$ such that

$$
\begin{eqnarray}
    & &
        x_{1}
        \neq
        0
        ,
        \
        x_{2}
        \neq
        0
    \nonumber
    \\
    \forall x \in \mathbb{R}^{n},
    \
    x \neq 0,
    \
    & &
        \lambda(x_{1}, A)
        :=
        \frac{
            x_{1}^{\mathrm{T}}Ax_{1}
        }{
            x_{1}^{\mathrm{T}}x_{1}
        }
        \le
        \frac{
            x^{\mathrm{T}}Ax
        }{
            x^{\mathrm{T}}x
        }
        \le
        \frac{
            x_{2}^{\mathrm{T}}Ax_{2}
        }{
            x_{2}^{\mathrm{T}}x_{2}
        }
        =:
        \lambda(x_{2}, A)
\end{eqnarray}
$$

Moreover, if $A$ is symmetric, $$\lambda(x_{1}, A)$$ and $$\lambda(x_{2}, A)$$ is smallest and largest eigenvalus of $A$ respectively.
$$x_{1}$$ and $$x_{2}$$ are eigenvectors corresponding to the eigenvalues.

#### proof.
From Theorem 21.5.6 in Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.

$$

$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem9. Existence of eigenvalue
* $A \in \mathbb{C}^{n \times n}$
    * symmetric matrix

Then $A$ has an eigenvalue.

#### proof.
From Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.


<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem10. Orthogonal diagonalization
* $A \in \mathbb{C}^{n \times n}$
    * symmetric matrix

$A$ is orthogonally dagonalizable.

#### proof.
From Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.

We prove this by mathematical induction.
Every $1 \times 1$ matrix is orthogonaly diagonalizable.
Suppose that $(n-1) \times (n-1)$ symmetric matrix is orthogonally diagonalizable where $n \ge 2$.
Let $A$ be $n \times n$ symmetric matrix.
Let $\lambda$, $u$ be eigenvalue of $A$ and eigenvector of norm 1 corresponding to $\lambda$.
By gram schmidt orthogonalization, there is a matrix $$V := (v_{i})_{i=2, \ldots, n} \in \mathbb{C}^{n \times (n - 1)}$$ which is orthogonal to $u$.
Since

$$
    u^{\mathrm{T}}V
    =
    0 \in \mathbb{C}^{1 \times (n - 1)}
    ,
$$

then

$$
\begin{eqnarray}
    (u, V)^{\mathrm{T}}A(u, V)
    & = &
        (u, V)^{\mathrm{T}}(Au, AV)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                u^{\mathrm{T}}Au
                &
                    u^{\mathrm{T}}AV
                \\
                V^{\mathrm{T}}Au
                &
                    V^{\mathrm{T}}AV
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                u^{\mathrm{T}}\lambda u
                &
                    (\lambda u)^{\mathrm{T}}V
                \\
                V^{\mathrm{T}}\lambda u
                &
                    V^{\mathrm{T}}AV
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                \lambda
                &
                    0
                \\
                    0
                &
                    V^{\mathrm{T}}AV
            \end{array}
        \right)
    \nonumber
    .
\end{eqnarray}
$$

Since $V^{\mathrm{T}}AV$ is $(n -1) \times (n -1)$ symmetric matrix so that by assumption there exists orthogonal matrix $R \in \mathbb{C}^{(n - 1) \times (n - 1)}$ such that $$R^{\mathrm{T}}(V^{\mathrm{T}}V)R = \mathrm{diag}(d_{2}, \ldots, d_{n})$$.
Define

$$
\begin{eqnarray}
    S
    & := &
        \left(
            \begin{array}{cc}
                1
                &
                    0
                \\
                0
                &
                    R
            \end{array}
        \right)
    \nonumber
    \\
    P
    & := &
        (u, V)S
    .
    \nonumber
\end{eqnarray}
$$

Then,

$$
\begin{eqnarray}
    S^{\mathrm{T}}S
    & = &
        \left(
            \begin{array}{cc}
                1
                &
                    0
                \\
                0
                &
                    R^{\mathrm{T}}R
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                1
                &
                    0
                \\
                0
                &
                    I_{n-1}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        I_{n}
\end{eqnarray}
$$

so that $S$ is orthogonal.
Moreover $P$ is orthogonal since $(u, V)$ is orthogonal, that is,

$$
\begin{eqnarray}
    P^{\mathrm{T}}P
    & = &
        S^{\mathrm{T}}(u, V)^{\mathrm{T}}(u, V)S
    \nonumber
    \\
    & = &
        S^{\mathrm{T}}I_{n}S
    \nonumber
    \\
    & = &
        I_{n}
    .
    \nonumber
\end{eqnarray}
$$

Further,

$$
\begin{eqnarray}
    P^{\mathrm{T}}AP
    & = &
        S^{\mathrm{T}}(u, V)^{\mathrm{T}}A(u, V)S
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                1
                &
                    0
                \\
                0
                &
                    R
            \end{array}
        \right)
        ^{\mathrm{T}}
        \left(
            \begin{array}{cc}
                \lambda
                &
                    0
                \\
                0
                &
                    V^{\mathrm{T}}AV
            \end{array}
        \right)
        \left(
            \begin{array}{cc}
                1
                &
                    0
                \\
                0
                &
                    R
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                \lambda
                &
                    0
                \\
                0
                &
                    R^{\mathrm{T}}V^{\mathrm{T}}AVR
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                \lambda
                &
                    0
                \\
                0
                &
                    \mathrm{diag}(d_{2}, \ldots, d_{n})
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

so that $P^{\mathrm{T}}AP$ euqals a diagonal matrix.
Therefore $A$ is orthogonally diagonalizable.

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary11
* $A$
    * $n \times n$ symmetric matrix
* $$d_{1}, \ldots, d_{n}$$,
    * not necessarily distinct eigenvalues of $A$

Then there exists $n \times n$ orthogonal matrix $Q$ such that

$$
    Q^{\mathrm{T}}AQ
    =
    \mathrm{diag}(d_{1}, \ldots, d_{n})
$$

#### proof.
From Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.

Accoding to <a href="#theorem10-orthogonal-diagonalization">theorem10</a>,


<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 12
* $A \in \mathbb{R}^{n \times n}$,
* $B \in \mathbb{R}^{n \times n}$,
    * positive definite so that its inverse exists
* $\lambda_{i}(A)$,
    * $i$-th largest eivenvalue of $A$,
* $$\lambda(A) := \{\lambda_{i}(A)\}_{i}$$,

(1)

$$
    \lambda_{i}(E - A)
    =
    1
    -
    \lambda_{i}(A)
    .
$$

(2)

$$
    \lambda_{i}(B^{-1})
    =
    \frac{
        1
    }{
        \lambda_{n - i}(B)
    }
    .
$$

(3) $c > 0$,

$$
    \lambda_{i}(cA)
    =
    c \lambda_{i}(B)
    .
$$

(4) $k \in \mathbb{N}$,

$$
    \lambda_{i}(B^{k/2})
    =
    \lambda_{i}(B)^{k/2}
    .
$$

(5)



#### proof
(1)

If all eigenvalues are distinct,

$$
\begin{eqnarray}
    (E - A)x
    & = &
        x
        -
        Ax
    \nonumber
    \\
    & = &
        x
        -
        \lambda_{i}(A)x
    \nonumber
    \\
    & = &
        (1 - \lambda_{i}(A))x
    .
    \nonumber
\end{eqnarray}
$$

(2)

$$
\begin{eqnarray}
    (E - A)x
    & = &
        x
        -
        Ax
    \nonumber
    \\
    & = &
        x
        -
        \lambda_{i}(A)x
    \nonumber
    \\
    & = &
        (1 - \lambda_{i}(A))x
    .
    \nonumber
\end{eqnarray}
$$

(3)

(4)

Let $VDV^{-1}$ be diagonalization of $B$.

$$
\begin{eqnarray}
    D
    & = &
        \mathrm{diag}(\lambda_{1}(B), \ldots, \lambda_{n}(B))
    \nonumber
    \\
    D^{k/2}
    & = &
        \mathrm{diag}(\lambda_{1}(B)^{k/2}, \ldots, \lambda_{n}(B)^{k/2})
    \nonumber
    .
\end{eqnarray}
$$

Then

$$
\begin{eqnarray}
    B^{k/2}
    & = &
        VD^{k/2}V^{-1}
    .
    \nonumber
\end{eqnarray}
$$

Since eigenvalues of $$VD^{k/2}V^{-1}$$ is equals to $D^{k/2}$,

$$
\begin{eqnarray}
    \lambda_{i}(VD^{k/2}V^{-1})
    & = &
        \lambda_{i}(B)^{k/2}
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Remark
In general, there is no relation between eigenvalues of product of matrix $\lambda(AB)$ and eigenvalues of $\lambda(A)$ and $\lambda(B)$.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.

