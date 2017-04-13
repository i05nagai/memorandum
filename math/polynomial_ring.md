---
title: Polynomial Ring
---

## Formal Polynomial Ring

$$
    R[[x]]
    :=
    \left\{
        \sum_{i=0}^{\infty}
            a_{i}x^{i}
        \mid
        a_{i} \in R
    \right\}
$$

$R[[x]]$に以下の和と積の演算を与えたものをFormal Polynomial Ringという。
$\sum_{i=0}^{\infty} a_{i}x^{i}$は$$\mathbb{R}^{\mathbb{N}}$$の元を級数の形に表現しているに過ぎない。
その意味でFormal series（形式的べき級数）という。
$f, g \in R[[x]]$について、

$$
\begin{eqnarray}
    f(x)
    & = & 
        \sum_{i=0}^{\infty}
            a_{i}x^{i}
    \nonumber
    \\
    g(x)
    & = &
        \sum_{i=0}^{\infty}
            b_{i}x^{i}
    \nonumber
\end{eqnarray}
$$

とする。

$$
\begin{eqnarray}
    f(x) + g(x)
    & := &
        \sum_{i=0}^{\infty}
            (a_{i} + b_{i})x^{i}
    \nonumber
    \\
    f(x)g(x)
    & := &
        \sum_{i=0}^{\infty}
            \sum_{j + k = i}
                (a_{j}b_{k})x^{i}
    \nonumber
\end{eqnarray}
$$

更に以下のように商を定義することもできる。
Formal Polynomial Ringに以下の商を与えたものは、Formal Polynomial Ringの分数体になる。

$$
\begin{eqnarray}
    \frac{f(x)}{g(x)}
    & := &
        h(x)
    \nonumber
\end{eqnarray}
$$

ここで、$h \in R[[x]]$は以下を満たす。

$$
\begin{eqnarray}
    h(x)
    & = & 
        \sum_{i=0}^{\infty}
            c_{i}x^{i}
    \nonumber
    \\
    f(x)
    & = &
        g(x)h(x)
    \nonumber
    \\
    \sum_{i=0}^{\infty}
        a_{i}x^{i}
    & = &
        \sum_{i=0}^{\infty}
            \sum_{j + k = i}
                (b_{j}c_{k})x^{i}
    \nonumber
\end{eqnarray}
$$

最初の数項を書き下すと、

$$
\begin{eqnarray}
    a_{0}
    & = &
        b_{0}c_{0}
    \nonumber
    \\
    a_{1}
    & = &
        b_{0}c_{1}
        +
        b_{1}c_{0}
    \nonumber
    \\
    a_{2}
    & = &
        b_{0}c_{2}
        +
        b_{1}c_{1}
        +
        b_{2}c_{0}
    \nonumber
    \\
    & \vdots &
    \nonumber
\end{eqnarray}
$$

上から順番にとくと

$$
\begin{eqnarray}
    c_{0}
    & = &
        \frac{a_{0}}{b_{0}}
    \nonumber
    \\
    c_{1}
    & = &
        \frac{1}{b_{0}}
        \left(
            a_{1}
            -
            b_{1}c_{0}
        \right)
    \nonumber
    \\
    c_{2}
    & = &
        \frac{1}{b_{0}}
        \left(
            a_{2}
            -
            b_{1}c_{1}
            -
            b_{2}c_{0}
        \right)
    \nonumber
    \\
    \nonumber
    \\
    & = &
        \frac{1}{b_{0}}
        \left(
            a_{2}
            -
            \sum_{i=1}^{2}
            b_{i}c_{2-i}
        \right)
    \nonumber
    \\
    & \vdots &
    \nonumber
    \\
    c_{n}
    & = &
        \frac{1}{b_{0}}
        \left(
            a_{n}
            -
            \sum_{i=1}^{n}
            b_{i}c_{n-i}
        \right)
    \nonumber
\end{eqnarray}
$$

## Ring of Formal Laurent series

$$
    R((x))
    :=
    \left\{
        \sum_{i=w}^{\infty}
            a_{i}x^{i}
        \mid
        w \in \mathbb{Z},
        \
        a_{i} \in R
    \right\}
$$

とする。
$R((x))$に以下の和と積の演算を付与したものをRing of Formal Laurent Seriesと呼ぶ。
$f, g \in R((x))$について

$$
\begin{eqnarray}
    f(x)
    & = & 
        \sum_{i=w_{f}}^{\infty}
            a_{i}x^{i}
    \nonumber
    \\
    g(x)
    & = &
        \sum_{i=w_{g}}^{\infty}
            b_{i}x^{i}
    \nonumber
\end{eqnarray}
$$

