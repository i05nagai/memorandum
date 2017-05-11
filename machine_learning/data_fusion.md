---
title: Data Fusion
---

## Data Fusion

* Voting
* Web-link
* IR-based?
* Bayesian method
    * Bayesian networks
    * Graphical model
* Relation based
    * 
* Matrix Factorization

Data fusionの3つの分類

* Early (or full) integration
* Late (decision) integration
* Intermediate (partial) integration


### Type1
* 行列分解
* Clustering

### Type2
* 完全データ
    * 共通の変数の値は既知
    * 一部のデータは全ての変数の値が既知
    * Clustering
        * 値が分かっているデータへの近さを求めて、最も近いデータの変数の値で全て置き換える
        * 未知変数が多次元ある場合は、未知変数感の構造や制約を考慮しなくて良い
        * K-近傍法
        * Kernel SVM
    * 
* 部分データ

### Type3
* Matrix Factorization

## Reference
1. Žitnik, M., & Zupan, B. (2015). Data fusion by matrix factorization. IEEE Transactions on Pattern Analysis and Machine Intelligence, 37(1), 41–53. https://doi.org/10.1109/TPAMI.2014.2343973
2. [Tokyor26 data fusion](https://www.slideshare.net/yokkuns/tokyor26-data-fusion)
1. [data fusion についてのメモ - 盆栽日記](http://d.hatena.ne.jp/dichika/20110907/1315359207)


