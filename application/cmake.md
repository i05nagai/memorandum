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

## reference

* [便利なコマンド](http://qiita.com/mrk_21/items/5e7ca775b463a4141a58)
* [configure_file解説](http://qiita.com/osamu0329/items/edc66e2e1b6c96947771)
* [1](http://qiita.com/termoshtt/items/539541c180dfc40a1189)
* [2](http://qiita.com/janus_wel/items/4e6c12f9104f501104c7)
* [tutorial](http://opencv.jp/cmake/cmake_tutorial.html)

