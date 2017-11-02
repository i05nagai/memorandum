---
title: Convex Programming
---

## Convex Programming

## Definition

### Definition1 Mathematical Programming problem
* $$n, m, k \in \mathbb{N}$$,
* $$X \subset \mathbb{R}^{n}$$,
* $$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$$,
* $$g: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$,
    * $$g(x) = (g^{1}(x), \ldots, g^{m}(x))$$,
* $$h: \mathbb{R}^{n} \rightarrow \mathbb{R}^{k}$$,
    * $$h(x) = (h^{1}(x), \ldots, h^{k}(x))$$,

constraind mathematrical programming problem is a promblem as follows:

$$
\begin{equation}
    \min
    \left\{
        f(x)
        \mid
        x \in X,
        \
        i = 1, \ldots, m,
        \
        g^{i}(x) \le 0,
        \
        j = 1, \ldots, k,
        \
        h^{j}(x) = 0,
    \right\}
    \label{mathematical_programming_problem}
\end{equation}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition2 Convex programming problem
* $$n, m, k \in \mathbb{N}$$,
* $$X \subset \mathbb{R}^{n}$$,
* $$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$$,
* $$g: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$,
    * $$g(x) = (g^{1}(x), \ldots, g^{m}(x))$$,
* $$h: \mathbb{R}^{n} \rightarrow \mathbb{R}^{k}$$,
    * $$h(x) = (h^{1}(x), \ldots, h^{k}(x))$$,

$$\eqref{mathematical_programming_problem}$$ is said to be convex programming problem if

* $X$ is convex
* $$f, g_{1}, \ldots,g_{m}$$ are real-valued conve functions
* There are no equality constraints i.e. $$h_{i} \equiv 0$$,

$$\eqref{mathematical_programming_problem}$$ is simplified to

$$
\begin{equation}
    \min
    \left\{
        f(x)
        \mid
        x \in X,
        \
        i = 1, \ldots, m,
        \
        g^{i}(x) \le 0,
    \right\}
    .
    \label{convex_programming_problem}
\end{equation}
$$

We denote

$$
    \mathcal{A}(f, X, g)
    :=
    \left\{
        f(x)
        \mid
        x \in X,
        \
        i = 1, \ldots, m,
        \
        g^{i}(x) \le 0,
    \right\}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Proposition3
* $$n, m \in \mathbb{N}$$,
* $$X \subset \mathbb{R}^{n}$$,
    * convex
* $$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$$,
    * convex function
* $$g: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$,
    * $$g(x) = (g^{1}(x), \ldots, g^{m}(x))$$,
    * $$g^{i}$$ is a convex function

If there exist nonnegative $$\lambda_{1}, \ldots, \lambda_{m}$$ such that the inequality

$$
\begin{eqnarray}
    \inf_{x \in X}
    \left\{
        f(x)
        +
        \sum_{j=1}^{m}
            \lambda_{j}g_{j}(x)
    \right\}
    & \ge &
        c
    \nonumber
    \\
    \lambda_{j}
    & \ge &
        0
        \quad
        j = 1, \ldots, m
    \label{proposition_dual_problem}
\end{eqnarray}
$$

has solution, then the following inequality system

$$
\begin{eqnarray}
    f(x)
    & < &
        c
    \nonumber
    \\
    g^{j}(x)
    & \le &
        0,
        \quad
        j = 1, \ldots, m,
    \nonumber
    \\
    x
    & \in &
        X
    \label{proposition_primal_problem}
\end{eqnarray}
$$

has no solution.

## proof.
Suppose that there exists $$\lambda_{1}, \ldots, \lambda_{m}$$ such that satisfies $$\eqref{proposition_dual_problem}$$.
Suppose $$\eqref{proposition_primal_problem}$$ has solution $$x^{*} \in X$$.

$$
    \lambda_{i} g^{i}(x^{*})
    \le
    0
$$

$$
    f(x^{*})
    +
    \sum_{i=1}^{m}
        \lambda_{i} g^{i}(x^{*})
    <
    c
$$

But this is contradiction since

