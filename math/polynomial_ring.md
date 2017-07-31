---
title: Polynomial Ring
---

## Notations
* $R$
    * 可換な整域とする

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
    \\
    & = &
        \sum_{i=0}^{\infty}
            \sum_{j=0}^{i}
                (a_{j}b_{i - j})x^{i}
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


## Operations over polynomials
環としての構造を持たない多項式の間にも、和、積、除の演算を考えることができる。
応用上有用である場合もあるので、幾つか記しておく。

### Operation 1
係数が体だとする。

$$
\begin{eqnarray}
    f(x)
    & := &
        \sum_{i=0}^{n}
            a_{i}x^{i}
    \nonumber
    \\
    g(x)
    & := &
        \sum_{i=0}^{m}
            b_{i}x^{i}
    \nonumber
\end{eqnarray}
$$

ここで、$n < m$としておく。
除算を以下で定義する。

$$
\begin{eqnarray}
    \frac{
        f(x)
    }{
        g(x)
    }
    & := &
        h(x)
    \nonumber
    \\
\end{eqnarray}
$$

ここで、$h(x)$は以下を満たす。

$$
\begin{eqnarray}
    h(x)
    & = &
        \sum_{i=0}^{\infty}
            c_{-i}x^{-i}
    \nonumber
    \\
    f(x)
    & = &
        g(x)h(x)
    \nonumber
\end{eqnarray}
$$

両辺の係数を具体的に書き下す。

$$
\begin{eqnarray}
    \sum_{i=0}^{n}
        a_{i}x^{i}
    & = &
        \sum_{i=0}^{m}
            b_{i}x^{i}
        \sum_{i=0}^{\infty}
            c_{-i}x^{-i}
    \nonumber
    \\
    & = &
        b_{m} c_{0} x^{m}
        +
        (b_{m} c_{-1} + b_{m-1} c_{0})
            x^{m-1}
        +
        (b_{m} c_{-2} + b_{m-1} c_{-1} + b_{m}c_{0})
            x^{m-2}
    \nonumber
    \\
    & &
        +
        \cdots
        +
        \sum_{j=0}^{k}
            b_{m-j} c_{k-j}
            x^{m-k}
        +
        \cdots
        +
        \sum_{j=0}^{m}
            b_{m-j} c_{k-j}
            x^{m-m}
    \nonumber
    \\
    & &
        +
        (
            b_{m} c_{-m-1}
            + b_{m-1} c_{-m}
            + b_{m-2}c_{-m+1}
            + \cdots
            + b_{0}c_{-1}
        )
            x^{-1}
        +
        (
            b_{m} c_{-m-2}
            + b_{m-1} c_{-m-1}
            + b_{m-2}c_{-m}
            + \cdots
            + b_{0}c_{-2}
        )
            x^{-2}
    \nonumber
    \\
    & &
        +
        \cdots
        +
        (
            \sum_{j=0}^{m}
                b_{m-j}c_{-(m-j)+k}
        )
            x^{-k}
        +
        \cdots
    \nonumber
    \\
    & = &
        \sum_{i=-m}^{0}
            \sum_{j=0}^{m + i}
                b_{m - j} x^{m - j}
                c_{-i - (m - j)} x^{-i - (m - j)}
        +
        \sum_{i=1}^{\infty}
            \sum_{j=0}^{m}
                b_{j} x^{j}
                c_{-(i + j)} x^{-(i + j)}
    \nonumber
    \\
    & = &
        \sum_{i=-m}^{0}
            \sum_{j=0}^{m + i}
                b_{m - j}
                c_{-i - (m - j)}
                x^{-i}
        +
        \sum_{i=1}^{\infty}
            \sum_{j=0}^{m}
                b_{j}
                c_{-(i + j)}
                x^{-i}
    \nonumber
\end{eqnarray}
$$

両辺の係数を比較すると$n < m$より

$$
\begin{eqnarray}
    (\forall i = -m, \ldots, -(n+1))
    \quad
    0
    & = &
        \sum_{j=0}^{m+i}
            b_{m-j}c_{-i-(m-j)}
    \label{operation01_solution_first_part}
    \\
    (\forall i = -n, \ldots, 0)
    \quad
    a_{-i}
    & = &
        \sum_{j=0}^{m+i}
            b_{m-j}c_{-i-(m-j)}
    \label{operation01_solution_second_part}
    \\
    (\forall i = 1, 2, \ldots)
    \quad
    0
    & = &
        \sum_{j=0}^{m}
            b_{j}c_{-(i+j)}
    \label{operation01_solution_last_part}
\end{eqnarray}
$$

