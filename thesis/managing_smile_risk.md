---
layout: math
title: Managing Smile Risk
---

# Managing Simle Risk

## Abstract
DupireのLocal volatility modelでsmilesとskewに対応していた。
local vol modelのmarketのsmileのdynamicsは、marketで観測されるものと反対の動きをする。
原資産の価格が下がった時、local vol modelではsmileがより高い価格へshiftする。
原資産の価格が上がった時、local vol modelではsmileがより低い価格へshiftする。
marketとmodelの挙動の不整合により、deltaとvega hedgeがBSと比べて安定しない。

この論文では、以下のSABRモデルを導入する。

$$
\begin{eqnarray}
    dF & = & \alpha F^{\beta} dW_{1} \\
    d\alpha & = & v \alpha dW_{2} 
\end{eqnarray}
$$

ここで、$F$は原資産の価格で、$\alpha$はvolatility、$dW_{1} dW_{2} = \rho dt$である。

## Introduction


## 2.Reprice

2つの問題。
1つはexotic optionのpricingの問題。
例えば、$K_{1}$をストライクとする$K_{2} (< K_{1})$を下回るとknock outするcall optionを考える。
この時、$K_{1}$のcall optionのimplied volatility、$K_{2}$のimplied volatility、またはその両方を考慮すべきである。
adjustmentなしにすべてのstrikeについて計算できる、単一のself-consistentなmodelでなければこれらを考慮できない。
各strikeと各maturityについて、それぞれ異なるBS modelを考える方法ではだめ。

2つ目はヘッジの問題。
異なるstrikeに別のmodelを使っていると、deltaとvegaのriskが他のstrikeで計算されたものとどう関係するのかがわからなくなる。
例えば、high strikeの1 month optionが1MMドルのdeltaのriskを持っており、low strikeの1 month optionが-1MMドルのdeltaのriskを持っている。
vega riskについても同様の問題がある。
volのparallel shiftないし、proportional shiftによるtotal vega riskを想定するべきだろうか？
具体的には、$K=100$で$\sigma_{B} = 20%$、$K=90$で$\sigma_{B} = 24%$で、図2.1の1m optionとする。
vegaを計算するために

* それぞれのoptionに対して$\sigma_{B}$を0.2% bump
* 最初のoptionに対して$\sigma_{B}$を0.2% bump

などが考えられる。
これらの問題は重要で、portfolio全体のdeltaとvegaのriskを一括してmanagementするために重要である。
すべてのstrikeを考慮できるmodelである必要がある。

3つめの問題は、implied volatilityのカーブ$\sigma_{B}(K)$の発展に関する問題である。
$\sigma_{B}$は$K$に依存するので、forward priceの現在の価値$f$にも依存する。
よって、$\sigma_{B} = \sigma_{B}(K, f)$を考える。
この場合、図2.1のように、原資産のforward priceが変わると$\sigma-{B}$の値も変わる。

### 2.2 Local volatility models.
これらの一つの解決方法は、Dupire[2]とDerman[4][5]によりLocal volatility modelである。
Black modelの問題だったのは、係数$C(t, *)$を$\sigma_{B}F$という単純すぎる形にしたことである。
1つの代替案は、$C$をMarkovianと仮定し$C = C(t, F)$とすることである。
以後、$C(t, F)$を$\sigma_{loc}(t, F)$と書くことにする。
local volatiltiy modelはforward priceをforward measureの元で下記の通りmodel化する。

$$
	dF_{t} = \sigma_{loc}(t, F_{t}) dW_{t},  F_{0} = f
$$

Dupireは$\sigma_{loc}(t, F_{t})$を流動性のあるEuropean optionのmarketpriceにcalibrateして得ることを提案した。
calibrationにおいて、local volatility function$\sigma_{loc}(t, F)$を与えて、

