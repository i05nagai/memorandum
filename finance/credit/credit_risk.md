---
title: Credit Risk
---

## Credit Risk


* Structual form
    * In structual form, we call default when the value of a company is less than the amount of company's debt
    * we could interpret this situation as call option
* Reduced form
    * reduced form constructs a model of a company's default probability or credit risk


* $R_{t}$,
    * survival time from $t$

* $\mathcal{T} := [0, T]$,
    * for continuous r.v.
* $\mathcal{T} := {0, \ldots, T}$,
    * for discrete r.v.
* $$\{\mathcal{F}_{t}\}_{\mathcal{T}}$$,
    * filtrations
* $P_{t}: \mathcal{F} \rightarrow [0, 1]$,
    * $P_{t}(A) := P(A \mid \mathcal{F}_{t})$,
    * conditonal probability measure


#### cumulative default probability

$$
    F_{t, PD}(x)
    :=
    P(R_{t} \ge x \mid \mathcal{F}_{t})
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### survival probability

$$
    P_{t}(R_{t} > x)
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### discrete hazart rate
* $R_{t}$
    * discrete r.v.
    * survival time from $t$

Hazard rate is the probability that survival rate is exactly $n$ under 

$$
    h_{t}(n)
    :=
    P_{t}(R = n \mid R \ge n)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### continuous hazart rate
* $R_{t}$,
    * continuous r.v.
    * survival time from $t$

Survival rate from $t$ $S_{t}: \Omega \rightarrow [0, 1]$

$$
    S_{t}(x)
    :=
    P_{t}(R \ge x)
    .
$$

Suppose that $S_{t}(x)$ is differentiable with respect to $x$. Then hazard rate is defined as

$$
    h_{t}(x)
    :=
    -
    \frac{d }{d x}
        \ln S_{t}(x)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
Hazard rate is a instantaneous rate that a company survive at time $x$ and then a company fails to survive right after time $x$.

$$
\begin{eqnarray}
    \lim_{y \rightarrow 0}
        \frac{
            P_{t}(R < x + y \mid R \ge x)
        }{
            y
        }
    & = &
    \lim_{y \rightarrow 0}
        \frac{
            \frac{
                P_{t}(x \le R < x + y)
            }{
                P_{t}(R \ge x)
            }
        }{
            y
        }
    \nonumber
    \\
    & = &
    \lim_{y \rightarrow 0}
        \frac{
            P_{t}(R < x + y)
            -
            P_{t}(x > R)
        }{
            y
            S_{t}(x)
        }
    \nonumber
    \\
    & = &
    \lim_{y \rightarrow 0}
        \frac{
            (1 - S(x + y))
            -
            (1 - S(x))
        }{
            y
            S_{t}(x)
        }
    \nonumber
    \\
    & = &
    \lim_{y \rightarrow 0}
        \frac{
            - S(x + y)
            +
            S(x)
        }{
            y
            S_{t}(x)
        }
    \nonumber
    \\
    & = &
        -
        \frac{
            S^{\prime}(x)
        }{
            S_{t}(x)
        }
    \nonumber
    \\
    & = &
        -
        \frac{d }{d x} 
            \ln S_{t}(x)
    \nonumber
    \\
    & = &
        h_{t}(x)
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
