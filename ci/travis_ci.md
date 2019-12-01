---
title: Travis Ci
---

## Travis CI

* `dist:trusty`
   * g++-4.8.4がdefaultで使える
* `g++-4.6`

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

```yaml
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

```yaml
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


## Using Docker in Builds
以下が必要。

```yaml
sudo: required
services:
  - docker
```

Building a Docker image from a Dcokerfile

Dockerfileのbuildは普通にできる。
実行前に行いたい場合は、`before_install`などに記載すれば良い。

Pushing docker image to a Registory

環境変数として、`DOKCER_USERNAME`と`DOCKER_PASSWORD`を定義しておく。
CLIであれば、以下。

```
travis env set DOCKER_USERNAME myusername
travis env set DOCKER_PASSWORD secretsecret
```

docker loginをすればOK。

```
docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
```

Using Docker Compose

dockerが使えればdefaultで入っている。
最新のversionがほしい場合は、以下のようにすれば良い。

```yaml
env:
  - DOCKER_COMPOSE_VERSION=1.4.2
before_install:
  - sudo rm /usr/local/bin/docker-compose
  - curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > docker-compose
  - chmod +x docker-compose
  - sudo mv docker-compose /usr/local/bin
```

Intalling a newer Docker version

dockerのversionをupdateする場合は

* apt.dockerproject.orgからDL

```yaml
before_install:
  - sudo apt-get update
  - sudo apt-get -y -o Dpkg::Options::="--force-confnew" install docker-engine
```

* download.docker.comからDL

```yaml
before_install:
  - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  - sudo apt-get update
  - sudo apt-get -y install docker-ce
```

## Notifications

### slack
1. slackの`App & Integraiton`より、Travis CIを選択
2. 登録するとTokenが発行される
3. 以下のいずれかを`.travis.yml`に記載
    * simple

```yaml
notifications:
  slack: i05nagai:Onqc91K8U1WKSLYGgThWftTY
```

multi-channel

```yaml
notifications:
  slack:
    rooms:
      - account_name:token#channel
      - account_name:token#channel
```

### Encrypting your credentials
Use travis CLI.

## Environment Variables
* [Environment Variables - Travis CI](https://docs.travis-ci.com/user/environment-variables/#Default-Environment-Variables)

Defining Variables in Repository Settings

Default Environment Variables

Travisで利用可能な環境変数の一覧

* TRAVIS_BUILD_DIR
    * Travis CIにcopyされたrepositoryのtop directory


## Encrypting Files and Data

### Detailed Discussion
どのように暗号化されたテキストが復号化されるかを説明する。

以下のようになっているとすると

```yaml
notifications:
  campfire:
    rooms:
      secure: "encrypted string"
```

次のように解釈される。

```yaml
notifications:
  campfire:
    rooms: "decrypted string"
```

一方、次の場合は

```yaml
notifications:
  campfire:
    rooms:
      - secure: "encrypted string"
```

次のようになる。

```yaml
notifications:
  campfire:
    rooms:
      - "decrypted string"
```

環境変数も同様である。

```yaml
env:
  - secure: "encrypted string"
```

```yaml
env:
  - "decrypted string"
```


## Tips

### travis command line tools
* [travis-ci/travis.rb: Travis CI Client (CLI and Ruby library)](https://github.com/travis-ci/travis.rb)


### Adding private key
Private keyを追加する方法。

* [squeezing private SSH key into .travis.yml file](https://gist.github.com/lukewpatterson/4242707)
* [Travis-CI でコミットして GitHub にプッシュする - 公開鍵認証を利用してみる | そんなこと覚えてない](http://blog.eiel.info/blog/2014/02/18/github-push-from-travis/)

### OSXのビルドの開始が遅い
OSXのビルドは、物理マシンを利用しているので、利用者が多い場合は開始に時間がかかる。 下記にTravis CIのビルドステータスがある。

* [Travis CI Status](https://www.traviscistatus.com/)

OSXでのjob数はずっと同じ値になっており、Jobがスタックしているのが分かる。

* [OSX builds extremely slow to start · Issue #7304 · travis-ci/travis-ci](https://github.com/travis-ci/travis-ci/issues/7304)

### PRのブランチは全てビルド、pushはmasterのみにする場合
`.travis.yml`に以下を記載。

```yaml
branches:
  only: 
    # branchs through PR are built
    - master
```

上記は`push`でのビルドのみに影響を与える。
travis ciのsettingsから`Build pushs`と`Build pull requests`をONにすれば良い。

pushでのビルドをオフにすると、merge後のmaster branchのビルドが行われない為、badgeが更新されない。
PRでのビルドはOSSの場合必須なので、ビルドは抑えたい場合はこのような設定が必要。

### Use GCC48
For OSX, [The OS X Build Environment - Travis CI](https://docs.travis-ci.com/user/osx-ci-environment/#OS-X-Version)

```
brew install gcc48
```


### Validating .travis.yml files
以下のサイトでonlineのvalidationができる。

* [Validate your .travis.yml file](http://lint.travis-ci.org/)

```
travis lint /path/to/.travis.yml
```

### Docker images
* [Quay Container Registry · Quay](https://quay.io/organization/travisci)

#### Add deploy key for Github
Register environment variables to travis as `DEPLOY_KEY`.

```
cat /path/to/keyfile | base64 --wrap=0
```

You can add the following line to push commits to the repository.

```
ssh-agent bash -c "
  echo \"${DEPLOY_KEY}\" | base64 -d | ssh-add -
  GIT_SSH_COMMAND='ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no' git push origin master
"
```


## Reference
* [C++14 on Travis CI with CMake](https://jonasw.de/_posts/2015-07-22-cplusplus14-on-travis-with-cmake.md)
* [http://packsaddle.org/articles/differences-between-travis-ci-and-circle-ci/ TravisCIとCircleCIでちょっとずつ違うビルド環境の考え方の違い – Saddler - checkstyle to anywhere]
* [Travis CIからgithub.ioにデプロイする方法 - Qiita](http://qiita.com/dora56/items/cafae475daec802b6b8f)
* [promises-guide/deploy-gh-pages.sh at master · w3ctag/promises-guide · GitHub](https://github.com/w3ctag/promises-guide/blob/master/deploy-gh-pages.sh)
