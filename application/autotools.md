---
title: autotools
---

## autotools

overview

1. Makefile.amの作成
2. autoscan実行
    * configure.scan生成
3. configure.scanの修正してconfigure.acを作成
4. aclocal実行
5. automake -a実行
    *  Makefile.in生成
6. autoheader実行
    * config.h.in生成
7. autoconf実行
    * configure生成
8. ./configure実行
    * Makefile生成

## Makefile.am
ファイル名のワイルドカードは使えない。

```automake
SUBDIRS = target
```
サブディレクトリの`target`に`Makefile.am`がある場合は指定する。
再帰的に`Makefile.am`を利用していく。

```automake
bin_PROGRAMS = hello
```
実行ファイルのプログラム名を設定する。
この変数をセットすると実行ファイルが生成される。

```automake
target_SOURCES = hello.c folder/hello.c
```
`target`という名前のプロジェクトのソースファイルを指定する。
`target`の部分は一意な名前。

```automake
AUTOMAKE_OPTIONS = subdir-objects
```
automakeのオプションを指定する。
* `subdir-objects`
     * ディレクトリのオブジェクトファイルも含める。
     `Mkaefile.am`のあるディレクトリの下にディクレトリがある場合は指定する。

```automake
target_CPPFLAGS = -g
```
cppのコンパイラオプションを渡す。

```automake
test_LDADD = -lm
```
使用しているライブラリ

```automake
include_HEADERS = book.h
```
インストールするヘッダファイル

```automake
### 以下はライブラリを作成する際の設定(オプション)
# インストールするヘッダファイル
include_HEADERS = book.h
# インストールする際のライブラリ名
lib_LIBRARIES = libbook.a
# Cコンパイラへ渡すオプション(ここではコメントアウトしています)
# libbook_a_CFLAGS = -g
# C++コンパイラへ渡すオプション
libbook_a_CXXFLAGS = -g
# ライブラリ生成に必要なソースコード
libbook_a_SOURCES = book.h book.cpp
```

```automake
AM_CFLAGS = $(WARNINGCFLAGS)
bin_PROGRAMS = prog1 prog2
prog1_SOURCES = 
prog2_SOURCES = 
prog2_CFLAGS = 
prog2_LDFLAGS = 
```

## configure.ac
`Makefile.am`を作った後は、`autoscan`コマンドを使うと、雛形の`configure.scan`ができる。
`configure.scan`を`configure.ac`に変更し、修正を加える。

```autoconf
AC_PROG_RANLIB
```

```autoconf
AC_LIBTOOL_WIN32_DLL
AC_PROG_LIBTOOL
```
libtoolを使用する場合は設定する。
windwosの場合は`AC_LIBTOOL_WIN32_DLL`を前に追加しておく。
UNIXの場合は不要。

```autoconf
AC_PROG_
```

## Macros

* AM_INIT_AUTOMAKE
    * [automake: Public Macros](https://www.gnu.org/software/automake/manual/html_node/Public-Macros.html)
    * [automake: List of Automake options](https://www.gnu.org/software/automake/manual/html_node/List-of-Automake-options.html#List-of-Automake-options)
* AC_SUBST()
    * [Setting Output Variables - Autoconf](https://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/Setting-Output-Variables.html)
    * shell variableから`@variable@`の変数を作成する
* AC_ARG_VAR(variable, description)
* AS_IF(test1, [run-if-true1], test2, ..., [run-if-false])
    * [Common Shell Constructs - Autoconf](https://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/Common-Shell-Constructs.html)
    * test1を実行してexit 0なら、true1を実行,そうでなければtest2を実行を繰り返す



## 参考
[tilte](http://www.02.246.ne.jp/~torutk/cxx/automake/automake.html)
[title](http://transitive.info/2012/07/21/autotools-tutorial2-automake/)
[title](http://markuskimius.wikidot.com/programming:tut:autotools)
[title](http://qiita.com/KAGE_MIKU/items/5aed05f7bd70d8035f54)
[title](http://www.jaist.ac.jp/~kiyoshiy/memo/autoconf.html)
[autotoolsライブラリ構成サンプル](http://capm-network.com/?tag=autotools%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E6%A7%8B%E6%88%90%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB)


