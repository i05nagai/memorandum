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
* $c \in \mathbb{R}$,
    * constant

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

* (a) $$\eqref{proposition_primal_problem}$$ is solvable.
* (b) $$\eqref{proposition_dual_problem}$$ is unsolvable,

## proof.
(a) $\Rightarrow$ (b)
By the proposition above.

(a) $\Leftarrow$ (b)
Suppose $$\eqref{proposition_primal_problem}$$ has no solution.
We show that $$\eqref{proposition_dual_problem}$$ has solution.

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
    .
    \nonumber
\end{eqnarray}
$$

We claim that

* (i) $S$ and $T$ are nonempty convex sets,
* (ii) $S \cap T = \emptyset$.

We first prove (i).
$c \in \mathbb{R}$ so that $T$ is not empty set.
Additionally,

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
For $S$, we have

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

This is contradiction that primal problem $$\eqref{proposition_primal_problem}$$ has no solution.

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

Now We claim that

* (iii) $a \ge 0$,
* (iV) $a^{0} > 0$.

We first prove (iii).
Suppose that $\exists j = 0, \ldots, m$ such that  $a^{j} < 0$.
The RHS of equation $$\eqref{convex_theorem_on_alternative_separation_theorem}$$ attains $+\infty$ since we can take a sequence $$(u_{i})_{i \in \mathbb{N}} \in T$$ such that

$$
    \forall i \in \mathbb{N},
    \
    u_{i}^{j} < 0,
    \
    u_{i}^{k} = 0 \ (k \neq j),
    \
    u_{i}^{j} \rightarrow -\infty \ (i \rightarrow \infty)
$$

But $S$ is not empty set so that the LHS of $$\eqref{convex_theorem_on_alternative_separation_theorem}$$ is finite.
Thus $a \ge 0$.

From $$\eqref{convex_theorem_on_alternative_separation_theorem}$$ and the definition of $T$,

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
        \sup_{u^{0} < c, u^{1}, \ldots, u^{m} \le 0}
            \sum_{j=0}^{m}
                a^{j} u^{j}
    \nonumber
    \\
    & = &
        \sup_{u^{0} < c, u^{1}, \ldots, u^{m} \le 0}
            a^{0}u^{0}
        \quad
        (\because a \ge 0)
    \nonumber
    \\
    & = &
        a^{0}c
\end{eqnarray}
$$

The LHS of $$\eqref{convex_theorem_on_alternative_separation_theorem}$$ is not less than the LHS of dual problem $$\eqref{proposition_dual_problem}$$, that is,

$$
\begin{eqnarray}
    \inf_{x \in X}
        \left(
            a^{0}f(x)
            +
            \sum_{j=1}^{m}
                a^{j}g^{j}(x)
        \right)
    & = &
    \inf_{x \in X}
        \langle a, F(x) \rangle
    \nonumber
    \\
    & \ge &
        \inf_{u \in S}
            \langle a, u \rangle
    \label{convex_theorem_on_alternative_upper_bound_of_sepration}
\end{eqnarray}
$$

Indeed, it is easy to check that $$\forall x \in X$$, $F(x) \in S$ since $$F(x) \le F(x)$$.
Hence by definition of infimum, the inequality holds.

Then $$\eqref{convex_theorem_on_alternative_upper_bound_of_sepration}$$ implies that

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
    \label{convex_theorem_on_alternative_lower_bound_of_sepration}
\end{equation}
$$

Now let us proove that $$a^{0} > 0$$.
By slater condition, we can take $\bar{x} \in X$ such that

$$
    \forall i = 1, \ldots, m,
    \
    g^{i}(x) < 0
    .
$$

From $$\eqref{convex_theorem_on_alternative_lower_bound_of_sepration}$$, we have

$$
    a^{0}f(\bar{x})
    +
    \sum_{j=1}^{m}
        a^{j}g^{j}(\bar{x})
    \ge
    a^{0}c
    .
$$

If $a^{0} = 0$, RHS of the above equation 0 but the LHS could be less than 0 by taking $$a^{j} > 0$$.
Hence $a^{0} > 0$.

Finally, since $a^{0} > 0$, we can define $$\lambda_{j} := a^{j} / a^{0} > 0$$.
Then

$$
    \inf_{x \in X}
        \left(
            f(x)
            +
            \sum_{j=1}^{m}
                \lambda_{j}
                g^{j}(x)
        \right)
    \ge
    c
    .
$$

This is a solution of $$\eqref{proposition_dual_problem}$$.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference

