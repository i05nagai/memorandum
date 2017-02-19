---
title: cmake
---

# cmake

## variables

### `CMAKE_INSTALL_PREFIX`
デフォルトだと以下の値。
* Unix
  * `/usr/local`
* Windows
  * `c:/Program Files`

### `project`
```cmake
project(<PROJECT-NAME> [LANGUAGES] [<language-name>...])
project(<PROJECT-NAME>
        [VERSION <major>[.<minor>[.<patch>[.<tweak>]]]]
                [LANGUAGES <language-name>...])
```

以下の変数がsetされる。
* `PROJECT_NAME`
* `PROJECT_SOURCE_DIR`
* `PROJECT_BINARY_DIR`
* `<PROJECT_NAME>_SOURCE_DIR`
* `<PROJECT_NAME>_BINARY_DIR`

`VERSION`が指定された場合は、`VERSION`変数に値がsetされる。
無指定の場合は`VERSION`変数は空文字。

またversion numberは以下の変数にsetされる。

* `PROJECT_VERSION`, `<PROJECT-NAME>_VERSION`
* `PROJECT_VERSION_MAJOR`, `<PROJECT-NAME>_VERSION_MAJOR`
* `PROJECT_VERSION_MINOR`, `<PROJECT-NAME>_VERSION_MINOR`
* `PROJECT_VERSION_PATCH`, `<PROJECT-NAME>_VERSION_PATCH`
* `PROJECT_VERSION_TWEAK`, `<PROJECT-NAME>_VERSION_TWEAK`

## pre compile header
[pch](http://qiita.com/mrk_21/items/264f6135679239ff018a)

## debug build
* 指定なし
    * 初期状態で CMAKE_BUILD_TYPE シンボルを書き換えないとこの状態
    * 一度でも他の値で書き換えるとずっと記憶するので、あらためて指定なしにしたい場合は -DCMAKE_BUILD_TYPE= とする
* Debug
    * CMAKE_C_FLAGS / CMAKE_CXX_FLAGS に加えて変数 CMAKE_C_FLAGS_DEBUG / CMAKE_CXX_FLAGS_DEBUG の値も使われる
* Release
    * CMAKE_C_FLAGS / CMAKE_CXX_FLAGS に加えて変数 CMAKE_C_FLAGS_RELEASE / CMAKE_CXX_FLAGS_RELEASE の値も使われる
* RelWithDebInfo
    * 最適化しつつデバッグ用情報も付加するためのモード
    * CMAKE_C_FLAGS / CMAKE_CXX_FLAGS に加えて変数 CMAKE_C_FLAGS_RELWITHDEBINFO / CMAKE_CXX_FLAGS_RELWITHDEBINFO の値も使われる
* MinSizeRel
    * 実行ファイルのサイズを一番小さくするためのモード
    * CMAKE_C_FLAGS / CMAKE_CXX_FLAGS に加えて変数 CMAKE_C_FLAGS_MINSIZEREL / CMAKE_CXX_FLAGS_MINSIZEREL の値も使われる

* [CMake 簡易まとめ - Qiita](http://qiita.com/janus_wel/items/a673793d448c72cbc95e)

## Tips

### ビルドのオプション/条件分岐
`OPTION`コマンドを使う

```cmake
OPTION(USE_FEATURE_HOGE, "Use feature hoge" ON)
# if option is on
IF(USE_FEATURE_HOGE)
    # define macro ENABLE_FEATURE_HOGE
    add_definitions(-DENABLE_FEATURE_HOGE)
ENDIF()
```

* `OPTION(variable_name, "description", initial_value)`
    * `initial_value`はデフォルト値で下記の変数設定を何もしない場合にセットされる

* cmakeのコマンドライン引数で-DUSE_FEATURE_X=ON/OFFをつける
* CMakeLists.txt中でsetコマンドを使う
* 明示的には指定しない → 初期値またはキャッシュされた値を使う

### Reference
* [CMakeを使ってみた (4) ビルドオプション - wagavulin's blog](http://blog.wagavulin.jp/entry/2011/11/27/222650)


## CXX や CXX_FLAGS などのコンパイルに関わる変数の設定を変更する方法
以下の2つ。

1. トップレベルの CMakeLists.txt に下記を追加する方法
2. cmake時にコマンドラインオプションとして指定する方法

以下はdebug buildを実行し、かつdebug用のビルドオプションを設定する方法である。

```shell
cmake \
    -D CMAKE_CXX_FLAGS_DEBUG="-Wall -g" \
    -D CMAKE_BUILD_TYPE=Debug \
    .
```

### Reference
* [cmake の使い方 - PukiWiki](http://www.cs.gunma-u.ac.jp/~nagai/wiki/index.php?cmake%20%A4%CE%BB%C8%A4%A4%CA%FD)

## reference

* [便利なコマンド](http://qiita.com/mrk_21/items/5e7ca775b463a4141a58)
* [configure_file解説](http://qiita.com/osamu0329/items/edc66e2e1b6c96947771)
* [1](http://qiita.com/termoshtt/items/539541c180dfc40a1189)
* [2](http://qiita.com/janus_wel/items/4e6c12f9104f501104c7)
* [tutorial](http://opencv.jp/cmake/cmake_tutorial.html)
