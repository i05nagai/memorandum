---
title: MeCab
---

## MeCab

install python3 version

```
pip install mecab-python3
```

```
import sys
import MeCab
m = MeCab.Tagger("-Ochasen")
print(m.parse ("今日もしないとね"))

m = m.parseToNode(text)
# 品詞
m.feature
# 形態素の文字列情報
m.surface
# 累積コスト
m.cost
```

既知のbugとして、以下のようなものがある。
空文字をparseすると治るらしい。

https://qiita.com/piruty/items/ce218090eae53b775b79

```python
d = m.parseToNode('')
# 表層形
d.surface
# 品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
d.feature
```

`/usr/local/lib/mecab/ipadic/dicrc`に出力形式が記載されている。


## Reference
* [スクリプト言語のバインディング](https://taku910.github.io/mecab/bindings.html)
* [Python3で形態素解析エンジンMeCabを使えるようにする(2016年3月版) - Qiita](https://qiita.com/grachro/items/4fbc9bf8174c5abb7bdd)

