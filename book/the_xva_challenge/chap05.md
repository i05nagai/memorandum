---
title: 5 Netting, Close-out and Related Aspects
book_title: The XVA Challenges
book_chapter: 5
---

# 5 Netting, Close-out and Related Aspects.

## 5.1 Introduction

### 5.1.1 Overview
　この章では、Nettingとclose-outについて述べる。
* Nettingは、Counterparty riskを軽減する伝統的な方法
* close-outは、倒産したCounterpartyに対する契約の解決及び終了のプロセス
nettingとclose-outについて延契約及び法律の観点、xVAへの影響とrisk reductionの観点からのそれらの影響を述べる。

### 5.1.2 The need for netting and close-out
 OTC derivatives marketは、銀行やヘッジファンドのような参加者のポジション変更によって、変化が速い。
 さらに、derivatives portfolioは、お互いにhedgeを行うことなどによって、多くのtransactionを含んでいることがある。
 これらの取引はcashflowや資産の契約上の交換が行われる。 
 これらは理想的には単一の支払いに単純化できる(nettingできる)
 更にそのような状況では、counterpartyのデフォルトは非常に難しいイベントとなる。
 デフォルトしたcounterpartyと数千の様々なderivativesの取引を持っているとする。
 これらの取引を即座に終了させ、全てのポジションをrehedgeする必要がある。
 更にこの場合、デフォルトしたcounterpartyに貸しているものと借りているものがoffset出来た方が望ましい。

 nettingとclose-outをより理解する為に、Figure5.1の状況を考える。
 party Aとparty Bが双方で取引しており、2つのtransactionがあるとする。
 この状況は潜在的に複雑すぎる。
1. Cashflows
    * Party AとBは、transaction1, 2に関連したcashflowや資産の交換を定期的に行っている。
	しかし、同じ日にcashflowが交換される場合gross amountのsettlement riskが発生する。
	この場合、net amountをやり取りした法が好まれるであろう。
2. Close-out
    * AかBの一方がデフォルトした場合、生き残った方は支払われない取引がある一方、支払わなければならない取引を持つ。
	これは、支払いか他のcounterpartyにtransactionを移し替える能力の不確実性を生み出す。
近年、OTC derivativesのrisk経験の必要性が重要視されている。
例えば、Lehman Brothersの倒産は、OTC derivativeの資産や負債の評価と、異なった債務のoffsetに対する能力に関連した訴訟を引き起こした。
これは、counterpartyのデフォルトが起こったときの処理が定義されたドキュメントの重要性を示した。

### 5.1.3 Payment and close-out netting
 Bilateral OTC derivatives marketは歴史的に、お互いが借りているものをoffsetできるnetting方法として発展してきた。
 次の2つのメカニズムがSection 5.1.2で上げられた2つの点に関連して、nettingを促進する。
* Payment netting
    * partyに同じ日におこるcashflowをnetする能力を与える。
	これはsettlement riskに関連する。
* Close-out netting
    * 倒産者と非倒産者の間で全ての契約を終わらせることを許すもの。
	全ての取引の価値をoffsetする。
	これは、counterparty riskに関連する。
derivativesのnettingの法律は、多くの国の主要なマーケットに適用されている。
International Swap and Derivatives Association(ISDA)は、Master Agreementsのclose-outとnettingの条項を指示する専門家の意見を得ている。
37の国はnettingを強制する法律をもっている。
しかし、nettingがデフォルトシナリオで明確に強制されない地域も残っている。

