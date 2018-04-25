---
title: Google Stackdriver Monitoring
---

## Google Stackdriver Monitoring

* Uptime check
    * HTTP, TCP, HTTPSのcheckができる
    * resoruce typeは
        * URL, instance, App Engine, Elastic Load Balancer
    * respocenのtextに特定の文字列が含まれているかのcheckができる

## Metrics
* [GCP Metrics List  |  Stackdriver Monitoring  |  Google Cloud](https://cloud.google.com/monitoring/api/metrics_gcp)
* [Metrics, Time Series, and Resources  |  Stackdriver Monitoring  |  Google Cloud](https://cloud.google.com/monitoring/api/v3/metrics)


* Metrics types
    * label
        * labelがある場合は、descriptionに記載されている
* MetricKind
    * [REST Resource: projects.metricDescriptors  |  Stackdriver Monitoring  |  Google Cloud](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)
    * DELTA
        * metricは前回記録された値からの差分
    * GAUGE
        * An instantaneous measurement of a value.
    * CUMULATIVE
        * start tiemが同じで、endtimeが増えていく
* ValueType
    * DISTRIBUTION
        * [TimeSeries  |  Stackdriver Monitoring  |  Google Cloud](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Distribution)
    * MONEY


* bigquery
    * qyert/count
        * in flight query
    * query/execution_times 
        * 

## Custom metrics

* Naming
    * [Structure of Metric Types  |  Stackdriver Monitoring  |  Google Cloud](https://cloud.google.com/monitoring/api/v3/metrics-details#label_names)
    * metric type
    * Custom metricsのNamingはprojectで一意である必要がある
    * `custom.googleapis.com/cpu_utilization`
    * `type`としてlabelされている
* Resouce name
    * gcpで一意な名前を持つ`projects/[PROJECT_ID]/metricDescriptors/[METRIC_TYPE]`
    * `projects/my-project-id/metricDescriptors/custom.googleapis.com/cpu_utilization`
    * REST APIで使う場合は `projects/my-project-id/metricDescriptors/custom.googleapis.com%2Fcpu_utilization`
    * `name`としてlabelされている
        


## Tutorial
* [Using Stackdriver's monitoring and logging to get better visibility into your application's health](https://codelabs.developers.google.com/codelabs/cloud-stackdriver-getting-started/index.html?index=..%2F..%2Findex#0)

Install logging agent

```
curl -sS https://dl.google.com/cloudagents/install-logging-agent.sh | sudo bash
```

## GCE/GKE nodeのdiskのmonitoring
* metric typeを`volume usage`で調べる
* diskのmetricはdisk write/readしかない

## Monitoring Kubernetes
* [Google StackdriverでKubernetesのモニタリングに挑戦してみよう (1/3)：CodeZine（コードジン）](https://codezine.jp/article/detail/10644)
* [GKEでは StackDriver Loggingに どうやってログを送っているか // Speaker Deck](https://speakerdeck.com/ytakky2014/gkedeha-stackdriver-loggingni-douyatuteroguwosong-tuteiruka)

* GKEのコンテナの指標
    * CPU使用率
    * ディスク使用率
    * ページフォールト（メジャー）
    * ページフォールト（マイナー）
    * メモリー消費量
    * ノード（GCEのVM）のメトリクス
* CPU使用率
    * ディスク読み込みI/O
    * ディスク書き込みI/O
    * ネットワーク インバウンド トラフィック
    * ネットワーク アウトバウンド トラフィック


* Disk capacity
    * `device_name` でattachしているvolumeの使用量がとれる
    * aggregation
        * sum
    * group by
        * device_name
    * filter
        * device_name: `Volume: volume-name-`
        * device_name: `cluster-name: cluster-name-`
* Disk usage
    * `device_name` でattachしているvolumeの使用量がとれる
    * aggregation
        * sum
    * group by
        * device_name
    * filter
        * device_name: `Volume: volume-name-`
        * device_name: `cluster-name: cluster-name-`

## Pricing
June 30, 2018以降の料金
premium tierでなくてもalert,notificationが使えるようになる。

* Stackdriver Monitoring data
    * free
        * All GCP metrics
        * Non-GCP metrics `< 150MB`
    * price
        * Non-GCP metrics
            * 0.2580USD/MB: 150-100,000MB
            * 0.1510USD/MB: 100,000-250,000MB
            * 0.0610USD/MB: >250,000 MB
* Stackdriver Monitoring API calls
    * free
        * First 1 million API calls
    * price
        * 0.01USD/1,000 API calls

## Reference
* [Stackdriver Monitoring Documentation  |  Stackdriver Monitoring  |  Google Cloud Platform](https://cloud.google.com/monitoring/docs/)
