---
title: Gibss Sampler
---

## Gibss Sampler
簡単にいえば、条件付き密度関数から周辺分布を近似する方法。

## Simple two r.v. case
2変数の場合で説明しよう。

* $$(X, Y)$$,
    * r.v.s
* $$f_{X, Y}$$,
    * joint distributino of $X, Y$
* $$f_{X \mid Y}(\cdot \mid y)$$,
    * conditional p.d.f. of $X$ given $Y=y$
* $$f_{Y \mid X}(\cdot \mid x)$$,
    * conditional p.d.f. of $Y$ given $X=x$
* $$f_{X}$$,
    * marginal p.d.f. of $X$
* $$f_{Y}$$,
    * marginal p.d.f. of $Y$

Notationとして、$X$がp.d.f.$$f_{X}$$を持つとき$$X \sim f_{X}$$とかくことにする。
ここで、$$f_{X}$$をconditional p.d.f.で近似する方法を考える。

### Algorithm
$$y_{0}$$を$$Y$$の値域の中から適当に選ぶ。
以下がgivenとなる。

* $$f_{X, Y}$$,
* $$f_{X \mid Y}$$,
* $$f_{Y \mid X}$$,
* $$y_{0}$$,
* $K \in \mathbb{N}$
    * 終了回数

Gibbs samplerは以下の手順で$$f_{X}$$を近似する。

* Step 1. $t = 0$とおく
* Step 2. 

$$
    X_{t} \sim f_{X \mid Y}(\cdot \mid y_{t})
$$

として、$$X_{t}$$のsampleを$$x_{t} := X_{t}(\omega)$$とおく。

* Step3. 

$$
    Y_{t} \sim f_{Y \mid X}(\cdot \mid x_{t})
$$

として、$$Y_{t}$$のsampleを$$y_{t} := Y_{t}(\omega)$$とおく。

* Step4. $t \leftarrow t + 1$として,$t < K$ならばStep2へ

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        f_{X \mid Y}(x \mid Y_{K})
    \right]
    & = &
        \int
            f_{X \mid Y}(x \mid y_{K})
            f_{Y \mid X}(y_{K} \mid X_{K})
        \ d y_{K}
    \nonumber
    \\
    & = &
        \int
        \int
            f_{X \mid Y}(x \mid y_{K})
            f_{Y \mid X}(y_{K} \mid x_{K})
            f_{X \mid Y}(x_{K} \mid Y_{K-1})
        \ dy_{K}
        \ dx_{K}
    \nonumber
    \\
    & = &
        \int
            \left(
                \int
                    f_{X \mid Y}(x \mid y_{K})
                    f_{Y \mid X}(y_{K} \mid x_{K})
                \ dy_{K}
            \right)
            f_{X \mid Y}(x_{K} \mid Y_{K-1})
        \ dx_{K}
    \nonumber
    \\
    & = &
        \int
            K(x, x_{K})
            f_{X \mid Y}(x_{K} \mid Y_{K-1})
        \ dx_{K}
    \nonumber
    \\
    & = &
        \int
            f_{X \mid Y}(x \mid y_{K})
            f_{Y \mid X}(y_{K} \mid x_{K})
            f_{X \mid Y}(x_{K} \mid Y_{K-1})
            \cdots
            f_{Y \mid X}(y_{1} \mid x_{1})
            f_{X \mid Y}(x_{1} \mid y_{0})
        \ dy_{K}
        \ dx_{K}
        \cdots
        \ dy_{1}
        \ dx_{1}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    f_{X}(x)
    & = &
        \int
            f_{X, Y}(x, y)
        \ d y
    \nonumber
    \\
    & = &
        \int
            f_{X \mid Y}(x \mid y)
            f_{Y}(y)
        \ d y
    \nonumber
    \\
    & = &
        \int
            f_{X \mid Y}(x \mid y)
            \left(
                \int
                    f_{X, Y}(x^{\prime}, y)
                \ d x^{\prime}
            \right)
        \ d y
    \nonumber
    \\
    & = &
        \int
            f_{X \mid Y}(x \mid y)
            \left(
                \int
                    f_{Y \mid X}(y \mid x^{\prime})
                    f_{X}(x^{\prime})
                \ d x^{\prime}
            \right)
        \ d y
    \nonumber
    \\
    & = &
        \int
            \left(
                \int
                    f_{X \mid Y}(x \mid y)
                    f_{Y \mid X}(y \mid x^{\prime})
                \ d y
            \right)
            f_{X}(x^{\prime})
        \ d x^{\prime}
    \nonumber
    \\
    & = &
        \int
            K(x, x^{\prime})
            f_{X}(x^{\prime})
        \ d x^{\prime}
    \label{integral_equation}