## 5.2 DEFAULT, NETTING AND CLOSE-OUT
### 5.2.1 The ISDA Master Agreement
 counterparty riskを減らし、効率性を増加する標準的なドキュメンテーションの発展んあしに、OTC derivatives marketの急速な発展はなかっただろう。
 ISDAは、OTC derivativesの実行者に対する取引機関である。
 OTC derivativesの標準的なドキュメントはISDA Master Agreementで、1985年に最初に導入され主要なマーケット参加者に使用されている。

 ISDA Master Agreementは、bilateralのフレームワークでOTC derivatives取引を統治する条項や条件を含んでいる。
 ?Multiple transactionsは、無期限の単一の契約を形成する一般的なMaster Agreementの下でカバーされている。
 Master Agreementsは、共通のcore sectionと当事者間で合意する調整可能な条項を含んだscheduleで構成されている。 
 これは、nettingや担保、termination event、デフォルトの定義、close-outの手続きなどの条項を定めている。
 これによって、法律上の不確かさを軽減し、counterparty riskを軽減するメカニズムを提供している。
 個別の取引の条項は、一般的な条項を定めたtrade confirmationを参照し定めている。
 Master Agreementsのの合意はかなりの時間を要するが、一度契約が完了すると、Master Agreementの下に個別のtradeは契約される為、契約の変更や更新が不要となる。
 基本的に、EnglandやNYの法律が適用される。

 counterparty riskの観点から、ISDA Master Agreementは次のリスク軽減の特徴を持っている。
 * 担保の差し入りに関する条項(6章)
 * デフォルトとterminationのイベント
 * 全ての取引は1つの単一の債務としてnetされる。
 * close-out processのシステムが定義されている。

### 5.2.2 Events of default
counterparty riskに関連して、デフォルトイベントは契約期限及びclose-out proessの開始前の取引の終了を引き起こす。
Master Agreementsでカバーされているデフォルトイベントは、
* 支払いとderliverの不履行
* Agreementの違反
* Credit support default
    1. 適格担保や金利を差し入れること怠った場合
	2.  CSAで規定されている債務やmaterial agreementの履行を怠った場合。
	3.
* 誤解(misinterpretation)
* 特定金融取引におけるデフォルト
* cross default
* 倒産
* 想定していない合併
上記に共通しているのは、支払いの不履行と倒産である。

### 5.2.3 Payment netting
 payment nettingは、counterparty間の同じ取引の同じ通貨の支払いのnettingである。
例えば、固定対変動のIRSの支払いを考える。
例えば、このIRSは、ある特定の日にA->Bの60の固定の支払いがあるとB->Aの100の変動の支払いがあるとする。
この時、payment nettingはB->Aへ40支払うことを指す。
partyは同じ日の同じ通貨の複数の取引の支払いをnetすることを選択するかもしれない。
これは、事務負担とsettlement riskを軽減する。

 Settlement riskはFX marketでも重要である。
 一方の通貨を支払い他方の通貨を受け取るようなFX Marketの場合、netして支払いをするのは難しい。(payment cityが異なる為)
 FXのsettlement riskを軽減する為に、銀行はContinusou Linked Settlement(CLS)と呼ばれる組織を2002年に設立した。
 例えば、Bank Aが€100 millionをLSに届け、Bank Bが$125 millionをCLSに届けるとする。
 両方ともCLSに届けられたら、CLSがAとBニ支払いをする。
 これは、Payment versus payment(PVP)と言われる。
 settlement riskは、multilateral nettingによっても減らすことができる。

 Payment nettingは、同じ日に起こる支払いから発生する全てのriskを減少させる単純なprocessである。 
 しかしながら、operational riskは残る。
```
    Case Study: The case of KfW Bankengruppe ("Germany's dumbest bank")
	Lehman Brothersの問題が起こった時、多くのcounterpartyはLehman brothersとの取引をやめた。
	しかしながら、国有のドイツの銀行のKfW Bankengruppeは、彼らが"automated transfer"と呼ぶ€300mのLehman Brothersへの送金を倒産直前に行った。
	これは、ドイツの新聞紙がKfWを"Germany's dumbest bank"と呼ぶ講義を引き起こした。
	運営委員会のメンバーの二人とrisk-contorl部署のheadが停職となった。
	二人の内一人は後の解雇に対してbankを首尾よく訴えた。
```
 KfW Bankengurppeの取引は、euroをLehmanに支払いdollarをKfWに支払うCCSであった。
 Lehman Brothersが倒産を宣言した日、KfWは€300mの自動化された送金を実施したが、Lehmanはdollarを支払うことはなかった。
 今では、CLSによってこの手のCCSは安全に取引できる。
 もし、KfWが支払いを差し控えていたならば、Lehman Brothersの財産権の管理者から意義を申し立てられていたかもしれないことは付け加えておかなければならない。

