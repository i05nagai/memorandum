---
title: Application of bandit
book_title: Theory and Algorithms for Bandit Problems
book_chapter: 10
---

## バンディット手法の応用

## 10.1 モンテカルロ木探索

## 10.2 インターネット広告
* 広告配信会社
    * ブロガー、webサイト運営者から広告スペースを借りる
    * 広告配信会社は、広告スペースに掲載する広告を選ぶ
    * 広告配信会社のサイトを経由して、広告主のサイトに
* 広告主
    * 広告配信会社に掲載する広告を提供する
    * 最近は、Pay Per Click(PPC)が多い

PPCの場合は、広告配信会社はクリック率が高い広告を配信したい。
新しい広告については、クリック率のデータがないので、特徴量に対するクリック率の高い広告の探索とクリック率の高い広告の配信をバランスする必要がある。
この意味で、バンディット問題は有用であると考えられる。

広告配信で考慮されるべき要素としては

* 人気広告かどうか
    * もともと知名度の高い人気の商品の広告は、クリック率は高い
* 広告主の予算
    * 広告主の予算を上限として、配信回数が決まっている
* 広告と掲載ページの相性
    * スポーツ用品のサイトに手芸用品の広告など
    * 掲載ページの閲覧者の属性

以上を考慮すると、 次の雑な線形計画問題を考えることができる。

* $K \in \mathbb{N}$
    * 広告掲載ページ数
    * givenと思って良い
* $i = 1, \ldots, K$
    * 広告掲載ページ$i$
* $$p_{i}$$,
    * ページ$i$のアクセス数
    * 問題によっては、線形計画問題を解く時に推定が必要
* $L \in \mathbb{N}$
    * 広告数
    * givenと思って良い
* $j = 1, \ldots, L$
    * 広告$j$
* $$d_{j}$$,
    * 広告$j$のある期間の配信回数の上限
    * givenと思って良い
* $$x_{i, j} \in \mathbb{Z}_{\ge} \ (i = 1, \ldots, K,\ j = 1, \ldots, L)$$,
    * ページ$i$に対する広告$j$の配信回数
    * 線形計画問題の変数
* $$\rho_{i, j} \in [0, 1] \ (i = 1, \ldots, K,\ j = 1, \ldots, L)$$,
    * ページ$i$に対する広告$j$のクリック率
    * 線形計画問題を解く時点で既知のデータを使って、推定する

$$
\begin{align}
    \max_{x_{i, j}}
    & & &
        \sum_{i=1}^{L}
            \sum_{j=1}^{K}
                \rho_{i,j}
                x_{i, j}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \sum_{j=1}^{K}
            x_{i, j} = p_{i}
        \quad
        (i = 1, \ldots, L)
    \nonumber
    \\
    & & &
        \sum_{i=1}^{L}
            x_{i, j} = d_{i}
        \quad
        (j = 1, \ldots, K)
    \nonumber
\end{align}
$$

制約の第一式は、配信回数がページのアクセス回数を超えないという制約である。
第二式は、配信回数が予算を超えないという制約である。
この線形計画問題に対して、$$\rho_{i, j}$$をバンディット手法によって推定するという手法が考えられる。
特に、ギッティンズ指標を用いて、配信回数が少ないことによる、推定精度の悪さを補う方法が提案されている。

次に、最近良く利用される広告オークション(advertising auction, ad auction)について考える。
ad auctionでは、各クリックに対して支払っても良い金額を各広告主が掲示し、あらかじめ決められた規準に基いて、掲示された広告の中から広告配信会社が配信する広告を決める。
つまり、各クリックごとに広告主がオークションの参加者となって、金額をbidするのである。
以下では、広告スペースは一つ固定して単純化して議論する。
この単純化は、広告スペースの閲覧者層によってクリック率が変わる広告主の立場から深刻であるが、応用上は広告配信会社の広告配信決定問題が中心的である為、ここではこれを認める。

* $T \in \mathbb{N}$
    * クリック回数、オークションの開催回数
* $t = 1, \ldots, T$
    * $t$回目のクリック、オークション
* $L$
    * 広告の数
    * 記法の簡便さのため、広告と広告主は一対一に対応するとする
        * この仮定は、以下の議論では問題にならない
* $$b_{t, j} \in \mathbb{R}_{\ge 0}$$,
    * クリック$t$に対する広告$j$の広告主が掲示する金額
