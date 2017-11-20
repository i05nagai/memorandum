---
title: Convex function
---

## Convex Function
Properties of convex function.

## Definition
* $f: \mathbb{R}^{N}\rightarrow \mathbb{R}$

$f$が凸関数であるとは、

$$
\begin{equation}
    \forall \lambda \in [0, 1],
    \quad
    \forall x_{1}, x_{2} \in \mathbb{R}^{N},
    \quad
    f(\lambda x_{1} + (1 - \lambda)x_{2})
    \le
    \lambda f(x_{1}) + (1 - \lambda) f(x_{2})
\end{equation}
$$

を満たすことを言う。

$f$が狭義凸関数であるとは、　

$$
\begin{equation}
    \forall \lambda \in (0, 1),
    \quad
    \forall x_{1}, x_{2} \in \mathbb{R}^{N},
    \quad
    x_{1} \neq x_{2},
    \quad
    f(\lambda x_{1} + (1 - \lambda)x_{2})
    <
    \lambda f(x_{1}) + (1 - \lambda) f(x_{2})
\end{equation}
$$

を満たすことを言う。

$f$ is concave if $-f$ is convex.

## Properties

### Property. 1
開区間で定義された凸関数は、連続

### proof.
<div class="QED" style="text-align: right">$\Box$</div>

### Property. 2
開区間で定義された凸関数は、高々可算個の点を除いて微分可能。

### proof.
<div class="QED" style="text-align: right">$\Box$</div>

### Property. 3
$f$を凸関数とする。
$f$が$C^{2}$級とすると、以下は同値。

* $f$が凸関数
* 凸集合の内部で、$f$のヘッセ行列が半正定値

### proof.
<div class="QED" style="text-align: right">$\Box$</div>


### Proposition 1
* $f:\mathbb{R}^{N} \rightarrow \mathbb{R}$, $g: \mathbb{R}^{N} \rightarrow \mathbb{R}$を凸関数とする。
* $a, b \in \mathbb{R}_{\ge 0}$とする。

$a f + b g$ is convex.

### proof.
$\forall \lambda \in [0, 1]$, $$ x, y \in \mathbb{R}^{N}$$,

$$
\begin{eqnarray}
    a f(\lambda x + (1 - \lambda) y)
    +
    b g(\lambda x + (1 - \lambda) y)
    & \le &
        a (\lambda f(x) + (1 - \lambda) f(y))
        +
        b (\lambda g(x) + (1 - \lambda) g(y))
    \nonumber
    \\
    & \le &
        \lambda (af(x) + bg(x))
        +
        (1 - \lambda)(af(y) + bg(y))
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition 2
* $$I := \{1, \ldots, m\}$$,
* $$I_{i} := I \setminus \{i\}$$,
* $h:\mathbb{R}^{m} \rightarrow \mathbb{R}$,
    * convex function

$\forall i \in I$, $$x_{i}, x_{i}^{\prime} \in \mathbb{R}$$, $$x_{i} \le x_{i}^{\prime}$$,

$$
\begin{equation}
    \forall k \in I_{i},
    \
    \forall x_{k} \in \mathbb{R},
    \
    h(x_{1}, \ldots, x_{i}, \ldots, x_{m})
    \le
    h(x_{1}, \ldots, x_{i}^{\prime}, \ldots, x_{m})
    \label{condition_non_decreasing}
\end{equation}
$$

* $$f_{i}:\mathbb{R}^{N} \rightarrow \mathbb{R} \ (i \in I)$$,
    * convex function

Then $$g(x) := h(f_{1}(x), \ldots, f_{m}(x))$$ is convex.

### proof.
$\forall \lambda \in [0, 1]$, $$ x, y \in \mathbb{R}^{N}$$,

$$
\begin{eqnarray}
    h
    \left(
        f_{1}(\lambda x + (1 - \lambda) y),
        \cdots,
        f_{m}(\lambda x + (1 - \lambda) y)
    \right)
    & \le &
        h
        \left(
            \lambda f_{1}(x) + (1 - \lambda) f_{1}(y),
            \cdots,
            f_{m}(\lambda x + (1 - \lambda) y)
        \right)
    \nonumber
    \\
    & \le &
        h
        \left(
            \lambda f_{1}(x) + (1 - \lambda) f_{1}(y),
            \cdots,
            \lambda f_{m}(x) + (1 - \lambda) f_{m}(y)
        \right)
    \nonumber
    \\
    & \le &
        \lambda
        h
        \left(
            f_{1}(x),
            \cdots,
            f_{m}(x)
        \right)
        +
        (1 - \lambda)
        h
        \left(
            f_{1}(y),
            \cdots,
            f_{m}(y)
        \right)
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition 3
* $f: \mathbb{R}^{N} \rightarrow \mathbb{R}$,
    * convex
