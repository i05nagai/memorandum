---
title: Chapter2. ベクトルと行列
book_title: regression_analysis
book_chapter: 2
---

## 2. ベクトルと行列

## 2.3 2字形式の標準化

### 2.3.1 固有値とベクトル

#### Proposition
対称行列$A$の$N$個の固有値はすべて実数であり、対応する固有ベクトルもまた実ベクトル

#### proof.
固有値を$\lambda = \alpha + i\beta$とする。
対応する固有ベクトルを$p = a + i b$とする。

$$
\begin{eqnarray}
    & &
        A(u + iv)
        =
        (\alpha + i \beta)(u + iv)
    \nonumber
    \\
    & \Leftrightarrow &
        Au + iAv
        =
        (\alpha u - \beta v)
        +
        i (\alpha v + \beta u)
    \nonumber
\end{eqnarray}
$$

実部と虚部を比較すると、

$$
\begin{eqnarray}
    Au
    & = &
        \alpha u - \beta v
    \nonumber
    \\
    Av
    & = &
        \alpha v + \beta u
    \nonumber
\end{eqnarray}
$$

である。
第一式に$v^{\mathrm{T}}$を左からかけ、第二式に$u^{\mathrm{T}}$を左かける。
$A$が対称なので、$(v^{\mathrm{T}} A u)^{\mathrm{T}} = u^{\mathrm{T}} A v$となって第二式に等しい。
よって、

$$
\begin{eqnarray}
    & &
        v^{\mathrm{T}} \alpha u - v^{\mathrm{T}} \beta v
        =
        u^{\mathrm{T}} \alpha v + u^{\mathrm{T}} \beta u
    \nonumber
    \\
    & \Leftrightarrow &
        \alpha v^{\mathrm{T}} u - \beta v^{\mathrm{T}} v
        =
        \alpha u^{\mathrm{T}}v + \beta u^{\mathrm{T}} u
    \nonumber
    \\
    & \Leftrightarrow &
        - \beta v^{\mathrm{T}} v
        - \beta u^{\mathrm{T}} u
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        \beta (v^{\mathrm{t}} v + \beta u^{\mathrm{t}} u)
        =
        0
    \nonumber
\end{eqnarray}
$$

となる。
$p \neq 0$より、二乗和$$v^{\mathrm{t}} v + \beta u^{\mathrm{t}} u \neq = 0$$.
よって、$\beta = 0$となり、固有値$\lambda$は実数である。
$\beta = 0$より、$v = 0$として、$Ap = \lambda p$を満たす。

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition
正定値対称行列の固有値は全て正であり、半正定値の固有値は全て非負である。

#### proof.
$\lambda$を固有値、対応する固有ベクトルを$x$とする。

$$
\begin{eqnarray}
    & &
        A x
        =
        \lambda x
    \nonumber
    \\
    & \Leftrightarrow &
        x^{\mathrm{T}} A x
        =
        \lambda x^{\mathrm{T}}x
    \nonumber
\end{eqnarray}
$$

$A$は正定値なので、右辺は正である。
$\| x \| \ge 0$より、$\lambda > 0$である。

半正定値の場合も同様に示せる。

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition
対称行列の相異なる固有値$$\lambda_{1} \neq \lambda_{2}$$に対応する固有ベクトル$$x_{1}, x_{2}$$は直交する。

#### proof.
固有値が実数であることの証明と殆ど同じ。
使える条件が、対称性と固有値の式しかないから当たり前か。

$$
\begin{eqnarray}
    & &
        A x_{1}
        =
        \lambda_{1} x_{1}
    \nonumber
    \\
    & \Leftrightarrow &
        x_{2}^{\mathrm{T}} A x_{1}
        =
        \lambda_{1} x_{2}^{\mathrm{T}} x_{1}
    \nonumber
\end{eqnarray}
$$

同様に

$$
\begin{eqnarray}
    & &
        A x_{2}
        =
        \lambda_{2} x_{2}
    \nonumber
    \\
    & \Leftrightarrow &
        x_{1}^{\mathrm{T}} A x_{2}
        =
        \lambda_{2} x_{1}^{\mathrm{T}} x_{2}
    \nonumber
\end{eqnarray}
$$

となる。
左辺を転置すれば、上二式は一致する。
よって、

$$
    \lambda_{1} x_{1}^{\mathrm{T}} x_{2}
    =
    \lambda_{2} x_{1}^{\mathrm{T}} x_{2}
$$

であり、$\lambda_{1} \neq \lambda_{2}$より$x_{1}^{\mathrm{T}} x_{2} = 0$となる。

<div class="QED" style="text-align: right">$\Box$</div>

#### Proposition
$A$が対称行列とする。
このとき、直交行列$P$が存在して、$P^{\mathrm{T}} A P$が対角行列となるようにできる。

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

$A$が対称行列とすると、propositionよりある直交行列が存在して$P^{\mathrm{T}} A P = \Lambda$と対角化できる。
$P = (p_{1}, \ldots, p_{N})$と縦ベクトルで表すと、両辺を変形すれば

$$
\begin{eqnarray}
    A
    & = &
        P \Lambda P^{\mathrm{T}}
    \nonumber
    \\
    & = &
        \sum_{k=1}^{N} 
            \lambda_{k} p^{k} (p^{k})^{\mathrm{T}}
    \nonumber
\end{eqnarray}
$$

とできる。
式変形は、[行列]({{site.baseurl}}/math/matrix_formula.html)にある。
これを行列のスペクトル分解という。

