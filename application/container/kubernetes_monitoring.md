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



## Reference
