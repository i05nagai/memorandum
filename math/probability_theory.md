---
title: Probability Theory
---

## Probability Theory

## Independence

### Def. Pair-wise Independence
$$\{ \mathcal{A}_{i} \}_{i \in I}$$が $\mathcal{F}$ 上の $\sigma$ -algebraの族とする。
以下が成り立つとき、$$\{ \mathcal{A}_{i} \}_{i \in I}$$は互いに独立(pairwise independence)であるという。

$$
    \forall i \neq j,
    \quad
    P(A_{i} \cap A_{j}) 
        = P(A_{i}) P(A_{j}),
    \quad
    \forall A_{i} \in \mathcal{A}_{i}, \forall A_{j} \in \mathcal{A}_{j}
$$

### Def. Independence of $\sigma$-algebra
$$\{ \mathcal{A}_{i} \}_{i \in I}$$が $\mathcal{F}$ 上の $\sigma$ -algebraの族とする。
以下が成り立つとき、$$\{ \mathcal{A}_{i} \}_{i \in I}$$が独立であるという。

$$
    \forall N \in \mathbb{N},
    \quad
    \forall i_{1}, \ldots, i_{N} \in I,
    \quad
    P(A_{i_{1}} \cap \cdots \cap A_{i_{N}}) 
        = \prod_{j=1}^{N}P(A_{i_{j}}),
    \quad
    \forall A_{i_{1}} \in \mathcal{A}_{i_{1}}, \ldots, \forall A_{i_{N}} \in \mathcal{A}_{i_{N}}
$$

### Def. Independence of random variables
$$\{X_{i}\}_{i \in I}$$が $\mathcal{F}$ 上の確率変数の族とする。
各確率変数が生成する$\sigma$-algebraが独立のとき、$$\{X_{i}\}_{i \in I}$$が独立であるという。
つまり、

$$
    \forall N \in \mathbb{N},
    \quad
    \forall i_{1}, \ldots, i_{N} \in I,
    \quad
    P(A_{i_{1}} \cap \cdots \cap A_{i_{N}}) 
        = \prod_{j=1}^{N}P(A_{i_{j}}),
    \quad
    \forall A_{i_{1}} \in \sigma(X_{i_{1}}), \ldots, \forall A_{i_{N}} \in \sigma(X_{i_{N}}).
$$

### Remark
独立性は$\sigma$-algebraを通して定義される。
よって、$\sigma$-algbera上での独立を議論すれば十分である。


### Remark
$\forall i \neq j$について、$A_{i}$と$A_{j}$が独立であっても、$A_{1}, \ldots, A_{N}$が独立であるとは限らない。
実際、

* $N=3$
* $\Omega := \\{\omega_{000}, \omega_{001}, \omega_{010}, \ldots, \omega_{111} \\}$
* $\mathcal{F} := 2^{\Omega}$
    * $\Omega$のべき集合
* $X_{1}, X_{2}, X_{3}$は0,1の値を取る確率変数
    * $X_{i}(\omega_{k_{1}k_{2}k_{3}}) := k_{i}$とする

確率変数の確率$P$を以下で定義する。


* $P(X_{1}=1,\ X_{2}=1,\ X_{3}=1) = 1/8$
* $P(X_{1}=1,\ X_{2}=1,\ X_{3}=0) = 0$
* $P(X_{1}=1,\ X_{2}=0,\ X_{3}=1) = 0$
* $P(X_{1}=1,\ X_{2}=0,\ X_{3}=0) = 1/8$
* $P(X_{1}=0,\ X_{2}=1,\ X_{3}=1) = 1/8$
* $P(X_{1}=0,\ X_{2}=1,\ X_{3}=0) = 1/4$
* $P(X_{1}=0,\ X_{2}=0,\ X_{3}=1) = 1/4$
* $P(X_{1}=0,\ X_{2}=0,\ X_{3}=0) = 1/8$

以上より、

