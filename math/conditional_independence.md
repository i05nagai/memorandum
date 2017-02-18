---
title: Conditional Independence
---

## Conditional Independence
条件付き独立の定義と性質について記載する。

## Definition

### Symbols
* $(\Omega, \mathcal{F}, P)$
    * 確率空間
* $X, Y, Z$
    * 確率変数
* $X_{1}, \ldots, X_{N}$
    * 確率変数

### By measure
$X, Y$が$Z$の下条件付き独立であるとは、

$$
\begin{equation}
    P(X \cap Y \mid Z)
    =
    P(X \mid Z) P(Y \mid Z)
\end{equation}
$$

が成り立つことを言う。
$N$変数の場合は、$X_{1}, \ldots, X_{N}$が$Z$の下条件付き独立であるとは、


### By Probability density function
確率密度関数を使って以下のようにできる。

$X, Y$が$Z$の下条件付き独立であるとは、

$$
\begin{equation}
    p_{X, Y \mid Z}(x, y \mid z)
    =
    p_{X \mid Z}(x \mid z) p_{Y \mid Z}(y \mid z)
\end{equation}
$$

これは以下と同値である。

$$
\begin{equation}
    p_{X \mid Y, Z}(x\mid y, z)
    =
    p_{X \mid Z}(x \mid z)
\end{equation}
$$

実際

$$
\begin{eqnarray}
    & &
        p_{X, Y \mid Z}(x, y \mid z)
        =
        p_{X \mid Z}(x \mid z) p_{Y \mid Z}(y \mid z)
    \nonumber
    \\
    & \Leftrightarrow &
        \frac{
            p_{X, Y, Z}(x, y, z)
        }{
            p_{Z}(z)
        }
        =
        p_{X \mid Z}(x \mid z)
            \frac{
                p_{Y, Z}(y, z)
            }{
                p_{Z}(z)
            }
    \nonumber
    \\
    & \Leftrightarrow &
        \frac{
            p_{X, Y, Z}(x, y, z)
        }{
            p_{Y, Z}(y, z)
        }
        =
        p_{X \mid Z}(x \mid z)
    \nonumber
    \\
    & \Leftrightarrow &
        p_{X \mid Y, Z}(x \mid y, z)
        =
        p_{X \mid Z}(x \mid z)
    \nonumber
\end{eqnarray}
$$

である。

## Properties
TBD


