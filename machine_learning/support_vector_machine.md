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
* $\beta := (\beta^{1}, \ldots, \beta^{d})^{\mathrm{T}} \in \mathbb{R}^{d}$,
* $\beta_{0} \in \mathbb{R}$,
* $f(x; \beta, \beta_{0}) := \beta^{\mathrm{T}}x + \beta_{0}$,
    * 傾き$\beta$、切片$\beta_{0}$の超平面

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
        \beta^{\mathrm{T}} x + \beta_{0}
    }{
        \| \beta \|
    }
    =
    \frac{
        f(x; \beta, \beta_{0})
    }{
        \| f^{\prime}(x; \beta, \beta_{0}) \|
    }
    \label{svm_distance_between_point_and_hyper_plane}
\end{equation}
$$

但し、$$\beta^{*} := \beta / \| \beta \|$$である。
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
        \frac{1}{\| f^{\prime}(x; \beta, \beta_{0}) \|}
            f(x; \beta, \beta_{0})
    \nonumber
\end{eqnarray}
$$

## Algorithm
Support Vector Machineでは、超平面とデータ$$x_{1}, \ldots, x_{N}$$の距離が最大になるようにデータを分類する。
$\eqref{svm_distance_between_point_and_hyper_plane}$より、法線ベクトルの向きに応じて距離は正負の値を取るので、$$y_{i} \frac{f(x_{i}; \beta, \beta_{0})}{\| \beta \|}$$が距離の絶対値となるように、超平面で分類すれば良い。

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

$\beta$は自由にとれるので、$$\| \beta \| = \bar{\beta} / M$$として、$\bar{\beta}$について最大化しても同じである。
$\bar{\beta}$を改めて、$\beta$とおけば

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

となる。
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

このままでは、データが線形分離可能でない場合は解が求まらない。
よって、分離面に調整幅を持たせる。

$$
\begin{align}
    \min_{\beta_{0} \in \mathbb{R}, \beta \in \mathbb{R}^{d}}
    & & &
        \frac{1}{2}
            \| \beta \|^{2}
        +
        C
        \sum_{i=1}^{N} \xi_{i}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        y_{i} (\beta^{\mathrm{T}}x_{i} + \beta_{0}) \ge 1 - \xi_{i},
        \quad
        \forall i = 1, \ldots, N
    \nonumber,
    \\
    & & &
        \xi_{i} \ge 0
        \quad
        \forall i = 1, \ldots, N
    \nonumber,
\end{align}
$$

$C$は線形分離が可能であれば大きい値を、線形分離不可能であれば$C$を小さい値に設定する。
データが線形分離可能なとき、$C := \infty$とすればこれは元の問題と等価となる。

Lagrangeの未定乗数法より、双対問題を考える。
Lagrange定数を$$\lambda_{1}, \ldots, \lambda_{N}, \mu_{1}, \ldots, \mu_{N}$$と置く。

$$
\begin{equation}
    L(\beta, \beta_{0}, \xi, \lambda, \mu)
    :=
    \frac{1}{2} \| \beta \|^{2}
    +
    C
    \sum_{i=1}^{N}
    \xi_{i}
    -
    \sum_{i=1}^{N}
        \lambda_{i}
            \left(
                y_{i} 
                (
                    \beta^{\mathrm{T}} x_{i} + \beta_{0}
                )
                -
                (1 - \xi_{i})
            \right)
    -
    \sum_{i=1}^{N}
        \mu_{i}\xi_{i}
    \label{SVM_lagrange_objective_function}
\end{equation}
$$

最小化する変数に対する偏微分を求めると以下のようになる。　

$$
\begin{eqnarray}
    \frac{\partial L(\beta, \beta_{0}, \xi, \lambda, \mu)}{\partial \beta^{k}}
    & = &
        \beta^{k}
        -
        \sum_{i=1}^{N}
            \lambda_{i}
            y_{i} x_{i}^{k}
        \quad
        \forall k = 1, \ldots, d,
    \nonumber
    \\
    \frac{\partial L(\beta, \beta_{0}, \xi, \lambda, \mu)}{\partial \beta_{0}}
    & = &
        \sum_{i=1}^{N}
            \lambda_{i} y_{i}
    \nonumber
    \\
    \frac{\partial L(\beta, \beta_{0}, \xi, \lambda, \mu)}{\partial \xi_{k}}
    & = &
        C
        -\lambda_{k}
        - \mu_{k}
        \quad
        \forall k = 1, \ldots, N,
    \nonumber
\end{eqnarray}
$$

偏微分を0とおけば

$$
\begin{eqnarray}
    \beta^{k}
    & = &
        \sum_{i=1}^{N}
            \lambda_{i}
            y_{i} x_{i}^{k}
        \quad
        \forall k = 1, \ldots, d,
    \label{SVM_KKT_condition_derivative_with_respect_to_beta}
    \\
    \sum_{i=1}^{N}
        \lambda_{i} y_{i}
    & = &
        0
    \label{SVM_KKT_condition_derivative_with_respect_to_beta0}
    \\
    \lambda_{k}
    & = &
        C
        - \mu_{k},
        \quad
        \forall k = 1, \ldots, N,
    \label{SVM_KKT_condition_derivative_with_respect_to_xi}
\end{eqnarray}
$$

また、KKT条件より以下を満たす必要がある。

