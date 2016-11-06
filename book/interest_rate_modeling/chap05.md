---
layout: math
title: Interest Rate Modeling 1
---

# 5 Fixed Income Instruments

### 5.10.1 Cash-Settled Swaptions
ここまで扱ったSwaptionは全て、Phisical settlementのswaptionである。

* Physical swaption
    * swap-settled swaptionとも言われる。
    * optionの満期にoptionが行使されると実際のIRSが行われるもの
* Physical swaptionと経済的に等しい取引
    * optionの満期にoptionが行使されると$T_{0}$のswapのPVが支払われる
    * 金利スワップの取引は行われない

どちらも場合もpayers swaptionのpayoffは

$$
\begin{equation}
    A(T_{0}) (S(T_{0}) - k)^{+},
    \label{chap5_15_payoff_physical_settled_swaption}
\end{equation}
$$

である。
ヨーロッパのマーケットでは、これらと異なるcash settledと呼ばれるswaptionの取引が一般的である。

* cash-settled swaption
    * 金利スワップの取引は行われない
    * optionの保持者は、満期日にoptionを行使すると現金を受取る
    * 現金は以下のpayoffで支払われる。

$$
    V_{\mathrm{CSS}}(T_{0})
        = a(S(T_{0}) (S(T_{0}) - k)^{+},
$$

ここで、

$$
    a(x)
        = \sum_{n=0}^{N-1} \frac{\tau_{n}}{\prod_{i=0}^{n}(1 + \tau_{i}x}.
$$

つまり、payoffはswap rateの関数で支払われる。

* phisical settlmetはcash flowの日付のdiscount factorが分かれば良い
    * yield curveの引き方やbid-ask spreadの影響で、dealer間と異なる 
* cach-settled swaptionは厳密には、Black formulaで計算できるようなvanilla optionではない
* $a(S(t))$はマルチンゲールではないので、何らかのdriftの調整が必要になる
* Section 16.6.12で詳細に扱う。
* cash-settled swaptionはeuropean marketでは最も流動性のある金利optionの取引なので、金利のvolatilityの情報を得る為に利用される。



