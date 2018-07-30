---
title: Rademacher Distribution
---

## Rademacher Distribution
Discrete distribution.


$\mathrm{Rad}(k)$ is a p.d.f. of Rademacher distribution,

$$
\begin{eqnarray}
    \mathrm{Rad}(k)
    & := &
        \begin{cases}
            \frac{1}{2}
            &
                k = \pm
            \\
            0
            &
                \text{otherwise}
        \end{cases}
    \nonumber
    \\
    & = &
        \frac{1}{2}
        \left(
            \delta_{k-1}
            +
            \delta_{k+1}
        \right)
    \nonumber
\end{eqnarray}
    .
$$

where $\delta_{a}$ is dirac delta function 


### Proposition1. 
* $(\phi_{n})_{n \in \mathbb{N}}$,
    * a sequence of independent symmetric real-valued random variables
* $(r_{n}) _{n \in \mathbb{N}}$,
    * Rademacher sequence independent of $(\phi_{n})_{n \in \mathbb{N}}$,

Then

$(\phi_{n})$ and $$(r_{n}|
\phi_{n}
|)_{n \in \mathbb{N}}$$ are identically distribuited.

### proof.
For all $n \in \mathbb{N}$, and all borrel set $B$,

$$
\begin{eqnarray}
    P(r_{n}|\phi_{n}| \in B)
    & = &
        P(r_{n} = 1, \phi_{n} \ge 0, \phi_{n} \in B)
        +
        P(r_{n} = 1, \phi_{n} < 0, \phi_{n} \in -B)
    \nonumber
    \\
    & &
        +
        P(r_{n} = -1, \phi_{n} \ge 0, \phi_{n} \in -B)
        +
        P(r_{n} = -1, \phi_{n} < 0, \phi_{n} \in B)
    \nonumber
    \\
    & = &
        \frac{1}{2}
        P(\phi_{n} \ge 0, \phi_{n} \in B)
        +
        \frac{1}{2}
        P(\phi_{n} < 0, \phi_{n} \in -B)
    \nonumber
    \\
    & &
        +
        \frac{1}{2}
        P(\phi_{n} \ge 0, \phi_{n} \in -B)
        +
        \frac{1}{2}
        P(\phi_{n} < 0, \phi_{n} \in B)
        \quad
        (\because \text{independence})
    \nonumber
    \\
    & = &
        P(\phi_{n} \ge 0, \phi_{n} \in B)
        +
        P(\phi_{n} < 0, \phi_{n} \in -B)
    \nonumber
    \\
    & &
        P(\phi_{n} \in B)
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Definition. Rademacher average
* $n \in \mathbb{N}$,
* $A \subseteq \mathbb{R}^{n}$,
* $r_{i} \ (i = 1, \ldots, n)$,
    * independent random variables with Rademacher distribution,

$$
    R_{n}(A)
    :=
    \mathrm{E}
    \left[
        \sup_{a \in A}
            \frac{1}{n}
            \sum_{i=1}^{n}
                r_{i}
                a_{i}
    \right]
$$

is called Randemacher average.

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition 2
* $A \subseteq \mathbb{R}^{n}$,
    * symmetric (i.e. $a \in A$ if and only if $-a \in A$)

Then

$$
    R_{n}(A)
    =
    \mathrm{E}
    \left[
        \sup_{a \in A}
            \frac{1}{n}
            \left|
                \sum_{i=1}^{n}
                    r_{i}
                    a_{i}
            \right|
    \right]
$$

### proof

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition 3
* $A, B \subseteq \mathbb{R}^{n}$,
* $c \in \mathbb{R}^{n}$,

$$
\begin{eqnarray}
    R_{n}(A \cup B)
    & \le &
        R_{n}(A) + R_{n}(B)
    \\
    R_{n}(cA)
    & = &
        |c|R_{n}(A)
    \\
    R_{n}(A + B)
    & \le &
        R_{n}(A) + R_{n}(B)
\end{eqnarray}
$$

### proof

<div class="QED" style="text-align: right">$\Box$</div>

### lemma 4
* $\sigma > 0$,
* $$X_{1}, \ldots, X_{N}$$,
    * rela valued r.v.s with

$$
    \forall \lambda > 0,
    \
    1 \le i \le N,
    \
    \mathrm{E}
    \left[
        e^{\lambda X_{i}}
    \right]
    \le
    e^{\lambda^{2}\sigma^{2}/2}
    .
$$

Then

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \max_{i = 1, \ldots, N}
            X_{i}
    \right]
    \le
    \sigma
    \sqrt{
        2 \ln N
    }
\end{eqnarray}
$$

### proof
By Jensen's inequality, for all $\lambda > 0$,

$$
\begin{eqnarray}
    \exp
    \left(
        \lambda
        \mathrm{E}
        \left[
            \max_{i=1,\ldots, N}
                X_{i}
        \right]
    \right)
    & \le &
        \mathrm{E}
        \left[
            \exp
            \left(
                \lambda
                \max_{i=1,\ldots, N}
                    X_{i}
            \right)
        \right]
        \quad
        (\because \text{Jensen's inequality})
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \max_{i=1,\ldots, N}
            \exp
            \left(
                \lambda
                X_{i}
            \right)
        \right]
    \nonumber
    \\
    & \le &
        \sum_{i=1}^{N}
        \mathrm{E}
        \left[
            \exp
            \left(
                \lambda
                X_{i}
            \right)
        \right]
    \nonumber
    \\
    & \le &
        N
        \exp
        \left(
            \lambda^{2}
            \sigma^{2}
            /
            2
        \right)
        \quad
        (\because \text{assumption})
    \nonumber
    \\
    & = &
        \exp
        \left(
            \ln N
            +
            \lambda^{2}
            \sigma^{2}
            /
            2
        \right)
    \nonumber
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \max_{i = 1, \ldots, N}
            X_{i}
    \right]
    & \le &
        \frac{
            \ln N
        }{
            \lambda
        }
        +
        \frac{
            \lambda \sigma^{2}
        }{
            2
        }
    .
    \nonumber
