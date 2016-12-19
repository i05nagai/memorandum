---
layout: math
title: Theory and Algorithms for Bandit Problems
---


# Symbols
* $\mathcal{N}}(\mu, \sigma^{2})$
    * 平均ｎ$\mu$, 分散$\sigma^{2}$の正規分布
* $\mathcal{N}^{d}(\mu, \Sigma)$
    * 平均$\mu$、共分散行列$\Sigma$の多次元正規分布
* $\mathbb{R}_{\geq 0}^{d}$
    * $d$次元の非負ベクトル
* $K \in \mathbb{N}$
    * 選択数。行動の数。
* $T \in \mathbb{N}$
    * 試行回数
* $X_{i}(t)\ (\forall t = 1, \ldots, T, \forall i = 1, \ldots, K)$
    * $t$での選択肢$i$の報酬
* $\bar{\mu}_{i}(t) := \mathrm{E}[X\_{i}(t)]$
    * $t$での選択肢$i$の報酬の期待値
* $\bar{\mu}^{*}(t) := \max_{i} \bar{\mu}_{i}(t)$
    * $t$での報酬の期待値の最大値
* $N_{i}(t)$
    * $t$までに選択肢$i$を選択した回数
* $i(t)$
    * $t$で選んだ選択肢
* $\mathcal{A}_{T}$
    * $T$までの選択肢の集合
    * 連続腕バンディット以外では$\mathcal{A}_{T} := \\{1, \ldots, K\\}^{T}$
    * 連続腕バンディットでは、$\mathcal{A}_{T} \subset \mathbb{R}^{d \times T}$
* $I_{T} := (i_{1}, \ldots, i_{T})  \in \mathcal{A}_{T}$
    * $T$までに選択した選択肢
* $\hat{\mu}_{i}(t)$
    * $t$までの選択肢$i$の標本平均

$$
    \hat{\mu}_{i}(t) 
        := 
            \frac{1}{N_{i}(t)}
            \sum_{s=\{1, \ldots t\} : i(s)=i } X_{i}(s)
$$

* $\mathrm{Regret}(t; I_{t})$
    * $t$までに選択した選択肢によるRegret

$$
\begin{eqnarray*}
    \mathrm{Regret}(T; I_{T})
        := \max_{i \in \{1, \ldots, K\}}
            \left(
                \sum_{s=1}^{T} X_{i}(s) 
            \right)
            - \sum_{s=1}^{T} X_{i(s)}(s)
\end{eqnarray*}
$$

* 期待Regeret(expected regret)

$$
\begin{eqnarray*}
    \mathrm{Regret}_{\mathrm{expect}}(T; I_{T})
        & := &
            \mathrm{E}
            \left[
                \mathrm{Regret}(T; I_{T})
            \right]
        \\
        & = &
            \mathrm{E}
            \left[
                \max_{i \in \{1, \ldots, K\}}
                    \left(
                        \sum_{s=1}^{T} X_{i}(s) 
                    \right)
            \right]
            -
            \mathrm{E}
            \left[
                \sum_{s=1}^{T} X_{i(s)}(s)
            \right]
\end{eqnarray*}
$$
 
* 擬Regeret(pseudo regret)

$$
\begin{eqnarray*}
    \mathrm{Regret}_{\mathrm{pseudo}}(T; I_{T})
        & := &
            \max_{i \in \{1, \ldots, K\}}
            \left(
                \mathrm{E}
                \left[
                    \sum_{s=1}^{T} X_{i}(s) 
                -
                    \sum_{s=1}^{T} X_{i(s)}(s)
                \right]
            \right)
        \\
        & = &
            \max_{i \in \{1, \ldots, K\}}
            \left(
                \mathrm{E}
                \left[
                    \sum_{s=1}^{T} X_{i}(s) 
                \right]
            \right)
            - \sum_{s=1}^{T} 
            \mathrm{E}
            \left[
                X_{i(s)}(s)
            \right]
        \\
        & = & \sum_{s=1}^{T} (\bar{\mu}^{*}(s) - \hat{\mu}_{i_{s}}(s))
        \\
        & = & \sum_{i \in \{1, \ldots, K\} : \mu_{i}(t) < \mu^{*}(t)} (\bar{\mu}^{*}(s) - \hat{\mu}_{i_{s}}(s))
\end{eqnarray*}
$$


## summary
バンディット問題とは、きめられた時刻$T \in \mathbb{N}$までの間に、得られる報酬の和を最大にする選択肢の組$I_{T}$を見つける問題である。
得られる報酬の和を最大化せずに、regretと呼ばれる量を考えて、regeretを最小にする選択肢の組を見つける場合が多い。
つまり、以下を求める。

$$
    \arg \min_{I_{T} \in \mathcal{A}_{T}}
        \mathrm{Regret}(t; I_{T})
$$

ただし、各時刻$t$でのユーザの選択は$t-1$までの選択に依存して決めて良い。

報酬$X_{i}(s)$に対する仮定により問題は以下のように分類される。
* 敵対的バンディット
    * 報酬$X_{i}(s)$に確率分布を仮定しない
* 確率的バンディット
    * 報酬$X_{i}(s)$に確率分布を仮定
    * 報酬$X_{i}(s)\ (s = 1, \ldots, T)$は、$X_{i}$の独立同分布

確率的バンディットにおいて、$X$の従う確率分布に仮定を置くおくことで、以下の問題が考えられる。

* 線形バンディット
    * $X_{i}(s) =  a_{i}(s)^{\mathrm{T}}\theta + \epsilon(s)$
    * $\theta$は$\mathbb{R}^{d}$値の有界な確率変数
    * $\epsilon(s)$は時刻$s$での誤差で、期待値0の$\mathbb{R}$値確率変数
    * $a_{i}(s)$は$\mathbb{R}^{d}$値のdeterministicな変数
    * 本では、$a_{i}(s)$は$\\{0, 1\\}$値のdeterministicな変数
* 連続腕バンディット
    * $X(s) = f(i(s)) + \epsilon(s)$
    * 本では$a(s) = i(s)$を使用しているが、行動$i(s)$が何らかの関数$f$を通して報酬が得られる
    * $i(s)$が$s$での行動(選択）で、$i(s) \in \mathcal{A} \subset \mathbb{R}^{d}$ 
    * $\epsilon(s)$は時刻$s$での誤差で、期待値0の$\mathbb{R}$値確率変数

### Remark
線形な連続腕バンディット問題も考えることができる。
$i(s) \in \mathcal{A}$, $\theta \in \mathbb{R}^{d}$, $a_{\cdot} : \mathcal{A} \rightarrow \mathbb{R}^{d}$とおくと

$$
    f(i(s); \theta, \epsilon(s)) := a_{i(s)}^{\mathrm{T}} \theta + \epsilon(t)
$$

