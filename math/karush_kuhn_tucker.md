---
title: Karush-Kuhn-Tucker Condition
---

## Karush-Kuhn-Tucker Condition
KKT条件は非線形計画問題に対する、最適解の必要条件を与える。
非線形計画問題が良い条件を持てば、十分条件にもなる。

## Defnition

## Theorem
以下の非線形計画問題を考える。

$$
\begin{align}
    \max_{x \in \mathbb{R}^{d}}
    & & &
        f(x)
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        g_{k}(x) \le 0,
        \
        \forall k = 1, \ldots, M
    \nonumber
    \\
    & & &
        h_{k}(x) = 0,
        \
        \forall k = 1, \ldots, L
    \nonumber
\end{align}
$$

ここで、$$f: \mathbb{R}^{d} \rightarrow \mathbb{R}$$, $$g_{k}: \mathbb{R}^{d} \rightarrow \mathbb{R}$$、$$h_{k}: \mathbb{R}^{d} \rightarrow \mathbb{R}$$である。
Lagrange関数最大化の場合は

$$
    L(x, \lambda)
    :=
    f(x)
    - \sum_{k=1}^{M} \lambda_{k} g_{k}(x)
    - \sum_{k=1}^{M} \mu_{k} h_{k}(x)
$$

最小化の場合はk

$$
    L(x, \lambda)
    :=
    f(x)
    + \sum_{k=1}^{M} \lambda_{k} g_{k}(x)
    + \sum_{k=1}^{M} \mu_{k} h_{k}(x)
$$

である。
ここで、$$x^{*} \in \mathbb{R}^{d}$$, $$\lambda^{*} \in \mathbb{R}^{M}$$を最適解とすると、以下を満たす。

$$
\begin{eqnarray}
    \nabla_{x} L(x^{*}, \lambda^{*})
    & = &
        0
    \nonumber
    \\
    \lambda_{k} g_{k}(x)
    & = &
        0,
        \
        \forall k = 1, \ldots, M
    \nonumber
    \\
    g_{k}(x)
    & \le &
        0,
        \
        \forall k = 1, \ldots, M
    \nonumber
    \\
    h_{k}(x)
    & = &
        0,
        \
        \forall k = 1, \ldots, L
    \nonumber
    \\
    \lambda_{k}
    & \ge &
        0,
        \
        \forall k = 1, \ldots, M
    \nonumber
\end{eqnarray}
$$

Wikipediaより。

## proof.

<div class="QED" style="text-align: right">$\Box$</div>


## Theorem
以下の凸計画問題を考える。

$$
\begin{align}
    \max_{x \in \mathbb{R}^{d}}
    & & &
        f(x)
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \forall k = 1, \ldots, M
        \
        g_{k}(x) \ge 0,
    \nonumber
    \\
    & & &
        \forall k = 1, \ldots, L
        \
        h_{k}(x) = 0,
    \nonumber
\end{align}
$$

ここで、$f$, $g_{k}$は凸関数である。
Lagrange関数は

$$
    L(x, \lambda)
    :=
    f(x) + \sum_{k=1}^{M} \lambda_{k} g_{k}(x)
$$

である。
ここで、$$x^{*} \in \mathbb{R}^{d}$$, $$\lambda^{*} \in \mathbb{R}^{M}$$が以下の条件を満たすとき、最適解となる。
また、逆も成り立つ。

$$
\begin{eqnarray}
    \nabla_{x} L(x^{*}, \lambda^{*})
    & = &
        0,
    \nonumber
    \\
    \lambda_{k} g_{k}(x)
    & = &
        0,
        \
        \forall k = 1, \ldots, M
    \nonumber
    \\
    g_{k}(x)
    & \ge &
        0,
        \
        \forall k = 1, \ldots, M
    \nonumber
    \\
    \lambda_{k}
    & \ge &
        0, 
        \
        \forall k = 1, \ldots, M
    \nonumber
\end{eqnarray}
$$

言語処理のための機械学習入門より。

## proof.

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
* [Karush–Kuhn–Tucker conditions - Wikipedia](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions)