\end{eqnarray}
$$

ここで、

$$
    K(x, x^{\prime})
    :=
        \int
            f_{X \mid Y}(x \mid y)
            f_{Y \mid X}(y \mid x^{\prime})
        \ d y
$$

とおいた。
上の式変形を考慮して次の線形作用素$$T:L^{p} \rightarrow L^{p}$$を定義する。

$$
\begin{eqnarray}
    f \in L^{p},
    \
    x \in \Omega,
    \quad
    (Tf)(x)
    :=
        \int
            K(x, x^{\prime})
            f(x^{\prime})
        \ d x^{\prime}
\end{eqnarray}
$$

$$g_{0} \in L^{p}$$とする。
再帰的に$$g_{i}$$を定義する。

$$
    i \in \mathbb{N},
    \
    g_{i}(x) := Tg_{i-1}
$$

$$\eqref{integral_equation}$$から$$f_{X}$$は$$g_{i}$$の不動点であることがわかる。

以下では、 $$g_{i}$$が$$f_{X}$$に収束することを示す。
また、$g \in L^{1}$で$g \le 0$のものに限れば、不動点が一意であることを示す。
まず、次が成り立つ。

### Proposition.
$f \in L^{1}$, $f \ge 0$とすると、

$$
    \| Tf \|
    =
    \| f \|
$$

である。
またこれより、$f \in L^{1}$

$$
    \| T |f| \|
    =
    \| f \|
$$

### proof.

$$
\begin{eqnarray}
    \int
        K(x, x^{\prime})
    \ d x
    & = &
        \int
            \int
                f_{X \mid Y}(x \mid y)
                f_{Y \mid X}(y \mid x^{\prime})
            \ d y
        \ d x
    \nonumber
    \\
    & = &
        \int
            f_{Y \mid X}(y \mid x^{\prime})
        \ d y
    \nonumber
    \\
    & = &
        1
    \nonumber
\end{eqnarray}
$$

より、 $f \ge 0$とすると、

$$
\begin{eqnarray}
    \| Tf \|
    & = &
        \int
            \left|
                \int
                     K(x, x^{\prime})
                     f(x^{\prime})
                \ d x^{\prime}
            \right|
        \ d x
    \nonumber
    \\
    & = &
        \int
            \int
                 K(x, x^{\prime})
                 f(x^{\prime})
            \ d x^{\prime}
        \ d x
    \nonumber
    \\
    & = &
        \int
            \int
                 K(x, x^{\prime})
                 f(x^{\prime})
            \ d x
        \ d x^{\prime}
    \nonumber
    \\
    & = &
        \|f\|
\end{eqnarray}
$$

これで、第一式は示した。
$f \in L^{1}$とすると、

$$
    \|T |f| \|
    =
    \| |f| \|
    =
    \| f \|
$$

で第二式もでる。

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition.

$$
\begin{equation}
    \forall i = 0, 1, \ldots,
    \quad
    \|
        g_{i+1} - f_{X} 
    \|
    \le
        \|
            g_{i} - f_{X}
        \|
    \label{inequality_contraction_mapping}
\end{equation}
$$

### proof.
前のpropostionより、$f \ge 0$であれば$$\|Tf \| = \|f \|$$である。
よって$$f, g \in L^{p}$$について$$f \ge g$$とすれば

$$
    T(f - g)
    =
    \int
         K(x, x^{\prime})
         \left(
             f(x^{\prime})
             -
             g(x^{\prime})
         \right)
    \ d x^{\prime}
    \ge
    0
