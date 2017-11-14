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

## Definiton6 Lagrange Function and Lagrange Duality
* $$n, m, k \in \mathbb{N}$$,
* $$X \subset \mathbb{R}^{n}$$,
    * convex
* $$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$$,
    * convex
* $$g: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$,
    * $$g(x) = (g^{1}(x), \ldots, g^{m}(x))$$,
    * convex

$$
\begin{equation}
    L(x, \lambda)
    :=
    f(x)
    +
    \sum_{j=1}^{m}
        \lambda_{j}g^{j}(x)
    \label{def_lagrange_function}
\end{equation}
$$

$L$ is said to be Lagrange function of inequality constrained problem $$\eqref{convex_programming_problem}$$.

$$
\begin{eqnarray}
    \underline{L}(\lambda)
    & := &
        \inf_{x \in X}
            L(x, \lambda)
    \nonumber
    \\
    & = &
        \inf_{x \in X}
        \left(
            f
            +
            \sum_{j=1}^{m}
                \lambda_{j}g_{j}(x)
        \right)
    \label{def_infimum_of_lagrange_function}
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Theorem7 Convex programming duality theorem
* $$n, m, k \in \mathbb{N}$$,
* $$X \subset \mathbb{R}^{n}$$,
    * convex
* $$f_{0}: \mathbb{R}^{n} \rightarrow \mathbb{R}$$,
* $$g: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$,
    * $$g(x) = (g^{1}(x), \ldots, g^{m}(x))$$,

* (1) $$\underline{L}(\lambda)$$ is lower bound of $$\eqref{convex_programming_problem}$$ for all $\lambda$, that is,

$$
\begin{equation}
    \forall \lambda \ge 0,
    \
    \underline{L}(\lambda)
    \le
    f(x^{*})
    \label{theorem_lower_bound_of_optimal_value}
\end{equation}
$$

where $$x^{*} \in X$$ is optimal value of $$\eqref{convex_programming_problem}$$.
Moreover,

$$
\begin{equation}
    \sup_{\lambda \ge 0}\underline{L}(\lambda)
    \le
    f(x^{*})
    \label{theorem_supremum_infimum_lagrange_function}
    .
\end{equation}
$$

* (2) If inequality constrained problem $$\eqref{convex_programming_problem}$$
    * is convex programming problem,
    * is bounded below
    * satisfies the Slater condition,

then there exists $$\lambda^{*} \in \mathbb{R}_{\ge 0}^{m}$$ such that

$$
    \underline{L}(\lambda^{*})
    =
    \sup_{\lambda \ge 0}
        \underline{L}(\lambda)
    =
    f(x^{*})
$$

## proof.
(1)
The latter statement of (1) is immediate consequence of the former statement.
Suppose that $$\underline{L}$$ is not lower bound of the optimal value.

$$
    \exists \lambda \in \mathbb{R}_{\ge 0}^{m},
    \
    \text{ s.t. }
    \
    \underline{L}(\lambda) > f(x^{*})
    .
$$

$$x^{*} \in X$$ is solution of $$\eqref{convex_programming_problem}$$ so that $$g(x^{*}) \ge 0$$.
Hence we have

$$
    \underline{L}(\lambda)
    >
    f(x^{*})
    +
    \sum_{j=1}^{m}
        \lambda_{j}g(x^{*})
    .
$$

This is contradiction to the definition of $$\underline{L}$$.

(2)
Let $$c^{*} := f(x^{*})$$.
Since $$x^{*}$$ is an optimal solution of $$\eqref{convex_programming_problem_primal_problem}$$, the following inequality constrained problem has no solution, tha is,

$$
    f(x)
    <
    c^{*},
    \
    g^{j}(x) \le 0,
    \quad
    \forall j = 1, \ldots, m
    .
$$

By <a href="#theorem5-convex-theorem-on-alternative">convex theorem on alternative</a>, $$\eqref{proposition_dual_problem}$$ has solution;

$$
\begin{equation}
    \exists \lambda^{*} \in \mathbb{R}_{\ge 0}^{m}
    \
    \text{ s.t. }
    \
    \underline{L}(\lambda^{*})
    \ge
    c^{*}
    \label{theorem_optimal_value_of_dual_problem}
\end{equation}
    .
$$

This implies that

