---
title: Euclidean Geometry
---

## Euclidean Geometry

#### Definition Inner Product
- $a, b \in \mathbb{R}^{n}$,

$$
    \langle a, b \rangle
    :=
    a \cdot b
    :=
    \sum_{i=1}^{n}
        a_{i}b_{i}
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Cross Product
- $a, b \in \mathbb{R}^{3}$

$$
\begin{eqnarray}
    a \times b
    & := &
        \norm{a}
        \norm{b}
        \sin(\theta)
        n
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                a_{2}b_{3} - a_{3}b_{2}
                \\
                a_{3}b_{1} - a_{1}b_{3}
                \\
                a_{1}b_{2} - a_{2}b_{1}
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

where $n$ is a unit vector perpendicular to the plane containing $a$ and $b$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Outer Product
- $a \in \mathbb{R}^{m}$,
- $b \in \mathbb{R}^{n}$,

$$
\begin{eqnarray}
    a \times b
    & := &
        \left(
            \begin{array}{c}
                a_{1}
                \\
                \vdots 
                \\
                a_{m}
            \end{array}
        \right)
        \times
        \left(
            \begin{array}{c}
                b_{1}
                \\
                \vdots 
                \\
                b_{n}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                a_{1}
                \\
                \vdots 
                \\
                a_{m}
            \end{array}
        \right)
        \left(
            \begin{array}{c}
                b_{1}
                \\
                \vdots 
                \\
                b_{n}
            \end{array}
        \right)^{T}
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{cccc}
                a_{1}b_{1} & a_{1}b_{2} \cdots & a_{1}b_{m}
                \\
                \vdots & & & \vdots
                \\
                a_{n}b_{1} & a_{n}b_{2} \cdots & a_{n}b_{m}
            \end{array}
        \right)
    \nonumber
    .
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Definition Exterior Product
- $a, b \in \mathbb{R}^{n}$

$$
\begin{eqnarray}
    a \wedge b
    & = &
        \sum_{i=1}^{n}
        \sum_{j=1}^{n}
            a_{i}
            b_{j}
            e_{i}
            \wedge
            e_{j}
    \nonumber
\end{eqnarray}
$$

where $e_{i} \wedge e_{j} = -e_{j} \wedge e_{i}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Example 1
- $a \in \mathbb{R}^{2}$,
- $b \in \mathbb{R}^{2}$,
- $e_{1}, e_{2}$
    - basis

$$
\begin{eqnarray}
    a \wedge b
    & = &
        a_{1}b_{1} e_{1}\wedge e_{1}
        +
        a_{1}b_{2} e_{1}\wedge e_{2}
        +
        a_{2}b_{1} e_{2}\wedge e_{1}
        +
        a_{2}b_{2} e_{2}\wedge e_{2}
    \nonumber
    \\
    & = &
        a_{1}b_{2} e_{1}\wedge e_{2}
        -
        a_{2}b_{1} e_{1}\wedge e_{2}
    \nonumber
    \\
    & = &
        (a_{1}b_{2} - a_{2}b_{1}) e_{1}\wedge e_{2}
    .
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Example 2
- $a \in \mathbb{R}^{3}$,
- $b \in \mathbb{R}^{3}$,
- $e_{1}, e_{2}, e_{3}$
    - basis

$$
\begin{eqnarray}
    a \wedge b
    & = &
        a_{1}b_{1} e_{1}\wedge e_{1} 
        +
        a_{1}b_{2} e_{1}\wedge e_{2}
        +
        a_{1}b_{3} e_{1}\wedge e_{3}
        +
        a_{2}b_{1} e_{2}\wedge e_{1}
        +
        a_{2}b_{2} e_{2}\wedge e_{2}
        +
        a_{2}b_{3} e_{2}\wedge e_{3}
        +
        a_{3}b_{1} e_{3}\wedge e_{1}
        +
        a_{3}b_{2} e_{3}\wedge e_{2}
        +
        a_{3}b_{3} e_{3}\wedge e_{3}
    \nonumber
    \\
    & = &
        a_{1}b_{2} e_{1}\wedge e_{2}
        +
        a_{1}b_{3} e_{1}\wedge e_{3}
        +
        a_{2}b_{1} e_{2}\wedge e_{1}
        +
        a_{2}b_{3} e_{2}\wedge e_{3}
        +
        a_{3}b_{1} e_{3}\wedge e_{1}
        +
        a_{3}b_{2} e_{3}\wedge e_{2}
    \nonumber
    \\
    & = &
        a_{1}b_{2} e_{1}\wedge e_{2}
        +
        a_{1}b_{3} e_{1}\wedge e_{3}
        -
        a_{2}b_{1} e_{1}\wedge e_{2}
        +
        a_{2}b_{3} e_{2}\wedge e_{3}
        -
        a_{3}b_{1} e_{1}\wedge e_{3}
        -
        a_{3}b_{2} e_{2}\wedge e_{3}
    \nonumber
    \\
    & = &
        (a_{1}b_{2} - a_{2}b_{1}) e_{1}\wedge e_{2}
        +
        (a_{1}b_{3} - a_{3}b_{1}) e_{1}\wedge e_{3}
        +
        (a_{2}b_{3} - a_{3}b_{2}) e_{2}\wedge e_{3}
    .
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### 2-d vectors
- $a, b, c, d \in \mathbb{R}^{2}$,

