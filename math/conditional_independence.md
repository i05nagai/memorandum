---
title: Conditional Independence
---

## Conditional Independence
条件付き独立の定義と性質について記載する。

## Definition

#### Definition 1 in measure theory
* $(\Omega, \mathcal{F}, P)$
    * probability sp.
* $X, Y, Z$
    * r.v.
* $X_{1}, \ldots, X_{N}$
    * r.v.

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

$$
    \forall n = 2, \ldots, N,
    \quad
    0 \le \forall i_{1} \le \ldots \le \forall i_{n} \le N,
    \quad
    P(X_{i_{1}} \cap \cdots \cap X_{i_{n}} \mid Z)
    =
    P(X_{i_{1}} \mid Z) \cdots P(X_{i_{n}} \mid Z)
$$

を満たすことを言う。

<div class="end-of-statement" style="text-align: right">■</div>

たまに、

$$
    P(X_{1} \cap \cdots \cap X_{N} \mid Z)
    =
    P(X_{1} \mid Z) \cdots P(X_{N} \mid Z)
$$

という文献もある。
どっちが正しい？
Bayes推定の議論が成り立つのはどっちだろ？

#### Definition 2 with probability density function
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

<div class="end-of-statement" style="text-align: right">■</div>

## Properties
TBD


