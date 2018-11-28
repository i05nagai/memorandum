---
title: Band-Diagonal Matrix
---

## Band-Diagonal Matrix

* $$[i:j] := \{i, i + 1, \ldots, j\}$$,
    * if  $i < j$, $[i:j] := \emptyset$,
* $A := (a_{j}^{i})_{i, j \in [1:n]}$,
    * $n \times n$ matrix


#### Definiiton
* $q \in [0:n]$,

$A$ is said to have upper bandwidth $q$ if

$$
    j > i + q,
    \
    a_{j}^{i} = 0
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definiiton
* $p \in [0:n]$,

$A$ is said to have lower bandwidth $p$ if

$$
    i > j + p,
    \
    a_{j}^{i} = 0
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Theorem
* $A = LU$,
    * LU decomposition of $A$

If $A$ has upper bandwidth $q$ and lower bandwidth $p$, then

* $U$ has upper bandwidth $q$,
* $L$ has lower bandwidth $p$.

#### proof
We prove by induction on $n$.
In case of $n = 1$, the statement holds by definition.

Suppose the statement hold up to $n-1$.
Let

$$
    A
    =:
    \left(
        \begin{array}{cc}
            a_{1}^{1}
            &
                a_{2:n}^{1}
            \\
            a_{1}^{2:n}
            &
                a_{2:n}^{2:n}
        \end{array}
    \right)
    .
$$

$$
\begin{eqnarray}
    \left(
        \begin{array}{cc}
            1
            &
                0
            \\
            \frac{1}{a_{1}^{1}}
            a_{1}^{2:n}
            &
                I_{n-1}
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
                a_{2:n}^{2:n}
                -
                \frac{1}{a_{1}^{1}}
                a_{1}^{2:n}
                a_{2:n}^{1}
        \end{array}
    \right)
    \left(
        \begin{array}{cc}
            a_{1}^{1}
            &
                a_{2:n}^{1}
            \\
            0
            &
                I_{n-1}
        \end{array}
    \right)
    & = &
        \left(
            \begin{array}{cc}
                1
                &
                    0
                \\
                \frac{1}{a_{1}^{1}}
                a_{1}^{2:n}
                &
                    a_{2:n}^{2:n}
                    -
                    \frac{1}{a_{1}^{1}}
                    a_{1}^{2:n}
                    a_{2:n}^{1}
            \end{array}
        \right)
        \left(
            \begin{array}{cc}
                a_{1}^{1}
                &
                    a_{2:n}^{1}
                \\
                0
                &
                    I_{n-1}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                a_{1}^{1}
                &
                    a_{2:n}^{1}
                \\
                a_{1}^{2:n}
                &
                    \frac{1}{a_{1}^{1}}
                    a_{1}^{2:n}
                    a_{2:n}^{1}
                    +
                    a_{2:n}^{2:n}
                    -
                    \frac{1}{a_{1}^{1}}
                    a_{1}^{2:n}
                    a_{2:n}^{1}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cc}
                a_{1}^{1}
                &
                    a_{2:n}^{1}
                \\
                a_{1}^{2:n}
                &
                    a_{2:n}^{2:n}
            \end{array}
        \right)
\end{eqnarray}
$$

$A$ is decomposed to the above matrices.
Since $A$ has upper bandwidth $q$ and lower bandwidth $p$, $a_{2:q}^{1} = 0$ and $a_{1}^{2:p} = 0$.
$$a_{2:n}^{2:n} - \frac{1}{a_{1}^{1}} a_{1}^{2:n} a_{2:n}^{1}$$ also has has upper bandwidth $q$ and lower bandwidth $p$.
Let $L_{1}U_{1}$ be LU decomposition of the matrix.

$$
    L_{1}U_{1}
    :=
    a_{2:n}^{2:n}
    -
    \frac{1}{a_{1}^{1}}
    a_{1}^{2:n} a_{2:n}^{1}
    .
$$

