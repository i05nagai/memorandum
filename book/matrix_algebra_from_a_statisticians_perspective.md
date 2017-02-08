---
layout: slate_page
title: Matrix Algebra from a Statisticians perspective
---

## Overviews

## Symbols
* $\mathcal{R}(A)$
    * 行列$A$の行ベクトルの貼る線形空間
* $\mathcal{C}(A)$
    * 行列$A$の列ベクトルの貼る線形空間
* $\mathcal{R} \left(
        \begin{array}{c}
            A \\
            B
        \end{array}
    \right)$
    * $ \left(
        \begin{array}{c}
            A \\
            B
        \end{array}
    \right)$のブロック行列の行ベクトルの貼る線形空間
* $\mathcal{C}(A, B)$
    * $(A, B)$のブロック行列の列ベクトルの貼る線形空間

## Chapter 4 

### 4.4

#### Theorem 4.4.3

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### 4.5

#### Theorem 4.5.7

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>


## Chapter 8 逆行列

### 8.3

#### Corollary 8.3.3

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### 8.5

#### Theorem 8.5.1

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 8.5.2

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 8.5.3

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### 定理 8.5.4
* $T$: $m \times m$行列
* $V$: $n \times m$行列
* $W$: $n \times n$行列

このとき、$(m + n) \times (m + n)$分割行列

$$
    \left(
        \begin{array}{cc}
            T & 0 \\
            V & W
        \end{array}
    \right),
    \quad
    \left(
        \begin{array}{cc}
            W & V \\
            0 & T 
        \end{array}
    \right),
$$

が正則であること、$T, W$が正則であることは同値。
またこのとき、

$$
\begin{eqnarray}
    \left(
        \begin{array}{cc}
            T & 0 \\
            V & W
        \end{array}
    \right)
    & = &
        \left(
            \begin{array}{cc}
                T^{-1}         & 0 \\
                -W^{-1}VT^{-1} & W^{-1}
            \end{array}
        \right),
    \label{5_8a}
        \\
    \left(
        \begin{array}{cc}
            W & V \\
            0 & T 
        \end{array}
    \right)
    & = &
        \left(
            \begin{array}{cc}
                W^{-1} & -W^{-1}VT^{-1} \\
                0      & T^{-1}
            \end{array}
        \right)
    \label{5_8b}
\end{eqnarray}
$$

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### 定理 8.5.10
* $T$: $m \times m$行列
* $U$: $m \times q$行列
* $V$: $n \times m$行列
* $W$: $n \times q$行列
* $\mathrm{rank}(T) = m$、つまりT$は正則

このとき、

$$
\begin{eqnarray}
    \mathrm{rank}
    \left(
        \begin{array}{cc}
            T & U \\
            V & W
        \end{array}
    \right)
    & = &
        \mathrm{rank}
        \left(
            \begin{array}{cc}
                U & T \\
                W & V 
            \end{array}
        \right)
        \nonumber
        \\
    & = &
        \mathrm{rank}
        \left(
            \begin{array}{cc}
                V & W \\
                T & U 
            \end{array}
        \right)
        \nonumber
        \\
    & = &
        \mathrm{rank}
        \left(
            \begin{array}{cc}
                W & V \\
                U & T 
            \end{array}
        \right)
        \nonumber
        \\
    & = &
        m + \mathrm{rank}(W - VT^{-1}U)
\end{eqnarray}
$$

#### proof.

<div class="QED" style="text-align: right">$\Box$</div>

#### Theorem 8.5.11
* $T$: $m \times m$行列
* $U$: $m \times n$行列
* $V$: $n \times m$行列
* $T$は正則

このとき、

$$
    Q := W - VT^{-1}U
$$

が正則であることと

$$
    \left(
        \begin{array}{cc}
            T & U \\
            V & W
        \end{array}
    \right)
$$

が正則であることは同値。
更に、このとき

$$
\begin{eqnarray}
    A_{1} := 
    \left(
        \begin{array}{cc}
            T & U \\
            V & W
        \end{array}
    \right)^{-1}
        & = &
        \left(
            \begin{array}{cc}
                T^{-1} + T^{-1}UQ^{-1}VT^{-1} & -T^{-1}UQ^{-1} \\
                -Q^{-1}VT^{-1}                & Q^{-1}
            \end{array}
        \right)
        \\
        & = &
        \left(
            \begin{array}{cc}
                T^{-1} & 0 \\
                0 & 0
            \end{array}
        \right)
            +
            \left(
                \begin{array}{c}
                    -T^{-1}U \\
                    I_{n}
                \end{array}
            \right)
            Q^{-1}
            \left(
                \begin{array}{cc}
                    -VT^{-1}, & I_{n}
                \end{array}
            \right)
\end{eqnarray}
$$

$$
\begin{eqnarray}
    A_{2} 
    :=
    \left(
        \begin{array}{cc}
            W & V \\
            U & T
        \end{array}
    \right)^{-1}
    & = &
    \left(
        \begin{array}{cc}
            Q^{-1} & -Q^{-1}VT^{-1} \\
            -T^{-1}UQ^{-1} & T^{-1} + T^{-1}UQ^{-1}VT^{-1} 
        \end{array}
    \right)
    \\
    & = &
        \left(
            \begin{array}{cc}
                0 & 0 \\
                0 & T^{-1}
            \end{array}
        \right)
        +
        \left(
            \begin{array}{c}
                I_{n} \\
                -T^{-1}U
            \end{array}
        \right)
        Q^{-1}
        (I_{n}, -VT^{-1})
\end{eqnarray}
$$

#### proof.
定理8.5.10より、$Q$が正則であることと$A_{1}$は正則であることは同値。

<div class="QED" style="text-align: right">$\Box$</div>
