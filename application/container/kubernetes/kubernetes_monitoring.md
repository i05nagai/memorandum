---
title: Kubernetes Monitoring
---

## Kubernetes Monitoring

## Kubernetes
* [Monitoring Kubernetes performance metrics](https://www.datadoghq.com/blog/monitoring-kubernetes-performance-metrics/#toc-heapster-vs-native-container-metrics)

* 各nodeで、cAdviserがconitanerのmetricsを集めるj
* Heapster がkubletを通してqueryをなげる

Heapster v.s. native container metrics

* docker/rktなどのcontainer engineのMericsとkubernetesのMetricsの値は異なる
* kubernetesはcgroup fileを直接みずHeapster経由でmetricsを取得する
* Heapsterは`housekeeping interval`の間隔でmetricsを収集する点が 

key performance metrics for monitoring

* CPU and memory usage are likely the first resource metrics you will want to review.
    * Kubernetesよりdockerの提供するmetricsをみるべき
    * `kube-state-metrics`
        * `kube_node_status_capacity_cpu_cores`
        * `kube_node_status_capacity_memory_bytes`
    * podのCPU requestとlimitの合計はmonitoringする
    * request の合計 > limitの合計であればresourceを効率的につかえている
    * podのrequest/limitはmonitoringしながら調整する
* disk
    * volumeではなくdiskの容量を監視する
    * diskの容量の80%を超えたらalertをだすなどする
    * i/o read/write bytesを監視するlatencyのcheckに使える

* kubernetesのmonitoringとtraditional systemのmonitoringの違い
    * tag/labelが必須
    * monitoringするcomponemntsが多い
* labelの例
    * Frontend/Backend
    * Application (website, mobile app, database, cache…)
    * Environment (prod, staging, dev…)
    * Team
    * Version
* kubernetesのbasic informati
    * pod_id, pod_name, pod_namespace,
    * containers (container_base_image, container_name),
    * nodes (host_id, hostname)
    * as well as namespace
    * service name
    * deployment name
* monitoringの仕組み
    * Heapsterがmetricsの収集をしている
    * each nodeでcAdviserがnodeのkubletを通してHeapsterにmetricsを送る
    * cAdviserがcontainer, cAdviser自身とdocker daemonのCPU, memory, file system, networkを計測している
    * ![aaa](https://datadog-prod.imgix.net/img/blog/how-to-collect-and-graph-kubernetes-metrics/kubernetes-heapster.png?fit=max)

## Reference
