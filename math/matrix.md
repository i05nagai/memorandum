---
layout: math
title: Matrix
---

# matrix

## 行列の微分

### 記号の定義
* $N \in \mathbb{N}$
* $N \in \mathbb{M}$
* $A = (a_{j}^{i})_{i,j}$
    * $N \times N$の正方行列
    * $A$の$i$行$j$番目の要素を$a_{j}^{i}$とかく
* $a^{i}$
    * 行列$A$の$i$番目の行ベクトル
* $a_{j}$
    * 行列$A$の$j$番目の列ベクトル

つまり、

$$
A 
    = \left(
        \begin{array}{ccc}
            a_{1}^{1} & \ldots &  a_{N}^{1} \\
            \vdots & \ddots & \vdots \\
            a_{1}^{N} & \ldots & a_{N}^{N}
        \end{array}
    \right)
    = \left(
        \begin{array}{c}
            a^{1} \\
            \vdots \\
            a^{N}
        \end{array}
    \right)
    =
    \left(
        a_{1}, \ldots, a_{N}
    \right)
$$

同様に

* $B = (b_{j}^{i})_{i,j}$
    * $M$行$N$列の行列
    * $B$の$i$行$j$番目の要素を$b_{j}^{i}$とかく
* $b^{i}$
    * 行列$B$の$i$番目の行ベクトル
* $b_{j}$
    * 行列$B$の$j$番目の列ベクトル

* $x = (x^{i})_{i} \in \mathbb{R}^{N}$
    * 長さ$N$の縦ベクトル
    * $x$の$i$番目の要素を$x^{i}$で表す。

$$
x  = 
    \left(
        \begin{array}{c}
            x^{1} \\
            \vdots \\
            x^{N}
        \end{array}
    \right)
   
$$

転置をとる場合は、要素の添字を上下反転させる。
つまり、

$$
A^{T} = (a_{i}^{j})_{i,j}
    = \left(
        \begin{array}{ccc}
            a_{1}^{1}, \ldots, a_{1}^{N} \\
            \vdots \ddots \vdots \\
            a_{N}^{1}, \ldots, a_{N}^{N}
        \end{array}
    \right)
$$

で$a_{i}^{j}$は$j$行$i$番目を表す。
また、

$$
x^{T} 
    = ((x^{i})_{i})^{T}
    = (x_{i})_{i}
    = (x_{1}, \ldots, x_{N})
$$

で、横ベクトルある。
$x_{i} = x^{i} \ (\forall i)$に注意する。


多変数関数$h: \mathbb{R}^{N} \rightarrow \mathbb{R}$の微分を以下で定義する。

$$
\frac{\partial h}{\partial x}(x) 
    := \left(
        \begin{array}{c}
            \frac{\partial h}{\partial x^{1}}(x) \\
            \vdots \\
            \frac{\partial h}{\partial x^{N}}(x)
        \end{array}
    \right)
$$

多変数ベクトル値関数$h: \mathbb{R}^{N} \rightarrow \mathbb{R}^{M}$の微分を以下で定義する。

$$
\frac{\partial h}{\partial x}(x) 
    := \left(
        \begin{array}{c}
            \left( \frac{\partial h^{1}}{\partial x}(x) \right)^{T} \\
            \vdots \\
            \left( \frac{\partial h^{M}}{\partial x}(x) \right)^{T}
        \end{array}
    \right)
    = \left(
        \begin{array}{ccc}
            \frac{\partial h^{1}}{\partial x^{1}}(x) & \ldots & \frac{\partial h^{1}}{\partial x^{N}}(x) \\
            \vdots & \ddots & \vdots \\
            \frac{\partial h^{M}}{\partial x^{1}}(x) & \ldots & \frac{\partial h^{M}}{\partial x^{N}}(x)
        \end{array}
    \right)
$$

ここで、$h^{i}:\mathbb{R}^{N} \rightarrow \mathbb{R}$は$h$の$i$番目の成分関数。
つまり

$$
h(x) 
    = \left(
        \begin{array}{c}
            h^{1}(x) \\
            \vdots \\
            h^{M}(x)
        \end{array}
    \right)
$$


### 公式

### 主要な行列演算

### $f(x):\mathbb{R}^{N} \ni x \mapsto x^{T}Ax \in \mathbb{R}$の微分
$f(x)$の$x$での微分を考える。
$k = 1, \ldots, N$として、$\frac{\partial f(x)}{\partial x_{k}}$を求める。

まず、

$$
x^{T}Ax
    = \left( \sum_{i}x_{i}a_{1}^{i}, \ldots, \sum_{i}x_{i}a_{N}^{i} \right) x 
    = \sum_{j} \left( \sum_{i}x_{i}a_{j}^{i} \right) x^{j}
    = \sum_{j} \sum_{i} x_{i}a_{j}^{i}x^{j}
$$

である。
また、

$$
x^{T}Ax
    = \sum_{j \neq k} \sum_{i} x_{i}a_{j}^{i}x^{j} 
        + \sum_{i} x_{i}a_{k}^{i}x^{k} 
    = \sum_{j \neq k} \sum_{i} x_{i}a_{j}^{i}x^{j} 
        + \sum_{i \neq k} x_{i}a_{k}^{i}x^{k} 
        + x_{k}a_{k}^{k}x^{k} 
$$

である。
以上より

$$
\frac{\partial f(x)}{\partial x_{k}}
    = \sum_{j \neq k} a_{j}^{k}x^{j} 
        + \sum_{i \neq k} x_{i}a_{k}^{i}
        + 2a_{k}^{k}x^{k} 
    = \sum_{j} a_{j}^{k}x^{j} 
        + \sum_{i} x_{i}a_{k}^{i}
    = \langle (a^{k})^{T}, x\rangle
        + \langle a_{k}, x\rangle
$$

を得る。
上式の第1項は、$A$の$k$番目の行ベクトルと$x$との内積である。
上式の第2項は、$A$の$k$番目の列ベクトルと$x$との内積である。
これに注意すると、

$$
\frac{\partial f(x)}{\partial x} 
    = Ax + A^{T}x.
$$

特に$A$が対称行列の場合は、

$$
\frac{\partial f(x)}{\partial x} 
    = 2Ax.
$$

### $f(x): \mathbb{R}^{N} \ni x \mapsto Bx \in \mathbb{R}^{M}$の微分
まず、

$$
Bx 
    = \left(
        \begin{array}{c}
            \sum_{j}b_{j}^{1}x^{j} \\
            \vdots \\
            \sum_{j}b_{j}^{M}x^{j}
        \end{array}
    \right)
$$

である。
$k = 1, \ldots, N$とすると、

$$
\frac{\partial f}{\partial x^{k}}
    = \left(
        \begin{array}{c}
            b_{k}^{1} \\
            \vdots \\
            b_{k}^{M}
        \end{array}
    \right)
   = b_{k}
$$

と$B$の$k$番目の列ベクトルの転置なる。
よって、

$$
\frac{\partial f(x)}{\partial x} 
    = \left(
        \begin{array}{c}
            b_{1}^{T} \\
            \vdots \\
            b_{N}^{T}
        \end{array}
    \right)
    = B^{T}
$$

### $g(f(x)):\mathbb{R}^{L} \rightarrow \mathbb{N}$の合成関数の微分 