* $P(X_{1} = 1) = 1/4$
* $P(X_{1} = 0) = 3/4$
* $P(X_{2} = 1) = 1/2$
* $P(X_{2} = 0) = 1/2$
* $P(X_{3} = 1) = 1/2$
* $P(X_{3} = 0) = 1/2$
* $P(X_{1} = 1)P(X_{2} = 1) = 1/8$
* $P(X_{1} = 1)P(X_{2} = 0) = 1/8$
* $P(X_{1} = 0)P(X_{2} = 1) = 3/8$
* $P(X_{1} = 0)P(X_{2} = 0) = 3/8$
* $P(X_{1} = 1)P(X_{3} = 1) = 1/8$
* $P(X_{1} = 1)P(X_{3} = 0) = 1/8$
* $P(X_{1} = 0)P(X_{3} = 1) = 3/8$
* $P(X_{1} = 0)P(X_{3} = 0) = 3/8$ 
* $P(X_{1} = 1,\ X_{2} = 1) = 1/8$
* $P(X_{1} = 1,\ X_{2} = 0) = 1/8$
* $P(X_{1} = 0,\ X_{2} = 1) = 3/8$
* $P(X_{1} = 0,\ X_{2} = 0) = 3/8$
* $P(X_{1} = 1,\ X_{3} = 1) = 1/8$
* $P(X_{1} = 1,\ X_{3} = 0) = 1/8$
* $P(X_{1} = 0,\ X_{3} = 1) = 3/8$
* $P(X_{1} = 0,\ X_{3} = 0) = 3/8$

であり、$\forall i \neq j$について$X_{i}, X_{j}$は独立である。
一方、

* $P(X_{1}=1,\ X_{2}=1,\ X_{3}=1) = 1/8$
* $P(X_{1}=1)P(X_{2}=1)P(X_{3}=1) = 1/16$

で$X_{1}, X_{2}, X_{3}$は独立でない。

### Proposition
確率変数が密度関数をもつ場合は密度関数によって、独立性を定義できる。

$X_{1}, \ldots, X_{N}$を確率変数とする。
$$f_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})$$を$$X_{1}, \ldots, X_{N}$$を同時密度関数とする。
また、$$f_{X_{1}}, \ldots, f_{X_{N}}$$を確率変数の周辺密度関数とする。
このとき以下は同値

* $$X_{1}, \ldots, X_{N}$$が独立
* 密度関数について以下が成立

$$
    \forall M \in \{1, \ldots, N\},
    \quad
    1 \le \forall i_{1} \le \cdots \le \forall i_{M} \le N,
    \quad
    f_{X_{i_{1}}, \ldots, X_{i_{M}}}(x_{i_{1}}, \ldots, x_{i_{M}})
    =
    f_{X_{i_{1}}}(x_{i_{1}}) \cdots, f_{X_{i_{N}}}(x_{i_{N}})
$$

### proof.


$$
\begin{eqnarray}
    \prod_{j=1}^{N}
    P(X_{i_{j}} \in A_{j})
    & = &
        \prod_{j=1}^{N}
        \int_{A_{j}} f_{X_{i_{j}}}(x_{j})\ d x_{j}
    \nonumber
    \\
    & = &
        \int_{A_{j}} 
            \prod_{j=1}^{N}
            f_{X_{i_{j}}}(x_{j})
        \ d x_{j}
    \nonumber
\end{eqnarray}
$$

に注意すれば良い。
 
<div class="QED" style="text-align: right">$\Box$</div>

### Proposition(Independence with p.d.f.)
確率変数が密度関数をもつ場合は、独立性はやや簡単になる。
次が成立する。

$$X_{1}, \ldots, X_{N}$$を確率変数とし、joint p.d.f $$f_{X_{1}, \ldots, X_{N}}$$を持つとする。
このとき、以下は同値

1. $$X_{1}, \ldots, X_{N}$$が独立
2. 以下が成立

$$
    f_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})
    =
    \prod_{i=1}^{N}f_{X_{i}}(x_{i})
$$

