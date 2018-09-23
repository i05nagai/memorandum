---
title: Positive Definite Matrix
---

## Positive Definite Matrix

## Definition

#### Definition. Inequality for vector
* $$z = (z_{1}, \ldots, z_{N})^{\mathrm{T}} \in \mathbb{R}^{N}$$,

$$
\begin{eqnarray}
    z \ge 0
    & \overset{\mathrm{def}}{\Leftrightarrow} &
        \forall i,
        \
        z_{i} \ge 0
    \nonumber
    \\
    z \le 0
    & \overset{\mathrm{def}}{\Leftrightarrow} &
        \forall i,
        \
        z_{i} \le 0
\end{eqnarray}
$$

$z$ is said to be null vector if $$\forall i$$, $$z_{i} = 0$$.
This is equivalent to $$z \ge 0$$ and $z \le 0$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. positive definite matrix
* $$M$$,
    * $N \times N$

$M$ is positive definite matrix (p.s.d. for short) if

$$
    z \in \mathbb{R}^{N} \setminus \{0\},
    \
    z^{\mathrm{T}}Mz > 0
$$

We denote $$\mathcal{S}_{n}^{+}$$ as a set of all p.d.

<div class="end-of-statement" style="text-align: right">■</div>


#### Definition. nonnegative definite.
* $$M$$,
    * $N \times N$

$M$ is nonnegative definite matrix if

$$
    z \in \mathbb{R}^{N},
    \
    z^{\mathrm{T}}Mz \ge 0
$$

We denote $$\mathcal{S}_{n}^{\ge 0}$$ as a set of all nonnegative definite.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition. positive semidefinite.
* $$M$$,
    * $N \times N$

$M$ is positive semidefinite matrix if $M$ is nonnegative positve matrix but not positve definite.
That is, there are some nonnull vectors $z$ such that $$z^{\mathrm{T}}Mz = 0$$

We denote $$\mathcal{S}_{n}$$ as a set of all p.s.d.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition1 equivalence
The definition of p.d. are equivalent to

$$
\begin{equation}
    \exists r > 0,
    \
    \text{ s.t. }
    \
    \forall z \in B_{0, r} \setminus \{0\},
    \
    z^{\mathrm{T}}Mz > 0
    .
\end{equation}
$$

where $B_{0, r}$ is unit ball centered at 0,

$$
    a \in \mathbb{R}^{n},
    \
    r \in > 0,
    \
    B_{a, r}
    :=
    \{
        y \in \mathbb{R}^{n}
        \mid
        \|a - y \|
        \le
        r
    \}
    .
$$

#### proof
For any $$z \in \mathbb{R}^{n} \setminus \{0\}$$, letting $$t := \max_{i}|z_{i}|$$, $x := z / t$, $x \in B_{0, 1}$ and $z = tx$, that is,

$$
    \forall z \in \mathbb{R}^{n} \setminus \{0\},
    \
    \exists t > 0,
    \
    \exists x \in B_{0, 1} \setminus \{0\}
    \text{ s.t. }
    z = xt
    .
$$

Thus,

$$
\begin{eqnarray}
    & &
        \forall x \in B_{1} \setminus \{0\},
        \
        x^{\mathrm{T}}Mx
        > 0
    \nonumber
    \\
    & \Rightarrow &
        \forall t > 0,
        \
        \forall x \in B_{1} \setminus \{0\},
        \
        (tx)^{\mathrm{T}}M(tx)
        > 0
    \nonumber
\end{eqnarray}
    .
$$

Coverse is obvious.

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary2 equivalence
The definition of p.d. are equivalent to

$$
\begin{equation}
    \exists r > 0,
    \
    \exists a \in \mathbb{R}^{n},
    \
    \text{ s.t. }
    \
    \forall z \in B_{a, r} \setminus \{0\},
    \
    z - a \neq 0,
    \
    (z - a)^{\mathrm{T}}M(z - a) > 0
    .
\end{equation}
$$

#### proof
$z - a \in B_{0, r}$ if and only if $z \in B_{a, r}$.
The result is immediate consequence of the previous proposition.

<div class="QED" style="text-align: right">$\Box$</div>

#### Remark.
* If $M$ is positve definite, then $M$ is nonnegative definite.
* If $M$ is positve semidefinite, then $M$ is nonnegative definite.
* Since $$x^{\mathrm{T}}I_{n}x = \sum_{i=1}^{n}x_{i}^{2}$$, $$I_{n}$$ is positive definite.
* Since $$x^{\mathrm{T}}J_{n}x = (\sum_{i=1}^{n}x_{i})^{2}$$, $$J_{n}$$ is nonnegative definite.
    * But not positive definite so that $J$ is positive semidefinite.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definitions. nonpositive definite, negative definite, negative semidefinite
* $$M$$,
    * $n \times n$


