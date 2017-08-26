---
title: Convex function
---

## Convex Function
凸関数

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


### Proposition. 1
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

### Proposition. 2
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

### Proposition. 3
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


### Proposition. 5
$f:\mathbb{R}^{N} \rightarrow \mathbb{R}$を凸関数とする。
$a \in \mathbb{R}$とする。

レベル集合$$\{x \in \mathbb{R}^{N} \mid f(x) < a \}$$及び$$\{x \in \mathbb{R}^{N} \mid f(x) \ge a\}$$は凸集合である。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition. 6
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

### Optimum
* 凸関数の極小値は最小値
* 狭義凸関数は最小値を取る点が存在するならば、1点である


## Example of convex functions



## Reference
* [凸関数 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%87%B8%E9%96%A2%E6%95%B0)
* [Convex function - Wikipedia](https://en.wikipedia.org/wiki/Convex_function)

