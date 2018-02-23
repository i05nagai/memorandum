---
title: mecab ipadic neologd
---

## mecab ipadic neologd

## Install

```
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
```

```
$ cd mecab-ipadic-neologd
```

```
$ ./bin/install-mecab-ipadic-neologd -n
```

* `--newest`, `-n`
* `--forceyes`, `-y`
    * testの結果にかかわらずinstall
* `--asuser`, `-u`
* `--create_user_dic`
    * user辞書としてinstall

```
$ echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
```

Usage

```
mecab --dicdir=`mecab-config --dicdir`"/mecab-ipadic-neologd"
```


## Reference
* [neologd/mecab-ipadic-neologd: Neologism dictionary based on the language resources on the Web for mecab-ipadic](https://github.com/neologd/mecab-ipadic-neologd)