* $g: \mathbb{R}^{N} \rightarrow \mathbb{R}$,
    * convex

$$\max\{f, g\}$$ is convex.

### proof.
$$h(x, y) := \max\{x, y\}$$ is convex and satisfy $$\eqref{condition_non_decreasing}$$.

<div class="QED" style="text-align: right">$\Box$</div>

### Propostion. 4
* $\phi:\mathbb{R}^{N} \rightarrow \mathbb{R}$ is concave
* $h:\mathbb{R} \rightarrow \mathbb{R}$ is convex and non increasing.
    * i.e. $x \le y$, $h(x) \ge h(y)$

$h(\phi(x))$ is convex

### proof.
$$x, y \in \mathbb{R}^{N}$$, 

$$
    \phi(\lambda x + (1 - \lambda) y)
    \ge
    \lambda
    \phi(x)
    +
    (1 - \lambda)
    \phi(y)
$$

Hence

$$
\begin{eqnarray}
    h(\phi(\lambda x + (1 - \lambda) y))
    & \le &
        h(\lambda \phi(x) + (1 - \lambda) \phi(y))
    \nonumber
    \\
    & \le &
        \lambda
        h(\phi(x))
        +
        (1 - \lambda)
        h(\phi(y))
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


### Proposition5
* $f:\mathbb{R}^{N} \rightarrow \mathbb{R}$
    * convex set
* $a \in \mathbb{R}$

$$
    \mathrm{level}_{a}(f)
    :=
    \{
        x \in \mathbb{R}^{N}
        \mid
        f(x) \le a
    \}
$$

* (1) level set $$\mathrm{level}_{a}(f)$$ is convex
* (2) $$\{x \in \mathbb{R}^{N} \mid f(x) < a \}$$ is convex,
* (3) $$\{x \in \mathbb{R}^{N} \mid f(x) \ge a\}$$ is convex

### proof.
(1)
By <a href="#proposition8">proposition</a>, level set is convex.

(2)

(3)

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition 6
* $f: \mathbb{R}^{N} \rightarrow \mathbb{R}$
    * convex function
* $$i \in \{1, \ldots, N\}$$,
* $$g: \mathbb{R}^{N-1} \rightarrow \mathbb{R}$$,

$$
    g(x_{1}, \ldots, x_{i-1}, x_{i+1}, \ldots, x_{N})
    := \sup_{x_{i} \in \mathbb{R}}f(x_{1}, \ldots, x_{N})
$$

* $$D := \{x \in \mathbb{R}^{N-1} \mid g(x) > -\infty \}$$,

Then $g$ is convex over $D$.

### proof.
$N = 2$, $$g(x_{1}) := \sup_{x_{2} \in \mathbb{R}} f(x_{1}, x_{2})$$とする。
$$\lambda \in [0, 1]$$, $$\forall x_{1}, y_{1} \in D$$とする。
ここで、$$\forall x_{2} \in \mathbb{R}$$とすると、$\mathbb{R}$が連結より、$$\exists x_{2}^{\prime}, y_{2}^{\prime}(x_{2}) \in \mathbb{R}$$, s.t.

$$
    x_{2}
    =
    \lambda x_{2}^{\prime} + (1-\lambda) y_{2}^{\prime}
$$

となる。
このとき、

$$
\begin{eqnarray}
    \forall x_{2} \in \mathbb{R},
    \
    f(\lambda x_{1} + (1 - \lambda) y_{1}, x_{2})
    & \le &
        f(\lambda x_{1} + (1 - \lambda) y_{1}, \lambda x_{2}^{\prime} + (1 - \lambda) y_{2}^{\prime})
    \nonumber
    \\
    & \le &
        \lambda
        f(x_{1}, x_{2}^{\prime})
        +
        (1 - \lambda)
        f(y_{1}, y_{2}^{\prime})
    \nonumber
    \\
    & \le &
        \lambda
        \sup_{y \in \mathbb{R}}
        f(x_{1}, y)
        +
        (1 - \lambda)
        \sup_{y \in \mathbb{R}}
        f(y_{1}, y)
    \nonumber
    \\
    & \le &
        \lambda
        g(x_{1})
        +
        (1 - \lambda)
        g(y_{1})