つまり、最長のjoint p.d.fについてのみ、考慮すれば良い。

### proof.
1から2は自明である。
2から1は、marginal p.d.f. がjoint p.d.f.でかけることを利用すれば良い。
例えば、

$$
\begin{eqnarray}
    f_{X_{1}, \ldots, X_{N-1}}(x_{1}, \ldots, x_{N-1})
    & = &
        \int f_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})\ dx_{N}
    \nonumber
    \\
    & = &
        \int
            \prod_{i=1}^{N}
            f_{X_{i}}(x_{i})
        \ dx_{N}
    \nonumber
    \\
    & = &
        \prod_{i=1}^{N-1}
        f_{X_{i}}(x_{i})
\end{eqnarray}
$$

である。
同様に任意の有限個の組について示すことができる。

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem (Dynkin's theorem)
Dynkin族定理。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

### Proposition
$$\{ \mathcal{G}_{i} \}_{i \in I}$$をsub $\sigma$-algberaとする。
$$\mathcal{C}_{i}$$を$\pi$系とし、$$\sigma(\mathcal{C}_{i}) = \mathcal{G}_{i}$$とする。
以下は同値

1. $$\{\mathcal{G}_{i}\}_{i \in I}$$が独立
2. 以下が成立

$$
    \forall N \in \mathbb{N}
    \quad
    \forall A_{1} \in \mathcal{C}_{i_{1}}, \ldots, A_{N} \in \mathcal{C}_{i_{N}},
    \quad
    P(A_{1}) \cdots P(A_{N})
    =
    P(A_{1} \cap \cdots \cap A_{N})
$$

### proof.
1から2は自明であるので、2から1を示す。

<div class="QED" style="text-align: right">$\Box$</div>


### Def. Conditional Independence
TBD.

## Conditional Probability Density Function
条件付き確率密度関数について考える。

### Gaussian Distribution
$N$変数の正規分布の密度関数は以下でかける。

$$
	f_{X}(x)
		= \frac{1}{(2 \pi)^{N/2} \sqrt{| \Sigma |} }
			\exp
			\left(
			    - \frac{1}{2}(x - \mu)^{\mathrm{T}} \Sigma^{-1} (x - \mu)
			\right)
$$

ここで、$\mu \in \mathbb{R}^{N}$, $\Sigma \in \mathbb{R}^{N} \times \mathbb{R}^{N}$ の対称正定値行列である。

#### Example 2-dim gaussian distribution

2変数の場合の正規分布の条件付き期待値の例をみる。

$$
	\Sigma 
		= 
		\left(
			\begin{array}{cc}
				\sigma_{11}^{2} & \sigma_{12} \\
				\sigma_{21} & \sigma_{22}^{2} 
			\end{array}
		\right)
$$

ここで、$\sigma_{12} = \sigma_{21}$である。

$$
	|\Sigma|
		= \sigma_{11}^{2} \sigma_{22}^{2} - \sigma_{12}^{2} 
		= \sigma_{11}^{2} \sigma_{22}^{2}
			\left(
				1 - \frac{\sigma_{12}^{2}}{\sigma_{11}^{2}\sigma_{22}^{2}}
			\right)
		= \sigma_{11}^{2} \sigma_{22}^{2}(1 - \rho^{2})
$$

ここで、$\rho^{2} := \frac{\sigma_{12}^{2}}{\sigma_{11}^{2} \sigma_{22}^{2}}$である。

$$
	\Sigma^{-1}
		= \frac{1}{| \Sigma |} 
			\left(
			   	\begin{array}{cc}
					\sigma_{22}^{2} & -\sigma_{12} \\
					-\sigma_{12} & \sigma_{11}^{2}
				\end{array}
			\right)
		= 
			\left(
			   	\begin{array}{cc}
					\frac{1}{\sigma_{11}^{2}(1 - \rho^{2})} & -\frac{\sigma_{12}}{\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})} \\
					-\frac{\sigma_{12}}{\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})} & \frac{1}{\sigma_{22}^{2}(1 - \rho^{2})}
				\end{array}
			\right)
