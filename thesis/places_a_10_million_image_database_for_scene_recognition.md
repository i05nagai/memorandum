---
title: Places A 10 million Image Database for Scene Recognition
---

## Places A 10 million Image Database for Scene Recognition

* 2012年のPlaces dataseの改良版のdataset
* Scene recognitionに対する10 millionのdatasetを作成した
* object detectionで使われているgooglenet, VGG16, alexnetなどの手法を今回のdatasetで学習させて、testを行った

datsetは以下のTerms of useの下公開されている。

* [Places2: A Large-Scale Database for Scene Understanding](http://places2.csail.mit.edu/download.html)

```
Terms of use: by downloading the image data you agree to the following terms:

You will use the data only for non-commercial research and educational purposes.
You will NOT distribute the above images.
Massachusetts Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
You accept full responsibility for your use of the data and shall defend and indemnify Massachusetts Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.
```

またこのdatasetのweb demoが下記で公開されている。

* [Places2: A Large-Scale Database for Scene Understanding](http://places2.csail.mit.edu/demo.html)


## 1. Introduction

## 1.1 The rise of multi-million datasets
Supervised learningで重要なこと

* algorithmが問題に適していること
* training dataが問題の答えを適当に網羅しており、十分なdata量があること
    * 画像のclass分類の場合は、各classごとに十分な種類の画像があり、画像数が多いこと

適当なdatasetはsupervised learningにおいて重要である。
本論文のdatasetはscene recognitionのdatasetに焦点をあてて作られている。

## 1.2 Scene-centric Datasets
既存のscene recognitionのdatasetsについて簡単に述べる。
Deep learningによるobject detectionで使われるImageNetのような大規模datasetに相当するものは、scene recognitionにおいてはない。

Scene recognitionに関連したdatasetとして有名なものは以下

* Scene15 database
    * 15 scene categories
    * 1 scene あたり数百枚
* MIT indoor67 database
    * 67 indoor categories
* SUN (Scene UNderstanding) database
    * 397 categoreis
    * 130, 519 images

scene recognitionに限らない画像のdatasetとして有名なものは以下

* Pascal VOC dataset
    * segmentationとobject detection用の情報が付与されたdataset
* COCO dataset
    * object instance
    * 写真中のobjectにbounding boxや多面体による座標情報が付与されている
* Visual Genome dataset
    * objectとその属性とobjectの間の関係などの情報が付与されている
* ADE20K
    * scene, object, objectの部分などに対する情報が付与されている

## 2 Places Database
本研究で作成したdatasetとその前身となるPlaces datasetについて述べる。

## 2.1 Coverage of the categorical space
まず、scene categoryの作成方法について述べる。
Places datasetでは、SUN datasetを参考にscene categoryを作成しており、Places datasetでは人間が訪れることができる場所に限定して、scene categoryを作成している。

SUN datasetは最初にscene categoryを表現するwordについてまとめたdatasetで、 SUN datasetでは以下のようにしてscene categoryを作成している。

* WordNetという単語のdatasetを利用してscene, 場所, 環境を表現する70,000 wordを選んだ
    * 具体的には`I am in a 'place'`, `let's go to the/a 'place'`などのphraseに利用できる単語を選んでいる
* synonymで表現されているclassたり、同じ語だが異なる画像を持つclassを分け(churchesをinside churchesとoutside churchesに分けるなど)、900 の異なるschene categoryを作成した

Places datasetではSUN datasetのscene categoryを踏襲し、幾つかの変更を加えて利用している
変更については、2.2で述べる。

## 2.2. Construction of the database
Places datasetの作り方について述べる。
Places databsaeは4つのstepを通して、作成された。

* Step1. scene categoryのimageをscene categoryを検索語としてinternetからDLする
    * このとき、DLしたimageにscene categoryのlabelをつける
* Step2. DLしたimageがscene categoryの画像かどうかを判定して、正しければscene categoryの画像として分類する
* Step3. classifierを利用して、Step2で分類できなかった画像をscene categoryごとに分類しなおし、labelをつける
    * step1でDLした画像が他のscene categoryに属している場合がある
* Step4. scene categoryの中で、似ているscene categoryを統合したり、境界が曖昧なscene categoryをまとめる

他の画像系のimage setの作成方法としては、 ImageNetの場合

* ImageNetのcategoryは、Wordnetにもとづいて作成されている
* WordNetのsynonimを利用していくつかのsearch engineで候補の画像を取得
* AMTでcategoryに属すか属さないかの分類を行って判定している
* Quality controlのために、複数のuserに同じ画像を判定させている
* 500-1200 のgrouop-truth imageがsynonymごとに得られている

COCO datasetの場合は

* 画像内のobject instanceに焦点をあててannotationを行っている
* iconっぽい画像を減らすために、画像の候補はFlickrから取得してる
* COCOのannotationのprocessは以下に分けてAMTで行われた
    * objectにcategory lableをづける
    * object instanceの場所の指定
    * instanceのsegmentaiton
* COCOでは80 objectのcategoryと 2 million のobject instanceのdataがある

Placesでのdatasetの各stepについて詳しく述べる。

### 2.2.1 Step1: Downloading images using scene category and attributes
Places datasetは以下の方法で、画像の収集を行った。

* google images, bing images, flickrを利用して、画像を集める
    * query wordはSUN datasetのscene categoryを利用する
    * 見た目のdiversityのために、それぞれのsceneで696のcommon English adjective(messy, spaare, sunny, desolateなど)を使って検索した画像を利用する
* 少なくとも200x200のsizeのcolor画像を60 million収集し、URLでidをつける
* SUN datasetと異なるように、PCAで画像の類似度を調べ、SUN datasetと同じものを取り除いている

<div style="text-align: center">
    <img src="image/places_a_10_million_image_database_for_scene_recognition_figure01.png">
    <br>
    Figure1. adjectiveごとの画像の例
</div>

### 2.2.2 Step2: Labeling images with ground truth category
step1で収集した画像をAmazon Mechanical Turc(AMT)にcloud sourcingする。
このstepでAMTのworkerで、分類可能なものを判別する。

* scene category (e.g. cliff)に属するimageであれば、YES、属さなければNOをつけてもらう
    * scene categoryはstep1のquery wordを利用する

<div style="text-align: center">
    <img src="image/places_a_10_million_image_database_for_scene_recognition_figure03.png">
    <br>
    Figure3.  画像の例
</div>


<div style="text-align: center">
    <img src="image/places_a_10_million_image_database_for_scene_recognition_figure04.png">
    <br>
    Figure4. AMTの画面の例
</div>

AMTによる画像のscene categoryの判別は、2度に分けて行われる。

* 1回目のAMT
    * SUN datasetの収集時の知見から、onlineで集めた画像の50%はcategoryに適した画像ではないため、AMTの画面はdefaultでNOにする
    * AMTのworkerは、画像がcategoryに属さなければspace keyで次の画像のcheckに進む
        * 赤の囲み線がNO
    * 画像がcategoryに属せば、特定のkeyをおしてYESをsetして次の画像のcheckに進む
        * 緑の囲み線がYES
    * AMTの各workerはこれを750 imagesに対して行う
    * quality controlの指標として、各workerのtaskの画像の中に、SUN datasetからYESの画像とNOの画像を30枚ずつ加えておく
        * workerのtaskはこのquality controlの画像が90%の精度で分類できている場合のみ利用する
* 2回目のAMT
    * 1度目でYESと回答された画像のみ集め、もう一度同様にAMTのworkerにtaskとして依頼する
    * このとき、defaultの回答はYESにする
    * このtaskで25.4%の画像がNOと回答された

3度目のAMTではNOと回答されるimageの数が有意な数に満たなかったので、判別には用いていない。

上記の2度のclearningで、7,076,580 の画像と476 scene categoryが得られた。
その中で、413 scene categoryは、少なくとも1,000あり、98 sceneについては20,000以上ある。

### 2.2.3 Step3: scaling up the dataset using a classifier
Spte2では、scene categoryを検索後として集めた画像がscene categoryに属するものかどうかを判別した。
Step3では、 classifierによって、NOと判別された53 millionの画像を再度476 scene categoryのいずれかに分け直すという作業を行う。
例えば、living-roomのqueryでbedroomの画像がDLされた場合は、living-roomかどうかという問に対してworkerはNOという回答をしている場合がある。
この画像については、bedroomというscene categoryを付与すれば、正しい分類になる可能性がある。
このように画像にscene categoryをつけなおし、再度AMTで判別を行う。

ここでは、AlexNetを使って53 millionの画像を再度分類する。
classifierの作成と分類は以下の方法で行う。

* それぞれのscene categoryから1000の画像をrandomに選び、traning setとする
* 同様にscene categoryから50の画像をrandomに選び、validation setとする
* AlexNetでは32%の精度でvalidation setの分類ができた
* この学習済みのAlexNetで、53 millionの画像について、各classに属するか否かを判定する[0, 1]のscoreを出力する
* Step2で画像が少なかったcategoryに対して、scoreが0.8以上の画像を集め、step2と同様の手順でAMTでの分類を行う

最終的に、401のcategoryが5,000 imagesをもち、240 scene categoryが20,000以上の画像をもった。
このstepで3 millionの画像が新たに追加された。

### 2.2.4 Step 4: Improving the separation of similar classes
SUN datasetはWordNetを用いてsynonymをまとめていたが、依然として幾つかの似たようなcategory名が存在した。
例えば、`ski lodge`と`ski resort`や`garbage dump`と`landfill`などである。
これらを手で、46のsynonymのpairにまとめて、1つのcategoryに統合した。

更に、いくつかのscene categoryは境界が曖昧なものがあることを発見した。

<div style="text-align: center">
    <img src="image/places_a_10_million_image_database_for_scene_recognition_figure05.png">
    <br>
    Figure5. 境界が曖昧なscene category
</div>

これらのcategoryでは、`Does image belongs to A?`などの一方に属する設問には回答しづらく、 `Does image I belongs to class A or B?`のような設問であれば回答しやすくなる。
Step3までのannotationの結果をみて、幾つかのscene categoryのpairでworkerが上記のような混乱していることが判明した。
例えば、`canyon`と`mountain`, `butte`と`mountain`などである。
また、`jacuzzi`と`swimming pool indoor`, `pond`と`lake`, `volcano`と`mountain`, `runway`と`highway`と`road`, `operating room`と`hospital room`などである。
53の曖昧なcategoryを区別し、新しいAMTのinterfaceで再度workerに分類を依頼した。

<div style="text-align: center">
    <img src="image/places_a_10_million_image_database_for_scene_recognition_figure06.png">
    <br>
    Figure6. 境界が曖昧な画像に対するAMTの画面の例
</div>

最終的に、10,624,928 imagesと434のplaces categoryを得た。


## 3. Places Benchmarks
Places datasetを利用したbenchmarkについて述べる。
algorithmの検証用にPlaces datasetのsubsetとして幾つかのdatasetが提供されている。

* Places365-Standard
    * 365 category
    * 各category 3068から5000までの画像
    * 1,803,460 training set
    * validation setは各class 50 images
    * test setは各class 900 image
    * この論文の実験は全てこのdatasetで行われている
* Places365-Challenge
    * 365 categoryでPlaces365-Standardと同じcategory
    * 8 million training set
    * validation setは各class 50 images
    * test setは各class 900 image
    * この論文の実験は全てこのdatasetで行われている
* Places205
    * Places 1 datasetのsubset
    * 205 scene category
    * 2.5 million
    * 各categoryについて、5,000から15000
    * 2,448,873のtraning set
    * validation setは各category 100 images
    * test setは各category 200 image
* Places88
    * 88 common scene category
        * ImageNet, SUN, Places 205で共通
    * Places 1のround 2までの画像で構成されている
    * このdatasetは異なるdataset間でのperformanceの計測に使われる
    * categoryは共通だが、dataset間で同じ画像は含んでいない
* ImageNet88
    * 88 common scene category
        * ImageNet, SUN, Places 205で共通
    * このdatasetは異なるdataset間でのperformanceの計測に使われる
* SUN88
    * 88 common scene category
        * ImageNet, SUN, Places 205で共通
    * このdatasetは異なるdataset間でのperformanceの計測に使われる

## 4 Comparing Scene-Cenetric Datasets
Places88/ImageNet88/SUN88 benchmarkを用いてdataset間の比較を行う。
Places88が最も多くのdataをもつdatasetである。
次節でdatasetのdiversityについての比較を行う。

## 4.1 Dataset Diversity
image dataset間の比較はopen problemである。
image dataset間の比較において重要なのは、以下の2つである。

* dataのdense
    * dataの集中度
* dataのdiversity
    * dataが見た目と視点の多様性

diversityを測るために、biologyでecosystem間の比較に利用されるSimpson index for diversityを応用する。
simpson index for diversityは、ecosystem間で異なる種がどの程度分布しているかを調べる指標として利用される手法である。

次のideaに基いて、simpson index for diversityを拡張する。
画像の集合$A$が集合$B$よりdiverseであるとは、$B$からrandomに選んだ2つの画像の類似度より、$A$からrandomに選んだ２つの画像の類似度の方が小さい。
$B$に対する$A$の類似度は

$$
\begin{equation}
    \mathrm{Div}_{B}(A)
    :=
    1
    -
    P(d(A_{1}, A_{2}) < d(B_{1}, B_{2}))
\end{equation}
$$

ここで、$$A_{1}, A_{2}$$は$A$からrandomに選んだ画像で、$$B_{1}, B_{2}$$は$B$からrandomに彫らんだ画像である。
式は、$d$は画像間の非類似度を与え、$$d(A_{1}, A_{2})$$は$$A_{1}, A_{2}$$の非類似度である。

$$
    \mathrm{Div}_{A_{2}, \ldots, A_{N}}(A_{1})
    :=
    1
    -
    P(d(A_{1, 1}, A_{1, 2}) < \min_{i=1, \ldots, N}d(A_{i, 1}, A_{i,2}))
$$

$$A_{i,1}, A_{i, 2}$$は$$A_{i}$$からrandomに取得した画像。

この指標を用いて、SUN88, ImageNet88, Places88のdiversityをAMTを用いて行う。
ここで、AMTのworkerは式中のdiversityを測る$d$の役割を担う。

* 各datasetの各categoryから画像のpairを2つrandomに選ぶ
    * 一様分布
* 各datasetから4 pairを選ぶ

playgournd, veranda, waiting roomの3つのcategoryで比較した結果がFigure 8となる。

<div style="text-align: center">
    <img src="image/places_a_10_million_image_database_for_scene_recognition_figure08.png">
    <br>
    Figure8.
</div>

## 5 Convolutional Neural Networks For Scene Classification
* 手法
    * CNN
    * AlexNet
    * GoogLeNet
    * VGG16
    * ResNet
* dataset
    * Places205
    * Places365-Standard

で比較した結果を示す。
計算環境は

* framework
    * Caffe
* Nvidia GPUs Tesla K40
* Nvidia GPUs Titan X


精度は1つだけ予測した場合と上位5つを予測結果とした場合の精度を示している。

<div style="text-align: center">
    Table 2
    <br>
    <img src="image/places_a_10_million_image_database_for_scene_recognition_table02.png">
</div>

<div style="text-align: center">
    <img src="image/places_a_10_million_image_database_for_scene_recognition_figure10.png">
    <br>
    Figure 10.
</div>

## 5.2 Web-demo for Scene Recognition
Places-CNNのWeb demoが公開されている。
demo中のheatmapはCAM techniqueで生成している。

* http://places.csail.mit.edu/demo.html
    * Places205-AlexNet
* http://places2.csail.mit.edu/demo.html

## Reference
* Zhou, B., Lapedriza, A., Khosla, A., Oliva, A., & Torralba, A. (2017). Places: A 10 million Image Database for Scene Recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence, 8828(c), 1–14. https://doi.org/10.1109/TPAMI.2017.2723009
