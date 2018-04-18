---
title: Fluentd Output
---

## Fluentd Output

### out_copy
store句に複数のコピー先をかける。

* `<store>`
    * storeの中に

### prometheus
* [fluent/fluent-plugin-prometheus: A fluent plugin that collects metrics and exposes for Prometheus.](https://github.com/fluent/fluent-plugin-prometheus)

```
<source>
  @type prometheus
</source>
```

* bind
    * default `0.0.0.0`
* port
    * listen port. default `24231`
* metrics_path
    * metrics HTTP endpoint
    * default `/metrics`

### out_google_cloud
* [GoogleCloudPlatform/fluent-plugin-google-cloud: Plugin for Fluentd that sends logs to the Google Cloud Platform's log ingestion API.](https://github.com/GoogleCloudPlatform/fluent-plugin-google-cloud)

```
<match **>
  type google_cloud
</match>
```

google application default credentialsを使って、logをGCPにおくる。


* buffer_type file
    * Set the buffer type to file to improve the reliability and reduce the memory consumption
* buffer_path /var/log/fluentd-buffers/kubernetes.containers.buffer
    * Set queue_full action to block because we want to pause gracefully in case of the off-the-limits load instead of throwing an exception
* buffer_queue_full_action block
    * Set the chunk limit conservatively to avoid exceeding the GCL limit of 10MiB per write request.
* buffer_chunk_limit 2M
    * Cap the combined memory usage of this buffer and the one below to 2MiB/chunk * (6 + 2) chunks = 16 MiB
* buffer_queue_limit 6
    * Never wait more than 5 seconds before flushing logs in the non-error case.
* flush_interval 5s
    * Never wait longer than 30 seconds between retries.
* max_retry_wait 30
    * Disable the limit on the number of retries (retry forever).
* disable_retry_limit
    * Use multiple threads for processing.
* num_threads 2


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
