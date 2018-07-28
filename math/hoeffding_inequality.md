---
title: Hoeffding Lemma
---

## Hoeffding Lemma

* $a, b \in \mathbb{R}$,
    * $a \le 0 \le b$,
* $X$,
    * $\mathbb{R}$ valued r.v.
    * $\mathrm{E}[X] = 0$,
    * $X \in [a, b]$ almost surely

Then

$$
    \forall \lambda \in \mathbb{R},
    \
    \mathrm{E}
    \left[
        e^{\lambda X}
    \right]
    \le
    \exp
    \left(
        \frac{
            \lambda^{2}
            (b - a)^{2}
        }{
            8
        }
    \right)
    .
$$

### proof.
Let $\lambda \in \mathbb{R}$ be fixed.
Since $e^{\lambda x}$ is a convex function of $x$, we have

$$
\begin{eqnarray}
    \forall x \in [a, b],
    \
    e^{\lambda x}
    & \le &
        e^{\lambda a}
        \frac{
            b - x
        }{
            b - a
        }
        +
        e^{\lambda b}
        \frac{
            x - a
        }{
            b - a
        }
    .
    \nonumber
\end{eqnarray}
$$

Taking expectation both sides replacing $x$ with $X$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        e^{sX}
    \right]
    & \le &
        e^{\lambda a}
        \frac{
            b - \mathrm{E}[X]
        }{
            b - a
        }
        +
        e^{\lambda b}
        \frac{
            \mathrm{E}[X] - a
        }{
            b - a
        }
    \\
    & = &
        e^{\lambda a}
        \frac{
            b
        }{
            b - a
        }
        -
        e^{\lambda b}
        \frac{
            a
        }{
            b - a
        }
    \nonumber
    \\
    & = &
        \frac{
            -a
        }{
            b - a
        }
        e^{\lambda a}
        \left(
            -
            \frac{
                b
            }{
                a
            }
            +
            e^{\lambda (b - a)}
        \right)
    \nonumber
    \\
    & = &
        \theta
        e^{ -(b - a) \theta\lambda}
        \left(
            -
            \frac{
                b - a
            }{
                a
            }
            -
            1
            +
            e^{\lambda (b - a)}
        \right)
    \nonumber
    \\
    & = &
        e^{-(b - a) \theta\lambda }
        \left(
            1
            -
            \theta
            +
            \theta
            e^{\lambda (b - a)}
        \right)
        \label{hoeffding_lemma_inequality}
\end{eqnarray}
$$

where $\theta := - \frac{a}{b - a}$.
We define $\phi: \mathbb{R} \rightarrow \mathbb{R}$ by

$$
    c \in \mathbb{R},
    \
    \phi(c)
    :=
    -\theta c
    +
    \log
    (1 - \theta + \theta e^{c})
    .
$$

$\phi$ is well-defined on $\mathbb{R}$.
Indeed,

$$
\begin{eqnarray}
    1 - \theta + \theta e^{c}
    & = &
        \theta
        \left(
            \frac{1}{\theta}
            -
            1
            +
            e^{c}
        \right)
    \nonumber
    \\
    & = &
        \theta
        \left(
            -
            \frac{b}{a}
            +
            e^{c}
        \right)
    \nonumber
    \\
    & > &
        0
        \quad
        (\because \theta > 0, \frac{b}{a} < 0)
    .
\end{eqnarray}
$$

Let $u := \lambda (b - a)$.
Then $$\eqref{hoeffding_lemma_inequality}$$ can be written

$$
    \mathrm{E}
    \left[
        e^{\lambda X}
    \right]
    \le
    e^{\phi(u)}
    .
$$

By taylor theorem, there exists $v \in [0, u]$ such that

$$
    \phi(c)
    =
    \phi(0)
    +
    u
    \phi^{\prime}(0)
    +
    \frac{1}{2}
    \phi^{\prime\prime}(v)
    .
$$

We have

