---
title: kube-state-metrics
---

## kube-state-metrics
Add-on agent to generate and expose cluster-level metrics.

## Metrics
* [kube-state-metrics/Documentation at master · kubernetes/kube-state-metrics](https://github.com/kubernetes/kube-state-metrics/tree/master/Documentation)

#### kube-state-metrics vs. Heapster
* Heapster
    * CPU and memory utilizationをkubernetes API serverから取得
    * metricsはkubernetesによって作られている
    * format and forward metrics that already exist, and write them into sinks
* kube-state-metrics
    * kubernetesのobject's stateからmetricsの値を取得
    * holds an entire snapshot of Kubernetes state in memory and continuously generates new metrics based off of it but has no responsibility for exporting its metrics anywhere.

## Install
* [kube-state-metrics/kubernetes at master · kubernetes/kube-state-metrics](https://github.com/kubernetes/kube-state-metrics/tree/master/kubernetes)

deployに必要なyamlのsampleは上においてある。
`kubernetes/`をcopyして

```
kubectl apply -f kubernetes
```

を実行すればOK


#### GKE
GKEの場合は、permissionの関係で上記が動かない。

```
$ kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud info | grep Account | cut -d '[' -f 2 | cut -d ']' -f 1)
Clusterrolebinding "cluster-admin-binding" created
```

上記の実行後に上のinstructionを実行する。

## Reference
* [kubernetes/kube-state-metrics: Add-on agent to generate and expose cluster-level metrics.](https://github.com/kubernetes/kube-state-metrics)
