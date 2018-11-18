---
title: Iterative Improvement
---

## Iterative Improvement

$$
\begin{equation}
    Ax = b
    \label{original_equation}
\end{equation}
$$

Let $x_{0}$ be a numerical solution of the equation.
Let

$$
    r_{0}
    :=
    b - Ax_{0}
    .
$$

We can improve the solution by solving the following equation with respect to $d$;

$$
\begin{equation}
    Ad = r_{0}
    \label{equation_for_improvement}
\end{equation}
    .
$$

Improved solution is defined as

$$
    \hat{x}_{1}
    :=
    \hat{x}_{0} + d_{0}
    .
$$

where $d_{0}$ is the numerical solution of the equation.
When we solve the original equaton $$\eqref{original_equation}$$, we obtain LU decomposition of $A$.
Thus the solution of the equation $$\eqref{equation_for_improvement}$$ can solve $O(N^{2})$.

#### Remark
Unfortunately, the naive execution of the algorithm renders an $x_{1}$ that is no more accurate than $x_{0}$.
The efficient situations are

* The solution of $x_{0}$ is calculated with floating point precision. On the other hand, $r_{0}$ and $x_{1}$ are calculated with double floating point precision.
* With some pivot strategies that are used to preserve sparcity, Gaussian elimination sometimes does not provide a nearby solution.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition
* $A \in \mathbb{R}^{n\times n}$,
    * nonsingular
* $b \in \mathbb{R}^{n}$,

$$
\begin{eqnarray}
    \abs{A}
    & := &
        \left(
            \abs{a_{j}^{i}}
        \right)_{i,j = 1,\ldots,n}
    \nonumber
    \\
    \abs{b}
    & := &
        \left(
            \abs{b^{i}}
        \right)_{i = 1,\ldots,n}
    \nonumber
\end{eqnarray}
$$

$$
    \norm{ b }_{\infty}
    :=
    \max_{i = 1,\ldots, n}
        \abs{b_{i}}
    .
$$

$$
    e
    :=
    \left(
        \begin{array}{c}
            1
            \\
            \vdots 
            \\
            1
        \end{array}
    \right)
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition componentwise backward error

$$
    E \in \mathbb{R}_{\ge 0}^{n \times n},
    \
    f \in \mathbb{R}_{\ge 0}^{n}
    \
    y \in \mathbb{R}^{n},
    \
    \omega_{E, f}(y)
    :=
    \min\{
        \epsilon
        \mid
        (A + \Delta A) y
        =
        b
        +
        \Delta b,
        \
        \abs{\Delta A}
        \le
        \epsilon E,
        \
        \abs{\Delta b}
        \le
        \epsilon f
    \}
    .
$$

If $E = \abs{A}$ and $f = \abs{b}$, we call it the componentwise relative backward error.

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 1.1

$$
    \omega_{E, f}(y)
    =
    \max_{i = 1,\ldots, n}
        \frac{
            \abs{r_{i}}
        }{
            \left(
                E\abs{y}
                +
                f
            \right)_{i}
        }
    .
$$

where $r := b - Ay$.

#### proof

<div class="QED" style="text-align: right">$\Box$</div>

#### Definition Condition number

$$
\begin{eqnarray}
    \mathrm{cond}(A, x)
    & := &
        \frac{
            \norm{
                \abs{A^{-1}}
                \abs{A}
                \abs{x}
            }_{\infty}
        }{
            \norm{x}_{\infty}
        }
    \nonumber
    \\
    \mathrm{cond}(A)
    & := &
        \mathrm{cond}(A, e)
    \nonumber
    \\
    & = &
        \frac{
            \norm{
                \abs{A^{-1}}
                \abs{A}
                \abs{e}
            }_{\infty}
        }{
            \norm{e}_{\infty}
        }
    \nonumber
    \\
    & = &
        \norm{
            \abs{A^{-1}}
            \abs{A}
        }_{\infty}
    \nonumber
    \\
    & \le &
        \norm{
            A^{-1}
        }_{\infty}
        \norm{
            A
        }_{\infty}
    \nonumber
    \\
    & =: &
        \kappa_{\infty}(A)
    \nonumber
