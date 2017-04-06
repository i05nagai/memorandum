---
title: Ridder Method
---

# ridder method

## Symbol

## Definition

## Problem
$f(x) = 0$を満たす$x \in \mathbb{R}$を見つける問題。

## Algorithm
2点を与える$(x_{0}, f(x_{1}))$, $(x_{1}, f(x_{1}))$とする。
まず、

$$
    g(x) := f(x) e^{(x - x_{0})Q}
$$

とおく。
Ridder methodは$f$ではなく$g$に対するfalse position methodである。
$x_{2} := (x_{1} - x_{0}) / 2$とすると、 $g(x_{0}) = f(x_{0})$, $g(x_{1}) = f(x_{1})e^{(x_{1} - x_{0}) Q}$, $g(x_{2}) = f(x_{2})e^{(x_{1} - x_{0}) Q / 2}$となる。
$Q$は$g(x_{0})$, $g(x_{1})$の線形補間と$g(x_{2})$が等しくなるようにとる。

$$
\begin{eqnarray}
    & &
        g(x_{2})
            =
            \frac{1}{2}
            (g(x_{0}) + g(x_{1}))
    \nonumber
    \\
    & \Leftrightarrow &
        f(x_{2})
        e^{(x_{1} - x_{0}) Q / 2}
        =
        \frac{1}{2}
        (
            f(x_{0})
            +
            f(x_{1})
            e^{(x_{1} - x_{0}) Q}
        )
    \nonumber
    \\
    & \Leftrightarrow &
        f(x_{1})
        e^{(x_{1} - x_{0}) Q}
        -
        2f(x_{2})
        e^{(x_{1} - x_{0}) Q / 2}
        +
        f(x_{0})
        =
        0
\end{eqnarray}
$$

上式は$e^{Q}$についての２次方程式になっている。
これを解くと、

$$
\begin{eqnarray}
    e^{Q}
    & = &
    \frac{
        e^{(x_{1} - x_{0})}
        f(x_{2})
        \pm
        \sqrt{(f(x_{2})e^{(x_{1} - x_{0})})^{2} - e^{(x_{1} - x_{0})}f(x_{1}) f(x_{0}) }
    }{
        f(x_{1})e^{(x_{1} - x_{0})}
    }
    \nonumber
    \\
    & = &
        \frac{
            f(x_{2})
            \pm
            \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
        }{
            f(x_{1})e^{(x_{1} - x_{0})/2}
        }
    \nonumber
\end{eqnarray}
$$

より

$$
\begin{eqnarray}
    e^{(x_{1} - x_{0}) Q / 2}
    & = &
        \frac{
            f(x_{2})
            \pm
            \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
        }{
            f(x_{1})
        }
    \nonumber
\end{eqnarray}
$$

となる。
$(x_{0}, g(x_{0}))$, $(x_{2}, g(x_{2}))$に対してfalse position法を適用する。
つまり、2点の線形補間が$x$軸と交差する点が$x_{3}$となる。

$$
\begin{eqnarray}
    x_{3}
    & := &
        x_{2}
        -
        g(x_{2})
        \frac{
            x_{2}
            -
            x_{0}
        }{
            g(x_{2}) - g(x_{0})
        }
    \nonumber
    \\
    & = &
        x_{2}
        -
        f(x_{2})
        e^{(x_{2} - x_{0}) Q /2}
        \frac{
            x_{2}
            -
            x_{0}
        }{
            f(x_{2})
            e^{(x_{1} - x_{0}) Q / 2}
            -
            f(x_{0})
        }
    \nonumber
    \\
    & = &
        x_{2}
        -
        f(x_{2})
        e^{(x_{2} - x_{0}) Q /2}
        \frac{
            x_{2}
            -
            x_{0}
        }{
            f(x_{2})
            e^{(x_{1} - x_{0}) Q / 2}
            -
            f(x_{0})
        }
    \nonumber
    \\
    & = &
        x_{2}
        -
        f(x_{2})
        \frac{
            f(x_{2})
            \pm
            \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
        }{
            f(x_{1})
        }
        \frac{
            x_{2}
            -
            x_{0}
        }{
            f(x_{2})
            \frac{
                f(x_{2})
                \pm
                \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
            }{
                f(x_{1})
            }
            -
            f(x_{0})
        }
    \nonumber
    \\
    & = &
        x_{2}
        -
        f(x_{2})
        (
            f(x_{2})
            \pm
            \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
        )
        \frac{
            x_{2}
            -
            x_{0}
        }{
            f(x_{2})
            (
                f(x_{2})
                \pm
                \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
            )
            -
            f(x_{0})
            f(x_{1})
        }
        \nonumber
        \\
        & &
        -
        \frac{
            (
                x_{2}
                -
                x_{0}
            )
            f(x_{0})
            f(x_{1})
        }{
            f(x_{2})
            (
                f(x_{2})
                \pm
                \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
            )
            -
            f(x_{0})
            f(x_{1})
        }
        +
        \frac{
            (
                x_{2}
                -
                x_{0}
            )
            f(x_{0})
            f(x_{1})
        }{
            f(x_{2})
            (
                f(x_{2})
                \pm
                \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
            )
            -
            f(x_{0})
            f(x_{1})
        }
    \nonumber
    \\
    & = &
        x_{0}
        +
        \frac{
            (
                x_{2}
                -
                x_{0}
            )
            f(x_{0})
            f(x_{1})
        }{
            f(x_{2})^{2}
            -
            f(x_{0})
            f(x_{1})
            \pm
            f(x_{2})
            \sqrt{f(x_{2})^{2} - f(x_{1}) f(x_{0}) }
        }
\end{eqnarray}
$$


## Reference

