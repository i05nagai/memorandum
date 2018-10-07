---
title: doxygen
---

## doxygen

## Install
OSX

```
brew install doxygen
```

## Usage
デフォルトの設定ファイルを作る。
以下で`Doxyfile`が作成される。

```
doxygen -g
```

doxygenを実行する。
`<config-file>`を省略するとカレントディレクトリの`Doxyfile`を利用する。

```
doxygen <config-file>
```

## CSS
[Velron/doxygen-bootstrapped: Customize doxygen output to use the twitter bootstrap framework.](https://github.com/Velron/doxygen-bootstrapped)

## config
* `USE_MATHJAX = NO`
* `MATHJAX_RELPATH = http://cdn.mathjax.org/mathjax/latest`
* `MATHJAX_EXTENSIONS =`
* `SEARCH_INCLUDES = YES`
    * INCLUDE_PATH
* `INCLUDE_PATH=`
    * 検索するincude
* `INCLUDE_FILE_PATTERNS=`
* `PROJECT_NAME = "My Project"`
* `OUTPUT_DIRECTORY=`
    * documentの出力先
    * defaultはcurrent directory
* `CREATE_SUBDIRS= NO`
    * documentの出力時にsubdirを作るか
* `RECURSIVE=NO`
    * directoryを再帰的に探索するか
* `INPUT=`
    * documentのsourceがあるdirectory, file
    * space区切りで複数記載できる
    * projectのtopを指定して、RECURSIVEにする
* `EXCLUDE=`
    * documentのsourceとして除外するdirectory, fileを指定する
    * 相対pathはdoxygenが実行されている場所から見た相対path
* `EXCLUDE_SYMLINKS=NO`
    * inputからsymlinkを無視するか
* `EXCLUDE_PATTERNS=`
    * 除外するfileをregexで指定する
    * 絶対pathから見て除外されるので、`test` directoryのfileを全て除外する場合は`*/test/*`とする
    * projectのtopの不要なdirectoryとfileを除く
* `EXCLUDE_SYMBOLS=`
    * 除外するclass名や関数名を指定
    * 
* `USE_MDFILE_AS_MAINPAGE=`
    * markdown fileをmain pageに利用する
    * projectのREADMEがある場合に便利
* `GENERATE_HTML=YES`
    * htmlを出力するか
* `HTML_OUTPUT=html`
    * 作成するhtmlの出力場所
    * 相対pathを指定した場合は、OUTPUT_DIRECTORYの値から見た相対pathになる
* `GENERATE_LATEX=YES`
    * latexを作成するか
* `LATEX_OUTPUT=latex`
    * 作成するlatexの出力場所
    * 相対pathを指定した場合は、OUTPUT_DIRECTORYの値から見た相対pathになる
* `GENERATE_RTF=NO`
    * RTFを作成するか
* `RTF_OUTPUT=rtf`
    * 作成するrtfの出力場所
    * 相対pathを指定した場合は、OUTPUT_DIRECTORYの値から見た相対pathになる
* `GENERATE_MAN=NO`
    * man fileを作成するか
* `MAN_OUTPUT=man`
    * 作成するmanの出力場所
    * 相対pathを指定した場合は、OUTPUT_DIRECTORYの値から見た相対pathになる
* `GENERATE_XML=NO`
    * xmlを作成するか
* `XML_OUTPUT=xml`
    * 作成するxmlの出力場所
    * 相対pathを指定した場合は、OUTPUT_DIRECTORYの値から見た相対pathになる

## Documentation
* [List](https://www.stack.nl/~dimitri/doxygen/manual/lists.html)
* [Doxygen Manual: Documenting the code](https://www.stack.nl/~dimitri/doxygen/manual/docblocks.html)
* [Special Commands](https://www.stack.nl/~dimitri/doxygen/manual/commands.html)
* [Doxygenチートシート \- Qiita](https://qiita.com/yuta-yoshinaga/items/84887a89f6a21a7dcfd5)

## Reference
* [Doxygen](http://www.doxygen.jp/manual.html)
