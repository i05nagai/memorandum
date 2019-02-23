---
title: Kubernetes Object Deployment
---

## Kubernetes Object Deployment
* [Deployments | Kubernetes](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

Controllerの1つ。
PodとRelicaSetに対するupdate方法を記載する。
Rolling updateをする場合は、`Deployment`を使う。
Deploymentが作成する、`ReplicaSet`は直接変更しない。


* Proportional scaling
    * https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#proportional-scaling
    * RollingUpdate Deployments support running multiple versions of an application at the same time
    * maxSurge=3, and maxUnavailable=2.
* MaxSurge
    * an optional field that specifies the maximum number of Pods that can be created over the desired number of Pods
    * The value cannot be 0 if MaxUnavailable is 0
    * The absolute number is calculated from the percentage by rounding up
    * For example, when this value is set to 30%,
        * the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new Pods does not exceed 130% of desired Pods
* MaxUnavailable
    * that specifies the maximum number of Pods that can be unavailable during the update process
    * when this value is set to 30%, the old ReplicaSet can be scaled down to 70% of desired Pods immediately when the rolling update starts Once new Pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of Pods available at all times during the update is at least 70% of the desired Pods.
    * desided pod 100 -> 70 available + 30 new pods -> 40 available + 30 new avaiable + 30 new pods -> 10 availabe + 60 new avaiable + 30 new pods -> 90 new avaiable + 10 new pods


## API

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

* `metadata.labels`
    * lables for deployment
* `metadata.name`
    * name of deployment
* `spec.selector`
    * how the Deployment finds which Pods to manage
    * Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment
    * It must match the pod template's labels.
    * Do not overlap labels or selectors with other controllers (including other Deployments and StatefulSets)
* `spec.template.metadata.labels`
    * lables for Pods


## Reference