とする。

$$
\begin{eqnarray}
    f(x) + g(x)
    & := &
        \sum_{i=\min(w_{f}, w_{g})}^{\infty}
            (a_{i} + b_{i})x^{i}
    \nonumber
    \\
    f(x)g(x)
    & := &
        \sum_{i=w_{f} + w_{g}}^{\infty}
            \sum_{j=w_{f} + w_{g}}^{i}
                (a_{j - w_{g}}b_{i - j + w_{g}})x^{i}
    \nonumber
    \\
    & = &
        \sum_{i=w_{f} + w_{g}}^{\infty}
            \sum_{j=0}^{i - w_{f} - w_{g}}
                (a_{w_{f} + j}b_{w_{g} + i - j})x^{i}
    \nonumber
\end{eqnarray}
$$

但し、和の定義において$$w_{f} \le w_{g}$$ならば

$$
\begin{eqnarray}
    \forall i = w_{f}, w_{f} + 1, \ldots, w_{g},
    \quad
    b_{i}
    & = & 
        0
    \nonumber
\end{eqnarray}
$$

であり、$$w_{f} > w_{g}$$ならば

$$
\begin{eqnarray}
    \forall i = w_{g}, w_{g} + 1, \ldots, w_{f},
    \quad
    a_{i}
    & = & 
        0
    \nonumber
\end{eqnarray}
$$

としておく。
更に以下のように商を定義することもできる。
Ring of Formal Laurent Serriesに以下の商を与えたものは、Ring of Formal Laurent Seriesの分数体になる。

$$
\begin{eqnarray}
    \frac{f(x)}{g(x)}
    & := &
        h(x)
    \nonumber
\end{eqnarray}
$$

ここで、$h \in R((x))$は以下を満たす。

$$
\begin{eqnarray}
    h(x)
    & = & 
        \sum_{i=w_{h}}^{\infty}
            c_{i}x^{i}
    \nonumber
    \\
    f(x)
    & = &
        g(x)h(x)
    \nonumber
    \\
    \sum_{i=w_{f}}^{\infty}
        a_{i}x^{i}
    & = &
        \sum_{i=w_{g} + w_{h}}^{\infty}
            \sum_{j = w_{g} + w_{h}}^{i}
                (b_{i - w_{g}}c_{i - j + w_{g}})x^{i}
    \nonumber
\end{eqnarray}
$$

上の式から$$w_{h} = w_{f} - w_{g}$$である。
最初の数項を書き下すと、

$$
\begin{eqnarray}
    a_{w_{f}}
    & = &
        b_{w_{g}}c_{w_{h}}
    \nonumber
    \\
    a_{w_{f} + 1}
    & = &
        b_{w_{g}}c_{w_{h} + 1}
        +
        b_{w_{g} + 1}c_{w_{h}}
    \nonumber
    \\
    a_{w_{f} + 2}
    & = &
        b_{w_{g}}c_{w_{h} + 2}
        +
        b_{w_{g} + 1}c_{w_{h} + 1}
        +
        b_{w_{g} + 2}c_{w_{h}}
    \nonumber
    \\
    & \vdots &
    \nonumber
\end{eqnarray}
$$

上から順番にとくと

$$
\begin{eqnarray}
    c_{w_{h}}
    & = &
        \frac{a_{w_{f}}}{b_{w_{f}}}
    \nonumber
    \\
    c_{w_{h} + 1}
    & = &
        \frac{1}{b_{w_{g}}}
        \left(
            a_{w_{f} + 1}
            -
            b_{w_{g} + 1}c_{w_{h}}
        \right)
    \nonumber
    \\
    c_{w_{h} + 2}
    & = &
        \frac{1}{b_{w_{g}}}
        \left(
            a_{w_{f} + 2}
            -
            b_{w_{g} + 1}c_{w_{h} + 1}
            -
            b_{w_{g} + 2}c_{w_{h}}
        \right)
    \nonumber
    \\
    & = &
        \frac{1}{b_{w_{g}}}
        \left(
            a_{w_{f} + 2}
            -
            \sum_{j=1}^{2}
                b_{w_{g} + j}c_{w_{h} + 2 - i}
        \right)
    \nonumber
    \\
    & \vdots &
    \nonumber
    \\
    c_{n}
    & = &
        \frac{1}{b_{w_{g}}}
        \left(
            a_{n}
            -
            \sum_{j=1}^{n}
                b_{w_{g} + j}c_{w_{h} + n - i}
        \right)
    \nonumber
\end{eqnarray}
$$


## Reference
* [Formal power series - Wikipedia](https://en.wikipedia.org/wiki/Formal_power_series)


