---
title: Cross Validation
---

## Cross Validation

* $N \in \mathbb{N}$,
    * the number of data
* $M \in \mathbb{N}$,
    * the number of cross valiation
* $r \in \mathbb{N}$,
    * the input dimension
* $X_{k} := (x_{j,k}^{i})_{j=1, \ldots, r}^{i=1,\ldots,N}\ (k = 1, \ldots, r)$,
* $y_{k} := (y_{k}^{i})^{i=1,\ldots,N} \ (k = 1, \ldots, r)$,
* $f: \mathbb{R}^{r} \rightarrow \mathbb{R}$,
    * true model
* $g(\cdot; X_{k}, y_{k}): \mathbb{R}^{r} \rightarrow \mathbb{R}$,
    * the prediction model learned from data $(X_{k}, y_{k})$,
* $\sigma_{k} > 0$,
    * deviation of $k$-th set of cross validation
* $Z_{k} := (Z_{k}^{i})^{i=1,\ldots,n}$,
    * I.I.D. standard normal r.v. 

$$
\begin{eqnarray}
    y_{k}
    & = &
        f(X_{k})
        +
        \sigma_{k}
        y_{k}
    \nonumber
    \\
    \left(
        \begin{array}{c}
            y_{k}^{1}
            \\
            \vdots 
            \\
            y_{k}^{n}
        \end{array}
    \right)
    & = &
        \left(
            \begin{array}{c}
                f(x_{k}^{1})
                \\
                \vdots 
                \\
                f(x_{k}^{n})
            \end{array}
        \right)
        +
        \sigma_{k}
        \left(
            \begin{array}{c}
                Z_{k}^{1}
                \\
                \vdots 
                \\
                Z_{k}^{1}
            \end{array}
        \right)
\end{eqnarray}
$$

* $N_{1}, N_{2} \le N$,
    * such that $N_{1} + N_{2} = N$,
    * $N_{1}$ is the number of learning/training data
    * $N_{2}$ is the number of testing data

Let $C_{1}$ be the segmentation for learning data and $C_{2}$ be the segmentation for testing data defined as

$$
\begin{eqnarray}
    C_{1}(X_{k})
    & = &
        (x_{j,k}^{i})_{j=1,\ldots,r}^{i=1,\ldots,N_{1}}
    \nonumber
    \\
    C_{2}(X_{k})
    & = &
        (x_{j,k}^{i})_{j=1,\ldots,r}^{i=N_{1}+1,\ldots,N}
    .
    \nonumber
\end{eqnarray}
$$

We indulge to use $C_{1}$ and $C_{2}$ for other variables;

$$
\begin{eqnarray}
    C_{1}(y_{k})
    & = &
        (y_{k}^{i})_{j=1,\ldots,r}^{i=1,\ldots,N_{1}}
    \nonumber
    \\
    C_{1}(Z_{k})
    & = &
        (Z_{k}^{i})_{j=1,\ldots,r}^{i=1,\ldots,N_{1}}
    .
    \nonumber
\end{eqnarray}
$$

It is enough that the segmentations only splits data into the first $N_{1}$ of the data and the rest because we assume that the data itself might vary in each cross validation step.

Let $e_{k} \in \mathbb{R}^{N_{1}}$ be the learning error defined as

$$
\begin{eqnarray}
    E_{k}^{C}
    & := &
        g(C_{1}(X_{k}); C_{1}(X_{k}), C_{1}(y_{k}))
        -
        C_{1}(y_{k})
    \nonumber
    \\
    E_{k}^{T}
    & := &
        g(C_{2}(X_{k}); C_{1}(X_{k}), C_{1}(y_{k}))
        -
        C_{2}(y_{k})
    \nonumber
    \\
    E_{k}^{S}
    & := &
        g(C_{1}(X_{k}); C_{1}(X_{k}), C_{1}(y_{k}))
        -
        g(C_{2}(X_{k}); C_{2}(X_{k}), C_{2}(y_{k}))
    \nonumber
\end{eqnarray}
$$

#### Theorem1

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \norm{E_{k}^{C}}
    \right]
    \le
    \mathrm{E}
    \left[
        \norm{E_{k}^{T}}
    \right]
    +
    \mathrm{E}
    \left[
        \norm{E_{k}^{S}}
    \right]
\end{eqnarray}
$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>


## Reference

