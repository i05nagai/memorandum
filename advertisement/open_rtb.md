---
title: Open RTB
---

## Open RTB

## Terminology
* RTB
    * impressionに対するreal timeのbidding
* Exchange
* Bidder
    * impressionを獲得するためのrealtime のauctionの参加者
* Seat
    * impressionを獲得するために、Biddersを代表として利用するもの
* Publisher
    * 1つ以上のsiteを運営するもの
* Site
    * 広告機能をもった web site/web application
* Deal ID
    * PublisherとSeatの間の同意


## 2. 

## 2.1 Transport
* 基本的にHTTP
* payloadが大きいのでHTTP PostがBid requestに使われる
* 全てのAPI callは200を返す必要がある
* no bidの掲示に推奨される204を除く
* Best practice
    * Keep aliveでHTTPのconnectionを切らないようにする
    * HTTPのconnection costは無視できないほど大きい

## 2.2 Security
* SSLはcomplinceに不要である
    * server to serverの通信なので、client serverのような
* SSLはoverheadのため推奨されない

## 2.3 Data Format
* Bid request, bid responseはどちらもJSONが使われる
* payloadのformatは Section 3, 4
* bidderが以下のformatを要求してくる場合もある
    * compressed json
    * XML
    * Apache Avro
    * ProtoBuf
    * Thrift
    * others
* `Content-Type: application/json`
    * JSONの場合はbid request, bid responseともに
* 他のformatの場合は適切なContent-Typeを設定する
    * `Content-Type: avro/binary`
    * `Content-Type: application/x-protobuf`
    * `Content-Type`がない場合は、bidderは`application/json`と仮定する


### 2.4 Data Encoding
* HTTP1.1ではcompressionができる
* 多くのserverはgzipに対応しているので、gzipを使うのが理想的
* exchangeが対応しているecondingについては、`Accept-Encoding`をつけてbidderのserverに知らせる

```
Accept-Encoding: gzip
```

* bidderのserverが対応しているcompressionであれば、bidderは`Content-Encoding`を指定して、encoding済みのresponseを返す

```
Content-Encoding: gzip
```

* HTTP1.1ではresponseに対して、 `Content-Encoding`が指定されるが、OpenRTBではrequest時に`Content-Encoding`を指定することが許容される
* 





### Open RTB version HTTP Header
* OpenRTBのversionをheaderに記載するo
* `x-openrtb-version: 2.3`
* `<majtor>.<minor>`の形式で指定する
    * minorのchangeは基本的には後方互換である


### 2.5 Privacy by Design
* OpenRTBはdo-not-track, COPPA restriction signalingをsupportする

### 2.6 Relationship to IAB QUality Assurance Guidelines
* OpenRTBはIAB Qualit Assurance Guideline(QAG)と互換的である

### 2.7 Customization and Extensions

## 3. Bid Request Specification
Exchangeからbidderへのrequest

### 3.1 Object Model

Object | Description
-- | --
BidRequest | Top level object
Source | header biddingのようにpost auctionの決定に必要なソースの要求
Regs | bid requestにおける全てのimpressionに対する規制の条件
Imp | requestに対して少なくとも1つ
Metric | impressionの定量化可能なhistrocical data
Banner | banner imporession (in-banner videoを含む) とvieo companion adの情報
Video | video impressionの情報
Audio | audio impressionの情報
Native | daynamic native adas APIに対するnative impressionの情報
Format | bannerの許容サイズ
Pmp | このimpressionに応用できるprivate marketplaceのdealsの集合
Deal | sellerとbuyerの間のimpressionの関係
Site | impressionにあったwebsiteの情報
App | impressionのあったapplicationの情報
Publisher | 
Content | 
Producer | 
Device | 
Geo | 
User | 
Data | 
Segment | 


### 3.2 Object Specifications
上記のObjectの詳細

* requiredがついている属性は必須
* recommendedはbusiness的な重要性なものについている
* default valueがついてないものを省略した場合は、unknownになる

#### 3.2.1 Object:BidRequest
一意なbid request IDかauction IDを持つ。

