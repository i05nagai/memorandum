---
title: QR decomposition
---

## QR decomposition
It is also called QR factorization.

* $$[1:n] := \{1, \ldots, n\}$$,

#### Definition1 QR decomposition
* $m \ge n$,
    * assumption
* $A \in \mathbb{R}^{m \times n}$,
* $Q \in \mathbb{R}^{m \times m}$,
    * orthogonal
* $R \in \mathbb{R}^{m \times n}$,
    * upper triangular

$$
    A
    =
    QR
    .
$$

The decomposition is called QR decomposition.

<div class="end-of-statement" style="text-align: right">■</div>

QR decomposition can be used to solve systems of linear equations.

$$
\begin{eqnarray}
    & &
        Ax
        =
        b
    \nonumber
    \\
    & \Leftrightarrow &
        Rx
        =
        Q^{\mathrm{T}}
        b
    \nonumber
\end{eqnarray}
$$

The number of the operations of QR decomposition is twice as many operations as LU decomposition.
However, QR decomposition can be updated more efficiently in particular cases.
Let $A = QR$.
Then QR decomposition of $A^{\prime}$ defined below is given as follows.

$$
\begin{eqnarray}
    A^{\prime}
    & := &
        A + s \otimes t
    \nonumber
    \\
    A^{\prime}
    & = &
        Q^{\prime}
        R^{\prime}
    \nonumber
    \\
    & = &
        Q
        \left(
            R
            +
            u \otimes v
        \right)
    \nonumber
    \\
    t
    & := &
        v
    \nonumber
    \\
    u
    & := &
        Q^{\mathrm{T}}s
    \nonumber
\end{eqnarray}
$$

There are various alogirhtm to decompose $A$ into $QR$.

* Householder QR
* Block Householder Householder QR
* Givens QR
* Hessenberg QR visa Givens
* Fast Givens QR
* Gram-Schmidt
* Modified Gram-Schmnit

## Householder QR

#### Algorithm 2

Let $A \in \mathbb{R}^{m \times n}$.
A few steps of Householder QR algorithm are as follows;

$$
\begin{eqnarray}
    A^{(1)}
    & := &
        A
    \nonumber
    \\
    & = &
        (a_{1}, \ldots, a_{n})
    \nonumber
    \\
    x^{(1)}
    & := &
        a_{1}^{1:m, (1)}
        \in \mathbb{R}^{m}
    \nonumber
    \\
    (v^{(1)}, \beta^{(1)})
    & := &
        \mathrm{Householder}(x^{(1)})
    \nonumber
    \\
    P_{v^{(1)}, \beta^{(1)}}A^{(1)}
    & := &
        I_{m}
        -
        \beta^{(1)} v^{(1)}(v^{(1)})^{\mathrm{T}}
        \in \mathbb{R}^{m \times m}
    \nonumber
    \\
    H^{(1)}
    & := &
        \mathrm{diag}(I_{1 - 1}, P_{v^{(1)}, \beta^{(1)}})
    \nonumber
    \\
    & = &
        P_{v^{(1)}, \beta^{(1)}}
    \nonumber
    \\
    A^{(1 + 1)}
    & := &
        H^{(1)}A^{(1)}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{ccccc}
                a_{1}^{1,(2)}  & a_{2}^{1,(2)} & \cdots &   & a_{n}^{1,(2)}
                \\
                0  & a_{2}^{2, (2)}  &    & \cdots & \vdots
                \\
                \vdots &    &    & \ddots &
                \\
                0 & \vdots & \ddots & \ddots & 
                \\
                0 & a_{2}^{m, (2)} &        &   &  a_{n}^{m, (2)}
            \end{array}
        \right)
    \nonumber
    \\
    x^{(2)}
    & := &
        a_{2}^{2:m, (2)}
        \in \mathbb{R}^{m-1}
    \nonumber
    \\
    (v^{(2)}, \beta^{(2)})
    & := &
        \mathrm{Householder}(x^{(2)})
    \nonumber
    \\
    H^{(2)}
    & := &
        \mathrm{diag}(I_{1}, P_{v^{(2)}, \beta^{(2)}})
    \nonumber
    \\
    A^{(3)}
    & := &
        H^{(2)}
        A^{(2)}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{ccccc}
                a_{1}^{1,(3)}  & a_{2}^{1,(3)} & \cdots &   & a_{n}^{1,(3)}
                \\
                0  & a_{2}^{2, (3)}  &  a_{2}^{2,(3)}  & \cdots & \vdots
                \\
                \vdots & 0 & \ddots & \ddots &
                \\
                0 & \vdots & \ddots & \ddots & 
                \\
                0 & 0 & a_{3}^{m, (3)} & \cdots  &  a_{n}^{m, (3)}
            \end{array}
        \right)
    \nonumber
    \\
    & \vdots &
    \nonumber