$$

である。
よって、2変数の場合の同時密度関数は以下でかける。

$$
	f_{X}(x_{1}, x_{2})
		= \frac{1}{2 \pi \sqrt{\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})}}
			\exp
			\left(
			    -\frac{1}{2} 
				\frac{(x_{1} - \mu_{1})^{2} \sigma_{22}^{2}
					- 2 (x_{1} - \mu_{1})(x_{2} - \mu_{2}) \sigma_{12}
					+ (x_{2} - \mu_{2})^{2}\sigma_{11}^{2}}{\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})}
			\right)
$$

$X_{1}$の周辺密度関数は以下である。

$$
    f_{X_{1}}(x_{1}) 
        = \frac{1}{\sqrt{2 \pi \sigma_{11}^{2}}}
			\exp
				\left(
				    -\frac{1}{2} \frac{(x_{1} - \mu_{1})^{2}}{\sigma_{11}^{2}}
				\right)
$$


$$
\begin{eqnarray*}
	\left(
		\frac{(x_{1} - \mu_{1})^{2} \sigma_{22}^{2}
			- 2 (x_{1} - \mu_{1})(x_{2} - \mu_{2}) \rho \sigma_{11}\sigma_{22}
			+ (x_{2} - \mu_{2})^{2}\sigma_{11}^{2}}{\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})}
		- \frac{(x_{1} - \mu_{1})^{2}}{\sigma_{11}^{2}}
	\right)
	& = &
		\frac{(x_{1} - \mu_{1})^{2} \sigma_{22}^{2}
			- 2 (x_{1} - \mu_{1})(x_{2} - \mu_{2})  \rho \sigma_{11}\sigma_{22}
			+ (x_{2} - \mu_{2})^{2}\sigma_{11}^{2}
			- (x_{1} - \mu_{1})^{2} \sigma_{22}^{2}(1 - \rho^{2})
		}{
			\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})
		}
	\\
	& = &
		\frac{(x_{1} - \mu_{1})^{2} \sigma_{22}^{2}(1 -1 + \rho^{2})
			- 2 (x_{1} - \mu_{1})(x_{2} - \mu_{2})  \rho \sigma_{11}\sigma_{22}
			+ (x_{2} - \mu_{2})^{2}\sigma_{11}^{2}
		}{
			\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})
		}
	\\
	& = &
		\frac{(x_{1} - \mu_{1})^{2} \sigma_{22}^{2}\rho^{2}
			- 2 (x_{1} - \mu_{1})(x_{2} - \mu_{2})  \rho \sigma_{11}\sigma_{22}
			+ (x_{2} - \mu_{2})^{2}\sigma_{11}^{2}
		}{
			\sigma_{11}^{2}\sigma_{22}^{2}(1 - \rho^{2})
		}
	\\
	& = &
		\frac{(x_{1} - \mu_{1})^{2} \frac{\sigma_{22}^{2}\rho^{2}}{\sigma_{11}^{2}}
			- 2 (x_{1} - \mu_{1})(x_{2} - \mu_{2})  \rho \frac{\sigma_{22}}{\sigma_{11}}
			+ (x_{2} - \mu_{2})^{2}
		}{
			\sigma_{22}^{2}(1 - \rho^{2})
		}
	\\
	& = &
		\frac{
			\left(
				(x_{2} - \mu_{2})
				- (x_{1} - \mu_{1}) \frac{\sigma_{22}\rho}{\sigma_{11}} 
			\right)^{2}
		}{
			\sigma_{22}^{2}(1 - \rho^{2})
		}
\end{eqnarray*}
$$

以上より、

