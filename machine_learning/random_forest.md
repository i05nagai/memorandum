---
title: Random Forests
---

## Random Forests
Random Forestsは決定木を理解していればアルゴリズム自体は単純である。

## Good

## Bad

## Definition
* $N \in \mathbb{N}$
    * 訓練データの数
* $y_{1}, \ldots, y_{N}$,
    * 目的変数の観測値
* $d$
    * 説明変数の数、変数の次元
* $x_{i}^{j}$,
    * $$i \in \{1, \dots, N\}$$番目のデータの$$j \in \{1, \ldots, d\}$$番目の説明変数
* $x_{i} := (x_{i}^{1}, \ldots, x_{i}^{d})$
    * $$i \in \{1, \dots, N\}$$番目のデータの説明変数
* $D := \{(x_{1}, y_{1}), \ldots, (x_{N}, y_{N})\}$
    * 訓練データの全体
* $M$
    * ブートストラップサンプルする数
* $n_{\mathrm{min}}$
    * 各決定木のノートの総数
    * 推奨されている値は以下の通り
    * 分類の場合は1、つまり深さ2の二分木
    * 回帰の場合は5
* $L$
    * 各決定木で選択する説明変数の数
    * 推奨されている値は以下の通り
    * 分類の場合は$\sqrt{d}$
    * 回帰の場合は$d / 3$

## Algorithms

1. 訓練データからデータをランダムにサンプルを取る。
    * $D_{1}, \ldots, D_{M} \subset D$とする。
2. 各$D_{m}$について、以下の方法で決定木を作る
3. 指定したノード数$n_{\mathrm{min}}$になるまで、繰り返し木のノードを作る
    * 説明変数から$L$個の変数をランダムに選び、決定木を作る
    * 決定木のアルゴリズムは適当に選ぶ

## Tips 
$D_{m}$に対して、決定木を作る際に、説明変数をランダムに選ばずそのまま使う方法をbaggingという。
Random Forestsはbaggingに対して、説明変数のサンプリングを行うことで、説明変数間の相関を減らしている。

## Reference
* [Random subspace method - Wikipedia](https://en.wikipedia.org/wiki/Random_subspace_method)
* [ランダムフォレスト - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E3%83%95%E3%82%A9%E3%83%AC%E3%82%B9%E3%83%88)