\end{eqnarray}
$$

The above provedure generates $H^{(1)}, \cdots, H^{(n)}$.
Let $R := A^{(n)}$ and $Q := H^{(1)} \cdots H^{(n)}$.
By proposition, $H^{(i)}$ is orthonomal and symmetric.
Thus, $Q$ is orthonomal and symmetric as well.
By construction, $A^{(n)}$ is upper triangular matrix.

$$
\begin{eqnarray}
    & &
        R
        =
        H^{(n)} \cdots H^{(1)} A
    \nonumber
    \\
    & \Leftrightarrow &
        Q R
        =
        A
    .
    \nonumber
\end{eqnarray}
$$

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Householder QR}
    \begin{algorithmic}
    \REQUIRE $A \in \mathbb{R}^{m \times n}$
    \REQUIRE $m \ge n$
    \PROCEDURE{HouseholderQR}{$A$}
        \FOR{$j = 1$ \TO $n$}
            \STATE $(v, \beta) \leftarrow \mathrm{ComputeHouseholderVector}(A_{j}^{j:m})$
            \STATE $A_{j:n}^{j:m} \leftarrow (I_{m - j + 1} - \beta v v^{\mathrm{T}}) A_{j:n}^{j:m}$
            \COMMENT{$2(m-(j-1)) (n - (j - 1)) (m - (j - 1))$ flops}
            \IF{$j < m$}
                \STATE $A_{j}^{(j+1):m} \leftarrow v^{2:(m-j+1)}$
            \ENDIF
        \ENDFOR
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

where `ComputeHouseholderVector` is defined on <a href="{{ site.baseurl }}/math/matrix/householder_transformation.html">Householder Transformation</a>.
Time complexity of the algorithm is $O(n^{2}m)$, more precicely $2n^{2}(m - n/3)$.
$A$ is overwritten like

