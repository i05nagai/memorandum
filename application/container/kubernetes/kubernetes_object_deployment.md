---
title: Kubernetes Object Deployment
---

## Kubernetes Object Deployment
* [Deployments | Kubernetes](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

Controllerの1つ。
PodとRelicaSetに対するupdate方法を記載する。
Rolling updateをする場合は、`Deployment`を使う。
Deploymentが作成する、`ReplicaSet`は直接変更しない。


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
