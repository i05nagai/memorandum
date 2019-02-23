---
title: Kubernets Object DaemonSet
---

## Kubernets Object DaemonSet
Controllerの1つ。
全てかいくつかのNodeで実行されることが保証されるPod

* `glusterd`, `ceph`などのcluster storage daemonをNodeで実行
* `fluentd`, `logstash`など
* Prometheus Node explorerなどのmonitoring daemon

#### Alternatives to DaemonSet

* `Init scripts`
    * DaemonSetは各Nodeで、`systemd`, `upstartd`, `init`などで大体することも可能
    * DaemonSetの利点は
        * applicationと同じ方法でDaemonのlogとmonitoringができる
        * Pod templatesで記述できる
        * Resourceの制限つきで利用できる
* Bare Pod
* Static Pod
* Deployment
* Job

#### Update damoesets
https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/#updating-a-daemonset

* if node labels are updated, 
* Update fileds in Daemonsets
    * Pods do not allow all fields to be updated

You can perform a rolling update for Daemonset

* Strategy 
    * `OnDelete`
        * With OnDelete update strategy, after you update a DaemonSet template, new DaemonSet pods will only be created when you manually delete old DaemonSet pods.
    * `RollingUpdate`
        * by default


```
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  name: daemonset-sample
spec:
  updateStrategy:
    type: "RollingUpdate"
    maxUnavailable: 1
    minUnavailable: 0
```

## Kubernetes API

* `apiVersion`
* `kind`
* `metadata`
* `spec`
    * DaemonSetSpec
    * `template`
        * PodTemplateSpec
        * `metadata`
        * `spec`
* `status`

## Reference
