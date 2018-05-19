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
[link1](http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c)

anaconda

* 仮想環境構築

```
conda create -n py2 python=2.7 numpy scipy pandas jupyter
#anacondaとしてまとめて入れることも可能。
conda create -n anaconda2 python=2.7 anaconda
```

* 仮想環境確認

```
conda env list
# こちらでも出る。
conda info -e
```

* 仮想環境の出入り

```
# 仮想環境に入る
source activate py2
# windowsではactivate py2
# 仮想環境から抜ける
source deactivate
# windowsではdeactivate
```

* 仮想環境の削除

```
conda remove -n py2 --all
```

## setup.py
* [Python/setup.pyによるインストール - Glamenv-Septzen.net](http://www.glamenv-septzen.net/view/373#idbc17a7)


### パッケージ管理
* パッケージのインストール&アンインストール
```
conda install numpy scipy # pipと同じでスペース区切りで複数OK
conda install numpy=1.10.4 # バージョン指定も可能
conda install -n py2 numpy scipy # -nで環境名を指定もできる

conda update numpy # update

pip install numpy # pipも使える。condaにないときはこちらを利用
source activate py2;pip install numpy # 仮想環境に入れるときは、activateしなければいけない

conda uninstall -n py2 numpy # アンインストール
```

* パッケージの確認

```
conda list
# 現在入っているパッケージリスト

conda list -n py2
# -nで仮想環境下も選択可能

conda list --export > env.txt
conda create -n py2_copy --file env.txt
# エクスポートして再利用することも可能だが、
# pipで入れたパッケージはエクスポートできないのでpip freezeで別途出力しておく必要がある。
```

## pyenv
pythonの仮想環境作成する。
`python`コマンドのversionは変わらない。
`python`コマンドのversionを変更する場合は、`pyenv-virtualenv`をいれる。

```shell
brew install pyenv
```

`bash_profile`などに以下を追加する。

```shell
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
export PYENV_ROOT=/usr/local/var/pyenv
```

### for Linux
Linuxの場合は、

```
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
```

### pyenvに特定のversionのpythonをInstall

以下のコマンドでインストール可能なpythonのversionが表示される。

```shell
pyenv install -l
```

例えば、2.7.9のpythonをインストールしたければ以下のようにかく。

```shell
pyenv install 2.7.9
```

### 全体で利用するバージョンの設定
`3.5.2`は、installされているpythonを指定する。
pyenvのpythonのversionが設定される。

```
pyenv global 3.5.2
```

### 特定のディレクトリ以下のversionの指定

`3.5.2`は、installされているpythonを指定する。
カレントディレクト以下で利用するpyenvのpythonのversionが設定される。

```
pyenv local 3.5.2
pyenv version
# 3.5.2
cd ..
pyenv version
# other version
```

## pyenv-virtualenv
以下を実行すると、`pyenv virtualenv`系のコマンドが使えるようになる。

```shell
brew install pyenv-virtualenv
```

`bash_profile`に以下を追加する。

```shell
## pyenv
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

```

### 環境作成

以下で現在pyenvに設定されているpython環境が`env_name`という名前で作成される。

```shell
pyenv virtualenv env_name
```

### 環境をactiveにする

以下で、作成した`env_name`に入ることができる。

```shell
pyenv activate env_name
```

### 環境をdeactiveにする

```shell
pyenv deactivate
```

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

###  creating directory
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

## Reference
* [6.2 Assert 文 (assert statement)](http://docs.python.jp/2.4/ref/assert.html)
