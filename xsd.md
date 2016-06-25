# xsd

## xsdとは？
Xml Scheme Definitionの略。
xmlファイルのformatを指定する定義するもの。
一般にxml形式のファイルは以下のように複数個の要素(タグ)とネストした要素で構成される。

```xml
<?xml version="1.0" encoding="utf-8"?>
<tag1>
    <tag2 name="hogehoge">
    </tag2>
</tag1>
```

出現する要素の位置やネストは、xmlの形式上特に制限がない。
xsdファイルは、このxml形式のタグの構造に制限を課す。


## xsdの要素一覧
xsdの要素は大きく2つに分けられる。
* 単純型
    * 属性や子要素を持たない
* 複雑型
    * 属性や子要素を持つ
    * `xsd:complexType`を使用する。

### element

```xml
<xsd:element name="greeting" type="xsd:string"/>
```

* `name`
    * 要素の名前を指定する。
    * `greeting`という名前の要素
* `type`
    * `contents`の型を限定する。
    * `string`型の場合は、子要素も許す。

```xml
<greeting>some string here</greeting>
```

#### ref属性
`xsd:element`は`ref`属性を持てる。
例えば、同じ要素が複数個所で出てくる場合、その要素の定義を何度も書くの面倒である。
一度定義した`xsd:element`は`ref`属性によってその名前を指定することで、別の場所でも利用可能となる。
```xml
<xsd:element ref="user">
<xsd:element name="user">
    <xsd:complexType>
        <xsd:element name="name" type="xsd:string"/>
        <xsd:element name="age" type="xsd:string"/>
    </xsd:complexType>
</xsd:element>
```

#### maxOccurs/minOccurs
要素の出現回数を制限する。
* `maxOccurs`
    * 最大出現回数
    * 制限がない場合は、`unbounded`を指定する。
* `minOccurs`
    * 最小出現回数
    * なくても良い要素は`0`を指定。

### complexType
複雑型を表す。
`xsd:element`要素の直下におく。

```xml
<xsd:element name="hoge">
    <xsd:complex type>
</xsd:element>
```

### sequence
要素の順番を表す。
以下は要素が`name`要素、`age`要素の順番で書かれていることを定義している。
```xml
<xsd:sequence>
    <xsd:element name="name" type="xsd:string"/>
    <xsd:element name="age" type="xsd:string"/>
</xsd:sequence>
```


### attribute
要素に属性を指定する場合は、`xsd:attribute`を指定する。
`xsd:attribute`は`xsd:complexType`の子要素になる。

```xml
<xsd:element name="user">
    <xsd:complexType>
        <xsd:attribute name="id" type="xsd:string"/>
        <xsd:element name="name" type="xsd:string"/>
        <xsd:element name="age" type="xsd:integer"/>
    </xsd:complexType>
</xsd:element name="user">
```

```xml
<user id="hogehoge">
    <name>hoge</name>
    <age>11</age>
</user>
```

## データ型
`xsd:strinig`などのデータ型の一覧。

###  データ型
| データ型の名前     | 内容                                                  | 例                                        |
|:------------------:|:-----------------------------------------------------:|:-----------------------------------------:|
| boolean            | 真偽                                                  | true、false、1、0                         |
| base64Binary       | Base64エンコードされたバイナリ値                      | GpM7                                      |
| hexBinary          | 16進数                                                | 0FB7                                      |
| float              | 単精度32ビット浮動小数                                | -INF、-1E4、-0、0、12.78E-2、12、INF、NaN |
| double             | 倍精度64ビット浮動小数                                | -INF、-1E4、-0、0、12.78E-2、12、INF、NaN |
| decimal            | 10進数                                                | -1.23、0、123.4、1000.00                  |
| integer            | 整数                                                  | -126789、-1、0、1、126789                 |
| nonPositiveInteger | 0以下の整数                                           | -126789、-1、0                            |
| negativeInteger    | 0未満の整数                                           | -126789、-1                               |
| long               | -9223372036854775808から9223372036854775807までの整数 | -1、12678967543233                        |
| int                | -2147483648から2147483647までの整数                   | -1、126789675                             |
| short              | -32768から32767までの整数                             | -1、12678                                 |
| byte               | -128から127までの整数                                 | -1、126                                   |
| nonNegativeInteger | 0以上の整数                                           | 0、1、126789                              |
| unsignedLong       | 0から18446744073709551615までの整数                   | 0、12678967543233                         |
| unsignedInt        | 0から4294967295までの整数                             | 0、1267896754                             |
| unsignedShort      | 0から65535までの整数                                  | 0、12678                                  |
| unsignedByte       | 0から255までの整数                                    | 0、126                                    |
| positiveInteger    | 1以上の整数                                           | 1、126789                                 |


| データ型の名前 | 内容                                                                                               | 例                            |
|:--------------:|:--------------------------------------------------------------------------------------------------:|:-----------------------------:|
| duration       | ある一定の期間。例は「1年2カ月3日10時間30分12.3秒」を表す                                          | P1Y2M3DT10H30M12.3S           |
| dateTime       | 特定の日時。例は「世界時間（UTC）から5時間遅れの東部標準時における1999年5月31日午後1時20分」を表す | 1999-05-31T13:20:00.000-05:00 |
| time           | 時刻。例は「世界時間（UTC）から5時間遅れの東部標準時における午後1時20分」を表す                    | 13:20:00.000-05:00            |
| date           | 日付。例は「1999年5月31日」を表す                                                                  | 1999-05-31                    |
| gYearMonth     | グレゴリアン暦の年月。例は「1999年2月」を表す                                                      | 1999-02                       |
| gYear          | グレゴリアン暦の年。例は「1999年」を表す                                                           | 1999                          |
| gMonthDay      | グレゴリアン暦の月日。例は「5月31日」を表す                                                        | --05-31                       |
| gMonth         | グレゴリアン暦の月。例は「5月」を表す                                                              | --05--                        |
| gDay           | グレゴリアン暦の日。例は「31日」を表す                                                             | ---31                         |

| データ型の名前     | 内容                                                                                                            | 例                                  |
|--------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------|
| string             | 文字列                                                                                                          | Confirm this is electric.           |
| Again ,confirm it. |                                                                                                                 |                                     |
| normalizedString   | 改行文字、タブ文字を含まない文字列                                                                              | Confirm this is electric            |
| token              | 改行、先頭・末尾の空白、および2つ以上連続した空白を含まない文字列                                               | Confirm this is electric            |
| language           | xml:lang属性の値として有効なもの。XML 1.0で定義されている                                                       | en-GB、en-US、fr                    |
| Name               | XML 1.0 Name型。要素や属性の名前に使用可能な形式の文字列で、先頭と2文字目以降に使用できる文字が規定された文字列 | shipTo                              |
| QName              | XML Namespace のQName。名前空間URIとローカル名の組からなる                                                      | po:USAddress                        |
| NCName             | XML Namespaceの NCName。QNameより接頭辞とコロンを取り除いたもの                                                 | USAddress                           |
| anyURI             | URIの形式をした文字列                                                                                           | http://www.example.com/doc.html#ID5 |

## 参考
[title](http://www.atmarkit.co.jp/ait/articles/0312/02/news002.html)
