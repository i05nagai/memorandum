---
title: Dataset ImageNet
---

## Dataset ImageNet
* 14,197,122 images
* 21841 synsets indexed.

* [ImageNet Tree View](http://image-net.org/synset?wnid=n02084071)
    * list of category and image


```
curl -O http://image-net.org/archive/words.txt
```

## Utility
* [GitHub - tzutalin/ImageNet_Utils: Utils to help download images by id, crop bounding box, label images, etc.](https://github.com/tzutalin/ImageNet_Utils)

There is a utility tools to download images.

```
git clone --recursive https://github.com/tzutalin/ImageNet_Utils.git
```

```
$ ./downloadutils.py --downloadImages --wnid n02084071
```


## API
* [ImageNet](http://image-net.org/download-API)

API for downloading data is provided.
The name of category is based on the words in WordNet 3.0, having `wnid`, word net id.
The image-net supports only noun category, so the wnid of the category starts from `n`.

`http://www.image-net.org/synset?wnid=n02084071`で対応する画像の一覧が見れる。
`n02084071`に対応するsynetは`Dog, domestic dog, Canis familiaris`である。
synetのsubcategoryとして、hyponym(下位語)が定義してある。
下位語のwnidは以下のAPIで取得できる

```
http://www.image-net.org/api/text/wordnet.structure.hyponym?wnid=n00021265&full=1
```

wnidに対応するsynetは以下で取得できる。

```
http://www.image-net.org/api/text/wordnet.synset.getwords?wnid=[wnid]
```

wnidとwordnetのsynetの対応の一覧は以下で取得できる。

```
http://image-net.org/archive/words.txt
```

wnidの一覧は以下から取得できる。

```
http://www.image-net.org/api/text/imagenet.synset.obtain_synset_list
```

wnidの間の親子関係は以下から取得できる。

```
http://www.image-net.org/archive/wordnet.is_a.txt
```

wnidに分類されている画像のURL

```
http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00021265
```


```
http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid=n00021265
```

## Image Feature

* [ImageNet](http://image-net.org/download-features)
    * SIFT feature

```
curl -O http://www.image-net.org/api/text/imagenet.synset.obtain_synset_list
```

## Object Bounding Boxes

## Reference
* [ImageNet](http://www.image-net.org/index)
