---
layout: math
title: Probability Theory
---

# Probability Theory

## Conditional Expectation

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

