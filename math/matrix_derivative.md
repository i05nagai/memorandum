---
title: Matrix Derivative
---

## matrix

## 行列の微分

### 記号の定義
* $N \in \mathbb{N}$
* $M \in \mathbb{N}$
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
\begin{eqnarray}
	\frac{\partial h}{\partial x}(x) 
    & := &
		\left(
			\begin{array}{c}
				\left( \frac{\partial h^{1}}{\partial x}(x) \right)^{T} \\
				\vdots \\
				\left( \frac{\partial h^{M}}{\partial x}(x) \right)^{T}
			\end{array}
		\right)
	\nonumber
	\\
    & = &
		\left(
			\begin{array}{ccc}
				\frac{\partial h^{1}}{\partial x^{1}}(x)
				&
				\ldots 
				&
				\frac{\partial h^{1}}{\partial x^{N}}(x)
				\\
				\vdots & \ddots & \vdots \\
				\frac{\partial h^{M}}{\partial x^{1}}(x)
				&
				\ldots
				&
				\frac{\partial h^{M}}{\partial x^{N}}(x)
			\end{array}
		\right)
	\nonumber
\end{eqnarray}
$$

ここで、$h^{i}:\mathbb{R}^{N} \rightarrow \mathbb{R}$は$h$の$i$番目の成分関数。
つまり

$$
	h(x) 
    =
	\left(
        \begin{array}{c}
            h^{1}(x) \\
            \vdots \\
            h^{M}(x)
        \end{array}
    \right)
$$


### 公式

### 主要な行列演算

### 線形関数の微分
$f(x):\mathbb{R}^{N} \ni x \mapsto a^{\mathrm{T}} x \in \mathbb{R}$の微分。
ここで、$a = (a^{1} ,\ldots, a^{N})^{\mathrm{T}} \in \mathbb{R}^{N}$, $c \in \mathbb{R}$である。

$$
\begin{equation}
	(\nabla f)(x)
	=
	a
\end{equation}
$$

$$
\begin{equation}
	(\nabla^{2} f)(x)
	=
	\left(
		\begin{array}{ccc}
			 0 & \cdots & 0
			 \\
			 0 & \ddots & 0
			 \\
			 0 & \cdots & 0
		\end{array}
	\right)
	\in \mathbb{R}^{N \times N}
\end{equation}
$$

### 導出
まず、

$$
	\frac{\partial f(x)}{\partial x^{i}} 
	=
	a^{i}
$$

より、

$$
\begin{eqnarray}
	(\nabla f)(x)
	& = &
		\left(
			\begin{array}{c}
				a^{1} \\
				\vdots \\
				a^{N}
			\end{array}
		\right)
	\nonumber
	\\
	& = &
		a
\end{eqnarray}
$$

二階微分は明らか。

### 二次形式への変換の微分
$f(x):\mathbb{R}^{N} \ni x \mapsto x^{T}Ax \in \mathbb{R}$の微分。

* $A$が対称でない

$$
\begin{equation}
	\frac{\partial f(x)}{\partial x} 
    =
	Ax + A^{T}x.
	\label{derivative_bilinear_form_general}
\end{equation}
$$

$$
\begin{equation}
	\frac{\partial^{2} f(x)}{\partial x^{2}} 
    =
	A + A^{T}
	\label{second_derivative_bilinear_form_general}
\end{equation}
$$

* $A$が対称

$$
\begin{equation}
	\frac{\partial f(x)}{\partial x} 
    =
	2Ax
	\label{derivative_bilinear_form_symmetric}
\end{equation}
$$

$$
\begin{equation}
	\frac{\partial^{2} f(x)}{\partial x^{2}} 
    =
	2A
	\label{second_derivative_bilinear_form_symmetric}
\end{equation}
$$

* $A$が単位行列
	* $x$のノルムの微分

$$
\begin{equation}
	\frac{\partial f(x)}{\partial x} 
    =
	2x
	\label{derivative_bilinear_form_identity}
\end{equation}
$$

$$
\begin{equation}
	\frac{\partial^{2} f(x)}{\partial x^{2}} 
    =
	2I
	\label{second_derivative_bilinear_form_identity}
\end{equation}
$$

### 導出
$f(x)$の$x$での微分を考える。
$k = 1, \ldots, N$として、$\frac{\partial f(x)}{\partial x_{k}}$を求める。

まず、

$$
\begin{eqnarray}
	x^{T}Ax
	& = &
		\left( \sum_{i}x_{i}a_{1}^{i}, \ldots, \sum_{i}x_{i}a_{N}^{i} \right) x 
	\nonumber
	\\
    & = &
		\sum_{j} \left( \sum_{i}x_{i}a_{j}^{i} \right) x^{j}
	\nonumber
	\\
    & = &
		\sum_{j} \sum_{i} x_{i}a_{j}^{i}x^{j}
	\nonumber
\end{eqnarray}
$$

である。
また、

$$
\begin{eqnarray}
	x^{T}Ax
    & = &
		\sum_{j \neq k} \sum_{i} x_{i}a_{j}^{i}x^{j} 
			+ \sum_{i} x_{i}a_{k}^{i}x^{k} 
	\nonumber
	\\
	& = &
		\sum_{j \neq k} \sum_{i} x_{i}a_{j}^{i}x^{j} 
			+ \sum_{i \neq k} x_{i}a_{k}^{i}x^{k} 
			+ x_{k}a_{k}^{k}x^{k} 
	\nonumber
\end{eqnarray}
$$

である。
以上より

