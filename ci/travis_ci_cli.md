---
title: Travis CI CLI
---

## Travis CI CLI
Travis CI provides CLI tools to manage Travis CI from CLI.

## Install
* Ruby1.9.3
* RubyGem

```
gem install travis --no-rdoc --no-ri
```

## CLI

```
travis encrypt
```

```
travis encrypt-file
```

## Usage

## Configuration

## Tips


### Validating .travis.yml files
以下のサイトでonlineのvalidationができる。
* [Validate your .travis.yml file](http://lint.travis-ci.org/)

lint

```
travis lint /path/to/.travis.yml
```

### Encrypting your credentials
tokenがわかると誰でも通知できてしまうので、tokenを暗号化したものを`.travis.yml`に記載する。
暗号化はCommand line toolsをインストールし、以下を実行する。

```
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

```yaml
notifications:
  slack:
    rooms:
      - secure: "key"
```

Travis CLIで、暗号化ができる。
どのくらい信頼度があるかは不明。

```
travis encrypt SOMEVAR=secretvalue
```

を実行すると

```
secure: ".... encrypted data ...."
```

と暗号化されたデータが得られる。
これを暗号化前のkeyとしてymlにおけば良い。

## Reference
