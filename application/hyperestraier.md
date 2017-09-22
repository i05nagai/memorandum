---
title: Hyper Estraier
---

## Hyper Estraier
全文検索system.

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

```
estcmd create [-tr] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-attr name type] db
```

filesystemを探索して、indexに登録する。

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
estcmd gather [-tr] [-cl] [-ws] [-no] [-fe|-ft|-fh|-fm] [-fx sufs cmd] [-fz] [-fo] [-rm sufs] [-ic enc] [-il lang] [-bc] [-lt num] [-lf num] [-pc enc] [-px name] [-aa name value] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-ss name] [-sd] [-cm] [-cs num] [-ncm] [-kn num] [-um] db [file|dir]
```

```
estcmd put [-tr] [-cl] [-ws] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] db [file]
```

```
estcmd out [-cl] [-pc enc] db expr
```

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

index内の文書のkeywordを抽出したdatabaseを作る。

* `-um`
    * keywordの抽出に形態素解析をする

```
estcmd extkeys [-no] [-fc] [-dfdb file] [-ncm] [-ni] [-kn num] [-um] [-attr expr] db [prefix]
```

## Tips

属性検索は遅い。
属性にもindexをはれるが、通常の検索より遅くCPU resourceが必要。
属性にindexをはるとindexの作成が遅くなる。

## Reference
* [Hyper Estraier: a full-text search system for communities](http://fallabs.com/hyperestraier/)
* [unoh.github.com by unoh](https://unoh.github.io/2008/10/10/tips_for_hyperestraier.html)
