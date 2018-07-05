---
title: cmake
---

## cmake
* [Policies/CMake Coding Style - KDE Community Wiki](https://community.kde.org/Policies/CMake_Coding_Style)
    * style guide

## Usage

* `CMakeLists.txt`に必要な設定をかく

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
    * 初期状態で `CMAKE_BUILD_TYPE` シンボルを書き換えないとこの状態
    * 一度でも他の値で書き換えるとずっと記憶するので、あらためて指定なしにしたい場合は `-DCMAKE_BUILD_TYPE=` とする
* Debug
    * `CMAKE_C_FLAGS` / `CMAKE_CXX_FLAGS` に加えて変数 `CMAKE_C_FLAGS_DEBUG` / `CMAKE_CXX_FLAGS_DEBUG` の値も使われる
* Release
    * `CMAKE_C_FLAGS` / `CMAKE_CXX_FLAGS` に加えて変数 `CMAKE_C_FLAGS_RELEASE` / `CMAKE_CXX_FLAGS_RELEASE` の値も使われる
* RelWithDebInfo
    * 最適化しつつデバッグ用情報も付加するためのモード
    * `CMAKE_C_FLAGS` / `CMAKE_CXX_FLAGS` に加えて変数 `CMAKE_C_FLAGS_RELWITHDEBINFO` / `CMAKE_CXX_FLAGS_RELWITHDEBINFO` の値も使われる
* MinSizeRel
    * 実行ファイルのサイズを一番小さくするためのモード
    * `CMAKE_C_FLAGS` / `CMAKE_CXX_FLAGS` に加えて変数 `CMAKE_C_FLAGS_MINSIZEREL` / `CMAKE_CXX_FLAGS_MINSIZEREL` の値も使われる

* [CMake 簡易まとめ - Qiita](http://qiita.com/janus_wel/items/a673793d448c72cbc95e)

## LDFlags
以下の4つがある。

```
CMAKE_EXE_LINKER_FLAGS
CMAKE_MODULE_LINKER_FLAGS
CMAKE_SHARED_LINKER_FLAGS
CMAKE_STATIC_LINKER_FLAGS
```

## Define preprocessor macro
コンパイルスイッチなどに用いるマクロを定義　

```
add_definitions(-DFOO -DBAR=xyz -UHOGE)
```

* `-D`で定義
* `-U`で未定義可

### Reference
* [gcc - CMake: How to set the LDFLAGS in CMakeLists.txt? - Stack Overflow](http://stackoverflow.com/questions/6077414/cmake-how-to-set-the-ldflags-in-cmakelists-txt)

## Directories

* `CMAKE_BINARY_DIR`

### Reference
* [CMake Useful Variables - KitwarePublic](https://cmake.org/Wiki/CMake_Useful_Variables)

## OSで処理を分ける

### for windows
```cmake
IF(WIN32)
ENDIF(WIN32)
```

基本的に上でOK

```cmake
if(MSVS OR MSYS OR MINGW OR CYGWIN)
endif()
```

### for OSX

```cmake
if(APPLE)
endif()
```

### for Unix and Linux

```cmake
IF(UNIX AND NOT APPLE AND NOT CYGWIN)
ENDIF(UNIX)
```

### combination

```cmake
IF(WIN32)
	# WINDOWS
ELSEIF(APPLE)
	# OSX
ELSEIF(UNIX AND NOT APPLE AND NOT CYGWIN)
	# Unix and Linux
ENDIF()
```

### Reference
* [c++ - OS specific instructions in CMAKE: How to? - Stack Overflow](http://stackoverflow.com/questions/9160335/os-specific-instructions-in-cmake-how-to)
* [c++ - OS specific instructions in CMAKE: How to? - Stack Overflow](http://stackoverflow.com/questions/9160335/os-specific-instructions-in-cmake-how-to)

## if condition

```cmake
if(expression)
elseif(expression2)
else(expression)
endif(expression)
```

* `else(exp)`は`exp`省略可
* `endif(exp)`の`exp`は省略可

## GNU standard installation dir

```cmake
include(GNUInstallDirs)
```

* `CMAKE_INSTALL_FULL_?`
	* `?`には以下の文字列が使える

```
BINDIR           - user executables (bin)
SBINDIR          - system admin executables (sbin)
LIBEXECDIR       - program executables (libexec)
SYSCONFDIR       - read-only single-machine data (etc)
SHAREDSTATEDIR   - modifiable architecture-independent data (com)
LOCALSTATEDIR    - modifiable single-machine data (var)
LIBDIR           - object code libraries (lib or lib64 or lib/<multiarch-tuple> on Debian)
INCLUDEDIR       - C header files (include)
OLDINCLUDEDIR    - C header files for non-gcc (/usr/include)
DATAROOTDIR      - read-only architecture-independent data root (share)
DATADIR          - read-only architecture-independent data (DATAROOTDIR)
INFODIR          - info documentation (DATAROOTDIR/info)
LOCALEDIR        - locale-dependent data (DATAROOTDIR/locale)
MANDIR           - man documentation (DATAROOTDIR/man)
DOCDIR           - documentation root (DATAROOTDIR/doc/PROJECT_NAME)
```

### Refernce
* [GNUInstallDirs — CMake 3.0.2 Documentation](https://cmake.org/cmake/help/v3.0/module/GNUInstallDirs.html) 

## join two lists

```cmake
function(JOIN VALUES GLUE OUTPUT)
  string (REGEX REPLACE "([^\\]|^);" "\\1${GLUE}" _TMP_STR "${VALUES}")
  string (REGEX REPLACE "[\\](.)" "\\1" _TMP_STR "${_TMP_STR}") #fixes escaping
  set (${OUTPUT} "${_TMP_STR}" PARENT_SCOPE)
endfunction()

SET( letters "" "\;a" b c "d\;d" )
JOIN("${letters}" ":" output)
MESSAGE("${output}") # :;a:b:c:d;d
```

## execute shell scripts in cmake test

```cmake
find_program(BASH_PROGRAM bash)

if (BASH_PROGRAM)
    add_test(mytest ${BASH_PROGRAM} ${CMAKE_CURRENT_SOURCE_DIR}/script.sh)
endif (BASH_PROGRAM)
```

### Reference
* [c++ - Integrate bash test scripts in cmake - Stack Overflow](http://stackoverflow.com/questions/25627336/integrate-bash-test-scripts-in-cmake)

## change output directory

```cmake
#executable
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../../../libs)
#static lib(both needed)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ../../../libs)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ../../../libs)
```

### Reference
* [出力ディレクトリを指定する - Faith and Brave - C++で遊ぼう](http://faithandbrave.hateblo.jp/entry/2014/05/14/162719)

## Link pthread
Ubuntuではpthreadはlinkしないと使えない。
CMake 3.1.0+

```cmake
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(my_app Threads::Threads)
```

CMake 2.8.12+

```cmake
find_package(Threads REQUIRED)
if(THREADS_HAVE_PTHREAD_ARG)
    target_compile_options(PUBLIC my_app "-pthread")
endif()
if(CMAKE_THREAD_LIBS_INIT)
    target_link_libraries(my_app "${CMAKE_THREAD_LIBS_INIT}")
endif()
```

Other

```cmake
find_package(Threads REQUIRED)
if(THREADS_HAVE_PTHREAD_ARG)
    set_property(TARGET my_app PROPERTY COMPILE_OPTIONS "-pthread")
    set_property(TARGET my_app PROPERTY INTERFACE_COMPILE_OPTIONS "-pthread")
endif()
if(CMAKE_THREAD_LIBS_INIT)
    target_link_libraries(my_app "${CMAKE_THREAD_LIBS_INIT}")
endif()
```

### Reference
* [pthreads - cmake and libpthread - Stack Overflow](http://stackoverflow.com/questions/1620918/cmake-and-libpthread)

## Tips

### ビルドのオプション/条件分岐
* [CMakeを使ってみた (4) ビルドオプション - wagavulin's blog](http://blog.wagavulin.jp/entry/2011/11/27/222650)

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
    * OFFだと定義されない
* CMakeLists.txt中でoptionコマンドを使う
* 明示的には指定しない → 初期値またはキャッシュされた値を使う

例えば、利用しているlibararyの`CMakeLists.txt`の中で、libraryのtestのON/OFFの設定にoptionを使っているとする。
libraryを利用する側としては、Library自体のtestは不要である場合が多い。
この場合は、自身のlibraryで`option`を使ってON/OFFの設定をすることをできる。


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

## ctest
* [ctest(1) — CMake 3.1.3 Documentation](https://cmake.org/cmake/help/v3.1/manual/ctest.1.html#manual:ctest(1))

順番が大事
`INCLUDE(Dart)`は多分最後がよい。
`INCLUDE(Dart)`実行時に、ctestへの設定が更新されるっぽい？ 

```cmake
SET(MEMORYCHECK_COMMAND_OPTIONS "--leak-check=full --show-leak-kinds=definite,possible --error-exitcode=1")
SET(MEMORYCHECK_SUPPRESSIONS_FILE "${PROJECT_SOURCE_DIR}/ci/valgrind_suppression.supp" )
FIND_PROGRAM(CTEST_MEMORYCHECK_COMMAND NAMES valgrind)
INCLUDE(Dart)
```

## reference

* [便利なコマンド](http://qiita.com/mrk_21/items/5e7ca775b463a4141a58)
* [configure_file解説](http://qiita.com/osamu0329/items/edc66e2e1b6c96947771)
* [1](http://qiita.com/termoshtt/items/539541c180dfc40a1189)
* [2](http://qiita.com/janus_wel/items/4e6c12f9104f501104c7)
* [tutorial](http://opencv.jp/cmake/cmake_tutorial.html)