$$
    A
    =
    \left(
        \begin{array}{ccccc}
            r_{1}^{1}     & r_{2}^{1}     & \cdots &              & r_{n}^{1}
            \\
            v^{2,(1)}   & r_{2}^{2}     &        & \cdots       & \vdots
            \\
            \vdots        & v^{3,(2)}   &        & \ddots       &
            \\
            v^{m-1,(1)} & v^{m-1,(2)} & \ddots & \ddots       & r_{m-1}^{n}
            \\
            v^{m,(1)}   & v^{m,(2)}   &        & v^{m,(n-1)} & v^{m,(n)}
        \end{array}
    \right)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Algorithm 3

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{ComputeFactoredForm}
    \begin{algorithmic}
    \REQUIRE $A \in \mathbb{R}^{m \times n}$
    \REQUIRE $m \ge n$
    \REQUIRE $r := \mathrm{rank}(A)$
    \PROCEDURE{ComputeFactoredForm}{$A$}
        \STATE $Q \leftarrow I_{n}$
        \FOR{$j = r - 1$ \TO $0$} 
            \STATE $v^{j:n} \leftarrow \left(
                    \begin{array}{c}
                        1
                        \\
                        A_{j}^{(j+1):n}
                    \end{array}
                \right)$
            \STATE $Q_{j:n}^{j:n} \leftarrow (I_{n} - \beta_{j}v^{j:n}(v^{j:n})^{\mathrm{T}}Q_{j:n}^{j:n}$
        \ENDFOR
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>


<div class="end-of-statement" style="text-align: right">■</div>

## Householder QR with Column Pivoting
If $A$ is not full-rank,

$$
\begin{eqnarray}
    A^{(1)}
    & := &
        A\Pi^{(1)}
    \nonumber
    \\
    x^{(1)}
    & := &
        a_{1}^{1:m, (1)}
        \in \mathbb{R}^{m}
    \nonumber
    \\
    (v^{(1)}, \beta^{(1)})
    & := &
        \mathrm{Householder}(x^{(1)})
    \nonumber
    \\
    P_{v^{(1)}, \beta^{(1)}}A^{(1)}
    & := &
        I_{m}
        -
        \beta^{(1)} v^{(1)}(v^{(1)})^{\mathrm{T}}
        \in \mathbb{R}^{m \times m}
    \nonumber
    \\
    H^{(1)}
    & := &
        \mathrm{diag}(I_{1 - 1}, P_{v^{(1)}, \beta^{(1)}})
    \nonumber
    \\
    & = &
        P_{v^{(1)}, \beta^{(1)}}
    \nonumber
    \\
    A^{(1 + 1)}
    & := &
        H^{(1)}A^{(1)}\Pi^{(2)}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{ccccc}
                a_{1}^{1,(2)}  & a_{2}^{1,(2)} & \cdots &   & a_{n}^{1,(2)}
                \\
                0  & a_{2}^{2, (2)}  &    & \cdots & \vdots
                \\
                \vdots &    &    & \ddots &
                \\
                0 & \vdots & \ddots & \ddots & 
                \\
                0 & a_{2}^{m, (2)} &        &   &  a_{n}^{m, (2)}
            \end{array}
        \right)
    \nonumber
    \\
    x^{(2)}
    & := &
        a_{2}^{2:m, (2)}
        \in \mathbb{R}^{m-1}
    \nonumber
    \\
    (v^{(2)}, \beta^{(2)})
    & := &
        \mathrm{Householder}(x^{(2)})
    \nonumber
    \\
    H^{(2)}
    & := &
        \mathrm{diag}(I_{1}, P_{v^{(2)}, \beta^{(2)}})
    \nonumber
    \\
    A^{(3)}
    & := &
        H^{(2)}
        A^{(2)}
        \Pi^{(3)}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{ccccc}
                a_{1}^{1,(3)}  & a_{2}^{1,(3)} & \cdots &   & a_{n}^{1,(3)}
                \\
                0  & a_{2}^{2, (3)}  &  a_{2}^{2,(3)}  & \cdots & \vdots
                \\
                \vdots & 0 & \ddots & \ddots &
                \\
                0 & \vdots & \ddots & \ddots & 
                \\
                0 & 0 & a_{3}^{m, (3)} & \cdots  &  a_{n}^{m, (3)}
            \end{array}
        \right)
    \nonumber
    \\
    & \vdots &
    \nonumber
    \\
    A^{(n+1)}
    & := &
        H^{(n)}
        A^{(n)}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{ccccc}
                a_{1}^{1,(3)}  & a_{2}^{1,(3)} & \cdots &   & a_{n}^{1,(3)}
                \\
                0  & a_{2}^{2, (3)}  &  a_{2}^{2,(3)}  & \cdots & \vdots
                \\
                \vdots & 0 & \ddots & \ddots &
                \\
                0 & \vdots & \ddots & \ddots & 
                \\
                0 & 0 & \cdots & 0  &  a_{n}^{m, (3)}
            \end{array}
        \right)
\end{eqnarray}
$$

where $\Pi^{(i)}$ is a permutation matrix.

$$
\begin{eqnarray}
    Q
    & := &
        H^{(1)} \cdots H^{(n)}
    \nonumber
    \\
    R
    & := &
        A^{(n+1)}
    \nonumber
    \\
    Z
    & := &
        \Pi^{(1)}\cdots\Pi^{(n)}
    \nonumber
    \\
    & &
        A^{(n+1)}
        =
        H^{(n)} \cdots H^{(1)}
        A
        \Pi^{(1)}\cdots\Pi^{(n)}
    \nonumber
    \\
    & \Leftrightarrow &
        R
        =
        Q^{\mathrm{T}}
        A
        Z
    \nonumber
    \\
    & \Leftrightarrow &
        Q
        R
        =
        A
        Z
    .
    \nonumber