となる。
順番にとくと$x^{n+1}$から$x^{m}$までの係数は全て0である。
よって

$$
\begin{eqnarray}
    0
    & = &
        b_{m}c_{0}
    \nonumber
    \\
    0
    & = &
        b_{m}c_{-1}
        +
        b_{m-1}c_{0}
    \nonumber
    \\
    0
    & = &
        b_{m}c_{-2}
        +
        b_{m-1}c_{-1}
        +
        b_{m-2}c_{0}
    \nonumber
    \\
    & \vdots &
    \nonumber
    \\
    0   
    & = &
        b_{m}c_{-m + n + 1}
        +
        b_{m-1}c_{-m + n}
        +
        \cdots
        +
        b_{n+1}c_{0}
    \nonumber   
\end{eqnarray}
$$

より

$$
\begin{eqnarray}
    c_{0}
    & = &
        0
    \nonumber
    \\
    c_{-1}
    & = &
        0
    \nonumber
    \\
    c_{-2}
    & = &
        0
    \nonumber
    \\
    & \vdots &
    \nonumber
    \\
    c_{-m + n + 1}
    & = &
        0
    \nonumber   
\end{eqnarray}
$$

となる。
同様に

$$
\begin{eqnarray}
    a_{n}
    & = &
        b_{m}c_{-m + n}
        +
        b_{m-1}c_{-m + n + 1}
        +
        \cdots
        +
        b_{n}c_{0}
    \nonumber   
    \\
    a_{n-1}
    & = &
        b_{m}c_{-m + n - 1}
        +
        b_{m-1}c_{-m + n}
        +
        \cdots
        +
        b_{n-1}c_{0}
    \nonumber   
    \\
    a_{n-2}
    & = &
        b_{m}c_{-m + n - 2}
        +
        b_{m-1}c_{-m + n - 1}
        +
        b_{m-2}c_{-m + n}
        +
        \cdots
        +
        b_{n-2}c_{0}
    \nonumber   
    \\
    & \vdots &
    \nonumber   
    \\
    a_{k}
    & = &
        b_{m}c_{-m + k}
        +
        b_{m-1}c_{-m + k + 1}
        +
        b_{m-2}c_{-m + n + 2}
        \cdots
        +
        b_{k}c_{0}
    \nonumber   
    \\
    & \vdots &
    \nonumber   
    \\
    a_{0}
    & = &
        b_{m}c_{-m}
        +
        b_{m-1}c_{-m + 1}
        +
        \cdots
        +
        b_{0}c_{0}
    \nonumber   
\end{eqnarray}
$$

より、

$$
\begin{eqnarray}
    c_{-m + n}
    & = &
        \frac{
            a_{n}
        }{
            b_{m}
        }
    \nonumber   
    \\
    c_{-m + n - 1}
    & = &
        \frac{1}{b_{m}}
        \left(
            a_{n-1}
            -
            b_{m-1}c_{-m + n}
        \right)
    \nonumber   
    \\
    c_{-m + n - 2}
    & = &
        \frac{1}{b_{m}}
        \left(
            a_{n-2}
            -
            b_{m-1}c_{-m + n - 1}
            -
            b_{m-2}c_{-m + n}
        \right)
    \nonumber   
    \\
    & \vdots &
    \nonumber   
    \\
    c_{-m + k}
    & = &
        \frac{1}{b_{m}}
        \left(
            a_{k}
            -
            b_{m-1}c_{-m + k + 1}
            -
            b_{m-2}c_{-m + k + 2}
            \cdots
            -
            b_{k}c_{0}
        \right)
    \nonumber
    \\
    & = &
        \frac{1}{b_{m}}
        \left(
            a_{k}
            -
            \sum_{j=1}^{n - k}
                b_{m-j}
                c_{-m + k + j}
        \right)
    \nonumber   
    \\
    & \vdots &
    \nonumber   
    \\
    c_{-m}
    & = &
        \frac{1}{b_{m}}
        \left(
            a_{0}
            -
            \sum_{j=1}^{n}
                b_{m-j}
                c_{-m + j}
        \right)
    \nonumber   
\end{eqnarray}
$$

となる。
同様に

$$
\begin{eqnarray}
    & &
        0
        =
        \sum_{j=0}^{m}
            b_{j}c_{-(i+j)}
    \nonumber
    \\
    & \Leftrightarrow &
        0
        =
        b_{m}c_{-(i+m)}
        +
        \sum_{j=0}^{m-1}
            b_{j}c_{-(i+j)}
    \nonumber
    \\
    & \Leftrightarrow &
        c_{-(i+m)}
        =
        \frac{-1}{b_{m}}
        \left(
            \sum_{j=0}^{m-1}
                b_{j}c_{-(i+j)}
        \right)
