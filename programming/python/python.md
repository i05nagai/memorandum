---
title: python
---

## python
What you need to learn as pythonista

* unit test framework
    * pytest
* documentation
    * sphinx
* CI
    * Travis CI/Circle CI
    * codeclimate / coverall
* bencharmk
    * asv
* packaging
    * pip
    * setup.py
* environment management
    * pyenv, pyenv-virtualenv
    * conda

## Install

### windows
[link1](http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c)
* `choco install miniconda`は動かない。
* `choco install miniconda3`は動かない。
1.[link](http://conda.pydata.org/miniconda.html)からinstallを落とす。
2. インストーラーをぽちぽちして、パスなどは通しておく。

### 仮想環境
* [link1](http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c)

## setup.py
* [Python/setup.pyによるインストール - Glamenv-Septzen.net](http://www.glamenv-septzen.net/view/373#idbc17a7)

## Tips

### 'module' object has no attribute '_strptime' with several threads Python
* [multithreading - 'module' object has no attribute '_strptime' with several threads Python - Stack Overflow](https://stackoverflow.com/questions/32245560/module-object-has-no-attribute-strptime-with-several-threads-python)

### pretty print
* [8.18. pprint — Data pretty printer — Python 2.7.13 documentation](https://docs.python.org/2/library/pprint.html)

辞書や、listをpretty printしたい場合に利用する。


```python
import pprint
pp = pprint.PrettyPrinter(indent=4)
data_dict = {
    'hoge1': 'hohoho',
    'hoge2': 'Hohoho',
}
pp(data_dict)
```

### assert
pythonのassertは以下と等価。

```python
if __debug__:
       if not expression: raise AssertionError
```

`__debug__`は、通常は1。
pythonのinterepreterに`-O`の最適化オプションを渡すと0になる。
`-O`が渡されているときは、interepreterはコンパイル時にassertに関するコードは一切生成しない。
つまり、上記のifにあたるコードは生成されない。

### import
import下のディレクトリは、環境変数`PYTHONPATH`で指定されたディレクトリも対象になる。
正確には以下の順序でimport先のディレクトリが決定される。

1. 実行ディレクトリと同ディレクトリ
2. カレントディレクトリ
3. 環境変数「PYTHONPATH」に列挙したディレクトリ
4. sys.pathに含むディレクトリ

1. pythonコマンドで入力されたscriptのあるディレクトリ
    * 入力されなかった場合はcurrent directory
2. 環境変数PYTHONPATH
3. インストールごとのデフォルトのディレクトリ
4. sys.pathに含むディレクトリ

### string to date
使えるディレクティブは以下。
* [8.1. datetime — 基本的な日付型および時間型 — Python 2.7.13 ドキュメント](http://docs.python.jp/2/library/datetime.html#strftime-and-strptime-behavior)

### Inherits object
以下のclassのあるなしの違い。

* [2 PEPs 252 and 253: Type and Class Changes](https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html)
* [Python class inherits object - Stack Overflow](https://stackoverflow.com/questions/4015417/python-class-inherits-object)

```
class MyClass(object):
    pass

class MyClass:
    pass
```

`object`を継承する方法はpython2.2でclassの仕様が変わった際に導入された。
`object`を継承することで、(classの新しい機能が使える)新しい方式でクラスを使用することを明示する。
Python2系ではデフォルトでは古い形式なので、明示的にobjectを継承した方が良い。
Python3では継承の有無にかかわらず新しい方式での継承になるので、つけてもつけなくても良い。


### subprocess
標準入力からの入力をうけつけて、

```python
import subprcess
p = subprocess.Popen(
    ["echo", "hoge"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    stderr=subprocess.STDOUT)
result = p.communicate(input=input_str)[0]
```

### hash
pythonの2.7系はid(object) / 16を返すらしい。
idはobjectのアドレスを返す。

* [hash function in python - Stack Overflow](https://stackoverflow.com/questions/17192418/hash-function-in-python)
* [2. Built-in Functions — Python 2.7.13 documentation](https://docs.python.org/2/library/functions.html#id)

### creating directory
* [python - How can I create a directory if it does not exist? - Stack Overflow](https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist)

以下で作成可能だが、ifの判定の後にdirectoryが作られると`OSError`で落ちる。

```python
if not os.path.exists(directory):
    os.makedirs(directory)
```

以下は改良版。
directoryが存在することによるerrorは無視している。
例外を握りつぶしているのが問題。

```python
import os
import errno

try:
    os.makedirs(directory)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
```

## variable scope
* [変数のスコープ - Qiita](http://qiita.com/yoichi22/items/8ae2ca180407a5ad5a6d)

* 関数定義はscopeを作る
* for文はscopeを作らない
* python2ではlist 内包表記の変数は外へもれる
    * `[i for i in range(3)]`
* set内包表記は外へもれない
    * `{i for i in range(3)}`

下記では、ll == 1がgeneratorの最初で実行されるようにすれば、errorにならない

```python
def set_visit_id(lll):
    for ll in lll:
        if ll == 1:
            seq = 0
            print(seq)
        else:
            seq = seq + 1
            print(seq)
        yield ll


lll = [1, 0, 0, 0]
a = set_visit_id(lll)
print(a)
next(a)
next(a)
next(a)
# no error
# 0, 1, 2, 3, 4
lll = [0, 1, 0, 0]
a = set_visit_id(lll)
print(a)
next(a)
next(a)
next(a)
# error
# un initialized variable: seq
```

### built-in function
* `class slice(stop)`
* `class slice(start, stop[, step])`


#### built-in type
- [Built\-in Types — Python 3\.7\.3 documentation](https://docs.python.org/3/library/stdtypes.html#truth)
    - Following values are evaluated as False
        - None, False
        - 0, 0.0, 0j, Decimal(0), Fraction(0.0),
        - '', (), [], set(), range(0),



## Reference
* [6.2 Assert 文 (assert statement)](http://docs.python.jp/2.4/ref/assert.html)
