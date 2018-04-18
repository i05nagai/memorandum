---
title: Fluentd filter
---

## Fluentd filter
* [Filter Plugin Overview | Fluentd](https://docs.fluentd.org/v0.12/articles/filter-plugin-overview)

event streamsの書き換え
filterはconfigurationを上から下へ実行される。


* filesの値でgrepしてlogをfitlerする
* filedを足す
* filedのdelete/masking

```
<filter foo.bar>
  @type grep
  regexp1 message cool
</filter>
```

以下を満たすものだけconfigurationが適用される。

* `foo.bar`
    * tagにmatch
* `message` fieldが`cool`を含んでいる

### grep

```
<filter foo.bar>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
    tag ${tag}
  </record>
</filter>
```

### parser
* [parser Filter Plugin | Fluentd](https://docs.fluentd.org/v0.12/articles/filter_parser)
    * `in_tail`と同様

```
<filter foo.bar>
  @type parser
  format /^(?<host>[^ ]*) [^ ]* (?<user>[^ ]*) \[(?<time>[^\]]*)\] "(?<method>\S+)(?: +(?<path>[^ ]*) +\S*)?" (?<code>[^ ]*) (?<size>[^ ]*)$/
  time_format %d/%b/%Y:%H:%M:%S %z
  key_name message
</filter>
```

* format
    * required
    * regexp
    * `/^(?<severity>\w)(?<time>\d{4} [^\s]*)\s+(?<pid>\d+)\s+(?<source>[^ \]]+)\] (?<log>.*)/`
* key_name
    * required
    * parseするfield
* time_format
* reserved_data
    * true/false
    * default false
    * falseだと以下のようにparseしたdataだけになる

```
<filter foo.bar>
  @type parser
  format json
  key_name log
  reserve_data true
</filter>
```

trueの場合

```
# input data:  {"key":"value","log":"{\"user\":1,\"num\":2}"}
# output data: {"key":"value","log":"{\"user\":1,\"num\":2}","user":1,"num":2}
```

falseの場合

```
# input data:  {"key":"value","log":"{\"user\":1,\"num\":2}"}
# output data: {"user":1,"num":2}
```

### record-transformer
* [sonots/fluent-plugin-record-reformer: Fluentd plugin to add or replace fields of a event record](https://github.com/sonots/fluent-plugin-record-reformer)

```
<match foo.**>
  type record_reformer
  remove_keys remove_me
  renew_record false
  enable_ruby false
  
  tag reformed.${tag_prefix[-2]}
  <record>
    hostname ${hostname}
    input_tag ${tag}
    last_tag ${tag_parts[-1]}
    message ${record['message']}, yay!
  </record>
</match>
```

* remove_keys
    * comma separated deleted field
* renew_record
    * defualt false
    * input recordsをextendせずに新しくrecordをつくる
* renew_time_key
* enable_ruby
    * placeolderにrubyのcodeを使う
* auto_typecast
* placeholders
    * `${record["key"]}`
    * `${hostname}`
    * `${tag}`
    * `${tags[N]}`
        * obsolete
    * `${tag_parts[N]}`
    * `${tag_prefix[N]}`
        * dot seprated prefix

input

```
foo.bar {
  "remove_me":"bar",
  "not_remove_me":"bar",
  "message":"Hello world!"
}
```

output

```
reformed.foo {
  "not_remove_me":"bar",
  "hostname":"YOUR_HOSTNAME",
  "input_tag":"foo.bar",
  "last_tag":"bar",
  "message":"Hello world!, yay!",
}
```

### filter_stdout



## Reference