$$
    \sup_{\lambda \in \mathbb{R}_{\ge 0}^{m}}
        \underline{L}(\lambda)
    \ge
    c^{*}
    .
$$

From $$\eqref{theorem_supremum_infimum_lagrange_function}$$, 

$$
    \sup_{\lambda \in \mathbb{R}_{\ge 0}^{m}}
        \underline{L}(\lambda)
    =
    c^{*}
    .
$$

By $$\eqref{theorem_lower_bound_of_optimal_value}$$ and $$\eqref{theorem_optimal_value_of_dual_problem}$$, we obtain

$$
    \underline{L}(\lambda^{*})
    \ge
    c^{*}
    \ge
    \sup_{\lambda \in \mathbb{R}_{\ge 0}^{m}}
        \underline{L}(\lambda)
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Definition8. Primal and Dual problem
The primal problem of optimization problem is 

$$
\begin{align}
    \min_{x \in X}
    & & &
        f(x)
        \label{convex_programming_problem_primal_problem}
    \\
    \mathrm{subject\ to}
    & & &
        g^{j}(x) \ge 0,
        \
        j = 1, \ldots, m
    \nonumber
\end{align}
$$

and its Lagrange Dual problem

$$
\begin{equation}
    \sup_{\lambda \in \mathbb{R}_{\ge 0}^{m}}
        \underline{L}(\lambda)
    \label{convex_programming_problem_dual_problem}
\end{equation}
$$


<div class="end-of-statement" style="text-align: right">■</div>

## Remark9
Primal problem of optimization problem and its dual problem 

<div class="end-of-statement" style="text-align: right">■</div>

## Proposition10

* (1) $$(x^{*}, \lambda^{*})$$ is a saddle point of the Lagrange function $L$
* (2) $$x^{*}$$ is an optimal solution to $$\eqref{convex_programming_problem_primal_problem}$$ and $$\lambda^{*}$$ is an optimal solution to $$\eqref{convex_programming_problem_dual_problem}$$.

If (1) holds, the optimal values in $$\eqref{convex_programming_problem_primal_problem}$$ and in $$\eqref{convex_programming_problem_dual_problem}$$ are equal to each other.

## proof.

<div class="QED" style="text-align: right">$\Box$</div>


## Theorem11 Saddle point formulation of Optimality Conditions in Convex Programming
* $$x^{*} \in X$$,

Then

* (i) There exists $$\lambda^{*} \in \mathbb{R}_{\ge 0}^{m}$$ such that $$(x^{*}, \lambda^{*})$$ is asaddle point of the Lagrange function $$L(x, \lambda)$$ i.e.

$$
\begin{equation}
    \forall x \in X,
    \
    \lambda \in \mathbb{R}_{\ge 0}^{m},
    \quad
    L(x, \lambda^{*})
    \ge
    L(x^{*}, \lambda^{*})
    \ge
    L(x^{*}, \lambda),
    \label{theorem_saddle_point_of_lagrange_function}
\end{equation}
$$

* (ii) $x^{*}$ is a optimal solution to $$\eqref{convex_programming_problem_primal_problem}$$


(1) If (i) holds, then (ii) holds.

(2) Moreover, if the problem $$\eqref{convex_programming_problem_primal_problem}$$

* is convex
* and satisfies the Slater condition

then (ii) implies that (i) holds

## proof.
(1)
Suppose that there exists $$\lambda^{*} \in \mathbb{R}_{\ge 0}^{m}$$ such that $$\eqref{theorem_saddle_point_of_lagrange_function}$$ is satisfied.
First of all, $$x^{*}$$ is feasible to $$\eqref{convex_programming_problem_primal_problem}$$.
Indeed, if $$g^{j}(x^{*}) > 0$$, then

$$
    \sup_{\lambda \in \mathbb{R}_{\ge 0}^{m}}
        L(x^{*}, \lambda)
    =
    + \infty
    .
$$

But this is forbidden by the second inequality in $$\eqref{theorem_saddle_point_of_lagrange_function}$$.

Since $x^{*}$ is feasible, $$g^{j}(x^{*}) \le 0 \ (\forall j)$$.
Hence $$\sup_{\lambda \in \mathbb{R}_{\ge 0}^{m}}L(x^{*}, \lambda) = f(x^{*})$$.
From second inequality of $$\eqref{theorem_saddle_point_of_lagrange_function}$$, we have

