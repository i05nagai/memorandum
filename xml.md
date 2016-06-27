# xml

## xmlとは


## 要素
要素(タグ)は次のような構造を持つ

```xml
<element_name attribution="value">contents</element_name>
```

```xml
<element_name attribution="value"/>
```

* `element_name`
    * 要素の名前
    * 属性がcontentsを含まない場合は`<element_name />`と書くことができる。
* `attiritbuion`
    * 要素は0個以上の属性を含む
    * 属性は属性名と値のペア
* `contents`
    * 要素名の間はテキストを記載できる。

## 名前空間
xmlは名前空間をもつことができる。
名前空間によって、同じ名前の要素で名前空間が異なる要素をもつことができる。
名前空間の宣言は下記のようになる。

```xml
<xmlns:xsd="http://www.w3.org/2001/XMLSchema"/>
```

上では`xsd`という名前空間を宣言している。
`xsd`の後のURLは識別子としての役割をしており、`xsd`という名前空間がそのURLで定義されたものであるということを示す。
`xsd`名前空間によって下記の2つの要素は異なる要素を定義している。
```
<xsd:element name="hoge" type="xsd:string" />
<element name="hoge" type="xsd:string" />
```



