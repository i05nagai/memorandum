---
title: Normal Distribution
---

## Normal Distribution
Gaussian Distributionともいう。

* $N \in \mathbb{N}$
* $$\mu \in \mathbb{R}^{d}$$,
* $$\Sigma \in \mathbb{R}^{d \times d}$$,
    * 対称正定値行列

以下の分布関数を平均$\mu$、分散$\Sigma$の$N$次元ガウス分布という。

$$
\begin{eqnarray}
    F(x)
    & := &
        \int_{(-\infty, x_{1}] \times (-\infty, x_{N}]}
            f(y;\mu, \Sigma)
        \ dy
    \nonumber
    \\
    f(y; \mu, \Sigma)
    & := &
		\frac{
			1
		}{
			(2\pi)^{k/2}
			| \Sigma |^{1/2}
		}
		\exp
		\left(
			-
			\frac{1}{2}
			(y - \mu)^{\mathrm{T}}
            \Sigma ^{-1}
			(y - \mu)
		\right)
    \nonumber
\end{eqnarray}
$$

$f(y; \mu, \Sigma)$は密度関数である。
ここで、$\mu \in \mathbb{R}^{N}$, $\Sigma \in \mathbb{R}^{N} \times \mathbb{R}^{N}$ の対称正定値行列である。

## Conditional distribution

### Example. 2-dim gaussian distribution

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
	f_{X_{2} \mid X{1}}(x_{2} \mid x_{1})
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
	f(x_{1} | x_{2})
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

### Example. $N$-dim gaussian distribution
$N$次元のガウス分布を考える。
$N_{1}, N_{2} \in \mathbb{N}$とし、$N = N_{1} + N_{2}$とする。
$N$次元の正規分布に従う確率変数の組に対して、最後の$N_{2}$個の確率変数で条件つけられた最初の$N_{1}$個の確率変数の条件付き分布を求める。
つまり、条件付き確率密度関数$f_{X_{1}, \ldots, X_{N_{1}} \mid X_{N_{1} + 1}, \ldots, X_{N}}$を求める。
記法を簡潔にするために、

* $$\mathbf{X}_{1} := (X_{1}, \ldots, X_{N_{1}})$$, 
* $$\mathbf{X}_{2} := (X_{N_{1} + 1}, \ldots, X_{N_{1}})$$, 
* $\mu \in \mathbb{R}^{N}$
    * $\mu_{1} \in \mathbb{R}^{N_{1}}$
    * $\mu_{2} \in \mathbb{R}^{N_{2}}$
* $\Sigma \in \mathbb{R}^{N} \times \mathbb{R}^{N}$,
    * 正定値対称行列
    * $\Sigma_{11} \in \mathbb{R}^{N_{1}} \times \mathbb{R}^{N_{1}}$,
    * $\Sigma_{12} \in \mathbb{R}^{N_{1}} \times \mathbb{R}^{N_{2}}$, 
    * $\Sigma_{21} \in \mathbb{R}^{N_{2}} \times \mathbb{R}^{N_{1}}$, 
    * $\Sigma_{22} \in \mathbb{R}^{N_{2}} \times \mathbb{R}^{N_{2}}$,

ここで、

$$
\begin{eqnarray}
    X
        & = &
        \left(
            \begin{array}{c}
                \mathbf{X}_{1}
                \\
                \mathbf{X}_{2}
            \end{array}
        \right)
    \\
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

とする。

確率変数の組$X := (X_{1}, \ldots, X_{N})$は以下の確率分布に従うとする。

$$
    X \sim
        \mathcal{N}^{N}(\mu, \Sigma)
$$

このとき、条件付き確率密度関数$$f_{\mathbf{X}_{1} \mid \mathbf{X}_{2}}$$は、平均$$\mu_{\mathbf{X}_{1} \mid \mathbf{X}_{2}}$$分散$$\Sigma_{\mathbf{X}_{1} \mid \mathbf{X}_{2}}$$である。

$$
\begin{eqnarray}
    \mu_{\mathbf{X}_{1} \mid \mathbf{X}_{2}}
        & := & 
            \mu_{1} + \Sigma_{12}\Sigma_{22}^{-1}(a - \mu_{2}),
    \\
    \Sigma_{\mathbf{X}_{1} \mid \mathbf{X}_{2}}
        & := &
            \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}
\end{eqnarray}
$$

導出は2変数の場合と同様である。
まず、$\mathbf{X}_{1}$ のmarginal p.d.f. は以下である。

