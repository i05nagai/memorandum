---
title: Hyper Estraier
---

## Hyper Estraier
全文検索system.

For Ubuntu

```
sudo apt-get install hyperestraier
```

install先は`/usr/lib/estraier`

## Attribute
body textに対してattributeを付与できる。
systemで予約されているattributeは`@`で始まる。
attributeは`%`で始まってはいけない。


* @id : the ID number determined automatically when the document is registered.
* @uri : the location of a document which any document should have.
* @digest : the message digest calculated automatically when the document is registered.
* @cdate : the creation date.
* @mdate : the last modification date.
* @adate : the last access date.
* @title : the title used as a headline in the search result.
* @author : the author.
* @type : the media type.
* @lang : the language.
* @genre : the genre.
* @size : the size.
* @weight : the scoring weight.
* @misc : miscellaneous information.

## File formats

* plain text
* HTML
* MIME
* Document Draft
    * `.est`の拡張子をもつ独自format
    * sampleは以下

```
@uri=http://www.music-estraier.com/mididb/t/tw/twinkle.kar
@title=Twinkle Twinkle Little Star
@author=Jane Taylor
@cdate=2004-11-01T23:11:18+09:00
@mdate=2005-03-21T08:07:45+09:00
category=chorus,dance

Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!
        Twinkle Twinkle Little Star
        Jane Taylor
```

## Search condition
`@title STRINC IMPORTANT`はこんな感じで条件をつけることができる。

* STREQ : is equal to the string
* STRNE : is not equal to the string
* STRINC : includes the string
* STRBW : begins with the string
* STREW : ends with the string
* STRAND : includes all tokens in the string
* STROR : includes at least one token in the string
* STROREQ : is equal to at least one token in the string
* STRRX : matches regular expressions of the string
* NUMEQ : is equal to the number or date
* NUMNE : is not equal to the number or date
* NUMGT : is greater than the number or date
* NUMGE : is greater than or equal to the number or date
* NUMLT : is less than the number or date
* NUMLE : is less than or equal to the number or date
* NUMBT : is between the two numbers or dates

結果の順序を以下のように指定できる。

```
STRA : ascending by string
STRD : descending by string
NUMA : ascending by number or date
NUMD : descending by number or date
```

## CLI
indexを作る

* `-attr name type`
    * attribute indexの対象のattiribution nameとtypeを指定
    * 複数指定可能
* `db`
    * indexのdb

Indexを作る

```
estcmd create [-tr] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-attr name type] db
```


```
estcmd optimize [-onp] [-ond] db
```

indexの最適化する。
使い続けているとindexが肥大化する。

```
estcmd gather [-tr] [-cl] [-ws] [-no] [-fe|-ft|-fh|-fm] [-fx sufs cmd] [-fz] [-fo] [-rm sufs] [-ic enc] [-il lang] [-bc] [-lt num] [-lf num] [-pc enc] [-px name] [-aa name value] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-ss name] [-sd] [-cm] [-cs num] [-ncm] [-kn num] [-um] db [file|dir]
```

localのfileを検索して、indexに登録する。
fileがdocument draft

* [file|dir]
    * fileの場合はdocumentのpathのlist
    * `-`の場合は標準入力
    * dirの場合はdir以下
* `-il ja`
    * 文字コードの判定で優先される言語
* `-xs`
    * 50000件未満の文書を登録することを想定してインデックスを作成
* `-xl`
    * 300000件以上の文書を登録することを想定してインデックスを作成
* `-xh`
    * 1000000件以上の文書を登録することを想定してインデックスを作成
* `-xh2`
    * 5000000件以上の文書を登録することを想定してインデックスを作成
* `-xh3`
    * 10000000件以上の文書を登録することを想定してインデックスを作成
* `-cs`
    * cache memoryのsizeをMBで指定
    * defaultは64MB
* `-tr`
    * 既に文書のindexがある場合もindexを生成する
* `-cl`
    * 上書きされた文書の整理
* `-sd`
    * ファイルの更新日時を文書の属性として追加
* `-cm`
    * 文書の属性の更新日時がファイルの更新日時より古い場合にのみindexを作成
* `file`
    * fileを文書として登録
