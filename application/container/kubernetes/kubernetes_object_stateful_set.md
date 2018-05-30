---
title: Kuberbetes Object StatefulSet
---

## Kuberbetes Object StatefulSet
* [StatefulSet Basics - Kubernetes](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)

以下の1つ以上必要な場合に役に立つ。

* Stable
    StableはPod schedulingによる一貫性と同じ意味。
    * unique network identifiers.
    * persistent storage.
* Ordered
    * graceful deployment and scaling.
    * graceful deletion and termination.
    * automated rolling updates.

persistent storageをread and writeでmountする場合は基本的に使う。
writableのMountは1つのcontainerに限るので、deploymentではscale/rolling updateできない。


```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 2
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
        image: k8s.gcr.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```


## Reference
