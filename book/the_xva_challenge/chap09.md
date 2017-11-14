---
title: 9 Counterparty Risk Intermediation
book_title: The XVA Challenges
book_chapter: 9
---

# 9 Counterparty Risk Intermediation.

## 9.1 INTROUCTION
保証や保険の提供者 and/or 仲介人として活動する機関によるCounterparty riskの軽減について解説する。

* Derivative Product Companies(DPCs)
* Monoline insurer
* CCP

など。

ここでの議論の多くは歴史的なものだが、これらの機関ができる原因に関連するいくつかの教訓について議論する。
また、OTC derivatives Counterparty riskを軽減するCCPの役割についても触れる。
CCPの役割は、標準化されたOTC derivativesのclearingの義務化において、重要な要素となっている。

取引所で取引されるderivativeはCounterparty riskをコントロールするために長い間中央精算を利用していた。
2007年の金融危機より前、主要なderivative dealerがデフォルトする前に、dealer-dominatedなOTC marketは取引所のmarketよりCounterparty riskに対して弱いということが知られていた。
より大きく複雑なOTC derivatives marketは、Counterparty riskの軽減のために、CCPを含む多くの方法を開発してきた。
これらの方法は、counterparty riskの仲介を基礎としており、第三者が保証者として間に入り、一方もしくは両方のcounterpartyのperformanceを保証し、counterparty riskを軽減する。
保証者は保証する機関より良いcredit qualityが必要となる。

多くの異なったcounterparty risk intermediationの形式がある。
それらは、central clearingの前身とも見ることができるが、 それに伴ってほかの多くのriskを生成している。(Figure 9.2)

* Special Purpose Vehicles
    * デフォルト時の債権者としてcounterpartyを処理し、default-remoteな機関を作ることを目的とした器である。
    SPVの設立者の倒産時におけるSPVの資産に対する扱いが明確でないという、legal riskが存在する。
* Guarantees
    * derivativeのcounterpartyのperformanceを保証する第三者機関である。
    これはオリジナルのderivativeのcounterpartyと保証者が両方デフォルトしたときにのみ損失がおこるという*double default*の概念(Sect 8.1.3)を生み出した。
    よくある単純な保証としては、子会社が親会社に保証されるといったグループ内のものである。
    ほかの例としては、銀行信用状(letter of credit, L/C)と呼ばれる指定期間・金額を銀行が顧客の手形支払いを保証するものがある。
    保証を提供する機関は、元のcounterpartyより高いcreditを持つべきであり、また元のcounterpartyと明らかな関係があってはならない。
* Derivative Product Companies
    * DPCは、追加の資本やoperational ruleを持つことでGuaranteeの概念を発展させたものである。
    一方、それに伴いoperational riskとmarket riskを生み出した。
    DPCは仲介の特別な形式で、銀行が倒産と関係の薄いSPVを設立し、triple-Aの格付けを得るために資本を追加したものである。
    MonolineとCredit DPCは,credit derivativeへの特別な応用として見ることができる。
    この場合counterpartyと参照機関の間の関係がwrong-way riskの為、特に重要な問題となる。
* Central counterparty(CCP).
    CCPは、担保の差し入れとdefault fundを要求することでDPCの概念を拡張し、performanceを保証するためにloss mutualisationのような方法を使用している。
    これは、CCPがデフォルト時の契約の置き換えを目的としているためliquidity riskを生み出した。
    CCPの大きさは、systemic riskも生み出している。
    CDSをclearingするCCPは、CDPC(section 9.24)の発展とみることができ、おそらくwrong-way riskの為により難しい役目を担っている。

Derviate marketは多くの他のmarketのように、損失を相互化(to mutualise)する為の方法やriskを移転するために再保険や保証のようなものが必要である。
しかし、この保険やmutualisationが失敗するならば、大きな混乱が起きる。
我々は、これがmonoline保険会社の場合にどのように起こったか、なぜ起こったか、学ぶべき教訓があるかどうかについて議論する。
特に急速に拡大しているCCPが将来OTC derivative marketで持つであろう役割について議論する。

## 9.2 SPVS, DPCS, CDPCS AND MONOLINES

### 9.2.1 Default remoteness and "too big to fail"
ここでの議論の肝は、"default remote entity"である。
defualt remote eintityの一般的なアイディアは、counterparty riskや倒産確率が無視できるような良いcredit qualityのcounterpartyを提供することである。
credit raitingが正確かつ動的なcredit qualityの評価を提供するものとしてみられていた時代は、triple Aのcredit qualityを適用されていた。
counterpartyのdefaultはめったに起こりえないものされていたので、そのような機関はcounterparty riskを軽減するのにとても役立つと以前は考えられていた。
これらの仮定は適当で、marketの慣習のlazinessとも見ることできる。

