---
title: Fluentd
---

## Fluentd

## Config

### source
input pluginを指定する。
sourceはいくらでも指定できる。
defaultのinput pluignとして、`forward`と`http`が利用できる。

* type
    * forward
        * TCP packetsをうけつる
        * portでうけつけるport番号を指定する
    * http
        * fluentdがhttpアクセスをうけつけ
        * portでうけつけるport番号を指定する

```
<source>
    type forward
    port 2323
</source>
```


tcpの場合は、json messageにtagを含めておくる。

```
stream:
  message...

message:
  [tag, time, record]
  or
  [tag, [[time,record], [time,record], ...]]

example:
  ["myapp.access", 1308466941, {"a":1}]["myapp.messages", 1308466942, {"b":2}]
  ["myapp.access", [[1308466941, {"a":1}], [1308466942, {"b":2}]]]
```

httpの場合は、URLのpathの部分がtagとなる。


### match
他のsystemにoutputする。
output pluginとも呼ばれる。

tagにmatchしたsourceからの入力のみ出力する。

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

* Match Order
    * 複数にmatchする場合は最初にmatchしたものが使われる
    * 複数に贈りたい場合は、`out_copy` pluginを使う必要がある

## Plugins
sourceでinput pluginを指定する。
matchでoutput pluiginを指定する。

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

### out_kinesis_stream
* [awslabs/aws-fluent-plugin-kinesis: Fluent Plugin for Amazon Kinesis](https://github.com/awslabs/aws-fluent-plugin-kinesis#configuration-kinesis_streams)

以前は`kinesis` pluginだったがdeprecatedになっていくつかのpluginにわかれた`kinesis_stream`になった。

```
<match your_tag>
  @type kinesis_streams
  region us-east-1
  stream_name your_stream
  partition_key key  # Otherwise, use random partition key
</match>
```

* `stream_name`
    * kinesisのstreamの名前
* `region`
    * AWSのkinesiのreagionを文字列で指定
* `partition_key`
    * JSON objectが分割用のkeyを指定をする
    * defaultはnilでnilだとrandomなKeyを割り当てて分割する
    * このkeyのMD5 hashもとにshardに分散する


### out_kinesis_producer
* [awslabs/aws-fluent-plugin-kinesis: Fluent Plugin for Amazon Kinesis](https://github.com/awslabs/aws-fluent-plugin-kinesis)


### kinesis_firehose
* [awslabs/aws-fluent-plugin-kinesis: Fluent Plugin for Amazon Kinesis](https://github.com/awslabs/aws-fluent-plugin-kinesis)

```
<match your_tag>
  @type kinesis_firehose
  region us-east-1
  delivery_stream_name your_stream
</match>
```

* `delivery_stream_name`
    * 
* `region`


throughputをあげるための設定の例。

```
  flush_interval 1
  buffer_chunk_limit 1m
  try_flush_interval 0.1
  queued_chunk_flush_interval 0.01
  num_threads 15
```

### out_rewrite_tag_filter
* [fluent/fluent-plugin-rewrite-tag-filter: Fluentd Output filter plugin to rewrite tags that matches specified attribute.](https://github.com/fluent/fluent-plugin-rewrite-tag-filter)

Apache httpの`mode_rewrite`のようにURLの下記かえを行う

```
<match td.apache.access>
  @type rewrite_tag_filter
  capitalize_regex_backreference yes
  rewriterule1 path   \.(gif|jpe?g|png|pdf|zip)$  clear
  rewriterule2 status !^200$                      clear
  rewriterule3 domain !^.+\.com$                  clear
  rewriterule4 domain ^maps\.example\.com$        site.ExampleMaps
  rewriterule5 domain ^news\.example\.com$        site.ExampleNews
  rewriterule6 domain ^(mail)\.(example)\.com$    site.$2$1
  rewriterule7 domain .+                          site.unmatched
</match>
```

書き換えのルール定義は以下。

```
rewriterule<num> <attribute> <regex_pattern> <new_tag>
```

* `<num>`
    * ruleの番号
* `<attribute>`
    * path
        * URLのhost以降のpathの部分の書き換え
    * domain
        * URLのdomain部分の書き換え
    * status
        * http statusの書き換え
* `<regex_pattern>`
    * 書き換え対象の正規表現
* `<new_tag>`
    * 書き換え後の文字列
    * マクロみたいなものも一部使える


## Reference
* [Configuration File Syntax | Fluentd](http://docs.fluentd.org/v0.12/articles/config-file#1-ldquosourcerdquo-where-all-the-data-come-from)
