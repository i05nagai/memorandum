---
title: Bayes
---

# Symbols
* $(\Omega, \mathcal{F}, P)$
    * probablity space
* $p_{X}(\cdot)$
    * 確率変数$X$の確率密度関数
* $p_{X \| Y}(\cdot \| y)$
    * 確率変数$Y=y$が与えられたときの$X$の条件付き確率密度関数

# Bayes

## Preliminary
以下では、全ての確率変数は密度関数を持つと仮定する。

### Def. Conditionally i.i.d
$X$が確率変数とする。
$X_{1}, \ldots, X_{N}$が$\Theta$の上の$X$のi.i.d.であるとは、

* $X_{1}, \ldots, X_{N}$が$\Theta$について条件付き独立
* $X_{1}, \ldots, X_{N}$の$\Theta$についての条件付き分布が同分布

を満たすことを言う。

### Remark
$X_{1}, \ldots, X_{N}$が$\Theta$について条件付き独立であることは、$X_{1}, \ldots, X_{N}, \Theta$が独立であることより弱い。
条件付き独立性はBayesでは勝手に仮定されていることが多い。


## Bayesian Framework

* $X$を$m$次元の確率変数とする
    * $X$は観測されているデータの元となる確率変数
* $X_{1}, \ldots, X_{N}$を$m$次元の確率変数で、$X$のi.i.dとする
    * $X$から得られるサンプル
    * 我々が観測している値は、この確率変数の実現値
    * 各$i = 1, \ldots, N$の実現値として$X_{i}(\omega) = x_{i}$と書かれることが多い
* $\Theta$を$l$次元の確率変数とする
    * $\Theta$はparameterを表す確率変数である
    * Bayesの世界では、parameterを確率変数として考えることが重要である

機械学習では、観測された$N$個のデータの組$(x_{1}, \ldots, x_{N})$（つまり、$X_{1}(\omega), \ldots, X_{N}(\omega)$）から、$X$の分布を何らかの意味で決定するparameter $\theta$を求めるのが基本的な問題となる。

By Bayes Theorem,

$$
    p_{\Theta | X}
        = \frac{
            p_{X | \Theta} p_{\Theta}
        }{
            p_{X}
        }
$$

holds where

* $p_{\Theta \| X}$
    * $\Theta$ a posterior distribution
    * 観測値が与えられた時のパラメータのの条件付き確率
* $p_{X \| \Theta}$
    * $\Theta$ likelihood function
    * パラメータが与えられた時の条件付き確率
* $p_{\Theta}$
    * $\Theta$ prior distribution
    * パラメータの周辺分布
* $p_{X}$
    * $X$ prior distribution
* $p_{X, \Theta}$
    * 同時分布
    * 一般的な用語

By definition,

$$
    p_{X \| \Theta}
    :=
    \frac{
        p_{X, \Theta}(x, \theta)
    }{
        p_{\Theta}(\theta)
    }
$$

また、$X_{1}, \ldots, X_{N}$が$X$のi.i.idより、各サンプルについて以下が成り立つ。

$$
\begin{eqnarray}
    p_{\Theta | (X_{1}, \ldots, X_{N})}
        & = &
            \frac{
                p_{(X_{1}, \ldots, X_{N}) | \Theta} p_{\Theta}
            }{
                p_{X_{1}, \ldots, X_{N}}
            }
        \nonumber
        \\
        & = &
            \left(
                \prod_{i=1}^{N} p_{X_{i} | \Theta}
            \right)
            \frac{
                p_{\Theta}
            }{
                p_{X_{1}, \ldots, X_{N}}
            }
        \nonumber
        \\
        & = &
            (p_{X | \Theta})^{N}
            \frac{
                p_{\Theta}
            }{
                p_{X_{1}, \ldots, X_{N}}
            }
        \nonumber
\end{eqnarray}
$$


## Maximum A Posteriori estimation
MAP推定。

### Determination of $\theta$
MAP推定では、各サンプル$X_{1}, \ldots, X_{N}$から$\theta$を事後分布を最大にする$\theta^{*}$として求める。
その為に、事前分布$p_{\Theta}$と尤度$p_{X \| \Theta}$が何らかの確率分布従うと仮定し、モデル化する。
つまり、事前分布$p_{\Theta}$と尤度$p_{X \| \Theta}$, 観測値$(x_{1}, \ldots, x_{N})$をgivenとし、以下の問題を解く。