default remoteの概念に関連して"too big to fail"という良く知られた概念がある。
too big to failなcounterpartyとは倒産するかもしれないが、単純にほかのリスクがあるため倒産を許容するには大きすぎるcounterpartyということである。
したがってcounterparty riskの評価において上記と同じlazinessが存在する可能性がある。
too big to failなcounterpartyは、フォーマルにはSystemically Important Financial Institutions(SIFIs)としてしられている。
Regulatorは、SIFIsを大きさや金融活動からの収益、資産の繋がりなどのようなものでSIFIsを区分しており、解散させるかより多くの資本要求を課し、より厳格な監視対象としている。
これらは、Lehman Brothersの倒産やBear Stearns, AIGに対する救済が必要になるようなOTC derivatives marketの混乱を繰り返さないことを目的としている。
これは有益なステップである一方、モラルハザードの問題が残っている。
つまり、金融機関は政府や中央銀行からの暗黙的な補助があることを信じてSIFIsと取引をする可能性がある。

default-remotenessや"too big to fail"のアイディアは、counterparty riskに対するfinanial marketのアキレス腱であることが示された。
triple-Aの格付けは、counterpartyや法的機関に対して割り当てられたが、それらは法律やビジネスモデルにおける論理的な不備に基づいている。
triple-Aの格付けは修正されるかもしれないが、counterparty riskが低いという本質的な誤解が存在する。
さらに、モラルハザードはマーケットの参加者にcounterpartyが存在しないという幻想による行動を引き起こす。
monoline保険会社やAIGの救済のような金融機関の失敗は、counterparty riskを認識し管理する方法に大きな影響を与えた。

我々は、derivative product companiesとmonoline insurerのOTC derivative marketにおける役割について振り返り、default-remotenessの考えがどのように問題であるかについて考える。
主に過去の振り返りと反省であるが、この議論はcentral counterpartyの概念を考える上で基礎となっている。

### 9.2.2 Special purpose vehicles
SPVは、Special Purpose Entity(SPE)とも呼ばれれる。
SPVは法的な機関（たとえば、会社や有限責任組合(limited partnership))であり、counterparty riskから機関を切り離すことを目的して作られる。
以下の目的で利用される。

* 資産の管理の為に資産をSPVに移転する為 or
* 会社全体やcounterpartyをリスクに曝すことなしに大きなプロジェクトの資金調達を行う為