$$
\begin{eqnarray}
    \phi(0)
    & = &
        0
    \nonumber
    \\
    \phi^{\prime}(c)
    & = &
        -\theta
        +
        \frac{
            1
        }{
            1 - \theta + \theta e^{c}
        }
        \theta e^{c}
    \nonumber
    \\
    \phi^{\prime}(0)
    & = &
        -\theta
        +
        \frac{
            1
        }{
            1 - \theta + \theta
        }
        \theta
    \nonumber
    \\
    & = &
        0
    \nonumber
    \\
    \phi^{\prime\prime}(c)
    & = &
        \frac{
            \theta
            e^{c}
            (1 - \theta + \theta e^{c})
            -
            \theta
            e^{c}
            \theta e^{c}
        }{
            (1 - \theta + \theta e^{c})^{2}
        }
    \nonumber
    \\
    & = &
        \frac{
            \theta
            e^{c}
        }{
            (1 - \theta + \theta e^{c})
        }
        \frac{
            (1 - \theta + \theta e^{c})
            -
            \theta
            e^{c}
        }{
            (1 - \theta + \theta e^{c})
        }
    \nonumber
    \\
    & = &
        \frac{
            \theta
            e^{c}
        }{
            (1 - \theta + \theta e^{c})
        }
        \left(
            1
            -
            \frac{
                \theta
                e^{c}
            }{
                (1 - \theta + \theta e^{c})
            }
        \right)
    \nonumber
    \\
    & = &
        t
        \left(
            1
            -
            t
        \right)
    \nonumber
    \\
    & = &
        -
        \left(
            t
            -
            \frac{1}{2}
        \right)^{2}
        +
        \frac{1}{4}
    \nonumber
    \\
    & \le &
        \frac{1}{4}
    \nonumber
    \\
    \phi^{\prime\prime}(v)
    & \le &
        \frac{ 1 }{ 4 }
    \nonumber
        .
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    \phi(u)
    & \le &
        \frac{1}{2}
        u^{2}
        \frac{1}{4}
    \nonumber
    \\
    & = &
        \frac{1}{8}
        u^{2}
    \nonumber
    \\
    & = &
        \frac{1}{8}
        s^{2}
        (b - a)^{2}
    \nonumber
\end{eqnarray}
    .
$$

Therefore,

$$
    \mathrm{E}
    \left[
        e^{\lambda X}
    \right]
    \le
    \exp
    \left(
        \frac{1}{8}
        s^{2}
        (b - a)^{2}
    \right)
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Heoffding inequality
* $X_{1}, \ldots, X_{N}$,
    * independent r.v.s
    * $X_{i} \in [0, 1]$,

$$
    \bar{X}
    :=
    \frac{1}{N}
    \sum_{i=1}^{N}
        X_{i}
    .
$$

Then $0 < t < \bar{X} - \mathrm{E}[\bar{X}]$,

$$
    P(
        \bar{X} - \mathrm{E}
        \left[
            \bar{X}
        \right]
        \ge
        t
    )
    \le
    e^{-2nt^{2}}
    .
$$

### proof.


<div class="QED" style="text-align: right">$\Box$</div>

### Heoffding inequality
* $[a_{i}, b_{i}] \subset \mathbb{R}$,
    * sequence of intervals
* $X_{1}, \ldots, X_{N}$,
    * independent r.v.s
    * $X_{i} \in [a_{i}, b_{i}]$,

$$
\begin{eqnarray}
    \bar{X}
    & := &
        \frac{1}{N}
        \sum_{i=1}^{N}
            X_{i}
    \nonumber
    \\
    S_{N}
    & := &
        X_{1} + \cdots + X_{N}
    \nonumber
\end{eqnarray}
    .
$$

For all $t \ge 0$,

$$
\begin{eqnarray}
    P(
        S_{N}
        -
        \mathrm{E}
        \left[
           S_{N} 
        \right]
        \ge
        t
    )
    & \le &
        \exp
        \left(
            -
            \frac{
                2t^{2}
            }{
                \sum_{i=1}^{N}
                    (b_{i} - a_{i})
            }
        \right)
    \label{hoeffding_inequality_inequality_statement_sum}
    \\
    P(
        \bar{X} - \mathrm{E}
        \left[
            \bar{X}
        \right]
        \ge
        t
    )
    & \le &
        \exp
        \left(
            -
            \frac{
                2N^{2}t^{2}
            }{
                \sum_{i=1}^{N}
                    (b_{i} - a_{i})
            }
        \right)
    \label{hoeffding_inequality_inequality_statement_mean}
    \\
    P(
        \left|
            \bar{X} - \mathrm{E}
            \left[
                \bar{X}
            \right]
        \right|
        \ge
        t
    )
    & \le &
        2
        \exp
        \left(
            -
            \frac{
                2N^{2}t^{2}
            }{
                \sum_{i=1}^{N}
                    (b_{i} - a_{i})
            }
        \right)
        \label{hoeffding_inequality_inequality_statement_absolute}