\end{eqnarray}
$$

We discuss how we can determine the permutation matrice.
Let

$$
\begin{eqnarray}
    A^{(k)}
    & = &
        \left(
            \begin{array}{cc}
                a_{1:(m-k+1)}^{1:(k-1), (k)}
                &
                    a_{k:(n-k+1)}^{1:(k-1), (k)}
                \\
                0
                &
                    a_{k:(n-k+1)}^{k:(m-k+1), (k)}
            \end{array}
        \right)
    .
    \nonumber
\end{eqnarray}
$$

If $k - 1 = \mathrm{rank}(A)$,

$$
\begin{eqnarray}
    \norm{
        a^{k:(m-k+1), (k)}
    }_{\infty}
    & := &
        \max
        \left\{
            \norm{
                a_{k}^{k:(m-k+1), (k)}
            }_{2},
            \cdots,
            \norm{
                a_{n}^{k:(m-k+1), (k)}
            }_{2}
        \right\}
    \nonumber
    \\
    p^{(k)}
    & := &
        \arg
        \max_{p \ge k}
        \left\{
            \norm{
                a_{p}^{k:(m-k+1), (k)}
            }_{2}
        \right\}
    \nonumber
\end{eqnarray}
$$

is zero.
Otherwise, let $\Pi^{(k)}$ be the permutation matrix with columns $p^{(k)}$ and $k$ interchanged.

#### Algorithm

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Householder QR with column pivotting}
    \begin{algorithmic}
    \REQUIRE $A \in \mathbb{R}^{m \times n}$
    \REQUIRE $m \ge n$
    \REQUIRE $r := \mathrm{rank}(A)$
    \PROCEDURE{HouseholderQRWithPivotting}{$A$}
        \FOR{$j = 1$ \TO $n$}
            \STATE $c^{j} \leftarrow A_{j}^{1:m}$
        \ENDFOR
        \STATE $r \leftarrow 0$
        \STATE $\tau \leftarrow \max\{c^{1}, \ldots, c^{n}\}$
        \STATE $k \leftarrow \arg\min\{k^{\prime} \in [1:n] \mid c^{k^{\prime}} = \tau\}$
        \WHILE{$\tau > 0$} 
            \STATE $r \leftarrow r + 1$
            \STATE $p^{r} = k$
            \STATE $\mathrm{swap}(A_{r}^{1:m}, A_{k}^{1:m})$
            \STATE $\mathrm{swap}(c^{r}, c^{k})$
            \STATE $(v, \beta) \leftarrow \mathrm{ComputeHouseholderVector}(A_{r}^{r:m})$
            \STATE $A_{r:n}^{r:m} \leftarrow (I_{m-r+1} - \beta v v^{\mathrm{T}}) A_{r:n}^{r:m}$
            \STATE $A_{r}^{(r+1):m} \leftarrow v^{2:(m-r+1)}$
            \FOR{$r+1$ \TO $n$}
                \STATE $c^{i} \leftarrow c^{i} - (A_{i}^{r})^{2}$
            \ENDFOR
            \IF{$r < n$}
                \STATE $\tau \leftarrow \max\{c^{r+1}, \ldots, c^{n}\}$
                \STATE $k \leftarrow \arg\min\{k^{\prime} \in [r+1:n] \mid c^{k^{\prime}} = \tau\}$
            \ELSE
                \STATE $\tau \leftarrow 0$
            \ENDIF
        \ENDWHILE
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

## Givens QR
See <a href="{{ site.baseurl }}/math/matrix/givens_rotation.html">Givens Rotation</a>.
Givens Rotation can zero one elment in a matrix by applying Givens Rotation.
Let $A \in \mathbb{R}^{m \times n}$.

