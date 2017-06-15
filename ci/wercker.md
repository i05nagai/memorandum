## Wercker

`wercker.yml`に設定を記述する。


## Python
* [Getting started with Wercker & Python](http://devcenter.wercker.com/docs/quickstarts/building/python)

```yaml
# The container definition we want to use for developing our app
box: python:2.7-slim

dev:
  steps:
    # first we want to run pip-install to install all the dependencies
    - pip-install
    # then we want to run a wercker step that watches your files and reloads
    # when changes are detected.
    - internal/watch:
        code: python app.py
        reload: true
```

* `box: python:2.7-slim`
    * DockerHubのContainerを指定できる
    * 他のregistryも設定で登録可能
* `dev:`
    * development pipelineのコマンドなど
    * pipelineの中はstepで構成される
    * stepは自分で記述するか、werckerやcommunityによって提供されるbash scriptなど
* `pip-install`
    * dev pipelineのstep

## Steps
Step registoryでcommunity から提供されているstepを利用できる。

* https://app.wercker.com/#explore/steps/search/

### Internal Steps

* `internal/watch`
    * fileの変更で更新されるstep
    * よくあるのが、front-end developerがwebserverにファイルの変更を知らせる
    * 以下はnpmの例

```yaml
box: nodesource/trusty
dev:
  steps:
    - npm-install
    - internal/watch:
        code: node app.js
        reload: true
```

これを実行する場合は、

```
wercker dev --publish 5000
```

`5000`でserverを見ることができる。

OSXで使う場合は、一度に大量のファイルを監視すると制限に引っかかるため、以下のコマンドでしきい値を変更する。

```
sysctl -w kern.maxfiles=20480 (or whatever number you choose)
sysctl -w kern.maxfilesperproc=18000 (or whatever number you choose)
```

#### Internal/shell
shellのコマンドを実行したい場合は、`internal/shell`を使う。

* `cmd`
    * 起動するshell
* `code`
    * 実行するshellコマンド

```yaml
box: nodesource/trusty
dev:
  - npm-install
  - internal/shell:
      cmd: /bin/sh  #defaults to /bin/bash
      code: |
        # some code to automatically run in your shell session
        # before you start interacting
        cd /var/log
```

### Script Step
単純なshell commandを実行できる。
interna/shellとの使い分けは？

```yaml
build:
  steps:
    - script:
      name: indentify distribution
      code: cat /etc/lsb-release
    - script:
      name: starting xvfb
      code: |
        # Start xvfb which gives the context an virtual display
        # which is required for tests that require an GUI
        export DISPLAY=:99.0
        start-stop-daemon --start --quiet --pidfile /tmp/xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -screen 0 1024x768x24 -ac +extension GLX +render -noreset
        # Give xvfb time to start. 3 seconds is the default for all xvfb-run commands.
        sleep 3
```

### Creating Steps
Step registryに目的のstepがない場合は自分で定義することができる。


### Install Packages
containerに必用な依存ファイルをinstallする場合は、 `install-packages` stepを使う。
versionの指定も可能。

```yaml
- install-packages:
        packages: apache2=2.2.20-1ubuntu1
```


### After steps
step実行後に実行する場合は、`after-steps`というstepを使う。

```yaml
deploy:
    steps:
        - script:
            name: fabric deploy
            code: |
              fab deploy
    after-steps:
        - hipchat-notify:
            token: $HIPCHAT_TOKEN
            room_id: id
            from-name: name
```

## Environment variables



## reference
* [まだ CircleCI で消耗してるの？ - Qiita](http://qiita.com/KeithYokoma/items/b839ef3f5496a22f3e7a#_reference-3b29690796d83937e179)
* [Werckerの仕組み，独自のboxとstepのつくりかた | SOTA](http://deeeet.com/writing/2014/10/16/wercker/)
