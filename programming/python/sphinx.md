# Sphinx

## Theme

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
* 