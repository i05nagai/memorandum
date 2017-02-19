---
title: Brent method
---

## Brent method

## Summary


## Symbol

## Definition

## Problem
2点を与える$(x_{0}, f(x_{1}))$, $(x_{1}, f(x_{1}))$とする。
$[x_{0}, x_{1}]$が$f(x)=0$となる$x$を含んでいるとする。
$f(x) = 0$を満たす$x \in \mathbb{R}$を見つける問題。

## Theory

## Algorithm
2点を与える$(x_{0}, f(x_{1}))$, $(x_{1}, f(x_{1}))$とする。
$x_{2} := (x_{0} + x_{1}) / 2$とおく。
上の三点に対して、$x$に対する2次補間を行う。
つまり、$x$軸と$y$軸を考えた場合、$x$を$y$の関数だと思って２次補間する。
補間方法は以下の簡単なものを用いる。

$$
\begin{eqnarray}
    x
    =
    \frac{
        (y - f(x_{0}))(y - f(x_{1}))
    }{
        (f(x_{2}) - f(x_{0}))(f(x_{2}) - f(x_{1}))
    }
    x_{2}
    +
    \frac{
        (y - f(x_{0}))(y - f(x_{2}))
    }{
        (f(x_{1}) - f(x_{0}))(f(x_{1}) - f(x_{2}))
    }
    x_{1}
    +
    \frac{
        (y - f(x_{1}))(y - f(x_{2}))
    }{
        (f(x_{0}) - f(x_{1}))(f(x_{0}) - f(x_{2}))
    }
    x_{0}
\end{eqnarray}
$$

この時、$y=0$とし、$$R := f(x_{1}) / f(x_{2})$$, $$S := f(x_{1}) / f(x_{0})$$, $$T := f(x_{0}) / f(x_{2})$$とおく。
また、$$ST = R$$より$$R^{2} - ST = STR - ST^{2}$$に注意する。