Attributes | Type | condition | Description
--|--|--
id | string | required | exchangeによって提供される一意なID
imp | array | required | Imp objectの配列。少なくとも1つ要素がある
site | object | recommended | publisherのwebsiteについてのSite object。impressionがwebsiteの場合に使用する
app | object | recommended | PublisherのAppについてのApp objectの情報。impressionがappの場合に使用する
device | object | recommended | imporessionが発生したuserのdeviceのDevice object
user | object | recommended | deviceのuserについての情報User object
test | integer | default 0 | requestがtestかどうかのフラグ。0はlive mode、1はtest mode
at | integer | default 2 | AuctionTypeの略。1 = first price auction, 2 = second price plus. exchange特有のauction typeは500より大きい値を利用する
tmax | integer | | internetのlatencyを含むexchangeがbidを待つ時間millisecondsでのmiximum time 
wseat | string array | | このimpressionにbidできるbuyerのseat(e.g. advertisers, agencies)のwhite list。 seatのIDで指定する。 wseatとbseatと両方省略した場合は制限なし。
bseat | string array | | buyer seat(e.g. advertiser, agencies)のblock list。seatのIDで指定する。wseatとbseatを両方省略した場合は制限なし
allimps | integer | default 0 | road-blockingのためのflag。exchangeが(web pageの全てのimpressionや動画のpre/mid/postといった一連の広告をまとめて扱える場合は1にする。0はunkownかno。
cur | string array | | bid可能なcurrencies。ISO-4217に従って指定する。exchangeが複数通貨を扱える場合に推奨される。
wlang | string array | | ISO-639-1-alpha-2に従って、creativeに利用可能な言語のwhite list。何も指定しない場合は制限はなしだが、DeviceやContent objectのlanguage属性を参考にした方が良い。
bcat | string array | | blockされた広告のcategoryをIAB content category (List 5.1)で指定する。
badv | string array | | domainで指定するadvertiserのblock list (e.g. `food.com`)
bapp | string array | | platformに依存したexchangeと無関係なapplicationの識別子によるapplicationのblock list。Androidの場合はbundleかpackage name (e.g. `com.foo.mygame`)で、iOSは整数値のID。
source | object | | Source object。
regs | object | | Regs object。
ext | object | | extension

### 3.2.2 Object: Source
bid requestの提示元についての情報。
post auctionやexchangeの上流で最終的な表示の決定がされる場合に利用される。
header biddingでよく利用される。
他の RTB exchangeや仲介業者などを通した取引の場合にも利用される。

Attribute | Type | | Description
-- | -- | -- | --
fd | integer | recommended | 最終的なimpressionの販売の決定権をもつ機関を表すフラグ。0はexchangeで1はそれより上流。
tid | string | recommended | bid requestのtransaction ID。参加者の間で共通
pchain | string | recommended | TAG payment ID protocol v1.0で表現されるpyament ID chain
ext | object | | extension

### 3.2.3 Object: Regs
legal, 政府、業界による規制の情報。
United States Children's Online Privcy Protection Act (COPPA)に関するflagのみ存在する。

Attribute | Type | | Description
-- | -- | -- |--
coppa | integer | | 0の場合は規制の対象にならないrequest。1の場合は規制の対象になるrequest。
iext | object | | extension

### 3.2.4 Imp

Attribute | Type | | Description
-- | -- | -- | --
id | string | required | 1から始まるimpressionのID
metric | object array | | Metric objectの配列
banner | object | | Banner object。impressionがbanner adの場合に必要
video | object | | Video object。impressionがvideo adの場合に必要。
audio | object | | Audio object。impressionがaudio adの場合に必要。
native | object | | Native object。impressionがnative adの場合に必要。
pmp | object | | Pmp object。このimpressionにprivate marketplaceの
displaymanager | string | | 実際の広告のrenderingを行う仲介業者やSDKなど(通常はvideo や mobileなど)。videoとappで推奨推奨される。
displaymanagerver | string | | displaymanagerのversion
instl | integer | default 0 | 1はinterstitialかfull screenで、0はinterstitialでない。
tagid | string | | ad の場所やadを表すtagをつける。debugやbuyerの最適化で使われる
bidfloor | float | default 0 | このimpressionに対するCPM換算でののminimum bid
bidfloorcur | string | default "USD" | bidfloorのcurrency。ISO-4217で記述する。
clickbrowser | integer | | creativeをclickした時に、開かれるbrowserの種類。0がembeddedで、1はnativeである。iOS9.xのSafari View Conttrollerはnativeに分類される。
secure | integer | | creativeにHTTPS URLが必要かどうかのフラグ。0は不要。1は必要。
iframebuster | string array | | exchangeがサポートしているiframe busterの名前の配列
exp | integer | | 
ext | object | | extension

### 3.2.5 Metric
impresisonに対してmetricのarrayが付随する。
impressionに対する直近のCTRやviewablityなどの情報をbidderに提供する。

Attribute | Type | | Description
-- | -- | -- | --
type | string | required | 
value | float | required | metricの値
vendor | string | recommended | valueの情報元。exchange自身が情報元の場合は`EXCHANGE`を使うことが推奨される。
ext | object | | extension

### 3.2.6 Banner

Attribute | Type | | Description
-- | -- | -- |
format | object aray | recommended | banner sizeを表すforamt objectの配列。何も指定しない場合は、`w`, `h` objectを使うことが推奨される。
w | integer | | deviceに依存しないpixcelサイズ。`format` objectを指定しない場合に推奨される。
h | integer | | deviceに依存しないpixcelサイズ。`format` objectを指定しない場合に推奨される。
wmax | integer | DEPRECATED | maximum width
hmax | integer | DEPRECATED | maximum height
wmin | integer | DEPRECATED | minimum width
hmin | integer | DEPRECATED | minimum height
btype | integer array | | banner typeでのblock list。List 5.2
battr | integer array | | craetive attributeでのblock list。 List 5.3
pos | integer | | スクリーン上のad position。List 5.4
mimes | string array | | contentのMIME type。よく使われるものは"application/x-shockwave-flash", "image/jpg", "image/gif"
topframe | integer | | bannerがtopframeにある場合。
expdir | integer array | | bannerがexpandされる方向。List 5.5
api | integer array | | サポートしているAPIのlist。何も指定しない場合はsupportしているAPIはなし。List 5.6
id | string | | bannerのID。companion adを表現するために、video objectと一緒にbannerを使う場合に、推奨される。impressionの中でunique。IDは通常1から始まる
vcm | integer | | 
ext | object | | extension

### 3.2.7 Video
in-stream video impressionの情報。
多くのfieldは必須ではない。
VAST standardに従う。
banner objectの配列によってcompanion adなどが、supportされる。


Attribute | Type | | Description
-- | -- | -- |
mimes | string array | required | "video/x-ms-wmv", "video/mp4"などのMIME
minduration | integer | recommeded | 最小のvideo ad duration in sec
maxdurationt | integer | recommeded | 最大のvide ad duraiont in sec
protocols | integer | recommended| supportしているvideo protocolの配列。`protocol`か`protocols`で少なくとも1つのprotocolを指定する。List 5.8.
protocol | integer | DEPRECATED | 
w | integer | recommended | devideに依存しないvideo playerのwidth
h | integer | recommended | devideに依存しないvideo playerのheigth
startdelay | integer | recommended | pre-roll, mid-roll, post-rollのstart delayをsecondで表現。List 5.12.
placement | integer | | impressionの表示位置。List 5.9.
linearity | integer | | impressionがlinearかnonlinearか。何も指定しない場合は全て許容。List 5.7.
skip | integer | | videoがskip可能かどうか。0は不可、1は可能。bidderがskippableなmarkup/creativeを送った場合、bid objectは`attr`の配列に16を指定する必要がある。
skipmin | integer | | adがskippableの場合に、この秒数より長いvideoはskip可能とする
skipafter | integer | default 0 | adがskippableの場合に、何秒後にskip可能かを指定する。
sequence | integer | | bid requestで複数のad impressionが提供されたとき、impressionを順序づけるための番号。
battr | integer array | | creativeの属性のblock list。List 5.3
maxextended | integer | | extensionが許可されていたときに、最大のextensionの時間。0か指定なしの場合は、extensionは不許可。-1はextensionが許可され、制限なし。0より大きい場合は、`maxduration`の値をこえて再生される時間の秒数。
minbitrate | integer | | minimum bit rate in Kbps.
maxbitrate | integer | | maximum bit rate in Kbps.
boxingallowed | integer array | default 1 | 4:3のcontentを16:9 windowにletter boxing可能かどうか。0は不可, 1は可能
playbackmethod | integer array | | 利用される可能性のあるplayback method。何もなければ何らかの方法が利用される。慣習的に1つのmethodのみが利用されている。将来的には1つの整数値に仕様変更される可能性がある。配列の最初の配列のみを使うことが強く推奨される。List 5.10.
playbackend | integer | | playbackの終了となるイベント。List 5.11.
delivery | integer array | | 動画の提供方法(e.g. streaming, progressive)何もなければ全てsupportしている。List 5.15.
pos | integer | | screen上のAd postion. List 5.4.
companionad | object array | | Banner objectのarray。companion adを使う場合
api | integer array | | supportしているAPI frameworks。List 5.6. 何も指定しない場合はsupportしているAPIはなし。
companiontype | integer array | | supportしているVAST companion ad type. List 5.14. companionad arrayが指定されている場合は推奨される。companionadのbannerが一つでもend-cardとして描画された場合、vcm属性としてbannerを指定する
ext | object | | extension

### 3.2.8 Audio
in-stream video impressionの情報。
多くのfieldは必須ではない。
DAAST standardに従う。

`Audio` objectは`Imp` objectに含まれる。
publiserhの観点では、同じimpressionがbannerやvideo, nativeとしても提供される。

Attribute | Type | | Description
-- | -- | -- |
mimes | string array | required | `audio/mp4`などのMIME
minduration | integer | recommended | 最小のaudio ad duration in seconds
maxduration | integer | recommended | 最大のaudio ad duration in seconds
protocols | integer array | recommended | supportしているaudio protocolの配列.List 5.8.
startdelay | integer | recommended | pre-roll, mid-roll, post-rollのstart delayをsecondで表現。List 5.12.
sequence | integer | | bid requestで複数のad impressionが提供されたとき、impressionを順序づけるための番号。
battr | integer array | | creativeの属性のblock list。List 5.3
maxextended | integer | | extensionが許可されていたときに、最大のextensionの時間。0か指定なしの場合は、extensionは不許可。-1はextensionが許可され、制限なし。0より大きい場合は、`maxduration`の値をこえて再生される時間の秒数。
minbitrate | integer | | minimum bit rate in Kbps.
maxbitrate | integer | | maximum bit rate in Kbps.
delivery | integer array | | 動画の提供方法(e.g. streaming, progressive)何もなければ全てsupportしている。List 5.15.
companionad | object array | | Banner objectのarray。companion adを使う場合
api | integer array | | supportしているAPI frameworks。List 5.6. 何も指定しない場合はsupportしているAPIはなし。
companiontype | integer array | | supportしているDAAST companion ad type. List 5.14. companionad arrayが指定されている場合は推奨される。
maxseq | integer | | 同時に再生可能なaudio adsの数
feed | integer | | audio feedの型。List 5.16.
stitched | integer | | adがaudio contentと同時に提供されるか、別々に提供されるか。0は別々、1は一緒。
nvol | integer | | volume nomalization mode. List 5.17.
ext | object | | extension

### 3.2.9 Native
周囲のcontentとseemlessに見ることができる広告(e.g. sponsored Twitter or Facebook post)。
そのような場合、responseはpublisherが十分にコントロールできるだけの情報を含む必要がある。

Dynamic Native Ads APIをよぶようにしている。
request parametersとresponse markupの構造を定義する。

Attribute | Type | | Description
-- | -- | -- |
request | string | required |
ver | string | recommended | 
api | integer array | |
battr | integer array | |
ext | object | | extension

### 3.2.10 Format
表示可能なサイズを表現。
Flex Ad parametersでbanner impressionを表現できる。
`w`/`h`かFlex Adの`wration`/`hration`/`wmin`の形式の指定が可能

Attribute | Type | | Description
-- | -- | -- |
w | integer | | deviceに依存しないwitdhを pixelで
h | integer | | heightに依存しないheightを pixelで
wratio | integer | | 比率でのwidth
hratio | integer | | 比率でのheight
wmin | integer | | deviceに依存しないminimum widthをpixelで指定
ext | object | | extension

### 3.2.11 Pmp
buyerとsellerの間のdirect dealのためのprivate marketplace.
実際のdealは`Deal` objectで表現。
Seciton 7.3で詳しく述べる。

Attribute | Type | | Description
-- | -- | -- |
private_auction | integer | default 0 | 0は全てのbidを許可、1はbidは一部のseatに制限されている
deals | object array | `Deal` objectの配列。これで指定したdealのみ取引の対象
ext | object | | extension

### 3.2.12 Deal
buyerとsellerの間ので事前に成立しているdealを表す。
`Pmp`が存在する場合は、このobjectで表現されたDealに取引が制限される。
Seciton 7.3を見る。

Attribute | Type | | Description
-- | -- | -- |
id | string | required | direct dealのID
bidfloor | float | default 0 | floor priceをCPMで表現する
bidfloorcur | string | default 0 | ISO-4217でbidfloorの通貨を指定する
at | integer | | bid requestのauction type。1はfirst price, 2はsecond price plus, 3は`bidfloor`で取引する
wseat | string array | | bidが許可されているbuyer seats (e.g. advertiser, agencies) のwhite list。seatのIDを記載する
wadomain |string array | | bidが許可されるadvertiserのdomain(e.g. advertiser.com)m
ext | object | | extension

### 3.2.13 Site
広告の表示先がwebsiteの場合に使用する。
`Site`か`App`の一方を指定する。
少なくともsite IDかpage URLを指定するのが望ましいが、強く推奨されているわけではない。

Attribute | Type | | Description
-- | -- | -- |
id | string | recommended |　exchangeが指定するsite ID
name | string | | website name
domain | string | | websiteのdomain (e.g. mysite.foo.com)
cat | string array | | steのcategoryをIAB content categoryの配列として表現。List 5.1
sectioncat | | | siteのsectionのcategoryをIAB content categoryの配列として表現
pagecat | string array | | siteのpageのcategoryをIAB content categoryの配列として表現
page | string | | impressionが表示されるsiteのURL
ref | string | | impressionが発生したpageへのreferrer
search | string | | impressionが発生したpageへの検索ワード
mobile | integer | | mobile deviceに対してsiteが最適化されるか。0は最適化されない、1はされる。
privacypolicy | integer | | siteがprivacypolicyがある場合は、1でない場合は0
publisher | object | | siteの`Publisher`の詳細
content | object | | site内のcontentの詳細
keywords | string | | siteを表すKeywordをcomma区切りで表現
ext | object | | extension

### 3.2.14 App
広告の表示先がappの場合に使用する。
`Site`か`App`の一方を指定する。
App IDかbundleの一方を提供するのが望ましいが、強く推奨されてはいない。

Attribute | Type | | Description
-- | -- | -- |
id | string | recommended | exchangeごとのApp ID
name |string | | App name. publisherが指定した別名。
bundle | string | | Exchangeに依存しないplatformごとのapplicationの識別子。iOSはnumeric ID. Androidはbundle or package name(e.g. com.foo.mygame)
domain | string | | appのdomai (e.g. `mygame.foo.com`)
storeurl | string | | installされたappのApp sotreのURL. IQG 2.1に準拠。
cat | string array | | appのIAB content categoryによるcategoryのarray. List 5.1
sectioncat | string array | | appの現在のsectionのIAB content categoryによるcategoryのarray. List 5.1
pagecat | string array | | appの現在のpageのIAB content categoryによるcategoryのarray. List 5.1
ver | string | | applicationのversion
privacypolicy | integer | | appがprivacy policyを保つ場合は1ない場合は0
paid | integer | | appがfreeなら0, paid versionなら1
publisher | object | | appのpublisherの詳細
content | object | | appのcontentの詳細
keywords | string | | appのkeywordsのcomma separetd list
ext | object | | extension

### 3.2.15 Publisher
広告が表示されるmedia, siteのpublisehrの情報。
publisherは基本的にsellerになる。

Attribute | Type | | Description
-- | -- | -- |
id | string | | Exchangeによる publisherのID
name | string | | publisherの名前
cat | string array | | IAB content categoryによるpublisherのcategoryのarray. List 5.1
domain | string | | publisherの最も上位のdomain (e.g. `publisher.com`)
ext | object | | extension

### 3.2.16 Content
impressionが表示されるページのcontentの情報。
contentはsyndicated/non syndicatedの両方の可能性がある。
このobjectはimpressionの発生したcontentがsyndicated contentの場合に便利である。
syndication methodの場合はexchangeがpageのcontentの情報を持ってない場合がある。
iframeでvideo contentが埋め込まれている場合は、埋め込まれた先のpageの情報がない場合がある。

Attribute | Type | | Description
-- | -- | -- |
id | string | | contentのID
episode | integer | | episode number
title | string | | contentのtitle。Videoの場合。Videoの場合、`Search Committee`, `A New Hope`, `Endgame`. video以外の例、`Why an Antarctic Glacier Is Melting So Quickly`.
series | string | | contentのseries。Videoの例、`The Office`, `Star Wars`, `Arby N The Chief`, 海外のシリーズもののドラマと映画, web movie。Video以外の例、`Ecocentric` (time magazineのblogのcategory).
season | string | | Content season. (e.g. `Season 3`)
artist | string | | contentにcreditされたartist
genere | string | | contentを表すgenre (e.g. rock, pop, etc)
album | string | | contentが所属するalbum. audioの場合に利用される。
isrc | string | | ISO-3961のInternational Standard Recording Codeの識別子。国際標準レコーディングコード。音源の識別子。
producer | object | | contentの`Producer`の情報
url | string | | contentのURL. buy-sideのための情報
cat | string array | | IAB content categoryによるcontent producerのcategoryのarray. List 5.1
prodq | integer | |  production quality. List 5.13.
videoquality | integer | deprecated | prodqができたのでdeprecated.
context | integer | | contentのtype. (e.g. game, video, text, etc.). List 5.18
contentrating | string | | content rationg (e.g. MPAA(アメリカの映画協会))
userrating | string | | contentのuser rating. (e.g. number of stars, likes, etc.)
qagmediarating | integer | | IQG guidelineごとのmediaのrating. List 5.19.
keywords | string | | contentのkeywordsをcomma separatedで。
livestream | integer | | 0=not live, 1=content is live (e.g. stream, live blog)
sourcerelationship | integer | | 0=indirect, 1=direct. ?
len | integer | | contentの秒数。audio, videoの場合に利用。
language | string | | ISO-639-1-alpha-2でcontentの言語を指定。
embeddable | integer | | contentが埋め込み可能かどうか、0は埋め込み不可、1は可能
data | object array | | 追加のcontent data. `Data` はそれぞれ別のdata souceになる
ext | object | | extension

### 3.2.17 Producer
adが表示されるcontentのproducerの情報。
syndicatedの場合に有用。
異なるpublisherで同じcontentが配布されているときに、syndicatedかどうかを識別できる。

Attribute | Type | | Description
-- | -- | -- |
id | string | | content producerかoriginatorのID. contentがsyndicateの場合に有用。
name | string | | content producer or originatorの名前. (e.g. `Warner Bros`)
cat | string array | | IAB content categoryによるcontent producerのcategoryのarray. List 5.1
domain | string | | producerの最上位のdomain. (e.g. `producer.com`)
ext | object | | exntension

catはcontentのcatとかぶるきがするけど、どうするの？

### 3.2.18 Device
userが仕様しているdeviceについての情報。
hardware, platform, location, carrier dataなどの情報を含む。
mobile handoset, desktop computer, set top box, などのdeviceを表す。

Attribute | Type | | Description
-- | -- | -- |
ua | string | recommended | Browserのuser agent
geo | object | recommeded | `Geo` objectでuserの現在位置についての情報を記載。
dnt | integer | recommeded | `Do not Track` flag. userのbrwoserに指定されている場合は1, 指定がない場合は0
lmt | integer | recommeded | `Limit Ad Tracking` iOSやAndroidに埋め込まれているsignal. 0はtrackingの制限なし、1はcomercial guidelineに従う必要がある。
ip | string | recommeded | deviceに最も近いIPv4 address.
ipv6 | string | | deviceに最も近いIPv6 address.
devicetype | integer | | deviceの一般的なtype. List 5.21.
make | string | | Deviceのmake (e.g. `Apple`)
model | string | | Device model (e.g `iPohone`)
os | string | | Device　operating system (e.g. `iOS`)
osv | string | | Device operating system version (e.g `3.1.2`)
hwv | string | | deviceのhardwareのversion (e.g. `5S` for iPhone)
h | integer | | screenの物理的な高さをpixelで。
w | integer | | screenの物理的な長さをpixelで。
ppi | integer | | pixcel per inch. screen sizeをppiで指定。
pxration | float | | deviceに依存しないpixcelでの比率。
js | integer | | JavaScriptのsupportがあるか。0はなし、1はあり
geofetch | integer | | bannerで実行されるときにJavascriptのgeolocation APIが使えるかどうか。0は使えない、1は使える。
flashver | string | | browserがsupportしているflashのversion.
language | string | | ISO-639-1-alpha-2でBrowserの言語を指定。
carrier | string | | Carrier or ISP (e.g. `VERIZON`, ベライゾン・ワイヤレスというcarrierの会社)を指定。bidderに事前に送信される名前。
mccmnc | string | | mobileのcarrierのMCC-MNC code (e.g. `310-005`, verizon Wireless CDMA in the USA). Mobile Country Code, Mobile Network Code. 詳細はwikipediaを見ろ。MMCとMNCの間の`-`は必須。
connectiontype | integer | | Networkのconnection type. List 5.22
ifa | string | | advertiserにより制限されたID. Hash化してない。?
didsha1 | string | |  SHA1でhash化したHardware device ID. (e.g. IMEI)
didmd5 | string | | MD5でhash化したHardware device ID.
dpidsha1 | string | | SHA1でhash化したPlatform device ID. (e.g. Android ID)
dpidmd5 | string | | MD5でhash化したPlatform device ID. (e.g. Android ID)
macsha1 | string | | SHA1でhash化したMAC address.
macmd5 | string | | MD5でhash化したMAC address
ext | object | | extension

Best Practice

devicemake, model, operating system, or carriesのOpen sourceのListはない。
exchangeは商用のlistや有料のListを利用している。
open standardのこれらのlistが利用可能になるまで、exchangeが作成したこれらのlistをあらかじめ、閲覧できるようにしておくことが強く推奨される。

mobileの適切なIPの検出は単純ではない。
送信元のIP addressを表す`x-forwarded-for` headerを調べ carrierのprivate networks (e.g. 10.x.x.x or 192.x.x.x), carrierのIP addressの範囲を調べることなどが必要。
ExchangeはIPをbidderに提供する場合はこれらを調べ慎重に実装する必要がある。

* [XFF（ X-Forwarded-For ）とは](http://www.infraexpert.com/study/loadbalancer11.html)


### 3.2.19 Geo
geographic locationの情報を表示。
`Device` objectで利用された場合は、deviceのuserの現在位置を表す。
`User` objectで利用された場合は、 Userの活動の拠点（現在位置でなくても良い）を表す。
`lat/lon`は`type`属性の精度を満たす場合に指定されるべきである。

Attribute | Type | | Description
-- | -- | -- |
lat | float | | Lantitude(緯度). -90.0から90.0. 負は南.
lon | float | | Longtitude(経度). -180.0から180.0. 負は西.
type | integer | | location dataの情報元。`lat/lon`を指定する場合は推奨される。List 5.20
accuracy | integer | | locationの精度。`lat/lon`が指定される場合に推奨され、`type=1`のときは、device location serviceから取得される。deviceからreportされる. OSごとのdocumentを確認する。
lastfix | integer | | geolationが確定するまでに計測にかかった時間を秒で指定。deviceは複数の問い合わせに対応するために、locationをcacheする場合がある。
ipservice | integer | | IPからgeolocationを特定するために利用したproviderやservice. `type=2`の場合. List 5.23
country | string | | ISO-3166-1-alpha-3を使ったcountry code.
region | string | | ISO-3166-2を使ったregion code. USAの場合は2-letter state code.
regionfips104 | string | | FIPS 10-4 notationを使ったcountryのregion. NIST(アメリカ国立標準技術研究所)は2008にFIPS 10-4を利用するのをやめた。
metro | string | | google metro code. Nielsen DMAsと同じではないが、似たもの。AppendixにcodeへのLinkがある。
city | string | | United Nations Code for Trade & Transport Locationsを使ったcity. appendixにcodeへのlinkがある。
zip | string | | zip or postal code.
utcoffset | integer | | local time. UTCからの+/-の分。
ext | object | | extension

### 3.2.20 User
deviceのuserについての情報。


Attribute | Type | | Description
-- | -- | -- |
id | string | recommeded | exchangeごとのuserのID.
buyeruid | string | recommeded | buyerごとのuserのID. exhcnageがbuyerのために対応させたもの。`buyeruid`か`id`の少なとも一方は指定することが推奨される。
yob | integer | recommeded | 4-digit integerでの生まれた年
gender | string | | `M`はmale, `F`はfemail, `O`はother. 省略は不明。
keywords | string | | keywords, interests, or intentを表すcomma separated list.
customdata | string | | exchangeのcookieに設定されたdata. dataは、base85 cookie safe characterで、formatは何でも良い。JSON encodingはquotationをescapeしている必要がある。
geo | object | | `Geo` object. userの活動拠点。現在位置である必要はない。
data | object array | | 追加のuser dataを`Data` objectで表現。異なる`Data` objectは異なるdata sourceを表す。
ext | object | | extension


### 3.2.21 Data

Attribute | Type | | Description
-- | -- | -- |
id | string | |
name | string | |
segment | object array | |
ext | object | | extension

### 3.2.22 Segment

Attribute | Type | | Description
-- | -- | -- |

# 4. Bid Response Specification

## 4.1 Object Model

## 4.2 Object Specification

### 4.2.1 BidResponse

### 4.2.2 SeatBid

### 4.2.3 Bid

## 4.3 Ad Serving Options

### 4.3.1 Markup Served on the Win Notice

### 4.3.2 Markup Served in the Bid

### 4.3.3 Comparison of Ad Serving Approaches

## 4.4 Substitution Macros

# 5. Enumerated Lists Specification

## 5.1 Content Categories

## 5.2 Banner Ad Types

Value | Description
--|--
1 | XHTML Text Ad
2 | XHTML Banner Ad
3 | JavaScript Ad; must be valid XHTML
4 | iframe

## 5.3 Creative Attributes
Creativeの分類

Value | Description
--|--
1 | Audio Ad (Auto Play)
2 | Audio Ad (Userが再生する)
3 | Expandable (Automatic)
4 | Expadable (Userのclick)
5 | Expadable (Userのrollover)
6 | In-Banner Video Ad (Autoplay)
7 | In-Banner Video Ad (Userが再生する)
8 | Pop (PopOver, Pop under, Pop upon Exit)
9 | 挑発的、刺激的な画像
10 | ゆれる、ひかる、明滅する、アニメーション
11 | 調査
12 | テキストのみ
13 | User intractive (埋め込みのゲーム）
14 | Windows dialog, alertでの広告
15 | AudioのOn/OFF buttonがある
16 | 広告のskipがある (skip button on pre0roll video)

## 5.4 Ad Position
広告の位置

Vale | Description
-- | --
0 | Unkown
1 | スクロールしなくても見ることができるウェブページの上部。above-the-fold
2 | DEPRECATED 
3 | スクロールしないと見ることができないウェブページの下部
4 | web pageのHeader
5 | web pageのFooter
6 | web pageのSidebar
7 | FUll Screan

## 5.5 Expandable Direction


## 5.6 API Frameworks
PublisherのsupportするAPI

* MRAID-1
    * MRAID-2のsubset
* OpenRTB2.1以前は、3は`MRAID`だったが、MRAIDの仕様を全て実装していないPublisherもあったので、MRAIDのsubsetを定義し、分離した

Value | 
-- |--
1 | VPAID 1.0
2 | VPAID 2.0
3 | MRAID-1
4 | ORMMA
5 | MRAID-2

## 5.7 Video Linearity
in-stream/linear videoは、以下のvideo contentの一部として広告が表示される形式のもの

* pre-roll
    * video contentの開始前
* post-roll
    * video contentの終了後
* mid-roll
    * video contentの途中
    * CMみたいな形式か

non-linearなものは、Overlayなどのvideo contentに重なる形で表示される広告

Value | Descaription
-- | --
1 | Linear / In-Stream
2 | Non Linear / Overlay

## 5.8 Protocols
Exchangeがsupportするbid responseのprotocol

Value | Description
-- | --
1 | VAST 1.0
2 | VAST 2.0
3 | VAST 3.0
4 | VAST 1.0 Wrapper
5 | VAST 2.0 Wrapper
6 | VAST 3.0 Wrapper

## 5.9 Video Placement Types

## 5.10 Playback Methods

## 5.11 Playback Cessation Modes

## 5.12 Start Delay
Linear/non-linear関係なく、videoがいつ開始するか

|Value | Descriptino
|-- | --
|> 0 | Mid-Rollで、数字は開始までの秒数
|0 | Pre-Roll
|-1 | generic Mid-Roll
|-2 | generic Post-Roll

## 5.13 Production Quality
VideoのQuality。
以下の用語は、IABで定義されているものに準拠。

Value | Description
-- | --
0 | Unkown
1 | Professionally produce
2 | 
3 | 


## 5.14 Comparison Types

## 5.15 Content Delivery Methods

## 5.16 Feed Types

## 5.17 Volume Normalization Modes

## 5.18 Content Context

## 5.19 IQG Media Ratings

## 5.20 Location Type

## 5.21 Device Type

## 5.22 Connection Type

## 5.23 IP Location Services

## 5.24 No-Bid Reason Codes

## 5.25 Loss Reason Codes

## 5.9 Video Plyback Methods
playbackの方法。

Value | Description
-- | --
1 | Auto PlayでSound On
2 | Auto PlayでSound Off
3 | Clickで開始
4 | Mouse-Overで開始

# 6. Bid Request/Response Samples

## 6.1 GitHub Repository

## 6.2 Validator

## 6.3 Bid Requests 

### 6.3.1 Example 1 - Simpler Banner

### 6.3.2 Example 2 - Expandable Creative

### 6.3.3 Example 3 - Mobile

### 6.3.4 Example 4 - Video

### 6.3.5 Example 5 - PMP with Direct Deal

### 6.3.6 Example 6 - Native Ad

## 6.4 Bid Responses

### 6.4.1 Example 1 Ad Served on Win Notice

### 6.4.2 Example 2 VAST XML Document Returned inline

### 6.4.3 Example 3 Direct Deal Ad Served on Win Notice

### 6.4.4 Example 4 Native Markup Returned inline

# 7. Implementation Notes

## 7.1 No-Bid Signaling

## 7.2 Impression Expiration

## 7.3 PMP & Direct Deals

## 7.4 Skippability

## 7.5 COPPA Regulation Flag

# Appendix

## Reference