<div class="QED" style="text-align: right">$\Box$</div>


#### Lemma1
* $$A := (a_{j}^{i})$$,
    * $n \times n$ matrix
* $$B := (b_{j}^{i})$$,
    * $n \times n$ matrix

Then

$$
\begin{eqnarray}
    & &
        \forall x,
        \
        x^{\mathrm{T}}Ax
        =
        x^{\mathrm{T}}Bx
    \nonumber
    \\
    & \Leftrightarrow &
        \forall i = 1, \ldots, n,
        \
        a_{i}^{i} = b_{i}^{i}
        ,
        \quad
    \nonumber
    \\
    & &
        \forall j, k = 1, \ldots, n,
        \
        a_{k}^{j} + a_{j}^{k}
        =
        b_{k}^{j} + b_{j}^{k}
    \nonumber
\end{eqnarray}
$$

#### proof.
($\Rightarrow$)
Let $$e_{i}$$ be $i$-th unit vector.
By assumption, we observe that

$$
    a_{i}^{i}
    =
    e_{i}^{\mathrm{T}}Ae_{i}
    =
    e_{i}^{\mathrm{T}}Be_{i}
    =
    b_{i}^{i}
    .
$$

Moreover let $$e_{i}$$, $$e_{j}$$ be $i$-th and $j$-th unit vector.

$$
\begin{eqnarray}
    a_{i}^{i}
    +
    a_{j}^{i}
    +
    a_{i}^{j}
    +
    a_{j}^{j}
    & = &
        e_{i}^{\mathrm{T}}
            A
            e_{i}
        +
        e_{j}^{\mathrm{T}}
            A
            e_{i}
        +
        e_{i}^{\mathrm{T}}
            A
            e_{j}
        +
        e_{j}^{\mathrm{T}}
            A
            e_{j}
    \nonumber
    \\
    & = &
        (e_{i} + e_{j})^{\mathrm{T}}
            A
            e_{i}
        +
        (e_{i} + e_{j})^{\mathrm{T}}
            A
            e_{j}
    \nonumber
    \\
    & = &
        (e_{i} + e_{j})^{\mathrm{T}}
            A
            (e_{i} + e_{j})
    \nonumber
    \\
    & = &
        (e_{i} + e_{j})^{\mathrm{T}}
            B
            (e_{i} + e_{j})
    \nonumber
    \\
    & = &
        b_{i}^{i}
        +
        b_{j}^{i}
        +
        b_{i}^{j}
        +
        b_{j}^{j}
    \nonumber
\end{eqnarray}
$$

($\Leftarrow$)
Let $x$ be arbitrary vector.
Since $x$ can be written $x = \sum_{i=1}^{n}x_{i}e_{i}$,

$$
\begin{eqnarray}
    x^{\mathrm{T}}Ax
    & = &
        (\sum_{i=1}^{n} x_{i}e_{i})^{\mathrm{T}}
            A
            \sum_{i=1}^{n} x_{i}e_{i}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            x_{i}^{2}e_{i}^{\mathrm{T}}Ae_{i}
        +
        \sum_{i \neq j}^{n}
            x_{i}
            x_{j}
            e_{i}^{\mathrm{T}}
            A
            e_{j}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            x_{i}^{2}a_{i}^{i}
        +
        \sum_{i = 1}^{n}
            \sum_{j > i}^{n}
            \left(
                x_{i}
                x_{j}
                a_{j}^{i}
                +
                x_{j}
                x_{i}
                a_{i}^{j}
            \right)
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            x_{i}^{2}b_{i}^{i}
        +
        \sum_{i = 1}^{n}
            \sum_{j > i}^{n}
            \left(
                x_{i}
                x_{j}
                b_{j}^{i}
                +
                x_{j}
                x_{i}
                b_{i}^{j}
            \right)
    \nonumber
    \\
    & = &
        x^{\mathrm{T}}Bx
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma2
* $$D := \mathrm{diag}(d_{1}, \ldots, d_{n})$$,
    * diagonal matrix

Then

* (1). $D$ is nonegative definite if and only if $$d_{1}, \ldots, d_{n}$$ are nonnegative.
* (2). $D$ is positive definite if and only if $$d_{1}, \ldots, d_{n}$$ are positve.
* (3). $D$ is positive semidefinite if and only if $$d_{1}, \ldots, d_{n}$$ are nonnegative and $$\mathrm{card}(\{i \mid d_{i} = 0\}) > 0$$.

#### proof.
These are obvious from the following calculation:

$$
    x^{\mathrm{T}}Dx
    =
    \sum_{i=1}^{n}
        d_{i}x_{i}^{2}
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>


#### Lemma3
* $$A \in \mathbb{R}^{n \times n}$$,
    * symmetric
    * nonnegative definite and nonpositive definite matrix

Then $M$ is null matrix.