$$
    \inf_{x \in X}
    \left\{
        f(x)
        +
        \sum_{j=1}^{m}
            \lambda_{j}g_{j}(x)
    \right\}
    \ge
    c
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Definition4. Slater condition
* $$X \subseteq \mathbb{R}^{n}$$,
* $$g^{1}, \ldots, g^{m}$$,
    * real valued functions on $X$

We say that these functions satisfy the Slater condition on $X$ if

$$
    \exists x \in X,
    \
    \text{ s.t. }
    \
    g^{j}(x) < 0,
    \
    j = 1, \ldots, m
    .
$$

An inequality constrained problem

$$
    \min
    \left\{
        f(x)
        \mid
        g^{j}(x)
        \le
        0,
        \
        j = 1, \ldots, m,
        \
        x \in X
    \right\}
$$

is said to satisfy the Slater condition if

$$
    \exists x \in X,
    \
    \forall i = 1, \ldots, m,
    \
    g^{i}(x) < 0
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Theorem5 Convex theorem on alternative
* $X \subseteq \mathbb{R}^{n}$
    * convex
* $$f, g^{1}, \ldots, g^{m}$$,
    * convex real-valued function on $X$
* $$g^{1}, \ldots, g^{m}$$,
    Salter condition on $X$

Then the following are equivalent:

* (a) $$\eqref{proposition_dual_problem}$$ is solvable,
* (b) $$\eqref{proposition_primal_problem}$$ is unsolvable.

## proof.
(a) $\Rightarrow$ (b)
By proposition.

(a) $\Leftarrow$ (b)
Suppose $$\eqref{proposition_dual_problem}$$ has no solution.
Let

$$
    F(x)
    :=
    \left(
        \begin{array}{c}
            f(x)
            \\
            g^{1}(x)
            \\
            \vdots 
            \\
            g^{m}(x)
        \end{array}
    \right)
$$

and

$$
\begin{eqnarray}
    S
    & := &
        \{
            u := (u^{0}, \ldots, u^{m}) \in \mathbb{R}^{m + 1}
            \mid
            \exists x \in X,
            \
            F(x)
            \le
            u
        \}
    \nonumber
    \\
    T
    & := &
        \{
            (u^{0}, \ldots, u^{m}) \in \mathbb{R}^{m + 1}
            \mid
            u^{0} < c,
            \
            u^{1} \le 0,
            \
            \ldots,
            \
            u^{m} \le 0
        \}
    \nonumber
\end{eqnarray}
$$

We claim that

* (i) $S$ and $T$ are nonempty convex sets,
* (ii) $S$ and $T$ do not intersect.

We first prove (i).
$c \in \mathbb{R}$ so that $T$ is not emptyset.

$$
\begin{eqnarray}
    \forall u, v \in T,
    \
    \forall \lambda \in [0, 1],
    \
    \lambda u^{0}
    +
    (1 - \lambda) v^{0}
    & < &
        c
    \nonumber
    \\
    \lambda u^{i}
    +
    (1 - \lambda) v^{i}
    & \le &
        0
    \nonumber
\end{eqnarray}
$$

Hence $T$ is convex set.

$$
\begin{eqnarray}
    \forall u, v  \in S,
    \
    \exists x_{u}, y_{u} \in X
    \
    \forall \lambda \in [0, 1],
    \
    F(\lambda x_{u} + (1 - \lambda) x_{v})
    & \le &
        \lambda F(x_{u})
        +
        (1 - \lambda) F(x_{v})
    \nonumber
    \\
    & \le &
        \lambda u
        +
        (1 - \lambda) v
    \nonumber
\end{eqnarray}
$$

Since $X$ is convex, $$\lambda x_{u} + (1 - \lambda) x_{v} \in X$$.
Hence $S$ is convex set.

For (ii), suppose that $$S \cap T \neq \emptyset$$.
We can take $$u \in S \cap T$$.
We have

$$
    \exists x \in X,
    \
    f(x) \le u^{0} < c,
    \
    g^{i}(x) \le u^{i} \le 0
$$

This is contradiction that $$\eqref{proposition_dual_problem}$$ has no solution.

Since $S$ and $T$ is convex and nonempty, according to <a href="{{ site.baseurl }}/math/convex_function.html#thereom10-separation-theorem">separation theorem on convex sets</a>, there exists $a := (a^{0}, \ldots, a^{m}) \neq 0$ such that

