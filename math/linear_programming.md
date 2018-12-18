---
title: Linear Programming
---

## Linear Programming

#### Theorem1 Farkas
* $A \in \mathbb{R}^{m \times n}$,
    * $$A = (a_{1}, \ldots, a_{n})$$,
* $c \in \mathbb{R}^{n}$,

Then following statemetns are selective.
(i.e. If (1) holds, then (2) cannot hold. Vice versa if (2) hold, then (1) cannot hold)

(1)

$$
\begin{eqnarray}
    \exists x \in \mathbb{R}^{n},
    \
    \text{ s.t. }
    \quad
    \langle c, x \rangle
    & > &
        0,
    \nonumber
    \\
    Ax
    & \le &
        0,
    \nonumber
\end{eqnarray}
$$

(2)

$$
\begin{eqnarray}
    \exists y \in \mathbb{R}^{m},
    \
    \text{ s.t. }
    \
    & &
        A^{\mathrm{T}}y = c
    \nonumber
    \\
    & &
        y \ge 0,
    \nonumber
\end{eqnarray}
$$

### proof.
(1) $$\Rightarrow$$ not (2)

Let

$$
    S
    :=
    \{
        x \in \mathbb{R}^{n}
        \mid
        x = A^{\mathrm{T}}y,
        \
        y \ge 0
    \}
    .
$$

$S$ is closed convex set.
Suppose that (2) does not hold.
By <a href="{{ site.baseurl }}/math/convex_function.html#theorem12-separation-theorem-between-a-point-and-a-set">separation theorem between a point and a set</a>, there exist $$\alpha \in \mathbb{R}$$ and $$c \in \mathbb{R}^{n}$$ such that

$$
\begin{eqnarray}
    & &
        \langle a, c \rangle
        >
        \alpha
    \nonumber
    \\
    \forall x \in S,
    \quad
    & &
        \langle a, x \rangle
        \le
        \alpha
    .
\end{eqnarray}
$$

Since $0 \in S$, substituing $x=0$ into the equation above we have

$$
    \langle a, 0 \rangle
    =
    0
    \le
    \alpha
$$

It follows that $\langle a, c \rangle > 0$.
Next, for all $y \ge 0$, 

$$
\begin{eqnarray}
    \alpha
    & \ge &
        \langle a, x \rangle
    \nonumber
    \\
    & \ge &
        \langle a, A^{\mathrm{T}}y \rangle
    \nonumber
    \\
    & = &
        \langle Aa, y \rangle
    .
    \nonumber
\end{eqnarray}
$$

Then $$Aa \le 0$$.
Indeed, if $$Aa > 0$$, there exists $$i \in \{1, \ldots, m\}$$ such that $$(Aa)_{i} > 0$$.
This is contradiction since

$$
    \forall y \in \mathbb{R}^{n},
    \quad
    \langle y, Aa \rangle
    \le
    \alpha
    .
$$

not (1) $$\Leftarrow$$ (2)

Suppose there exists $$x \in \mathbb{R}^{n}$$ such that $$Ax \le 0$$.
Then

$$
\begin{eqnarray}
    \langle c, x \rangle
    & = &
        \langle A^{\mathrm{T}}y, x \rangle
    \nonumber
    \\
    & = &
        \langle y, Ax \rangle
        \le
        0
        \quad
        (\because Ax \le 0,\ y \ge 0)
    .
    \nonumber
\end{eqnarray}
$$

Hence (1) cannot hold.

<div class="QED" style="text-align: right">$\Box$</div>

### Remark2
<a href="#theorem1-farkas">farkas's theorem</a> is equivalent that not (1) if and only if (2), that is,

$$
\begin{eqnarray}
    \forall x \in \mathbb{R}^{n},
    \quad
    (
        \langle c, x \rangle > 0
        \Rightarrow
        Ax \ge 0
    )
    \text{ or }
    (
        \langle c, x \rangle \le 0
        \Rightarrow
        Ax < 0
    )
\end{eqnarray}

$$


<div class="end-of-statement" style="text-align: right">■</div>

### Lemma2 Homogeneous Farkas Lemma
* $c \in \mathbb{R}^{n}$,
* $$a^{i} \in \mathbb{R}^{n}$$,

Then following statmeents are equivalent:

(1) Inequality system below has no solution in $\mathbb{R}^{n}$

$$
\begin{eqnarray}
    \langle c, x \rangle
    & < &
        0
    \nonumber
    \\
    \langle a^{i}, x \rangle
    & \ge &
        0
        \quad
        i = 1, \ldots, m
\end{eqnarray}
$$

(2)

$$
    \exists y \ge 0,
    \
    \text{ s.t. }
    \
    c
    =
    \sum_{i=1}^{m}
        y_{i}a^{i}
$$

### proof

$$
    A
    :=
    \left(
        \begin{array}{c}
            a^{1}
            \\
            \vdots 
            \\
            a^{m}
        \end{array}
    \right)
$$

where $$a^{i} \in \mathbb{R}^{n}$$ is $i$ th row vector.

$$
    Ax
    =
    \left(
        \begin{array}{c}
            (a^{1})^{\mathrm{T}}x
            \\
            \vdots 
            \\
            (a^{m})^{\mathrm{T}}x
        \end{array}
    \right)
$$

Then

$$
    A^{\mathrm{T}}y
    =
    \sum_{i=1}^{n}
        y^{i}a^{i}
$$


$$
    \langle c, x \rangle < 0
    \Rightarrow
    \langle a^{j}, x \rangle < 0
    \quad
    \langle a^{i}, x \rangle \ge 0
    \Rightarrow
    \langle c, x \rangle \ge 0
$$

Since $x \in \mathbb{R}^{n}$, (1) is equivalent that inequality system below has no solution


$$
\begin{eqnarray}
    \langle c, x \rangle
    & > &
        0
    \nonumber
    \\
    \langle a^{i}, x \rangle
    & \le &
        0
        \quad
        i = 1, \ldots, m
    \nonumber
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>

#### Definition 3
* $A$,
    * $m$ rows $n$ cols matrix
* $b \in \mathbb{R}^{n}$,
* $c \in \mathbb{R}^{n}$,

Primal LP problem is defined as

$$
\begin{align}
    \min_{x \in \mathbb{R}^{n}}
    & & &
        c^{\mathrm{T}}x
        \label{mathmatical_programming_problem_lp_primal}
    \\
    \mathrm{subject\ to}
    & & &
        Ax - b
        \ge
        0
    .
    \nonumber
\end{align}
$$

Dual of LP problem is defined as

$$
\begin{align}
    \min_{y \in \mathbb{R}^{m}}
    & & &
        b^{\mathrm{T}}y
        \label{mathmatical_programming_problem_lp_dual}
    \\
    \mathrm{subject\ to}
    & & &
        A^{\mathrm{T}}y - c
        \ge
        0
    \nonumber
    \\
    & & &
        y
        \ge
        0
    \nonumber
    .
\end{align}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem

(1) Dual of dual probelm is a primal problem

(2) Let $y^{\prime}$ be a feasible solution of $$\eqref{mathmatical_programming_problem_lp_dual}$$.
Let $x^{\prime}$ be a feasible solution of $$\eqref{mathmatical_programming_problem_lp_primal}$$.

$$
\begin{eqnarray}
    b^{\mathrm{T}}y^{\prime}
    \le
    c^{\mathrm{T}}x^{\prime}
    \nonumber
\end{eqnarray}
$$

(3)

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Anatoli Iouditski](https://ljk.imag.fr/membres/Anatoli.Iouditski/optimisation-convexe.htm)
