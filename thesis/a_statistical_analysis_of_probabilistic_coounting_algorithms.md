---
title: A Statistical Analysis of Probabilistic Counting Algorithms
---

## A Statistical Analysis of Probabilistic Counting Algorithms


## 3 Order statistics
Maximal term sketch.

### 3.1 Continuous random variables
- $T \in \mathbb{N}$,
    - terminal time
- $\mathcal{I}$,
    - data types
- $(i_{t}, d_{t}) \ i_{t} \in \mathcal{I}, \ d_{t} \mathbb{Z}$ $(t = 1, \ldots, T)$
    - $i_{t}$ observed data type at $t$
    - $d_{t}$ quantity

$$
    i \in \mathcal{I},
    \
    a_{i}(T)
    :=
    \sum_{i=1}^{T}
        d_{t} 1_{\{i_{t} = i\}}
    .
$$

What we want to calcualte is

$$
    c_{count}
    :=
    \sum_{i \in \mathcal{I}}
        1_{\{a_{i}(T) > 0\}}
    .
$$

### 3.2

#### Proposition 1
- $m \in \mathbb{N}$,
- $f(y; c) := cy^{c - 1}$ where $y \in (0, 1)$
- $Y_{i}$ whose p.d.f. is $f$

$$
    c_{MLE}
    =
    \frac{
        -m
    }{
        \sum_{j=1}^{m}  \log Y_{j}
    }
    .
$$

#### proof
Log of the likelihood is

$$
\begin{eqnarray}
    L(y_{1}, \ldots, y_{m}; c)
    & := &
        \log \prod_{j=1}^{m} f(y_{i})
    \nonumber 
    \\
    & = &
        \sum_{j=1}^{m}
            \log c y_{i}^{c-1}
    \nonumber 
    \\
    & = &
        m\log c
        +
        (c - 1)
        \sum_{j=1}^{m}
            \log y_{i}
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        \frac{
            \partial L(y_{1}, \ldots, y_{m}; c)
        }{
            \partial c
        }
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \frac{
            m
        }{
            c
        }
        +
        \sum_{j=1}^{m}
            \log y_{i}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        c
        =
        +
        =
        \frac{
            -m
        }{
            \sum_{j=1}^{m}
                \log y_{i}
        }
    .
\end{eqnarray}
$$

$c_{MLE}$ converges in distribution $N(c, c^{2}/m)$ by MLE estimator.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 2
- $0 < k < c$,
- $h_{j} \sim U(0, 1)$,
    - i.i.d. uniformly distributed on $(0, 1)$
- $Y_{j}$
    - $k$-th order statistc of $h_{j}$


$$
\begin{eqnarray}
    L(y_{1}, \ldots, y_{m}; c)
    & := &
        \log (\prod_{j=1}^{m} f(y))
    \nonbumber
    \\
    & = &
        \sum_{j=1}^{m}
            \log f(y)
\end{eqnarray}

$$

#### proof

<div class="QED" style="text-align: right">$\Box$</div>


## Reference