(1) $a$ and $b$ are perpendicular if

$$
    \langle a, b \rangle
    =
    a_{1}b_{1}
    +
    a_{2}b_{2}
    =
    0.
$$

(2) $a$ and $b$ are parallel if

$$
    a \times b
    =
    a_{1}b_{2} - a_{2}b_{1}
    =
    0
    .
$$

(4) $c$ is on a line which contains $a$ and $b$ if 

$$
    (b - a) \times (c - a)
    =
        (b_{1} - a_{1})(c_{2} - a_{2})
        -
        (b_{2} - a_{2})(c_{1} - a_{1})
    =
    0
    .
$$

(5) $c$ is on a line segment $b - a$ if 

$$
    (b - a) \times (c - a)
    =
        (b_{1} - a_{1})(c_{2} - a_{2})
        -
        (b_{2} - a_{2})(c_{1} - a_{1})
    =
    0
$$

and 

$$
    \langle a - c, b - c \rangle
    \le
    0
    .
$$

(7) The distance between the line $b - a$ and a point $c$ is given by

$$
\begin{eqnarray}
    \norm{c - a} |\sin(\theta)|
    & = &
        \frac{
            (b - a) \times (c - a)
        }{
            \norm{x}
        }
    \nonumber
\end{eqnarray}
$$

(8) The minimum distance between the line segment $b - a$ and a point $c$ is given by

$$
\begin{cases}
    \frac{
        (b - a) \times (c - a)
    }{
        \norm{x}
    }
    &
        (\langle a - c, b - c \rangle \neq 0)
    \\
    c - a
    &
        (\text{otherwise})
\end{cases}
$$

<div class="end-of-statement" style="text-align: right">■</div>

(9) Two line seguments $b -a$ and $d - c$ are interesected if

$$
\begin{eqnarray}
    (b - a) \times (c - a) (b - a) \times (d - a)
        & < & 0,
    \nonumber
        \\
    (d - c) \times (a - c) (d - c) \times (b - c)
        & < &0.
    \nonumber
\end{eqnarray}
$$

(10) The intersection of two line seguments $b - a$ and $d - c$ is given by

$$
\begin{eqnarray}
    a
    +
    \frac{
        (d - c)
        \times
        (c - a)
    }{
        (d - c)
        \times
        (b - a)
    }
    (b - a)
    & = &
        a
        +
        \frac{
            (d_{1} - c_{1})
            (c_{2} - a_{2})
            -
            (d_{2} - c_{2})
            (c_{1} - a_{1})
        }{
            (d_{1} - c_{1})
            (b_{2} - a_{2})
            -
            (d_{2} - c_{2})
            (b_{1} - a_{1})
        }
        (b - a)
    .
\end{eqnarray}
$$

Note that the equation cannot detect the case where the both lines are in parallel.
Indeed, if $(b - a)$ and $(d - c)$ are in parallel,

$$
    (b - a)
    \times
    (d - c)
    =
    0
    .
$$

#### Translation

Let $f(x) := a x + b$. The line which shifts $f(x)$ $m$ in a direction parallel to $f(x)$.
Let $g(x)$ be the line.
$g(x)$ has the same slope so $g(x) = ax + c$.
There is $n$ such that

$$
    ax + c
    =
    a(x - n) + b
    .
$$

By rearranging the equation

$$
    n
    =
    \frac{
        b - c
    }{
        a
    }
    .
$$

The similarilty of right triangles implies

$$
    m:(b - c) = l:n
$$

That is

$$
    l
    =
    \frac{
        m n
    }{
        (b - c)
    }
    =
    \frac{
        m
    }{
        a
    }
    .
$$

By Pythagorean theorem,

$$
\begin{eqnarray}
    & &
        n^{2}
        =
        l^{2}
        +
        m^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        n^{2}
        =
        \left(
            \frac{ m }{ a }
        \right)^{2}
        +
        m^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        n^{2}
        =
        \frac{
            m^{2}
            +
            a^{2}m^{2}
        }{
            a^{2}
        }
    \nonumber
    \\
    & \Leftrightarrow &
        n
        & = &
        \frac{
            m\sqrt{1 + a^{2}}
        }{
            a
        }
    \nonumber
\end{eqnarray}
$$

Hence

$$
\begin{eqnarray}
    & &
        \frac{(b - c)}{a}
        =
        \frac{
            m\sqrt{1 + a^{2}}
        }{
            a
        }
    \nonumber
    \\
    & \Leftrightarrow &
        c
        =
        b - m\sqrt{1 + a^{2}}
    \nonumber
\end{eqnarray}
$$

then

$$
    g(x)
    =
    ax
    +
    b - m\sqrt{1 + a^{2}}
    .
$$


## Reference
- https://en.wikipedia.org/wiki/Outer_product
- https://en.wikipedia.org/wiki/Cross_product
- https://en.wikipedia.org/wiki/Exterior_algebra