\end{eqnarray}
$$

ここで、$$x_{2}$$は任意であったから

$$
    g(\lambda x_{1} + (1-\lambda)y_{1})
    \le
    \lambda
    g(x_{1})
    +
    (1 - \lambda)
    g(y_{1})
$$

となる。

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition 7
* $$C \subseteq \mathbb{R}^{n}$$,
    * closed convex set

$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$を以下のように定義すると、$f$はconvex functionである。

$$
\begin{eqnarray}
    f(x)
    & := &
        \mathrm{dist}(x, C)
    \nonumber
    \\
    & := &
        \inf
        \{
            \|x - y\|
            \mid
            y \in C
        \}
    \nonumber
    \\
    & = &
        \min
        \{
            \|x - y\|
            \mid
            y \in C
        \}
    \nonumber
\end{eqnarray}
$$

### proof.
$$x_{1}, x_{2} \in \mathbb{R}^{n}$$, $\lambda \in [0, 1]$とする。
$\forall y \in C$について、

$$
\begin{eqnarray}
    \|\lambda x_{1} + (1 - \lambda) x_{2} - y\|
    & = &
        \|\lambda x_{1} + (1 - \lambda) x_{2} - (\lambda y + (1 - \lambda)y )\|
    \nonumber
    \\
    & \le &
        \lambda \|x_{1} - y_{1} \|
        +
        (1 - \lambda) \| x_{2} - y_{2} \|
\end{eqnarray}
$$

となる。
ここで、左辺のinfをとれば

$$
\begin{eqnarray}
    f(\lambda x_{1} + (1 - \lambda) x_{2})
    & \le &
        \lambda \|x_{1} - y_{1} \|
        +
        (1 - \lambda) \| x_{2} - y_{2} \|
    \nonumber
\end{eqnarray}
$$

となる。
左辺は$y$に依存しないから右辺の第一項の$y$についてinfをとれば、

$$
    f(\lambda x_{1} + (1 - \lambda) x_{2})
    \le
        \lambda f(x_{1})
        +
        (1 - \lambda) \| x_{2} - y_{2} \|
$$

であり、 同様に

$$
    f(\lambda x_{1} + (1 - \lambda) x_{2})
    \le
        \lambda f(x_{1})
        +
        (1 - \lambda) f(x_{2})
$$

を得る。

<div class="QED" style="text-align: right">$\Box$</div>

### Remark
closed convex への射影がconvex functionになるということを延べている。
命題の中で、infがminになることの証明は与えていないが、これば$\mathbb{R}$上のHilbert空間一般に成り立つ性質である。
この証明は <a href="{{ site.baseurl }}/math/hilbert_space.html#theorem-3">ここ</a>に譲る。

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition8
* $$f: \mathbb{R}^{n} \rightarrow \mathbb{R}$$,
    * convex function
* $$g: \mathbb{R}^{n} \rightarrow \mathbb{R}$$,
    * convex function
* $c \in \mathbb{R}$,

$$
\begin{eqnarray}
    \forall x \in \mathbb{R}^{n},
    \
    f(x)
    & \le &
        c
    \nonumber
    \\
    g(x)
    & \le &
        c
    \nonumber
\end{eqnarray}
$$

Then

$$
    \forall \lambda \in [0, 1]
    \
    \lambda f(x)
    +
    (1 - \lambda) g(x)
    \le
    c
    .
$$

### proof.
It is easy to see that

$$
\begin{eqnarray}
    \lambda f(x)
    +
    (1 - \lambda) g(x)
    & \le &
        \lambda c
        +
        (1 - \lambda) c
    \nonumber
    \\
    & = &
        c
    \nonumber
    .
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition9
* $A \subseteq \mathbb{R}^{n}$
    * convex set
* $B \subseteq \mathbb{R}^{n}$
    * convex set

Then