$$
\begin{eqnarray}
    \left(
        \begin{array}{cc}
            1
            &
                0
            \\
            \frac{1}{a_{1}^{1}}
            a_{1}^{2:n}
            &
                I_{n-1}
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
                L_{1}
                U_{1}
        \end{array}
    \right)
    \left(
        \begin{array}{cc}
            a_{1}^{1}
            &
                a_{2:n}^{1}
            \\
            0
            &
                I_{n-1}
        \end{array}
    \right)
    & = &
        \left(
            \begin{array}{cc}
                1
                &
                    0
                \\
                \frac{1}{a_{1}^{1}}
                a_{1}^{2:n}
                &
                    I_{n-1}
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
                    L_{1}
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
                    U_{1}
            \end{array}
        \right)
        \left(
            \begin{array}{cc}
                a_{1}^{1}
                &
                    a_{2:n}^{1}
                \\
                0
                &
                    I_{n-1}
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
                \frac{1}{a_{1}^{1}}
                a_{1}^{2:n}
                &
                    L_{1}
            \end{array}
        \right)
        \left(
            \begin{array}{cc}
                a_{1}^{1}
                &
                    a_{2:n}^{1}
                \\
                0
                &
                    U_{1}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        L
        U
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Cororally
The time complexity of LU decomposition for band diagonal matrix is $O(npq) \approx 2npq$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>


## Gaussian Elimination
Let

$$
\begin{eqnarray}
    a_{j}^{i, (1)}
    & := &
        a_{j}^{i}
    \nonumber
    \\
    a_{j}^{i, (k)}
    & := &
        a_{j}^{i, (k - 1)}
        -
        m^{i, (k-1)}
        a_{j}^{i, (k - 1)}
    \nonumber
    \\
    m^{i, (k)}
    & := &
        \frac{
            a_{k}^{i, (k)}
        }{
            a_{k}^{k, (k)}
        }
    \nonumber
    \\
    r^{(k)}
    & := &
        (0, \ldots, m^{k, (k)}, m^{k+1,(k)}, \ldots, m^{n, (k)})^{\mathrm{T}}
    \nonumber
    \\
    M^{(k)}
    & := &
        I
        -
        r^{(k)}
        (e^{k})^{\mathrm{T}}
    \nonumber
    \\
    & = &
        I
        -
        \left(
            \begin{array}{ccccc}
                0 & \cdots &  & r^{1, (k)} & 0
                \\
                0 & \cdots & 0 & r^{2, (k)} & 0
                \\
                0 & \cdots & 0 & \vdots & 0
                \\
                 & \vdots & \vdots & \vdots &
                \\
                0  & \cdots & 0 & r^{n, (k)} & 0
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    M^{(n - 1)}
    \cdots
    M^{(1)}
    A
    & =: &
        U
    \nonumber
    \\
    & = &
        \left(
            I
            -
            \left(
                \begin{array}{ccccc}
                    0 & \cdots &  & r^{1, (k)} & 0
                    \\
                    0 & \cdots & 0 & r^{2, (k)} & 0
                    \\
                    0 & \cdots & 0 & \vdots & 0
                    \\
                     & \vdots & \vdots & \vdots &
                    \\
                    0  & \cdots & 0 & r^{n, (k)} & 0
                \end{array}
            \right)
        \right)
        B
    \nonumber
    \\
    & = &
        B
        -
        \left(
            \begin{array}{cccc}
                r^{1, (k)} b_{1}^{k}
                &
                    \cdots
                &
                    r^{1, (k)} b_{n-1}^{k}
                &
                    r^{1, (k)} b_{n}^{k}
                \\
                 & \vdots & \vdots & \vdots &
                \\
                r^{n, (k)} b_{1}^{k}
                &
                    \cdots
                &
                    r^{n, (k)} b_{n-1}^{k}
                &
                    r^{n, (k)} b_{n}^{k}
            \end{array}
        \right)
\end{eqnarray}
.
$$

Hence 

$$
\begin{eqnarray}
    L
    & := &
        (M^{(1)})^{-1}
        \cdots
        (M^{(n-1)})^{-1}
    \nonumber
\end{eqnarray}
$$

Interestingly, if $r^{k, (k)} = 0$,

$$
\begin{eqnarray}
    (M^{(k)})^{-1}
    & = &
        (I + r^{(k)}(e^{k})^{\mathrm{T}})
    \nonumber
    \\
    (I - r^{(k)}(e^{k})^{\mathrm{T}})
    (I + r^{(k)}(e^{k})^{\mathrm{T}})
    & = &
        I
        -
        r^{(k)}(e^{k})^{\mathrm{T}}
        r^{(k)}(e^{k})^{\mathrm{T}}
    \nonumber
    \\
    & = &
        I
        -
        \left(
            \begin{array}{cccc}
                0
                &
                    \cdots
                &
                    r^{1, (k)}
                    r^{k, (k)}
                &
                    \cdots
                &
                    0
                \\
                0
                &
                    \cdots
                &
                    r^{2, (k)}
                    r^{k, (k)}
                &
                    \cdots
                &
                    0
                \\
                 & \vdots & \vdots & \vdots &
                \\
                0
                &
                    \cdots
                &
                    r^{n, (k)}
                    r^{k, (k)}
                &
                    \cdots
                &
                    0
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        I
    \nonumber
\end{eqnarray}
    .
$$

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{LU decomposition with Gaussian Elimination Outer PProduct}
    \begin{algorithmic}
    \REQUIRE
        $A \in \mathbb{R}^{n \times n}$: has upper bandwidth $q$ and lower bandwidth $p$
    \FOR{$k = 1$ \TO $n - 1$}
        \FOR{$r = k + 1$ \TO $\min(k + p, n)$}
            \STATE $A(r, k) = A(r, k) / A(k, k)$
            \COMMENT{$p$-th lower bandwidth}
        \ENDFOR

        \FOR{$r = k + 1$ \TO $\min(k + q, n)$}
            \FOR{$c = k + 1$ \TO $\min(k + p, n)$}
                \STATE $A(r, c) = A(r, c) - A(r, k) / A(k, k)$
            \ENDFOR
        \ENDFOR
    \ENDFOR
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

#### Lower triangular matrix
Solving linear equations $Lx = b$ where $L$ is lower triangular and band-diagonal.
If $p \ll n$, the computational complexity is $O(2np)$.

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Bandiagonal lower triangular solver}
    \begin{algorithmic}
    \REQUIRE \\
        $L \in \mathbb{R}^{n \times n}$: lower triangular matrix who has lower bandwidth $p$, \\
        $b \in \mathbb{R}^{n}$,
    \FOR{$k = 1$ \TO $n$}
        \FOR{$r = k + 1$ \TO $\min(k + p, n)$}
            \STATE $b(r) = b(r) - L(r, k)b(k)$
        \ENDFOR
    \ENDFOR
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

#### Upper triangular matrix
Solving linear equations $Ux = b$ where $L$ is upper triangular and band-diagonal.
If $q \ll n$, the computational complexity is $O(2nq)$.

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Bandiagonal upper triangular solver}
    \begin{algorithmic}
    \REQUIRE \\
        $U \in \mathbb{R}^{n \times n}$: upper triangular matrix who has upper bandwidth $q$, \\
        $b \in \mathbb{R}^{n}$,
    \FOR{$k = n - 1$ \TO $1$}
        \STATE b(k) = b(k) / U(k, k)
        \FOR{$r = \max(1, k - q) $ \TO $k - 1$}
            \STATE $b(r) = b(r) - U(r, k)b(k)$
        \ENDFOR
    \ENDFOR
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

## Inverting Matrix

$$
\begin{eqnarray}
    LUX
    & = &
        B
    \nonumber
    \\
    Y
    & := &
        UX
    \nonumber
    \\
    LY
    & = &
        B
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    y_{j}^{i}
    & = &
        \frac{
            1
        }{
            l_{i}^{i}
        }
        \left(
            b_{j}^{i}
            -
            \sum_{k=1}^{i-1}
                l_{k}^{i}
                y_{j}^{k}
        \right)
    \nonumber
    \\
    x_{j}^{i}
    & = &
        \frac{
            1
        }{
            u_{i}^{i}
        }
        \left(
            y_{j}^{i}
            -
            \sum_{k=1}^{n-i}
                u_{k}^{i}
                x_{j}^{k}
        \right)
    \nonumber
\end{eqnarray}
$$


## Reference
* G. H. Golub and C. F. Van Loan. Matrix Computations. Johns Hopkins University Press, Baltimore, MD, USA, fourth edition, 2012
