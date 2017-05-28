---
title: Chapter4. Unbiasedness Theory and First Applications
book_title: Testing Statistical Hypotheses
book_chapter: 4
---

## 4.1 Unbiasedness For Hypothesis Testing

* $\Theta \subseteq \mathbb{R}^{p}$,
* $$\Theta_{H}, \Theta_{K}$$,
    * $$\Theta_{H} \cup \Theta_{K} = \Theta$$,


### Definition. Unbiased
* $\phi: \mathcal{X} \rightarrow [0, 1]$
    * 検定
* $\alpha \in [0, 1]$

検定が水準$\alpha$の不偏検定であるとは、

$$
\begin{eqnarray}
    \beta_{\phi}(\theta) \le \alpha,
    & &
        \theta \in \Theta_{H}
    \nonumber
    \\
    \beta_{\phi}(\theta) \ge \alpha,
    & &
        \theta \in \Theta_{K}
    \label{chap04_04_01_unbiasesed_test}
\end{eqnarray}
$$

満たすことをいう。
第一式は、Error of the first kindである。
第二式は、powerである。
また、水準$\alpha$の検定は定義より第一式を満たす。

<div class="end-of-statement" style="text-align: right">■</div>

### Remarks
検定におけるRisk function $$R(\theta, \delta_{\phi})$$

$$
\begin{equation}
    R(\theta, \delta_{\phi})
    =
        \begin{cases}	
            \mathrm{E}_{\theta}
            \left[
                \phi
            \right]
            &
                (\theta \in \Theta_{H})
            \\
            1
            -
            \mathrm{E}_{\theta}
            \left[
                \phi
            \right]
            &
                (\theta \in \Theta_{K}) 
        \end{cases}
    \nonumber
\end{equation}
$$

であった。
検定が不偏検定であれば、riskの意味では

$$
\begin{eqnarray}
    R(\theta, \delta_{\phi})
    & \le &
        \alpha,
        \quad
        (\theta \in \Theta_{H}) 
    \nonumber
    \\
    R(\theta, \delta_{\phi})
    & \le &
        1 - \alpha,
        \quad
        (\theta \in \Theta_{K}) 
    \nonumber
\end{eqnarray}
$$

となる。

また、$\forall \phi$について、$\beta_{\phi}$が$\theta$について連続で、$$\Theta_{H}^{f} \cap \Theta_{K}^{f} \neq \emptyset$$(これは、$$\Theta_{K}, \Theta_{H}$$が$$\Theta$$の分割であれば、成り立つ)とすれば

$$
\begin{equation}
    \beta_{\phi}(\theta)
    =
    \alpha,
    \
    \forall \theta \in \Theta_{H}^{f} \cap \Theta_{K}^{f},
    \
    \label{chap04_04_02_similar_on_boundary}
\end{equation}
$$

ただし、$$\Theta_{H}^{f}, \Theta_{K}^{f}$$は$$\Theta_{H}, \Theta_{K}$$の境界である。
実際、$$\Theta_{H} = (\Theta_{K})^{c}$$より、$$\forall \theta \in \Theta_{H}^{f}$$について、

$$
    \{\theta_{H, i}\}_{i \in \mathbb{N}} \subset \Theta_{H}, 
    \
    \{\theta_{K, i}\}_{i \in \mathbb{N}} \subset \Theta_{K}, 
    \
    \theta_{H, i} \rightarrow \theta,
    \
    \theta_{K, i} \rightarrow \theta,
$$

がとれる。
よって、

$$
\begin{eqnarray}
    \beta_{\phi}(\theta_{H, i}) \le \alpha
    & \rightarrow &
        \beta_{\phi}(\theta) \le \alpha
    \nonumber
    \\
    \beta_{\phi}(\theta_{K, i}) \ge \alpha
    & \rightarrow &
        \beta_{\phi}(\theta) \ge \alpha
    \nonumber
\end{eqnarray}
$$

よりOK。

<div class="end-of-statement" style="text-align: right">■</div>

### Definitions. similar
* $$\Theta^{\prime} \subset \Theta$$,
* $c \in [0, 1]$

以下を満たす時、検定$\phi$は$\Theta^{\prime}$上、similar（相似）という。

$$
    \forall \theta \in \Theta^{\prime},
    \
    E_{\theta}[\phi]
    =
    c
$$

<div class="end-of-statement" style="text-align: right">■</div>