$$
\begin{eqnarray}
    x
    & = &
        \frac{
            f(x_{0})f(x_{1})
        }{
            (f(x_{2}) - f(x_{0}))(f(x_{2}) - f(x_{1}))
        }
        x_{2}
        +
        \frac{
            f(x_{0})f(x_{2})
        }{
            (f(x_{1}) - f(x_{0}))(f(x_{1}) - f(x_{2}))
        }
        x_{1}
        +
        \frac{
            f(x_{1})f(x_{2})
        }{
            (f(x_{0}) - f(x_{1}))(f(x_{0}) - f(x_{2}))
        }
        x_{0}
    \nonumber
    \\
    & = &
        \frac{
            f(x_{0})
            f(x_{1})
            (f(x_{1}) - f(x_{0}))
        }{
            (f(x_{0}) - f(x_{2}))
            (f(x_{1}) - f(x_{2}))
            (f(x_{1}) - f(x_{0}))
        }
        x_{2}
        +
        \frac{
            f(x_{0})
            f(x_{2})
            (f(x_{0}) - f(x_{2}))
        }{
            (f(x_{1}) - f(x_{0}))
            (f(x_{1}) - f(x_{2}))
            (f(x_{0}) - f(x_{2}))
        }
        x_{1}
        +
        \frac{
            -
            f(x_{1})
            f(x_{2})
            (f(x_{1}) - f(x_{2}))
        }{
            (f(x_{1}) - f(x_{0}))
            (f(x_{0}) - f(x_{2}))
            (f(x_{1}) - f(x_{2}))
        }
        x_{0}
    \nonumber
    \\
    & = &
        \frac{
            f(x_{0})
            f(x_{1})
            (f(x_{1}) - f(x_{0}))
        }{
            f(x_{2})(T - 1)
            f(x_{2})(R - 1)
            f(x_{0})(S - 1)
        }
        x_{2}
        +
        \frac{
            f(x_{0})
            f(x_{2})
            (f(x_{0}) - f(x_{2}))
        }{
            f(x_{0})(S - 1)
            f(x_{2})(R - 1)
            f(x_{2})(T - 1)
        }
        x_{1}
        +
        \frac{
            -
            f(x_{1})
            f(x_{2})
            (f(x_{1}) - f(x_{2}))
        }{
            f(x_{0})(S - 1)
            f(x_{2})(T - 1)
            f(x_{2})(R - 1)
        }
        x_{0}
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            f(x_{2})^{2}
            f(x_{0})
            (T - 1)
            (R - 1)
            (S - 1)
        }
        \left(
            f(x_{0})
            f(x_{1})
            (f(x_{1}) - f(x_{0}))
            x_{2}
            +
            f(x_{0})
            f(x_{2})
            (f(x_{0}) - f(x_{2}))
            x_{1}
            -
            f(x_{1})
            f(x_{2})
            (f(x_{1}) - f(x_{2}))
            x_{0}
        \right)
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            f(x_{2})^{2}
            f(x_{0})
            (T - 1)
            (R - 1)
            (S - 1)
        }
        \left(
            f(x_{0})
            f(x_{1})^{2}
            x_{2}
            -
            f(x_{0})^{2}
            f(x_{1})
            x_{2}
            +
            f(x_{0})^{2}
            f(x_{2})
            x_{1}
            -
            f(x_{0})
            f(x_{2})^{2}
            x_{1}
            -
            f(x_{1})^{2}
            f(x_{2})
            x_{0}
            +
            f(x_{1})
            f(x_{2})^{2}
            x_{0}
        \right)
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            f(x_{2})^{2}
            f(x_{0})
            Q
        }
        \left(
            Q
            x_{1}
            f(x_{2})^{2}
            f(x_{0})
            -
            Q
            x_{1}
            f(x_{2})^{2}
            f(x_{0})
            +
            f(x_{0})
            f(x_{1})^{2}
            x_{2}
            -
            f(x_{0})^{2}
            f(x_{1})
            x_{2}
            +
            f(x_{0})^{2}
            f(x_{2})
            x_{1}
            -
            f(x_{0})
            f(x_{2})^{2}
            x_{1}
            -
            f(x_{1})^{2}
            f(x_{2})
            x_{0}
            +
            f(x_{1})
            f(x_{2})^{2}
            x_{0}
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{
            1
        }{
            f(x_{2})^{2}
            f(x_{0})
            Q
        }
        \left(
            -
            Q
            x_{1}
            f(x_{2})^{2}
            f(x_{0})
            +
            f(x_{0})
            f(x_{1})^{2}
            x_{2}
            -
            f(x_{0})^{2}
            f(x_{1})
            x_{2}
            +
            f(x_{0})^{2}
            f(x_{2})
            x_{1}
            -
            f(x_{0})
            f(x_{2})^{2}
            x_{1}
            -
            f(x_{1})^{2}
            f(x_{2})
            x_{0}
            +
            f(x_{1})
            f(x_{2})^{2}
            x_{0}
        \right)
    \nonumber
\end{eqnarray}
$$

更に、

$$
\begin{eqnarray}
    x
    & = &
        x_{1}
        +
        \frac{
            1
        }{
            Q
        }
        \left(
            -
            Q
            x_{1}
            +
            R^{2}
            x_{2}
            -
            R
            T
            x_{2}
            +
            T
            x_{1}
            -
            x_{1}
            -
            S
            R
            x_{0}
            +
            S
            x_{0}
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{1}{Q}
        \left(
            -
            Q
            x_{1}
            +
            x_{2}
            (R^{2} - R T)
            +
            x_{1}
            (T - 1)
            +
            S
            x_{0}
            (1 - R)
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{1}{Q}
        \left(
            -
            S
            (R - 1)
            (T - 1)
            x_{1}
            +
            (R - 1)
            (T - 1)
            x_{1}
            +
            x_{1}
            (T - 1)
            +
            x_{2}
            S(TR - T)
            +
            S
            x_{0}
            (1 - R)
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{1}{Q}
        \left(
            -
            S
            (R - 1)
            (T - 1)
            x_{1}
            +
            R 
            (T - 1)
            x_{1}
            +
            x_{2}
            S(TR - T)
            +
            S
            x_{0}
            (1 - R)
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{S}{Q}
        \left(
            (1 - R)
            T
            x_{1}
            -
            (1 - R)
            x_{1}
            +
            T
            (T - 1)
            x_{1}
            +
            x_{2}
            (TR - T)
            +
            x_{0}
            (1 - R)
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{S}{Q}
        \left(
            T
            x_{1}
            (1 - R + T - 1)
            +
            x_{2}
            (TR - T)
            -
            (1 - R)
            (x_{1} - x_{0})
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{S}{Q}
        \left(
            T
            x_{1}
            (T - R)
            +
            x_{2}
            (TR - T)
            -
            (1 - R)
            (x_{1} - x_{0})
        \right)
    \nonumber
    \\
    & = &
        x_{1}
        +
        \frac{S}{Q}
        \left(
            T
            (x_{2} - x_{1})
            (R - T)
            -
            (1 - R)
            (x_{1} - x_{0})
        \right)
    \nonumber
    \\
    & = &
        x_{1} + \frac{P}{Q}
\end{eqnarray}
$$

ただし、

$$
\begin{eqnarray}
    Q
    & := &
    (R - 1)
    (S - 1)
    (T - 1),
    \nonumber
    \\
    P
    & := &
    S
    (
        T(R - T)(x_{2} - x_{1})
        -
        (1 - R)(x_{1} - x_{0})
    ),
\end{eqnarray}
$$

とおいた。
今、$x_{2} := x_{0}$とおくと

$$
\begin{eqnarray}
    x_{3}^{\mathrm{Q}}
    & := &
    x_{1} + \frac{P}{Q}
    \\
    x_{3}^{\mathrm{B}}
    & := &
    (x_{2} + x_{1}) / 2
    \\
    & = &
    (x_{0} + x_{1}) / 2
\end{eqnarray}
$$

が定義できる。

## Reference
