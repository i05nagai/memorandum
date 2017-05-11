---
title: Fluentd
---

## Fluentd

## Config

### source

### match
他のsystemにoutputする。
output pluginとも呼ばれる。

```
# Match events tagged with "myapp.access" and
# store them to /var/log/fluent/access.%Y-%m-%d
# Of course, you can control how you partition your data
# with the time_slice_format option.
<match myapp.access>
    @type file
    path /var/log/fluent/access
</match>
```

typeでoutput pluginを指定。

上記の例では、`http://this.host:9880/myapp.access?json={"event":"data"}`のアクセスに対して、`{"event":"data"}`がpathに出力される。

## Plugins

### monitor_agent
* [td-agent(fluentd) の monitor_agent で取得出来る情報を Graphite + Grafana で見る試み - ようへいの日々精進XP](http://inokara.hateblo.jp/entry/2014/05/31/081249)


### tail
* [fluentd tailプラグインの仕様について - oranie's blog](http://oranie.hatenablog.com/entry/20121006/1349509523)

tailプラグインはLinuxコマンドで言う「tail -F」と同じような挙動を取る事により、ファイルに追記された情報をfluentd内に取り込む事が出来ます。追記されたかどうかはIOイベントを読み取って動作します。

* `path`
    * 対象のファイルパスを指定
* `tag`
    * tailしたデータのtag
* `format`
    * tailするデータの形式
    * template名か正規表現
* `pos_file`
    * tailしているファイルのどこまでをtailしたかを記録するファイルのパス

### out_copy
store句に複数のコピー先をかける。

### out_forward
別のfluentd nodeにデータをforwardする。
replicationには`out_copy`を使う

```config
<match pattern>
  @type forward
  send_timeout 60s
  recover_wait 10s
  heartbeat_interval 1s
  phi_threshold 16
  hard_timeout 60s

  <server>
    name myserver1
    host 192.168.1.3
    port 24224
    weight 60
  </server>
  <server>
    name myserver2
    host 192.168.1.4
    port 24224
    weight 60
  </server>
  <secondary>
    @type file
    path /var/log/fluent/forward-failed
  </secondary>
</match>
```

* `heartbeat_type`
    * defaultはudp
    * tcp, noneも可能
* `flush_interval`
    * defaultは60s
    * bufferのflushの間隔？
    * bufferの内容を書き出す間隔?
* `buffer_type`
    * defaultはmemory
    * fileも可
    * fileの場合は`buffer_path`が必要

## Reference
* [Configuration File Syntax | Fluentd](http://docs.fluentd.org/v0.12/articles/config-file#1-ldquosourcerdquo-where-all-the-data-come-from)