$$
\begin{eqnarray}
    \theta^{*} 
    & := &
        \argmax_{\theta}
            p_{\Theta | (X_{1}, \ldots, X_{N})}(\theta | (x_{1}, \ldots, x_{N}))
    \nonumber
    \\
    & = &
        \argmax_{\theta}
        \left(
            \prod_{i=1}^{N} p_{X | \Theta}(x_{i} | \theta)
        \right)
        \frac{
            p_{\Theta}(\theta)
        }{
            p_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})
        }
    \nonumber
    \\
    & = &
        \argmax_{\theta}
        \left(
            \prod_{i=1}^{N} p_{X | \Theta}(x_{i} | \theta)
        \right)
        \frac{
            p_{\Theta}(\theta)
        }{
            \int 
                p_{X_{1}, \ldots, X_{N} \mid \Theta}(x_{1}, \ldots, x_{N} \mid \theta) 
                    p_{\Theta}(\theta) 
            \ d \theta
        }
    \nonumber
\end{eqnarray}
$$

$x_{1}, \ldots, x_{N}$は観測値として与えられていることを踏まえれば、$\theta$の関数として最大化問題をとけば良い。

### Prediction

一度$\theta^{*}$が求まれば、 $$p_{X_{N+1} \mid \Theta}(x_{N+1} \mid \theta^{*})$$ を用いて予測を行う。

## Bayesian Estimation
ベイズ推定では、予測に使う分布を先に考える。（下記Prediction）
具体的な$\theta$の値が必要な場合は、予測分布の

### Determination of $\theta$
Bayes推定では、予測に用いる分布に$\theta$を含めない。
よって、$\Theta$は直接求めることはせず、事後分布$p_{\Theta | X_{1}, \ldots, X_{N}}$のみ考える。
具体的な$\Theta$の値が必要な場合は、以下の期待値を用いることが多い。

$$
    \theta^{\mathrm{Bayes}} 
    :=
    \int_{A_{\theta}}
        \theta
            p_{\Theta | X_{1}, \ldots, X_{N}}(\theta | x_{1}, \ldots, x_{N})
    \ d\theta
$$

### Prediction
Bayes推定では、予測の分布として$p_{X_{N+1} | X_{1}, \ldots, X_{N}}(x_{N+1} | x_{1}, \ldots, x_{N})$を考える。
この分布をBayexの予測分布(predictive distribution)という。
bayesの予測分布は、サンプルの確率変数$X_{1}, \ldots, X_{N+1}$が$\theta$について条件付き独立であることを仮定すれば積分によって表現できる。
つまり、以下を仮定する。

$$
    p_{X_{1} | \Theta} \times \cdots \times p_{X_{N+1} | \Theta} 
    =
    p_{X_{1}, \ldots, X_{N+1} | \Theta},
$$

このとき、$A_{\Theta}$が$\Theta$の値域全体とすると以下が成り立つ。

$$
\begin{eqnarray}
    p_{X_{N+1} | X_{1}, \ldots, X_{N}}(x | x_{1}, \ldots, x_{N})
    & = &
        \int_{A_{\Theta}}
            p_{X_{N+1} | \Theta}(x | \theta)
                p_{\Theta | X_{1}, \ldots, X_{N}}(\theta | x_{1}, \ldots, x_{N})
        \ d\theta
    \nonumber
\end{eqnarray}
$$

実際、

$$
\begin{eqnarray}
    \int_{A_{\Theta}}
        p_{X_{N+1} | \Theta}(x_{N+1} | \theta) 
        p_{\Theta | X_{1}, \ldots, X_{N}}(\theta | x_{1}, \ldots, x_{N})
    \ d\theta
    & = &
        \int_{A_{\Theta}}
            p_{X_{N+1} | \Theta}(x_{N+1} | \theta) 
            \frac{
                p_{\Theta, X_{1}, \ldots, X_{N}}(\theta, x_{1}, \ldots, x_{N})
            }{
                p_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})
            }
        \ d\theta
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            p_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})
        }
        \int_{A_{\Theta}}
            p_{X_{N+1} | \Theta}(x_{N+1} | \theta) 
            p_{X_{1}, \ldots, X_{N} | \Theta}(x_{1}, \ldots, x_{N} | \theta)
            p_{\Theta}(\theta)
        \ d\theta
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            p_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})
        }
        \int_{A_{\Theta}}
            p_{X_{1}, \ldots, X_{N}, X_{N+1} | \Theta}(x_{1}, \ldots, x_{N}, x_{N+1} | \theta)
            p_{\Theta}(\theta)
        \ d\theta
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            p_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})
        }
        \int_{A_{\Theta}}
            p_{X_{1}, \ldots, X_{N}, X_{N+1}, \Theta}(x_{1}, \ldots, x_{N}, x_{N+1}, \theta)
        \ d\theta
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            p_{X_{1}, \ldots, X_{N}}(x_{1}, \ldots, x_{N})
        }
        p_{X_{1}, \ldots, X_{N}, X_{N+1}}(x_{1}, \ldots, x_{N}, x_{N+1})
    \nonumber
