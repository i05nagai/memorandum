---
title: Fisher Exact Test
---

## Fisher Exact Test
Fisher exact model.

We consider following 2x2 contingency table:

* $N$,
    * the total number of people
* $K$,
    * the number of people under YES condition
* $n$,
    * the number of people in treatment group

| Condition | treatment group | control group   | total   |
|-----------|-----------------|-----------------|---------|
| YES       | $k$             | $K − k$         | $K$     |
| NO        | $n − k$         | $N + k − n − K$ | $N − K$ |
|-----------|-----------------|-----------------|---------|
| total     | $n$             | $N − n$         | $N$     |

In Fisher exact model, we interpret $k$ is a observed value of r.v. $X^{t}$ which follows <a href="{{ site.baseurl }}/math/distribution/hypergeometric_distribution.html">hypergeometric distribution</a> with parameters $N$, $K$, $n$.

The p.d.f. and c.d.f. of $X^{t}$ is given by

$$
\begin{eqnarray}
    \mathrm{Hyper}(k; N, K, n)
    & = &
        P
        \left(
            X^{t}
            =
            k
        \right)
    \nonumber
    \\
    F_{\mathrm{Hyper}}(k; N, K, n)
    & = &
        \sum_{i=0}^{k}
            P
            \left(
                X^{t}
                =
                k
            \right)
    .
    \nonumber
\end{eqnarray}
$$

Let $\alpha \in [0, 1]$ be significance level.
Then p-value $p_{\alpha}$ is calculated by

$$
\begin{eqnarray}
    k_{\alpha}
    & := &
        \inf
        \{
            k
            \mid
            F_{\mathrm{Hyper}}(x^{t}; N, K, n)
            \le
            \alpha
        \}
    \\
    p_{\alpha}
    & := &
        F_{\mathrm{Hyper}}(k_{\alpha}; N, K, n)
\end{eqnarray}
$$

## Example
* $N = 30$,
* $K = 19$,
* $n = 15$,
* $$x_{i}^{c} \in \{0, 1\}$$,
    * 1 means that $i$-th person became infected with influenza
    * people innoculated with a recombinant DNA influenza vaccine
    * control group
* $$x_{i}^{t} \in \{0, 1\}$$,
    * 1 means that $i$-th person became infected with influenza
    * people innoculated with a placebo
    * treatment group
* $x^{c} := \sum_{i=1}^{n} x_{i}^{c}$,
    * the number of infected people in the control group
* $x^{t} := \sum_{i=1}^{n} x_{i}^{t}$,
    * the number of infected people in the treatment group


| Infection status | Vacctine          | Placebo            | Total |
|------------------|-------------------|--------------------|-------|
| Yes = 1          | 7 = $x^{t}$ (47%) | 12 = $x^{c}$ (80%) | 19    |
| No  = 0          | 8 (53%)           | 3 (20%)            | 11    |
|------------------|-------------------|--------------------|-------|
| Totals           | 15                | 15                 | 30    |


Fisher exact model

* $X^{t}$,
    * hypergemetric distribution with $N := 30$, $K := 19$, $n := 15$.
* $$X^{t}(\omega) = x^{t}$$,
* $\Theta := [0, 1]$,

One-side test

$$
\begin{eqnarray}
    F_{\mathrm{Hyper}}(x^{t}; N, K, n)
    & = &
        \sum_{k = 0}^{x^{t}}
            \mathrm{Hyper}(k; N, K, n)
    \nonumber
    \\
    & \approx &
        0.0640679660169915
\end{eqnarray}
$$


## Reference
* [Contingency Tables](http://www.stat.wisc.edu/~st571-1/06-tables-4.pdf)
