---
layout: math
title: Interest Rate Modeling 3
---

# TOC

<!-- vim-markdown-toc GFM -->

* [Interest Rate Modeling 3](#interest-rate-modeling-3)
	* [Symbols](#symbols)
	* [16.3 Terminal Swap Rate Models](#163-terminal-swap-rate-models)
		* [16.3.4 Swap-Yield TSR Model](#1634-swap-yield-tsr-model)
	* [16.4 Libor-in-Arrears](#164-libor-in-arrears)
	* [16.6 CMS and CMS-Linked Cash Flows](#166-cms-and-cms-linked-cash-flows)
		* [16.6.1 The replication Method for CMS](#1661-the-replication-method-for-cms)
		* [16.6.2 Annuity Mapping Function as a Conditional Expected Value](#1662-annuity-mapping-function-as-a-conditional-expected-value)
			* [Proposition 16.6.1](#proposition-1661)
			* [Proposition 16.6.2](#proposition-1662)
			* [sketch of proof](#sketch-of-proof)
		* [16.6.3 Swap-Yield TSR Model](#1663-swap-yield-tsr-model)
		* [16.6.4 Linear and Other TSR Models](#1664-linear-and-other-tsr-models)
		* [16.6.5 The Quasi-Gaussian Model](#1665-the-quasi-gaussian-model)
		* [16.6.6 The Libor Market Model](#1666-the-libor-market-model)

<!-- vim-markdown-toc -->

# Interest Rate Modeling 3

## Symbols

* $0 = T_{0} < T_{1} < \ldots < T_{N}$
* $\tau_{n} := T_{n+1} - T_{n}$
* $A_{n, m}(t)$
* $A(T)$: annuity, PVBP

$$
    A(t) 
        := A_{0, N}(t) 
        = \sum_{n=0}^{N-1} \tau_{n}P(t, T_{n+1})
$$

* $p(t, S; T, K)$: $t$での満期$T$, forward $S$, strike $K$のput optionの(non-deflated)価格。
* $c(t, S; T, K)$: $t$での満期$T$, forward $S$, strike $K$のcall optionの(non-deflated)価格。
* $q(M)$: 次を満たす添字$0, \ldots, N$, $M \in [T_{q(M)}, T_{q(M)})$。
    ただし、$T_{N+1} = \infty$
    * index function

## 16.3 Terminal Swap Rate Models
* $0 < T = T_{0} < T_{1} < \ldots < T_{N}, \tau_{n} := T_{n+1} - T_{n}$

TSR modelでは、以下のように$P(T, M)$をmodel化する。

$$
    P(T, M) = \pi(S(T), M),\ M \ge T
$$

ここでで、$\pi$は

### 16.3.4 Swap-Yield TSR Model
coupon bond yield forumlaから考え出されたTSR model。


## 16.4 Libor-in-Arrears


現実的には、無限のoptionを扱えないことを考慮すると、static hedgeの積分は以下のように離散化できる。

$$
    E^{M}(L(T)^{2}) 
        \approx L(0)^{2} + \sum_{i} w_{i}^{p}p(0, L(0); T, K_{i}) + \sum_{i} w_{i}^{c}c(0, L(0); T, K_{i})
$$

特に、$(x_{\min}, x_{\max})$の範囲が与えられたとき、すべての$x \in (x_{\min}, x_{\max})$に対してsuper-replicationになるように選ぶことができる。

$$
    \sum_{i} \bar{w}_{i}^{p} p(T, x; T, K_{i}) + \sum_{i} \bar{w}_{i}^{c} c(T, x; T, K_{i})
    \ge 2 \int_{-\infty}^{L(0)} p(T, x; T, K)\ d K    
        + 2 \int_{L(0)}^{\infty} c(T, x; T, K)\ dK = x^{2} - L(0)^{2}
$$

同様にsub-replicationとなるように選ぶことができる。

$$
    \sum_{i} \underline{w}_{i}^{p} p(T, x; T, K_{i}) 
        + \sum_{i} \underline{w}_{i}^{c} c(T, x; T, K_{i})
    \le 2 \int_{-\infty}^{L(0)} p(T, x; T, K)\ d K    
        + 2 \int_{L(0)}^{\infty} c(T, x; T, K)\ dK = x^{2} - L(0)^{2}
$$

$\bar{w}$と$\underline{w}$は離散化した被積分関数の上端と下端をとれば良い？

* super-replicationの最小値はlong LIAのupper bound
* sub-replicationの最大値はshort LIAのlower bound
* boundから外れたものはマーケットの商品でarbitrageが可能

## 16.6 CMS and CMS-Linked Cash Flows
* LIBOR In Arrears(LIA)や LIBOR with dealyの考え方は、CMSやCMS linked cash flowsのモデルを考えるのに重要な知見を与えてくれる
* CMSはswap rate$S(T)$を$T_{p} \ge T$に支払うもの(典型的には、$T_{p} \le T_{1}$
    * ここで$T_{1}$は参照しているswapの最初の支払日
* CMS-linked cash flowは$S(T)$の関数を支払いとするもの

* LIAからの類推として、swap measure$Q^{A}$の下での、market impliedな$S(T)$の分布はeuropean swaptionからわかっている。


$$
\begin{equation}
    V_{\mathrm{CMS}}(0) 
        := A(0) E^{A}
            \left(
                \frac{P(T, T_{p})}{A(T)}S(T) 
            \right)
        = P(0, T_{p}) E^{T_{p}}
            \left(
                S(T) 
            \right)
            \label{value_cms}
\end{equation}
$$

CMSのconvexity ajustment$D_{\mathrm{CMS}}$を以下で定義する。

$$
\begin{equation}
    D_{\mathrm{CMS}}(0) 
        := E^{T_{p}}(S(T)) - S(0)
        = \frac{V_\mathrm{CMS}}{P(0, T_{p})} - S(0)
        = \frac{A(0)}{P(0, T_{p})} E^{A}
            \left(
                \frac{P(T, T_{p})}{A(T)}S(T)
            \right) - S(0)
    \label{chap16_cms_convexity_ajustment}
\end{equation}
$$

* Sec16.5のLibor-with-delayの議論はCMSに適用できる。
* $\eqref{value_cms}$はTerm structure modelで計算できるが、計算が遅く、精度も悪い
* replicatoin methodの方が大抵better
    * そのためには$P(T, T_{p}) / A(T)$が$S(T)$の関数としてかける必要がある。
    * LIAやLibor-with-delayですでにやった

### 16.6.1 The replication Method for CMS
$P(T, T_{p})/A(T)$を$S(T)$の関数としてモデル化するために、$S(T)$から$P(T, T_{p})/A(T)$への関数を$\alpha(S(T))$をannuity mapping functionとして定義する。
つまり、

$$
\begin{equation}
    E^{A}
    \left(
        \frac{P(T, T_{p})}{A(T)}S(T)
    \right)
    = E^{A}
    \left(
        \alpha(S(T))S(T)
    \right)
    \label{chap16_value_cms_annuity_mapping_fucntion}
\end{equation}
$$

が成り立つとする。
Proposition 8.4.13をpayoffが$f(S(T)) = \alpha(S(T))S(T), K^{*}=S(0)$として、適用する。
$f'(S) = \alpha'(S)S + \alpha(S)$より、

$$
\begin{eqnarray}
    E^{A}(\alpha(S(T))S(T))
        & = &
            S(0) \alpha(S(0))
            + (\alpha'(S(0))S(0) + \alpha(S(0)))(S(0) - S(0))
            + \int_{-\infty}^{(0)} w(K)p(0, S(0); T, K)\ dK
            + \int_{S(0)}^{\infty} w(K)c(0, S(0); T, K\ dK
            \\
        & = & 
            S(0) \alpha(S(0))
            + \int_{-\infty}^{(0)} w(K)p(0, S(0); T, K)\ dK
            + \int_{S(0)}^{\infty} w(K)c(0, S(0); T, K\ dK
    \label{chap16_expectation_static_hedge}
\end{eqnarray}

$$

ここで、

$$
    w(s) := \frac{d^{2}}{ds^{2}}(\alpha(s)s)
$$

である。
$\eqref{chap16_expectation_static_hedge}$, $\eqref{chap16_value_cms_annuity_mapping_fucntion}$より、以下を得る。

$$
\begin{eqnarray}
    V_{\mathrm{CMS}}
        & = &  A(0)S(0) \alpha(S(0))
            + \int_{-\infty}^{S(0)} w(K)A(0)p(0, S(0); T, K)\ dK
            + \int_{S(0)}^{\infty} w(K)A(0)c(0, S(0); T, K)\ dK \\
        & = &  A(0)S(0) \alpha(S(0))
            + \int_{-\infty}^{S(0)} w(K)V_{\mathrm{rec}}(0, K)\ dK
            + \int_{S(0)}^{\infty} w(K)V_{\mathrm{pay}}(0, K)\ dK 
        \label{chap16_value_cms_static_hedge}
\end{eqnarray}
$$

ここで、$V_{\mathrm{rec}}, V_{\mathrm{pay}}$はそれぞれreciever/payer european swaptionの価格をあわらし、

$$
\begin{eqnarray*}
    V_{\mathrm{rec}}(0, K) 
        & = & A(0)p(0, S(0); T, K) = A(0) E[(K - S(T))^{+}]
    V_{\mathrm{pay}}(0, K) 
        & = & A(0)c(0, S(0); T, K) = A(0) E[(S(T) - K)^{+}]
\end{eqnarray*}
$$

である。
swaptionの価格は、marketの価格を直接に使うか選択したmodelで直接計算される。
replicatoin methodはmarketのすべてのstrikesのswaptionの価格と一貫したCMSの価格を計算するだけでなく、modelに依存しない($\alpha(s)$には依存する）payer/recieverのswaptionのポートフォリオを提供する。

$\eqref{chap16_value_cms_static_hedge}$に対して、いくつかの制約をいれることができる。
例えば、low strikeやhigh stirkeのswaptionは流動性が低いので、以下のように

$$
    A(0)S(0) \alpha(S(0))
        + \int_{K_{\min}}^{S(0)} w(K)V_{\mathrm{rec}}(0, K)\ dK
        + \int_{S(0)}^{K_{\max}} w(K)V_{\mathrm{pay}}(0, K)\ dK, 
    \label{chap16_value_cms_static_hedge_low_liquid}
$$

strikeに上限と下限をつけた形にもできる。
strikeが有限個の場合のrepliationについては、Sec16.4で議論をしている。

replication methodは、$g(S(T))$をpayoffに持ち、$T_{p} \ge T$にも支払いがある場合に拡張できる。
ただし、$g$は十分なめらかであるとする。
例えば、payoffとして、capletとfloorletの場合は以下のようになる。

$$
    g(s) := g_{\mathrm{caplet}}(s) := (s - K)^{+},
    \quad g(s) := g_{\mathrm{floorlet}}(s) := (K - s)^{+}
$$

この時、CMSの価格は以下のようにかける。

$$
    V_{\mathrm{gCMS}}(0) 
        := A(0) E^{A}
            \left[
                \frac{P(T, T_{p})}{A(T)} g(S)
            \right]
        = A(0) E^{A} [\alpha(S(T))g(S(T))] 
$$

また、weightは

$$
    w(s) := \frac{d^{2}}{ds^{2}} (\alpha(s)g(s)),
$$

となる。
financeで現れる多くのpayoff関数は、二階微分をするとdelta関数を含む。
capletとfloorletの場合は、delta関数が集中する点$s_{0}$での$V_{\mathrm{rec}}(0, s_{0})$ないし、$V_{\mathrm{pay}}(0, s_{0})$ (どちらを考慮するかは$s_{0}$と$K$の値による) の値の寄与を考えれば良い。

### 16.6.2 Annuity Mapping Function as a Conditional Expected Value
$\alpha(s)$を前節で導入したが、$\alpha(s)$を何とするかについては議論しなかった。
前節までで議論したTerminal Swap Rate modelsやTerm structure modelによる近似の例が参考になると期待できる。
まずはじめに、annuity mapping functionの理論的な意味についてみる。

$$
\begin{eqnarray*}
    V_{\mathrm{CMS}}
        & = & 
            A(0) E^{A}
                \left[
                    \frac{P(T, T_{p})}{A(T)} S(T) 
                \right] \\
       & = & 
            A(0) E^{A}
                \left[
                    E^{A} 
                    \left( 
                    \left.
                        \frac{P(T, T_{p})}{A(T)} S(T) 
                    \right|
                        S(T)
                    \right)
                \right] \\
       & = & 
            A(0) E^{A}
                \left[
                    S(T)
                    E^{A} 
                    \left( 
                    \left.
                        \frac{P(T, T_{p})}{A(T)}
                    \right|
                        S(T)
                    \right)
                \right] \\
\end{eqnarray*}
$$

これを、 $\eqref{chap16_value_cms_annuity_mapping_fucntion}$と比較する。


#### Proposition 16.6.1
annuity mapping function $\alpha(s)$は、modelに依存せず以下の条件付き期待値ととしてかくことができる。

$$
\begin{equation}
    \alpha(s) 
        = E
        \left[
        \left.
            \frac{P(T, T_{p})}{A(T)}
        \right|
            S(T) = s
        \right]
        \label{chap16_annutiy_mapping_function_as_conditional_expectation}
\end{equation}
$$


propositionから今までみてきた近似は、 $\eqref{chap16_annutiy_mapping_function_as_conditional_expectation}$で定義される条件つき期待値の近似と見ることができる。
前節までに見てきた方法の他に、条件付き期待値を直接近似する方法を考えることができる。
条件付き期待値は、確率変数$X, Y$について、$X$の$Y$での条件付き期待値は、$\sigma(Y) = \sigma(\{f(Y)) \mid f \in \mathcal{B} \})$を満たす関数全体を$\mathcal{B}$とすると、

$$
    E(X|Y) = f^{*}(Y), 
    f^{*} = \mathrm{argmin} \left\{
        E \left(
            (X - f(Y))^{2}, f \in \mathcal{B}
        \right)
    \right\}
$$

である。
条件付き期待値の近似として$\mathcal{B}$をsubspace $\tilde{\mathcal{B}} \subset \mathcal{B}$ として近似する方法がある。
つまり、

$$
    E(X|Y) \approx f^{*}(Y),
    f^{*} = \mathrm{argmin} \left\{
       E
       \left(
           (X - f(Y))^{2}, f \in \tilde{\mathcal{B}}
       \right)
    \right\}
$$

として、近似する。
$\tilde{\mathcal{B}}$を以下のように$\theta$のparameterでモデル化する。

$$
    \tilde{\mathcal{B}} 
        := { f(y; \theta), \theta \in \Theta }
        , \Theta \subset \mathbb{R}^{d}.
$$

最適値をとるためには、以下の必要条件
満たす必要がある。

$$
    \frac{\partial}{\partial \theta_{i}} 
    E
    \left(
        (X - f(Y;\theta))^{2}
    \right)
    = 0, i = 1, \ldots, d
$$

#### Proposition 16.6.2
確率変数$X, Y$と、parameter付けられた関数の集合$\{ f(y; \theta)\}, \theta \in \Theta \subset \mathbb{R}^{d}$を与える。
このとき$E(X|Y)$の近似は以下で与えられる。

$$
    E(X|Y) \approx f(Y; \theta^{*})
$$

ここで、$\theta^{*}$は

$$
    E
    \left(
        X \frac{\partial f}{\partial \theta_{i}} (Y; \theta)
    \right)
    = E
    \left(
        f(Y; \theta) \frac{\partial f}{\partial \theta_{i}} (Y; \theta)
    \right)
    , i = 1, \ldots, d 
$$

として定義される。

#### sketch of proof
微分と積分の順序交換を認めれば($Xf(Y; \theta) \le  G (\forall \theta)$なる期待値有限の確率変数$G$が存在すれば十分）

$$
    \frac{\partial}{\partial \theta_{i}} 
    E
    \left(
       (X - f(Y; \theta))^{2}
    \right)
    =
    \frac{\partial}{\partial \theta_{i}} 
    E
    \left(
       X^{2} - 2Xf(Y; \theta) + f(Y; \theta)^{2}
    \right)
    =
    \frac{\partial}{\partial \theta_{i}} 
    E
    \left(
       -2Xf(Y; \theta) 
    \right)
    + E
    \left(
       2f(Y; \theta) \frac{\partial}{\partial\theta_{i}}f(Y; \theta)
    \right)
$$

であることと、最適値では1階微分が0でなければならないことより成立

### 16.6.3 Swap-Yield TSR Model
16.3.4でのswap-yield modelを考える。
このModelはswap rateとannuityを結び付けるde-facto standardとなっている。

$q(M)$をindex functionとする。
Sec 16.3 で、$P(T, M)$をSwap rateの関数として、以下のようにModel化した。

$$
    P(T, M)
        = 
        \left(
            \prod_{i=0}^{q(M) - 1} \frac{1}{1 + \tau_{i}S(T)}
        \right)
        \left(
            \frac{1}{1 + \tau_{q(M)}S(T)}
        \right)^{\frac{(M - T_{q(M)})}{\tau_{q(M)}}}
$$

このとき、$q(T_{n+1}) = n$より、

$$
\begin{eqnarray*}
    A(T) 
        & = &
            \sum_{n=0}^{N-1} \tau_{n}P(T, T_{n+1}) \\
        & = &
            \sum_{n=0}^{N-1} \tau_{n} 
            \left(
                \prod_{i=0}^{q(T_{n+1}) - 1} \frac{1}{1 + \tau_{i}S(T)}
            \right)
            \left(
                \frac{1}{1 + \tau_{q(T_{n+1})}S(T)}
            \right)^{\frac{(T_{n+1} - T_{q(T_{n+1})})}{\tau_{q(T_{n+1})}}}
            \\
        & = &
            \sum_{n=0}^{N-1} \tau_{n} 
            \left(
                \prod_{i=0}^{n - 1} \frac{1}{1 + \tau_{i}S(T)}
            \right)
            \left(
                \frac{1}{1 + \tau_{n}S(T)}
            \right)^{\frac{(T_{n+1} - T_{n})}{\tau_{n}}}
            \\
        & = &
            \sum_{n=0}^{N-1} \tau_{n} 
            \left(
                \prod_{i=0}^{n} \frac{1}{1 + \tau_{i}S(T)}
            \right)
            \\
        & = &
            \frac{1}{S(T)}
            \sum_{n=0}^{N-1} 
            \left(
                \prod_{i=0}^{n} \frac{\tau_{n}S(T)}{1 + \tau_{i}S(T)}
            \right)
            \\
        & = &
            \frac{1}{S(T)}
            \sum_{n=0}^{N-1} 
            \left(
                \prod_{i=0}^{n} \frac{-1 + 1 + \tau_{n}S(T)}{1 + \tau_{i}S(T)}
            \right)
            \\
        & = &
            \frac{1}{S(T)}
            \sum_{n=0}^{N-1} 
            \left(
                - \prod_{i=0}^{n} \frac{1}{1 + \tau_{i}S(T)}
                + \prod_{i=0}^{n-1} \frac{1}{1 + \tau_{i}S(T)}
            \right)
            \\
        & = &
            \frac{1}{S(T)}
            \left(
                - \prod_{i=0}^{N-1} \frac{1}{1 + \tau_{i}S(T)}
                + 1
            \right)
\end{eqnarray*}
$$

となる。
最後の等式は、summationの隣り合う項が打ち消し合うことによる。
また、$T_{p} \in [T_{0}, T_{1}]$とすると、同様の議論により、

$$
    P(T, T_{p}) = 
        \left(
            \frac{1}{1 + \tau_{0}S(T)}
        \right)^{(T_{p} - T) / \tau_{0}}
$$

より、

$$
\begin{eqnarray*}
    \alpha(s) 
        & = &
            E^{A}
            \left[
            \left.
                \frac{P(T, T_{p})}{A(T)}
            \right|
                S(T) = s
            \right]
            \\
        & = & 
            s \frac{\frac{1}{1+\tau_{0}s}^{(T_{p} - T)/\tau_{0}}}{1 - \prod_{i=0}^{N-1}\frac{1}{1+\tau_{i}s}}
\end{eqnarray*}
$$

となる。
また、

$$
\begin{eqnarray*}
    P(0, T_{p}) 
        & = &
            \left(
                \frac{1}{1+\tau_{0}S(0)}
            \right)^{T_{p}/\tau_{0}}
            \\
    A(0)
        & = &
        \frac{1}{S(0)}
            \left(
                1 - \prod_{i=0}^{N-1} \frac{1}{1+\tau_{i}S(0)}
            \right)
            \\
    \frac{P(0, T_{p})}{A(0)}
        & = & 
           S(0)
           \frac{
               \frac{1}
               {1+\tau_{0}S(0)}^{T_{p}/\tau_{0}}
           }
           {
               1 - \prod_{i=0}^{N-1}\frac{1}{1+\tau_{i}S(0)}
           }
\end{eqnarray*}
$$

より、以下のマルチンゲール性は成り立たない。
この問題についてはSec 16.6.7で扱う。

$$
    E^{A}(\alpha(S(T)))
    =
    E^{A}
    \left(
        \frac{P(T, T_{p})}{A(T)}
    \right)
    \neq
    \frac{P(0, T_{p})}{A(0)}
$$

### 16.6.4 Linear and Other TSR Models
* 上記のTSR modelの議論は、Sec 16.3で熱方一般のTSR modelに用意に拡張できる
* simpleなlinear TSR modelから扱う


$$
    \alpha(s) := \alpha_{1}s + \alpha_{2}
$$

と定義する。
Sec 16.3では、$\alpha_{1} = a(T_{p}), \alpha_{2} = b(T_{p})$であった。
$\alpha_{1}$は入力として、与えられるものである。
$\alpha_{1}$が与えられると、$\alpha_{2}$は無裁定性を満たすように定義される。
つまり、

$$
    \frac{P(0, T_{p})}{A(0)}
        = E^{A}
            \left[
                \frac{P(T, T_{p})}{A(T)}
            \right]
        = E^{A}
        \left[
            \alpha_{1}S(T) + \alpha_{2}
        \right]
        = \alpha_{1}S(0) + \alpha_{2}
$$

が満たされるように、

$$
\begin{equation}
    \alpha_{2} := \frac{P(0, T_{p})}{A(0)} - \alpha_{1}S(0),
    \label{chap16_linear_tsr_model_def_alpha_2}
\end{equation}

$$

と置く。
以上のもと、CMSの価格は

$$
\begin{eqnarray}
    V_{\mathrm{CMS}}(0)
        & = &
            A(0) E^{A}
            \left[
                (\alpha_{1}S(T) + \alpha_{2})S(T)
            \right]
            \\
        & = & 
            \alpha_{2}A(0)S(0) + A(0) E^{A}
            \left[
                \alpha_{1}S(T)^{2}
            \right]
            \\
        & = &
            P(0, T_{p})S(0) - A(0)\alpha_{1}S(0)^{2} + \alpha_{1}A(0) E^{A}
            \left[
                S(T)^{2}
            \right]
            \\
        & = &
            P(0, T_{p})S(0) + A(0)\alpha_{1}\mathrm{Var}^{A}(S(T))
\end{eqnarray}
$$

となり、convexity ajustmentは $\eqref{chap16_cms_convexity_ajustment}$より、

$$
\begin{equation}
    D_{\mathrm{CMS}}(0) 
        = \frac{V_{\mathrm{CMS}}}{P(0, T_{p})} - S(0)
        = \alpha_{1} \frac{A(0)}{P(0, T_{p})} \mathrm{Var}^{A}
        \left[
            S(T)
        \right]
        \label{chap16_cms_convexity_ajustment_linear_tsr_model}
\end{equation}
$$

となる。
$S(T)$のぶんさんは、選択したModelないし、$(S(T) - S(0))$を積分して計算される。
$\eqref{chap16_cms_convexity_ajustment_linear_tsr_model}$は、LIAの式に似ておりよく使われるモデルである。
しかし、$\alpha$のとり方によっては、discount factorが負になるという問題がある。
Sec 16.3.2で述べたように$\alpha_{1}$は平均回帰的な役割を持つが、これについてはSec 16.6.8で扱う。
大雑把には、$T$のyield curveが十分低い状況（つまり、$S(T)$がゼロに近い状況）を考えることで、

$$
    \frac{P(T, T_{p})}{A(T)} 
        \approx \frac{1}{ \sum_{n=0}^{N-1} \tau_{n} }
$$

が成り立つと期待できる。
$\alpha_{2}$を$\alpha_{2} = E^{A}(\alpha_{1}S(T) + \alpha_{2} | S(T) = 0)$とかくと

$$
\begin{equation}
    \alpha_{2} 
        = \mathrm{E}^{A}
        \left[
        \left.
            \frac{P(T, T_{p})}{A(T)}
        \right|
            S(T) = 0
        \right]
        \approx \frac{1}{ \sum_{n=0}^{N-1} \tau_{n}},
    \alpha_{1} = \frac{1}{A(0)}
        \left(
            \frac{P(0, T_{p})}{A(0)} - \alpha_{2}
        \right)
\end{equation}
$$

とかける。
ここで、第二式は $\eqref{chap16_linear_tsr_model_def_alpha_2}$を使った。
この単純なapproachは、他の方法と比べ低い値になる。
図16.1に比較結果がある。

Proposition 16.6.1との関係について述べる。
$X = P(T, T_{p}), Y = S(T), f(s;\theta) := s\theta_{1} + \theta_{2}$として、Propositoin 16.6.2を適用すると、最適性の条件は

$$
    \frac{\partial }{\partial\theta_{1}} f(Y; \theta)
        = S(T),
    \frac{\partial }{\partial\theta_{2}} f(Y; \theta)
        = 1
$$

より、

$$
\begin{eqnarray*}
    \mathrm{E}^{A}
    \left[
       X \frac{\partial }{\partial\theta_{1}} f(Y; \theta) 
    \right]
        & = & \mathrm{E}^{A}
        \left[
            \frac{P(T, T_{p})}{A(T)} S(T)
        \right],
        \\
    \mathrm{E}^{A}
    \left[
       f(Y; \theta) \frac{\partial }{\partial\theta_{1}} f(Y; \theta) 
    \right]
        & = & \mathrm{E}^{A}
        \left[
            (\theta_{1}S(T) + \theta{2}) S(T)
        \right],
        \\
    \mathrm{E}^{A}
    \left[
       X \frac{\partial }{\partial\theta_{2}} f(Y; \theta) 
    \right]
        & = & \mathrm{E}^{A}
        \left[
            \frac{P(T, T_{p})}{A(T)}
        \right],
        \\
    \left[
       f(Y; \theta) \frac{\partial }{\partial\theta_{2}} f(Y; \theta) 
    \right]
        & = & \mathrm{E}^{A}
        \left[
            (\theta_{1}S(T) + \theta_{2})
        \right],
\end{eqnarray*}
$$

から、

$$
\begin{eqnarray*}
    \mathrm{E}^{A}
        \left[
            \frac{P(T, T_{p})}{A(T)} S(T)
        \right]
        & = & \mathrm{E}^{A}
        \left[
            (\theta_{1}S(T) + \theta{2}) S(T)
        \right],
        \\
    \mathrm{E}^{A}
        \left[
            \frac{P(T, T_{p})}{A(T)}
        \right]
        & = & \mathrm{E}^{A}
        \left[
            (\theta_{1}S(T) + \theta_{2})
        \right],
\end{eqnarray*}
$$

となる。
上の方程式の解は以下で与えれる。

$$
\begin{equation}
    \theta_{1}^{*}
        = \frac{P(0, T_{p})}{A(0)} \frac{D_{\mathrm{CMS}}}
            { 
                \mathrm{Var}^{A}
                \left[
                    S(T)
                \right]
            },
    \theta_{2}^{*}
        = \frac{P(0, T_{p})}{A(0)} - \theta_{1}^{*}S(0).
    \label{chap16_linear_tsr_model_conditional_expectation_solution}
\end{equation}

$$

実際

$$
\begin{eqnarray*}
    V_{\mathrm{CMS}}
        & = & A(0) \mathrm{E}^{A}
        \left[
            \mathrm{E}^{A}
            \left[
            \left.
                \frac{P(T, T_{p})}{A(T)}
            \right|
                S(T)
            \right]
            S(T)
        \right]
        \\
        & = & A(0) \mathrm{E}^{A}
        \left[
            \mathrm{E}^{A} (X | Y )
            S(T)
        \right]
        \\
        & \approx &  A(0) \mathrm{E}^{A}
        \left[
            f(Y; \theta^{*})
            S(T)
        \right]
        \\
        & = & A(0) \mathrm{E}^{A}
        \left[
            \theta_{1}^{*}S(T)^{2} + \theta_{2}^{*}S(T)
        \right]
        \\
        & = & A(0) \theta_{1}^{*} \mathrm{E}^{A}
        \left[
            S(T)^{2}
        \right]
        + A(0) \theta_{2}^{*}S(0)
        \\
        & = & A(0) \theta_{1}^{*} \mathrm{Var}^{A}
        \left[
            S(T)
        \right]
        + A(0) \theta_{1}^{*} S(0)^{2}
        + A(0) \theta_{2}^{*} S(0)
\end{eqnarray*}
$$


TODO


解 $\eqref{chap16_linear_tsr_model_conditional_expectation_solution}$はlinear TSR modelの$\alpha_{1}, \alpha_{2}$と一致する。

CMSのconvexity ajustmentはparameterのあるannuity mappincg functionで一意に決定できる。
これは、流動性のあるCMS swapにcalibrationする場合に重要である。
calibrationしたannuity mapping functionは、より複雑で流動性の低いCMS capやCMS range accrualsの計算に利用される。

linear TSR modelは解析しやすく、 Proposition 16.6.2は、他のexponential TSR modelなどにも同様に利用できる

### 16.6.5 The Quasi-Gaussian Model
auasi-Gaussian(qG)は、Sec16.5.3のLiboar-with-delayで見たように、annuityとswap rateの関係についての直感を与える。
(13.5)で見たように、 quasi-Gaussianのもと、discount bondは

$$
\begin{eqnarray*}
    P(T, M)
        & = & P(T, M, x(T), y(T)), M \ge T,
        \\
    P(T, M, x, y)
        & = &
            \frac{P(0, M)}{P(0, T)}
            \exp
            \left(
                -G(T, M) x - \frac{1}{2}G(T,M)^{2}y
            \right)
\end{eqnarray*}
$$

とかける。
ただし、$x(T), y(T)$は状態変数で、$G(T, M)$は平均回帰のdeterministic functionである。
また、上記のdiscount bondを用いて、annuity$A(T, x, y)$とswap rate$S(T, x, y)$も同様に定義する。

$$
    \bar{y}(T) 
        :=
        \left(
            \left. 
                \frac{\partial S(T, x, y)}{\partial x} 
            \right|_{x = y = 0}
        \right)^{-2}
        \mathrm{Var}^{A}
        \left[
            S(T)
        \right]
$$

$\mathrm{Var}^{A}(S(T))$はreplication methodでmodelと整合的に計算される。
また、$X(T, s)$を$x$に関する$S(T, x, \bar{y}(T))$の逆関数とする。
つまり、

$$
    x = X(T, S(T, x, \bar{y}(T)))
$$

である。
このとき、mapping functionを

$$
\begin{equation}
    \alpha(s) := \frac{P(T, T_{p}, X(T, s), \bar{y}(T)}{A(T, X(T,s), \bar{y}(T)}
\end{equation}
$$

と定義し、 $\eqref{chap16_value_cms_static_hedge}$より、$V_{\mathrm{CMS}}$を計算する。
marketと整合的なCMSの価値を計算するために、replication methodのswaptionの価値は、marketから直接得るか、marketにcalibrationしたvanilla modelを使って計算する。
一方、目的がquasi-Gaussian modelでのCMSのcash flowの価値の解析的近似が目的であるならば、swaptionをquasi-Gaussian modelで直接（Proposition 13.1.10のような近似を使って）計算すべきである。

### 16.6.6 The Libor Market Model
Libor Market Model(LMM)は、forward swap rateとannuityの関係を具体化する別の方法である。
callable CMS range accrualsやCMS spread TARNsのようなexotic optionのLMMの応用に役立つ。
LMMのCMS convexity adjustmentの値がmarketのconvexity ajustmentの値を裏付けることが望まれる。
LMMのCMS adjustmentの値をMonte carloで計算することもできるが、perforamnceが悪いので、semi-analytic approchが望まれる。

LMMのCMS adjustmentの計算の問題は、Gatarek[2003]のrepresentative approachなどがあるが、多くの方法はforward measureでのdriftの近似をする"freezing"という手法とみなせる。
freezingは精度の良い手法ではない。
Antonov and Arneguy[2009]が、$P(t, T_{P})/A(t)$を近似したSDEを導出することで、 $\eqref{chap16_linear_tsr_model_conditional_expectation_solution}$よりlinear annuity mapping functionを得え、以下の期待値を計算した。


$$
    \frac{P(0, T_{p})}{A(0)} \mathrm{E}^{T_{p}}
    \left[
        S(T)
    \right]
    = \mathrm{E}^{A}
    \left[
        \left(
            \frac{P(T, T_{p})}{A(T)}S(T)
        \right)
    \right]
$$

上記の方法は、精度は十分であったが、LMMで重要なのはannnuity mapping functionの非線形の影響を捉えることにある。
以下でその方法について議論する。
$\alpha(s)$が$P(T, T_{p})/A(T)$を$S(T)=s$として条件付けたものであった。
以下では、LMMのもとでこの条件付き期待値を近似することを考える。
Chap14と同様に

$$
    L_{n}(t) := L(t, T_{n}, T_{n+1}), n = 0, \ldots, N-1 
$$

とする。
簡単のため$T_{p} = T$とする。
$1/A(T)$は$\mathbb{L}(T) = (L_{0}(T), \ldots, L_{N-1}(T))^{\mathrm{T}}$の関数として

$$
    \prod_{i=0}^{n}(1 + \tau_{i}L_{i}(T))^{-1}
        = \prod_{i=0}^{n} \frac{P(T, T_{i+1})}{P(T, T_{i})}
        = \frac{P(T, T_{n+1})}{P(T, T_{0})}
        = P(T, T_{n+1})
$$

より

$$
    \frac{1}{A(T)} = \rho(\mathbb{L}(T)), 
    \rho(x) := 
        \left(
            \sum_{n=0}^{N-1} \tau_{n}
            \prod_{i=0}^{n}(1 + \tau_{i}x_{i})^{-1}
        \right)^{-1}
$$

であった。
$\alpha(s)$を以下で近似する。

$$
    \alpha(s) 
        = \mathrm{E}^{A}
        \left[
            \rho(\mathbb{L}(T)) | S(T_{n}) = s
        \right]
        \approx
            \rho( \mathrm{E}^{A}
            \left[
                \mathbb{L}(T) | S(T) = s
            \right]
            ).
$$

以上より、LMMで$\mathrm{E}^{A}(\mathbb{L}(T)|S(T)=s)$を計算する問題となった。
よく行われる方法として、Gaussian approximationを応用する。
具体的な議論をするために以下のLMMを考える。

$$
\begin{eqnarray}
    dL_{n}(t) 
        & = & \sqrt{z(t)}\phi(L_{n}(t)) \lambda_{n}(t) ^{\mathrm{T}} dW^{T_{n+1}}(t),
        \\
    d z(t)
        & = & \theta(z_{0} - z(t)) dt + \eta(t) \sqrt{z(t)} dZ(t), z(0) = z_{0} = 1,
        \\
    \langle dW^{T_{n+1}}(t), dZ(t) \rangle
        & = & 0
\end{eqnarray}
$$

$n = 0, \ldots, N-1$である。
$\lambda_{n}(t)$は$m$次元のdeterministic volatility functionで、$W^{T_{n+1}}(t)$は$m$次元$Q^{T_{n+1}}$のBM。
$\mathrm{E}^{A}(\mathbb{L}(T)|S(T) = s)$を計算するために、$Q^{A}$でのSDEを近似する。

$$
    L_{n}(t) \approx \hat{L}_{n}(t),
    S(t) \approx \hat{S}(t)
$$

$$
    d \hat{L}(t) 
        = \phi(L_{n}(0)) \lambda_{n}(t) ^{\mathrm{T}} dW^{A}(t), 
            \hat{L}_{n}(0) = L_{n}(0), 
            n = 0, \ldots, N-1,
$$

$$
    d \hat{S}(t)
        = \phi(S(0))
            \left(
                \sum_{i=0}^{N-1} w_{i}\lambda(t)^{\mathrm{T}}
            \right)
            d W^{A}(t),
            \hat{S}(0) = S(0),
$$

