* (i) $-A$ is convex
* (ii) $A + B$ is convex
* (iii) closure $\bar{A}$ is convex

### proof.
(i)

$$
    -A
    =
    \{
        -x
        \mid
        x \in A
    \}
$$

Since

$$
    \forall x^{\prime}, y^{\prime} \in (-A)
    \
    \exists x, y \in A,
    \
    \text{ s.t. }
    \
    x^{\prime} = -x,
    \
    y^{\prime} = -y,
$$

and $$\forall \lambda \in [0, 1]$$, $$\lambda x + (1 - \lambda) y \in A$$, we have

$$
    \forall \lambda \in [0, 1],
    \
    \lambda(-x)
    +
    (1 - \lambda)(-y)
    =
    -
    \left(
        \lambda x
        +
        (1 - \lambda) y
    \right)
    \in (-A)
    .
$$

(ii)
Since

$$
    \forall x^{\prime}, x^{\prime\prime} \in (A + B)
    \
    \exists u^{\prime}, u^{\prime\prime} \in A,
    \
    \exists v^{\prime}, v^{\prime\prime} \in B,
    \
    \text{ s.t. }
    \
    x^{\prime} = u^{\prime} + v^{\prime}
    \
    x^{\prime\prime} = u^{\prime\prime} + v^{\prime\prime}
$$

and $$\forall \lambda \in [0, 1]$$,

$$
\begin{eqnarray}
    \lambda u^{\prime}
    +
    (1 - \lambda) v^{\prime}
    & \in &
        A
    \nonumber
    \\
    \lambda u^{\prime\prime}
    +
    (1 - \lambda) v^{\prime\prime}
    & \in &
        B
    .
    \nonumber
\end{eqnarray}
$$

We have $\forall \lambda \in [0, 1]$,

$$
    \lambda x^{\prime}
    +
    (1 - \lambda) x^{\prime\prime}
    =
    (
        \lambda u^{\prime}
        +
        (1 - \lambda) v^{\prime}
    )
    +
    (
        \lambda u^{\prime\prime}
        +
        (1 - \lambda) v^{\prime\prime}
    )
    \in
    A + B
    .
$$

(iii)

$$
    \forall x, y \in \bar{A}
    \
    \exists (x_{i})_{i \in \mathbb{N}},
        (y_{i})_{i \in \mathbb{N}} \in A,
    \
    \text{ s.t. }
    \
    x_{i} \rightarrow x,
    \
    y_{i} \rightarrow y,
$$

Since

$$
\begin{eqnarray}
    \forall \lambda \in [0, 1]
    \
    \forall i \in \mathbb{N},
    \
    \lambda x_{i}
    +
    (1 - \lambda) y_{i}
    \in
    A
    \subseteq
    \bar{A}
    ,
\end{eqnarray}
$$

by taking the limit we obtain

$$
    \forall \lambda \in [0, 1]
    \
    \lambda x
    +
    (1 - \lambda) y
    \in
    \bar{A}
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Thereom10 Separation theorem
* $A \subseteq \mathbb{R}^{n}$
    * convex set
* $B \subseteq \mathbb{R}^{n}$
    * convex set

Then

$$
    \exists v \in \mathbb{R}^{n},
    \
    \exists c \in \mathbb{R},
    \
    \text{ s.t. }
    \
    \forall x \in A,
    \
    \forall y \in B,
    \
    \langle
        x,
        v
    \rangle
    \ge
    c
    \ge
    \langle
        v,
        y
    \rangle
$$

### proof.
Let

$$
\begin{eqnarray}
    K
    & := &
        A + (-B)
    \nonumber
    \\
    & = &
        \{
            x - y
            \mid
            x \in A,
            \
            y \in B
        \}
    .
    \nonumber
\end{eqnarray}
$$

Since $A$ and $B$ is convex, $K$ is convex.
Moreover closure of $K$, $\bar{K}$, is convex.
By <a href="{{ site.baseurl }}/math/hilbert_space.html#theorem-3">projection theorem</a>, there exists $v \in \bar{K}$ such that

$$
    \|v\|
    =
    \min_{u \in K}
    \|u\|
    .
$$

Since $\bar{K}$ is convex, we have

$$
    \forall x \in \bar{K},
    \
    \forall t \in [0, 1],
    \
    v + t(x - v) \in \bar{K}
    .
