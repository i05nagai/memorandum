---
title: Kubernetes Node
---

## Kubernetes Node
* [Assigning Pods to Nodes | Kubernetes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/)
    * nodeの指定は3種類
    * node selector
    * node affinity
    * inter-pod affinity

kubernetes 1.4からNodeに自動で以下のlabelが付与される。
値はprovider specific.

* kubernetes.io/hostname
* failure-domain.beta.kubernetes.io/zone
* failure-domain.beta.kubernetes.io/region
* beta.kubernetes.io/instance-type
* beta.kubernetes.io/os
* beta.kubernetes.io/arch


**Node selector**

* nodeを指定して、Podに割当ができる
* ndoeにlabelをつけられるので、labelで選択する
* PodsSpecにNodeのlabelを指定する。


```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    disktype: ssd
```


**Node Affinity**

nodeSelectorに似ているが、nodeSelectorより柔軟な表現でNodeの割当ができる。

* `requiredDuringSchedulingIgnoredDuringExecution`
    * hard
    * 割り当てられたNodeに必ずscheduleされる必要がある
    * 実行中の場合は無視する
* `preferredDuringSchedulingIgnoredDuringExecution`
    * soft
    * 割り当てられたNodeがなければ他のnodeで動く

PodSpecに記載する。

* available operator
    *  In, NotIn, Exists, DoesNotExist, Gt, Lt


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/e2e-az-name
            operator: In
            values:
            - e2e-az1
            - e2e-az2
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: another-node-label-key
            operator: In
            values:
            - another-node-label-value
  containers:
  - name: with-node-affinity
    image: k8s.gcr.io/pause:2.0
```

**inter-pod affinity and anti-affinity**

以下の形式でPodのscheduleのruleをかける。

This pod should (or, in the case of anti-affinity, should not) run in an X if that X is already running one or more pods that meet rule Y”

* Y
    * Label selectorで表現
    * namespaceも指定する
* X
    * topology domain like node, rack, cloud provider
    * `topologyKey` で指定
* affinityの計算は軽くないので、schedulerの負荷になるので、数百node程度までで使う
* use cases
    * 全てのpodsを同じnodeに置きたい
    * 全てのpodsを別のnodeに置きたい

## Reference
