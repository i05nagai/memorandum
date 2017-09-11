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

Indexを作る

```
estcmd create [-tr] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-attr name type] db
```

document draftをindexに登録する。
fileがdocument draft

```
estcmd put [-tr] [-cl] [-ws] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] db [file]
```

indexからDocumentの情報を削除

```
estcmd out [-cl] [-pc enc] db expr
```

indexのattributeを編集

```
estcmd edit [-pc enc] db expr name [value]
```

```
estcmd get [-nl|-nb] [-pidx path] [-pc enc] db expr [attr]
```

```
estcmd list [-nl|-nb] [-lp] db
```

```
estcmd uriid [-pidx path] [-nl|-nb] [-pc enc] db expr
```

indexの最適化する。
使い続けているとindexが肥大化する。

```
estcmd optimize [-onp] [-ond] db
```

localのfileを検索して、indexに登録する。

* [file|dir]
    * fileの場合はdocumentのpathのlist
    * `-`の場合は標準入力
    * dirの場合はdir以下

```
estcmd gather [-tr] [-cl] [-ws] [-no] [-fe|-ft|-fh|-fm] [-fx sufs cmd] [-fz] [-fo] [-rm sufs] [-ic enc] [-il lang] [-bc] [-lt num] [-lf num] [-pc enc] [-px name] [-aa name value] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-ss name] [-sd] [-cm] [-cs num] [-ncm] [-kn num] [-um] db [file|dir]
```

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

