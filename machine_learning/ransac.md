---
title: Random Sample Consensus (RANSAC)
---

## Random Sample Consensus (RANSAC)
RANdom SAmple ConsensでRANSAC.
以下をパラメータとする。

* $M \in \mathbb{N}$
    * 最初に選ぶ訓練データの数
* $\epsilon > 0$
    * 許容誤差
* $L \in \mathbb{N}$
    * 予測誤差が許容誤差を超えなかったdataの数
* $K \in \mathbb{N}$
    * iterationの上限

1. データからランダムに$M$個選び、選んだ$M$個を訓練データ、$N-M$個をテストデータとする
2. 1の訓練データにmodelをfitさせる
3. 1のテストデータに対して2のモデルで予測する
4. 予測誤差が$\epsilon$以下のtest dataの数が$L$以下であれば終了
5. $L$超過であれば、予測誤差が$\epsilon$を下回っているものを訓練データに加え、$K-1$回まで2-5を繰り返す


## Reference
* [Random sample consensus - Wikipedia](https://en.wikipedia.org/wiki/Random_sample_consensus)
* [ファジィシステムシンポジウム講演論文集原稿作成要領①](https://www.jstage.jst.go.jp/article/fss/28/0/28_991/_pdf)
