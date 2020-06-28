---
title: Homotopy
---

## Homotopy


#### Definition homotopy
* $X$,
    * top sp
* $I := [0, 1]$,
* $f: I \rightarrow X$,
    * continuous map
* $g: I \rightarrow X$,
    * continuous map
* $H: I \times I \rightarrow X$,
    * continuous map

$H$ is sait to be homotopy between $f$ and $g$.

$$
    H(0, t)
    :=
    f(t),
    \
    H(1, t)
    :=
    g(t).
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition homotop
* $X$,
    * top sp
* $I := [0, 1]$,
* $f: I \rightarrow X$,
    * continuous map
* $g: I \rightarrow X$,
    * continuous map

$f$ and $g$ is said to be homotop if there exists homotopy $H$ between $f$ and $h$.
We write $f \cong g$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
Homotop is a equivalence relation.
Let $f \cong \cong h$ and $H_{1}$ and $H_{2}$ be homotopy of $f \cong g$ and $g \cong h$ respecitvely.
We'll show that $f \cong h$.
Let

$$
    H(s, t)
    :=
    \begin{cases}
        H(2s, t)
        &
            (0 \le s \le 1/2)
        \\
        H(2s - 1, t)
        &
            (1/2 \le s \le 1)
    \end{cases}
    .
$$

$H$ is a homotopy between $f$ and $h$.
Reflective and symmetric properties are obvious.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition
* $f:I \rightarrow X$,
    * path

$$
    [f]
    :=
    \{
        g: \mathrm{pat}
        \mid
        f \cong g
    \}
    .
$$

$$
    f^{-1}(t)
    :=
    f(1 - t)
    .
$$

$$
    0_{x}(t)
    \equiv
    x
    .
$$

For any $x, y \in X$, a set of path from $x$ to $y$ $P(X; x, y)$ is defind

$$
    P(X; x, y)
    :=
    \{
        f: I \rightarrow X: \mathrm{continueous map}
        \mid
        f(0) = x,
        \
        f(1) = y
    \}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition fundamental group
* $X$,
    * top sp.
* $x \in X$,

Let

$$
    \pi(x, X)
    :=
    P(X; x, x)
    /
    \cong
    .
$$

We define multiplication is defined

$$
    [f] [g]
    :=
    [fg]
    .
$$

The inverse is $[f]^{-1} := [f^{-1}]$.
And unit is $[0_{x}]$.

$pi(x, X)$ is called a fundamental group.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
$pi(x, X)$ is a group.

Indeed, $[f][g]$ is well-defined.
Let $f^{\prime}$ and $g^{\prime}$ be another element in $[f]$ and $[g]$ respecitvely.
We'll show that $[fg] = [f^{\prime}g^{\prime}]$.
There eixst homotopies

$$
\begin{eqnarray}
    H_{f}(0, t)
    & = &
        f(t)
    \nonumber
    \\
    H_{f}(1, t)
    & = &
        f^{\prime}(t)
    H_{g}(0, t)
    & = &
        g(t)
    \nonumber
    \\
    H_{g}(1, t)
    & = &
        g^{\prime}(t)
    \nonumber
    .
\end{eqnarray}
$$

Let $H$ be

$$
    H(s, t)
    :=
    \begin{cases}
        H(s, 2t)
        &
            (0 \le t \le 1/2)
        \\
        H(s, 2t - 1)
        &
            (1/2 \le t \le 1)
    \end{cases}
    .
$$

$H$ is homotopy betwee $f * g$ and $f^{\prime} * g^{\prime}$.

$$[0_{x}]$$ is unit.
We'll show that $[0_{x}][f] = [f]$.
Let

$$
    H(s, t)
    :=
    \begin{cases}
        x
        &
            (0 \le t \le (-s + 1) / 2)
        \\
        f((2t - s - 1) / (s + 1))
        &
            ( (-s + 1) / 2 \le t \le 1)
    \end{cases}
    .
$$

Particularly,

$$
\begin{eqnarray}
    H(0, t)
    & = &
        \begin{cases}
            x
            &
                (0 \le t \le 1 / 2)
            \\
            f(2t - 1)
            &
                (1/ 2 \le t \le 1)
        \end{cases}
    \nonumber
    \\
    H(1, t)
    & = &
        f(t)
        \
        (0 \le t \le 1)
\end{eqnarray}
$$

$H$ is homotopy between $0_{x} * f$ and $f$.

Lastly, we'll show that $[f] [f^{-1}] = [0_{x}]$.
Let

$$
    H(s, t)
    :=
    \begin{cases}
        f(2t)
        &
            (0 \le t \le s/2)
        \\
        f(s)
        &
            (s/2 \le t \le 1 - t/2)
        \\
        f(2 - 2s)
        &
            (1 - s/2 \le t \le 1)
    \end{cases}

$$

$$
\begin{eqnarray}
    H(0, t)
    & = &
        \begin{cases}
            f(2t)
            &
                (0 \le t \le 0)
            \\
            f(0)
            &
                (0 \le t \le 1)
        \end{cases}
    \nonumber
    \\
    H(0, t)
    & = &
        \begin{cases}
            f(2t)
            &
                (0 \le t \le 0)
            \\
            f(0)
            &
                (0 \le t \le 1)
        \end{cases}
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
- http://www.math.tsukuba.ac.jp/~tasaki/lecture/ln2019/diffgeoI2019-dist.pdf
