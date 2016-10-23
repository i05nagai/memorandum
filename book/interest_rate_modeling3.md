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
		* [16.6.3 Swap-Yield TSR Model](#1663-swap-yield-tsr-model)
		* [16.6.4 Linear and Other TSR Models](#1664-linear-and-other-tsr-models)

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

$\bar{w}$と$\underline{w}$は離散化した積分の上端と下端をとれば良い？

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
        = \frac{A(0)}{P(0, T_{p})} E^{A}
            \left(
                \frac{P(T, T_{p})}{A(T)}S(T)
            \right) - S(0)
\end{equation}
$$

* Sec16.5のLibor-with-delayの議論はCMSに適用できる。
* $\eqref{value_cms}$はTerm structure modelで計算できるが、計算が遅く、精度も悪い
* replicatoin methodの方が大抵better
    * そのためには$P(T, T_{p}) / A(T)$が$S(T)$の関数としてかける必要がある。
    * LIAやLibor-with-delayですでにやった

## 16.6.1 The replication Method for CMS
* Prop 8.4.13をCMPSのpayoffに適用する。

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
swaptionの価格は、marketの価格か選択したmodelで直接計算される。
replicatoin methodはmarketのすべての価格のstrikesと一貫したCMSの価格を計算するだけでなく、modelに依存しない($\alpha(s)$には依存する）payer/recieverのswaptionのポートフォリオを提供する。

$\eqref{chap16_value_cms_static_hedge}$に対して、いくつかの制約をいれることができる。
例えば、low strikeやhigh stirkeのswaptionは流動性が低いので、以下のように

$$
    A(0)S(0) \alpha(S(0))
        + \int_{K_{\min}}^{S(0)} w(K)V_{\mathrm{rec}}(0, K)\ dK
        + \int_{S(0)}^{K_{\max}} w(K)V_{\mathrm{pay}}(0, K)\ dK, 
    \label{chap16_value_cms_static_hedge_low_liquid}
$$

かける。
有限個の場合のrepliationについては、Sec16.4で議論をしている。

replication methodは、$g(S(T))$をpayoffに持ち、$T_{p} \ge T$に支払いがある場合に拡張できる。
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
financeで現れるおおくのpayoff関数は、二階微分をするとdelta関数があらわれる。
capletとfloorletの場合は、delta関数が集中する点$s_{0}$での$V_{\mathrm{rec}}(0, s_{0})$ないし、$V_{\mathrm{pay}}(0, s_{0})$ (どちらを考慮するかは$s_{0}$と$K$の値による) の値の寄与を考えれば良い。

### 16.6.2 Annuity Mapping Function as a Conditional Expected Value
* $\alpha(s)$を前節で導入したが、$\alpha(s)$をどうするかは議論しなかった
* 前節までで議論したTerminal Swap Rate modelsやTerm structure modelによる近似の例が参考になると期待できる
* まずはじめに、annuity mapping functionの理論的な意味についてみる

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
条件付き期待値は、確率変数$X, Y$について、$X$の$Y$での条件付き期待値は、$Y$を可測にする関数全体への空間を$\mathcal{B}$とする。

$$
    E(X|Y) = f^{*}(Y), 
    \mathrm{where}\ 
    f^{*} = \mathrm{argmin} \left\{
        E \left(
            (X - F(Y))^{2}, f \in \mathcal{B}
        \right)
    \right\}
$$

条件付き期待値の近似として$\mathcal{B}$をsubspace $\tilde{\mathcal{B}} \subset \mathcal{B}$ として近似する方法がある。
つまり、

$$
    E(X|Y) \approx f^{*}(Y)
    \mathrm{where}
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
                \frac{1}{1+\tau_{0}S(0)}^{T_{p}/\tau_{0}}
            \right)
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