$$
    \forall \lambda^{\prime} \in \mathbb{R}_{\ge 0}^{m},
    \
    L(x^{*}, \lambda^{*})
    \ge
    \sup_{\lambda \in \mathbb{R}_{\ge 0}^{m}}
        L(x^{*}, \lambda)
    =
    f(x^{*})
    \ge
    L(x^{*}, \lambda^{\prime})
$$

The first equality of $$\eqref{theorem_saddle_point_of_lagrange_function}$$

$$
    \forall x \in X,
    \quad
    f(x)
    +
    \sum_{j=1}^{m}
        \lambda_{j}^{*}g^{j}(x)
    \ge
    f(x^{*})
$$

This implies that $$x^{*}$$ is optimal.
Indeed, if there exists an optimal value $$x^{\prime} \neq x^{*} \in X$$,

$$
    f(x^{\prime})
    \ge
    f(x^{\prime})
    +
    \sum_{j=1}^{m}
        \lambda_{j}^{*}g^{j}(x^{\prime})
    \ge
    f(x^{*})
$$

since $$g^{j}(x^{\prime}) \le 0$$.
Therefore $$x^{\prime}$$ cannot be an optimal value.

(2)
We will show that there exists $$\lambda^{*} \in \mathbb{R}_{\ge 0}^{m}$$ such that $$\eqref{theorem_saddle_point_of_lagrange_function}$$ is satisfied.
By <a href="#theorem7-convex-programming-duality-theorem">convex programming duality theorem</a>, there exists $$\lambda^{*} \in \mathbb{R}_{\ge 0}^{m}$$ such that

$$
    f(x^{*})
    =
    \underline{L}(\lambda^{*})
    =
    \inf_{x \in X}
        L(x, \lambda^{*})
$$

Hence

$$
\begin{equation}
    \lambda_{j}^{*} > 0
    \Rightarrow
    g^{j}(x^{*}) = 0
    \label{theorem_complementary_slackness}
\end{equation}
    .
$$

Indeed, if $$g^{j} < 0$$, then $$f(x^{*}) > \underline{L}(\lambda^{*})$$.
From the above equation $$\eqref{theorem_complementary_slackness}$$, we conclude that

$$
\begin{eqnarray}
    f(x^{*})
    & = &
        f(x^{*})
        +
        \sum_{j=1}^{m}
            \lambda_{j}^{*}g^{j}(x^{*})
    \nonumber
    \\
    & = &
        L(x^{*}, \lambda^{*})
    \nonumber
\end{eqnarray}
    .
$$

Hence the second equality of $$\eqref{theorem_saddle_point_of_lagrange_function}$$ holds, that is,

$$
    L(x^{*}, \lambda^{*})
    =
    f(x^{*})
    =
    \inf_{x \in X}
        L(x^{*}, \lambda^{*})
    .
$$

On the other hand, since $$x^{*} \in X$$ is feasible for $$\eqref{convex_programming_problem_primal_problem}$$, $$g^{j}(x^{*}) \ge 0$$.
Therefore first inequality of $$\eqref{theorem_saddle_point_of_lagrange_function}$$ holds;

$$
\begin{eqnarray}
    L(x^{*}, \lambda)
    & = &
        f(x^{*})
        +
        \sum_{j=1}^{m}
            \lambda_{j}^{*}g^{j}(x^{*})
    \\
    & \ge &
        f(x^{*})
    \nonumber
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Remark12
* The equation $$\eqref{theorem_complementary_slackness}$$ is known as complementary slackness.
* Theorem11 (1) holds for an arbitrary inequality constrained optimization program, not necessarily convex.
* Theorem11 does not give us how to verify whether $$(x^{*}, \lambda^{*})$$ is saddle point of lagrange function or not.

<div class="end-of-statement" style="text-align: right">■</div>

## Definition13 restricted Slater assumption
* $$X$$,
* $$f, g^{1}, \ldots, g^{m}$$,

An inequality constrained problem $$\eqref{convex_programming_problem_primal_problem}$$ is said to satisfy restricted Slater assumption if

$$
\begin{eqnarray}
    \exists x \in X
    \
    \text{ s.t. }
    \
    & &
        g^{j}: \text{ nonlinear}
        \Rightarrow
        g^{j}(x) \ge 0
    \\
    & &
        g^{j}: \text{ linear}
        \Rightarrow
        g^{j}(x) \le 0
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Theorem12 Karush-Kuhn-Tucker Optimality Conditions in Convex case
* $$x^{*} \in \mathrm{int}(X)$$,
    * interior feasible solution to $$\eqref{convex_programming_problem_primal_problem}$$,
