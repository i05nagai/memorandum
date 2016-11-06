# python

## 環境構築
### windows
[link1](http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c)
* `choco install miniconda`は動かない。
* `choco install miniconda3`は動かない。
1.[link](http://conda.pydata.org/miniconda.html)からinstallを落とす。
2. インストーラーをぽちぽちして、パスなどは通しておく。
3. おわり。


## anaconda
下記のコピペ。
[link1](http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c)

### 仮想環境
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

## unit testing framework
nose が良さそう。

| テストツール      | 特徴                                                                                                 | カバレッジ |
|-------------------|------------------------------------------------------------------------------------------------------|------------|
| unittest          | Python標準パッケージに含まれている単体テストライブラリ                                               | ×          |
| Django + unittest | Django の manage.py ユーティリティから、unittest が便利に使うことができる                            | ×          |
| nose              | 多彩なオプションで柔軟なテストができ、カバレッジを取ることもできる。特定のクラスを継承する必要がない | ○          |
| django-nose       | Django の manage.py ユーティリティから、nose を使えるようにしたもの                                  | ○          |

### nose

```
pip install nose
pip install coverage
```

noseの命名規則

* [Finding and running tests — nose 1.3.7 documentation](http://nose.readthedocs.io/en/latest/finding_tests.html)

### reference
* [Python, Django 界隈の単体テスト事情（unittest / nose / django-nose） - akiyoko blog](http://akiyoko.hatenablog.jp/entry/2015/01/01/212712)
* [Python nose でユニットテストを書いてみた / 桃缶食べたい。](http://blog.chocolapod.net/momokan/entry/80)
