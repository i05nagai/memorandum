---
title: cpplint
---

## cppplint
pythonでかかれたgoogleのC++ style guideのlint tool

## Install
pipでいれる場合は以下。

```
pip install cpplint
```

gogoleのrepositoryから本体をcopyして利用する。

* [styleguide/cpplint.py at gh-pages · google/styleguide · GitHub](https://github.com/google/styleguide/blob/gh-pages/cpplint/cpplint.py)


## Usaage

```
python cpplint.py <file>
```

* `--filter`
    * 警告の除外と追加ができる


## Reference
* [ブログズミ: cpplint でコーディングチェック](http://srz-zumix.blogspot.jp/2015/11/cpplint.html)