$$

よって、

$$
    Tf \ge Tg
$$

となる。
ここで、

$$
\begin{eqnarray}
    T(g_{i} - f_{X})
    =
    g_{i+1} - f_{X}
\end{eqnarray}
$$

より、

$$
\begin{eqnarray}
    \| g_{i+1} - f_{X} \|
    & = &
        \|T(g_{i} - f_{X}) \|
    \nonumber
    \\
    & \le &
        \| T|g_{i} - f_{X}| \|
    \nonumber
    \\
    & = &
        \| |g_{i} - f_{X}| \|
    \nonumber
    \\
    & = &
        \| g_{i} - f_{X} \|
\end{eqnarray}
$$

となる。
<div class="QED" style="text-align: right">$\Box$</div>

### Condition A
* $K(x, x^{\prime})$がuniformly bounded
* $$\{ K(\cdot, x^{\prime})\}_{x^{\prime} \in A}$$がequicontinuous
* $\forall x_{0} \in A$, $x_{0}$の近傍$\exists U$が存在して、$$\forall x , x^{\prime} \in X$$について、$$K(x ,x^{\prime}) > 0$$

この条件はp.d.f. $$f_{X}$$から定まる$K$が上の性質を持てばということである。

<div class="end-of-statement" style="text-align: right">■</div>


### Lemma 1.
Condition Aのもと、このとき$T$の不動点$f_{X}$は連続で、任意$x$の$f_{X}(x) > 0$である。

### proof.
$$f_{X} \ge 0$$である。
$x_{1}, x \in A$とすると、

$$
\begin{eqnarray}
    | f_{X}(x_{1}) - f_{X}(x) |
    & = &
        \left|
            \int
                K(x_{1}, x^{\prime})
                f_{X}(x^{\prime})
            \ d x^{\prime}
            -
            \int
                K(x, x^{\prime})
                f_{X}(x^{\prime})
            \ d x^{\prime}
        \right|
    \nonumber
    \\
    & = &
        \left|
            \int
                \left(
                    K(x_{1}, x^{\prime})
                    -
                    K(x, x^{\prime})
                \right)
                f_{X}(x^{\prime})
            \ d x^{\prime}
        \right|
    \nonumber
    \\
    & \le &
        \int
            \left|
                K(x_{1}, x^{\prime})
                -
                K(x, x^{\prime})
            \right|
            f_{X}(x^{\prime})
        \ d x^{\prime}
\end{eqnarray}
$$

equicontinuousより、$x_{1} \rightarrow x$のとき、$0$になる。
よって、$f_{X}$は連続。

次に$f_{X}$が正である。

$$
    C
    :=
    \{
        x \in A
        \mid
        f_{X}(x) > 0
    \}
$$

とおく。
$C \neq A$とすると、$f_{X}$の連続性より$$x_{0} \in A$$で$$f_{X}(x_{0}) = 0$$が存在する。
$f_{X}(x_{0}) = 0$と連続性より、$x_{0}$を含む近傍では$f_{X} \neq 0$である。
Condition Aより、$x_{0}$の近傍$U$が存在して

$$
    x, x^{\prime} \in U,
    \
    K(x, x^{\prime}) > 0
$$

である。
$g(x_{0})$は

$$
    0
    =
    f_{X}(x_{0})
    \ge
    \int_{U}
        K(x_{0}, x^{\prime})
        f_{X}(x^{\prime})
    \ d x^{\prime}
    >
    0
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Lemma2.
Condition Aを仮定する。
$f \in L^{1}$とすると、$f^{+}$, $f^{-}$がどちらも恒等的に0でなければ、$$\|Tf \| < \|f\|$$

### proof.
$$
    x
    \in
    \mathrm{supp}(f^{+}),
$$

とすると、$$f^{+}(x) > 0$$である。
また、Condition Aより、$x$の近傍で$$U_{x}$$が存在して、$$y, z \in U_{x}$$で$$K(y, z) > 0$$である。

