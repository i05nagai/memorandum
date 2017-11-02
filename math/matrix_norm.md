---
title: Matrix Norm
---

## Matrix Norm


### Definition. Frobenius Norm
* $$A \in \mathbb{C}^{m \times n}$$,

$$
\begin{eqnarray}
    \|A\|_{\mathrm{F}}
    & := &
        \sqrt{
            \sum_{i=1}^{m}
                \sum_{j=1}^{n}
                    (a_{j}^{i})^{2}
        }
    \nonumber
    \\
    & = &
        \sqrt{
            \sum_{i=1}^{m}
                (a^{i})^{\mathrm{T}}
                (a^{i})
        }
    \nonumber
    \\
    & = &
        \sqrt{
            \sum_{j=1}^{n}
                (a_{j})^{\mathrm{T}}
                (a_{j})
        }
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition 2.
* $$A = (a_{1} \cdot a_{n}) \in \mathbb{C}^{m \times n}$$,
    * $$a_{i} \in \mathbb{C}^{m}$$ is column vectors of $A$.

$$
    \|A \|_{\mathrm{F}}^{2}
    =
    \mathrm{tr}(A^{\mathrm{T}}A)
    =
    \mathrm{tr}(AA^{\mathrm{T}})
$$

### proof.
We show first equality as follows:

$$
\begin{eqnarray}
    \mathrm{tr}(A^{\mathrm{T}}A)
    & = &
        \left(
            \begin{array}{c}
                a_{1}^{\mathrm{T}}
                \\
                \vdots 
                \\
                a_{n}^{\mathrm{T}}
            \end{array}
        \right)
        (a_{1} \cdot a_{n})
    \\
    & = &
        \mathrm{tr}
        \left(
            (a_{j_{1}}^{\mathrm{T}}a_{j_{2}})_{j_{1},j_{2}=1,\ldots, n}
        \right)
    \nonumber
    \\
    & = &
        \sum_{j=1}^{n}
            (a_{j}^{\mathrm{T}}a_{j})
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{tr}(AA^{\mathrm{T}})
    & = &
        \mathrm{tr}((A^{\mathrm{T}}A)^{\mathrm{T}})
    \nonumber
    \\
    & = &
        \mathrm{tr}
        \left(
            \left(
                (a_{j_{1}}^{\mathrm{T}}a_{j_{2}})_{j_{1},j_{2}=1,\ldots, n}
            \right)^{\mathrm{T}}
        \right)
    \nonumber
    \\
    & = &
        \sum_{j=1}^{n}
            (a_{j}^{\mathrm{T}}a_{j})
    \nonumber
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition3.
* $A \in \mathbb{R}^{m \times n}$,
* $U \in \mathbb{R}^{m \times m}$
    * unitary matrix
* $V \in \mathbb{R}^{n \times n}$
    * unitary matrix

Then

$$
    \|UAV\|_{F}
    =
    \|A\|_{F}
    .
$$

### proof.

$$
\begin{eqnarray}
    \|UA\|_{F}^{2}
    & = &
        \mathrm{tr}
        (
            (UA)^{\mathrm{T}}UA
        )
    \nonumber
    \\
    & = &
        \mathrm{tr}
        (
            A^{\mathrm{T}}A
        )
    \nonumber
\end{eqnarray}
$$

Moreover,

$$
\begin{eqnarray}
    \|AV\|_{F}^{2}
    & = &
        \mathrm{tr}
        (
            AV(AV)^{\mathrm{T}}
        )
    \nonumber
    \\
    & = &
        \mathrm{tr}
        (
            AA^{\mathrm{T}}
        )
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


### Propositon 4.
* $$A \in \mathbb{C}^{m \times n}$$,
* $$U \in \mathbb{C}^{m \times m}$$,
    * unitary matrix
* $$\Sigma \in \mathbb{C}^{m \times n}$$,
    * $$\Sigma = \mathrm{diag}(\sigma_{1}, \ldots, \sigma_{r}, 0, \ldots, 0)$$,
    * singular value of $A$
* $$V \in \mathbb{C}^{n \times n}$$,
    * unitary matrix

Suppose SVD $A = U\Sigma V$ holds.
Then

$$
    \|A\|_{F}^{2}
    =
    \sum_{i=1}^{r}
        (\sigma_{i})^{2}
$$

### proof.
By the above proposition,

$$
\begin{eqnarray}
    \|A\|_{F}^{2}
    & = &
        \|U\Sigma V\|_{F}^{2}
    \nonumber
    \\
    & = &
        \|\Sigma \|_{F}^{2}
    \nonumber
    \\
    & = &
        \mathrm{tr}(\Sigma \Sigma)
    \nonumber
    \\
    & = &
        \mathrm{tr}(\Sigma^{2})
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition5
* $S$
    * symmetric (i.e. $S = S^{\mathrm{T}}$),
* $K$
    * skew symmetric (i.e. $K = -K^{\mathrm{T}}$),

Then

$$
    \|S + K\|_{F}^{2}
    =
    \|S\|_{F}^{2} + \|K\|_{F}^{2}
$$

### proof.

$$
\begin{eqnarray}
    \|S + T\|_{F}^{2}
    & = &
        \mathrm{tr}((S + T)^{\mathrm{T}}(S + T))
    \mathrm{tr}
    \left(
        (S^{\mathrm{T}} + T^{\mathrm{T}})
        (S + T)
    \right)
    \nonumber
    \\
    & = &
        \mathrm{tr}
        \left(
            S^{\mathrm{T}}S + T^{\mathrm{T}}S
            +
            S^{\mathrm{T}}T + T^{\mathrm{T}}S
        \right)
    \nonumber
    \\
    & = &
        \mathrm{tr}
        \left(
            S^{\mathrm{T}}S + (-TS)
            +
            (TS)^{\mathrm{T}} + T^{\mathrm{T}}T
        \right)
    \nonumber
    \\
    & = &
        \mathrm{tr}
        \left(
            S^{\mathrm{T}}S
        \right)
        +
        \mathrm{tr}
        \left(
            -TS
        \right)
        +
        \mathrm{tr}
        \left(
            (TS)^{\mathrm{T}}
        \right)
        +
        \mathrm{tr}
        \left(
            T^{\mathrm{T}}T
        \right)
    \nonumber
    \\
    & = &
        \|S\|_{F}^{2}
        +
        \|T\|_{F}^{2}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [行列のフロベニウスノルムとその性質  高校数学の美しい物語](https://mathtrain.jp/frobeniusnorm)

