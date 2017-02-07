
<!-- vim-markdown-toc GFM -->

* [Circle CI](#circle-ci)
	* [Getting Started](#getting-started)
		* [Configuring CircleCI](#configuring-circleci)
			* [File Structure and Content](#file-structure-and-content)
		* [Manual build setup](#manual-build-setup)
			* [The anatomy of a CircleCI build](#the-anatomy-of-a-circleci-build)
			* [Checking out code](#checking-out-code)
			* [Setting up your dependencies](#setting-up-your-dependencies)
			* [Setting up your test databases](#setting-up-your-test-databases)
			* [Running your tests](#running-your-tests)
	* [Build Image](#build-image)
	* [Languages](#languages)
		* [Continuous Integration and Continuous Deployment with Python](#continuous-integration-and-continuous-deployment-with-python)
			* [Version](#version)
	* [How-To](#how-to)
		* [Code Coverage](#code-coverage)
	* [Troubleshooting](#troubleshooting)
		* [SSH access to builds](#ssh-access-to-builds)
	* [reference](#reference)

<!-- vim-markdown-toc -->

# Circle CI

## Getting Started

### Configuring CircleCI
repositoryのroot directoryに`circle.yml`ファイルを置くことで、設定ができる。

#### File Structure and Content
`circle.yml`は大きく以下のsectionに分かれている。
上から順に設定される。

1. `machine:`
    * VMの動作の設定をする
1. `checkout:`
    * codeのcheckoutに関する設定をする
1. `dependencies:`
    * プロジェクトの依存関係を整理する
1. `database:`
    * testに利用するdatabaseを設定する
1. `compile:`
    * compileが必要な場合にcompilerする
1. `test:`
    * テストを実行する
1. `deployment:`
    * web serverにdeployする

更に`circle.yml`では以下の2つのoptionalな設定を記載できる。

* `general:`
	* build全体で利用する設定
* `experimental:`
	* 開発中の機能をtestするためのコマンド

#### Timezone
wikipediaのTZの値が利用できる。

```yml
machine:
  timezone:
    America/Los_Angeles
```

* [List of tz database time zones - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

#### Python Version
Circle CIはpyenvを使っている。
下記の方法でversion番号を指定できる。

```
machine:
  python:
    version: 2.7.5
```

#### Deployment
branchにあわせてdeploy先を変更できる。

```yml
deployment:
  production:
    branch: production
    commands:
      - ./deploy_prod.sh
  staging:
    branch: master
    commands:
      - ./deploy_staging.sh
```

branchはリストで指定できる。


### Manual build setup 

#### The anatomy of a CircleCI build
以下の順番でセットアップが実行される。

1. Configure the test machine
1. Check out your code
	* githubからのcodeのcheckoutが実行される
1. Set up your test dependencies
	* githubからのcodeのcheckoutが実行される
1. Set up your test databases
1. Run your tests
1. (Optionally) deploy your code

#### Checking out code
checkout sectionの`post:`は、codeのcheckout後に実行されるコマンドを記述する。
defaultでは、submoduleはcheckoutされない。
checkoutが必要な場合は、自分で設定する。

```yml
checkout:
  post:
    - git submodule sync
    - git submodule update --init
```

#### Setting up your dependencies
buildとtestの依存関係の設定をする。
CircleCIではデフォルトで、rubyのGemfileやpythonのrequiremetns.txtやClojureのproject.cljやNodeのpackage.jsonなどを見つけ、依存関係を読み込む。
`pre:`, `override:`, `post:`を記載できる。

```yml
dependencies:
  pre:
	- some_command_here
  override:
    - some_command_here
  post:
    - python ./install-packages
```

#### Setting up your test databases
test実行前にtestに必要なdatabaseの設定を行う。
MySQLとPostgresについては、CircleCIが用意している`circle_test`databseと`ubuntu`userが使えるようになっている。
全てのdatabaseでpasswordは要求されない。
例えば、以下のように記載する。

```yml
database:
  override:
    - mysql -u ubuntu circle_test < my-database-setup.sql
```

#### Running your tests
testを実行する。
`override:`に実行したいコマンドを記載する。

```yml
test:
  override:
    - php ./test-suite/run.php --unit-tests
```

先にserverを実行する必要がある場合などは、以下のようにする。

```yml
test:
  override:
    - php ./app/run-server.php --daemon
    - php ./test-suite/run.php --unit-tests
```

## Build Image
* Ubuntu 12.04 (Precise)
* Ubuntu 14.04 (Trusty)


## Languages

### Continuous Integration and Continuous Deployment with Python

#### Version

## How-To

### Code Coverage

## Troubleshooting

### SSH access to builds
debugの最も効率的な方法の1つは、sshでCI端末にアクセスし、log fileやprocessを確認することである。


<img src="https://circleci.com/docs/assets/img/docs/ssh-build-button-current.png" width="640px">

<img src="https://circleci.com/docs/assets/img/docs/ssh-build-button-rebuild.png" width="640px">

#### Reference
* [SSH access to builds - CircleCI](https://circleci.com/docs/ssh-build/)


## Circle CIのenvironment variableに登録できるサイズの上限
約130KB。
環境変数の数にもよる。

### Reference
* [CircleCIに任意のデータを登録しておく方法 - Qiita](http://qiita.com/minodisk/items/ce488178d74ce63c3e53)

## email notification
Account settings -> 

* [Streamline Your Inbox with Per-Project Notification Settings - CircleCI](https://circleci.com/blog/streamline-your-inbox-with-per-project-notification-settings/)

## slack integration
* [Slack Integration - CircleCI](https://circleci.com/blog/slack-integration/)

## githubのprivate key


## reference
* [CircleCIアンチパターン 2015春 - tehepero note(・ω<)](http://blog.stormcat.io/entry/2015/03/31/154300)
* [まだ Travis で消耗してるの？ - Qiita](http://qiita.com/KeithYokoma/items/cf56ef89c8362953a6a7)
* [まだ CircleCI で消耗してるの？ - Qiita](http://qiita.com/KeithYokoma/items/b839ef3f5496a22f3e7a#_reference-3b29690796d83937e179)
