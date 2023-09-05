---
title: Matrix formula
---

## Matrix Formula

## Definition
* $N \in \mathbb{N}$
* $M \in \mathbb{N}$
* $A = (a_{j}^{i})_{i,j}$
    * $N \times N$の正方行列
    * $A$の$i$行$j$番目の要素を$a_{j}^{i}$とかく
* $a^{i}$
    * 行列$A$の$i$番目の行ベクトル
* $a_{j}$
    * 行列$A$の$j$番目の列ベクトル
* $\Lambda := \diag (\lambda_{1}, \ldots, \lambda_{N})$
    * $N$行$N$列の対角行列

## Proposition

$$
\begin{equation}
    A A^{\mathrm{T}}
    =
    \sum_{i=1}^{N} 
        a^{k} (a^{k})^{\mathrm{T}}
\end{equation}
$$

行列の積が、列ベクトルの和でかけるよという話。
よく使う。

## proof.
左辺の$i$行$j$列の要素は

$$
    (A A^{\mathrm{T}})_{i}^{j}
    =
    \sum_{k=1}^{N} 
        a_{i}^{k} a_{j}^{k}
$$

とかける。
また、右辺の各$k$について

$$
\begin{equation}
    (a^{k} (a^{k})^{\mathrm{T}})_{i}^{j}
    =
    a_{i}^{k} a_{j}^{k}
    \label{matrix_formula_column_multiply_transposed_column}
\end{equation}
$$

かける。
よって、右辺の和を取れば一致する。

<div class="QED" style="text-align: right">$\Box$</div>

## Proposition

$$
\begin{eqnarray}
    A \Lambda A^{\mathrm{T}}
    = 
    \sum_{k=1}^{N}
        \lambda_{k} a^{k} (a^{k})^{\mathrm{T}}
\end{eqnarray}
$$

行列のスペクトル分解の話。

## proof.
左辺の$i$行$j$列の要素は

$$
    (A \Lambda A^{\mathrm{T}})_{i}^{j}
    = 
    \sum_{l=1}^{N}
        \sum_{k=1}^{N} 
            a_{i}^{k} \lambda_{k}^{l} a_{j}^{l}
$$

とかける。
$\Lambda_{k}^{l}$は$k \neq l$のとき、$\Lambda_{k}^{l} = 0$より

$$
    (A \Lambda A^{\mathrm{T}})_{i}^{j}
    = 
    \sum_{k=1}^{N} 
        a_{i}^{k} \lambda_{k} a_{j}^{k}
$$

となる。
右辺は各$k$について$\eqref{matrix_formula_column_multiply_transposed_column}$でかけるので、成立する。

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition
* $B = (b_{i}^{j})_{i}^{j}$
    * $N \times N$行列
* $C$
    * $N \times N$行列

$C$の$i,j$成分$c_{i}^{j}$が以下でかけるとする。

$$
    c_{i}^{j}
    =
    (a^{i})^{\mathrm{T}}
    B
    a^{j}
$$

このとき、

$$
    C
    =
    A^{\mathrm{T}}
    B
    A
$$

PCAで使う。

### proof.

$$
\begin{eqnarray}
    (A^{\mathrm{T}}B)_{i}^{j}
    & = &
        \sum_{k=1}^{N}
            a_{k}^{i}
                b_{k}^{j},
    \nonumber
    \\
    (A^{\mathrm{T}}BA)_{i}^{j}
    & = &
        \sum_{l=1}^{N}
            \sum_{k=1}^{N}
                a_{k}^{i}
                    b_{k}^{l}
                    a_{l}^{j}
    \nonumber
    \\
    & = &
        (a^{i})^{\mathrm{T}}
        B
        a^{j}
    \nonumber    
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition. Inverse formula for block symmetric matrix
* $A$
    * $m \times m$行列
    * 正則
* $B$
    * $m \times n$行列
* $C$
    * $m \times n$行列
* $D$
    * $n \times n$行列

$S$はSchur's complementで

$$
\begin{equation}
    S
    :=
    C - B^{\mathrm{T}}A^{-1}B
\end{equation}
$$

である。
このとき、$S$が正則であれば、

$$
\begin{eqnarray}
    \left(
        \begin{array}{cc}
            A & B
            \\
            C & D
        \end{array}
    \right)^{-1}
    & = &
        \left(
            \begin{array}{cc}
                A^{-1}
                + 
                A^{-1}BS^{-1}CA^{-1}
                    & 
                        -A^{-1}BS^{-1}
                \\
                -S^{-1}CA^{-1}
                    &
                        S^{-1}
            \end{array}
        \right)
    \\
    \left(
        \begin{array}{cc}
            D & C
            \\
            B & A
        \end{array}
    \right)^{-1}
    & = &
        \left(
            \begin{array}{cc}
                S^{-1}
                    & 
                    -S^{-1} C A^{-1}
                \\
                -A^{-1}BS^{-1}
                    &
                        A^{-1}
                        + 
                        A^{-1}BS^{-1}CA^{-1}
            \end{array}
        \right)
\end{eqnarray}
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>
