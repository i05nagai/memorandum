---
title: Locality Senstive Hashing
---

## Locality Senstive Hashing
局所性鋭敏型ハッシュともいう。
高次元のデータを確率的に次元圧縮する方法。

## Definitions
* $$(\Omega, \mathcal{F}, P)$$,
    * probability space

### Definiton. LSH Family
* $\mathcal{M} := (M, d)$
    * metris space
* $$R \in \mathbb{R}_{> 0}$$,
    * 閾値
* $$c > 1$$,
    * approximation factor
* $S$
    * 集合
* $$\mathcal{A} \subseteq \{h: M \rightarrow S\}$$,
* $$p_{1}, p_{2} \in [0, 1]$$,

$\mathcal{A}$が以下を満たす時、$\mathcal{A}$をLSH familyという。
$\forall p, q \in M$について、$h \in \mathcal{A}$を一様乱数で選んだ時、

* $d(p, q) \le R$ならば、$h(p) = h(q)$が少なくとも確率$$p_{1}$$でおこる
* $d(p, q) \ge cR$ならば、$h(p) = h(q)$が多くとも確率$$p_{1}$$でおこる

つまり、$X: \Omega \rightarrow \mathcal{A}$として、一様乱数に従う確率変数とすれば、$\forall p, q \in M$について

* $d(p, q) \le R$ならば、$$P(\{\omega \in \Omega \mid X(\omega)(p) = X(\omega)(q)\}) \ge p_{1}$$,
* $d(p, q) \ge cR$ならば、$$P(\{\omega \in \Omega \mid X(\omega)(p) = X(\omega)(q)\}) \le p_{2}$$,

である。
特に、$$p_{1} > p_{2}$$のとき、$$(R, cR, p_{1}, p_{2})$$-sensitiveなLSH familyという。

<div class="end-of-statement" style="text-align: right">■</div>

### Definition. LSH scheme
* $U$
    * set
* $S$
    * set
* $\phi: U \times U \rightarrow [0, 1]$
* $F$
    * $S$上の確率分布 
* $$\mathcal{A} \subseteq \{h: U \rightarrow S\}$$,
    * 位相空間
* $X: \Omega \rightarrow \mathcal{A}$
    * 確率変数で、$F$を分布としてもつ

以下を満たす$(\phi, \mathcal{A}, F)$をLSH schemeという。 

$$
    \forall a, b \in U,
    \
    P(\{\omega \in \Omega \mid X(\omega)(a) = X(\omega)(b)\})
    =
    \phi(a, b)
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Locality-sensitive hashing - Wikipedia](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)
* [局所性鋭敏型ハッシュ - Wikipedia](https://ja.wikipedia.org/wiki/%E5%B1%80%E6%89%80%E6%80%A7%E9%8B%AD%E6%95%8F%E5%9E%8B%E3%83%8F%E3%83%83%E3%82%B7%E3%83%A5)
* [lec9.pdf](http://sd.is.uec.ac.jp/koga/lecture/IF2/lec9.pdf)