$$
\begin{eqnarray}
    \lambda_{i}
    \left(
        y_{i}(\beta^{\mathrm{T}}x_{i} + \beta_{0})
            - (1 - \xi_{i})
    \right)
    & = &
        0
        \quad
        \forall i = 1, \ldots, N
    \\
    \mu_{i}
    \xi_{i}
    & = &
        0
        \quad
        \forall i = 1, \ldots, N
    \\
    y_{i}(\beta^{\mathrm{T}}x_{i} + \beta_{0})
    & \ge &
        1 - \xi_{i}
        \quad
        \forall i = 1, \ldots, N
    \\
    \xi_{i}
    & \ge &
        0
        \quad
        \forall i = 1, \ldots, N
    \\
    \lambda_{i}
    & \ge &
        0
        \quad
        \forall i = 1, \ldots, N
    \\
    \mu_{i}
    & \ge &
        0
        \quad
        \forall i = 1, \ldots, N
\end{eqnarray}
$$

以上を$$\eqref{SVM_lagrange_objective_function}$$に代入する。
以下の式変形に注意する。
$$\eqref{SVM_lagrange_objective_function}$$の第一項について

$$
\begin{eqnarray}
    \| \beta \|
    & = &
        \sum_{k=1}^{N}
            \sum_{i=1}^{N}
                \sum_{j=1}^{N}
                    \lambda_{i} \lambda_{j}
                    y_{i} y_{j}
                    x_{i}^{k} x_{j}^{k}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                \lambda_{i} \lambda_{j}
                y_{i} y_{j}
                \sum_{k=1}^{N}
                    x_{i}^{k} x_{j}^{k}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                \lambda_{i} \lambda_{j}
                y_{i} y_{j}
                x_{i}^{\mathrm{T}} x_{j}^{\mathrm{T}}
\end{eqnarray}
$$

である。
$$\eqref{SVM_lagrange_objective_function}$$の第2項、第4項について

$$
\begin{eqnarray}
    C \sum_{i=1}^{N}
        \xi_{i}
    -
    \sum_{i=1}^{N}
        \mu_{i}xi_{i}
    & = &
        \sum_{i=1}^{N}
            \xi_{i}
            (C - \mu_{i})
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \xi_{i}
            \lambda_{i}
\end{eqnarray}
$$

$$\eqref{SVM_lagrange_objective_function}$$の第3項について

$$
\begin{eqnarray}
    \sum_{i=1}^{N}
        \lambda_{i}
            \left(
                y_{i} 
                (
                    \beta^{\mathrm{T}} x_{i} + \beta_{0}
                )
                -
                (1 - \xi_{i})
            \right)
    & = &
        \sum_{i=1}^{N}
            \lambda_{i}
            y_{i} 
            \left(
                \beta^{\mathrm{T}} x_{i}
            \right)
        +
        \sum_{i=1}^{N}
            \lambda_{i}
            y_{i} 
            \left(
                \beta_{0}
            \right)
        -
        \sum_{i=1}^{N}
            \lambda_{i}
        +
        \sum_{i=1}^{N}
            \lambda_{i}
            \xi_{i}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \lambda_{i}
            y_{i} 
            \sum_{j=1}^{N}
                \left(
                    \lambda_{j}
                    y_{j} 
                    x_{j}^{\mathrm{T}}
                \right)
            x_{i}
        -
        \sum_{i=1}^{N}
            \lambda_{i}
        +
        \sum_{i=1}^{N}
            \lambda_{i}
            \xi_{i}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                \lambda_{i}
                \lambda_{j}
                y_{i} 
                y_{j} 
                x_{i}^{\mathrm{T}}
                x_{j}
        -
        \sum_{i=1}^{N}
            \lambda_{i}
        +
        \sum_{i=1}^{N}
            \lambda_{i}
            \xi_{i}
\end{eqnarray}
$$

二つ目の等号は、$$\eqref{SVM_KKT_condition_derivative_with_respect_to_beta}$$, $$\eqref{SVM_KKT_condition_derivative_with_respect_to_beta0}$$による。
以上をあわせると、$$\eqref{SVM_lagrange_objective_function}$$は

$$
\begin{eqnarray}
    L(\beta, \beta_{0}, \xi, \lambda, \mu)
    & = &
        \frac{1}{2}
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                \lambda_{i} \lambda_{j}
                y_{i} y_{j}
                x_{i}^{\mathrm{T}} x_{j}^{\mathrm{T}}
        -
        \left(
            \sum_{i=1}^{N}
                \sum_{j=1}^{N}
                    \lambda_{i}
                    \lambda_{j}
                    y_{i} 
                    y_{j} 
                    x_{i}^{\mathrm{T}}
                    x_{j}
            -
            \sum_{i=1}^{N}
                \lambda_{i}
            +
            \sum_{i=1}^{N}
                \lambda_{i}
                \xi_{i}
        \right)
        +
        \sum_{i=1}^{N}
            \xi_{i}
            \lambda_{i}
    \nonumber
    \\
    & = &
        -
        \frac{1}{2}
        \sum_{i=1}^{N}
            \sum_{j=1}^{N}
                \lambda_{i} \lambda_{j}
                y_{i} y_{j}
                x_{i}^{\mathrm{T}} x_{j}^{\mathrm{T}}
            +
            \sum_{i=1}^{N}
                \lambda_{i}
\end{eqnarray}
$$

とかける。


## Reference

