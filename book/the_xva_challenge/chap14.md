---
layout: math
title: Theory and Algorithms for Bandit Problems
---

# 14 Credit and Debt Value Ajustments

## 14.1 OVERVIEW
この章では、CVAとDVAについて扱う。
CVAとDVAはcredit spreadのvolatilityと会計(IFRS 13)及び資本規制(Basel III)によって、銀行にとって重要な話題となっている。
しかし、銀行に限らず大きなOTC derivativeをもっている他の金融機関や企業にとっても重要な話題である。
この章では次の仮定をおく。

```
仮定 
credit exposureと倒産確率は独立。
つまり、wrong-way riskは考慮しない(Chap17で扱う）
```

## 14.2 CREDIT VALUE AJUSTMENT

### 14.2.1 Why CVA is not straightforward
債券のように支払いが一方から一方にしかないものは、credit riskを考えるのは難しくない。
cashflowをdiscountし、 倒産時の支払いを足せば良い。
多くのデリバティブは、swapのように相互に支払いがあるものが殆どで、これによりcredit exposureとcounterparty riskの定量化を難しくしている。
例えば、債券は常に全てリスクに晒されているが、swapはoffsetするのでCashFlowの一部がリスクに晒される。
この一部を知る為に、yield curveの形状やforward rateやvolatilityを知る必要がある為複雑である。

### 14.2.2 History of CVA
CVAは基は以下のような形で表現されていた。(Appendix 14A)

$$
\mathrm{Risky\ value} = \mathrm{Risk\ free\ value} - CVA
$$

* 価値の評価とcounterparty riskの計算が分かれているのが良い。
* risk-free-valueとしてOIS discountingが使われる場合もある。
* 歴史的には、CVAはcredit chargeや倒産時の為のreserveとして扱われていた

上記の式の良い所は、Risk-free-valueとCVAの計算を別々にできること。
CVAの計算をする部署とrisk-free-valueを計算する部署が、transfer priceを通じて管理する。
この考えは、他のxVAに対しても適用される。

一見上式はsimpleに見えるが、nettingやcollateralがあるので取引ごとに足すことができないという複雑さもある。
CVAはこれらを考慮して計算する必要がある。

### 14.2.3 CVA formula
典型的なCVAの要因として次の公式がある。

$$
\mathrm{CVA} = -\mathrm{LGD} \sum\_{i=1}^{m} \mathrm{EE}(t\_{i}) \times \mathrm{PD}(t\_{i-1}, t\_{i})
$$

* Loss given default(LGD)
    * LGD = 100% - Recovery-rate
* Expected Exposure(EE)
    * \\( t_{i} \\) でdisocuntされたExpected Exposure(EE). 
    EEはChap10で扱った。
    risk-freeでdiscountするのが良い。
* Default Probability(PD)
    * \\( t\_{i-1}, t\_{i} \\) の倒産確率。倒産確率の推定はChap12で扱った。

上式について

* CVAは、LGD, EE, PDにだいたい比例する。
* EE, PDは、Section 7.2.3や12.2.4でみたようにtime-inhomogeneousとする。
* EEとPDの分布を考慮する為に、時間に対して積分をとる。
* CVAは損失を表す為マイナスをつける。
むかしは、マイナスがつかないこともあったが、xVAの話がでてきてからつくようになった。
* 図14.2は上式の概念図。

### 14.2.4 CVA example
CVA formulaをforward contract typeのexposureを例に適用する。
Section7.3.2の式7.3より以下が成り立つ。

$$
\mathrm{EE} \propto \sqrt{t}
$$

また、式12.1のrisk-neutral PDを使用する。

* credit spread = 300bpsで定数
* LGD = 60%
* 式14.2の期間0.25年刻み

