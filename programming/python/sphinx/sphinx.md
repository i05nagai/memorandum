---
title: Sphinx
---

## Sphinx
Pip is recommended way to install Sphinx.
You can install Sphinx via apt or brew, but those are prepared for dependency of other packages.

## Tutorial
1. githubに新しくrepositoryで`repository_docs`という名前でrepositoryを作っておく。
1. `sphinx`を使用するので、`pip`でいれる。

```
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

## Tutorial2
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

## Theme
* sphinx_rtd_doc

## autosummary

```
.. currentmodule:: sphinx

.. autosummary::

   environment.BuildEnvironment
      util.relative_uri
```


```rest
.. autosummary::
   :toctree: DIRNAME

   sphinx.environment.BuildEnvironment
   sphinx.util.relative_uri
```

### sphinx-autogen autodocのスタブページを作成
スタブページとは、autosmmaryされている関数用のページを指す。
`autosammary`のリンク先を自動で作成することができる。


以下のコマンドでカレントディレクトリの`*.rst`ファイルを走査し、中に定義されている`autosammary`テーブルを読み込む。

```
$ sphinx-autogen -o generated *.rst
```

`autosummary`の各要素に対応するファイルを`generated`ディレクトリに出力する。
デフォルトでは以下のような`rst`ファイルが作成される。

```
sphinx.util.relative_uri
========================

.. autofunction:: sphinx.util.relative_uri
```

### Reference
* [sphinx.ext.autosummary – autodocのサマリーの生成 — Sphinx 1.4.4 ドキュメント](http://docs.sphinx-users.jp/ext/autosummary.html?highlight=autosummary#directive-autosummary)


## autodoc
Sphinxは汎用的なdocument builderだが、重要な機能としてソースコードのコメントからAPI documentを生成する機能がある。
同様のツールとして有名なのは、`doxygen`である。
doxygenより良いところは、

* modernなのでthemeが豊富
	* doxygenの生成するhtmlはweb2.0以前のもの
	* 一応Twitter bootstrapを利用したthemeもあるが、defaultのthemeとの二者択一
* restructredTextでかける
	* markdownもかけるが、構造化されたドキュメントはmarkdownよりrestructredTextやAsciiDocが良い

注意が必要な点として

* doxygenはソースコードにドキュメント用のコメントを記載していれば自動生成される

### Supported languages
対応している言語は以下？

* C
* C++
* JavaScript

* [Sphinxドメイン — Sphinx 1.4.9 ドキュメント](http://www.sphinx-doc.org/ja/stable/domains.html)


### python
pythonのソースコード内ドキュメントの作り方。
ディレクトリ構成が以下だとする。

```
project_root
├── benchmarks
├── docs
├── examples
└── project
```

* documentのソースファイルと`Makefile`を分ける
* document作成用のrootは`docs`

#### sphinx-apidoc
sphinx-apidocコマンドには、documentのソース・ファイルと`Makefile`などを別のディレクトリに分けるコマンドは用意されていない？
プロジェクトに存在するdocstringを解析して、デフォルトのsourceファイルを作成してくれるので、多少便利。

```python
cd project_root
sphinx-apidoc --full -o temp --separate project
```

* `--separate`は、moduleごとにsourceファイルを分ける
* `--full`は、`sphinx-quickstart`にもとづいてプロジェクト全体のドキュメントを作成する。
* `-o`は出力ディレクトリ
* `project`はドキュメントを作成するプロジェクトのpathを指定

#### sphinx-quickstart
`sphinx-quickstart`コマンドでは、対話形式で必要な変数を入力し、sphinxが自動で設定ファイルなどを作成してくれる。
基本的には、こちらを使えば良い。

```
sphinx-quickstart \
  --ext-autodoc \
  --ext-doctest \
  --ext-todo \
  --ext-coverage \
  --ext-mathjax \
  --ext-viewcode \
  --extentions sphinx.ext.autosummary \
    [projectdir]