\end{eqnarray}
$$

となり、左辺に等しい。
ここで、2つめの等号から3つ目の等号で、条件付き独立性を使っていることに注意する。

## Example of Bayesian Framework
bayesを利用した機械学習の例を示す。
回帰の問題を考える。
$(Y, Z)$が2次元の確率変数とし、$Y$を独立変数とし、従属変数$Z$を求める回帰の問題を考える。

* $(Y_{1}, Z_{1}), \ldots, (Y_{N}, Z_{N})$
    * $(Y, Z)$のi.i.dサンプルとして得られているとする。
    * $X := (Y, Z)$で$m=2$次元の観測データ
* $(y_{1}, z_{1}), \ldots, (y_{N}, z_{N})$
    * $(Y_{1}, Z_{1}), \ldots, (Y_{N}, Z_{N})$の実現値
    * 観測された$N$個のデータの組
* $\beta > 0$は定数

ここで、尤度関数が$$p_{(Y, Z) \mid \Theta}$$で

## Bayesian optimization
$B \subset \mathbb{R}^{d}$とし、$d \in \mathbb{N}$とする。
ベイズ最適化とは、未知の関数$f: B \rightarrow \mathbb{R}$を与えられた$N$個のデータの組$(a_{i}, f(a_{i}))_{i=1,\ldots, N}$から$f$の$A$上の最大値を探す方法の1つである。
つまり、$f$を未知の関数として、以下を求める。

$$
    a^{*} := \arg\max_{a \in A} f(a).
$$

ベイズ最適化では、各パラメータを以下のように考える。

* $f$
    * 確率過程
    * ガウス過程を考えることが一般的
* $a_{1}, \ldots, a_{N}$
    * 確率過程の位置
    * 確率変数でない？
* $y_{i} := f(a_{i})(\omega)$
    * 観測されたデータ$a_{i}$での値$y_{i}$の組が観測されている

以上の設定のもと次の分布をベイズ最適化の予測分布として定義する。

$$
\begin{equation}
    p_{f(a_{N+1}) \mid (f(a_{1})), \ldots, f(a_{N}))}
    \quad
    \forall a_{N+1} \in B
    \label{baysian_optimization_predictive_distribuiton}
\end{equation}
$$

以下では、$f$がガウス過程に従うとして、ベイズ最適化を考える。

$f:\Omega \times B \rightarrow \mathbb{R}$がガウス過程に従うとする。
特に、平均$\mathrm{E}(f(a))$と分散$\mathrm{Var}(f(a))$が$a$の関数で以下のようにかけると仮定する。
つまり、$\forall M \in \mathbb{N}$について、$$\mathbf{a}_{M} := (\tilde{a}_{1}, \ldots, \tilde{a}_{M}) \in B^{M}$$とすると

$$
    (f(\tilde{a}_{1}), \ldots, f(\tilde{a}_{M}))
        \sim \mathcal{N}^{M}(\mu_{M}(\mathbf{a}_{M}), \sigma_{M}(\mathbf{a}_{M}, \mathbf{a}_{M})),
$$

ここで、$\mu(a)$は平均を表す関数で$\mu_{M}:B^{M} \rightarrow \mathbb{R}^{M}$、$\sigma_{M}(\cdot, \cdot)$は共分散を表す関数$\sigma:B \times B \rightarrow \mathbb{R}_{\ge 0}$で、特に以下のようにかけるとする。

$$
\begin{eqnarray}
    \mu_{M}(\mathbf{a}_{M})
        & := &
        \left(
            \begin{array}{c}
                \mu_{M}^{1}(a_{1}) \\
                \mu_{M}^{2}(a_{2}) \\
                \vdots \\
                \mu_{M}^{M}(a_{M}) 
            \end{array}
        \right),
    \\
    \sigma_{M}(\mathbf{a}_{M}, \mathbf{a}_{M})
        & := &
        \left(
            \begin{array}{cccc}
                k(a_{1}, a_{1}) & k(a_{1}, a_{2}) & \ldots & k(a_{1}, a_{M}) \\
                k(a_{2}, a_{1}) & k(a_{2}, a_{2}) & \ldots & k(a_{2}, a_{M}) \\
                \vdots &  & \ddots & \vdots \\
                k(a_{M}, a_{1}) & k(a_{M}, a_{2}) & \ldots & k(a_{M}, a_{M})
            \end{array}
        \right)
\end{eqnarray}
$$