$$

Then For $t \in (0, 1]$,

$$
\begin{eqnarray}
    & &
        \|v\|^{2}
        \le
        \|v + t(x - v)\|^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \|v\|^{2}
        \le
        \|v\|^{2}
        +
        2t\langle v, (x - v) \rangle
        +
        t^{2} \|x - v\|^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        0
        \le
        2t\langle v, x \rangle
        -
        2t\langle v, v \rangle
        +
        t^{2} \|x - v\|^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        0
        \le
        2\langle v, x \rangle
        -
        2\|v\|^{2}
        +
        t \|x - v\|^{2}
    \nonumber
\end{eqnarray}
$$

Letting $$t \rightarrow 0$$, we obtain

$$
\begin{eqnarray}
    & &
        0
        \le
        2 \langle v, x \rangle
        -
        2\| v\|^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        \| v\|^{2}
        \le
        \langle v, x \rangle
    .
    \nonumber
\end{eqnarray}
$$

Hence $$\forall y \in A, \forall z \in B$$,

$$
\begin{eqnarray}
    & &
        \| v\|^{2}
        \le
        \langle y - z, v \rangle
    \nonumber
    \\
    & \Leftrightarrow &
        \| v\|^{2}
        \le
        \langle y, v \rangle
        -
        \langle z, v \rangle
    \nonumber
    \\
    & \Leftrightarrow &
        \langle z, v \rangle
        +
        \| v\|^{2}
        \le
        \langle y, v \rangle
    \nonumber
\end{eqnarray}
$$

Thus, we take $$c := \|v\|^{2} + \sup_{y \in B}\langle y, v \rangle$$,

$$
    \forall y \in A,
    \
    \forall z \in B,
    \
    \langle z, v \rangle
    \le
    c
    \le
    \langle y, v \rangle
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem11
* $M \subseteq \mathbb{R}^{n}$,
    * convex set
* $f: M \rightarrow \mathbb{R}$,
    * convex function
* $x^{*} \in \mathbb{R}^{n}$,

Then

* (1) If $$x^{*}$$ is local minimizer of $f$ on $M$, then $$x^{*}$$ is global minimizer of $f$ on $M$.
* (2) Set of global minimizer, $$\arg\min_{x \in M}f(x)$$, is convex.

$$
    \arg\min_{x \in M}f(x)
    :=
    \{
        y \in \mathbb{R}^{n}
        \mid
        \min f(x)
        =
        y
    \}
$$

* (3) If $f$ is strictly convex, $$\mathrm{card}(\arg\min_{x \in M}f(x)) \in \{0, 1\}$$.

### proof.
(1)
Let $$B_{\epsilon}(x)$$ be $\epsilon$ oepn ball at $x$:

$$
    x \in \mathbb{R}^{n},
    \
    \epsilon > 0
    \quad
    B_{\epsilon}(x)
    :=
    \{
        y \in \mathbb{R}^{n}
        \mid
        |x - y| < \epsilon
    \}
$$

Since $$x^{*}$$ is a localm minimizer, we have

$$
    \exists \epsilon > 0,
    \
    \text{ s.t. }
    \
    \forall y \in B_{\epsilon}(x^{*})
    \
    \Rightarrow
    \
    f(y)
    \ge
    f(x^{*})
    .
$$

Let $y \in M$ be fixed.
Since $M$ is convex, it is easy to see

$$
\begin{eqnarray}
    \forall t \in (0, 1),
    \quad
    x_{t}
    & := &
        t y + (1 - t) x^{*}
        \in M
    \nonumber
\end{eqnarray}
$$

We take arbitrary constant $\delta > 0$ such that

$$
    \delta
    <
    \min
    \left\{
        1/2,
        \frac{
            \epsilon
        }{
            |x^{*} - y|
        }
    \right\}
    .
$$

Then

$$
    \forall t \in (0, \delta),
    \quad
    x_{t} \in B_{\epsilon}
    .
$$

Indeed,

$$
\begin{eqnarray}
    |x_{t} - x^{*}|
    & = &
        |ty - tx^{*}|
    \nonumber
    \\
    & = &
        |t|
        |y - x^{*}|
    \nonumber
    & < &
        \epsilon
    \nonumber
    .
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \forall t \in (0, \delta)
    \quad
    f(x_{t}) - f(x^{*})
    & \le &
            tf(y) + (1-t)f(x^{*}) - f(x^{*})
    \nonumber
    \\
    & \le &
            tf(y) - tf(x^{*})
    .
    \nonumber
