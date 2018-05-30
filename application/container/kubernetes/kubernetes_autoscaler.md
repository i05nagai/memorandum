---
title: Kubernetes Autoscaler
---

## Kubernetes Autoscaler
There are two types of autoscaler

* Horizontal Autoscaler
    * change the number of replicas
* Cluaster autoscaler
    * change the number of nodes


## Horizontal Autoscaler
* [Horizontal Pod Autoscaler | Kubernetes](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

cpu負荷などに応じてreplica数を増減させる。
custom metricsにも対応している。
cluster autoscalerはresource limitに応じてpods用のnodeを確保する。

* `--horizontal-pod-autoscaler-sync-period` がcpu loadを計算するperiod
    * default 30 sec
* each podにresource request API経由でCPUなどの情報を取得し、
* Horizontal AUtoscalerは以下の2つの方法でmetricsにaccessする
    * Heapster
        * Heapsterにproxyを通してaccess
        * Heapseterがkube-systemにdeployされている必要がある
    * REST API
        * custom metrics用のAPIがある
        * [community/custom-metrics-api.md at master · kubernetes/community](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md)
* `--horizontal-pod-autoscaler-downscale-delay`
    * downscaleまでのdelay
    * default 5m
* `--horizontal-pod-autoscaler-upscale-delay`
    * upscaleまでのdelay
    * default 3m


kubectlでHorizontal Autoscalerの設定できる。


## Cluster Autoscale
* [autoscaler/FAQ.md at master · kubernetes/autoscaler](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
* [Advanced Scheduling and Pod Affinity/Anti-affinity - Scheduling | Cluster Administration | OpenShift Origin Latest](https://docs.openshift.org/latest/admin_guide/scheduling/pod_affinity.html)

* When does Cluster Autoscaler change the size of a cluster?
    * increasing
        * there are pods that failed to schedule on any of the current nodes due to insufficient resources.
        * adding a node similar to the nodes currently present in the cluster would help.
    * decreasing
        * some nodes are consistently unneeded for a significant amount of time.
        * A node is unneeded when it has low utilization and all of its important pods can be moved elsewhere.
* What types of pods can prevent CA from removing a node?
    * `PodDisruptionBudget`のあるpods
    * `kube-system`のpodで、`"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`が指定されていない
        * are not run on the node by default
        * don't have PDB or their PDB is too restrictive
    * deployment/replicasetなどcontroller objectに作られてないpods
    * Pods with local storage
        * `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`が指定されてない
    * node selectorやpod affinityの制約で動かせない
* What are the Service Level Objectives for Cluster Autoscaler?
    * pending podsをdeployできるnodeを自動で生成することが目的
    * SLOはpodがunschedulableになってから、CAがscale outの命令をnodeに送るまでのlatencyでみることができる
    * latencyはmax20secを目標としているが、実際のtestでは
        * No more than 30 sec latency on small clusters (less than 100 nodes with up to 30 pods each), with the average latency of about 5 sec.
        * No more than 60 sec latency on big clusters (100 to 1000 nodes), with average latency of about 15 sec.
        * またpod affinityがある環境では、上記の3倍以上の時間がかかる
* Autoscaleを使うにはkubernetesのmanifestでcontainerのresourcesを指定しておく必要がある
* Cluster AutoscaleはCPU usage based autoscalerとは違う
    * cluster autoscalerはresourceのrequestに応じてpodsを割り当てるためのnodeを作るのみ
* What are the key best practices for running Cluster Autoscaler?
    * k

特定のnodeのscale downを防ぐ場合は、nodeにannotationに以下をつける。

```
"cluster-autoscaler.kubernetes.io/scale-down-disabled": "true"
```

既存のnodeにつける場合は以下のようにする。

```
kubectl annotate node <nodename> cluster-autoscaler.kubernetes.io/scale-down-disabled=true
```

## Reference
