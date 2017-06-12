---
title: You Are What Apps You Use Demographic Prediction Based on User's Apps
---

## You Are What Apps You Use Demographic Prediction Based on User's Apps
pre-printなので注意。

demographicの予測。
ユーザがある期間にインストールしたアプリの一覧から、ユーザのdemographicを推定する。
著者いわく、ユーザがインストールしたアプリの一覧は簡単に、app developperが分かると言っているがそんなことある？

* age, race, incomeの予測
    * genderが一番簡単で82.3%の精度で予測できた
    * incomeが一番難しく60.3%の精度で予測できた
* training dataの数

論文の主な貢献は、先行研究に対して大きくデータ・セットを増やした所。
Related workにdemographic prediction系の論文が良くまとまっている。

## Introduction
* 先行研究では、218のuserに対して予測を行ったが、今回3760のuserに対して予測を行った

## Material
* 今回用意したデータは、3760 android user

## Methods
* 特徴量の個数は8840
* データは3740

得量量の方が多いけど大丈夫？

手法は

* 他クラス分類に対するlogistic regression
* kernel SVM
    * kernelをかえて
* random forest

試したが、logistic regressionが一番良かった。


## Reference
* Malmi, E., & Weber, I. (2016). You Are What Apps You Use: Demographic Prediction Based on User’s Apps. Retrieved from http://arxiv.org/abs/1603.00059