$$
\begin{eqnarray}
    A
    & = &
        \left(
            \begin{array}{ccccc}
                \times   & \times & \cdots & \times & \times
                \\
                   &    &    & \cdots & \vdots
                \\
                \vdots &    &    & \ddots &
                \\
                    & \vdots & \ddots & \ddots & 
                \\
                \times  & \cdots &        &   & \times
            \end{array}
        \right)
    \nonumber
    \\
    A^{(1)}
    & := &
        G(m-1, m, \theta)^{\mathrm{T}}A
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{ccccc}
                \times   & \times & \cdots & \times & \times
                \\
                   &    &    & \cdots & \vdots
                \\
                \vdots &    &    & \ddots &
                \\
                \times    & \vdots & \ddots & \ddots & 
                \\
                0  & \times &        &   & \times
            \end{array}
        \right)
    \nonumber
    \\
    G(m-2, m-1, \theta)^{\mathrm{T}}A^{(1)}
    & = &
        \left(
            \begin{array}{ccccc}
                \times   & \times & \cdots & \times & \times
                \\
                   &    &    & \cdots & \vdots
                \\
                \times &    &    & \ddots &
                \\
                0    & \vdots & \ddots & \ddots & 
                \\
                0  & \times &        &   & \times
            \end{array}
        \right)
    \nonumber
    \\
    & \vdots &
    \nonumber
    \\
    G(1, 2, \theta)^{\mathrm{T}}A^{(m-1)}
    & = &
        \left(
            \begin{array}{ccccc}
                \times   & \times & \cdots & \times & \times
                \\
                0  &    &    & \cdots & \vdots
                \\
                \vdots &    &    & \ddots &
                \\
                0    & \vdots & \ddots & \ddots & 
                \\
                0  & \times &        &   & \times
            \end{array}
        \right)
    \nonumber
    \\
    G(m-1, m, \theta)^{\mathrm{T}}A^{(m)}
    & = &
        \left(
            \begin{array}{ccccc}
                \times   & \times & \cdots & \times & \times
                \\
                0  &    &    & \cdots & \vdots
                \\
                \vdots &    &    & \ddots &
                \\
                0    & \times & \ddots & \ddots & 
                \\
                0  & 0 &        &   & \times
            \end{array}
        \right)
    \nonumber
    \\
    & \vdots &
    \nonumber
    \\
    G(m-1, m, \theta)^{\mathrm{T}}A^{(m)}
    & = &
        \left(
            \begin{array}{ccccc}
                \times & \times & \cdots & \times & \times
                \\
                0      & \times &        & \cdots & \vdots
                \\
                \vdots & 0      &        & \ddots &
                \\
                0      & \vdots & \ddots & \ddots &
                \\
                0      & 0      & \cdots & 0      & \times
            \end{array}
        \right)
    \nonumber
    \\
    & =: &
        R
    \nonumber
\end{eqnarray}
$$

Since $G(i, j, \theta)$ is orthonomal, $Q^{\mathrm{T}} := G(m-1, m)^{\mathrm{T}} \cdots G(m-1, m)^{\mathrm{T}}$ satisfies

$$
    Q^{\mathrm{T}}A
    =
    R
    .
$$

#### Algorithm Givens QR

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Givens QR}
    \begin{algorithmic}
    \REQUIRE $A \in \mathbb{R}^{m \times n}$
    \REQUIRE $m \ge n$
    \PROCEDURE{GivensQR}{$A$}
        \FOR{$j = 1$ \TO $n$}
            \FOR{$i = m$ \TO $j+1$}
                \STATE $(c, s) \leftarrow \mathrm{ComputeGivensRotation}(A_{j}^{i-1}, A_{j}^{i})$
                \STATE $A_{j:n}^{(i-1):i} \leftarrow \mathrm{MultiplyGivensRotation}(c, s, A_{j:n}^{(i-1):i})$
            \ENDFOR
        \ENDFOR
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

* $A \in \mathbb{R}^{n \times n}$,
    * symmetric

If $A$ is symmetric, there exists a orthogonal matrix $Q$ such that

$$
    Q^{\mathrm{T}}AQ
    =
    T
$$

where $T$ is tridiagonal.

## Reference
* [chap4 example\.pdf](http://www.cs.nthu.edu.tw/~cherung/teaching/2008cs3331/chap4%20example.pdf)
* G. H. Golub and C. F. Van Loan. Matrix Computations. Johns Hopkins University Press, Baltimore, MD, USA, fourth edition, 2012
