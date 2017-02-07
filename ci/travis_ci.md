
<!-- vim-markdown-toc GFM -->

* [Travis CI](#travis-ci)
	* [Customizing the Build](#customizing-the-build)
		* [The Build Lifecycle](#the-build-lifecycle)
		* [Installing Packages Using apt](#installing-packages-using-apt)
		* [Builds Time out](#builds-time-out)
		* [Git clone depth](#git-clone-depth)
		* [Building specific branches](#building-specific-branches)
		* [Skipping a build](#skipping-a-build)
		* [Build Matrix](#build-matrix)
			* [Excluding Jobs](#excluding-jobs)
	* [Installing Dependencies](#installing-dependencies)
	* [Validating .travis.yml files](#validating-travisyml-files)
		* [online](#online)
		* [offline](#offline)
	* [Building a Python  Project](#building-a-python--project)
		* [What This Guide Covers](#what-this-guide-covers)
		* [Choosing Python versions to test against](#choosing-python-versions-to-test-against)
		* [Travis CI Uses Isolated virtualenv](#travis-ci-uses-isolated-virtualenv)
		* [PyPy Support](#pypy-support)
		* [Default Python Version](#default-python-version)
		* [Specifying Test Scrip](#specifying-test-scrip)
	* [Building a C++ Project](#building-a-c-project)
		* [What This Guide Covers](#what-this-guide-covers-1)
		* [CI environment for C++ Projects](#ci-environment-for-c-projects)
		* [Dependency Management](#dependency-management)
		* [Default Test Script](#default-test-script)
		* [Choosing compilers to test against](#choosing-compilers-to-test-against)
		* [Build Matrix](#build-matrix-1)
	* [Configuring Build Notifications](#configuring-build-notifications)
		* [Notifications](#notifications)
	* [Notifications](#notifications-1)
		* [slack](#slack)
		* [Encrypting your credentials](#encrypting-your-credentials)
	* [CI Environment Reference](#ci-environment-reference)
		* [The OS X Build Environment - Travis CI](#the-os-x-build-environment---travis-ci)
	* [Encrypting Files and Data](#encrypting-files-and-data)
		* [Usages](#usages)
			* [Note on escaping certain symbols](#note-on-escaping-certain-symbols)
			* [Notifications Example](#notifications-example)
			* [Detailed Discussion](#detailed-discussion)
	* [tips](#tips)
		* [travis command line tools](#travis-command-line-tools)
	* [.travis.yml](#travisyml)
		* [C++](#c)
			* [reference](#reference)

<!-- vim-markdown-toc -->


# Travis CI


## Customizing the Build
repositoryのtopにある`.travis.yml`ファイルに基づいてCIが実行される。
`.travis.yml`の中では以下を記載する。

* プロジェクトで使用しているプログラミング言語
* buildの前に実行するscriptやcommand
* test suiteを実行するのに必要なcommand
* e-mailやcampfire,IRCなどの通知サービスへの通知方法

### The Build Lifecycle
buildのライフサイクルは以下のようになる。
それぞれライフサイクルの設定を`yml`に記載する。

1. Install `apt addons`
1. `before_install`
    * `apt`自身のupdateやrepositoryの追加など、installに必要なコマンド自体のset-up
1. `install`
    * `apt-install`などでのプロジェクトの依存関係の整理
    * 各言語ごとのパッケージマネージャー(RubyのBundleやgem、pythonのpipなど）の実行
1. ` before_script`
    * scriptを実行する前に必要な処理
1. `script`
    * buildとtestの実行
    * 各言語ごとにデフォルトの処理があるので、必要なら上書きして自身のプロジェクト用に設定する。
1. `after_success` or `after_failure`
    * build/testが成功した時と失敗した時の処理について記載
1. OPTIONAL `before_deploy`
1. OPTIONAL `deploy`
1. OPTIONAL `after_deploy`
1. `after_script`

各言語ごとに、それぞれのステップでデフォルトの処理(skip、つまり処理なしも含む）が存在する。
自分のプロジェクトがデフォルトの処理では、依存関係やテストの実行などができない場合に、デフォルトの処理を上書きするというのが基本的な設定方法となる。

例えば、Rubyであればgem及びbundle、pythonであればpipなど標準的な依存関係解決の手段がある場合は、それらのinstallコマンドが実行されるようになっている。
詳細については、各言語ごとのhelpを見る必要がある。

### Installing Packages Using apt
依存関係の解決方法

```yml
before_install:
- sudo apt-get update -qq
- sudo apt-get install -qq [packages list]
```

### Builds Time out
buildの時間制限
* `travis-ci.org` は50分
* `travis-ci.com`は120分
* OSXの場合は、50分まで
* 10分ログの出力がないもの

Buildが止まる主な理由は
* keyboardの入力まち
* deadlock, livelockなどの並列計算での問題
* 他のアプリのinstallにかかる時間

### Git clone depth
git-cloneするときのcommitのcopyの深さ。
gitのperformanceをあげる時に有用。
maxは50。

```yml
git:
  depth: 3
```

### Building specific branches
buildするbranchとbuildしないbranchを指定できる。
`gh-pages`はsafelistにいれるない限りbuildされない。
`only`と`except`の両方に書いた場合は、`only`が優先される。

```yml
branches:
  # blocklist
  except:
    - legacy
    - experimental
# safelist
branches:
  only:
    - master
    - stable
```

branch名には、Rubyの正規表現も利用可能。

```yaml
branches:
  only:
    - master
    - /^deploy-.*$/
```

### Skipping a build
commit messageに`[ci skip]`, `[skip ci]`を入れてコミットするとbuildがskipされる。

### Build Matrix
各言語ごとに

#### Excluding Jobs


## Installing Dependencies


## Validating .travis.yml files

### online
以下のサイトでonlineのvalidationができる。
* [Validate your .travis.yml file](http://lint.travis-ci.org/)

### offline
オフラインの場合は下記が必要。
* Ruby1.9.3
* RubyGem

インストール

```yml
gem install travis --no-rdoc --no-ri
```

実行

```yml
travis lint /path/to/.travis.yml
```

## Building a Python  Project

### What This Guide Covers

### Choosing Python versions to test against
pythonの2.6, 2.7,...3.6でテストしたいときは以下のようにかく。
```yml
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


## Building a C++ Project

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

```yml
install: make get-deps
```

上記の場合は`make`にルールを書いておく必要がある。


### Default Test Script
Travis CIはデフォルトでは以下のコマンドでtestを実行する。

```yml
./configure && make && make test
```

上記でbuildとtestのチェックができるが、この処理を上書きたい場合は他の言語同様`script:`を上書きする。

```yml
script: cmake; ctest
```

### Choosing compilers to test against
gcc, clangの両方でテストが可能。
`compiler:`で指定する。

```yml
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

## Configuring Build Notifications
### Notifications

## Notifications
### slack
1. slackの`App & Integraiton`より、Travis CIを選択
2. 登録するとTokenが発行される
3. 以下のいずれかを`.travis.yml`に記載
    * simple

```yml
notifications:
  slack: i05nagai:Onqc91K8U1WKSLYGgThWftTY
```

    * multi-channel

```yml
notifications:
  slack:
    rooms:
      - account_name:token#channel
      - account_name:token#channel
```

    * 

### Encrypting your credentials
tokenがわかると誰でも通知できてしまうので、tokenを暗号化したものを`.travis.yml`に記載する。
暗号化はCommand line toolsをインストールし、以下を実行する。

```shell
travis encrypt "account_name:token#channel"
```

実行すると下記が出力される。

```
Detected repository as repository/name, is this correct? |yes| yes
Please add the following to your .travis.yml file:

  secure: "key"

  Pro Tip: You can add it automatically by running with --add.
```

`secure: "key"`の部分をコピーして`.travis.ylm`に以下のように貼り付ける。　

```
notifications:
  slack:
    rooms:
      - secure: "key"
```

## CI Environment Reference

### The OS X Build Environment - Travis CI
* [The OS X Build Environment - Travis CI](https://docs.travis-ci.com/user/osx-ci-environment/#OS-X-Version)

```
brew install gcc48
```

## Encrypting Files and Data

### Usages
Travis CLIで、暗号化ができる。
どのくらい信頼度があるかは不明。

```shell
gem install travis
```

```shell
travis encrypt SOMEVAR=secretvalue
```

を実行すると

```shell
secure: ".... encrypted data ...."
```

と暗号化されたデータが得られる。
これを暗号化前のkeyとしてymlにおけば良い。

#### Note on escaping certain symbols

#### Notifications Example 

#### Detailed Discussion
どのように暗号化されたテキストが復号化されるかを説明する。

以下のようになっているとすると

```yml
notifications:
  campfire:
    rooms:
      secure: "encrypted string"
```

次のように解釈される。

```yml
notifications:
  campfire:
    rooms: "decrypted string"
```

一方、次の場合は

```yml
notifications:
  campfire:
    rooms:
      - secure: "encrypted string"
```

次のようになる。

```yml
notifications:
  campfire:
    rooms:
      - "decrypted string"
```

環境変数も同様である。

```yml
env:
  - secure: "encrypted string"
```

```yml
env:
  - "decrypted string"
```


## tips
### travis command line tools
* [travis-ci/travis.rb: Travis CI Client (CLI and Ruby library)](https://github.com/travis-ci/travis.rb)


## .travis.yml
### C++
下記指定でC++としてのbuildとなる。
```yml
language:cpp
```
デフォルトでは、`autotool`想定で書きコマンドが実行される。

```shell
./configure && make && make test
```

compilerの指定は次のようにする。
```cpp
compiler:
	- clang
	- gcc
```
もしくは
```shell
compiler: gcc
```

### Private key
Private keyを追加する方法。

* [squeezing private SSH key into .travis.yml file](https://gist.github.com/lukewpatterson/4242707)
* [Travis-CI でコミットして GitHub にプッシュする - 公開鍵認証を利用してみる | そんなこと覚えてない](http://blog.eiel.info/blog/2014/02/18/github-push-from-travis/)


#### reference
* [C++14 on Travis CI with CMake](https://jonasw.de/_posts/2015-07-22-cplusplus14-on-travis-with-cmake.md)
* [http://packsaddle.org/articles/differences-between-travis-ci-and-circle-ci/ TravisCIとCircleCIでちょっとずつ違うビルド環境の考え方の違い – Saddler - checkstyle to anywhere]
* [Travis CIからgithub.ioにデプロイする方法 - Qiita](http://qiita.com/dora56/items/cafae475daec802b6b8f)
* [promises-guide/deploy-gh-pages.sh at master · w3ctag/promises-guide · GitHub](https://github.com/w3ctag/promises-guide/blob/master/deploy-gh-pages.sh)
