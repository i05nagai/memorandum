---
title: Upstart
---

## Upstart
scriptをdaemon化できる。
`/sbin/init` daemon (例えばSysVinit)を置き換えるもの。


## Configuration

```
description "(説明を書く)"
author  "(あなたの名前) <(メアド@ドメイン)>"

start on runlevel [(Run Level)]
stop on runlevel [(Run Level)]

chdir (作業ディレクトリ)
exec (起動コマンド)
respawn
```

`exec`か`script`が必須。

```
exec /bin/foo --opt -xyz foo bar
```

```
script
    # do some stuff
    if [ ... ]; then
        ...
    fi
end script
```

`exec`, `script`の前後に`pre-start`, `post-stop`で実行の前後の処理を記述できる。

* `pre-start`
* `post-start`
* `pre-stop`
* `post-stop`

```
pre-start script
    # prepare environment
    mkdir -p /var/run/foo
end script
post-stop script
    # clean up
    rm -rf /var/run/foo
end script
```

start/stopの条件は以下の4通り。

* `startup`
    * machineの起動時に開始
* `runlevel []`
    * [Linux Runlevels Explained – Liquid Web Knowledge Base](https://www.liquidweb.com/kb/linux-runlevels-explained/)
    * 指定したrunlevelのInit scriptと同じタイミングで実行
    * 0 : System halt.
    * 1 : Single-User mode.
    * 2 : Graphical multi-user plus networking (DEFAULT)
    * 3 : Same as "2", but not used.
    * 4 : Same as "2", but not used.
    * 5 : Same as "2", but not used.
    * 6 : System reboot.
    * 通常のstart
        * [Upstart Intro, Cookbook and Best Practises](http://upstart.ubuntu.com/cookbook/#normal-start)
        * `start on runlevel [2345]`
    * 通常のshutdown
        * `start on runlevel [016]`
* `stopped [jobname]`
   * 他のjobが止まったときに実行
* `started [jobname]`
   * 他のjobが開始されたときに

```
start on startup
start on runlevel [23]
start on stopped rcS
start on started tty1
```

停止については、`stop on`で記述する。

* `env`
    * `script` sectionで記述されたscriptで利用可能な環境変数の定義
* `export`
    * `env`で設定された変数を環境変数にする

```
env myvar="hello world"
export myvar
```

* `respawn`
    * jobがstopになる前に、もう一度jobを実行する
    * その際`pre-start`, `post-start`, `post-stop`が実行される

* `respawn limit COUNT INTERVAL | unlimited`
    * respawnの回数をCOUNT回にする
    * INTERVAL secごとに繰り返す

## CLI

設定の反映は以下で可能。

```
sudo initctl reload-configuration
```

設定されているinitの一覧

```
 sudo initctl list
```

`[name]`の起動。

```
sudo initctl start [name]
```


## Reference
* [Getting Started - upstart](http://upstart.ubuntu.com/getting-started.html)
* [Upstart を使ってお手軽 daemon 化 - インフラエンジニアway - Powered by HEARTBEATS](https://heartbeats.jp/hbblog/2013/02/upstart-daemon.html)
* [Upstart Intro, Cookbook and Best Practises](http://upstart.ubuntu.com/cookbook/)