$$
\begin{eqnarray}
    (Tf^{+})(x)
    & = &
        \int
            K(x, x^{\prime})
            f^{+}(x^{\prime})
        \ d x^{\prime}
    \nonumber
    \\
    & \ge &
        \int_{U}
            K(x, x^{\prime})
            f^{+}(x^{\prime})
        \ d x^{\prime}
    \nonumber
    \\
    & > &
        0
\end{eqnarray}
$$

より、

$$
    \mathrm{supp}(Tf^{+})
    \supsetneq
    \mathrm{supp}(f^{+}),
$$

同様に$A$の連結性とCondition Aより、

$$
    \mathrm{supp}(Tf^{-})
    \supsetneq
    \mathrm{supp}(f^{-})
$$

である。
仮定より$f^{+}$と$f^{-}$はどちらも恒等的に0ではないので、　

$$
\begin{equation}
    C
    :=
    \mathrm{supp}(Tf^{+})
    \cap
    \mathrm{supp}(Tf^{-})
    \neq
    \emptyset
    \label{support_is_not_empty}
\end{equation}
$$

である。

$$
\begin{eqnarray}
    |(Tf)(x)|
    & = &
        | (Tf^{+})(x) - (Tf^{-})(x)|,
    \nonumber
    \\
    (T|f|)(x)
    & = &
        (Tf^{+})(x) + (Tf^{-})(x)
    \nonumber
\end{eqnarray}
$$

であるから、$$\eqref{support_is_not_empty}$$より

$$
\begin{eqnarray}
    \int_{C}
        |(Tf)(x)|
    \ d x
    & < &
        \int_{C}
            (T|f|)(x)
        \ d x
\end{eqnarray}
$$

となる。

$$
\begin{eqnarray}
    \| Tf \|
    & = &
        \int_{C^{c}}
            |(Tf)(x)|
        \ d x
        +
        \int_{C}
            |(Tf)(x)|
        \ d x
    \nonumber
    \\
    & \le &
        \int_{C^{c}}
            (T|f|)(x)
        \ d x
        +
        \int_{C}
            |(Tf)(x)|
        \ d x
    \nonumber
    \\
    & < &
        \int_{C^{c}}
            (T|f|)(x)
        \ d x
        +
        \int_{C}
            (T|f|)(x)
        \ d x
    \nonumber
    \\
    & = &
        \int
            (T|f|)(x)
        \ d x
    \nonumber
    \\
    & = &
        \| T|f| \|
    \nonumber
    \\
    & = &
        \| f \|
\end{eqnarray}
$$


<div class="QED" style="text-align: right">$\Box$</div>

### Corollary
Condition Aを仮定する。
$$\| g_{i} - f_{X} \|$$は$i$について狭義単調減少である。

### proof.

$$
\begin{eqnarray}
    \|g_{i+1} - f_{X} \|
    & = &
        \|T(g_{i} - f_{X}) \|
    \nonumber
\end{eqnarray}
$$

ここで、$$g_{i} \neq f_{X}$$とすると、前定理より

$$
    \|T(g_{i} - f_{X}) \|
    <
    \|(g_{i} - f_{X}) \|
$$

となって、狭義単調減少である。
$$g_{i} = f_{X}$$の場合は、不動点$$f_{X}$$に収束している。

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem 2
Condition Aを仮定する。
$f_{X}$は、$g \in L^{1}$, $g \ge 0$を満たす関数の中で$T$の唯一の不動点である。

### proof.
$g \in L^{1}$を$Tg = g$を満たす別の不動点で、p.d.f., 特に$g \ge 0$とする。
$$h := f_{X} - g$$とおく。
Lemma1より$g$は連続で、$h$も連続である。
更に、

$$
    \int
        h(x)
    \ d x
    =
    0
$$


<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* George, C., & Edward, I. G. (n.d.). Explaining the Gibbs Sampler
    * 概要を理解するのに良い
        * 条件つき分布で周辺分布を求める方法であること
        * 積分方程式の解として求まること
* Tanner, M. A., & Wong, W. H. (1987). The Calculation of Posterior Distributions by Data Augmentation. Source Journal of the American Statistical Association, 82(398), 528–540. Retrieved from http://www.jstor.org/stable/2289457
    * 理論的な証明が書いてある
