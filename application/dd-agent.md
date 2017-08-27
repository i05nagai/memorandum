---
title: dd-agent
---

## dd-agent
DataDog のagent

## config
* [Writing an Agent Check](https://docs.datadoghq.com/guides/agent_checks/#configuration)
* [サービスチェック機能の設定方法 (イベントの送信)](https://docs.datadoghq.com/ja/guides/services_checks/)

場所は以下のいずれか。

* Datadog Agent の設定ファイルの保存先
    * `/etc/dd-agent/datadog.conf`
* インストールしたIntegrations の設定ファイルの保存先
    * `/etc/dd-agent/conf.d/`

設定ファイルのtemplateがdefaultでinstallされる。

* [dd-agent/datadog.conf.example at master · DataDog/dd-agent](https://github.com/DataDog/dd-agent/blob/master/datadog.conf.example)


* init_config
* instances
    * instances セクションには、チェックを実施するケースの詳細を記述していきます。
    * name (必須): すべてのTCP のチェック名を通して、一意である必要があります。
    * host (必須): 監視したいホスト名又は、IP (v4 or v6) アドレス。
    * port (必須): サービスチェックが接続するポート番号。
    * timeout (オプション): TCP リクエストのタイムアウト時間です。デフォルト値は10秒。リクエストのタイムアウトが発生した場合、そのサービスは停止していると見なされます。
    * notify (オプション): init_config セクションで指定した内容を、変更するための通知先リストです。

## Integration
integrationごとに設定ファイル`yaml`形式で記述する。
設定ファイルの名前が決まっているので、datadogのwebsiteで確認する。

* [Get Started with Datadog](https://docs.datadoghq.com/integrations/)

### NTP
* [Datadog-NTP Check Integration](https://docs.datadoghq.com/integrations/ntp/)

### fluentd
* [Datadog-Fluentd Integration](https://docs.datadoghq.com/integrations/fluentd/)

`fluentd.yaml`に記載する。

* monitor_agent_url
    * tagのlistを追加する

```yaml
init_config:

instances:
    # For every instance, you have an `monitor_agent_url`
    # and (optionally) a list of tags.
    -  monitor_agent_url: http://example.com:24220/api/plugins.json
       plugin_ids:
         - plg1
         - plg2
Fluentd YAML example
```

### Diskcheck
* [Datadog-Disk Integration](https://docs.datadoghq.com/integrations/disk/)

* use_mount
    * volumeではなくmountを使うか

### Network
* [Network check](https://docs.datadoghq.com/integrations/network/)

* collect_connection_state
    * `true`にするとTCP connectionのstateをとる
    * `SYS_SENT`, `ESTABLISHED`など
    * excluded_interfaces
        * 除外するnetwokr intefaceを記載

## Reference
* [DataDog/dd-agent: Datadog Agent](https://github.com/DataDog/dd-agent)
* [Agentの基本的な使用方法 (CentOS)](https://docs.datadoghq.com/ja/guides/basic_agent_usage/centos/)