\end{eqnarray}
$$

### proof.
We first prove $$\eqref{hoeffding_inequality_inequality_statement_sum}$$.

Let $s, t \ge 0$ be fixed.

$$
\begin{eqnarray}
    P(S_{N} - \mathrm{E} \left[ S_{N}\right] \ge t)
    & \le &
        e^{-st}
        \mathrm{E}
        \left[
            \exp
            \left(
               s
               (S_{N} - \mathrm{E}[ S_{N}] )
            \right)
        \right]
        \quad
        (\because \text{apply Markov inequality with } \phi(t) := e^{st})
    \nonumber
    \\
    & = &
        e^{-st}
        \prod_{i=1}^{N}
            \mathrm{E}
            \left[
                \exp
                \left(
                   s
                   (X_{i} - \mathrm{E} \left[ X_{i} \right] )
                \right)
            \right]
        \quad
        (\because \text{independence})
    \nonumber
    \\
    & \le &
        e^{-st}
        \prod_{i=1}^{N}
            \exp
            \left(
               \frac{1}{8}
               s^{2}
               (b_{i} - a_{i})^{2}
            \right)
        \quad
        (\because \text{Hoeffding lemma})
    \nonumber
    \\
    & = &
        \exp
        \left(
            -st
            +
            \frac{1}{8}
            s^{2}
            \sum_{i=1}^{N}
                (b_{i} - a_{i})^{2}
        \right)
    \label{hoeffding_inequality_inequality_derived}
    .
\end{eqnarray}
$$

Define $g: \mathbb{R} \rightarrow \mathbb{R}$

$$
\begin{eqnarray}
    g(c)
    & := &
        -ct
        +
        \frac{c^{2}}{8}
        \sum_{i=1}^{N}
            (b_{i} - a_{i})^{2}
    \nonumber
    \\
    & = &
        \frac{A}{8}
        \left(
            c
            -
            t
            \frac{
                4
            }{
                A
            }
        \right)^{2}
        -
        \frac{2t^{2}}{A}
    .
\end{eqnarray}
$$

where $A := \sum_{i=1}^{N} (b_{i} - a_{i})^{2}$.
$g$ achieves the minimum at

$$
    c
    =
    -\frac{2t^{2}}{A}
    .
$$

Hence $$\eqref{hoeffding_inequality_inequality_derived}$$ can be written

$$
    P(S_{N} - \mathrm{E} \left[ S_{N}\right] \ge t)
    \le
    \exp
    \left(
        -\frac{
            2t^{2}
        }{
            \sum_{i=1}^{N}
                (b_{i} - a_{i})^{2}
        }
    \right)
    .
$$

$$\eqref{hoeffding_inequality_inequality_statement_mean}$$ is immediate consequence of $$\eqref{hoeffding_inequality_inequality_statement_sum}$$ by taking $t$ as  $Nt$.
We show $$\eqref{hoeffding_inequality_inequality_statement_absolute}$$.

$$
\begin{eqnarray}
    P(
        \left|
            \bar{X} - \mathrm{E}
            \left[
                \bar{X}
            \right]
        \right|
        \ge
        t
    )
    & = &
        P
        \left(
            (
                \bar{X}
                -
                \mathrm{E}
                \left[
                    \bar{X}
                \right]
                \ge
                t
            )
            \cap
            (
                \bar{X}
                -
                \mathrm{E}
                \left[
                    \bar{X}
                \right]
                \ge
                0
            )
        \right)
        +
        P
        \left(
            (
                -
                (
                    \bar{X}
                    -
                    \mathrm{E}
                    \left[
                        \bar{X}
                    \right]
                )
                \ge
                t
            )
            \cap
            (
                \bar{X}
                -
                \mathrm{E}
                \left[
                    \bar{X}
                \right]
                \le
                0
            )
        \right)
    \nonumber
    \\
    & \le &
        \exp
        \left(
            -\frac{
                2N^{2}t^{2}
            }{
                \sum_{i=1}^{N}
                    (b_{i} - a_{i})^{2}
            }
        \right)
        +
        \exp
        \left(
            -\frac{
                2N^{2}t^{2}
            }{
                \sum_{i=1}^{N}
                    (b_{i} - a_{i})^{2}
            }
        \right)
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Hoeffding's lemma \- Wikipedia](https://en.wikipedia.org/wiki/Hoeffding%27s_lemma)
* [Hoeffding's inequality \- Wikipedia](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality)