\end{eqnarray}
$$

In particular, taking $\lambda := \sqrt{2 \ln N / \sigma^{2}}$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \max_{i = 1, \ldots, N}
            X_{i}
    \right]
    & \le &
        \frac{
            \sqrt{\ln N}
            \sigma
        }{
            \sqrt{2}
        }
        +
        \frac{
            \sigma \sqrt{\ln N}
        }{
            \sqrt{2}
        }
    \nonumber
    & = &
        \sqrt{\ln N}
        \sigma
        \sqrt{2}
    \nonumber
    .
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition 5
* $$A = \{a_{1}, \ldots, a_{N}\} \subseteq \mathbb{R}^{n}$$,
    * a finite set
    * $$a_{j} := (a_{j, 1}, \ldots, a_{j, n})$$,

$$
\begin{eqnarray}
    R_{n}(A)
    & \le &
        \max_{j = 1, \ldots, N}
        \|
            a_{j}
        \|_{1}
        \frac{
            \sqrt{2 \log N}
        }{
            n
        }
    \nonumber
    \\
    R_{n}(A)
    & \le &
        \max_{j = 1, \ldots, N}
        \|
            a_{j}
        \|_{2}
        \frac{
            \sqrt{2 \log N}
        }{
            \sqrt{n}
        }
\end{eqnarray}
$$

### proof
Let

$$
    X_{j}
    :=
    \frac{1}{n}
    \sum_{i=1}^{n}
        r_{i}a_{j, i}
    \quad
    (j \in = 1, \ldots, N)
    .
$$

It's easy to confirm that $$X_{j} \in [\underline{L}_{j}, \bar{L}_{j}]$$ almost surely where

$$
    \underline{L}_{j}
    :=
    -
    \frac{
        \|
        a_{j}
        \|_{2}
    }{
        \sqrt{n}
    }
    ,
    \
    \bar{L}_{j}
    :=
    -\underline{L}_{j}
    .
$$

Indeed,

$$
\begin{eqnarray}
    \frac{1}{n}
    \sum_{i=1}^{n}
        r_{i}a_{j, i}
    & \le &
        \frac{1}{n}
        \sum_{i=1}^{n}
            |
            a_{j, i}
            |
    \nonumber
    \\
    & = &
        \frac{1}{n}
        \|
        a_{j}
        \|_{1}
    \nonumber
    \\
    & \le &
        \frac{1}{\sqrt{n}}
        \|
        a_{j}
        \|_{2}
    .
    \nonumber
\end{eqnarray}
$$

Moreover, since $r_{j}$ is an I.I.D sequence, $X_{j}$ satisfies

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        X_{j}
    \right]
    =
    0
    .
\end{eqnarray}
$$

By Hoeffding inequality, we have for all $j = 1, \ldots, n$, $\lambda > 0$,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        e^{-\lambda X_{j}}
    \right]
    & \le &
        \exp
        \left(
            \mathrm{E}
            \left[
                -\lambda X_{j}
            \right]
            +
            \frac{
                \lambda^{2}(\bar{L}_{j} - \underline{L}_{j})^{2}
            }{
                8
            }
        \right)
    \nonumber
    \\
    & = &
        \exp
        \left(
            \frac{
                \lambda^{2}
                \|
                a_{j}
                \|_{1}^{2}
            }{
                2n^{2}
            }
        \right)
    \nonumber
    \\
    & \le &
        \exp
        \left(
            \frac{
                \lambda^{2}
                \sigma^{2}
            }{
                2
            }
        \right)
    \nonumber
    \\
    \sigma
    & := &
        \frac{
            \max_{j = 1, \ldots, N}
                \|
                a_{j}
                \|_{1}
        }{
            n
        }
        .
    \nonumber
\end{eqnarray}
$$


Now we can apply <a href="#lemma-4">lemma 4</a>,

$$
\begin{eqnarray}
    R_{n}(A)
    & = &
        \mathrm{E}
        \left[
            \max_{j = 1, \ldots, N}
                X_{j}
        \right]
    \nonumber
    \\
    & \le &
        \sigma
        \sqrt{2 \ln N}
        \quad
        (\because \text{lemma})
    \nonumber
    \\
    & = &
        \max_{j = 1, \ldots, N}
            \|
            a_{j}
            \|_{1}
        \frac{
            \sqrt{2 \ln N}
        }{
            n
        }
\end{eqnarray}
$$

For the other inequality, we know

$$
\begin{eqnarray}
    \|
    a_{j}
    \|_{1}
    & \le &
        \sqrt{n}
        \|
        a_{j}
        \|_{2}
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Rademacher distribution \- Wikipedia](https://en.wikipedia.org/wiki/Rademacher_distribution)
* https://ocw.tudelft.nl/wp-content/uploads/Lecture03.pdf
* Prediction, Learning, and Games