SVPは設立した会社自身がSPVを保有しないことが要求される場合がある。
SVPは、倒産のルールを変更することを目的としており、もしderivative counterpartyが支払い不能であっても、顧客はほか(e.g. 設立者の債権の保持者など）の要求に先立って投資額を受け取ることができる。
SVPは、仕組債の発行者より良いrating(triple-A)を持つことで、仕組債の元本に対するcounterparty riskを保証する為によく利用される。
SPVの信用力は、ratingを付与する前に法律の内容や機構を考慮し格付け機関によって評価される。

SPVは、counterparty riskをlegal riskに変換する。
明らかなlegal riskは、破産裁判所がoriginatorの資産とSPVの資産とを合わせて処理するというものである。(default remotenessの失敗）
この考えの基には、SPVは実質的にはoriginatorと同一であるので、SPVに移転された資産もoriginatorのものとして扱うべきというものである。
Consolidationは、US courtの場合はconsolidationについて過去の実績があるが、UK courtはあまりないなど司法などに依存する場合がある。

不幸なことに、SVPの法的な実行可能性については長い間試されていなかった為、 Lehman Brothersのケースでは、多くの問題が起こった。
Lehmanは、CDOのような複雑な取引に対して投資家をLehman自身のcounterparty riskから保護する為にSVPを利用していた。
documentのキーとなる条項は、"flip"条項として参照されており、それはLehmanが倒産した時、最初に投資額を回収できるということを意味していた。
しかし、US Bankruptcy Courtは、flip条項は実施できないとし、UK courtはflip条項は実施できるとした。

flip条項が法的に正しいかどうかの問題があったものの、Lehmanは示談で解決した。
ここで確かなことは、SPVが示したようにcounterparty riskの軽減する為にlegal riskを生み出すような機構は危険であるということだけだけである。

### 9.2.3 Derivative product companies
DPC(C is company/corporation)はOTC derivative marketにおいてcounterparty riskを軽減するために発展した。
DPCは、一般的にtriple-Aの機関であり、SPVと異なり1つ以上の銀行によって(triple-Aを得るために）資本を分離して設立される。
DPCは、DPCの母体の倒産を防ぐことによってcounterparty riskに対するprotectionを他のcounterpartyに提供している。
従ってDPCは、OTCマーケットの集中化を防ぎ柔軟性を維持したまま、取引所のシステムの持つ幾つかの利益を提供する。
初期のDPCの例として、Merril Lynch Derivative Products, Salomon Swapco, Morgan Stanley Derivative Products, Lehman Brothers Financial Productsがある。

DPCは、資本、担保、活動の制限を組み合わせることでtriple-A ratingを維持している。
個々のDPCは、それぞれの現在の信用リスクを定量的に評価する為のモデルを持っており、triple-A ratingに必要な基準を維持しているかを計測している。
DCPの格付けは下記によって決まる。

* Minimising market risk
    * DPCは契約をoffsetする取引を通してmarket-neutralに近づくよう試みる。
    理想的には、全ての取引の反対取引(mirror trade)を持つことで、neutralにすることができる。
    通常、mirror tradeはDPCの母体が持っている。
* Suport from a parent
    * DPCは良い格付けを得るために、SPVのようにBankruptcy-remoteとなるようサポートを受けている。
    DPCの母体が倒産したら、DPCは他の資本化された機関に渡されるか、取引を整然と終了させるのいずれかとなる。
    下記で議論するように、この問題は基本的に起こらない。
* Credit risk management and operational guidelines(limits, collateral, terms, etc.)
    * （母体でない他の）counterparty credit qualityと活動(position limits, collateral, etc.)に制限が課せられる。
    counterparty riskの管理は、日次の値洗いと担保の差し入れによって達成される。

良い格付けを得る一方で、DPCは何のイベント(母体の格付けの引き下げなど）が自身の倒産の引き金となるか、その後の倒産の処理がどのように機能するかを定義している。
結果として生じる*pre-packaged bankruptcy*は、標準的なOTC derivative counterpartyの倒産より単純で（また起こりにくいもの）と想定された。

DPCのideaは、1990年代に設立されて以来、金融危機までうまく機能していた。
一つの問題は、credit qualityの動的な尺度として格付けを利用していたことである。
例えば、Lehman Brothersは、single-A ratingを倒産時に得ており、アイスランドの銀行は倒産の数週間前にtriple-Aという格付けを得ていた。
2つのLehman Brothers DPCの自発的な連邦倒産法第11章の届け出は、DPCの資産を守る為の戦略的な努力であるが、母体とDPCが切り離せない繋がりを示している。(Lehmanの倒産がDPCの倒産につながった）
母体の衰退の後、Bear Stearns DPCは、JP Morganによって徐々に解体されていった。
驚くべきではないが、DPCの自治権の欠落の認識は、格付け機関のリアクションを導き、格付けの引き下げが起こなわれた。

SPVのようにDPCの概念は欠陥があり、DPCのtripe-A ratingは、DPCより悪い格付けであるDPCの母体の影響で殆ど信用力を持っていなかった。
DPCはcounterparty riskをlegal riskのみならずmarketやoperational riskへと変換するものである。
これは有益ではないかもしれない。
しかし、このような仕組みは、規制やマーケットの環境によって再びだろう。

### 9.2.4 Monolines and CDPCs
上述のように、DPCの設立は、OTC derivativeの取引時に高格付けのcounterpartyの必要性によって起こる。
しかし、このニーズは1998年ごろからcredit derivative marketの誕生と急速な成長に伴って発達した。
1つ以上credit eventに関連した支払いを持つと同時にcredit spreadの変化によってCDSの価値が変化するので、CDSは難しい。
この難しさは、Wrong way risk(Chap17)と呼ばれるものに起因しており、CDSのcounterpartyのcredit qualityは他のOTC derivativeより重要である。
CDSは比較的起こりにくいデフォルトイベントを参照する契約であり、難しいmarket conditionによって引き起こされるものである。

Monoline保険会社(とAIGのような似たような会社）は、triple-A ratingの金融保証会社である。
USの地方債に対する保証を提供する為に設立されたmonolineは、 格付けのない借り手にtriple-A ratingを提供し、より良い収益とcredit derivativesの多様化を達成する為に、credit系の仕組債などに対するCDS protectionを売っていた。
自身の格付けの為に、保証する資産に応じてキャピタルチャージが行われる。
ここで重要なのは、monolineは基本的に自身の取引に対して担保を差し入れることはないということである。

Credit Derivative Product Company(CDPC)はDPCとmonolineの概念に発想を得た機関で、DPCのモデルをcredit derivative productに拡張したものである。
CDPCは、レバレッジのついたcredit derivativeに投資する為に作られた機関で、基本的に社債や国債やsingle-nameやportfolioのAsset-Backed Securities(ABS)に対するprotectionをCDSの契約として売っている。
DPCが単純にBankruptcy-remoteを持った子会社である一方で、CDPCはcredit derivative protectionを売って収益を上げることを目的とする為に作られている。
伝統的なDPCと異なり、CDPCはoffsetされていないポジションを持っている為、market riskにさらされている。
monolineのように、CDPCは高いcredit qualityのcounterpartyとして機能するが、credit protectionの売る側(offsetしていない）として活動している。

金融危機以前は、一般的にmonolilneやCDPCは金融機関として安定していると思われていた。
```
Example

The credit quality of monolines(a quote from 2001).
主要なmonolineは十分強力なcredit qualityを持っており、投資家に素晴らしいcredit protectionを提供している。
発行者のcredit qualityと組み合わせることで、tripe-A riskよりベターなものとなっている。。
実際、投資家のキャピタルロスのリスクは、実務的には0で、格付け低下のリスクの方がやや高い。
risk特性の状態を仮定すると、monolineのtriple-Aは、十分に守られている。
4つの主要なmonolineは適切な資本レベルを保っており、リスクポジションに対する支払いの要求はあったとしても1つの大きなexposureに限定されている
```
monolilneやCDPCは取引に対して担保を差し入れる義務を持たない機関の為に、triple-A ratingが与えられていた。
担保の差し入れによるMTMの損失が起こるのでこれは重要である。

2007年に金融危機が起こった時、monolineは自身が売った保険によるMTMの損失による問題を経験した。
triple-A ratingと不十分な資本に対する関心が起こった。
monolineは、格付けの引き下げで、担保を差し入れるような条項を持っていた。(triple-A未満になった場合に起こるケースもあった）
例えば、2007/11にACA Financial Guarantee Corporationは自身のsingle-A credit ratingの損失が担保差し入れの必要を引き起こし、それは対処することはできないと述べた。
格付け機関は、すぐに反応しなかったが、一度monolineの格付けの引き下げを行うと担保の差し入れによって倒産する為、株価の下落が起こった。
Figure9.3は、MBIAとAMBACの株価の下落を表している。

多くの銀行は、銀行が購入したprotectionの価値の増加の為、monolineに対してriskをもっていることを認識した。
例えば、2008/6に、UBSは＄6.4 bllionがmonoline保険会社に対するriskに曝されていると見積もった。
また、CitigroupとMerrill Lynchは、＄4.8 billionと＄3 billionとそれぞれ見積もった。(Financial Times, 2008)
AIGの状況は大体これと同じ状況で、格付けの低下とAIGのポジションの急速な変化の結果として、大量の担保の差し入れが必要となった。
これによりAIGは大量の損失を蒙り、AIGの倒産によって多くのcounterpartyが損失を受けることになった。
しかし、AIGがUS政府によって＄182 billionの資金を投入し救済されたので、counterpartyが損失を受けることはなかった。
AIGは救済され、monoline保険会社は救済されなかったのか。

CDPCはmonolineのように、レバレッジがかけられており、担保を差し入れていない。
CDPCは金融危機の時に比較的うまくやっていたが、それは時期の問題である。
多くのCDPCは、金融危機の2007/6まで経営を完全には行っていなかった。
その為彼らは多くのcredit protection(特にsuper senior)の売り手が経験した最初の損失の波を逃れた。
CDPCのビジネスモデルはmonolineのものに近いということは無視できない。
例えば、2008/10にFitchは5つのCDPCの格付けを引き下げた。

monoline/CDPCのビジネスモデルは致命的な欠陥がある。
大量のcounterparty riskを保証する中央機関として機能しており、systemic riskの影響の緩衝材としての機能を提供していた。
しかし、保証債券の多様化に頼っている為、systemic riskの保証をしているというのは不適切である。
monolineとAIGの失敗は重要な教訓であり、特にCCPが将来果たす役割の重要性を示している。
CCPはmonolineやAIGと多くの異なる方法をとっており、counterparty riskの軽減を実現しており、systemic riskに焦点をあてている。
CCPは、最も巨大な"too big to fail"な機関である。

## 9.3 CENTRAL COUNTERPARTIES
ここまでの教訓は、SPVやDPCやmonolineやCDPCのような機関がdefault-remotenessによって、counterparty riskの軽減を行っていたことに問題があったということである。
近年、CCPが規制当局から多くの援助を受けていることに疑問を持つかもしれない。
CCPは自身の複雑さとリスクを持っているが、CCPの経営の方法は多くの点でSPVやmonolineなどのような機関と異なっている。
CCPの詳しい説明はGregory(2014)を見てね。

2007の金融危機は、Lehman Brothersの崩壊やmonoline保険会社の倒産、アイスランドの銀行の倒産などのイベントに触発され、counterparty riskに関する関心を引き起こした。
OTC derivativeのcounterparty riskは、金融システムの主要なリスクとして認識された。
counterparty riskの直接的な軽減の結果として起こる担保の管理やclose-out処理に関連するoperationalとlegal riskも勿論存在する。
CCPはこれらの問題に対する解決策であり、counterparty riskを保証し、担保と倒産の管理を提供する中央機関としての機能を提供している。

bilateral OTC derivative marketに伴った大きな問題は、close-out処理である。
close-outの処理は、多くの時間を必要とし法律上の手続が必要となる。
CCPは、close-outのルールを作成し強制することでこの手続きを改善し、他の取引を継続させsystemic riskを軽減している。
CCPによるOTC derivativeの倒産管理は、Lehman bankruptcyの後のbilateral marketより優れている。
bilateral marketは、いくつかの点において(ISDA close-out protocolの適用など）において改善がみられるが、CCPと同等と言えるほどではない。

2010年に、Europe(European CommisionのOTC der, CCPと取引に対する規制）とUS(Dodd-Frank Wall Sstreet ReformとComsumer Protection Act)の双方が全ての標準化されたOTC derivativeは2012年の終わりまでにCCPを通じて取引されなければならないと述べた。
これに対する理由の一部は、2008/9のLehman Brothersの崩壊の後に金融marketが崩壊した一方で、CCPはある程度うまく機能していた為である。
例えば、LCH.ClearnetとChicago Mercantile Exchange(CME)はLehmanの倒産時に、他の金融システムが機能しない中比較的うまく機能していた。
結果として、政策担当者は、CCPがcounterparty riskに対する万能薬に近いものとして、CCPに注目した。

以下では、OTC derivative clearingと取引所取引のderivativeにおけるCCPの幾つかの役割について議論する。

### 9.3.2 OTC clearing
clearingは取引の後に起こる手続きである。
この取引において、パフォーマンスを保証する為にcounterpartyの間にCCPが入る場合がある。
OTC CCPのメインの機能は、全ての売り手に対する買い手、全ての買い手に対する売り手として機能することで、counterpartyの権利と義務を引き受けることである。
これは、オリジナルのcounterpartyが直接的なリスクとならず、CCPが新たなcounterpartyになるということを意味する。
CCPは以下の方法で倒産時の損失を配分する。
全ての方法は、counterparty riskとsystemic riskを軽減するための手続きである。

* netting
    * bilateral marketでは、counterparty Aに対するポジションと同じかつ反対のポジションをcounterparty Bに持っている場合、counterparty riskがある。
    この2つの取引がCCPでclearingされていればnetされたポジションはリスクがない。
    * bilateral marketにおけるcompression.(sect5.3)
* 担保
    * CCPは参加者から担保を要求し、ポートフォリオの価値変化に関連したriskを減らす。
    * bilateral marketでの担保(Sect6.7)
* loss mutualisation
    * あるcounterpartyのLossを他のclearing memberに分散させる。
* close-outの促進
    * 再構築する必要がある取引をMultilateral nettingで減らし倒産者の契約上の義務をオークションにかけることで、価格とmarketのvolatilityへの影響を最小限にする。
    * ポジションを他のclearing memberに移転することを容易にする。

OTC CCPの一般的な役割は以下。

* clearing memberに対する基準とルールを策定
* 倒産したclearing memberのポジションをclose-outする責任
* 上記をサポートする為に、clearing memberの倒産時の損失をカバーするためのリソースの管理。
    * marketの変化にあった、variation margin
    * 流動性とclose-out costをカバーするためのinitial margin
    * シビアな倒産時の損失を相互化するためのdefault fund

CCPは金融のリソース(IM, default fund)が枯渇した時のシビアな状況における文書化されたプランを持っている。

* default fundの追加の要求
* variation marginのヘアカット
* ポジションの選択的な分割

OTC derivativeのend-uuserといくつかの銀行はclearing memberを通してCCPにアクセスする（clearing memberにはなれない）。
これは会員制であるためで、operationと流動性がclearing memberになるために要求される。
特に、定期的な"fire drill"に参加することとCCPオークション時の入札が、会員になれない主な理由である。

CCPにおいて、counterpartyの倒産はLehman Brothersのように大きいものであっても、劇的な影響とはならないことが想定される。
これはCCPが中心的な緩衝材として機能することで、"domino effect"を吸収するためである。
clearing memberのデフォルト時に、CCPは損失起こさずmemberのcounterpartyへの繋がりを断つ。
これは通常は、個々の取引について他のclearing memberに、倒産したmemberのcounterpartyへの再構築を行わせることで達成される。
これはCCPが倒産したmemberのポジションのオークションをmemberの間で行い、他の生き残ったmemberの生存を助ける。

### 9.3.3 The CCP landscape
CCPはbilateral marketのcounterparty riskを管理、配分、減少させることを目的として設計されたルールとoperationを表している。
CCPは、買い手と売り手の両方になることでmarketの形態を変える。(Figure9.4)
Figure9.4において、Dは巨大なグローバル銀行のdealerを表している。
2つの明らかな利点　は、この単純化された図に表れている。
* CCPは内部関連性を減らす。
* CCPはclearing memberの間の取引の透明性を提供する。

ここでの問題は、CCPがシステムのハブとなっており、CCPの倒産が破滅を引き起こすことである。

上記の分析は単純化されたものであるが、基本的には正しい。
実際のCCPはもっと複雑である。

* Client clearing
    * CCPのclearing memberになれない機関は、clearing memberを通してclearingする。
    これは担保の差し入れやデフォルト時のoperationの複雑さを増加させる
* Bilateral trades
    * 全てのOTC derivativeがCCPを通じてclearingされるわけではない。
    常に一定量はbilateral取引で行われる。
* Multiple CCPs
    * 色々なCCPが世界中にあり、clearing memberが複数のCCPに属することで内部の関連性が存在している。

### 9.3.4 CCP risk management
CCPは巨大なmarketの中心として居座っているとすると、適切なrisk管理と適切な資金が必要となる。
一つの明らかかつ重要な方法は担保であり、CCPは自身がclearする取引のmarket riskをカバーする為に担保を要求している。
CCPはvariation marginとinitial marginの両方を要求する。
VMはclearing memberのポジションの価値の変化をカバーする。
IMはCCPのclearing memberのデフォルト時の最悪のケースにおけるclose-out costをカバーする。

clearing memberが倒産した場合、CCPは損失をださないよう倒産したmemberのcounterpartyへの繋がりを断つ。
これは、通常倒産したclearing memberのポジションのオークションを通じて行われる。
オークションは、clearing memberの間でsub-portfolioベース(特定通貨のIRSなど）で行われる。
clearing memberはこのオークションに参加する強いインセンティブを持っており、default fundや他の方法で損失に曝されるよりオークションに参加することを選ぶ。
この場合、CCPがbinlateralで清算される価格より良い価格で取引をnovatingする場合もある。
しかし、CCPのオークションが失敗すると、よりアグレッシブな損失配分の方法がとられる。

clearing memberの倒産とオークションを経た損失は、CCPが持っている担保によって吸収される。
CCPによる担保の要求は、bilateral marketのものより厳しい。
特にVMはdailyもしくは日中ベースで取引され、基本的に取引通貨の現金で行われる。
IMの要求は保守的で、マーケットの状況に伴って変わり、現金か流動性のある資産（treasury bonds)で行われる。
IMと担保の流動性の組み合わせは、どちらも歴史的にbilateral marketでは要求されていなかった。　
これは、clearingが担保要求を通して高いコストの支払いを課していることを意味している。
しかし、bilateral marketも将来的には似たような担保のコストを支払う規制の影響を受けるだろう。(Sect 6.7)

IMとdefault fundの寄与が不十分である場合、およびまたオークションが失敗した場合、CCPは損失をカバーする為に他の資金を必要とする。
一般的に、"loss waterfall"がどの資金が使われるかを表現する為に使われる。
これはCCP間で異なるが、典型的なloss waterfallはFigure9.5となる。

CCPのmemberが資金に貢献する理想的な方法は、"defaulter pay"である。
"defaulter pay"は、全てのclearing memberが自身の将来的な倒産に対して支払う資金であるが、このままではそれぞれのメンバーが寄与する金額が高い為、非実用的である。
この理由の為に、資金はclearing memberが倒産したシナリオにおいて、高い信頼水準で損失のカバーを与えることを目的として決められる。
IMとdefault fundは枯渇するするような、極端なシナリオではCCPの自己資金から損失が補填される。
上に述べたコンポーネントが十分である限り、"defaulter pay"は遂行される。

CCPのOTC derivativeに対するIMの計算は、ヒストリカルシミュレーションで行われる。
ヒストリカルシミュレーションは、ポートフォリオ全体のリスクファクターの振る舞いを含んだ数年分のヒストリカルデータを使用する。
多くの期間でシミュレーションを行い、現在のポートフォリオがどのように振る舞うかを見る。
例えば、4年のデータを使用する場合は、日次のポートフォリオの変化を表現する1000の異なるシナリオが利用できる。
CCPはVaRやESを、99%の信頼水準を表現する最悪なケースにおけるパフォーマンスを測る為に用いる。
これは、倒産時のIMが関連する損失をカバーするのに十分であるかどうかを検証する為に行っている。
bilateral marketにおけるIMのアプローチは似ており、SIMM(Sect6.7.7)はOTC derivativeにおけるIMの計算のtracableなものである。

CCPはdailyないし日中の現金担保コール(no settlement delay)によりMPRを減少させている。
全ての計算に対してCCPは権限を持っており（disputeは許されない）、clearing memberが顧客の代表として担保を差し入れることを保証し、担保差し入れの要求する。
効率的な倒産時の手続きを迅速に行う為に、外部の妨害受けることなしでclearing memberの倒産を宣言することができ、 CCPはポジションのclose-outもbilateral marketより迅速に行うことができる
これらの理由の為、Sect8.6.3で述べたBasel IIIのbilateral取引に対する10 daysの計算に対して、CCPは5-daysで計算する。

中央精算の他の原理として、loss mutalisationがある。
loss mutualisationは、倒産したclearing memberの損失を他のCCPのmemberの間で分配する方法である。
CCPのmemberは、CCPに"default fund"として貢献しており、倒産者の資金が損失のカバーの為に使われた後に利用される。
default fundの大きさはclearing memberのIMの大きさによって決まり、動的に変化することはほとんどない。
全てのmemberがこのdefault fundを支払うので、極端な倒産の損失を吸収することができる。
CCPのdefault fundの大部分を消し去る損失は、ほとんど起こりえない。
しかし、それが起こった場合は、残ったmemberは追加のdefault fundを差し入れることを要求される。
この追加の差し入れは制限があり、モラルハザードを防ぐ為に(最初のdefault fundの額に応じて）キャップされている。
CCPは、取引の選択的なtear-upやVMのhaircutのように他の方法も持っている。
default fundを通じた損失の吸収と比較してこれらの方法はより異なった損失の配分を引き起こす。
loss allocationの方法の選択は、公平性とすべてのclearing memberの正しいインセンティブによって選択される。

いくつかのloss allocation方法は理論的に制限がない。
つまり、CCPは決して倒産しないようにclearing memberに損失を課す。
これらのallocation方法（e.g. tear-u or allocationの強要）はとてもシビアで残ったclearing memberを倒産へと導く。

loss allocation方法が有限であるとすると、CCPは外部の流動性の支援をうけない(中央銀行による救済など）限り潜在的に倒産しうる。
loss waterfallの下部にいたると、多くの資金のレイヤーが浸食される。
正確に定量化することはできないが、これはかなり低い確率の事象であるべきである。
CCPは自身が倒産することなしにdefault fundを通してmemberに損失を課すことができるという点は重要である。
CCPのメンバーはCCPの"mini-default”に苦しむこととなる。
倒産の損失は、実際に倒産したmemberとの取引ではないという点も重要である。
実際、倒産したmemberと一度も取引したことなく、CCPのnetポジションもなくとも損失を支払う可能性はある。

### 9.3.5 Comparing bilateral and central clearing
Table9.1は、bilateralとCCPの比較である。
標準化されたエキゾでないものだけが中央精算される。
CCPは強い担保の要求をmemberに強いる。
CCPのキャピタルチャージは、比較的穏やかで取引のレベルとdefault fund exposureに関連する。
bilateral marketでは、参加者はデフォルトリスクとCVA capital chargeに曝されている。
上で述べたように、中央精算の重要な機能はデフォルトシナリオにおけるオークションである。
bilateral marketでは、counterparty risk、funding, capitral からcostが発生するが、CCPでは、costは主にfunding(IM, 他の資金など）と比較的に少ないキャピタルチャージ（Sect9.3.7)である。

|  | Bilateral | Centrally cleard | 
| ----- | ----- | ----- | 
| Counterparty | Original | CCP | 
| Products | All | Must be standard, vanilla, liquid etc. | 
| Participants | All | Clearing members are usually large banks. Other collateral posting entities can clear through claering members |
| Collateral | Bilateral, bespoke arrangements dependent on credit quality and open to disputes. New regulatory rules being introduced from September 2016(Sect 6.7) | Full collateralisation, including IM enforced by CCP | 
| capital charges | Default risk and CVA capital | Trade level and default fund related | 
| Loss buffers | Regulatory capital and collateral | IM, default funds and CCP own capital | 
| Close-out  | Bilateral | Coordinated default management process(e.g. auction) |
| Costs | Counterparty risk, funding and capital costs. | Funding (IM) and (lower) capital costs. | 

### 9.3.6 Advantages and disadvantages of CCPs
CCPは明らかな利点がある一方で批判がないわけではない。
CCPは、過去に一度失敗したことがある。
1987年のブラックマンデーにおける金融システムに対する脅威によって、CCPはかつて困難に直面した。

CCPは市場の透明性やオークションにより代替可能かつ流動的な契約を与えるより安全な市場というメリットを提供する。
以下はCCPのメリットである。

* Transparency.
    * CCPはclearing memberの市場取引の大部分を引き受け、bilateral marketのような透明性のないものと異なる。
    memberが極端なexposureに曝されているとすると、CCPは取引を制限し被害が広がらないようにする。
    これによって、金融機関が実際に直面しているexposureに対する知識の欠落から起きるパニックを抑制することになる。
* Offsetting.
    * 述べたように、異なるcounterparty間の取引はCCPを通じてoffsetされる。
    これは、costを減らし、既存の取引を終了させ、新しい取引を促進する。
* Loss mutualisation.
    * 倒産によって倒産者の資産を超えた損失が起こった時、被害の拡大を防ぐためにCCP memberに損失が分配される。
* Legal and operational efficiency
    * CCPがsettlementやnetting,担保を引き受けることによって、事務効率を上げcostを減らす。
    CCPは中央精算化のルールと機能を提供することで、legal riskを減らすともいえるかも。
* Liquidity.
    * CCPはmultilateral nettingによる利益や取引を用意にすることによって市場の流動性の改善に寄与する。
    日々の担保コールは透明性のある価格を提供することにつながるかも。
* Default management.
    良く管理されたオークションは、clearing memberの倒産時の危険な時期に、replacement costのばらつきを抑制する。

CCPはmember制の機関なので、memberの資金をある程度維持しておかなければならない。
CCPのメンバーのデフォルトによる損失は、生き残ったメンバーの間で共有されるが、これは本質的に以下の問題を生み出す。

* Moral hazard.
    * 全てのリスクがCCPに渡されるので、CCPの参加者による正しいcounterparty risk管理のインセンティブがなくなる。
    これは保険業でよく知られた問題である。
* Adverse selection.
    CCPは逆選択の問題もある。
    CCPの逆選択とは、OTC Derivativeを取引しているmemberがCCPよりriskについて熟知している時に起こる。
    そのような状況では、riskを加味した実際の価格より、自身に有利な価格でCCPに危険な商品を渡すという問題が起こる。
    OTC Derivativeを専門とした大きな銀行は、CCPより多くの情報と知識を持っている。
    実際に、市場参加者の間で、異なるCCP間で固定対固定のIRSで安い価格となっていることが明らかになっている。
* Bifurcations.
    標準の商品をclearingする時に、Clearingされているものとされていないものに分かれる。
    この場合顧客はvolatileなcashflowに曝され、ヘッジポジションのミスマッチが起こる。
* Procyclicality.
    Procyclicalityは、経済と正の相関のあるものを表す語である。
    CCPはprocyclicalityの影響持つ。
    例えば、volatileなマーケットでの担保要求（or ヘアカット）である。
    CCPの担保の流動性と要求頻度の多さは(bilateralと比べて）procyclicalityを悪化させる。
    経済が悪い時にさらに担保要求とかすると更に経済の悪化を招くということ。

clearingは昔から取引所で取引されているものに限定されていた。
Bilateral OTC marketはここ20年で取引所の商品を超えて発展し、成功してきた。
OTC derivativeのclearingの問題は、流動性が低く、期間が長く、取引所のものと比べて複雑であるという点である。

### 9.3.7 CCP capital charges
CCPに対するexposureは、前の章で議論したbilateral取引に関連したcapital chargeを引き起こさない。
しかし、CCP-specificなcapital chargeがあり、CCPがrisk-freeではなく、default fundがCCPの倒産時に損失となるということを反映する必要がある。
詳細はBCBS(2014c)を見よ。

QualifyingCCP(QCCP)の為のCCP資本要求は以下である。

* Trade exposures.
    * 現在のMTM exposureとVMによるexposureで、PFEとCCPへのIMと共に現れる
    これらのexposureは、CCPの倒産(CCPのメンバーでなく）によってリスクに晒される。
    これらに対する資本要求は2%の比較的小さいrisk weightが課せられる。　
    Sect 8.1.2のIRB methodにおいては最も小さいrisk weight(= Capital Requiment × 12.5)で、34%(PD, LGD, EADの計算方法と値に依存）ととなる。
    取引のexposureは非常に大きくなる場合はある（IMのせい）が、capital chargeとしては比較的少なくなる。
* Default fund exposure.
    CCP default fundのカバーの為の資本。
    CCPが倒産せずともリスクに晒されている。
    CCP memberが一人でも倒産すると全てまたは一部が失われるexposureなので、定量化し辛い。
    更に、CCP memberの倒産の影響の大きさによっては、追加のdefault fundの差し入れが必要な場合もある。
    最後に、他のloss allocation方法の存在も計算を複雑にする。
    IMに比べてdefault fundの額は少ないものの、影響は大きい。
    2017の新しい規制のルールでは、CCPに関する資本については、SACARに比べて、改善されているように思われる。
    詳しくは、Gregory(2014)

### 9.3.8 Waht central clearing means for xVA
OTC Derivativeの中央精算は、担保を要求するCCPのrisk managementを通じてcounterparty riskを減らすことを目的としている。
CVAとKVAは、CCPを通じて取引する場合は問題とならない。
中央精算されたOTC derivativeが増加すると、clearingの義務によって、CVA(とxVA)はあまり問題にならなくなる。(Figure9.6)

しかし、2つの問題がある。

* counterparty risk, fundingとcapitalの問題(CVA, FVA, KVA)が金融機関でないend-user(sect 3.1)との担保のないOTC derivative取引で起こる。
end-userはCCPのclearingの義務がないので、自発的に行う以外に中央精算をしない。
彼らは、担保を差し入れるのは難しいのでclearingはしないだろう。　
よって、担保なし取引においてxVAは特に重要である。
* 今後のbilateralの担保ルール(Sect 6.7)の変更や中央精算などの要因で、CVAは減るかもしれないが、他の要因(FVA, MVAなど）は増加するかもしれない。
よって、xVAを考慮することは依然として重要である。

## 9.4 SUMMARY