$$
\begin{eqnarray}
    f_{\mathbf{X}_{1}}(\mathbf{x}_{1})
    & = &
		\frac{
			1
		}{
			(2\pi)^{N_{1}/2}
			| \Sigma_{11} |^{1/2}
		}
		\exp
		\left(
			-
			\frac{1}{2}
			(\mathbf{x}_{1} - \mu_{1})^{\mathrm{T}}
            \Sigma_{11} ^{-1}
			(\mathbf{x}_{1} - \mu_{2})
		\right)
\end{eqnarray}
$$

$$
\begin{eqnarray}
    f_{\mathbf{X}_{1}, \mathbf{X}_{2}}(\mathbf{x}_{1}, \mathbf{x}_{2})
    & = &
		\frac{
			1
		}{
			(2\pi)^{N/2}
			| \Sigma |^{1/2}
		}
		\exp
		\left(
			-
			\frac{1}{2}
			(\mathbf{x} - \mu)^{\mathrm{T}}
            \Sigma ^{-1}
			(\mathbf{x} - \mu)
		\right)
    \nonumber
\end{eqnarray}
$$

expの中を更に計算する。
まず、逆行列の公式から

$$
\begin{eqnarray}
    \Sigma^{-1}
    & = &
        \left(
            \begin{array}{cc}
                \Sigma_{11}^{-1} 
                +
                \Sigma_{11}^{-1}\Sigma_{12}S^{-1}\Sigma_{12}^{\mathrm{T}}\Sigma_{11}^{-1}
                    & 
                        -\Sigma_{11}^{-1}\Sigma_{12}S^{-1}
                \\
                -S^{-1}\Sigma_{12}^{\mathrm{T}}\Sigma_{11}^{-1}
                    &
                        S^{-1}
            \end{array}
        \right)
    \nonumber
    \\
    S
    & := &
        \Sigma_{22}
        -
        \Sigma_{12}^{\mathrm{T}}\Sigma_{11}^{-1}\Sigma_{12}
\end{eqnarray}
$$

* $A_{11} \in \mathbb{R}^{N_{1}} \times \mathbb{R}^{N_{1}}$,
* $A_{12} \in \mathbb{R}^{N_{1}} \times \mathbb{R}^{N_{2}}$, 
* $A_{21} \in \mathbb{R}^{N_{2}} \times \mathbb{R}^{N_{1}}$, 
* $A_{22} \in \mathbb{R}^{N_{2}} \times \mathbb{R}^{N_{2}}$,

$$
\begin{equation}
    \left(
        \begin{array}{cc}
            A_{11} & A_{12}
            \\
            A_{21} & A_{22}
        \end{array}
    \right)
    :=
    \Sigma^{-1}
\end{equation}
$$

とおくと、

$$
\begin{eqnarray}
    (\mathbf{x} - \mu)^{\mathrm{T}}
        \Sigma ^{-1}
        (\mathbf{x} - \mu)
    & = &
        (\mathbf{x}_{1} - \mu)^{\mathrm{T}}
            A_{11}
            (\mathbf{x}_{1} - \mu)
        +
        (\mathbf{x}_{1} - \mu)^{\mathrm{T}}
            A_{12}
            (\mathbf{x}_{2} - \mu)
        +
        (\mathbf{x}_{2} - \mu)^{\mathrm{T}}
            A_{21}
            (\mathbf{x}_{1} - \mu)
        +
        (\mathbf{x}_{2} - \mu)^{\mathrm{T}}
            A_{22}
            (\mathbf{x}_{2} - \mu)
    \nonumber
\end{eqnarray}
$$

であるから

$$
\begin{eqnarray}
    (\mathbf{x}_{1} - \mu)^{\mathrm{T}}
        A_{11}
        (\mathbf{x}_{1} - \mu)
    -
    (\mathbf{x}_{1} - \mu)^{\mathrm{T}}
        \Sigma_{11}^{-1}
        (\mathbf{x}_{1} - \mu)
    & = &
    (\mathbf{x}_{1} - \mu)^{\mathrm{T}}
        \Sigma_{11}^{-1}\Sigma_{12}S^{-1}\Sigma_{12}^{\mathrm{T}}\Sigma_{11}^{-1}
        (\mathbf{x}_{1} - \mu)
\end{eqnarray}
$$


## Reference
* [Normal distribution - Wikipedia](https://en.wikipedia.org/wiki/Normal_distribution)
* [Multivariate normal distribution - Wikipedia](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)

