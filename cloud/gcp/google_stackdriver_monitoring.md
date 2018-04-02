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


## Reference
* [Stackdriver Monitoring Documentation  |  Stackdriver Monitoring  |  Google Cloud Platform](https://cloud.google.com/monitoring/docs/)
