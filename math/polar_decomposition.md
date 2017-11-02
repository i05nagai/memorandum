---
title: Polar Decomposition
---

## Polar Decomposition
* $A \in \mathbb{C}^{n \times n}$

Polar decomposition of $A$ is a decompositionof the form

$$
    A
    =
    UP
$$

where $U \in \mathbb{C}^{n \times n }$ unitary matrix and $P$ is a positive-semidifinite hermitian matrix.

## Thereom
* $A \in \mathbb{C}^{n \times n}$,
* $W \in \mathbb{C}^{n \times n}$,
    * unitary matrix
* $V \in \mathbb{C}^{n \times n}$,
    * unitary matrix
* $\Sigma \in \mathbb{C}^{n \times n}$,
    * nonnegative realnumber diagonal matrix
* $U \in \mathbb{C}^{n \times n}$,
    * unitary matrix
* $P \in \mathbb{C}^{n \times n}$,
    * positive semidifinite hermitian matrix

Then following statements are equivalent:

* (a) Singular value decomposition of $$A = W\Sigma V^{*}$$ exists,
* (b) Polar decomposition of $A = UP$ exists.

## proof.
(a) $\Rightarrow$ (b)
Suppose $$A = W \Sigma V^{*}$$.
Let

$$
\begin{eqnarray}
    P
    & := &
        V \Sigma V^{*}
    \nonumber
    \\
    U
    & := &
        WV^{*}
    .
    \nonumber
\end{eqnarray}
$$

$U$ is unitary matrix since

$$
\begin{eqnarray}
    U^{*}U
    & = &
        VW^{*}WV^{*}
    \nonumber
    \\
    & = &
        I
    .
    \nonumber
\end{eqnarray}
$$

Diagonal matrix $\Sigma$ is positve semidefinite since

$$
\begin{eqnarray}
    x^{\mathrm{T}}\Sigma x
    =
    \sum_{i=1}^{r}
        d_{i}(x_{i})^{2}
    \ge
    0
\end{eqnarray}
$$

$P$ is positve definite since

$$
\begin{eqnarray}
    x^{*}V\Sigma V^{*}x
    & = &
        (V^{*}x)^{*}\Sigma (V^{*}x)
    \nonumber
\end{eqnarray}
$$

(a) $\Leftarrow$ (b)

$P$ is symmetric positive semidefinite so that by <a href="{{ site.baseurl }}/math/eigenvalue.html#theorem10-orthogonal-diagonalization">eigenvalue decomposition</a> weh have

$$
    P
    =
    VDV^{*}
$$

where $$V$$ unitary matrix and $$D = \mathrm{diag}(d_{1}, \ldots, d_{r}, 0, \ldots, 0)$$ and $$d_{i} > 0$$.
Then we define

$$
\begin{eqnarray}
    A
    & = &
        UP
    \nonumber
    \\
    & = &
        UVDV^{*}
    \nonumber
    \\
    & = &
        WDV
    \nonumber
\end{eqnarray}
$$

where $W := UV$.
$W$ is unitary matrix since $U$ and $V$ are both unitary.

<div class="QED" style="text-align: right">$\Box$</div>

## Thereom2
* $A \in \mathbb{C}^{n \times n}$,
    * nonsingular

Then polar decomposition is unique and $P$ is positive definite.

## proof.
Suppose that there exists another decomposition $$A = U_{1}P_{1}$$ where $$U_{1}$$ is unitary and $$P_{1}$$ is hermitian positive semidefinite matrix.

$$
    A^{\mathrm{T}}A
    =
    P_{1}^{\mathrm{T}}P
$$

TBD

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [Polar decomposition - Wikipedia](https://en.wikipedia.org/wiki/Polar_decomposition)
* http://www.cis.upenn.edu/~cis610/geombchap12.pdf
