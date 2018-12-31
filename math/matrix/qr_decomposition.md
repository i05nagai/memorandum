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

## Householder QR with Column Pivoting
If $A$ is not full-rank,

$$

$$

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
            \STATE $\mathrm{piv}^{r} = k$
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

## Reference

