---
title: Theory and Algorithms for Bandit Problems
book_title: Theory and Algorithms for Bandit Problems
book_chapter: 1
---

# 1 バンディット問題とは

## 1.4 プレイヤー方策の評価
報酬$X_{i} (\forall i)$が全て有界とする。
プレイヤーの方策を評価する指標として以下のようなもの考えることができる。
よく使われるのは、regret, 期待regeret, 擬regretである。


* 累積報酬
    * 試行回数が無限の場合には報酬に何らかの仮定が必要

$$
    \sum_{s=1}^{T} X_{i(s)}(s)
$$

* 幾何割引
    * 試行回数が無限の場合に使用することが多い
    * 無限級数の収束性を保証するために、$\gamma < 1$をかける
    * 無限回の試行をするが、手前の時刻の報酬に重みをおく

$$
    \sum_{s=1}^{\infty}  \gamma^{s-1}X_{i(s)}(s)
$$

* 最適選択肢との差
    * 各時刻での最適な選択肢の報酬の和とユーザの選択肢の差
    * 差が大きくなりすぎるため、使われないらしい
    * そのかわりregretを使う

$$
    \mathrm{Regret}(T; I_{T})
        := \sum_{s=1}^{T} 
            \max_{i \in \{1, \ldots, K\}}
            \left(
                X_{i}(s) 
            \right)
            - \sum_{s=1}^{T} X_{i(s)}(s)
$$

* regeret
    * 同じ選択肢を選び続けたときの累積報酬の最大値とユーザの選択した報酬の差
    * 累積報酬、幾何報酬は報酬のスケールに依存するが、最大値からの乖離を見ることでスケールの影響を軽減
    * ある時刻$t$の全ての選択肢の報酬が観測できるとは限らないので、実際にregretを観測できる場合は多くない
    * $I_{T}: = (i(1), \ldots, i(T)) \in \mathcal{A}_{T}$をユーザの選択肢とすると

$$
    \mathrm{Regret}(T; I_{T})
        := \max_{i \in \{1, \ldots, K\}}
            \left(
                \sum_{s=1}^{T} X_{i}(s) 
            \right)
            - \sum_{s=1}^{T} X_{i(s)}(s)
$$

* 期待regeret(expected regret)
    * regretの期待値
    * 理論的に扱いやすい
    * $I_{T}: = (i(1), \ldots, i(T)) \in \mathcal{A}_{T}$をユーザの選択肢とすると

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

* 擬regret(pseudo-regret)
    * 同じ報酬を選び続けたときの期待値の和の最大値とユーザの選択した報酬の期待値の和の差
    * 理論的に扱いやすい
    * $I_{T}: = (i(1), \ldots, i(T)) \in \mathcal{A}_{T}$をユーザの選択肢とすると

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
\end{eqnarray*}
$$

### Remark
$\max$が凸関数であることと、Jensen's inequalityより

$$
    \mathrm{Regret}_{\mathrm{expected}}(T; I_{T})
    \le
    \mathrm{Regret}_{\mathrm{pseudo}}(T; I_{T})
$$
