---
title: Google Kubernetes Engine Monitoring
---

## Google Kubernetes Engine Monitoring
DataDogはがGKEに対応している。


* [Google Container Engine(kubernetes)の監視環境の動向 - まーぽんって誰がつけたの？](http://www.mpon.me/entry/2017/11/09/011423)
* [Monitoring containers on GKE using Google Stackdriver](https://container-solutions.com/monitoring-containers-on-gke-with-google-stackdriver/)
    * [Sidecar pattern | Microsoft Docs](https://docs.microsoft.com/en-us/azure/architecture/patterns/sidecar)
* [ContainerSolutions/stackdriver-gke-custom-metrics: Example python code sending custom container metrics to Stackdriver Monitoring](https://github.com/ContainerSolutions/stackdriver-gke-custom-metrics)
* [Customizing Stackdriver Logs for Kubernetes Engine with Fluentd  |  Solutions  |  Google Cloud](https://cloud.google.com/solutions/customizing-stackdriver-logs-fluentd)

**Best Practice**

* Structured logging
    * Single-line JSON objects written to standard output or standard error will be read into Stackdriver as structured log entries. You can use advanced logs filters to filter logs based on their fields.
* Severities
    * By default, logs written to the standard output are on the INFO level and logs written to the standard error are on the ERROR level. Structured logs can include a severity field, which defines the log's severity. glog-formatted logs' severity is set automatically.
* Exporting to BigQuery
    * You can export logs to external services, such as BigQuery or Pub/Sub, for additional analysis. Logs exported to BigQuery retain their format and structure.
* Alerting
    * You can use logs-based metrics to set up altering policies when Stackdriver Logging logs unexpected behavior.
* Error Reporting
    * You can use Stackdriver Error Reporting to collect errors produced in your clusters.


## With stackdriver

### Container
contianerのmetricsを計測するには、labelをつける

### Instance
instanceのgroupingをする場合は、以下のcommandでclusterにlabelをつける。

```
gcloud beta container clusters update example-cluster --update-labels env=dev,release=stable
```

* clusterにlabelをつけると、clusterに属するnode_poolのInstanceにlabelが追加される
    * default node_poolのinstance
* default以外のnode_poolにinstanceをつける場合は


Stackdriverのinstanceに`Tag`がつくので、Tagを使ってGroupingができる。
clusterのInstanceにはdefaultで`goog-gke-node`というlabelがついているので、これを使ってInstanceにgroupingできる。

naming

* cluster-name: `<prefix>-<env>-<service>-<tier>`
* `<prefix>`
* `<env>`
    * dev/stg/prod/common
* `<service>`
    * core/workflow
        * core is shared with other sevices
* `<tier>`
    * tier is a component or a part of a service
    * e.g. default

Then labels are

* `environment=dev`
* `service=core`
* `tier=default`


## DataDog

## Reference

