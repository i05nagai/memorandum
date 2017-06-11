---
title: Vector space model
---

## Vector Space model
text documentをvectorとして扱う手法。
類似度はcosine類似度ではかるのが一般的。

* $$M$$,
    * documentの総数
* $$t$$,
    * 全documentの単語の総数
* $$d_{j} := (w_{1, j}, \ldots, w_{t, j})$$,
    * document $j$の単語の列
    * 単語がdocument $j$に含まれていれば$$w_{k, j}$$は非ゼロになる
* $$q = $$,
    * $q$は類似度を測りたいドキュメントないし、検索ワード

この類似度を以下で計測する。

$$
    s(d_{j}, q)
    :=
    \frac{
        <d_{j}, q>
    }{
        \|d_{j} \|
        \|q \|
    }
$$

## Reference
* [Vector space model - Wikipedia](https://en.wikipedia.org/wiki/Vector_space_model)
