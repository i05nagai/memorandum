---
title: Importance Sampling
---

## Importance Sampling
Importance sampling reduces the variance of the monte carolo estimator.

## Notation
* $(\Omega, \mathcal{F}, P)$,
* $h: \mathbb{R} \rightarrow \mathbb{R}$
    * mesurable function
* $X: \Omega \rightarrow \mathbb{R}$,
    * r.v.
* $f: \mathbb{R} \rightarrow \mathbb{R}$,
    * probability density function of $X$

## Problem
Compute a monte carlo estatimator of the expectation of $h(X)$ with low variance.

$$
\begin{eqnarray}
    \alpha
    & := &
        \mathrm{E}
        \left[
            h(X)
        \right]
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}}
            h(x)f(x)
        \ dx
    .
\end{eqnarray}
$$

## Good
* The algorithm is very simple.

## Bad
* In pactical, $g$ is chosen heuristically and empirically.
* The algorithm need to evaluate $f$ and $g$.

## Theory
* $g: \mathbb{R} \rightarrow \mathbb{R}$,
    * p.d.f
    * $f(x) > 0 \Rightarrow g(x) > 0$,
* $\mathrm{E}_{g}[]$,
    * expectation with a measure derived from $g$,

$$
\begin{eqnarray}
    \alpha
    & = &
        \int_{\mathbb{R}}
            h(x)
            \frac{f(x)}{g(x)}
            g(x)
        \ dx
    \nonumber
    \\
    & = &
        \mathrm{E}_{g}
        \left[
            h(X)
            \frac{f(X)}{g(X)}
        \right]
\end{eqnarray}
$$

The second momemnt of $h(X)f(X)/g(X)$ is 

$$
\begin{eqnarray}
    \mathrm{E}_{g}
    \left[
        \left(
            h(X)
            \frac{f(X)}{g(X)}
        \right)^{2}
    \right]
    & = &
        \mathrm{E}
        \left[
            \left(
                h(X)
                \frac{f(X)}{g(X)}
            \right)^{2}
            \frac{g(X)}{f(X)}
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            h(X)^{2}
            \frac{f(X)}{g(X)}
        \right]
        .
    \nonumber
\end{eqnarray}
$$

On the other hand, the second moment of $h(X)$ is

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        h(X)^{2}
    \right]
    .
\end{eqnarray}
$$

Hence $f(x)/g(x)$ controls the variablce of $h(X)$.

Choise of $g$.
Suppose that $h$ is nonnegative and holds

$$
    g(x)
    \propto
    h(x)
    f(x)
    .
$$

Then

$$
    \mathrm{E}_{g}
    \left[
        h(X)^{2}
        \frac{f(X)}{g(X)}
    \right]
    \approx
    \mathrm{E}
    \left[
        h(X)
    \right]
$$

## Algorithm
* Given probability density $g$
* $$\{X_{i}\}$$,
    * I.I.D
* $N \in \mathbb{N}$,
    * the number of MC simulation


Step0. $n = 1$,

Step1. Generate I.I.D. sample $x_{i} := X_{i}(\omega)$.

Step2. Calculate a monte calro estimator $\alpha_{n}$ defined by

$$
\begin{eqnarray}
    \hat{\alpha}_{n}
    & := &
        \frac{1}{n}
        \sum_{i=1}^{n}
            h(X_{i}(\omega))
    \nonumber
\end{eqnarray}
$$

Step3. If $n < N$, $n \leftarrow n + 1$ and go to Step 1. Otherwise, return $\hat{\alpha}_{n}$.


## Example

## Reference