図14.3がEEとPD
CVAは0.2%で、Notionalに対する割合で表現される。(EEが%で表現される為）

> Spreadsheet14.1にcredit spreadが200bpsの例がのっている。

正しい答えは0.193%である。
EEやPDの分割を細かくすれば精度はあがるが、次のようにすると同じ分割でも精度があがり0.192%となる。

$$
\mathrm{EE}(t\_{i}) \rightarrow \[ \mathrm{EE}(t\_{i}) + \mathrm{EE}(t\_{i-1}) \] / 2
$$

### 14.2.5 CVA as a spread
CVAを値としてではなく、年率のcredit chargeとして表現したい場合もある。
Appendix14Bの単純化した公式でrisky annuityは4.42と計算できる。
risky annuityからCVAをspreadとして次のように計算できる。
\\( -0.2\% / 4.42 * 10000 = -4.62 \\)bps(per annum)

Appendix14Cより上記の式は、より単純で役にたつ次の近似式としても表現できる。

$$
CVA \approx -EPE \times \mathrm{Spread}
$$

EPEは式7.2.6より求まる。
分割幅が0.25とすると先ほどの例ではEPE=1.51%となるので、CVA = -1.54% * 300 = -4.62bps.

上記の近似は、swap likeの商品にはよくあてはまるが、単調にEEが増加するものについてはあたはまりは良くない。
上式の良い所は、creditの項とmarket riskの項が分かれており直観的にCVAを理解しやすいという所である。

### 14.2.6 Exposure and discounting
先ほどのCVAの公式で、EEはdiscountされていた。
disount factorがEEとは無関係に表現されている場合は良いが、金利系の商品で金利が高いほどdiscount curveが緩やかになる場合などは良くない。
このconvexity effectを表現する為に、T-forward measureが利用される。
T-forward measureによって、discountの影響を期待値の外に出すことができる。

Appendix14Cの導出より、式14.4の近似はEPEがdisoucntされていないことを要求する。
しかし、CVAではEEはsimulationの中でdiscountされることが多いので、discountを分けることが有用である場合もあるという点は注意が必要である。

### 14.2.7 Risk-neutrality
Chap10で、リスク中立確率と実確率の栄子湯の違いを見た。
実務的にはCVAは通常risk-neutral (parameter)で計算される。
Sect2.1の標準的な会計によって、exit priceやヘッジコストに対して価格を定義することが求められているので、CVAの計算は価格計算と整合的である。
勿論correlationがmarketで観測できなかったり、volatilityの補間、補外の仮定によりrisk-neutralとは必ずしもならない。
また、volatilityはhistoricalに推計したものより、risk-neutralに求めたものの方が大きくなる。

更に良く議論されるのは、式14.4のPDである。
Chap12でrisk-neutralの倒産確率について議論した。

* risk-neutral PD >> real-world PD
* defaultは、single-nameの流動性のあるCDSが一般的にはないので、ヘッジできない。
* 銀行のビジネスモデルはcredit riskの貯蔵所.
real-worldの倒産確率に曝されている。

上記はややacademicな議論で、多くの銀行ではCVAの報告の為にcredit spreadを使用する必要がある。
下記のように、historical倒産確率がCVAの計算で使われるケースが最近ではある。

* 小さな地方銀行は、他の地方銀行などがCVAをhistricaPDで計算していることがある為、exit priceもそのpriceに依存すると考えている
* 日本のようにIFS13の会計基準がない国

上記のようなケースはまれだが、銀行はCVAはrisk-neutralのexit priceではなく損失時の補てん額と考えている。
Chap18で詳細に議論する。

### 14.2.8 CVA semi-analytical methods
nettingやcollateralは考慮できないが、いくかの商品ではCVAの公式は簡単にできる。

upfrontにpremiumを貰うlong optionのように、正の価格しかとらない商品の場合(Appendix14D)

$$
CVA \approx -LGD \times PD(0, T) \times V
$$

ここで、\\(T\\)は満期で\\(V\\)は商品の現在価値である。

他のより高度な方法は、Sorensen-Bollierのsemi-analytical formulaである(Section10.2.2)。
式14.4のEEをEuropean swaptionの価値として表現する。

上記は、risk-neutralな近似なのでreal-worldのcalibrationには使えない。

## 14.3 IMAPCT OF CREDIT ASSUMPTIONS
PDとLGDの影響について議論する。
PDとLGDについての数値例を示すが、CVAの例としてSect14.2.4の例を使う。

* flat credit curve:300bps
* LGD:60%
* notional:1M
* CVA:1,999(0.2%)

### 14.3.1 Credit spread impact
spread(bps)が150から10000まで変化した時のCVAの変化がTable14.1である。
基本的にspreadに対してCVAは単調に変化するが、倒産に近づくとCVAが増加する。
これについてはChap18で議論する。

次に、credit curveの変化の影響を見る。
Section12.2.4で考えた5年が300bpsのupwards-sloping, flat, downwards-slopingのcredis curveに、CVAの影響を見る。
Table14.2がそれぞれのcurveの5年と10年のCVAである。
downwards < flat < upwardsの順で影響が大きくなっている。
10年の場合は5年のspreadを補外してだしており、curveの差が非常に大きい。

### 14.3.2 Recovery impact
Chap12の図12.5で倒産時のsettled recoveryについて議論した。
式14.2に式12.1のPDの式を代入すると

$$
CVA = -\mathrm{LGD}\_{actual} \sum\_{i=1}^{m}\mathrm{EE}(t\_{i}) \times \left[ \exp \left( - \frac{s\_{t\_{i-1}}t\_{i-1}}{\mathrm{LGD}\_{settled}}\right) - \exp\left( - \frac{s\_{t\_{i}}t\_{i}}{\mathrm{LGD}\_{settled}}\right) \right]
$$

概念としては、settledとactualは異なる。
もしderivativeの請求権がCDSで参照されているものと同じseniorityならば、LGD_{actual}=LGD_{settled}を仮定する必要がある。
式より、LGD_{actual}=LGD_{settled}であればLGDの1次の項は消えるので、2次の影響しか出ない。

Table14.3は、actualとsettledを同じ値にして変化させた場合とactualとsettledを別の値にして計算した例となる。

## 14.4 CVA ALLOCATION AND PRICING
nettingやcollateralのCVAの影響を見る。
nettingする場合、CVAの計算負荷が増えるので、数値計算を工夫する必要がある。

### 14.4.1 Neetting and incremental CVA
nettingするとCVAは減る。

$$
\mathrm{CVA}\_{NS} \ge \sum\_{i=1}^{n}\mathrm{CVA}\_{i}
$$

\\(\mathrm{CVA}\_{NS}\\)はnetting setの取引のCVAの合計。
\\(\mathrm{CVA}\_{i}\\)は取引iのCVA。
nettingによって、CVAは減るがこのCVAのbenefitを個々の取引どう割り当てるかという問題がある。
incremental CVAはSection10.7.2のincremental EEのanalogyでbenefitを割り当てる。

$$
\mathrm{CVA}\_{i}^{incemental} = \mathrm{CVA}\_{NS+i} - \mathrm{CVA}\_{NS}
$$

取引iをNSに加えた時のCVAの変化分がincremental CVA。

Appendix14Eより、incremental CVAについて次の公式が得られる。

$$
CVA\_{i}^{incremental} = -\mathrm{LGD} \sum\_{i=1}^{m}\mathrm{EE}\_{i}^{incremental}(t\_{i}) \times PD(t\_{i-1},t\_{i})
$$

式14.2と同じ形だが\\( \mathrm{EE}\_{i} \\)が\\(\mathrm{EE}\_{i}^{incremental}\\)になっている。
CVAはEEの線形和で、nettingはexposureにしか影響を与えない。
Incremental EEは負になりうるので、その場合はCVA benefitとなる。

EEとnettingの特徴として、incremental CVAはnettingのない単体のCVAを下回る(CVAの符号は負）ことはない。
これにより、新しい取引の時に既存の取引を考慮して取引することに意味が生じる。
Cooper and Mello(1991)はこの影響を計算しており、銀行がより競争力のあるrateを提示できることを示した。

nettingの取り扱いはCVAの取り扱いを複雑にし、多次元の問題にする。
nettingをanalyticに操作することが試みられている一方、CVAの計算はEEのsimulationにMCが要求される。

### 14.4.2 Incremental CVA example
incremental CVAの例を見る。
7年のEUR payer IRSにおけるCVAの例がTable14.4である。

* icnremental CVAは単体のCVAを下回ることはない。
nettingはexposureを増加させない。
* EUR payer IRSと似たUSD payer IRSやUSD payer swaptionはnettingの効果が少ない為、EUR payer IRSのCVAと同程度のincremental CVA
* cross currency swapやreciver swapでは、incremental CVAは増える(正に近づく）。
reviever swapでは、その変わりDVAが減る(より負になる）。

### 14.4.3 Marginal CVA
Section10.7.3のMarginal EEを式14.2に代入することで、Marginal CVAが定義できる。
marginal CVAは、CVAの影響を個々の取引に割り当てる。

Table14.5はincremental CVAとmarginal CVAのPayer IRS 7YとUSD/JPYのcross currency swapにおける比較である。
EEは図10.26に示されており、credit curveはflatで300bpsである。
marginal CVAはincremental CVAより均等になっている。

Table14.6は、incremental CVAとMarginal CVAの比較である。
incremental CVAは取引の足す順序によって結果が大きく異なる(例えば、cross currency swap)。
しかし、これは以下の理由により大きな問題とはならない。
* incremental CVAの合計は、順序によらない。
netting setは、1つのtrading deskもしくはsalespersonが特定の顧客の取引をまとめて扱う為、trading desk/salsespersonへのchargeはtotal CVAで良い。
* 顧客の取引のキャッシュフローは、受け払いに偏りがあるので、nettingの効果がそもそも低い。

Marginal CVAはfairである一方、新しい取引のmarginal CVAがどうなるか予想しづらい。

### 14.4.4 CVA as a spread
他の問題として、CVAをufrontに受け取った時に、spread CVAの変換が難しいという問題がある。
例えば、upfront CVAを受け取っているswapのrateにspreadとして調整することで、chargeが容易になる。
1つの解決策はSection14.2.5のようにrisky durationでCVAを割る。

しかし、spreadを契約に加え契約の内容が変わるとその取引のCVAも変化するという問題がある。
再帰的にCVAを計算する必要があり、Section14.2.5の例で計算した場合、spread CVAは-4.83bpsで、Section 14.2.5の-4.79bpsと異なる。
CVAが小さければ大きな問題にはならないが、長い期間の取引やcredit spreadの大きいcounterpartyの場合は問題になる。

incremental CVAでは、新しい取引のサイズによってincremental CVAのnettingの影響が変わるという点は注意が必要である。
取引の規模が大きくなるほど、nettingの利益が減る。
図14.4が取引の大きさに対するincremental CVAの図である。

### 14.4.5 Numerical issures
式14.2からわかるようにCVAは計算負荷が大きい。
時価計算用の関数を改善する必要がある。
改善の方法として多くの方法があるが、一例として

* cash flowの生成やfixingなどunderlyingの時間に依存しないの共通の機能を分ける
* 時価計算関数の最適化
* 近似とgridの使用
* 並列化
* pathwise/direct simulation
    * pathwiseはPFEの計算をする場合は必要だが、CVAの場合はそうではない。
 
図14.5は5年のIRSに対するdirect/pathwise simulationの比較である。
pathwiseは10000パスで、time gridが183である。
direct simulationはtime gridなしでdefault時点をrandomに取り、default時点のexposureのみを10000*183回計算している。

pathwiseは、direct simulationの標準偏差の9.7倍になっている。
simulation回数の平方根で収束するので、9.7 * 9.7= 94倍早い?
Amadahls' law(Amdahl 1967)より計算速度向上を簡単な式で見積もることができ、

$$
\mathrm{improvement} = ((1-P) + P/S)^{-1}
$$

\(P\)は改善可能な計算の割合で、\(S\)は計算時間の改善である。
例えば、P=0.9だとするとS=94から、totalの改善は9.1である。
但し、direct simulationはpath dependentな担保付のものやexoticsには向かない。

またEEに対するCVAの計算で、連続barrier optionsなどのpath dependentなものに対してBrownian Bridgeを使って行使確率を求め、近似する方法が提案されている。

expotic商品でAmerican-typeのものに対して、Section10.3.3で議論したように、

1. Approximation
    * 近似を用いる
2. grids
    * あらかじめ決めたgridで、underlyingの変数として将来価値を計算する方法
	* 次元が低い場合に有効
3. American monte carlo Methods
    * xVAでよく使われるようになっている

## 14.5 CVA WITH COLLATERAL
collateralの影響を考える。
式14.2からcollateralはEEの項にしか影響を与えないことがわかる。
Seciton11.3のcollateralのEEへの影響の数値例を適用する。

* zero-thershold
* two-way CSA with MTA = 0.5
* roudingは0.1

CVAは、500bpsのflat credit curveで、LGD=40%とする。
CVAのcollateralがない場合は-0.2932である。

### 14.5.1 Impact of margin period of risk
MPRの影響を見る。
CSAありなしのEEの影響は式11.5で見ることができる為、CVAへの影響も11.5を通して計算することができる。
例えば、MPR=30 calendar daysとすると、-0.075がCSAありなしでの差となる。
しかし、実際の結果は-0.131である。

図14.6はMPRを0から60 calendar daysまで変化させたときのCVAの変化である。
MPR=0のとき、CVAはほぼゼロに近い(roundingとMTAの影響でゼロにはならない）。
MPRが30の時はNO CSAの時の半分程度である。
また、Section11.5の近似で計算した場合（図の点線）はMPR=20の時は非常に良い近似になっている。

### 14.5.2 Thresholds and initial margins
図14.7はIMとthresholdsの影響を表した図である(IMは負のthresholdとして扱う)。

図14.8はIMのCVAの影響を表した図である。
エラー棒は、MPRを20daysと40daysにした時の誤差である。
IMを増やすとCVA(-CVAは減る)は増えるが、MPRの影響は大きくなる。

IMは、segregatedされている限り、CVAの計算には関与しないが、MVAにおけるコスト(Chap16)となる。

## 14.6 DEBT VALUE ADJUSTMENT

### 14.6.1 Overview
DVAはcounterpartyではなく自身の倒産をderivativeのpriceに反映させる。
DVAは諸刃の剣で、CVAを理論的にサポートするが、問題も引き起こす。
次の章で、marketではDVAを考慮せずにFVAとして影響を考慮することが主流となりつつあることを見る。
しかし、DVAを理解することとFVAとDVAの関連を理解することは重要である。

### 14.6.2 Accounting standards and DVA
CVAとDVAを考慮するBilateral CVAは、2006年にFAS 157が銀行がDVAを会計として計上することを定めたことに由来する。
FAS 157では、報告機関自身のcredit riskを負債のfair valueで形状しなければならないことを述べている。

これによりUS(と一部のカナダと大きなヨーロッパ）の銀行はDVAを報告している。
しかし、DVAの会計上の扱いは一貫しておらず、多くの銀行はこれを無視している。
また、多くの金融機関はDVAにhistoricalやblended倒産確率を使用している。

Jan/2013のIFRS 13の導入によって会計上の扱いが明確になった。
IFRS 13ではderivativeはfair valueで報告されなければならないとし、負債のfair valueに、自身のcredit riskを含まなければならないとしている。

監査役の会社として、IFRS 13はrisk-neutral default probabilityを要求(via credit spread)しており、CVAとDVAが報告されなければならない。
日本は、IFRS 13を適用していないので、DVAを報告する必要はない。

### 14.6.3 DVA and Pricing
2008年のLehman Brotheresの倒産まで、金融機関は倒産しないと思われていたので、end-userのCVAだけ考慮していれば問題なかった。
実際、金融機関のcredit spreadは小さく、格付けも高格付けだった。

金融危機後、金融機関のcredit spreadは広がり、格付けも悪くなった。
更に、interbankでとr比企する場合、CVAの損失が担保などでない場合に、価格の折り合いをどのようにつけるかという問題が起こった。

DVAは価格の対称性を保証し、価格の折り合いをつけることを可能にする。
しかし、end-userと銀行の取引のよう(銀行が価格を掲示し、end-userは必要ならその価格で取引する）に価格の対称性は必ずしも必要ではなく、DVAによって起こる問題も存在している。

### 14.6.4 Bilateral CVA formula
BCVAは、自身とcounterpartyが同様にdefaultすることを考える。
Appendix14FでBCVAの公式を導出している。

$$
    BCVA = CVA + DVA
$$

$$
    CVA = -\mathrm{LGD}\_{C}\sum\_{i=1}^{m}\mathrm{EE}(t\_{i}) \times PD\_{C}(t\_{i-1}, t\_{i})
$$

$$
    DVA = -\mathrm{LGD}\_{P}\sum\_{i=1}^{m}NEE(t\_{i}) \times PD\_{P}(t\_{i-1}, t\_{i})
$$

添え字のPとCはpartyとcounterpartyである。
CVAは式14.2と同じである。
DVAはEEがNEEになっただけである。

式14.4の拡張として

$$
    BCVA = -EPE \times \mathrm{Spread}\_{C} - ENE \times \mathrm{Spread}\_{P}
$$

EPE = -ENEを仮定するならば、\\(BCVA = -EPE \times (\mathrm{Spread}\_{C}-\mathrm{Spread}\_{P}) \\)となる。

### 14.6.5 Close-out and default correlation
BCVAはいかの3つの要素を無視している。

* Survival
    * partyかcounterpartyの一方がデフォルトしたら取引は終わる。
	よって、一方がデフォルトしたらもう一方はその後の損失を考慮する必要はない。
* Default correlation
    * 二者間の相関は考慮していない。
    correlationが0でないなら正ならDVAとCVAに影響を与えるｌ。
* Close-out
    * Seciton7.1.3で議論したように、EEやNEEは実際のclose-outの仮定を考慮していない。
	仮定として、デフォルト時のMTMで取引が終了することを仮定している。
	close-outの仮定は、生き残ったpartyがrisk-freeではないとしているので、考慮する必要がある。

上記に関連した研究として

* Gregory(2009a)は、survival propabilityとdefault corellationについて研究している。
* Brigo and Morini(2010)はclose-out assumptionについて研究されている。

counterpartyが倒産した場合、close-outにおいて倒産時のrepalcement costを計算する。
この時partyのDVAは残っており、BCVAにおいては　partyのDVAを考慮してclose-out amountが計算するかどうかが重要となる。

* Market quotation
    * DVAは相手からみたCVAだが、その値は担保による。
    DVAを考慮する為には、無担保のmarket quotationを知る必要があるが、一般にmarketのquoteは担保付でquoteされている。
* Close-out amount
    * 2002 ISDA documentationでは、実際のmarket quotationは要求しておらず、Determining Partyのcreditを考慮しているかもしれないと明記してある。

close-outの仮定を定義するのが難しいだけでなく、定量化も難しい。
現在のBCVAを決める為にデフォルト時点のfuture BCVAを決める必要がある。
Brigo and Morini(2010)はloanについて、DVAがclose-outに含まれるならば、この問題は起きないことを示した。
Gregory and German(2012)は、two-sidedの場合にsimpleな結果はないが、式14.10が良い近似になることを示した。

一般的にmarketの参加者は複雑な方法をとらず、単純に生存確率で調整を行っている。
例えば、Ernst and Young Survey in 2012では、19の報告のうち6個がCVAとDVAを生存確率の調整でだしており、7個が式14.10で算出し、残りはDVAを出していなかった。

### 14.6.6 Example
BCVAの計算例。
Section14.2.4のCVAの例をbaseNi計算する。
EEとNEEが図14.9になる。
EE(CSA)とNEE(CSA)は、two-way, zero-threshold CSAの場合のEE, NEEである。
MPR=20 calendar days。

credit spread curveがflatで、counterparty200bps, party100bps、LGD=60%とした場合のCVA, DVAがTable14.7である。

担保付の場合符号が変わっており、利益ではなくcostになっている。
CVAだけの場合は、CSAは利益になるが、DVAを考慮する場合は必ず担保を入れることによるメリットは生まれない。
しかし、担保によってPFEや資本規制の影響を軽減する効果はある。

### 14.6.7 DVA and own-debt
会計においては、負債の価値を計算する際自身のcredit rsikを考慮するようになっている。
例えば、2006年のFinancial Accounting Standards Board of the United Statesが発行したSFAS 157において、負債の計算の際に自身のcredit qualityを考慮することができるとしている。
International Accounting Standards Board(IASB)によるIAS 39のamendmentsや2013年のIFRS 13でも同様である。

DVAは銀行にとって問題となっている。
British banksの利益は、自身の負債の価値が4 billion euro下がったことによるものである。
DVAは、自身のcredit qualityが下がった時に大きな会計上の利益を生むものになっている。

現在では、DVAを企業のperformance計測に利用しないことが多くなっている。

### 14.6.8 DVA in derivatives
derivativeのDVAはヘッジに基づいている為より厳格に扱われている。
DVAの批判

* DVAの利益は簡単にマネタイズできない。
* DVAから得られる利益は、ほかの要素(のれん代など)を無視している為、適当ではない。
    * Kenyon(2010)はDVAを使用するなら、のれん代も自身のcredit riskを考慮する必要があることを示した。
    のれんの損失は、DVAによる利益と対比される。

DVAの利益をどのようにmonetiseするかに対して次の意見がある。

* Defaulting
    * 倒産する時にDVAの利益を得る。
    自分の生命保険で利益を得るのと同じで、難しい。
* Unwinds and novations
    *  取引をcloseさせたりnovationしたりしてDVAの利益を得る。
    例えば、monolineは銀行との取引の一部をcloseし、銀行にCVAによる損失を負わせ、DVAによる利益を得た。
    monolineのMBIAはmulti-billion dollarのデリバティブのDVAをモルガンスタンレーから得た。
    これは、次のようにして起きた。
    monolineがデフォルトに近づいた時銀行は実際のデフォルトより前に取引を終了させようとした。
    実際にはmonolineのcredit qualityが急激に下がらない状況で、銀行は多くの取引を手放した。
* close-out process.
    * Section14.6.5で述べたようにclose-outプロセスもDVAの利益得る機会えある。
    Lehman brosersの時のようにこれはcommonである。
* Heding
    * ヘッジによりDVAの利益を得る。
    CVAの単純なヘッジはcouterpartyのcreditをshort(CDS買い)することである。
    DVAのヘッジは自身のcreditのlong（CDSの売り）であるが、これはできない。
    代替として、類似企業のCDSを売るという方法もあるが、correlationが100%でない為完全なヘッジとはならない。
    Lehman Brothersの倒産の時に、DVAのヘッジとしてLehmanのCDSを売っていた銀行もあったが、その銀行は倒産しなかった。

DVAはmonetiseが難しく、Basel commitee(BCBS 2011c)では、DVAはCVAのcapital chargeから除外されるべきだと決めた。
これにより、riskyな銀行が低いcapital chargeとなることを防いでいる。

図14.10はDVAを価格付けに反映させているマーケット参加者の割合を示している。
fullyと回答している場合でも、すべての取引でDVAを考慮しているわけではない。(例えばDVAがCVAより大きい時）

現在では、DVAをfunding benefitとしてとらえる。
実際、自身の社債を買い戻すことは自身のCDSを売ることと同様の意味を持っている。
多くの銀行は、DVAをfunding benefitとしてとらえている。

## 14.7 SUMMARY