\end{eqnarray}
$$

The LHS of the above equation is nonnegative since $$x_{t} \in B_{\epsilon}(x^{*})$$.
Therefore,

$$
    \forall t \in (0, \delta),
    \quad
    0
    \le
    tf(y) - tf(x^{*})
    \
    \Rightarrow
    \
    0
    \le
    f(y) - f(x^{*})
    .
$$

(2)
Let $$c := \min_{x \in M} f(x)$$.

$$
\begin{eqnarray}
    \arg \min_{x \in M}
        f(x)
    & = &
        \mathrm{level}_{c}(f)
    \nonumber
    \\
    & = &
        \{
            y \in \mathbb{R}^{n}
            \mid
            y \le c
        \}
    .
    \nonumber
\end{eqnarray}
$$

By <a href="#proposition5">proposition</a>, level set is convex so that $$\arg \min_{x \in M}f(x)$$ is convex.

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem12 Separation theorem between a point and a set
* $S \subseteq \mathbb{R}^{n}$
    * closed convex
* $y \notin S, y \in \mathbb{R}^{n}$,

There exist $$a \in \mathbb{R}^{n}$$, $$c \in \mathbb{R}$$ such that

$$
\begin{eqnarray}
    \langle a, y \rangle
    & > &
        c
    \nonumber
    \\
    \forall x \in S,
    \
    \langle a, x \rangle
    & \le &
        c
    \nonumber
\end{eqnarray}
$$

### proof.
Let $x \in S$ be fixed.
By <a href="{{ site.baseurl }}/math/hilbert_space.html#theorem-3">projection onto closed convex set over hilbert space</a>, there exists $$x_{0} \in S$$ such that

$$
\begin{eqnarray}
    \| x - x_{0}\|
    & = &
        \inf_{y \in S} \|x - y\|
    \nonumber
    \\
    \forall y \in S,
    \
    \langle x - x_{0}, x_{0} - y \rangle
    & \ge &
        0
    .
    \nonumber
\end{eqnarray}
$$

It follows that

$$
\begin{eqnarray}
    0
    & \le &
        \langle x - x_{0}, x_{0} - y \rangle
    \nonumber
    \\
    & = &
        \langle x, x_{0} - y \rangle
        -
        \langle x_{0}, x_{0} - y \rangle
    .
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    \langle x_{0}, x_{0} - y \rangle
    \le
    \langle x, x_{0} - y \rangle
    .
    \nonumber
\end{eqnarray}
$$

On the other hand, $$y \notin S$$,

$$
\begin{eqnarray}
    0
    & < &
        \|y - x_{0} \|^{2}
    \nonumber
    \\
    & = &
        \langle y - x_{0}, y - x_{0} \rangle
    \nonumber
    \\
    & = &
        \langle y, y - x_{0} \rangle
        -
        \langle x_{0}, y - x_{0} \rangle
    \nonumber
    \\
    & = &
        \langle y, y - x_{0} \rangle
        +
        \langle x_{0}, x_{0} - y \rangle
    .
    \nonumber
\end{eqnarray}
$$

Thus,

$$
\begin{eqnarray}
    \|y - x_{0}\|^{2}
    & \le &
        \langle y, y - x_{0} \rangle
        +
        \langle x, x_{0} - y \rangle
    \nonumber
    \\
    & = &
        \langle y - x, y - x_{0} \rangle
    \nonumber
    \\
    & = &
        \langle y - x_{0}, y - x \rangle
    \nonumber
\end{eqnarray}
$$

Now we take $$a := y - x_{0} \in \mathbb{R}^{n}$$.
Then

$$
\begin{eqnarray}
    \|a\|^{2}
    & \le &
        \langle a, y - x \rangle
    \nonumber
    & = &
        \langle a, y \rangle
        -
        \langle a, x \rangle
    \nonumber
\end{eqnarray}
$$

Hence we have

$$
    \forall x \in S,
    \quad
    \langle a, y \rangle
    \ge
    \|a\|^{2}
    +
    \langle a, x \rangle
    .
$$