#### 5.2.4 Close-out netting
 今まで述べたように、個別のcounterpartyに対して多くの異なるOTC derivative transactionを持つことは、珍しいことではない。
 そのような取引は単純ないし複雑かもしれないし、異なるasset classに股がった幅広い商品であったり、狭い商品かもしれない。
 更に、取引は（特に銀行の立場から）次の3つのカテゴリーに分類される。
 * hedge(or partially hedge)取引を構成しており、取引の価値が反対方向に動く取引。
 * transactionのcancelという点で、逆側のtransactionが実行される。
 従って、二つの取引が等しく反対の値であれば、もとの取引はcancelされる取引。
 * 大部分が独立なtransactions。
 つまり、異なるasset classや異なるunderlyings

倒産の手続きは、長く予測できないものである。
手続きの間、counterparty riskの損失のように、手続きの終了に関する不確かさによって妥協される。
破産した企業の借金を保持している債権者は、既知のexposureを持っており、最終的な回収額は不明であるが、回収額を推定し上限を定めることはできる。
しかし、hedged positionの維持のように定期的なrebalancingが必要となるderivativesにはあてはまらない。
更に、counterpartyがデフォルトすうと、cachflowは発生せず、残ったpartyはreplacement contractを必要とする。

payment nettingがsettlement riskを減らす一方、close-out nettingはpre-settlement riskを減らすのでcounterparty riskに関連している。
Nettingの同意は、同じcounterpartyのtransactionのoffsetの利益を認識する為に重要である。
close-out nettingは、タイムリーな契約の終了と全ての取引のnetした価値の清算を許すことを目的としており、counterpartyがデフォルトした時施行される。
close-out nettingは次の2つの要素からなる。
* Close-out
    * デフォルトしたcounterpartyとの取引を終了し、契約上の全ての支払いをやめる権利
* Netting
    * 取引全体の価値をoffsetし、*net balance*と言われる正と負の価値の和を決定する。

close-out nettingはportfolioの合計を反映したnet amountでの清算とデフォルトしたcounterpartyに対する全ての契約の終了を許す。
要するに、close-out nettingによって、全てのカバーされた取引を1つの取引へと潰すものである。
もしも、生き残ったpartyがお金を借りているならば、その金額に対して破産債権を作る。
close-out nettingは生き残った機関に取引の利益と損失を即座に知ることを可能にし、効果的に倒産の順番待ちを飛び越えることを可能にする。(Figure5.3)
close-out nettingは、デフォルト時点のMTMにのみ依存し、cashflowには依存しない。

Nettingはexposureを減らす方法として重要だが、デフォルトイベントにおける取引のclose-outに関連した複雑さを減らす点においても重要である。
OTC derivatives marketにおいて、生き残ったpartyはデフォルトした取引のreplaceを試みる。
nettingなしでは、取引と額面の総数がreplaceされ、marketの騒ぎを更に引き起こす。

### 5.25 Prodcut coverage and set-off rights
いくつかの機関は、IRやFX, commodity, equityやcoredit productと同様にloanやrepoのような多くの金融商品を取引している。
nettingをこれらの全て、または殆どの商品に適用する能力は、exposureを減らすために求められる。
しかし、異なる地域の異なる法人によってbookされた取引の為に、nettingの法的強制力について法律上の問題が起こる
nettingによって引き起こされるoperational riskや法律上の問題は無視されるベキものではない。

Bilateral nettingは、一般的にOTC derivatives、repo-style 取引、on balance-sheet loasnとdepositで評価される。
cross product nettingは、それらのカテゴリーの中で可能である。
例えば、IRとFXの間の取引など。
しかし、商品カテゴリをまたがった取引(例えば、OTC derivativesとrepos)は、ドキュメントが異なるので、ストレートにはできない。

しかし、*set-off*といわれる概念がある。
set-offは、close-out nettingに近い概念で、counterparty間の2つの債務から、支払いの差を表す新しい1つの債務を作り出す。
一般的にset-offは実際の債務に関連している。
一方、close-out nettingは計算額に関連しているだけである。
set-offは異なる法律の管轄地域で扱うことができるが、ときどきclose-out nettingと互換がある言葉として使われる。
set-offは、OTC derivativesを表すISDA close-out amountに対して他のAgreementからoffsettingのamountを適用される。
例えば、銀行がcounterpartyにloan agreementの下お金を貸していたとすると、固定金利laonを作ることでloanに関連したIR riskをIR swapを通してヘッジする。