$$
\begin{equation}
    \inf_{u \in S}
    \langle a, u \rangle
    \ge
    \sup_{u \in T}
    \langle a, u \rangle
    \label{convex_theorem_on_alternative_separation_theorem}
\end{equation}
$$

We claim that

* (iii) $a \ge 0$,
* (iV) $a^{0} > 0$.

We first prove (iii).
From $$\eqref{convex_theorem_on_alternative_separation_theorem}$$,

$$
\begin{eqnarray}
    \sup_{u \in T}
    \langle a, u \rangle
    & = &
        \sup_{u \in T}
            \sum_{j=0}^{m}
                a^{j} u^{j}
    \nonumber
    \\
    & = &
        \sup_{u^{0} < c, u^{1}, \ldots, u^{m} \ge 0}
            \sum_{j=0}^{m}
                a^{j} u^{j}
    \nonumber
    \\
    & = &
        \sup_{u^{0} < c, u^{1}, \ldots, u^{m} \ge 0}
            a^{0}u^{0}
    \nonumber
    \\
    & = &
        a^{0}c
\end{eqnarray}
$$

The LHS of $$\eqref{convex_theorem_on_alternative_separation_theorem}$$

$$
    \inf_{u \in S}
        \langle a, u \rangle
    \ge
    \inf_{x \in X}
        \left(
            a^{0}f(x)
            +
            \sum_{j=1}^{m}
                a^{j}g^{j}(x)
        \right)
$$

Indeed, suppose that

$$
    \inf_{u \in S}
        \langle a, u \rangle
    <
    \inf_{x \in X}
        \left(
            a^{0}f(x)
            +
            \sum_{j=1}^{m}
                a^{j}g^{j}(x)
        \right)
    .
$$

We take a sequence $$\{ \langle a, u_{i} \rangle \}_{i \in \mathbb{N}}$$ such that

$$
    \exists n \in \mathbb{N},
    \
    \forall i \ge n,
    \
    \inf_{u \in S}
        \langle a, u \rangle
    <
    \langle a, u_{i} \rangle
    <
    \inf_{x \in X}
        \left(
            a^{0}f(x)
            +
            \sum_{j=1}^{m}
                a^{j}g^{j}(x)
        \right)
    .
$$

This is contradiction since there exists $x \in \mathbb{R}^{m + 1}$ such that

$$
\begin{eqnarray}
    \langle a, u_{i} \rangle
    & = &
        \sum_{j=0}^{m}
            a^{i} u_{i}^{j}
    \nonumber
    \\
    & \ge &
        a^{0} f(x)
        +
        \sum_{j=1}^{m}
            a^{i} g^{j}(x)
    \nonumber
    .
\end{eqnarray}
$$

Moreover,

$$
\begin{equation}
    \inf_{x \in X}
        \left(
            a^{0}f(x)
            +
            \sum_{j=1}^{m}
                a^{j}g^{j}(x)
        \right)
    \ge
    a^{0}c
\end{equation}
$$

Indeed, suppose that

$$
    \inf_{x \in X}
        \left(
            a^{0}f(x)
            +
            \sum_{j=1}^{m}
                a^{j}g^{j}(x)
        \right)
    <
    a^{0}c
    .
$$

We take a sequence $$\{ a^{0}f(x_{i}) + \sum_{j=1}^{m} a^{j}g^{j}(x_{i}) \}_{i \in \mathbb{N}}$$ such that

$$
    \exists n \in \mathbb{N},
    \
    \forall i \ge n,
    \
    \inf_{x \in X}
        \left(
            a^{0}f(x)
            +
            \sum_{j=1}^{m}
                a^{j}g^{j}(x)
        \right)
    <
    a^{0}f(x_{i})
    +
    \sum_{j=1}^{m}
        a^{j}g^{j}(x_{i})
    <
    a^{0}c
$$

On the other hand, $$a \ge 0$$ implies that

$$
\begin{eqnarray}
    F(x_{i})
    \le
    \left(
        \begin{array}{c}
            c
            \\
            0
            \\
            \vdots
            \\
            0
        \end{array}
    \right)
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


## Reference

