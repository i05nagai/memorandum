---
title: Barnard Test
---

## Barnard Test
Barnard exact model

* $X_{i}^{c}$,
    * i.i.d. of bernoulli r.v with probability $p_{c}$.
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$x_{i}^{c} := X_{i}^{c}(\omega) \ (i = 1, \ldots, n)$$,
* $X_{i}^{t}$,
    * i.i.d. of bernoulli r.v.with probability $p_{t}$
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$x_{i}^{t} := X_{i}^{t}(\omega) \ (i = 1, \ldots, n)$$,
* $\Theta := [0, 1] \times [0, 1] $,


| Condition | treatment group | control group   | total               |
|-----------|-----------------|-----------------|---------------------|
| YES       | $x^{t}$         | $x^{c}$         | $x^{t} + x^{c}$     |
| NO        | $n − x^{t}$     | $N − n - x^{c}$ | $N − x^{t} - x^{c}$ |
|-----------|-----------------|-----------------|---------------------|
| total     | $n = c_{t}$     | $N − n = c_{c}$ | $N$                 |

We assume $$\{X_{i}^{c}\}$$ and $$\{X_{i}^{t}\}$$ are independent.
The probability of r.v.s are given by

$$
\begin{eqnarray}
    f(x^{c}, x^{t}; p_{c}, p_{t})
    & := &
        f(x_{1}^{c}, \ldots, x_{n}^{c}, x_{1}^{t}, \ldots, x_{n}^{t}; p_{c}, p_{t})
    \nonumber
    \\
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
                n \\
                x_{c}
            \end{array}
        \right)
        p_{c}^{x_{c}}
        (1 - p_{c})^{n - x_{c}}
        \left(
            \begin{array}{c}
                n \\
                x_{t}
            \end{array}
        \right)
        p_{t}^{x_{t}}
        (1 - p_{t})^{n - x_{t}}
\end{eqnarray}
$$

In Barnard's exact model, under null hypothesis is $$H_{0} := \{(p , p) \in \Theta \mid p \in [0, 1]\}$$. The p.d.f is given by

$$
\begin{eqnarray}
    f(x^{c}, x^{t}; p, p)
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


If we give the value of $p$, we can calculate the value of p.d.f.
Let $Y$ be some measurable function to determine decision area.

$$
    \hat{p}(p)
    :=
    \sum_{
        (\hat{x}^{c}, \hat{x}^{t}): Y(\hat{x}^{c}, \hat{x}^{t}) \ge Y(x^{c}, x^{t})
    }
        f(\hat{x}^{c}, \hat{x}^{t})
$$

p-values is defined by

$$
    p_{\mathrm{Barnard}}
    :=
    \sup
    \{
        \hat{p}(p)
        \mid
        p \in (0, 1)
    \}
    .
$$

Possible $Y$s are

* Wald statistics,
* Score statistics,
    * aka Z-pooled

$$
\begin{eqnarray}
    \bar{\pi}
    & := &
        \frac{
            x^{c} + x^{t}
        }{
            N
        }
    \nonumber
    \\
    \bar{\pi}_{t}
    & := &
        \frac{
            x^{t}
        }{
            n
        }
    \nonumber
    \\
    \bar{\pi}_{c}
    & := &
        \frac{
            x^{c}
        }{
            N - n
        }
    \\
    c_{t}
    & := &
        n
    \\
    c_{c}
    & := &
        N - n
    \nonumber
    \\
\end{eqnarray}
$$

Wald statiscs

$$
\begin{eqnarray}
    Y(x^{c}, x^{t})
    & := &
        \frac{
            \bar{\pi}_{c}
            -
            \bar{\pi}_{t}
        }{
            \sqrt{
                \frac{
                   \bar{\pi}_{t}(1 - \bar{\pi}_{t})
                }{
                    c_{t}
                }
                +
                \frac{
                   \bar{\pi}_{c}(1 - \bar{\pi}_{c})
                }{
                    c_{c}
                }
            }
        }
    \nonumber
\end{eqnarray}
$$

Score statistics

$$
\begin{eqnarray}
    Y(x^{c}, x^{t})
    & := &
        \frac{
            \bar{\pi}_{c}
            -
            \bar{\pi}_{t}
        }{
            \sqrt{
                \bar{\pi}(1 - \bar{\pi})
                \left(
                    \frac{
                        1
                    }{
                        c_{t}
                    }
                    +
                    \frac{
                       1
                    }{
                        c_{c}
                    }
                \right)
            }
        }
    \nonumber
\end{eqnarray}
$$


Let $\alpha \in [0, 1]$ be significance level.

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


Barnard exact model

* $X_{i}^{c}$,
    * i.i.d. of bernoulli r.v with probability $p_{c}$.
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$X_{i}^{c}(\omega) = x_{i}^{c} \ (i = 1, \ldots, N)$$,
* $X_{i}^{t}$,
    * i.i.d. of bernoulli r.v.with probability $p_{t}$
    * i.e. $$\{X_{i}^{t}\}$$ follows binomial distribution.
* $$X_{i}^{t}(\omega) = x_{i}^{t} \ (i = 1, \ldots, N)$$,

Score statistics of this contingency table is

$$
\begin{eqnarray}
    Y(x^{c}, x^{t})
    & \approx &
        1.8943380760602064
\end{eqnarray}
$$

One-side test

$$
\begin{eqnarray}
    \hat{p}(p)
    & = &
        \sum_{
            (\hat{x}^{c}, \hat{x}^{t}): Y(\hat{x}^{c}, \hat{x}^{t}) \ge Y(x^{c}, x^{t}))
        }
            f(\hat{x}^{c}, \hat{x}^{t})
\end{eqnarray}
$$

Let $\alpha \in [0, 1]$ be significance level.

## Reference
* [Lecture 14: Statistical Significance of 2x2 Contingency Tables, Part 2](https://www2.stat.duke.edu/courses/Spring12/sta10.1/Lectures/Lec14.pdf)
* [chi squared \- Which test for cross table analysis: Boschloo or Barnard? \- Cross Validated](https://stats.stackexchange.com/questions/169864/which-test-for-cross-table-analysis-boschloo-or-barnard)
* [breakfast\-club\-python/barnard\.py at master · roemera/breakfast\-club\-python](https://github.com/roemera/breakfast-club-python/blob/master/barnard/barnard.py)