\end{eqnarray}
$$

The componentwise condition number is defined as

$$
\begin{eqnarray}
    \mathrm{cond}_{E, f}(A, x)
    & := &
        \lim_{\epsilon \rightarrow 0}
        \sup
        \left\{
            \frac{
                \norm{\Delta x}_{\infty}
            }{
                \epsilon \norm{x}_{\infty}
            }
            \mid
            (A + \Delta A)
            (x + \Delta x)
            =
            b + \Delta b,
            \
            \norm{\Delta A} \le \epsilon E,
            \
            \norm{\Delta b} \le \epsilon f
        \right\},
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Assumptions

$$
    (A + \Delta A)x = b,
    \
    \abs{\Delta A} \le u W.
$$

$$
    u
    \norm{
        \abs{A^{-1}}
        W
    }_{\infty}
    <
    \frac{1}{2}
$$

where $A + \Delta A$ is nonsingular.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Forward error
The foward error of $\hat{x}_{i}$.

$$
    \frac{
        \norm{x - \hat{x}_{i}}_{\infty}
    }{
        \norm{x}_{\infty}
    }
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Iterative improvement of the solution of linear equations}
    \begin{algorithmic}
    \REQUIRE \\
        $A \in \mathbb{R}^{n \times n}$, \\
        $b \in \mathbb{R}^{n}$, \\
        $r_{0} := b$, \\
        $x_{0} := (0, \ldots, 0)^{\mathrm{T}} \in \mathbb{R}^{n}$,
        \FOR{$i = 1$ \TO $T$}
            \STATE Let $d_{i}$ be solution of $Ad = r_{i - 1}$ with respect to $x$,
            \STATE $r_{i} := b - Ax_{i}$,
            \STATE $x_{i} := x_{i - 1} + d_{i}$,
        \ENDFOR
        \RETURN $x_{T}$,
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>


## Heauristic analysis

#### Definition
* $\beta$, $t$,
    * the number are stored with $t$-digit $\beta$ base accuracy

$$
    u
    :=
    \frac{1}{2}
    \beta^{-t}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Heauristic 1
Gaussian elimination produces a solution of linear equation with a relatively small residual $r$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Heauristic 2
If the unit roundoff and condition satisfy $u \approx 10^{d}$ and $\kappa_{\infty}(A) \approx 10^{q}$, then Gaussian elimination produces a solution $x$ that has about $d - q$ correct decimal digits.

<div class="end-of-statement" style="text-align: right">■</div>

#### Heauristic 3
If the machine precision $u$ and condition satisfy $u \approx 10^{-d}$ and $\kappa_{\infty}(A) \approx 10^{d}$, then after $T$ executoins of Algorithm, $x$ has approximately $\min(d, k(d - q))$ correct digits.

<div class="end-of-statement" style="text-align: right">■</div>


<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Iterative improvement of the solution of linear equations}
    \begin{algorithmic}
    \REQUIRE \\
        $A \in \mathbb{R}^{n \times n}$, \\
        $b \in \mathbb{R}^{n}$, \\
        \STATE Let $\hat{x}$ be a solution of $Ax=b$.
        \STATE Let $r := b - A \hat{x}$
        \STATE Let $\hat{y}$ be $Ly=Pr$ with respect to $y$
        \STATE Let $\hat{z}$ be a solution of $Uz=\hat{y}$ with respect to $z$
        \STATE $x_{\mathrm{new}} := \hat{x} + z$,
        \RETURN $x_{\mathrm{new}}$,
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
Golub, Gene H., and Charles F. Van Loan. Matrix computations. Vol. 3. JHU Press, 2012.
