---
title: fluentd input
---

## fluentd input

### in_http

### in_forward

### in_td_monitor_agent
* [treasure-data/fluent-plugin-td-monitoring: Fluentd Plugin for Treasure Agent Monitoring Service](https://github.com/treasure-data/fluent-plugin-td-monitoring)

TD monitoring serviceにnodeとbufferの情報をおくる。

* `api_key`
    * Treasure dataのAPI key
* `instance_id`
    * fluentdのnode間のID
    * 指定しないとconfigへのpathが使われる

```
<source>
  type td_monitor_agent
  apikey YOUR_TREASURE_DATA_APIKEY
  instance_id aggregator1
</source>
```

### in_monitor_agent
* [td-agent(fluentd) の monitor_agent で取得出来る情報を Graphite + Grafana で見る試み - ようへいの日々精進XP](http://inokara.hateblo.jp/entry/2014/05/31/081249)

以下の設定をすると、httpアクセスでpluginなどの情報がとれる。

```
<source>
  type monitor_agent
  bind 0.0.0.0
  port 24220
</source>
```

```
curl -s http://${TD_AGENT_HOST}:24220/api/plugins.json | jq .
```

### tail
* [fluentd tailプラグインの仕様について - oranie's blog](http://oranie.hatenablog.com/entry/20121006/1349509523)

tailプラグインはLinuxコマンドで言う「tail -F」と同じような挙動を取る事により、ファイルに追記された情報をfluentd内に取り込む事が出来ます。追記されたかどうかはIOイベントを読み取って動作します。

* `path`
    * 対象のファイルパスを指定
* `tag string`
    * tailしたデータのtag
    * `hoge.*`
        * `*`はfilepathの`/`を`.`に置き換えたものをtagとしてふよする
* `format`
    * tailするデータの形式
    * template名か正規表現
* `pos_file`
    * highly recommended
    * tailしているファイルのどこまでをtailしたかを記録するファイルのパス
* `time_format`
    * `%Y-%m-%dT%H:%M:%S.%N%Z`
* `read_from_head`
    * default false
    * head of fileから読む

### systemd
* [reevoo/fluent-plugin-systemd: This is a fluentd input plugin. It reads logs from the systemd journal.](https://github.com/reevoo/fluent-plugin-systemd)

* `path`
    * default `/var/log/journal`
* `filters`
    * 
* `pos_file`
    * depreacated
    * use `<storage>`
* `read_from_head`
    * default false
    * falseだとtail
* `strip_underscores`
    * deprecated
* `tag`
* `<storage>`
* `<entry>`

```
<source>
  @type systemd
  tag kube-proxy
  path /var/log/journal
  filters [{ "_SYSTEMD_UNIT": "kube-proxy.service" }]
  read_from_head true
  <storage>
    @type local
    persistent false
    path kube-proxy.pos
  </storage>
  <entry>
    field_map {"MESSAGE": "log", "_PID": ["process", "pid"], "_CMDLINE": "process", "_COMM": "cmd"}
    fields_strip_underscores true
    fields_lowercase true
  </entry>
</source>
```
    

## Reference