?2002ISDA Master Agreementのもとでは、標準的なset-off条項が加えられている。
?契約終了時支払金(termination payment)のoffsetが許されている。
?他の契約に従っているpartyの支払額に対して。
(例えば、もし関連するlaon documentationがloan master agreementを許容するならば）
laonのような他のderivatives商品をset-offすることが、法律の観点から可能となる。
しかし、これは異なるdocumentの正確な言回し, 法人、法解釈など依存する。
いくつかの銀行では、CVAやexposureを減らす為にloanやderivativesの契約間のoffsetについて調査をしたが、これはstandard market practiceではない。

### 5.2.6 Close-out amount
close-out 金額は、デフォルトのシナリオ時にあるpartyが他のpartyに借りている金額を表す。(デフォルトした企業でもしてない企業でもどちらでもOK?）
もしこの金額が、デフォルトしてないpartyから見て正であるならば、デフォルトしたpartyの財産に対して請求権を持つ。
もし負ならば、デフォルトしたpartyに支払う義務がある。
デフォルトpartyは請求に対して全額支払うことはできないが、請求の額を確定することが重要である。
partiesはほぼ確実に同意しないので、適切なclose-outのきめることは手間がかかる。
デフォルトしてないpartyは、経済的に適切なclose-out amountとして、repacement transactionにかかくる費用(replacement cost)を考慮する。
デフォルトしたpartyは、bit-offer spreadなどが含まれたこの評価額に同意しそうにはない。

replacement costの概念は、"market quotation"法と言われるclose-out amountを定める方法を生み出した。
1992年のISDA Master Agreementでは、close-out amountを定めるもう一つの方法として"loss method"を提供している。
それぞれ以下の特徴を持つ。
* Market quotation
    * デフォルトしてないpartyが、market-makersからの3つのquoteの最小値を取り、close-out amountを決定する為に、これら最小値の平均を使用する。
	特定のtransactionに対するマーケットの流動性などを考慮した額を得ることができる。
	そのような流動性はLehman brothersのような大きいデフォルトの後では常にあるわけではない。
	exoticなものや非標準的な商品では特にそうである。
	よって、大きなデフォルトイベント後の複雑な取引に対してpriceを出すmarket-makersを見つけることが問題になる場合もある。
* Loss Method
    * 全ての取引にたいするmarket quotationを得ることが難しい場合に利用される代替的な方法である。
	そのような場合、close-out amountを決定するpartyは、誠実さと妥当な仮定の下にその損失を計算しする必要がある。
	決定する側のpartyに大きな裁量が与えられることになり、主観的になる。

Makret quotationは安定したmarketの状況で、複雑でない取引については良く機能する。
しかし、1992からより複雑なOTC derivatives取引が増え始めた。
これによって、market quoation amountの決定について無視できない数の議論が起こり始めた。
更に、loss methodは主観的すぎ、決定する側のpartyへの裁量が大きすぎるという意見もあった。
loss methodはEnglandとUS Courtによる矛盾する決定も自体を複雑にした。

上記の問題とmarketの発達(外部のpricing sourceが確保できる環境の発達）により、2002 ISDA Master Agreementはmarket quotationとLoss methodを*close-out amount*という単一の定義へと置き換えた。
これはclose-out amountを決定するparty対して十分な柔軟性を適用し、market stress下における複雑な商品のmarket quotationを得る為に起こる実務的な問題を解決することを意図して作られた。
close-out amountは、実際にトレード可能な価格を要求せず、商取引上の合理的な価格に達する為の内部モデル、パブリックなマーケットデータと価格のパブリックソース、indicative quoatationに依るという点でmarket quotationを弱めたものである。
更に、決定する側のpartの信用度が考慮され、fundingとhedgeも考慮されるかもしれない。

要するに、market quotationは実際の企業のquoteを使用するという点で客観的な方法である。
loss methodは、determining partyがlossとgainを決定するという点で柔軟であった。
close-out amountは、determining partyに決定法の選択を与えるという点で柔軟であるが、決定法が商取引として妥当であることを保証するを目的としている。
2002 ISA Master Agreementの後も、いくつかのpartyは1992 ISDA Master Agreementのmarket quotationがより客観的であるという理由で使い続けた。
しかし、global financial crisisの時、この問題はもう一度脚光を浴びることとなった。
結果として、2002 close-out amountを使うというtrendが形成されることとなった。
2009年、ISDAはcounterparty対counterpartyのbilateralのドキュメントの変更ではなく、1つのドキュメントにサインするということで古いISDA Master Agreementをclose-out aountに変更できるような新しいprotocolを提供した。

close-outについての契約上の定義は、counterpartyのデフォルトの経済的意味定める為重要であり、credit exposure(chap 7)の定義やCVA(chap 14)などの関連した概念のキーともなっている。

### 5.2.7 The impact of netting
close-out nettingはcounterparty riskに対する大きな軽減策であり、OTC derivatives marketの発展に重要である。
nettingなしでは、OTC derivatives marketの現在の流動性と大きさは、維持できないだろう。
nettingをするということは、marketのcredit exposureの増加が、marketのnotionalの増加の割合より少なくできるということである。
?Nettingは、資本規制の中で、銀行がOTC derivative businessを成長させることができるという面でも重要である。
derivatives marketの集中と拡大は、nettingの範囲を増加させており、ここ10年ではnettingによってexposureは90%近く減少している。(Figure 5.4)
しかし、netされたポジションは、本質的にsystemic riskをつくるunderlyingのgrossポジションより危険である。

Nettingは、OTC derivatives Marketのdynamicsに微妙な影響を持つ。
ポジションを消すtradeをしたい機関があったとする。
他のmarket参加者とポジションのoffsettingを実行し、market riskを除こうとすると、もとのcounterpartyと新しいcounterpartyのcounterparty riskをかかえることになる。
機関がポジションを消すtradeに対して強い理由があることを知っているcounterpartyであれば、最大限の利益を引き出す為に好ましくない条件を提供するかもしれない。
機関は、この望まない条件を受け入れるか、別のcounterpartyと取引をし、counterparty riskを受け入れるかしかない。

上記のポイントは異なるrisk exposureを持った複数のポジションを確立する場合にまで及ぶ。
IRとFXのhedgeをしたい機関がいたとする。
これらの取引は不十分な相関があるので、同じcounterpartyに対してhedgeを実行すると、全体のcounterparty riskは減り、機関はより好ましい条件を得るかもしれない。
しかし、これは同じcounterpartyと継続的な取引をする同期を生み出し、潜在的な集中リスク(concentration risk)を生み出す。

更なるnettingの影響は、市場参加者が特定のcounterpartyのriskの増加の知覚に反応する方法を変化させることができる点である。
credit exposureがgross positionによってdriveされたとする(つまりnettingなしの場合)と、問題を抱えたcounterpartyとの全ての既存の取引と全ての新しい取引を終了させる強い動機を持つだろう。
そのような行動は、問題を抱えているcounterpartyの財政難を生む結果となる。
nettingがある場合は、current exposureがない(MTMが負)ならば、機関は殆ど心配する必要がない。
一方PFEには関心が払われ、担保が要求されるかもしれない。
counterpartyが窮地にある時にnettingはそのような関心を減らし、結局systemic riskを減らす。

興味深いことにnettingの利益はOTC derivativesのclearingの義務化という脅威の下になりたっている。
なぜならclearing可能な取引はポートフォリオから取り除かれ、その結果残ったbilateralポートフォリオから得られるnettingの利益も取り除かれる。
Chap9で詳細に議論する。

### 5.3 MULTILATERAL NETTING AND TRADE COMPRESSION
### 5.3.1 Overview
nettingはOTC derivatives exposureを1桁%にまで減らすが、更に削減する方法を見つける必要がある。
典型的なISDA netting agreementsは、ただ2つのcounterpartyの間の取引である。
trade compressionは、更に一歩踏み込み、multilateral nettingを達成する。

compressionはmarketのポジションのgross notionalを最小化することを目的とする。
market risk特性は帰ることができないが、以下を削減する可能性を持つ。
* multiple Counterpartyのexposureを減らし、counterparty credit risk減らす。
* 取引の数を減らし、operational costを減らす。
* advanced modelを使うことなし(Current exposure method discussed in Section 8.2)に、銀行の資本規制の額を減らす。
* margin period riskが増加するadvanced modelの銀行の資本規制の額を減らす。
* Basel IIIがgross notionalに重点をおいていrので、leverage ratio(section 8.8.2)のようなものも減少させる。
* 取引のtransactionはnetで同等の取引と取り替えるので、nettingにおける法的不確定性を減らす。

### 5.3.2 Multilateral netting
party AはBに対するexposureをもっているとし、BはCにexposureを持っているとし、CはAに対するexposureも持つとする。
bilateral nettingを使っても、この3つのpartyはexposureを持つ。
ある種のtrilateral nettingを3者間で行うことでFigure5.5のように更なるnetを可能とするだろう。

### 5.3.3 Bilateral compression services
為替取引におけるcompressionと中央清算されたマーケットは、中央機関を通したclearingとtradingの自然な拡張である。
しかし、bilateral OTC marketにおけるmultilateral nettingの実現は、自明ではなく、手続きを促進する為にある種の第三者機関が必要となる。

(主要通貨の)IRSやsingle-name, index CDSやtranches, energy swapsなどの主要なOTC derivatives商品をカバーしているcompression serviceを提供するTriOptimaのTriReduce serviceの動機でもある。
これは、OTC derivatives marketのexposureを減らすのに役立ち、特にcredit derivativesのような急速な発展をしているareaで重要である。

compressionはOTC derivativesポートフォリオが時間とともに発達したが、トレーディングの性質から余分なものを含んでいる。
これは、取引が全体のrisk特性をかえることなしに、gross notionalと取引の数を減らすことができるということを提案している。
これは、operational costを減らし、counterparty riskを最小化する。
counterpartyがデフォルトした時にreplaceする必要がある契約が減ることでsystemic riskも減らすかもしれない。
compressionは、最大限のmultirateral nettingを達成した時、限界収益逓減を持つ。
counterpartyのcredit qualityは互いに好感可能である必要がある。（同程度のcredit qualityである必要）

?典型的なcompression cycleは、参加者たちが関連する取引を全て提出し、
?関連する取引とは、trade-reporting warehouseに対して相互参照された
?counterpartyの取引に適合した。
最適な解は、符号を変えたり、取引するのcounterpartyの数を増やしたりするかもしれない。
これと他の理由の為に、参加者は制限(counterpartyに対するtotal exposureや参加者の内部的なcredit limit)を与えることができる。
参加者はtoleranceを明記しなければならない。
?何故なら、compressionの目的は、market riskを減らしとcash neutralにしながら、MTMとrisk特性の小さな変化を許容することである。
?compressionの適用範囲を増やすことができる。
trade populationとtoleranceに基づいて、変更はmultilateral trade populationにおける余剰分に基づいて決定される。
手続きが一度終わると、変更は法的拘束力を持つ。
そのような変更は取引の調整によって効力を発揮することができ、新しい取引を開始し、他のcounterpartyにnovationをする。

compression serviceは中央清算と補完的である。
compressionによって、total notionalと契約の数を減らすことは、clearing memberのデフォルト時にclose-out positionの複雑さの減少とより効率的なoperationとなる。
しかし、トレードは執行された後すぐにclearingされ、trade compressionはCCP levelで行われる。

将来的には、より高度なcompression servicesの発展がOTC derivativeの取引のcost最適化において重要であるかもしれない。
特に、bilateralとcentral clearingされた商の両方に渡ったcompressionとgross notionalの代わりにxVAのような指標を使うことが重要になるかもしれない。

### 5.3.4 The need for standardisation
OTC derivativeは標準的な商品がない為、compressionできない。
CDS marketは標準化がなされた良い例。
financial crisisの後、主要な銀行がcompressionと中央清算を促進する為にISDAと共にCDS契約の標準化を行った。(maturityとcouponに関して）
現在は、CDSはfixed premiumとupfrontの支払いとtermination dateが3/20, 6/20, 9/20, 12/20のみとなっている。
これによって、single-name,indexとmaturityで一致すればバケットできるようになった。(以前はcouponとmaturity dateが異なる可能性があった）

契約の標準化は常に可能なわけではなく、IRSはできない。
IRSの場合は*coupon blending*のような同じ満期で異なるcoupon rateのスワップを組み合わせるような方法が必要となる。

### 5.3.5 Examples
Compressionの例。
Figure5.6を例にする。
図中の数値はnotionalだが、exposureや他の指標でも良い。
数値の合計*2(=gross notional)は1250。

compressionの目的は、counterpartyのnet positionを変えずににgross notionalを減らすこと。
上記に伴う問題は
1. 何を最小化するか？
    * total notionalを単純に最小化
	    * でかいポジションにペナルティがついていなかったり、非ゼロのポジションの数が多くなったり。
	* notionalの二乗和の最小化
	    * でかいポジションにペナルティがつく
	* ポジションの総数
	    * 非ゼロポジションの数が減る
2. 最適化に対して制約が必要
    * 単一のcounterpartyに対するポジションの大きさ
	* 取引のない場合は、取引を加えない
	    * Figure5.6の場合は1と3に直接の取引がないので、最適化後も取引はないままが望ましいかもしれない。
上記を達成するアルゴリズムは色々あるが、商業的な応用の為にシンプルなものが良いかもしれない。

nettingの例を見る。
total notionalを減らす方法は、nettingの閉路を探すこと。
* counterparty2, 3, 4の間で、60, 70, 85のnettingをし、60へ減らす(Figure 5.7)
* total notionalは1250から890(=1250 - 180 * 2)へ。
このプロセスを続けていくとFigure5.8の左と右の二つの解が得られる。
* Figure5.8の左側
    * counterparty4から5へのexposureが逆転している。
	* Notionalの合計は130
* Figure5.8の右側
    * counterparty4から5へのexposureが逆転している。
	* counterparty1から3への新たな取引が発生している。 
	* Notionalの合計は110

Table5.1はCDS compressionの単純な例。
3つのoriginal contractが1つのCounterpartyAに対する契約にcompressされている。
Couponはoriginalの3つのcontractのcouponの加重平均(200 * 40 - 150 * 25 - 300 * 10 = 5 * 250)となる。

## 5.4 TERMINATION FEATURES AND RESETS
期間が長いderivativesは、現在のexposureが少なく管理できる一方、時間がたつとexposureは大きく管理できないレベルになる。
この問題を軽減する方法は、大きなexposureを減らす行動を許す機能を持つことである。
これは、reset agreementsとbreak clauseのようなtermination featureの役割となる。

### 5.4.1 Walkaway features
今ではないが、昔のOTC derivativesは*walaway* or *tear-up*機能がついたものがあった。
これは、counterpartyがデフォルトした時に取引をキャンセルすることを許す条項である。
これは、counterpartyに借金がある場合にのみ利用されていた。
しかし、この機能はcredit exposureを減少させない一方、生き残ったpartyがcounterpartyにかりている額を清算する義務なしに、支払いをやめるという利益を得るものである。
この契約は1992 ISDA Master Agreement以前は普通であったが、今では標準的なISDA documentationには含まれていない。
しかし、1992年からの取引にはしばしば使われている。
?Walkaway 機能はcounterparty riskそれ自身は軽減しないが、損失のriskをoffsetする潜在的利益を提供する。

Walkawayは1990のDrexel Burnham Lambert(DBL) bankruptcyの例がある。
興味深いことにDBLのcounterpartyはwalkaway機能を使用せず、DBLに対する負債を清算した。
これは以下の理由による。
* walkaway agreementの法的正当性を示すcostに対する利益が少ない
* DBLの倒産で利益を得たというreputation costを懸念した

walkaway agreementなしで、institutionが利益を得る方法はデフォルトしたpartyとの契約をclose-outすることなしに支払いをやめることである。
次の興味深い例がある。
Enron Australia(Enron)とTXU Electricity(TXU)はelectricity swapsをEnronが2002年につぶれた時に取引していた。
この取引はwalkaway機能を扱っていなかったものの、ISDA documentationはTXUのEnronに対する$3.3mのMTMの支払いを避けることを支持するものであった。
Enronの清算人はTXUを訴えたが、New South Wales Supreme Courtは、TXUがここの契約が終了するまでは支払う必要がないという判決を下した。
(支払いがキャンセルされたのではなく、契約終了まで延期になった）

同様の例が、Lehman Brothersのときにも起こった。
Lehman BrothersのcounterpartyがTXUのようにcounterpartyにとってout-of-the-money(Lehmanにin-the-money)の支払いをやめた。
Lehmanの役員はUSとEnglandの裁判所に訴えたが、*walkaway event*の強制行使に異なる判決を得た。
* US
    * 支払え
* England
    * 支払いの差し控えを支持

walawayは基本的には避けるべき。
counterpartyの倒産で、利益を得る動機付けになるので、モラルハザードを引き起こす。

### 5.4.2 Termination events
ISDA Master Agreementの重要なものに、Additional Termination Event(ATE)がある。
ATEは、OTC derivativesの取引をある状況で終了することを許すものである。
* counterpartyの格付けが下がったら終了
* 格付けされていない場合(hedge fundなど）は、時価総額、純資産、key manの異動などで終了
ATEは、Counterpartyの信用が悪くなった時に何らかの対策を取るようにしたり、取引を早期終了できるようにする為counterparty riskを軽減する。
比較的良い格付けのpartyで、長い期間の取引をするときに特に良い。
そのような取引はMTMが正になったり、counterpartyの格付けが下がる可能性が十分ある。
ATEが行使荒れると、partyはその時点のreplacement valueで取引を終了させる。
これは、replacement costの定義の問題に発展する。(close-out amount同様)
ATEは、取引の終了だけでなく、担保の差し入れや第三者機関のcredit protectionの提供などもある。

ATEをISDA Master Agreementの下で全ての取引に適用する代わりに、*break clause*または*mutual put*と呼ばれる条項を取引ごとに参照する方法もある。
長い期間の取引(e.g. 10y以上)に対してはメリットがある。
break clauseは、義務、選択可能であったり、トリガーであったり、片方ないし両方のpartyに適用されるかもしれない。

ATEの危険性
* Risk reducing benefit
    * global financial crisisで観測されたようなcredit qualityの低下を無効化するは難しい。
* Weaknesses in credit ratings
    * credit qualityが下がるとexposureが増加するので、credit qualityが下がる前にbreakは実行される必要がある。
	最後の手段として利用するとsystemic riskの問題があるので有用ではない。
	格付けはcredit qualityの動的な尺度ではないので、格付け機関が格付けをさげるときにはbreakを実行するのは難しい状況にある。
	これはmonoline insurerのcounterpartyにみられた。
	実際Basel IIIではrating-based triggerに対する資本配分に対するメリットはない。

更に、格付けはネガティブな格付けの情報に対して、反応が遅く、次の問題がある。
* Cliff-edge effects
    * おおくの場合格付けの1単位の低下によって複数のcounterpartyが取引を終了させようとし、他のriskを引き起こすかもしれない。
	AIGが良い例(Section 6.2.2)
* Determination of valuation in the envet of a termination
    * close-out amountでも述べたが、妥当な価値の算出が難しい。
* Relationship issue
	* break clauseを実行するとcounterpartyとの関係が悪くなる。
	* 銀行の場合顧客との関係の為基本的に実行できない。
* Modelling difficulty
    * breaksは格付けのdynamimcsが必要。
	* デフォルト確率はマーケッットから求めることも可能だが、格付けの推移はヒストリカルにしかできない。

break clauseは伝統的に銀行のcreditとsalesの部署ではポピュラーだが、xVA deskでは複雑さを増やすものの限定的なメリットしかない。
break clauseは、一般的でなくなりつつあり、担保の差し入りや、条項を削除するということが行われている。

financial crisisより前は、担保なしのcounterpartyに対してbreak clauseの要求は一般的であった。
最近は、資産管理会社や年金基金のようなcounterpartyが、銀行にbreak clauseをつけることを要求している。
これは、金融危機の時の前例のないbanking sectorのcredit qualityの問題に関連している。
更に、近年はliquidity coverage ratio(Section 8.8.4)が最悪のcredit ratingの変更に大して流動性のバッファを銀行に要求する規制の影響もある。

### 5.4.3 Reset agreements 
 reset agreementsは、in-the-moneyになりすぎないように商品ごとに調整用のパラメーターを導入し、at-the-moneyになるようにresetをする方法である。
 reset dateは、payment dateと同じであったり、market valueでtriggerされたりする。
 例えば、CCSのMTM付きのものが例である。
 この場合、reset dateに現金でMTMの交換する。
 更に、FX rateがreset dateのspot rateでリセットされる。
 このリセットは、close-outの影響とreplacement transactionを行っているのに近い影響を与え、結果としてexposureがへる。
 このexposureの影響が図5.9である。
 これは、担保の差し入れより効果としては弱い。

## 5.5 SUMMARY

































