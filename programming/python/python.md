
<!-- vim-markdown-toc GFM -->

* [python](#python)
	* [setup](#setup)
		* [reference](#reference)
	* [doc](#doc)
		* [Sphinx](#sphinx)
	* [reference](#reference-1)
	* [環境構築](#環境構築)
		* [windows](#windows)
	* [anaconda](#anaconda)
		* [仮想環境](#仮想環境)
		* [パッケージ管理](#管理)
	* [pyenv](#pyenv)
		* [全体で利用するバージョンの設定](#全体利用設定)
		* [特定のディレクトリ以下のversionの指定](#特定以下version指定)
	* [pyenv-virtualenv](#pyenv-virtualenv)
		* [環境作成](#環境作成)
		* [環境をactiveにする](#環境active)
		* [環境をdeactiveにする](#環境deactive)
	* [unit testing framework](#unit-testing-framework)
		* [nose](#nose)
		* [reference](#reference-2)
	* [Tips](#tips)
		* [assert](#assert)
			* [Reference](#reference-3)

<!-- vim-markdown-toc -->


## python

## set up repository

* pytest
* travis CI
* codeclimate / coverall
* docs(sphinx)
* benchmark(asv)

### pytest

### travis CI

### codeclimate

### docs(sphinx)
1. githubに新しくrepositoryで`repository_docs`という名前でrepositoryを作っておく。
1. `sphinx`を使用するので、`pip`でいれる。

```shell
pip install sphinx
```

1. `hoge`にディレクトリ`docs`を作成し、sphinxの雛形を作成する。

```shell
# rootに移動
cd repository
# docsを作る
mkdir docs
cd docs
# sphinxの雛形生成
sphinx-quickstart
```

1. custom themeでRead the Docsをpipでいれる。

```shell
pip install sphinx_rtd_theme
```

1. ついでに`docs/requirements.txt`を作成し、以下を記載する。

```
sphinx=1.49
sphinx_rtd_theme==0.19
```

1. custom themeを使用するため`docs/sources/conf.py`に以下を挿入する

```python
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

1. `docs/build`以下はsphinxが生成したhtmlが格納される。こちらは別repositoryのgith pagesでhostingするので、最初に作成したgithubのrepositoryに一旦pushしておく。

```shell
cd docs/build
git init
# initial commit
git commit --allow-empty -m "Initial commit"
git remote add origin https://github.com/i05nagai/mafipy_docs.git
git push origin master
```

1. `hoge_docs`にgithub pagesのhosting用の設定とREADMEなどの設定をする
    * githubのsettingsを開く
        * Gihub Pagesの項目へ移動
        * SourceでNoneからmaster branchに変更する
    * `.nojekyll`を`repository_docs`のtopにおく
       * [Sphinx でドキュメントを作成して GitHub Pages で公開するまで - Qiita](http://qiita.com/key-amb/items/4f799fed51734987f3c5) 
       * GitHub Pages で使われている Jekyll の仕様で _static/ 配下の画像やCSSが読み込まれない

```shell
cd hoge/build
touch README.md
touch .nojekyll
git add README.md
git add .nojekyll
git add html
git add doctree
git commit -m "Set up for hosting by github pages"
git push origin master
```

1. 最後に`docs/build`を`hoge`のgit submoduleとして追加する。

```shell
cd hoge
git submodule add https://github.com/i05nagai/mafipy_docs.git docs/build
git commit -m "Add docs as git submodule"
```

### benchmark(asv)

* `results`と`html`はsubmodule管理するので、出力ディレクトリを変更する
    * `env`も統一感の為同じ位置にかえる
* resultsとhtmlはsubmodule化する
    * resultsが増えすぎる場合は


```
pip install asv
pip install virtualenv
```

```
mkdir benchmarks
cd benchmarks
asv quickstart
```

`asv quickstart`で`asv.conf.json`が生成される。
依存するライブラリなどは、`asv.conf.json`の`matrix`に記載する。
benchamrkの実行は以下でできる。

```
asv run
```

実行結果から、htmlを作成する。

```
asv publish
```

localにhtmlサーバをたてし、htmlをpreviewする。

```
asv preview
```

```
cd bechmarks/html
git init
git commit --alow-empty -m "Initial commit"
git add .
git commit -m "Add first benchmarks"
git remote add origin https://github.com/i05nagai/mafipy_benchmarks.git
git push origin master
```

Settings -> OptionsからGithu pagesのSourceをmaster branchに変更する。
READMEを以下の形で書いておくと、Github pagesにたどり着けるので楽。

```
echo "
mafipy benchmraks
=================

mafipy benchmarks

reference
=========
* Benchmark pages

    * https://i05nagai.github.io/mafipy_benchmarks/
" > README.rst

```

## circle ci with asv

最初の`asv run`実行時にmachine情報が必要。
Circle CIにsshでログインして、`asv run`を実行すると、入力画面がでて`~/.asv-machine.json`が生成される。
この中身をコピーしておき、`asv run`の前に`~/.asv-machine.json`を配置する。


## setup

### reference
* [Python/setup.pyによるインストール - Glamenv-Septzen.net](http://www.glamenv-septzen.net/view/373#idbc17a7)

## doc

### Sphinx
directory構造が以下のとき。

```
- project # Pythonプロジェクト
   |
   |- src # APIドキュメントを自動生成したいPythonコードのディレクトリ
   |   |- __init__.pyとか
   |   |- hoge # サブモジュールとか
   |
   |- docs # Sphinxプロジェクトのディレクトリ
```

```python
cd project
sphinx-apidoc -F -o docs/ src/
```

* `-F`
	* full project
* `-o dir`
	* doucment生成用の設定ファイルの置き場所
* `sphinx-apidoc dir`
	* プロジェクトファイルのdirectory

## reference
* [Sphinx でPythonのAPIドキュメントを自動作成 - Qiita](http://qiita.com/some-nyan/items/1980198a05c12d90e5c3) 
* [Sphinxドメイン — Sphinx 1.4.4 ドキュメント](http://docs.sphinx-users.jp/domains.html#directive-py:function)
    * autodocの書き方など


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

## Tips

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
1. カレントディレクトリ
1. 環境変数「PYTHONPATH」に列挙したディレクトリ
1. sys.pathに含むディレクトリ

### string to date

使えるディレクティブは以下。
* [8.1. datetime — 基本的な日付型および時間型 — Python 2.7.13 ドキュメント](http://docs.python.jp/2/library/datetime.html#strftime-and-strptime-behavior)


### 
* [install - pip error while installing Python: "Ignoring ensurepip failure: pip 8.1.1 requires SSL/TLS" - Stack Overflow](https://stackoverflow.com/questions/37723236/pip-error-while-installing-python-ignoring-ensurepip-failure-pip-8-1-1-requir/37723517)

Ubuntu

```
apt-get install libssl-dev
# or
apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev
```

CetOS

```
yum install openssl-devel
# or
yum install zlib-devel bzip2-devel sqlite sqlite-devel openssl-devel
```

#### Reference
* [6.2 Assert 文 (assert statement)](http://docs.python.jp/2.4/ref/assert.html)