* $j(t)$
    * $t$で実際に配信した広告
    * 広告配信会社は、広告主の掲示した金額とクリック実績などから、あらかじめ決められた規準に基いて決める
* $$p_{t, j}$$,
    * 広告$j$の広告主が$t$で広告配信会社に実際に支払うきんがく
    * $$j(t) = j$$のときかつまたその時に限り、$$p_{t, j} > 0$$
    * 一般には、広告主の掲示金額と支払金額は一致しない
        * $$b_{t, j(t)} \neq p_{t, j(t)}$$,
* $$v_{t, j}$$,
    * $t$で広告$j$が配信された場合の広告$j$の広告主の価値
    * 広告主の掲示金額とは別に、例えば1 impressionに対していくらと広告主側が考えているか
    * $$b_{t, j} = v_{t, j}$$の場合もあれば、$$b_{t, j} \neq v_{t, j}$$の場合もある

以上の記号の下に、用語を定義する。

### Definition. first-price auction
第1価格オークション(first price auction)とは、掲示金額が最も高い広告が配信され、掲示金額をそのまま支払う場合を言う。
つまり、

$$
\begin{eqnarray}
    j(t)
    & = &
        \argmax_{j}b_{t, j}
    \nonumber
    \\
    p_{t, j(t)}
    & = &
        \mathrm{max}_{j}b_{t, j}
    \nonumber
\end{eqnarray}
$$

である。

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. second-price auction
第2価格オークション(second price auction)とは、掲示金額が最も高い広告が配信され、2番目に高い掲示金額を支払い金額とする場合を言う。
つまり、

$$
\begin{eqnarray}
    j(t)
    & = &
        \argmax_{j}b_{t, j}
    \nonumber
    \\
    p_{t, j(t)}
    & = &
        \mathrm{smax}_{j}b_{t, j}
    \nonumber
\end{eqnarray}
$$

である。
但し、$$\mathrm{smax}_{j}$$は$j$で添字付けられた集合の中で2番目に大きい値である。

<div class="end-of-statement" style="text-align: right">■</div>
以下では、第二価格オークションの場合に限って話をすすめる。

* $$c_{t, j} \in \{0, 1\}\ (t = 1, \ldots, T, j = 1, \ldots, K)$$,
    * $t$で広告$j$がクリックされたら1、それ以外は0
* $C_{j}$
    * 広告$j$が配信された時のクリックの有無を表す確率変数
    * $$c_{t, j(t)}$$は$C_{j(t)}$のi.i.d
    * 配信されてないものについては、i.i.dではない
* $$C := (c_{t, j})_{j = 1, \ldots, K, t = 1, \ldots, L}$$,
    * クリックの有無の列