#### proof.
For every vector $x \in \mathbb{R}^{n}$,

$$
    x^{\mathrm{T}}Ax
    \ge
    0,
    \
    x^{\mathrm{T}}Ax
    \le
    0,
$$

Then $$x^{\mathrm{T}}Ax = 0$$.
Since $A$ is symmetric so that by lemma1 $A = 0$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma4.
* $k \in \mathbb{N}$,
* $A \in \mathbb{R}^{n \times n}$,
    * positve definite (positve semidefinite)
* $B \in \mathbb{R}^{n \times n}$,
    * positve definite (positve semidefinite)

Then

* (1) If $A$ is positve definite (positve semidefinite), $kA$ is positve definite (resp. positve semidefinite).
* (2) If $A$ and $B$ are nonnegative definite, $A + B$ is nonnegative definite.
* (3) If $A$ is positive definite and $B$ is nonnegative definite, $A + B$ is positive definite.

#### proof.

$$
\begin{eqnarray}
    x^{\mathrm{T}}(kA)x
    & = &
        kx^{\mathrm{T}}Ax
        >
        0
    \nonumber
\end{eqnarray}
$$

and

$$
\begin{eqnarray}
    x^{\mathrm{T}}(A + B)x
    & = &
        x^{\mathrm{T}}Ax
        +
        x^{\mathrm{T}}Bx
        >
        0
    .
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma5
* $A \in \mathbb{R}^{n \times n}$
    * matrix
* $B \in \mathbb{R}^{n \times n}$
    * matrix

If $B + B^{\mathrm{T}} = A + A^{\mathrm{T}}$, then

$$
\begin{eqnarray}
    A \in \mathcal{S}_{n}^{+}
    & \Leftrightarrow &
        B \in \mathcal{S}_{n}^{+}
    \nonumber
    \\
    A \in \mathcal{S}_{n}
    & \Leftrightarrow &
        B \in \mathcal{S}_{n}
    \nonumber
    \\
    A \in \mathcal{S}_{n}^{\ge 0}
    & \Leftrightarrow &
        B \in \mathcal{S}_{n}^{\ge 0}
\end{eqnarray}
$$

#### proof.
It safies to show one of neccecity and sufficiency.
Suppose that $$A \in \mathcal{S}_{n}$$.
Since $$A + A^{\mathrm{T}} = (a_{j}^{i} + a_{i}^{j})$$,

$$
\begin{eqnarray}
    & &
        A + A^{\mathrm{T}}
        =
        B + B^{\mathrm{T}}
    \nonumber
    \\
    & \Leftrightarrow &
        \forall i = 1, \ldots, n,
        \
        a_{i}^{i} = b_{i}^{i}
        ,
        \quad
    \nonumber
    \\
    & &
        \forall j, k = 1, \ldots, n,
        \
        a_{k}^{j} + a_{j}^{k}
        =
        b_{k}^{j} + b_{j}^{k}
    .
    \nonumber
\end{eqnarray}
$$

Then applying lemma1 we obtain $$x^{\mathrm{T}}Ax = x^{\mathrm{T}}Bx$$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Lemma6
* $A$
    * positive definite matrix

Then $A$ is nonsingular.

#### proof.
We will prove that by contradiction.
Suppose $A$ is singular.
Then we have $\exists x \in \mathbb{R}^{n}$ such that $Ax = 0$ and $x$ is a nonnull vector..
This implies

$$
    x^{\mathrm{T}}Ax
    =
    0
    .
$$

Hence $A$ is not positive definite.
<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem7
* $A \in \mathbb{R}^{n \times n}$,
    * matrix
* $P \in \mathbb{R}^{n \times m}$,
    * matrix

Then

* (1) If $A$ is nonnegative definite, then $$P^{\mathrm{T}}AP$$ is nonnegative definite.
* (2) If $A$ is nonnegative definite and $$\mathrm{rank}(P) < m$$, then $$P^{\mathrm{T}}AP$$ is positive semidefinite.
* (3) If $A$ is positive definite and $$\mathrm{rank}(P) = m$$, then $$P^{\mathrm{T}}AP$$ is positive definite.

#### proof.
proof of (1).
Since $A$ is nonnegative definite, we observe

$$
    x^{\mathrm{T}}P^{\mathrm{T}}APx
    =
    (Px)^{\mathrm{T}}APx
    \ge
    0
    .
$$

proof of (2).
By (1), $A$ is nonnegative definite so that $P^{\mathrm{T}}AP$ is nonnegative definite.
For arbitrary matrix $B$, $C$, $\mathrm{rank}(AB) \le \mathrm{rank}(B)$.
Hence

$$
    \mathrm{rank}(P^{\mathrm{T}}AP)
    \le
    \mathrm{rank}(P)
    <
    m
    .
$$

