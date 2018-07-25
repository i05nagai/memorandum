## Terms

* remnant
    * remnant inventory
    * stock of advertizement in a publisher
* media
    * 広告枠をもっているweb site
* advertiser
    * 広告を出したい広告主
* creative
    * 広告に表示される画像や動画、音楽など
* AdExchange
* Suppply Side Platform
    * media側が広告枠を売るために利用するplatform
    * 流れ
        1. mediaでimpressionが発生する
        2. mediaがimpressionの情報とaudienceの情報をSSPに渡す
        3. SSPは受け取った情報をもとに、各DSPにbidを要求する
            * Open RTBのBid Request
        4. 各DSPはbidと掲載したい広告の情報とbidをSSPに返す
            * Open RTBのBid Response
        5. SSPは得られたBidと広告の組の中から、最良のものを選ぶ
        6. SSPは選んだ広告をmediaに渡す
* Demand Side Platform
    * advertiserが広告枠を買うために利用するplatform
    * audienceの情報は、SSPから渡されることもあれば、DSPやadveritser, 第三者のDMPを利用する場合がある
* Data Mnagement Platform
    * access logとの違いは、自社サイトのアクセスだけではなく、他社から提供される情報ももつ
    * それらの情報を紐付けaudienceの情報を特定する
    * 例えば
        * 自社のweb siteの訪問履歴
        * 他社のweb siteの訪問履歴
        * demographic情報
        * 検索Keyword
        * EC siteなどでの購買履歴
        * smartphoneの位置情報
    * DMP専門の会社は、色々なmediaから情報を取得し、SSPやDSPに提供する場合もある
* dynamic allocation
* companion ad
    * pre/in/postなどのように1つのpage viewに対してimpressionを
* road blocking
    * [ロードブロッキングについて - DoubleClick for Publishers ヘルプ](https://support.google.com/dfp_premium/answer/177277?hl=ja)
    * 1つのweb page内の複数の広告枠を、1つのbid responseに含まれる複数のクリエイティブで埋める
    * 同じweb pageの複数広告枠の同時買い付け
* ad mobile
    * [What is Mobile Ad Mediation and How Does it Work?](http://www.adotas.com/2014/07/what-is-mobile-ad-mediation-and-how-does-it-work/)
* iframe buster
* linear
* letter boxing
    * 映像技術におけるレターボックス（英語：Letter box）とは、映像メディアの表示画面において他の画面サイズ規格でつぶれて表示されないよう、表示互換性をとるために、本来および横長比率の映像の撮影された映像部分の上限部に黒帯を追加した状態のものを呼ぶ。
* playback
* playbackend
* delivery
* parable
    * [Parrable: One Device, One ID](https://www.parrable.com/#)
* Black Heron
    * アドフラウドソリューション
    * [Momentum株式会社(M0mentum)～最先端のデジタル広告～](http://www.m0mentum.co.jp/service/blackheron.html)
* Black swan
    * ブランドセーフティーソリューション
* incremental reach
    * [動画広告が勃興するいま、見落としてはいけない3つの視点 | DIGIDAY［日本版］](http://digiday.jp/brands/suvt-3-point-of-view/)
    * TV CMのreachの不足分をmobileの動画広告などで補った分
* brand lift
    * 
* VPAID
    * IABが規定している動画広告format
    * VPAIDの方がrich
    * 広告効果の測定もしやすい
* VAST
    * IABが規定している動画広告format
* brand safety
    * 意図しないサイト・コンテンツの脇に広告表示される
* ad fraud
    * 広告が人ではなく、機械によってクリックされるリスク
* bid pooling
    * 1番高い入札価格以外の入札価格も保持しておき、browserがrereshなどされた場合に、もう一度bid requestを出さずに、2番目に高かったbid requestを使う
* publisher = media
    * web siteを持っていて広告を掲載する側
* viewablity
    * 定義は一つに定まってない
        * 実際に広告が見られたかどうか
        * 閲覧可能な広告枠か、非表示広告枠でないかなど
    * [Viewability Rate Definition | The Online Advertising Guide](https://theonlineadvertisingguide.com/glossary/viewability-rate/)
    * pageの下部にある広告は、page下部がin viewになった時に広告requestを投げればviewablity rateをあげられる
* advertising arbitrage
    * there is no strict definition
    * something dirty which agencies do


定義はIABのstudy guideによる

* CPM
    * Cost Per Mille
    * CPM = cost / 1000 impression
* CPA
    * Cost Per Action
    * CPA = cost / action
* CPC
    * Cost Per Click
    * CPC = cost / clicks
* CPS
    * Cost Per Sale
    * CPS = Cost / Sales
* eCPM
    * effective Cost Per Mille
    * eCPM = costs * 1000 / total impression
* CTR
    * Click Through Rate
    * CTR = clicks / impressions

* CVR
    * ConVersion Rate


## Reference
* [IAB-DMSC-Study-Guide-February-2017_v1.pdf](https://www.iab.com/wp-content/uploads/2017/02/IAB-DMSC-Study-Guide-February-2017_v1.pdf)
* [AdExchangeとSupply Side Platform(SSP)との違いって何よ？ - Web就活日記](http://yut.hatenablog.com/entry/2015/12/23/024629)
* [プログラマティックと自動取引 -媒体社の視点から- | プラットフォーム・ワン](https://www.platform-one.co.jp/IAB_Digital_Simplified_Programmatic_Sept_2013_JP.html)
* [ダイナミック アロケーション - DoubleClick for Publishers ヘルプ](https://support.google.com/dfp_premium/answer/3721872?hl=ja)
* [インターネット広告用語「CVR,CPC,CPA,CTR,CPM」の意味まとめ](http://deaimobi.com/mbnk-181/)
* [WTF is advertising arbitrage? \- Digiday](https://digiday.com/marketing/wtf-arbitrage/)
