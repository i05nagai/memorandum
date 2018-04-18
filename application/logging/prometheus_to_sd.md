---
title: prometheus-to-sd
---

## prometheus-to-sd
prometheus text formatで保存されているmetricをStrackDriverにexportする。


## Kubernetes
* [k8s-stackdriver/prometheus-to-sd-kube-state-metrics.yaml at master · GoogleCloudPlatform/k8s-stackdriver](https://github.com/GoogleCloudPlatform/k8s-stackdriver/blob/master/prometheus-to-sd/kubernetes/prometheus-to-sd-kube-state-metrics.yaml)

## CLI

```
/monitor
--stackdriver-prefix=custom.googleapis.com
--source=kube-state-metrics:http://localhost:8080
--pod-id=$(POD_NAME)
--namespace-id=$(POD_NAMESPACE)
```

* target-host
    * default localhost
    * The monitored component's hostname. DEPRECATED: Use --source instead.
* target-port
    * default 80
    * The monitored component's port. DEPRECATED: Use --source instead.
* component
    * The monitored target's name. DEPRECATED: Use --source instead.
* stackdriver-prefix
    * default container.googleapis.com/master
    * Prefix that is appended to every metric. (default "container.googleapis.com/master")
* whitelisted-metrics
    * Comma-separated list of whitelisted metrics. If empty all metrics will be exported. DEPRECATED: Use --source instead.
* auto-whitelist-metrics
    * default false
    * If component has no whitelisted metrics, prometheus-to-sd will fetch them from Stackdriver.
* metrics-resolution
    * default 60 sec
    * The resolution at which prometheus-to-sd will scrape the component for metrics.
* metric-descriptors-resolution
    * default 10 min
    * The resolution at which prometheus-to-sd will scrape metric descriptors from Stackdriver.
* api-override
    * The stackdriver API endpoint to override the default one used (which is prod).
* -source value
    * uri
    * source(s) to watch in [component-name]:http://host:port?whitelisted=a,b,c format
    * sourceは`heapster`のURI
* -pod-id string
    * default machine
    * Name of the pod in which monitored component is running.
* namespace-id string
    * Namespace name of the pod in which monitored component is running.
* omit-component-name
    * true
    * If metric name starts with the component name then this substring is removed to keep metric name shorter.
* -port uint
    * default 6061
    * Port on which debug information is exposed.
* -alsologtostderr
    * log to standard error as well as files
* -component string
    * The monitored target's name. DEPRECATED: Use --source instead.
* -log_backtrace_at value
    * when logging hits line file:N, emit a stack trace
* -log_dir string
    * If non-empty, write log files in this directory
* -logtostderr
    * log to standard error instead of files
* -stderrthreshold value
    * logs at or above this threshold go to stderr
* -v value
    * log level for V logs
* -vmodule value
    * comma-separated list of pattern=N settings for file-filtered logging


## Reference
* [k8s-stackdriver/prometheus-to-sd at master · GoogleCloudPlatform/k8s-stackdriver](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/prometheus-to-sd)