$$
\begin{eqnarray*}
	f(x_{1}, x_{2} | x_{1})
		& = & 
			\frac{f_{X_{1}, X_{2}}(x_{1}, x_{2})}{f_{X_{1}}(x_{1})}
		\\
		& = & 
			\frac{1}{\sqrt{2 \pi \sigma_{22}^{2}(1 - \rho^{2})}}
			\exp
			\left(
                -\frac{1}{2}
				\frac{
					\left(
						(x_{2} - \mu_{2})
						- (x_{1} - \mu_{1}) \frac{\sigma_{22}\rho}{\sigma_{11}} 
					\right)^{2}
				}{
					\sigma_{22}^{2}(1 - \rho^{2})
				}
			\right)
\end{eqnarray*}
$$

また、同様に、

$$
\begin{eqnarray*}
	f(x_{1}, x_{2} | x_{2})
		& = & 
			\frac{f_{X_{1}, X_{2}}(x_{1}, x_{2})}{f_{X_{2}}(x_{2})}
		\\
		& = & 
			\frac{1}{\sqrt{2 \pi \sigma_{11}^{2}(1 - \rho^{2})}}
			\exp
			\left(
                -\frac{1}{2}
				\frac{
					\left(
						(x_{1} - \mu_{1})
						- (x_{2} - \mu_{2}) \frac{\sigma_{11}\rho}{\sigma_{22}} 
					\right)^{2}
				}{
					\sigma_{11}^{2}(1 - \rho^{2})
				}
			\right)
\end{eqnarray*}
$$

である。

#### Example $N$-dim gaussian distribution
$N$次元のガウス分布を考える。
$N_{1}, N_{2} \in \mathbb{N}$とし、$N = N_{1} + N_{2}$とする。
$\mu \in \mathbb{R}^{N}$とし、$\Sigma \in \mathbb{R}^{N} \times \mathbb{R}^{N}$は正定値行列とする。
確率変数の組$X := (X_{1}, \ldots, X_{N})$は以下の確率分布に従うとする。

$$
    X \sim
        \mathcal{N}^{N}(\mu, \Sigma)
$$

このとき、条件付き確率密度関数$f_{X_{1}, \ldots, X_{N_{1}} \mid X_{N_{1} + 1}, \ldots, X_{N}}$は、平均$$\mu_{X_{1}, \ldots, X_{N_{1}} \mid X_{N_{1}+1}, \ldots, X_{N}}$$分散$$\Sigma_{X_{1}, \ldots, X_{N_{1}} \mid X_{N_{1}+1}, \ldots, X_{N}}$$である。

$$
\begin{eqnarray}
    \mu_{X_{1}, \ldots, X_{N_{1}} \mid X_{N_{1}+1}, \ldots, X_{N}}
        & := & 
            \mu_{1} + \Sigma_{12}\Sigma_{22}^{-1}(a - \mu_{2}),
    \\
    \Sigma_{X_{1}, \ldots, X_{N_{1}} \mid X_{N_{1}+1}, \ldots, X_{N}}
        & := &
            \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}
\end{eqnarray}
$$

ここで、

$$
\begin{eqnarray}
    \mu 
        & = &
        \left(
            \begin{array}{c}
                \mu_{1} \\
                \mu_{2}
            \end{array}
        \right)
    \\
    \Sigma
        & = &
        \left(
            \begin{array}{cc}
                \Sigma_{11} & \Sigma_{12} \\
                \Sigma_{21} & \Sigma_{22}
            \end{array}
        \right),
\end{eqnarray}
$$

であり、

* $\mu_{1} \in \mathbb{R}^{N_{1}}$
* $\mu_{2} \in \mathbb{R}^{N_{2}}$
* $\Sigma_{11} \in \mathbb{R}^{N_{1}} \times \mathbb{R}^{N_{1}}$,
* $\Sigma_{12} \in \mathbb{R}^{N_{1}} \times \mathbb{R}^{N_{2}}$, 
* $\Sigma_{21} \in \mathbb{R}^{N_{2}} \times \mathbb{R}^{N_{1}}$, 
* $\Sigma_{22} \in \mathbb{R}^{N_{2}} \times \mathbb{R}^{N_{2}}$,

である。

# Reference
* [Multivariate normal distribution - Wikipedia](https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Conditional_distributions)
