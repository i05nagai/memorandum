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

#### Definition. Hermitian matrix
* $$A = (a_{j}^{i})_{i = 1, \ldots, m, j = 1, \ldots, n} \in \mathbb{C}^{m \times n}$$,
    * matrix

$A$ is a hermitian matrix iff $$A^{*} = A$$ where

$$
    A^{*} := \bar{A}^{\mathrm{T}}.
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. Singluar Value
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

#### Theorem 1
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
* $$P := (P_{1}, P_{2}) \in \mathbb{C}^{m \times m}$$,
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
    \label{singular_value_decomposition_condition_01}
\end{equation}
$$

If there is $$P_{2}$$ such that

$$
\begin{equation}
    P_{1}^{\mathrm{T}}P_{2}
    =
    0
    .
    \label{singular_value_decomposition_condition_02}
\end{equation}
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

#### proof.
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

#### Theorem2. Existence of singular values
* $$A \in \mathbb{C}^{m \times n}$$,
    * rank $r$

Then there are $$Q_{1}$$, $$D_{1}$$ and $$P_{2}$$ such that

* $$Q_{1} \in \mathbb{C}^{n \times r}$$,
* $$Q_{2} \in \mathbb{C}^{n \times (n - r)}$$,
* $$Q := (Q_{1}, Q_{2}) \in \mathbb{C}^{n \times n}$$,
    * orthogonal matrix
* $$P_{1} := AQ_{1}D_{1}^{-1} \in \mathbb{C}^{m \times r}$$,
* $$P_{2} \in \mathbb{C}^{m \times (m - r)}$$,

and satisfy $$\eqref{singular_value_decomposition_condition_01}$$ and $$\eqref{singular_value_decomposition_condition_02}$$.

#### proof.
Existence of $Q$ is direct consequence from eigenvalue decomposition.
Since $A^{\mathrm{T}}A$ is $n \times n$ symmetric matrix, we can diagonalize $A^{\mathrm{T}}A$ by <a href="{{ site.baseurl }}/math/eigenvalue.html">threorem</a>.
Thus there are diagonal matrix $D^{\prime}$ and orthogonal matrix $Q$ such that $Q^{\mathrm{T}}A^{\mathrm{T}}AQ = D^{\prime}$.
$$A^{\mathrm{T}}A$$ is nonnegative definite since

$$
\begin{eqnarray}
    x^{\mathrm{T}}A^{\mathrm{T}}Ax
    & = &
        (Ax)^{\mathrm{T}}Ax
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            b_{i}^{2}
        \ge 0
    \nonumber
\end{eqnarray}
$$

where $$b^{i} := \sum_{j=1}^{n}a_{j}^{i}x^{j}$$.
Then all eigenvalues are nonnegative, that is, $$D^{\prime} = \mathrm{diag}(d_{1}, \ldots, d_{r}, 0, \ldots, 0)$$ where $$d_{1}, \ldots, d_{r} \ge 0$$.
Let $$s_{i} := \sqrt{d_{i}}$$ and $$D_{1} := \mathrm{diag}(s_{1}, \ldots, s_{r})$$.
We have

$$
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
    \right)
    .
$$

The existence of $$P_{2}$$ is easy to obtain by defining $$P_{1} := AQ_{1}D_{1}^{-1}$$ and $$P_{2} := AQ_{1}D_{1}^{-1}$$.
We obtain

$$
    P_{1}^{\mathrm{T}}P_{2}
    =
    D_{1}^{-1}Q_{1}^{\mathrm{T}}A^{\mathrm{T}}
    AQ_{1}D_{1}^{-1}
    =
    D_{1}^{-1}
    (D_{1})^{2}
    D_{1}^{-1}
    =
    I_{n}
    .
$$

Hence by the theorem. singular value decomposition of $A$ exists.

<div class="QED" style="text-align: right">$\Box$</div>

## Algorithms
There are a lot of algorithms to compute SVD.

#### Algorithm Golub-Kahan SVD Diagonalization
By applying Householder Bidiagonalization algorithm to $A \in \mathbb{R}^{m \times n}$, we obtain bidiagonal matrix $B \in \mathbb{R}^{m \times n}$.
Then we apply symmetric QR algorithm to tridiagonal matrix $T := B^{\mathrm{T}}B$.

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{ComputeGolub-KahanSVDDiagonalization}
    \begin{algorithmic}
    \REQUIRE $A \in \mathbb{R}^{m \times n}$
    \REQUIRE $m \ge n$
    \PROCEDURE{ComputeGolub-KahanSVDDiagonalization}{$A$}
        \STATE $B \leftarrow \mathrm{ComputeHouseholderBidiagonalization}(A)$,
        \STATE $\mu$
        \STATE $y \leftarrow t_{11} - \mu$
        \STATE $z \leftarrow t_{12}$
        \FOR{$k = 1$ \TO $n-1$}
            \STATE $(c, s) \leftarrow \mathrm{ComputeGivensRotation}(y, z)$
            \STATE $B \leftarrow B G(k, k + 1, c, s; n)$,
            \STATE $y \leftarrow b_{k}^{k}$
            \STATE $z \leftarrow b_{k}^{k+1}$
            \STATE $(c, s) \leftarrow \mathrm{ComputeGivensRotation}(y, z)$
            \STATE $B \leftarrow G(k, k + 1, c, s; m)^{\mathrm{T}}B$,
            \IF{$k < n - 1$}
                \STATE $y \leftarrow b_{k+1}^{k}$
                \STATE $z \leftarrow b_{k+2}^{k}$
            \ENDIF
        \ENDFOR
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

#### Algorithm Golub-Kahan SVD
* $U$,
    * orthogonal
* $V$,
    * orthogonal
* $D \in \mathbb{R}^{m \times n}$,
    * diagonal
* $E$,
    * $$\norm{E}_{2} \approx u \norm{A}_{2}$$ for some $u > 0$

$$
\begin{eqnarray}
    U^{\mathrm{T}}AV
    =
    D + E
    .
    \nonumber
\end{eqnarray}
$$

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{ComputeGolub-KahanSVD}
    \begin{algorithmic}
    \REQUIRE $A \in \mathbb{R}^{m \times n}$
    \REQUIRE $m \ge n$
    \REQUIRE $B \in \mathbb{R}^{n \times n}$
    \PROCEDURE{ComputeGolub-KahanSVD}{$A$}
        \STATE $\left(
            \begin{array}{c}
                B \\
                0
            \end{array}
        \right) \leftarrow \mathrm{ComputeHouseholderBidiagonalization}(A)$
        \WHILE{$q \neq 1$}
            \FOR{$i = 1$ \TO $n - 1$}
                \IF{$|b_{i+1}^{i}| < \epsilon (|b_{i}^{i}| + |b_{i+1}^{i+1}|)$}
                    \STATE $b_{i+1}^{i} \leftarrow 0$
                \ENDIF
            \ENDFOR
            \STATE $B \leftarrow B G(k, k + 1, c, s; n)$,
            \STATE $(c, s) \leftarrow \mathrm{ComputeGivensRotation}(y, z)$
            \STATE $B \leftarrow G(k, k + 1, c, s; m)^{\mathrm{T}}B$
            \IF{$k < n - 1$}
                \STATE $y \leftarrow b_{k+1}^{k}$
                \STATE $z \leftarrow b_{k+2}^{k}$
            \ENDIF
        \ENDWHILE
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [lecture3.pdf](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-fall-2004/lecture-notes/lecture3.pdf)
* Harville, David A. Matrix algebra from a statistician's perspective. Vol. 1. New York: Springer, 1997.
