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
The time complexity of LU decomposition for band diagonal matrix is $O(2npq)$.


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
        $A \in \mathbb{R}^{n \times n}$: has upper bandwidth $q$, lower bandwidth $p$
    \FOR{$k = 1$ TO $n - 1$}
        \FOR{$r = k + 1$ TO $\min(k + p, n)$}
            \STATE $A(r, k) = A(r, k) / A(k, k)$
            \COMMENT{$p$-th lower bandwidth}
        \ENDFOR

        \FOR{$r = k + 1$ TO $\min(k + q, n)$}
            \FOR{$c = k + 1$ TO $\min(k + p, n)$}
                \STATE $A(r, c) = A(r, c) - A(r, k) / A(k, k)$
            \ENDFOR
        \ENDFOR
    \ENDFOR
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>


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

In particular,

$$
\begin{eqnarray}
    y_{1}^{1}
    & = &
        \frac{
            b_{1}^{1}
        }{
            l_{1}^{1}
        }
    \nonumber
    \\
    & = &
        1
    \nonumber
    \\
    y_{1}^{2}
    & = &
        \frac{
            1
        }{
            l_{2}^{2}
        }
        \left(
            b_{1}^{2}
            -
            l_{1}^{2}
            y_{1}^{1}
        \right)
    \nonumber
    \\
    & = &
        -
        l_{1}^{2}
        y_{1}^{1}
    \nonumber
    \\
    & = &
        -
        l_{1}^{2}
    \nonumber
    \\
    y_{1}^{3}
    & = &
        \frac{
            1
        }{
            l_{3}^{3}
        }
        \left(
            -
            l_{1}^{3}
            y_{1}^{1}
            -
            l_{2}^{3}
            y_{1}^{2}
        \right)
    \nonumber
    \\
    & = &
        \left(
            -
            l_{1}^{3}
            +
            l_{2}^{3}
            l_{1}^{2}
        \right)
    \nonumber
    \\
    & = &
        -
        1
    y_{1}^{i}
    & = &
        \frac{
            1
        }{
            l_{i}^{i}
        }
        \left(
            b_{1}^{i}
            -
            \sum_{k=1}^{i-1}
                l_{k}^{i}
                y_{k}^{i}
        \right)
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            l_{i}^{i}
        }
        \left(
            -
            \sum_{k=1}^{i-1}
                l_{k}^{i}
                y_{k}^{i}
        \right)
    \nonumber
    \\
    y_{j}^{1}
    & = &
        \frac{
            1
        }{
            l_{1}^{1}
        }
        b_{j}^{1}
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
                x_{k}^{i}
        \right)
    \nonumber
\end{eqnarray}
$$

## Reference