```

projectdirはdocsを生成したい場所を指定。

```
	% cd project_root
	% sphinx-quickstart
	Welcome to the Sphinx 1.4.8 quickstart utility.

	Please enter values for the following settings (just press Enter to
	accept a default value, if one is given in brackets).

	Enter the root path for documentation.
	> Root path for the documentation [.]: docs

	You have two options for placing the build directory for Sphinx output.
	Either, you use a directory "_build" within the root path, or you separate
	"source" and "build" directories within the root path.
	> Separate source and build directories (y/n) [n]: y

	Inside the root directory, two more directories will be created; "_templates"
	for custom HTML templates and "_static" for custom stylesheets and other static
	files. You can enter another prefix (such as ".") to replace the underscore.
	> Name prefix for templates and static dir [_]:

	The project name will occur in several places in the built documentation.
	> Project name: mafipy
	> Author name(s): i05nagai

	Sphinx has the notion of a "version" and a "release" for the
	software. Each version can have multiple releases. For example, for
	Python the version is something like 2.5 or 3.0, while the release is
	something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
	just set both to the same value.
	> Project version: 0.0.1
	> Project release [0.0.1]:

	If the documents are to be written in a language other than English,
	you can select a language here by its language code. Sphinx will then
	translate text that it generates into that language.

	For a list of supported codes, see
	http://sphinx-doc.org/config.html#confval-language.
	> Project language [en]:

	The file name suffix for source files. Commonly, this is either ".txt"
	or ".rst".  Only files with this suffix are considered documents.
	> Source file suffix [.rst]:

	One document is special in that it is considered the top node of the
	"contents tree", that is, it is the root of the hierarchical structure
	of the documents. Normally, this is "index", but if your "index"
	document is a custom template, you can also set this to another filename.
	> Name of your master document (without suffix) [index]:

	Sphinx can also add configuration for epub output:
	> Do you want to use the epub builder (y/n) [n]: n

	Please indicate if you want to use one of the following Sphinx extensions:
	> autodoc: automatically insert docstrings from modules (y/n) [n]: y
	> doctest: automatically test code snippets in doctest blocks (y/n) [n]: n
	> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: n
	> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
	> coverage: checks for documentation coverage (y/n) [n]: y
	> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
	> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
	> ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
	> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
	> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n

	A Makefile and a Windows command file can be generated for you so that you
	only have to run e.g. `make html' instead of invoking sphinx-build
	directly.
	> Create Makefile? (y/n) [y]: y
	> Create Windows command file? (y/n) [y]: y

	Creating file docs/source/conf.py.
	Creating file docs/source/index.rst.
	Creating file docs/Makefile.
	Creating file docs/make.bat.

	Finished: An initial directory structure has been created.

	You should now populate your master file docs/source/index.rst and create other documentation
	source files. Use the Makefile to build the docs, like so:
	   make builder
	where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

* sourceファイルと`Makefile`を分ける場合は、`sphinx-quickstart`を使う必要がある。

## sphinx-build
```
sphinx-build [options] <sourcedir> <outdir> [filenames ...]
```

* `<sourcedir>/conf.py`を作成してbuildする
    

## Tips

### Add  custom CSS or Javascript
* [Adding Custom CSS or JavaScript to a Sphinx Project — Read the Docs 2\.7 documentation](https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html)

```python
# in conf.py
def setup(app):
    # file is placed in _static/css/custom.css
    # file is placed in _static/js/custom.js
    app.add_stylesheet('css/custom.css')
    app.add_javascript('js/custom.js')
```

## Reference
* [Sphinx でPythonのAPIドキュメントを自動作成 - Qiita](http://qiita.com/some-nyan/items/1980198a05c12d90e5c3) 
* [Sphinxドメイン — Sphinx 1.4.4 ドキュメント](http://docs.sphinx-users.jp/domains.html#directive-py:function)
    * autodocの書き方など