ここで、$k:B \times B \rightarrow \mathbb{R}$の関数である。
$M=1$の場合は、$f(a)$は各$a$について1次元のガウス分布に従っていることに注意する。
つまり、

$$
\begin{equation}
    f(\tilde{a})
        \sim \mathcal{N}(\mu(\tilde{a}), \sigma(\tilde{a}, \tilde{a})),
\end{equation}
$$

である。

以上の仮定より、ベイズ最適化の予測分布$$\eqref{baysian_optimization_predictive_distribuiton}$$は、$N$次の正規分布$(f(a_{1}), \ldots, f(a_{N}))$で条件付けられた正規分布となることがわかる。
正規分布の条件付き分布の性質より、 予測分布は以下の形でかける。

$$
\begin{eqnarray}
    p_{f(a_{N+1}) \mid (f(a_{1})), \ldots, f(a_{N}))}(y_{N+1} \mid y_{1}, \ldots, y_{N+1})
        & = &
            \Phi(a_{N+1}; \mu(y_{N+1}; y_{1}, \ldots, y_{N}), \sigma(y_{N+1}, y_{N+1}; y_{1}, \ldots, y_{N})
    \\
    \mu(y_{N+1}; y_{1}, \ldots, y_{N})
        & = & \mu_{2} + k^{\mathrm{T}}K^{-1}(y - \mu_{1})
    \\
    \sigma(y_{N+1}, y_{N+1}; y_{1}, \ldots, y_{N})
        & = &
            k(a_{N+1}, a_{N+1}) - k^{\mathrm{T}}K^{-1}k
\end{eqnarray}
$$

ここで、$\Phi(a; \mu, \sigma)$は平均$\mu$で分散$\sigma$の正規分布関数で、

$$
\begin{eqnarray}
    \left(
        \begin{array}{c}
            f(a_{1}) \\
            f(a_{2}) \\
            \vdots \\
            f(a_{N}) \\
            f(a_{N+1})
        \end{array}
    \right)
        & \sim &
            \mathcal{N}^{N+1}(\mu_{N+1}(\mathbf{a}_{N+1}), \sigma_{N+1}(\mathbf{a}_{N+1}, \mathbf{a}_{N+1}))
    \\
    \mu_{N+1}(\mathbf{a}_{N+1})
        & := &
        \left(
            \begin{array}{c}
                \mu_{1} \\
                \mu_{2}
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                \left(
                    \begin{array}{c}
                        \mu_{N+1}^{1}(a_{1}) \\
                        \mu_{N+1}^{2}(a_{2}) \\
                        \vdots \\
                        \mu_{N+1}^{N}(a_{N}) 
                    \end{array}
                \right) \\
                \mu_{N+1}^{N+1}(a_{N+1}) 
            \end{array}
        \right)
    \\
    \sigma_{M}(\mathbf{a}_{M}, \mathbf{a}_{M})
        & := &
            \left(
                \begin{array}{cccc}
                    K & k \\
                    k^{\mathrm{T}} & k(a_{N+1}, a_{N+1})
                \end{array}
            \right)
        \nonumber
        \\
        & = &
            \left(
                \begin{array}{cccc}
                    \left(
                        \begin{array}{cccc}
                            k(a_{1}, a_{1}) & k(a_{1}, a_{2}) & \ldots & k(a_{1}, a_{N}) \\
                            k(a_{2}, a_{1}) & k(a_{2}, a_{2}) & \ldots & k(a_{2}, a_{N}) \\
                            \vdots &  & \ddots & \vdots \\
                            k(a_{N}, a_{1}) & k(a_{N}, a_{2}) & \ldots & k(a_{N}, a_{N}) \\
                        \end{array}
                    \right)
                    &
                    \left(
                        \begin{array}{c}
                            k(a_{1}, a_{N+1}) \\
                            k(a_{2}, a_{N+1}) \\
                            \vdots \\
                            k(a_{N}, a_{N+1}) \\
                        \end{array}
                    \right)
                    \\
                    \left(
                        \begin{array}{cccc}
                            k(a_{N+1}, a_{1}) & k(a_{N+1}, a_{2}) & \ldots & k(a_{N+1}, a_{N})
                        \end{array}
                    \right)
                    &
                    k(a_{N+1}, a_{N+1})
                \end{array}
            \right)
            \nonumber
\end{eqnarray}
$$

である。

# Reference
* [ベイズ推定 - 機械学習の「朱鷺の杜Wiki」](http://ibisforest.org/index.php?%E3%83%99%E3%82%A4%E3%82%BA%E6%8E%A8%E5%AE%9A)
* [MAP推定 - 機械学習の「朱鷺の杜Wiki」](http://ibisforest.org/index.php?MAP%E6%8E%A8%E5%AE%9A)
