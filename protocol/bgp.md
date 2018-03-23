---
title: BGP
---

## BGP
BGPはRFC4271で定義されるBGP-4（BGP version 4）を指し、BGPとBGP-4という単語はほぼ同じ意味。
BGPはTCPポート179

* AS number
    * 2bytesだったが、4bytesに拡張された
    * ASN

Messages

* OPEN
    * TCP sessionの確立後に最初に送る
    * AS番号やピアの認証を行い、拡張機能などについて情報の交換
* KEEPALIVE
    * peerの確立を確認するために定期的に送る
* UPDATE
    * 経路の更新
    * 経路の追加と削除を知らせる
* NOTIFICATION
    * 継続不能なrrorが発生した場合に送る
    * 送信側は送信後にTCPsessionの切断をする

path attribute

* ORIGIN
    * IGP
        * AS内部で生成された経路
    * EGP
        * AS外部で異性生された経路
    * INCOMPLETE
        * IGP/EGP以外
* AS_PATH
    * 通過してきたAS番号を並べたもの
* NEXT_HOP
    * 

## Reference
* [インターネット10分講座：BGP - JPNIC](https://www.nic.ad.jp/ja/newsletter/No35/0800.html)