Let $$c := \sup_{x \in S}\langle a, x \rangle$$.
By the above equation, $$c < \infty$$.
Moreover, since $$\|a\|^{2}$$,

$$
\begin{eqnarray}
    \langle a, y \rangle
    & \ge &
        \|a\|^{2}
        +
        c
    \nonumber
    \\
    & > &
        c
    .
\end{eqnarray}
$$

By definition  of $c$,

$$
    \forall x \in S,
    \quad
    \langle a, x \rangle
    \ge
    c
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Optimum
* 狭義凸関数は最小値を取る点が存在するならば、1点である


## Example of convex functions
* $f: \mathbb{R}^{N} \rightarrow \mathbb{R}$
    * $C^{2}$ function
* $g: \mathbb{R}^{N} \rightarrow \mathbb{R}$
    * $C^{2}$ function

$h := f / g$とする。
$h$の二階微分を考えると,

$$
\begin{eqnarray}
    \frac{\partial h}{\partial x_{i}} 
    =
    \frac{
        \frac{\partial f}{\partial x_{i}} g
        -
        f \frac{\partial g}{\partial x_{i}}
    }{
        g^{2}
    }
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{\partial^{2} h}{\partial x_{i}^{2}} 
    & = &
        \frac{
            \left(
                \frac{\partial }{\partial x_{i}}
                    \left(
                        \frac{\partial f}{\partial x_{i}} g
                        -
                        f \frac{\partial g}{\partial x_{i}}
                    \right)
            \right)
                g^{2}
            -
            \left(
                \frac{\partial f}{\partial x_{i}} g
                -
                f \frac{\partial g}{\partial x_{i}}
            \right)
                2g
                \frac{\partial g}{\partial x_{i}} 
        }{
            g^{4}
        }
    \nonumber
    \\
    & = &
        \frac{
            \left(
                \left(
                    \frac{\partial^{2} f}{\partial x_{i}^{2}} g
                    +
                    \frac{\partial f}{\partial x_{i}}
                        \frac{\partial g}{\partial x_{i}}
                    -
                    \frac{\partial f}{\partial x_{i}}
                        \frac{\partial g}{\partial x_{i}}
                    -
                    f
                        \frac{\partial^{2} g}{\partial x_{i}^{2}}
                \right)
            \right)
                g
            -
            \left(
                2
                \frac{\partial f}{\partial x_{i}} g
                \frac{\partial g}{\partial x_{i}} 
                -
                2
                f
                \left(
                    \frac{\partial g}{\partial x_{i}}
                \right)^{2}
            \right)
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            \frac{\partial^{2} f}{\partial x_{i}^{2}} g^{2}
            -
            fg
                \frac{\partial^{2} g}{\partial x_{i}^{2}}
            -
            2
            \frac{\partial f}{\partial x_{i}} g
            \frac{\partial g}{\partial x_{i}} 
            +
            2 f
            \left(
                \frac{\partial g}{\partial x_{i}}
            \right)^{2}
        }{
            g^{3}
        }
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{\partial^{2} h}{\partial x_{i} \partial x_{j}} 
    & = &
        \frac{
            \left(
                \frac{\partial^{2} f}{\partial x_{i} \partial x_{j}} g
                +
                \frac{\partial f}{\partial x_{i}}
                    \frac{\partial g}{\partial x_{j}}
                -
                \frac{\partial f}{\partial x_{j}}
                    \frac{\partial g}{\partial x_{i}}
                -
                f
                    \frac{\partial^{2} g}{\partial x_{i} \partial x_{j}}
            \right)
                g
            -
            \left(
                2 g
                \frac{\partial f}{\partial x_{i}}
                \frac{\partial g}{\partial x_{j}}
                -
                2 f
                    \frac{\partial g}{\partial x_{i}}
                    \frac{\partial g}{\partial x_{j}}
            \right)
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            \frac{\partial^{2} f}{\partial x_{i} \partial x_{j}} g^{2}
            +
            \frac{\partial f}{\partial x_{i}}
                \frac{\partial g}{\partial x_{j}}
                g
            -
            \frac{\partial f}{\partial x_{j}}
                \frac{\partial g}{\partial x_{i}}
                g
            -
            f g
                \frac{\partial^{2} g}{\partial x_{i} \partial x_{j}}
            -
            2 g
            \frac{\partial f}{\partial x_{i}}
            \frac{\partial g}{\partial x_{j}}
            +
            2 f
                \frac{\partial g}{\partial x_{i}}
                \frac{\partial g}{\partial x_{j}}
        }{
            g^{3}
        }