This implies $P^{\mathrm{T}}AP$ is singular so that $P^{\mathrm{T}}PA$ is not positive definite.
Hence $P^{\mathrm{T}}AP$ is positive semidefinite matrix.

proof of (3).
$A$ is positive definite so that $(Px)^{\mathrm{T}}APx = 0$ is attained only when $Px = 0$.
Since $P$ is nonsigular, $Px = 0$ implies $x = 0$.

<div class="QED" style="text-align: right">$\Box$</div>

#### Corollary8

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 9
* $x := (x^{i})_{i} \in \mathbb{R}^{n}$,
* $A, B \in \mathbb{R}^{n \times n}$,
    * positive definite
* $y_{j} := (y_{j}^{i})_{i} \in \mathbb{R}^{n}$,

Then

(1) $xx^{\mathrm{T}}$ is positive definite.

(2) $A + B$ is positive definite.

(3) $\sum_{j=1}^{K}y_{j}y_{j}^{\mathrm{T}}$ is positive definite.


#### proof.
(1)

$$
\begin{eqnarray}
    \forall y \in \mathbb{R}^{n},
    \
    y^{\mathrm{T}}
    xx^{\mathrm{T}}
    y
    & = &
        (x^{\mathrm{T}}y)^{\mathrm{T}}
        x^{\mathrm{T}}
        y
    \nonumber
    \\
    & = &
        \|x^{\mathrm{T}}y\|^{2}
    \nonumber
    \\
    & \ge &
        0
    .
    \nonumber
\end{eqnarray}
$$

Moreover, if $y \neq 0$,

$$
\begin{eqnarray}
    & &
        \|x^{\mathrm{T}}y\|^{2}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \forall i,
        \
        x_{i}
        =
        0
    .
    \nonumber
\end{eqnarray}
$$

(2)


$$
\begin{eqnarray}
    \forall y \in \mathbb{R}^{n} \setminus \{0\},
    \
    y^{\mathrm{T}}
    (A + B)
    y
    & = &
        y^{\mathrm{T}}
        A
        y
        +
        y^{\mathrm{T}}
        B
        y
    \nonumber
    \\
    & > &
        0
    .
    \nonumber
\end{eqnarray}
$$

(3)

From (1), for all $j = 1, \ldots, K$, $y_{j}y_{j}^{\mathrm{T}}$ is positive definite.
Then by (2) the some of $y_{j}y_{j}^{\mathrm{T}}$ is positive definite.

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition 10
* $A \in \mathbb{R}^{n \times n}$,
    * positive semidefinite
* $B \in \mathbb{R}^{n \times n}$,
    * positive semidefinite

Then

(1) there exists $C \in \mathbb{R}^{n \times n}$ such that

$$
    A
    =
    C
    C
    .
$$

We denote $C$ by $A^{-1}$.

(2) if $A - B$ is positive semidefinite, $A^{1/2} - B^{1/2}$ is semidefinite

#### proof
(1)

Since $A$ is symmetric, by <a href="{{ site.baseurl }}/math/eigenvalue.html#theorem10.orthogonal-diagonalization"> proposition</a>, $A$ is orthogonalizable.

$$
\begin{eqnarray}
    A
    & = &
        V
        D
        V^{-1}
    \nonumber
    \\
    D
    & = &
        \mathrm{diag}(\lambda_{1}(A), \ldots, \lambda_{n}(A))
    \nonumber
    \\
    V
    & = &
        (v_{1}, \ldots, v_{n})
\end{eqnarray}
$$

where $v_{i} \in \mathbb{R}^{n}$ is an eigenvector corresponding to the eigenvalue $\lambda_{i}(A)$.
We define

$$
\begin{eqnarray}
    D^{1/2}
    & := &
        \mathrm{diag}(\lambda_{1}(A)^{1/2}, \ldots, \lambda_{n}(A)^{1/2})
    \nonumber
    \\
    C^{1/2}
    & := &
        V
        D^{1/2}
        V^{-1}
    .
    \nonumber
\end{eqnarray}
$$

Since $A$ is positive semidefinite, the square root of a eigenvalue exists.

$$
\begin{eqnarray}
    C 
    C
    & = &
        VD^{1/2}V^{-1}
        VD^{1/2}V^{-1}
    \nonumber
    \\
    & = &
        VDV^{-1}
    \nonumber
    \\
    & = &
        A
    .
    \nonumber
\end{eqnarray}
$$

(2)

$$
\begin{eqnarray}
    A^{1/2} - B^{1/2}
    & = &
        V_{A}D_{A}^{1/2}V_{A}^{-1}
        -
        V_{B}D_{B}^{1/2}V_{B}^{-1}
    \nonumber
    \\
    & = &
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [Positive-definite matrix - Wikipedia](https://en.wikipedia.org/wiki/Positive-definite_matrix)
