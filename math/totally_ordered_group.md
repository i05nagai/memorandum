---
title: Totally Ordered Group
---

## Totally Ordered Group
Linear Ordered Groupとも言う。
群に順序構造を付与したもので、順序関係の中で群の演算を保存する。

## Definition

### Definition. totally order
* $A$
    * set
* $R$
    * $G$上の二項関係

$R$が二項関係とは以下を満たすことを言う。

* $\forall a \in A$, $aRa$
* $\forall a, b \in A$
    * $aRb, bRa \Leftrightarrow a = b$
* $\forall a, b, c \in A$
    * $aRb, bRc \Leftrightarrow aRc$

順序関係の場合は$R$は$\le$や$\ge$が良く用いられる。

<div class="QED" style="text-align: right">■</div>

### Definition. left-ordered group
* $G$
    * group
* $\le$
    * $G$上の全順序関係

以下を満たす時、$(G, \le)$をleft ordered groupという。

$$
    \forall a, b, c \in G,
    \
    a \le b
    \Leftrightarrow
    c + a \le c + b,
$$

<div class="QED" style="text-align: right">■</div>

### Definition. right-ordered group
* $G$
    * group
* $\le$
    * $G$上の全順序関係

以下を満たす時、$(G, \le)$をright ordered groupという。

$$
    \forall a, b, c \in G,
    \
    a \le b
    \Leftrightarrow
    a + c \le b + c,
$$

<div class="QED" style="text-align: right">■</div>

### Definition. bi-ordered group
* $G$
    * group
* $\le$
    * $G$上の全順序関係

left-orderedかつright-orderedのとき、$(G, \le)$をbi-ordered groupという。

<div class="QED" style="text-align: right">■</div>

### Remark
* $G$がAbelian Groupの時は、Abelian Totally Ordered Groupともいう。
* 0を$G$の単位元とすると、$a \in G$が$0 \le a$の時$a$をpositiveという。

<div class="QED" style="text-align: right">■</div>

## Propositions


## Reference
* [Linearly ordered group - Wikipedia](https://en.wikipedia.org/wiki/Linearly_ordered_group)