不偏検定は境界上相似である。
一方、相似検定を考えた時に、不偏検定となるようにできるか？
次の定理から、境界上相似なUMP testは、不偏検定となることが分かる。

### Lemma 4.1.1
* $\beta_{\phi}$
    * $\theta \in \Theta$について、連続
* $\alpha \in [0, 1]$
* $\phi_{0}$
    * $$\eqref{chap04_04_02_similar_on_boundary}$$を満たすtestに対するUMP test
    * 水準$\alpha$のtest

このとき、$\phi_{0}$はUMP不偏検定である。

### proof.
まず、$\phi_{0}$は水準$\alpha$の検定であるから、定義より、

$$
    \forall \theta \in \Theta_{H},
    \
    \beta_{\phi}(\theta)
    \le
    \alpha
$$


$\phi \equiv \alpha$も$$\eqref{chap04_04_02_similar_on_boundary}$$を満たすから、$\phi_{0}$がUMP testより、

$$
    \forall \theta \in \Theta_{K},
    \
    \alpha
    =
    \beta_{\phi}(\theta)
    \le
    \beta_{\phi_{0}}(\theta)
$$



<div class="QED" style="text-align: right">$\Box$</div>

このことから、相似検定のみを考えれば良いことになる。

## 4.2 One-Parameter Exponential Families

### Definition. Exponential familiy
* $\Theta \subset \mathbb{R}^{m}$, 
* $$\mathcal{P} := \{P_{\theta}\}_{\theta \in \Theta}$$,
* $$\theta = (\theta_{1}, \ldots, \theta_{m}) \in \Theta$$,
* $g: \mathcal{X} \rightarrow \mathbb{R}$
    * 可測関数
* $T_{i}: \mathcal{X} \rightarrow \mathbb{R}$
    * 可測関数
* $\psi:\Theta \rightarrow \mathbb{R}$
    * 実数値関数
* $a_{i}:\Theta \rightarrow \mathbb{R}$
    * 実数値関数

$\mathcal{P}$が以下を満たす時、$\mathcal{P}$を指数型分布族という。

$$
    \theta \in \Theta,
    \
    \frac{
        P_{\theta}
    }{
        d \mu
    }
    =
    \exp
    \left(
        \sum_{i=1}^{m}
            a(\theta)_{i}
            T(x)
            -
            \phi(\theta)
    \right)
    g(x)
$$

<div class="end-of-statement" style="text-align: right">■</div>

以下では、指数型分布族の中で、$m = 1$で$$a_{i}$$を恒等写像で、$\phi(\theta) = -\log(C(\theta))$の場合を考える。
また、記法を本に合わせるために、$h=g$として書く。
つまり、

$$
    \theta \in \Theta,
    \
    \frac{
        P_{\theta}
    }{
        d \mu
    }
    =
    C(\theta)
    \exp
    \left(
        \theta
        T(x)
    \right)
    h(x)
$$

* case1
    * Corollary 3.4.1
    * $$H: \theta \le \theta_{0}$$,
    * $$K: \theta > \theta_{0}$$,
* case2: $$\theta_{1} < \theta_{2}$$,
    * Theorem 3.7.1
    * $H$: $$\theta \le \theta_{1}$$ or $$\theta \ge \theta_{2}$$,
    * $$K: \theta_{1} < \theta < \theta_{2}$$,
* case3: $$\theta_{1} < \theta_{2}$$,
    * $$H: \theta_{1} \le \theta \le \theta_{2}$$,
    * $K$: $$\theta < \theta_{1}$$ or $$\theta > \theta_{2}$$,

ここでは、case3の場合にUMP unbiased testがあることを示す。
このとき、test $\phi$は

$$
\begin{equation}
    \phi(x)
    :=
    \begin{cases}	
        1
        &
            T(x) < C_{1} \text{ or } T(x) > C_{2}
            \\
        \gamma_{i}
        &  
            T(x) = C_{1} \text{ or } T(x) = C_{2}
            \\
        0
        &  
            C_{1} < T(x) < C_{2}
            \\
    \end{cases}
    \label{chap04_04_03_test}
\end{equation}
$$

$\gamma_{i}$と$$C_{i}$$は以下を満たすようにきめる。

$$
\begin{equation}
    \mathrm{E}_{\theta_{1}}
    \left[
        \phi(X)
    \right]
    =
    \mathrm{E}_{\theta_{2}}
    \left[
        \phi(X)
    \right]
    =
    \alpha
    \label{chap04_04_04}
\end{equation}
$$


