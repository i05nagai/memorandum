---
title: Fisher Exact Test
---

## Fisher Exact Test
Fisher exact model

* $X_{i}^{c}$,
    * i.i.d. of bernoulli r.v with probability $p_{c}$.
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$X_{i}^{c}(\omega) = x_{i}^{c} \ (i = 1, \ldots, N)$$,
* $X_{i}^{t}$,
    * i.i.d. of bernoulli r.v.with probability $p_{t}$
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$X_{i}^{t}(\omega) = x_{i}^{t} \ (i = 1, \ldots, N)$$,
* $\Theta := [0, 1] \times [0, 1] $,

We assume $$\{X_{i}^{c}\}$$ and $$\{X_{i}^{t}\}$$ are independent.
The probability of r.v.s are given by

$$
\begin{eqnarray}
    f(x_{1}^{c}, \ldots, x_{n}^{c}, x_{1}^{t}, \ldots, x_{N}^{t}; p_{c}, p_{t})
    & := &
        P
        \left(
            \left(
                \bigcap_{i}
                \{X_{i}^{c} = x_{i}^{c}\}
            \right)
            \bigcap
            \left(
                \bigcap_{i}
                \{X_{i}^{t} = x_{i}^{t}\}
            \right)
        \right)
    \nonumber
    \\
    & = &
        \mathrm{Bi}(x_{1}^{c}, \ldots, x_{n}^{c}; p_{c})
        \mathrm{Bi}(x_{1}^{t}, \ldots, x_{n}^{t}; p_{t})
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                N \\
                x_{c}
            \end{array}
        \right)
        p_{c}^{x_{c}}
        (1 - p_{c})^{N - x_{c}}
        \left(
            \begin{array}{c}
                N \\
                x_{t}
            \end{array}
        \right)
        p_{t}^{x_{t}}
        (1 - p_{t})^{N - x_{t}}
\end{eqnarray}
$$

In Fisher's exact model, for given $(p, p) \in \Theta$, null hypothesis is $$H_{0} := \{(p , p) \in \Theta \mid p \in [0, 1]\}$$.

$$
\begin{eqnarray}
    f(x_{1}^{c}, \ldots, x_{n}^{c}, x_{1}^{t}, \ldots, x_{N}^{t}; p, p)
    & = &
        \left(
            \begin{array}{c}
                N \\
                x_{c}
            \end{array}
        \right)
        \left(
            \begin{array}{c}
                N \\
                x_{t}
            \end{array}
        \right)
        p^{x_{c} + x_{t}}
        (1 - p)^{N - x_{c} - x_{t}}
\end{eqnarray}
$$

Let $\alpha \in [0, 1]$ be significance level.

$$
    \alpha
$$

## Example
* $N = 15$,
* $$x_{i}^{c} \in \{0, 1\}$$,
    * 1 means that $i$-th person became infected with influenza
    * people innoculated with a recombinant DNA influenza vaccine
    * control group
* $$x_{i}^{t} \in \{0, 1\}$$,
    * 1 means that $i$-th person became infected with influenza
    * people innoculated with a placebo
    * treatment group
* $x^{c} := \sum_{i=1}^{N} x_{i}^{c}$,
    * the number of infected people in the control group
* $x^{t} := \sum_{i=1}^{N} x_{i}^{t}$,
    * the number of infected people in the treatment group


| Infection status | Vacctine          | Placebo            | Total |
|------------------|-------------------|--------------------|-------|
| Yes = 1          | 7 = $x^{t}$ (47%) | 12 = $x^{c}$ (80%) | 19    |
| No  = 0          | 8 (53%)           | 3 (20%)            | 11    |
|------------------|-------------------|--------------------|-------|
| Totals           | 15                | 15                 | 30    |


Fisher exact model

* $X_{i}^{c}$,
    * i.i.d. of bernoulli r.v with probability $p_{c}$.
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$X_{i}^{c}(\omega) = x_{i}^{c} \ (i = 1, \ldots, N)$$,
* $X_{i}^{t}$,
    * i.i.d. of bernoulli r.v.with probability $p_{t}$
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$X_{i}^{t}(\omega) = x_{i}^{t} \ (i = 1, \ldots, N)$$,
* $\Theta := [0, 1]$,


$$
\begin{eqnarray}
    P
    \left(
        \left(
            \bigcap_{i}
            \{X_{i}^{c} = x_{i}^{c}\}
        \right)
        \bigcap
        \left(
            \bigcap_{i}
            \{X_{i}^{t} = x_{i}^{t}\}
        \right)
    \right)
    & = &
        \left(
            \begin{array}{c}
                N \\
                x_{c}
            \end{array}
        \right)
        p^{x_{c} + x_{t}}
        (1 - p)^{N - x_{c} - x_{t}}
        \left(
            \begin{array}{c}
                N \\
                x_{t}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                15 \\
                12
            \end{array}
        \right)
        p^{19}
        (1 - p)^{-4}
        \left(
            \begin{array}{c}
                15 \\
                7
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        455
        p^{19}
        (1 - p)^{-4}
        6435
\end{eqnarray}
$$

## Reference
