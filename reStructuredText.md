# reStructuredText
reStructuredTextは軽量Markup languageの一つ。
Markdownとの違いは仕様が決まっている所。
拡張子は`rst`
githubはrstに対応しているのでREADMEもrstで書ける。

## hpyerlink
hyperlinkのlink名にスペースが含まれない場合は
```rst
このように `Linkname http://hogehoge.com/`_ とすればよい。
```

hyperlinkを張るときリンク名にスペースが含まれる場合は以下のように書く。
```rst
このように、 `Link name with space`_ すれば良い。

.. _Link name with space: http://hogehoge.file/
```

## セクション
`=`や`-`などの記号をテキストのアンダーラインとして使用した場合、アンダーラインされた文字がセクションとなる。
アンダーラインはテキストと同じか、それ以上の長さにする必要がある。
もし必要ならオーバーラインもつけることができる。
```rst
===============
This is section
===============
```

pythonのdocument guidelineでは次の順序で使うよう規定されている。
* `#` 部: オーバーライン付き
* `*` 章: オーバーライン付き
* `=` セクション
* `-` サブセクション
* `^` サブサブセクション
* `"` パラグラフ
```rst
############
this is part
############

***************
this is chapter
***************

this is section
===============

this is subsection
------------------

this is subsubsection
^^^^^^^^^^^^^^^^^^^^^

tihs is paragraph
"""""""""""""""""
```

個人的にはソースコード中にドキュメントをかくことを考えて、`=`はgitのconfilict次の記号とかぶるので`=`を抜いた以下を用いた方が良い気がする。
* `#` 部: オーバーライン付き
* `*` 章: オーバーライン付き
* `-` セクション
* `^` サブセクション
* `"` パラグラフ


## 参考
[仕様書](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html)
[sphinx reStructuredText入門](http://docs.sphinx-users.jp/rest.html)
[Sphinx Advent Calendar](http://advent-calendar2012.usaturn.net/index.html)

