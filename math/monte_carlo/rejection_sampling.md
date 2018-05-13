---
title: Rejection Sampling
---

## Rejection Sampling
It is also known as Acceptance-Rejection Sampling.
The acceptance-rejection method is introduced by Von Neumann[1].


## Notation
* $(\mathcal{X}, \mathcal{A})$
    * measurable sp.
* $f: \mathcal{X} \rightarrow \mathbb{R}$,
    * density over $\mathcal{X}$
* $g: \mathcal{X} \rightarrow \mathbb{R}$,
    * density over $\mathcal{X}$
* $c \in \mathbb{R}$,
    * constant
* $X \sim g$
    * r.v. of which density is $g$


## Problem
Acceptance-Rejection method generates a sample from $f$.

## Good
* We do not have to explicitly generate a sample from $f$. Only $g$ and an uniform random variable.

## Bad
* $g$ should be computed easily,
* From $$\eqref{rejection_sampling_denominator}$$, $c$ should be closer to 1 holding a relation $$g \le c f$$. In general, it's hard to choose $g$ and $c$.


## Theory
* $U$
    * uniform r.v. over $(0, 1)$,
* $$B := \{x \in \mathcal{X} \mid g(x) > 0\}$$,

Suppose that r.v. $Y$ has probability

$$
\begin{eqnarray}
    P(Y \in A)
    & = &
        P(X \in A \mid U \le \frac{f(X)}{cg(X)})
    .
    \label{rejection_sampling_def_y}
\end{eqnarray}
$$

Then

$$
\begin{eqnarray}
    P(Y \in A)
    & = &
        P(X \in A \mid U \le \frac{f(X)}{cg(X)})
    \nonumber
    \\
    & = &
        \frac{
            P(X \in A, U \le \frac{f(X)}{cg(X)})
        }{
            P(U \le \frac{f(X)}{cg(X)})
        }
    \nonumber
    \\
    & = &
        \frac{
            P(X \in A, U \le \frac{f(X)}{cg(X)})
        }{
            \frac{1}{c}
        }
    \nonumber
    \\
    & = &
        c P(X \in A, U \le \frac{f(X)}{cg(X)})
    \nonumber
    \\
    & = &
        c
        \int_{A}
            \frac{f(x)}{cg(x)}
            g(x)
        \ dx
    \nonumber
    \\
    & = &
        \int_{A}
            f(x)
        \ dx
\end{eqnarray}
$$

where the denominator is evaluated as

$$
\begin{eqnarray}
    P(U \le \frac{f(X)}{cg(X)})
    & = &
        \int_{\mathcal{X}}
            \frac{f(x)}{cg(x)}
            g(x)
        \ dx
    \nonumber
    \\
    & = &
        \frac{1}{c}
    .
    \label{rejection_sampling_denominator}
\end{eqnarray}
$$

Thus, $Y$ has density $f$.
Now the problem is reduced to generate $Y$.

* $X_{i}$,
    * I.I.D. r.v.s generated from $g$,
* $U_{i}$,
    * I.I.D. r.v.s generated from uniformly distribution over $(0, 1)$,

Let $i  = 1$.
$X_{i}$ is accepted if

$$
    U_{i}
    \le
    \frac{
        f(X_{i})
    }{
        c g(X_{i})
    }
    .
$$

Let $j$ be the first index of $X_{j}$ which is accpected.
Then $Y$ is defined by $Y := X_{j}$.

## Algorithm
Step 0. $i = 1$,

Step 1. Generate $X_{i}$ from distribution $g$,

Step 2. Generate $U_{i}$ from uniformly distribution over $(0, 1)$,

Step 3. If $U_{i} \le f(X_{i})/(cg(X_{i}))$, return $X$.
Otherwise, $i \leftarrow i + 1$ and go to Step 1.

## Example

## Reference
* [1] Various Techniques Used in Connection With Random Digits