\end{eqnarray}
$$

となる。
これは$i=1$から順にとける。
まとめると

$$
\begin{eqnarray}
    h(x)
    =
    \sum_{i=m-n}^{\infty}
        c_{-i}x^{-i}
    \nonumber
\end{eqnarray}
$$

である。

#### Example 1
具体的な計算例として以下の計算をする。

* $R := \mathbb{F}_{2}$
* $f(x) := 1$
    * $$a_{0} = 1$$,
* $n = 0$
* $g(x) := x + 1$
    * $$b_{1} = b_{0} = 1$$,
* $m = 1$

$$
    \frac{
        1
    }{
        x + 1
    }
    =
    h(x)
$$

を計算する。
順番に解くと、$$\eqref{operation01_solution_first_part}$$から$ i = -1$のとき、

$$
\begin{eqnarray}
    & &
       \sum_{j=0}^{m+i}
          b_{m-j}c_{-i-(m-j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
       \sum_{j=0}^{1-1}
          b_{1-j}c_{1-(1-j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
       \sum_{j=0}^{0}
          b_{1-j}c_{j}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        b_{1}c_{0}
        =
        0
\end{eqnarray}
$$

となって、$c_{0} = 0$である。
$$\eqref{operation01_solution_second_part}$$から$i=0$のとき、

$$
\begin{eqnarray}
    & &
        \sum_{j=0}^{m+i}
            b_{m-j}c_{-i-(m-j)}
        =
        a_{-i}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{1+0}
            b_{1-j}c_{-0-(1-j)}
        =
        a_{0}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{1}
            b_{1-j}c_{-1+j}
        =
        a_{0}
    \nonumber
    \\
    & \Leftrightarrow &
        b_{1}c_{-1}
        +
        b_{0}c_{0}
        =
        a_{0}
    \nonumber
    \\
    & \Leftrightarrow &
        c_{-1}
        +
        c_{0}
        =
        1
\end{eqnarray}
$$

より、$c_{-1} = 1$となる。
$$\eqref{operation01_solution_last_part}$$から$i=1$のとき、

$$
\begin{eqnarray}
    & &
        \sum_{j=0}^{m}
            b_{j}c_{-(i+j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{1}
            b_{j}c_{-(i+j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        b_{0}c_{-i}
        +
        b_{1}c_{-i-1}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        c_{-i}
        +
        c_{-i-1}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        c_{-1}
        +
        c_{-2}
        =
        0
    \nonumber
\end{eqnarray}
$$

となって、$c_{-2} = 1$である。
$i > 1$については、上の式より、

$$
    c_{-i}
    +
    c_{-i-1}
    =
    0
$$

であることが分かるので、$i=1$から順番に説いていけば、$c_{-i} = 1$であることがわかる。
以上を合わせると

$$
    h(x)
    =
    \sum_{i=1}^{\infty}
        x^{-i}
$$

である。
<div class="end-of-statement" style="text-align: right">■</div>

#### Example 2
また、別の例として、

* $R := \mathbb{F}_{2}$
* $f(x) := x$
    * $$a_{0} = 0, a_{1} = 1$$,
* $n = 1$
* $g(x) := x^{2} + x + 1$
    * $$b_{2} = b_{1} = b_{0} = 1$$,
* $m = 2$

$$
    \frac{
        x
    }{
        x^{2} + x + 1
    }
    =
    h(x)
$$

の$h$を計算する。
順番に解くと、$$\eqref{operation01_solution_first_part}$$から$ i = -2$のとき、

$$
\begin{eqnarray}
    & &
       \sum_{j=0}^{m+i}
          b_{m-j}c_{-i-(m-j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
       \sum_{j=0}^{2-2}
          b_{2-j}c_{2-(2-j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
       \sum_{j=0}^{0}
          b_{2-j}c_{j}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        b_{2}c_{0}
        =
        0
    \nonumber
\end{eqnarray}
$$

より、$c_{0} = 0$となる。
$$\eqref{operation01_solution_second_part}$$から

$$
\begin{eqnarray}
    & &
        \sum_{j=0}^{m+i}
            b_{m-j}c_{-i-(m-j)}
        =
        a_{-i}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{2+i}
            b_{2-j}c_{-i-(2-j)}
        =
        a_{-i}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{2+i}
            b_{2-j}c_{-i-2+j}
        =
        a_{-i}
    \nonumber
\end{eqnarray}
$$

$i=-1$とすれば、

$$
\begin{eqnarray}
    & &
        \sum_{j=0}^{2-1}
            b_{2-j}c_{1-2+j}
        =
        a_{1}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{1}
            b_{2-j}c_{-1+j}
        =
        a_{1}
    \nonumber
    \\
    & \Leftrightarrow &
        b_{2}c_{-1}
        +
        b_{1}c_{0}
        =
        a_{1}
    \nonumber
    \\
    & \Leftrightarrow &
        c_{-1}
        =
        a_{1}
    \nonumber
\end{eqnarray}
$$

となって、$c_{-1} = 1$である。
$i = 0$のとき、

$$
\begin{eqnarray}
    & &
        \sum_{j=0}^{2-0}
            b_{2-j}c_{0-2+j}
        =
        a_{0}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{2}
            b_{2-j}c_{-2+j}
        =
        a_{0}
    \nonumber
    \\
    & \Leftrightarrow &
        b_{2}c_{-2}
        +
        b_{1}c_{-1}
        +
        b_{0}c_{0}
        =
        a_{0}
    \nonumber
    \\
    & \Leftrightarrow &
        c_{-2}
        +
        1
        +
        0
        =
        0
    \nonumber
\end{eqnarray}
$$

より、$c_{-2} = 1$である。
$$\eqref{operation01_solution_last_part}$$から

$$
\begin{eqnarray}
    & &
        \sum_{j=0}^{m}
            b_{j}c_{-(i+j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{j=0}^{2}
            b_{j}c_{-(i+j)}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        b_{0}c_{-i-0}
        +
        b_{1}c_{-i-1}
        +
        b_{2}c_{-i-2}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        c_{-i}
        +
        c_{-i-1}
        +
        c_{-i-2}
        =
        0
    \nonumber
\end{eqnarray}
$$

で、$i=1$のとき、

$$
\begin{eqnarray}
    & &
        c_{-1}
        +
        c_{-2}
        +
        c_{-3}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        1
        +
        1
        +
        c_{-3}
        =
        0
\end{eqnarray}
$$

となって、$c_{-3} = 0$となる。
$i=2$のときは、

$$
\begin{eqnarray}
    & &
        c_{-2}
        +
        c_{-3}
        +
        c_{-4}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        1
        +
        0
        +
        c_{-4}
        =
        0
\end{eqnarray}
$$

で、$c_{-4} = 1$となる。
$i=3$のときは、

$$
\begin{eqnarray}
    & &
        c_{-3}
        +
        c_{-4}
        +
        c_{-5}
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        0
        +
        1
        +
        c_{-5}
        =
        0
\end{eqnarray}
$$

で、$c_{-5} = 1$となる。
以上より、$$c_{-3k} = 0, c_{-3k -1} = 1, c_{-3k-2} = 1$$となることがわかる。

$$
    h(x)
    =
    \sum_{k=0}^{\infty}
        \left(
            x^{-3k-1}
            +
            x^{-3k-2}
        \right)
$$

直接解く場合は、

$$
\begin{eqnarray}
    c_{0}
    & = &
        0
    \nonumber
    \\
    c_{-1}
    & = &
        \frac{a_{1}}{b_{2}}
        =
        \frac{1}{1}
    \nonumber
    \\
    c_{-2}
    & = &
        \frac{1}{b_{2}}
        \left(
            a_{0}
            -
            b_{1}c_{-1}
        \right)
        =
        \frac{1}{1}
        (0 - 1)
        =
        1
    \nonumber
    \\
    c_{-3}
    & = &
        \frac{-1}{b_{2}}
        \left(
            \sum_{j=0}^{2-1}
                b_{j}c_{-(i+j)}
        \right)
    \nonumber
    \\
    & = &
        \frac{-1}{1}
        \left(
            \sum_{j=0}^{1}
                b_{j}c_{-(i+j)}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            b_{0}c_{-i}
            +
            b_{1}c_{-i-1}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            c_{-i}
            +
            c_{-i-1}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            c_{-1}
            +
            c_{-2}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            1
            +
            1
        \right)
    \nonumber
    \\
    & = &
        0
    \nonumber
    \\
    c_{-4}
    & = &
        -1
        \left(
            c_{-2}
            +
            c_{-3}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            1
            +
            0
        \right)
    \nonumber
    \\
    & = &
        1
    \nonumber
    \\
        \vdots
    \nonumber
\end{eqnarray}
$$

として解ける。

<div class="end-of-statement" style="text-align: right">■</div>

#### Example 3
また、別の例として、

* $R := \mathbb{F}_{2}$
* $f(x) := x$
    * $$a_{0} = 0, a_{1} = 1$$,
* $n = 1$
* $g(x) := x^{3} + x + 1$
    * $$b_{3} = 1, b_{2} = 0, b_{1} = b_{0} = 1$$,
* $m = 3$

$$
    \frac{
        x
    }{
        x^{2} + x + 1
    }
    =
    h(x)
$$

の$h$を計算する。
直接解く。
まず、$i=0$から$i = -m + n + 1 = -3 + 1 + 1 = -1$までは

$$
\begin{eqnarray}
    c_{0}
    & = &
        0
    \nonumber
    \\
    c_{-1}
    & = &
        0
\end{eqnarray}
$$

である。
$$c_{i}$$について、$i = -m + n = -3 + 1 = -2$から$i=-m$までは、

$$
\begin{eqnarray}
    c_{-m+k}
    & = &
        \frac{1}{b_{m}}
        \left(
            a_{k}
            -
            \sum_{j=1}^{n-k}
                b_{m-j}c_{-m+k+j}
        \right)
\end{eqnarray}
$$

を解けば良いから、

$$
\begin{eqnarray}
    c_{-2}
    & = &
        \frac{1}{b_{3}}
        \left(
            a_{1}
        \right)
    \nonumber
    \\
    & = &
        1
    \nonumber
    \\
    c_{-3}
    & = &
        \frac{1}{b_{3}}
        \left(
            a_{0}
            -
            b_{3-1}c_{-3+0+1}
        \right)
    \nonumber
    \\
    & = &
        \frac{1}{b_{3}}
        \left(
            a_{0}
            -
            b_{2}c_{-2}
        \right)
    \nonumber
    \\
    & = &
        \left(
            0
            -
            0
        \right)
    \nonumber
    \\
    & = &
        0
\end{eqnarray}
$$

となる。
$$c_{i}$$の$i > -m$について、　

$$
\begin{eqnarray}
    c_{-(k+m)}
    & = &
        \frac{-1}{b_{m}}
        \left(
            \sum_{j=0}^{m-1}
                b_{j}c_{-(k+j)}
        \right)
    \nonumber
    \\
    & = &
        \frac{-1}{b_{3}}
        \left(
            \sum_{j=0}^{2}
                b_{j}c_{-(k+j)}
        \right)
    \nonumber
    \\
    & = &
        \frac{-1}{1}
        \left(
            b_{0}c_{-k}
            +
            b_{1}c_{-k-1}
            +
            b_{2}c_{-k-2}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            c_{-k}
            +
            c_{-k-1}
        \right)
\end{eqnarray}
$$

を解けば良いから

$$
\begin{eqnarray}
    c_{-4}
    & = &
        -1
        \left(
            c_{-1}
            +
            c_{-2}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            0
            +
            1
        \right)
    \nonumber
    \\
    & = &
        1
    \nonumber
    \\
    c_{-5}
    & = &
        -1
        \left(
            c_{-2}
            +
            c_{-3}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            1
            +
            0
        \right)
    \nonumber
    \\
    & = &
        1
    \nonumber
    \\
    c_{-6}
    & = &
        -1
        \left(
            c_{-3}
            +
            c_{-4}
        \right)
    \nonumber
    \\
    & = &
        -1
        \left(
            0
            +
            1
        \right)
    \nonumber
    \\
    & = &
        1
    \nonumber
    \\
    c_{-7}
    & = &
        -1
        \left(
            c_{-4}
            +
            c_{-5}
        \right)
    \nonumber
    \\
    & = &
        0
    \nonumber
    \\
    c_{-8}
    & = &
        -1
        \left(
            c_{-5}
            +
            c_{-6}
        \right)
    \nonumber
    \\
    & = &
        0
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Operations 2
?

### Formulas

$$
\begin{eqnarray}
    f(x)
    & = &
        \sum_{i=0}^{n}
            a_{i}x^{i}
    \nonumber
    \\
    f(x)^{2}
    & = &
        \sum_{i=0}^{2n}
            \sum_{j=0}^{i}
                a_{j}a_{i-j}
                x^{i}
    \nonumber
    \\
    f(x)^{3}
    & = &
        \sum_{i=0}^{3n}
            \sum_{j=0}^{i}
                \left(
                    \sum_{k=0}^{j}
                        a_{k}a_{j-k}
                \right)
                a_{i-j}
                x^{i}
    \nonumber
    \\
    & = &
        \sum_{i=0}^{3n}
            \sum_{j=0}^{i}
                \left(
                    a_{i-j}
                    \sum_{k=0}^{j}
                        a_{k}a_{j-k}
                \right)
                x^{i}
\end{eqnarray}
$$

## Reference
* [Formal power series - Wikipedia](https://en.wikipedia.org/wiki/Formal_power_series)