$$
\begin{eqnarray}
	\frac{\partial f(x)}{\partial x_{k}}
	& = &
		\sum_{j \neq k} a_{j}^{k}x^{j} 
			+ \sum_{i \neq k} x_{i}a_{k}^{i}
			+ 2a_{k}^{k}x^{k} 
	\nonumber
	\\
	& = &
		\sum_{j} a_{j}^{k}x^{j} 
			+ \sum_{i} x_{i}a_{k}^{i}
	\nonumber
	\\
	& = &
		\langle (a^{k})^{T}, x\rangle
			+ \langle a_{k}, x\rangle
	\nonumber
\end{eqnarray}
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

### 線形変換の微分
$f(x): \mathbb{R}^{N} \ni x \mapsto Bx \in \mathbb{R}^{M}$の微分。

$$
\begin{equation}
	\frac{\partial f(x)}{\partial x} 
    =
	\left(
        \begin{array}{c}
            b_{1}^{T} \\
            \vdots \\
            b_{N}^{T}
        \end{array}
    \right)
    = B^{T}
\end{equation}
$$

### 導出
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
    =
	\left(
        \begin{array}{c}
            b_{1}^{T} \\
            \vdots \\
            b_{N}^{T}
        \end{array}
    \right)
    = B^{T}
$$

### 合成関数の微分
$g(f(x)):\mathbb{R}^{N} \rightarrow \mathbb{R}^{L}$の合成関数の微分。

$$
\begin{eqnarray}
	\frac{\partial g(f(x))}{\partial x} 
	& = &
		\left(
			\begin{array}{c}
				(\nabla(g^{1} \circ f))(x) \\
				\vdots \\
				(\nabla(g^{L} \circ f))(x) \\
			\end{array}
		\right)
	\nonumber
	\\
	& = &
		\left(
			\begin{array}{ccc}
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{1}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{1}} 
				&
				\cdots
				&
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{1}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{N}} 
				\\
				\vdots \\
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{L}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{1}} 
				&
				\cdots
				&
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{L}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{N}} 
			\end{array}
		\right)
\end{eqnarray}
$$

### 導出
$$f: \mathbb{R}^{N} \rightarrow \mathbb{R}^{M}$$, $$g: \mathbb{R}^{M} \rightarrow \mathbb{R}^{L}$$とする。

$$
	x \in \mathbb{R}^{N},
	\quad
    f(x)
    :=
	\left(
		\begin{array}{c}
			f^{1}(x) \\
			\vdots \\
			f^{M}(x)
		\end{array}
	\right)
$$

また、

$$
	x \in \mathbb{R}^{M},
	\quad
    g(x)
    :=
	\left(
		\begin{array}{c}
			g^{1}(x) \\
			\vdots \\
			g^{L}(x)
		\end{array}
	\right)
$$

とすると、

$$
	x \in \mathbb{R}^{M},
	\quad
    g(f(x))
    =
	\left(
		\begin{array}{c}
			g^{1}(f(x)) \\
			\vdots \\
			g^{L}(f(x))
		\end{array}
	\right)
$$

とかけることに注意する。
合成関数の微分公式より、$$g^{k} \circ f: \mathbb{R}^{N} \rightarrow \mathbb{R}$$の微分は$$\forall i \in \{1, \ldots, N\}$$, $$\forall k \in \{1, \ldots, L \}$$について

$$
\frac{\partial g^{k} \circ f(x)}{\partial x^{i}} 
=
\sum_{j=1}^{M}
	\left.
		\frac{\partial g^{k}(y)}{\partial y^{j}} 
	\right|_{y=f(x)}
	\frac{\partial f^{j}(x)}{\partial x^{i}} 
$$

$$
\begin{equation}
	(\nabla (g^{k} \circ f))(x)
	=
	\left(
		\begin{array}{c}
			\displaystyle
			\sum_{j=1}^{M}
				\left.
					\frac{\partial g^{k}(y)}{\partial y^{j}} 
				\right|_{y=f(x)}
				\frac{\partial f^{j}(x)}{\partial x^{1}} 
			\\
			\vdots \\
			\displaystyle
			\sum_{j=1}^{M}
				\left.
					\frac{\partial g^{k}(y)}{\partial y^{j}} 
				\right|_{y=f(x)}
				\frac{\partial f^{j}(x)}{\partial x^{N}} 
		\end{array}
	\right)
	\nonumber
\end{equation}
$$

となる。
よって、

$$
\begin{eqnarray}
	\frac{\partial g(f(x))}{\partial x} 
	& = &
		\left(
			\begin{array}{c}
				(\nabla(g^{1} \circ f))(x) \\
				\vdots \\
				(\nabla(g^{L} \circ f))(x) \\
			\end{array}
		\right)
	\nonumber
	\\
	& = &
		\left(
			\begin{array}{ccc}
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{1}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{1}} 
				&
				\cdots
				&
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{1}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{N}} 
				\\
				\vdots \\
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{L}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{1}} 
				&
				\cdots
				&
				\displaystyle
				\sum_{j=1}^{M}
					\left.
						\frac{\partial g^{L}(y)}{\partial y^{j}} 
					\right|_{y=f(x)}
					\frac{\partial f^{j}(x)}{\partial x^{N}} 
			\end{array}
		\right)
	\nonumber
\end{eqnarray}
$$

### ノルムの微分
$$f(x):\mathbb{R}^{N} \ni x \mapsto \| x \|_{2}^{2} \in \mathbb{R}$$の微分。

$$
\begin{equation}
	\frac{\partial f(x)}{\partial x} 
    =
	2x
\end{equation}
$$

### 導出
$$\eqref{derivative_bilinear_form_general}$$の$A = I$の場合を考えれば良い。

$$
\begin{eqnarray}
	(\nabla f)(x) = 2x
\end{eqnarray}
$$