\end{eqnarray}
$$

$$f(x):= \sum_{i=1}^{N}$$, $$g(x) := \sum_{i=1}^{N} x$$,とすると、

$$
\begin{eqnarray}
    \frac{\partial f}{\partial x_{i}}
    & = &
        2x_{i}
    \nonumber
    \\
    \frac{\partial^{2} f}{\partial x_{i}^{2}}
    & = &
        2
    \nonumber
    \\
    \frac{\partial^{2} f}{\partial x_{i} \partial x_{j}}
    & = &
        0
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{\partial g}{\partial x_{i}}
    & = &
        1
    \nonumber
    \\
    \frac{\partial^{2} g}{\partial x_{i}^{2}}
    & = &
        0
    \nonumber
    \\
    \frac{\partial^{2} g}{\partial x_{i} \partial x_{j}}
    & = &
        0
    \nonumber
\end{eqnarray}
$$

より、

$$
\begin{eqnarray}
    \frac{\partial^{2} h}{\partial x_{i}^{2}}
    & = &
        \frac{
            \frac{\partial^{2} f}{\partial x_{i}^{2}} g^{2}
            -
            fg
                \frac{\partial^{2} g}{\partial x_{i}^{2}}
            -
            2
            \frac{\partial f}{\partial x_{i}} g
            \frac{\partial g}{\partial x_{i}} 
            +
            2 f
            \left(
                \frac{\partial g}{\partial x_{i}}
            \right)^{2}
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            2 g^{2}
            -
            0
            -
            2x_{i}g
            +
            2f
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            2 g^{2}
            -
            2x_{i}g
            +
            2f
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            2
        }{
            g^{3}
        }
        \left(
            g (g - x_{i})
            +
            f
        \right)
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{\partial^{2} h}{\partial x_{i} \partial x_{j}}
    & = &
        \frac{
            \frac{\partial^{2} f}{\partial x_{i} \partial x_{j}} g^{2}
            +
            \frac{\partial f}{\partial x_{i}}
                \frac{\partial g}{\partial x_{j}}
                g
            -
            \frac{\partial f}{\partial x_{j}}
                \frac{\partial g}{\partial x_{i}}
                g
            -
            f g
                \frac{\partial^{2} g}{\partial x_{i} \partial x_{j}}
            -
            2 g
            \frac{\partial f}{\partial x_{i}}
            \frac{\partial g}{\partial x_{j}}
            +
            2 f
                \frac{\partial g}{\partial x_{i}}
                \frac{\partial g}{\partial x_{j}}
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            0
            +
            2x_{i}g
            -
            2x_{j}g
            -
            0
            -
            2gx_{i}
            +
            2f
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            2x_{i}g
            -
            2x_{j}g
            -
            2gx_{i}
            +
            2f
        }{
            g^{3}
        }
    \nonumber
    \\
    & = &
        \frac{
            2
        }{
            g^{3}
        }
        \left(
            -
            x_{j}g
            +
            f
        \right)
\end{eqnarray}
$$

$$x \ge 0$$,

$$
\begin{eqnarray}
    \sum_{i=1}^{N}
        \sum_{j=1}^{N}
            x_{i}
            \frac{\partial^{2} h}{\partial x_{i} \partial x_{j}}
            x_{j}
    & = &
        \frac{2}{g^{3}}
        \left(
            \sum_{i=1}^{N}
                x_{i}^{2}
                ((g - x_{i})g + f)
            +
            \sum_{i=1}^{N}
                \sum_{i=j+1}^{N}
                2
                \left(
                    x_{i}
                    x_{j}
                    (f - x_{j}g)
                \right)
        \right)
\end{eqnarray}
$$

## Reference
* [凸関数 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%87%B8%E9%96%A2%E6%95%B0)
* [Convex function - Wikipedia](https://en.wikipedia.org/wiki/Convex_function)
* [Hyperplane separation theorem - Wikipedia](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem)
* [chapitre_3.pdf](https://ljk.imag.fr/membres/Anatoli.Iouditski/cours/convex/chapitre_3.pdf)
