---
title: Chapter4. 分類
book_title: Introduction to Machine Learning for Natural Language Processing
book_chapter: 4
---

## 4. 分類

* 4.2節
    * ナイーブベイズ
* 4.3節
    * SVM
* 4.4節
    * kernel SVM
* 4.5節
    * 対数線形モデル
    * 分類性能非常に高い
* 4.6節
    * 入力文の素性の表現方法について
    * 統計的に素性を選択する方法について

## 4.1 準備

* classification, categorization
    * グループにわける
* class, category
    * classificationの各グループ
* classifier
    * 分類器
* rule-based method
    * ルールベース
    * 人間が規則を定めてその規則にそって分類
* supervised learning
* unsupervised learning

* $$\mathcal{C} := \{c_{1}, \ldots, c_{N_{C}} \}$$
    * クラスの集合
* $$\mathcal{D}_{X}$$
    * データのとる値、離散ないし連続

## 4.2 ナイーブベイズ分類器
* $X$
    * 確率変数
    * 説明変数をあらわす
* $C$
    * 確率変数
    * クラスをあらわす
* $N$
    * 観測されるデータの数
* $$(X^{1}, C^{1}), \ldots, (X^{N}, C^{N})$$
    * 観測されるデータの組
    * $(X, C)$のi.i.dサンプル

naive bayes はベイズの定理を使って方法である。
naive bayesでのカテゴリの予測は、条件付き確率を最大にする$c^{*}$を出力する。
$x$を与えたとき

$$
\begin{eqnarray}
    c^{*}
    & := &
        \argmax_{c}
            \frac{
                p_{C}(c) p_{X \mid C}(x \mid c)
            }{
                p_{X}(x)
            }
    \nonumber
    \\
    & = &
        \argmax_{c}
            p_{C}(c) p_{X \mid C}(x \mid c)
    \label{naive_bayes_argmax_prediction}
\end{eqnarray}
$$

を求める。

$$p_{X \mid C}(x \mid c)$$に何らかの確率分布を仮定し求める。
仮定する確率分布は色々考えられるが、この本では多変数ベルヌーイモデルと多項モデルの場合を扱う。
どちらも、離散変数を扱う場合によく用いられるモデルである。（分布が離散の分布であるため）

### 4.2.1 多変数ベルヌーイモデル


