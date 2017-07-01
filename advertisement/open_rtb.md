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

Object
--|--
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

Attributes | Type | condition | Descriptin=on
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
allimps | integer | default 0 | exchange





### 5.2 Banner Ad Types

Value | Description
--|--
1 | XHTML Text Ad
2 | XHTML Banner Ad
3 | JavaScript Ad; must be valid XHTML
4 | iframe

### 5.3 Creative Attributes
Creativeの分類

Value | Description
--|--
1 | Audio Ad (Auto Play)
1 | Audio Ad (Userが再生する)
1 | Expandable (Automatic)
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

### 5.4 Ad Position
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

### 5.5 Expandable Direction


### 5.6 API Frameworks
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

### 5.7 Video Linearity
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


### 5.8 Vieo Bid Response Protocols
Exchangeがsupportするbid responseのprotocol

Value | Description
-- | --
1 | VAST 1.0
2 | VAST 2.0
3 | VAST 3.0
4 | VAST 1.0 Wrapper
5 | VAST 2.0 Wrapper
6 | VAST 3.0 Wrapper


### 5.9 Video Plyback Methods
playbackの方法。

Value | Description
-- | --
1 | Auto PlayでSound On
2 | Auto PlayでSound Off
3 | Clickで開始
4 | Mouse-Overで開始

### 5.10 Video Start Delay
videoの開始位置。
Linear/non-linear関係なく、videoがいつ開始するか

|Value | Descriptino
|-- | --
|> 0 | Mid-Rollで、数字は開始までの秒数
|0 | Pre-Roll
|-1 | generic Mid-Roll
|-2 | generic Post-Roll

### 5.11 Video Quality
VideoのQuality。
以下の用語は、IABで定義されているものに準拠。

Value | Description
-- | --
0 | Unkown
1 | Professionally produce
2 | 
3 | 

## Reference
