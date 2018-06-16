---
title: Travis CI Configuration
---

## Travis CI Configuration

## Configuration
You place `.travis.yml` in top of repository.

### C++
下記指定でC++としてのbuildとなる。

```yaml
language:cpp
```

デフォルトでは、`autotool`想定で書きコマンドが実行される。

```shell
./configure && make && make test
```

compilerの指定は次のようにする。

```yaml
compiler:
	- clang
	- gcc
```

もしくは

```yaml
compiler: gcc
```

### What This Guide Covers 
先にGetting Startedとgeneral build configurationを見るように。

### CI environment for C++ Projects
Travis CIのVirtual Machineは64bitで
* gcc
* clang
* core GNU build toolchain (autotools, make), cmake, scons

が備わっている。
travis-ci.orgはデフォルトでAutotoolsとMakeを使うことを想定している。

### Dependency Management
C++は他の言語のように標準的なdependency managementがないので、Travis CIでは特に何もしない。
必要なものがある場合は、`.travis.yml`の`install:`に記述する。

```yaml
install: make get-deps
```

上記の場合は`make`にルールを書いておく必要がある。


### Default Test Script
Travis CIはデフォルトでは以下のコマンドでtestを実行する。

```
./configure && make && make test
```

上記でbuildとtestのチェックができるが、この処理を上書きたい場合は他の言語同様`script:`を上書きする。

```yaml
script: cmake; ctest
```

### Choosing compilers to test against
gcc, clangの両方でテストが可能。
`compiler:`で指定する。

```yaml
#clangのみ
compiler: clang
#clangとgcc
compiler:
  - clang
  - gcc
```

`compiler:`を設定すると環境変数として以下が設定される。

* `CXX`に`g++` or `clang++`
* `CC`に`gcc` or `clang`

後述のbuild matrix

### Build Matrix
C++のbuild matrixの変数は、`env`と`compiler`の2つである。
つまり、`env`と`compiler`で指定した組み合わせの数だけbuildが実行される。

## Building a Python  Project

### What This Guide Covers

### Choosing Python versions to test against
pythonの2.6, 2.7,...3.6でテストしたいときは以下のようにかく。

```yaml
language: python
python:
  - "2.6"
  - "2.7"
  - "3.2"
  - "3.3"
  - "3.4"
  - "3.5"
  - "3.5-dev" # 3.5 development branch
  - "3.6-dev" # 3.6 development branch
  - "nightly" # currently points to 3.7-dev
# command to install dependencies
install: "pip install -r requirements.txt"
# command to run tests
script: pytest
```

### Travis CI Uses Isolated virtualenv
ciのpythonは全てvirtualenv上で実行される。
なのでpythonのpackageはaptではなくpipでいれる。


### PyPy Support
Travis CIはPyPyとPyPy3に対応している。

```yml
python:
  - "2.6"
  - "2.7"
  - "3.2"
  - "3.3"
  - "3.4"
  # PyPy versions
  - "pypy"
  - "pypy"  # PyPy2 2.5.0
  - "pypy3" # Pypy3 2.4.0
  - "pypy-5.3.1"
```

### Default Python Version
defaultは2.7

### Specifying Test Scrip
testの実行方法を記載。
以下では`pytest`というコマンドが実行される。
`script`がないとfailする。

```yml
# command to run tests
script: pytest
```

### Build Matrix
pythonのBuild matrixは`python`と`env`によって生成される。

## Reference