* `dir`
    * dir以下の文書を検索して登録


```
estcmd put [-tr] [-cl] [-ws] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] db [file]
```

filesystemを探索して、indexに登録する。
document draftをindexに登録する。

```
estcmd out [-cl] [-pc enc] db expr
```

indexからDocumentの情報を削除

```
estcmd edit [-pc enc] db expr name [value]
```

indexのattributeを編集

```
estcmd get [-nl|-nb] [-pidx path] [-pc enc] db expr [attr]
```

```
estcmd list [-nl|-nb] [-lp] db
```

```
estcmd uriid [-pidx path] [-nl|-nb] [-pc enc] db expr
```

```
estcmd extkeys [-no] [-fc] [-dfdb file] [-ncm] [-ni] [-kn num] [-um] [-attr expr] db [prefix]
```

index内の文書のkeywordを抽出したdatabaseを作る。

* `-um`
    * keywordの抽出に形態素解析をする

```
estcmd search [-nl|-nb] [-pidx path] [-ic enc] [-vu|-va|-vf|-vs|-vh|-vx|-dd] [-sn wnum hnum anum] [-kn num] [-ec rn] [-gs|-gf|-ga] [-cd] [-ni] [-sf|-sfr|-sfu|-sfi] [-hs] [-attr expr] [-ord expr] [-max num] [-sk num] [-aux num] [-dis name] [-sim id] db [phrase]
```

* indexを検索する
* `-nl`
    * file lockなしでindexを開く
* `-nb`
    * blockなしでfile lock
* `-vu`
    * IDとURIをタブ区切りで表示
* `-va`
    * 属性情報こみで表示
* `-vf`
    * draft形式で表示

## Tips

属性検索は遅い。
属性にもindexをはれるが、通常の検索より遅くCPU resourceが必要。
属性にindexをはるとindexの作成が遅くなる。

## Reference
* [Hyper Estraier: a full-text search system for communities](http://fallabs.com/hyperestraier/)
* [unoh.github.com by unoh](https://unoh.github.io/2008/10/10/tips_for_hyperestraier.html)

## config

### estseek.conf
`/usr/local/share/hyperestraier/`か`/usr/share/hyperestraier`にconfのsampleがある。

* `indexname`
    * indexへのpath

```
indexname: /home/www/casket
replace: file:///home/www/public_html/{{!}}http://www.estraier.ad.jp/
```

### estproxy.conf
`/usr/lib/estraier`

* `replace`
    * documentのURLを置換方法をregular expressionで記載
    * `from_regular_expression{{!}}to_expression`の形式で指定
    * `\1`, `\2`で置換前の文字を参照できる
* `allowrx`
    * validなURLの形式をregular expressionで指定
* denyrx 
    * invalidなURLの形式をregular expressionで指定
* passaddr
    * remote serverにclientのIP addressを渡すかどうか
    * 0:no, 1:yes
* limitsize
    * mega byteでdownload可能なdataの最大sizeを指定
* urlrule
    * URL ruleをregular expressionとmedia typeで指定
* typerule
    * media typeのruleを指定
* language
    * (0:English, 1:Japanese, 2:Chinese, 3:Korean, 4:misc).
* shownavi
    * navigation barを表示するか
    * 0:no, 1:yes

```
#replace: ^http://localhost/{{!}}file:///home/mikio/public_html/
allowrx: ^http://
#allowrx: ^file://
denyrx: /\.
passaddr: 1
limitsize: 32
urlrule: \.est${{!}}text/x-estraier-draft
urlrule: \.(eml|mime|mht|mhtml)${{!}}message/rfc822
typerule: ^text/x-estraier-draft${{!}}[DRAFT]
typerule: ^text/plain${{!}}[TEXT]
typerule: ^(text/html|application/xhtml+xml)${{!}}[HTML]
typerule: ^message/rfc822${{!}}[MIME]
language: 0
shownavi: 1
```

## Reference
* [Hyper Estraier: a full-text search system for communities](http://fallabs.com/hyperestraier/)
* [Ubuntu 10.04 LTSにHyperEstraierをインストールしてみる – BTY備忘録](http://bty.sakura.ne.jp/wp/archives/88)

