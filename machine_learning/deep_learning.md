---
title: Deep Learning
---

## Deep Learning

* one-hot vector
* Local Response Normalisation
* ReLu


## Layer
- Dense layer/Fully connected layer
    - neurons connect to all neurons in the preceding layer
- Convolutional layer
    - 
- Pooling layer
    - reduce the size of inputs
- Recurrent layer
    - Outputs of neurons are resued as inputs of neurons
    - There are many variants

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
* [CNN による画像分類で使われる前処理・テスト時処理まとめ - (iwi) 備忘録](http://iwiwi.hatenadiary.jp/entry/2016/12/31/162059)
    * 画像のData augumentationの手法のlsit
    * kerasのFine tuning officalのtutorial
* [37 Reasons why your Neural Network is not working – Slav](https://blog.slavv.com/37-reasons-why-your-neural-network-is-not-working-4020854bd607)
    * Deep learningで学習がうまくいかなかったときのよくある理由
* [The 9 Deep Learning Papers You Need To Know About (Understanding CNNs Part 3) – Adit Deshpande – CS Undergrad at UCLA ('19)](https://adeshpande3.github.io/adeshpande3.github.io/The-9-Deep-Learning-Papers-You-Need-To-Know-About.html)
    * Deep Learningのmodelの歴史が、各modelにどういうbreak throughがあったかが良くまとまっている
* [Torch | Training and investigating Residual Nets](http://torch.ch/blog/2016/02/04/resnets.html)
* [facebook/fb.resnet.torch: Torch implementation of ResNet from http://arxiv.org/abs/1512.03385 and training scripts](https://github.com/facebook/fb.resnet.torch)