* $$f, g^{1}, \ldots, g^{m}$$,
    * differentiable at $$x^{*}$$
* $$\eqref{convex_programming_problem_primal_problem}$$ is convex programming problem.


* (i)

$$
\begin{eqnarray}
    \exists \lambda^{*} \in \mathbb{R}_{\ge 0}^{m},
    \
    \text{ s.t. }
    \
    & &
        \forall j = 1, \ldots, m,
        \
        \lambda_{j}^{*}g^{j}(x^{*}) = 0,
    \\
    & &
        \nabla f(x^{*})
        +
        \sum_{j=1}^{m}
            \lambda_{j}^{*}
            \nabla g^{j}(x^{*})
        =
        0
\end{eqnarray}
$$

* (ii) $$x^{*}$$ to be optimal solution to $$\eqref{convex_programming_problem_primal_problem}$$.

Then

* (1) Sufficiency for an optimal value: (i) $\Rightarrow$ (ii),
* (2) Necessity and sufficiency for an optimal value: Under restricted Slater condition, (i) $$\Leftrightarrow$$ (ii).

## proof.
(i) $\Rightarrow$ (ii)

$$
\begin{eqnarray}
    X^{\prime\prime}
    & := &
        \{
            x \in X
            \mid
            g^{i + m}(x)
            =
            a_{i}^{\mathrm{T}}x - b_{i}
            \le
            0,
            \
            i = 1, \ldots, M
        \}
    \nonumber
    \\
    X
    & := &
        X^{\prime} \cap X^{\prime\prime}
    \nonumber
\end{eqnarray}
    .
$$

To show that $$x^{*}$$ is an optimal solution, $$\exists \lambda^{*} \in \mathbb{R}_{\ge 0}^{m}$$ such that

$$
\begin{eqnarray}
    \lambda_{j}^{*}
    g^{j}(x^{*})
    & = &
        0,
        \quad
        j = 1, \ldots, m,
    \nonumber
    \\
    x^{*}
    & \in &
        \arg \min_{x \in X}
            \left(
                f(x)
                +
                \sum_{j=1}^{m}
                    \lambda_{j}^{*}g^{j}(x)
            \right)
    \nonumber
    \\
    & = &
        \arg \min_{x \in X}
            L(x, \lambda^{*})
\end{eqnarray}
$$

Here we claim that following statements are equivalent:

* (iii) $$x^{*}$$ is a minimizer of $$L(x, \lambda^{*})$$ on $X$,
* (iV) $$x^{*}$$ is a minimizer of $$L(x, \lambda^{*})$$ on $$X^{\prime\prime}$$,

(iii) $\Rightarrow$ (iV)

Since $$x^{*} \in \mathrm{int}(X)$$, $$x^{*}$$ is local minimizer of $f$ on $X$.
It follows that $$x^{*}$$ is also local minimizer of $$X^{\prime\prime}$$.
$$L(x, \lambda^{*})$$ is convex with respect to $x$ so that $$x^{*}$$ is also global minimizer of $$X^{\prime\prime}$$ by <a href="{{ site.baseurl }}/math/convex_function.html#theorem11">theorem</a>.

(iV) $\Rightarrow$ (iii)

Since $$X \subseteq X^{\prime\prime}$$, a minimizer on $$X^{\prime\prime}$$ is also a minimizer on $X$.

Therefore, our claim is verified.
The claim says that if the minimizer exists, $$x^{*} \in X^{\prime\prime}$$.
Diffierentiable convex function $$L(x, x^{*\prime})$$ attains at $$x^{*}$$ its minimum on $$X^{\prime\prime}$$ if and only if

$$
    \nabla_{x} L(x^{*}, \lambda^{*})
    +
    \sum_{i \in I}
        \mu_{i}^{*}a_{i}
    =
    0
$$

where $$\mu_{i}^{*} \ge 0$$ and

<div class="end-of-statement" style="text-align: right">■</div>



## Reference
* [Anatoli Iouditski](https://ljk.imag.fr/membres/Anatoli.Iouditski/optimisation-convexe.htm)
