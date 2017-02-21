---
title: Support Vector Machine
---

## Support Vector Machine
超平面でクラスを2値分類する方法。
様々な拡張が存在する。

## Good

## Bad

## Defnition
* $N$
    * データの個数
* $(x_{1}, y_{1}), \ldots, (x_{N}, y_{N})$
    * データ
    * $x_{i}$が説明変数
    * $y_{1}$は-1, 1に値を取るカテゴリ

## Preliminary
$$\mathbb{R}^{d}$$上の超平面について考える。
$\beta \in \mathbb{R}^{d}$, $\beta_{0} \in \mathbb{R}$とする。
$\beta$, $\beta_{0}$のなす超平面を以下で定義する。

$$
    H(\beta_{0}, \beta) := \{ x \in \mathbb{R}^{d} \mid \beta^{\mathrm{T}}x + \beta_{0} = 0\}
$$

$\beta$は傾き、$\beta_{0}$は切片に対応する。

$H(\beta_{0}, \beta)$について以下が成り立つ。

$$
    \forall x \in H(\beta_{0}, \beta),
    \quad
    \beta^{\mathrm{T}} x = - \beta_{0}
$$

### Proposition1
$x \in \mathbb{R}^{d}$と超平面との距離は以下で与えられる。

$$
\begin{equation}
    \frac{
        f(x)
    }{
        \| f^{\prime}(x) \|
    }
    \label{svm_distance_between_point_and_hyper_plane}
\end{equation}
$$

但し、$f(x) := \beta^{\mathrm{T}} x + \beta_{0}$, $$\beta^{*} := \beta / \| \beta \|$$である。
上記の距離は、法線ベクトルと2点間の方向ベクトルが一致しない場合は、負になることに注意する。

### proof
超平面と点との距離は単位法線ベクトルと超平面上の点と対象の点との差の内積で与えられる。
つまり、$x_{0} \in H(\beta_{0}, \beta)$とすると、

$$
\begin{eqnarray}
    (\beta^{*})^{\mathrm{T}}
        (x - x_{0})
    & = &
        \frac{1}{\| \beta \|}
            (\beta^{\mathrm{T}} x + \beta_{0})
    \nonumber
    \\
    & = &
        \frac{1}{\| f^{\prime}(x) \|}
            f(x)
    \nonumber
\end{eqnarray}
$$

## Algorithm
Support Vector Machineでは、超平面とデータ$$x_{1}, \ldots, x_{N}$$の距離が最大になるようにデータを分類する。
$\eqref{svm_distance_between_point_and_hyper_plane}$より、法線ベクトルの向きに応じて距離は正負の値を取るので、$$y_{i} \frac{f(x_{i})}{\| \beta \|}$$が距離の絶対値となるように、超平面で分類すれば良い。

$$
\begin{align}
    \max_{\beta_{0} \in \mathbb{R}, \beta \in \mathbb{R}^{d}}
    & & &
        M
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        y_{i} \frac{\beta^{\mathrm{T}} x_{i} + \beta_{0}}{\| \beta \|} \ge M,
        \quad
        \forall i = 1, \ldots, N
    \nonumber,
\end{align}
$$

$\beta$は自由にとれるので、$\| \beta \| = 1 / M$を満たすように取ると

$$
\begin{align}
    \max_{\beta_{0} \in \mathbb{R}, \beta \in \mathbb{R}^{d}}
    & & &
        \frac{1}{\| \beta \|^{2}}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        y_{i} (\beta^{\mathrm{T}}x_{i} + \beta_{0}) \ge 1,
        \quad
        \forall i = 1, \ldots, N
    \nonumber,
\end{align}
$$

これは以下と等価である。

$$
\begin{align}
    \min_{\beta_{0} \in \mathbb{R}, \beta \in \mathbb{R}^{d}}
    & & &
        \frac{1}{2}
            \| \beta \|^{2}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        y_{i} (\beta^{\mathrm{T}}x_{i} + \beta_{0}) \ge 1,
        \quad
        \forall i = 1, \ldots, N
    \nonumber,
\end{align}
$$

Lagrangeの未定乗数法より、双対問題を考える。
Lagrange定数を$$\lambda_{1}, \ldots, \lambda_{N}$$と置く。

$$
    L(\lambda, \beta, \beta_{0})
    :=
    \frac{1}{2} \| \beta \|^{2}
    -
    \sum_{i=1}^{N}
        \lambda_{i}
            \left(
                y_{i} 
                (
                    \beta^{\mathrm{T}} x_{i} + \beta_{0}
                )
                -
                1
            \right)
$$

偏微分を$0$とおくと、

$$
    
$$

## Reference