$$
V_{call} := D(t_{settlement} E \left[ (F_{t_{ex}} - K )^{+} \mid F_{0} = f \right]
$$

また、$V_{call}$を用いて

$$
V_{put} := V_{call} - D(t_{ex})(f - K)
$$

を評価し、optionの理論価格を得る。


特別な以下のケースを考える。

$$
	dF_{t} = \sigma_{loc}(F_{t}) F dW_{t}, F_{0} = f
$$

[13], [14]で、singular perturbationでこのmodelを解析する。
European callとputの価格は、以下のimplied volatilityを代入したBlack formulaによって与えられる。

$$
	\sigma_{B}(K, f) 
		= \sigma_{loc}(\frac{1}{2}(f + K))
		\left( 
			1 + \frac{1}{24} \frac{\sigma_{loc}^{''}(\frac{1}{2}(f + K))}{\sigma_{loc}(\frac{1}{2}(f + K)}(f - K)^{2} + \cdots 
		\right)
$$

第二項は第一項の1%以下の補正しか与えない。

local volatility modelの挙動は第一項の分析による大部分を理解できる。

### 2.3 The SABR model.
local volatility modelの問題は、smile riskをcontrolする為には一つのBrown運動によるmarkovian modelの限界を示している。
この問題に対処するために、non-markovian modelやnon-Brownian motionのmodelを考えるのではなく、ここでは2-factor modelを考える。
forward measureの下で、以下のプロセスを考える。

$$
\begin{eqnarray}
    d\hat{F} & = & \hat{\alpha}\hat{F}^{\beta}dW_{1}, 
	\quad
	\hat{F}(0) = f,
	\\
    d\hat{\alpha} & = & \nu\hat{\alpha}dW_{2}, 
	\quad
	\hat{\alpha}(0) = \alpha,
	\\
	dW_{1} dW_{2} & = &  \rho dt.
\end{eqnarray}
$$

他の多くのstochastic volatility modelが提案されている[16], [17], [18], [19].
SABR modelは$\hat{F} , \hat{\alpha}$が同次のmodelで最も単純なものである。
以下ではSABR modelが任意の1つのexercise date$t_{ex}$のimplied volatility curveにあうことをみる。

stochastic volatility modelは、非完備市場のmodelで、stochastic volatilityのriskをhedgeできないという批判がしばしばある。
$\hat{\alpha}$の変化に対するrisk（vega risk）が原資産の売買でhedgeできないということは正しい。
しかし、原資産のoptionの売買によってriskをcontrolすることはできる。
現実的には、optionの売買でriskのhedgeをすることは日常的に行われており、非完備のmodelが問題かどうかは議論の余地がある。

SABR modelは、Appendix Bで詳細にみる。
singular perturbation methodでimplied volatility $\sigma_{B}(K f)$を求めている。
SABR modelの下European optionの価格は以下で与えられる。

$$
\begin{eqnarray}
	V_{call}(0) 
		& = & D(t_{set})(fN(d_{1}) - KN(d_{2}))
		\\
	V_{put}(0) 
		& = & V_{call} + D(t_{set})(K - f)
		\\
	d_{1}
		& := &
			\frac{
				\ln
				\left(
				    \frac{f}{K}
				\right)
				+ \frac{1}{2} \sigma_{B}^{2} t_{ex}
			}{
				\sigma_{B} \sqrt{t_{x}}
			}
		\\
	d_{2}
		& := &
			\frac{
				\ln
				\left(
				    \frac{f}{K}
				\right)
				- \frac{1}{2} \sigma_{B}(K, f)^{2} t_{ex}
			}{
				\sigma_{B}(K, f) \sqrt{t_{x}}
			}
\end{eqnarray}
$$

ここで、implied volatilityは以下で与えられる。

$$
\begin{eqnarray}
	\sigma_{B}(K, f; T)
		& \approx &
        \frac{
            \alpha
        }{
            (fK)^{(1-\beta)/2}
            \left(
                1
                + \frac{(1 - \beta)^{2}}{24}
                    \log^{2}\frac{f}{K}
                + \frac{(1 - \beta)^{2}}{1920}
                    \log^{4}\frac{f}{K}
            \right)
        }
        \left(
            \frac{z}{x(z)}
        \right)
        \left[
            1
            +
            \left(
                \frac{(1 - \beta)^{2}}{24}
                    \frac{\alpha^{2}}{(fK)^{1-\beta}}
                + \frac{1}{4}
                    \frac{\rho\beta\nu\alpha}{(fK)^{(1-\beta)/2}}
                + \frac{2 - 3\rho^{2}}{24}\nu^{2}
            \right) T
        \right],
    \\
    z 
        & := &
        \frac{\nu}{\alpha}
            (fK)^{(1-\beta)/2}
            \log\left( \frac{f}{K} \right),
    \\
    x(z) 
        & := &
            \log
            \left(
                \frac{
                    \sqrt{1 - 2\rho z + z^{2}} + z - \rho
                }{
                    1 - \rho
                }
            \right)
\end{eqnarray}
$$

更にATMの場合は、$f = K$なので、以下の簡単な形になる。

$$
\begin{equation}
	\sigma_{ATM}(S; T)
		:= \sigma_{B}(S, S; T)
        \approx
        \frac{\alpha}{S^{(1-\beta)}}
        \left[
            1
            + 
            \left(
                \frac{(1-\beta)^{2}}{24}
                    \frac{\alpha^{2}}{S^{2 - 2\beta}}
                + \frac{1}{4}
                    \frac{\rho \beta \alpha \nu}{S^{1-\beta}}
                + \frac{2 - 3\rho^{2}}{24} \nu^{2}
            \right) T
        \right]
\end{equation}
$$

## 3 Managing Smile Risk


## Appendix A. Analysis of the SABR Model

$$
\begin{eqnarray}
    d\hat{F} & = & \epsilon \hat{\alpha} C(\hat{F}) dW_{1},
    \label{a_1a}
    \\
    d \hat{\alpha} & = & \epsilon \nu \hat{\alpha} dW_{2},
    \label{a_1b}
    \\
    dW_{1}dW_{2} & = & \rho dt,
    \label{a_1c}
\end{eqnarray}
$$

### A.1

$$
\begin{equation}
    V(t, f, a) 
        = (f - K)^{+}
        + \frac{|f - K|}{4 \sqrt{\pi}}
            \int_{\frac{x^{2}}{2\tau_{ex}} - \epsilon^{2}\theta}^{\infty} 
            \frac{e^{-q}}{q^{3/2}}\ dq
    \label{a_52a}
\end{equation}
$$

$$
\begin{equation}
    \epsilon^{2}\theta
        = \log
        \left(
            \frac{
                \epsilon \alpha z
            }{
                f - K
            }
            \sqrt{B(0)B(\epsilon \alpha z)}
        \right)
        + \log
        \left(
            \frac{
                x I^{1/2} \epsilon \nu z
            }{
                z
            }
        \right)
        +\frac{1}{4} \epsilon^{2} \rho \nu \alpha b_{1} z^{2}
    \label{a_52b}
\end{equation}
$$

### A.2 Equivalent normal volatility.
$$\eqref{a_52a}$$と$$\eqref{a_52b}$$はSABR modelでのcall optionの価格であった。

$$
\begin{equation}
    \frac{z}{\chi(z)}
        := \frac{
            \zeta
        }{
            \log
            \left(
                \frac{
                    \sqrt{1 - 2\rho\zeta + \zeta^{2}} - \rho + \zeta
                }{
                    1 - \rho
                }
            \right)
        },
    \label{a_57b}
\end{equation}
$$

ここで、

$$
    \zeta
        := \epsilon \nu z
        = \frac{\nu}{\alpha}
            \int_{K}^{f} \frac{1}{C(\tilde{f})}\ d\tilde{f}
        = \frac{\nu}{\alpha}
            \frac{f - K}{C(f_{av})}(1 + O(\epsilon^{2})).
    \label{a_57c}
$$

ここで、$f_{av} := \sqrt{fK}$は$f$と$K$は幾何平均である。

$$
\begin{eqnarray}
    \epsilon^{2} \phi_{1}
        & := &
            \frac{1}{z^{2}} \log
            \left(
                \frac{
                    \epsilon \alpha z
                }{
                    f - K
                }
                \sqrt{C^{\prime}(f) C(K)}
            \right)
        \nonumber
        \\
        & = &
            \frac{
                2 \gamma_{2} - \gamma_{1}^{2}
            }{
                24
            }
            \epsilon^{2} \alpha^{2} C^{2}(f_{av})
            + \cdots
        \label{a_57d}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \epsilon^{2}\phi_{2}
        & = &
            \frac{1}{z^{2}}
            \log
            \left(
                \frac{\chi}{z} 
                    (1 - 2 \epsilon \rho \nu z + \epsilon^{2} \nu^{2} z^{2})^{1/4}
            \right)
        \\
        & = &
            \frac{2 - 3\rho^{2}}{24} \epsilon^{2} \nu^{2}
            + \cdots
\end{eqnarray}
$$

ここで、

$$
\begin{equation}
    \gamma_{1} := \frac{C^{\prime}(f_{av})}{C(f_{av})},
    \\
    \gamma_{2} := \frac{C^{\prime\prime}(f_{av})}{C(f_{av})}.
    \label{a_57g}
\end{equation}
$$


$$
\begin{eqnarray}
    d \hat{F} & = & \epsilon \hat{\alpha}C(\hat{F}) dW_{1},
    \quad
    \hat{F}(0) = f,
    \label{a_58a}
    \\
    d\hat{\alpha}
        & = & \epsilon \nu \hat{\alpha} dW_{2},
    \quad
    \hat{\alpha}(0) = \alpha,
    \label{a_58b}
    \\
    dW_{1} dW_{2} & = & \rho dt,
    \label{a_58c}
\end{eqnarray}
$$

$$
\begin{equation}
    \sigma_{N}
        := \frac{
            \epsilon \alpha (f - K)
        }{
            \int_{K}^{f} \frac{1}{C(\tilde{f})}\ d \tilde{f}
        }
        \left(
            \frac{\zeta}{\hat{\chi}(\zeta)}
        \right)
        \left[
            \left(
                \frac{
                    2\gamma_{2} - \gamma_{1}^{2}
                }{
                    24
                }
                \alpha^{2}C^{2}(f_{av})
                + \frac{1}{4} \rho \nu \alpha \gamma_{1} C(f_{av})
                + \frac{2 - 3 \rho^{2}}{24}\nu^{2}
            \right)\epsilon^{2} T
            + \cdots
        \right]
    \label{a_59a}
\end{equation}
$$

ここで、

$$
\begin{eqnarray}
    f_{av} 
        & := & \sqrt{fK},
    \\
    \gamma_{1} 
        & := & \frac{
            C^{\prime}(f_{av})
        }{
            C(f_{av})
        },
    \\
    \gamma_{2}
        & := & \frac{
            C^{\prime\prime}(f_{av})
        }{
            C(f_{av})
        },
    \\
    \zeta
        & := & 
            \frac{\nu}{\alpha} \frac{f - K}{C(f_{av})},
    \\
    \hat{\chi}(\zeta)
        & := &
            \log
            \left(
                \frac{
                    \sqrt{1 - 2\rho\zeta + \zeta^{2}} - \rho + \zeta
                }{
                    1 - \rho
                }
            \right)
\end{eqnarray}
$$



## Referenc
* [1]
* [2]