* $$x_{t, j} \in \{0, 1\}\ (t = 1, \ldots, T, j = 1, \ldots, K)$$,
    * $t$で広告$j$が配信されたら1, それ以外は0
    * 配信されなければクリックされないので、明らかに$$c_{t, j} <=x_{t, j}$$
    * $$x_{t, j(t)} = 1$$,
    * $$x_{t, j(t)} = 0\ (j \neq (t)$$,
    * 第二価格オークションでは配信の有無は掲示金額によって、決まるので$$\{b_{t, j}\}_{j=1, \ldots, K}$$で決まる
* $$x := (x_{t, j})_{j = 1, \ldots, K, t = 1, \ldots, L}$$,
    * 配信の有無の列

以上の記号の下、広告$j$の効用$$U_{j}$$を以下で定義する。

$$
\begin{eqnarray}
    U_{j}
    & := &
    \sum_{t=1}^{T}
         \left(
             v_{t, j}
             c_{t, j}
             x_{t, j}
             -
             p_{t, j}
         \right)
    \nonumber
    \\
    & = &
    \sum_{t=1}^{T}
         \left(
             v_{t, j}
             c_{t, j}
             -
             p_{t, j}
         \right)
    \nonumber
\end{eqnarray}
$$

つまり、広告$j$が配信された時の効用と支払った金額との差である。
advertising auctionの設計とは、各$t = 1, \ldots, T$時点において以下の2つを決めることである。

1. 以下を考慮して$t$で配信する広告$j(t)$を決定
    * 広告の掲示金額$$b_{t, j}\ (j = 1, \ldots, K)$$
    * 過去の配信広告$j(s) (s < t)$
    * クリックの履歴$$c_{s, j(s)}\ (s < t)$$
2. クリックされた場合の請求金額$$p_{t, j(t)}$$の決め方の決定
    * 関数形の決定
    * 例えば、第二価格オークションなら2番目に高い掲示金額が請求金額

### Remarks
$j(t)$が決まれば、$$x_{t, j}$$は完全に決まり、逆も同様である。
$$c_{t, j}$$は、配信の有無$$x_{t, j}$$とユーザに依存する。
ユーザなどの不確定性を確率的に考えれば、$$c_{t, j}$$は$$b_{t, j}$$に依存した確率変数と思える。
$$p_{t, j}$$は$$c_{t, j}$$と$$b_{t, j}$$に依存する(依存させることができる）。
$$c_{t, j}$$が確率変数と思えば、$$p_{t, j}$$も確率変数と思える。

<div class="end-of-statement" style="text-align: right">■</div>

広告代の合計の期待値を

$$
    \sum_{t=1}^{T}
        \sum_{j=1}^{K}
            \mathrm{E}
            \left[
                P_{t, j}
            \right]
$$

とする。
真のクリック率$\rho_{j}$がわかっていたとする。
つまり、$C_{j}$の真の分布がわかっていたとする。
この時の$t$での第二価格オークションの期待収益は

$$
    \rho_{j(t)}
    \mathrm{smax}_{j}
        b_{t, j}
$$

である。
この期待収益と実際に請求する金額の期待値との差を$T$-Regretと定義する。
つまり、

$$
\begin{eqnarray}
    T\mathrm{-Regret}
    & := &
        \sum_{t=1}^{T}
            \rho_{j(t)}
            \mathrm{smax}_{j}
                b_{t, j}
        -
        \sum_{t=1}^{T}
            \sum_{j=1}^{K}
                \mathrm{E}
                \left[
                    P_{t, j}
                \right]
    \nonumber
\end{eqnarray}
$$

である。


以下では
必要な用語を定義しよう。

### Definition. truthful auction for a click event sequence $C$
クリックの列$C$に対して正直なオークションとは、任意の$t$に対して、

$$
    \forall t = 1, \ldots, T,
    \
    \forall j = 1, \ldots, K,
    \quad
    b_{t, j}
    =
    v_{t, j}
    \Rightarrow
    \forall \{b_{t, j}^{\prime}\},
    \
    b_{t, j}^{\prime} \in \mathbb{R}_{\ge 0}
    \
    U_{j}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. always truthful auction
任意のクリック履歴について、正直なオークションを、常に正直なオークション(always truthful auction)という。
つまり、任意の$$\forall C \in \{0, 1\}^{K T}$$について、$C$に対して正直なオークションである。

<div class="end-of-statement" style="text-align: right">■</div>

次が成り立つ。

### Proposition.
第2オークションは正直なオークションである。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>

以上の準備のもと、次のアルゴリズムを考える。

### Algorithms 10.2  正直なオークション型広告配信設計
* $\tau \in \mathbb{R}_{> 0}$,
    * 探索回数を決定するパラメータ
    * $K$個の広告を約$\tau$回ずつ掲載する
* $\delta \in [0, 1]$
    * $1-\delta$の確率で、クリック率の推定値が上界に収まるとする

大きく3つに別れる。
最初に、$K$個の広告を約$\tau / K$回ずつ掲載して、クリック率に関する推定値を算出するためのクリック履歴を得る。
次に、得られたクリック履歴からクリック率の推定を行う。
最後に、推定値の良いものを配信する。

* 1 $$\forall t = 1, \ldots, K \lfloor \tau / K\rfloor$$,
    1. 各広告$j$のクリック時の掲示金額$$b_{t, j}$$を取得
    2. 広告$j(t) := t \% (K + 1)$を配信
    3. 配信してない広告のクリックは0なので、$$c_{t, j} = 0\ (j \neq j(t))$$とする
    4. 配信した広告のクリックの有無に応じて、$$c_{t ,j(t)}$$を設定
    5. すべての広告$j$に対して、$$p_{t, j} := 0$$円として、請求する
        * つまり請求しない
        * この期間はオークション性を無視して配信している
* 2 各広告$j$の推定クリック率$$\hat{\rho}_{j}$$としの信頼上界$$\hat{\rho}_{j}^{+}$$を以下で決める
    * $1 - \delta$で、$$\hat{\rho}_{j}^{+}$$に収まると仮定している

$$
\begin{eqnarray}
    \hat{\rho}_{j}
    & := &
        \sum_{t=1}^{K \lfloor \tau / K \rfloor}
            \frac{
                c_{t, j}
            }{
                \lfloor
                    \frac{ \tau }{ K }
                \rfloor
            },
    \nonumber
    \\
    \hat{\rho}_{j}^{+}
    & := &
        \hat{\rho}_{j}
        +
        \sqrt{
            2
            \frac{
                \left(
                    \log
                    \frac{K}{\delta}
                \right)
            }{
                \lfloor
                    \frac{\tau}{K}
                \rfloor
            }
        }
    \nonumber
\end{eqnarray}
$$

* 3 $$\forall t = K \lfloor \tau / K \rfloor + 1, \ldots, T$$,
    1. 各広告$j$のクリック時の掲示金額$$b_{t, j}$$を取得
    2. 広告$$j(t) := \argmax_{j} \hat{\rho}_{j}^{+}b_{t, j}$$を配信
    3. 配信してない広告のクリックは0なので、$$c_{t, j} = 0\ (j \neq j(t))$$とする
    4. 配信した広告のクリックの有無に応じて、$$c_{t ,j(t)}$$を設定
    5. 以下の通り請求
        * $$c_{t, j(t)} = 1$$であれば、広告$j(t)$に対して$$p_{t, j(t)}:=\frac{\mathrm{smax}_{j}\hat{\rho}_{j}^{+}b_{t, j}}{\hat{\rho}_{j(t)}}$$円請求し、広告$j \neq j(t)$については、$$p_{t, j} = 0$$円請求
        * $$c_{t, j(t)} = 0$$であれば、広告$j$については、$$p_{t, j} = 0$$円請求
        * ただし、$$\mathrm{smax}_{j}\mathrm{smax}_{j}\hat{\rho}_{j}^{+}b_{t, j}$$は2番目に大きい、$$\mathrm{smax}_{j}\hat{\rho}_{j}^{+}b_{t, j}$$の値を返す。

<div class="end-of-statement" style="text-align: right">■</div>

このアルゴリズムの$T$-Regretの上界は以下で与えられる。

### Thereom 10.1
Alogrithm 10.2において、

* $\delta := 1/T$
* $$\tau := K^{1/3}T^{2/3}\sqrt{\log KT}$$,

ととれば、

$$
    T\mathrm{-Regret}
    =
    O(b_{max}K^{1/3}T^{2/3}\sqrt{\log KT})
$$

となる。
ただし、$$b_{max} := \max_{j, t}b_{t, j}$$である。

### proof.

<div class="QED" style="text-align: right">$\Box$</div>


### Memo
以下のモデルを考えていると思って良さそう。

* $$(\Omega, \mathcal{F}, P)$$,
    * probability space
* $$b_{1, t}, \ldots, b_{k, t}$$,
    * $t$でgivenなので、確率的とは思ってない
* $$x_{j, t} := f(b_{1, t}, \ldots, b_{K, t})$$,
    * 配信枠は1つと思っているので$$\sum_{j=1}^{K}x_{j, t} = 1$$,
    * $f$は第2価格オークションの場合は$\mathrm{max}$でかける
* $C_{j}$
    * 広告$j$が配信された時のクリックの有無を表す確率変数
* $C_{j, t}$
    * $C_{j}$の$t$についてのi.i.d列
* $$c_{j, t} := x_{j, t}C_{j, t}(\omega)$$,
    * $$\omega \in \Omega$$,
    * クリックの実現値
* $$P_{j, t} := x_{j, t}C_{j, t}g(b_{1, t}, \ldots, b_{K, t})$$,
    * $P_{j, t}$が確率的なのは、$C$が確率的だから？
* $$p_{j, t} := x_{j, t}C_{j, t}(\omega)g(b_{1, t}, \ldots, b_{K, t})$$,
    * $$\omega \in \Omega$$,
    * $g$は第2価格オークションの場合は$\mathrm{smax}$でかける

ややこしいのは、$C_{j}$はあくまで、配信された場合のクリック率であるということ。
その為、$$c_{j, t} := C_{j, t}(\omega)$$ではない。
