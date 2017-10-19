---
title: Deep Learning
---

## Deep Learning

* one-hot vector
* Local Response Normalisation
* ReLu


## Fine tuning
* [A Comprehensive guide to Fine-tuning Deep Learning Models in Keras (Part I) | Felix Yu](https://flyyufelix.github.io/2016/10/03/fine-tuning-in-keras-part1.html)

Fine tuningの方法はいくつかあり明確な定義はない。
基本的には、最後の層から幾つかを新しく作った層といれかえて、入れ替えなかった層のparameterは学習済みのparameterを使うという点で共通している。
どこまで入れ替えるかと入れ替えた後の再学習の方法に違いある。

ImageNetでpretainしたVGG16 modelの場合の例を示す。
ImageNetの場合は、最終層は1000 categoryである。

* 1000 categoryのlast layer (softmax layer)を除き、10 categoryの新しいsoftmax layerを加える
    * backpropagationで10 categoryのtraining dataで学習する
    * learning rateは小さくする
        * よく利用される指標としてscratchのlearning rateの1/10にする
    * 最初の幾つかの層をfreezeして学習しないようにすることも良く行われる
        * 最初の幾つかのlayerは、curveやedgeなどの汎用的なものを学習しており、どのデータでも似たようなparameterになることが経験的に知られている


## Reference

