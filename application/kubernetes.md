---
title: Kubernetes
---

## Kubernetes

## Concepts

* Pod
    * Podはclusterで動いているprocessの表現
    * 1つ以上のcontainerで構成される
    * 以下のresourceはpod内でshare
        * storage resource
        * unique network IP
            * pod内のcontainerはlocalhostでやりとりする
    * Pods that run a single container.
        * most common
    * Pods that run multiple containers that need to work together
        * resourceを共有する必要があるような場合
    * [Kubernetes: The Distributed System ToolKit: Patterns for Composite Containers](http://blog.kubernetes.io/2015/06/the-distributed-system-toolkit-patterns.html)
        * Sidecar containers
            * Main: Node.js
            * Sidecar: git synchronizerでfilesystemをgit repositoryに動機
            * Sidecarに分けることで他のwebserverでも使える
        * Ambassador containers
        * Adapter containers
            * containerのoutputの標準化をする
            * 複数のserviceをmonitoringする際にadapter containerがoutputのwrapをする
    * [Kubernetes: Container Design Patterns](http://blog.kubernetes.io/2016/06/container-design-patterns.html)
    * NodeでschedulingされているPodがfailした場合Podはdeleteされる

* Namespace

### Nodes


### Service


### ReplicaSet
Controllerの1つ。

### StatefulSet
以下の1つ以上が必要な場合に役に立つ。

* Stable, unique network identifiers.
* Stable, persistent storage.
* Ordered, graceful deployment and scaling.
* Ordered, graceful deletion and termination.
* Ordered, automated rolling updates.

StableはPod schedulingによる一貫性と同じ意味。

### Deployment
Controllerの1つ。

Rolling updateをする場合は、`Deployment`を使う。

### DaemonSet
Controllerの1つ。
全てかいくつかのNodeで実行されることが保証されるPod

* `glusterd`, `ceph`などのcluster storage daemonをNodeで実行
* `fluentd`, `logstash`など
* Prometheus Node explorerなどのmonitoring daemon

DaemonSetと代替可能なもの

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

### Volumes
* [Volumes | Kubernetes](https://kubernetes.io/docs/concepts/storage/volumes/)



## CLI

## API
* [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#-strong-api-overview-strong-)

APIの引数をyamlで記載する。
以下のyamlの場合。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: memory-demo
spec:
  containers:
  - name: memory-demo-ctr
    image: vish/stress
    resources:
      limits:
        memory: "200Mi"
      requests:
        memory: "100Mi"
    args:
    - -mem-total
    - 150Mi
    - -mem-alloc-size
    - 10Mi
    - -mem-alloc-sleep
    - 1s
```


* [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#pod-v1-core)に引数の仕様がのっている
    * `Pod`に対するAPIの`v1`で、`metadata`の引数が`name=memory-demo`になっている
    * `spec`
        * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#podspec-v1-core)
        * PodSpecの引数をみる
        * `containers`
            * `Container`
* `Container`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#container-v1-core)
    * `args`
        * argument to the entrypoint
        * `$(VAR_NAME)`はcontainerの環境で評価される
    * `command`
    * `env`
    * `envFrom`
    * `image`
    * `imagePullPolicy`
    * `lifecycle`
    * `livenessProbe`
    * `name`
    * `volumeMounts`
        * array of `VolumeMount`
* `VolumeMount`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#volumemount-v1-core)
    * `mountPath`
        * container内のpath
        * `:`は含めない
    * `mountPropagation`
        * 将来的には消える
    * `name`
        * volumeの名前に一致
* `ObjectMeta`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#objectmeta-v1-meta)
    * `name`
        * namespace内でunique
    * `namespace`
        * emptyは`default`
* `PodSpec`
    * `volumes`
        * Volume Array
* `PodTemplateSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#podtemplatespec-v1-core)
    * `metadata `
    * `spec`
        * `PodSpec`
* `Deployment`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#deployment-v1-apps)
    * `apiVersion`
    * `kind`
        * Deployment
    * `metadata`
    * `spec`
        * `DeploymentSpec`
    * `satus`
        * `DeploymentStatus`
* `DeploymentSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#deploymentspec-v1-apps)
    * `replicas`
        * number of pods
        * defaultは1
    * `template`
        * `PodTemplateSpec`
* `DeploymentStatus`
* `Volume`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#volume-v1-core)
    * `hostPath`
        * host machineのfile/directory
        * 多くのcontainerで不要
    * `name`
        * Pod内でunique, `DNS_LABEL`
* `Service`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#service-v1-core)
    * `apiVersion `
    * `kind`
    * `metadata`
    * `spec`
        * `ServiceSpec`
    * `status`
* `ServiceSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#servicespec-v1-core)
    * `ports`
        * ServicePort
    * `selector`
    * `type`
        * `ExternalName`
        * `ClusterIP`
        * `NodePort`
        * `LoadBalancer`
* `ServicePort`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#serviceport-v1-core)
    * `name`
        * DNS_LABEL
    * `nodePort`
    * `port`
        * serviceがexposeするport
    * `protocol`
        * TCP/UDP
        * defaultはTCP
    * `targetPort`
* `ReplicaSet`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#replicaset-v1-apps)
    * `apiVersion`
    * `kind`
        * `ReplicaSet`
    * metadata
    * `spec`
        * `ReplicaSetSpec`
    * `status`
        * `ReplicaSetStatus`
* `ReplicaSetSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#replicasetspec-v1-apps)
    * `minReadySeconds `
    * `replicas`
    * `selector`
        * `LabelSelector`
    * `template`
        * `PodTemplateSpec`
* `ReplicaSetStatus`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#replicasetstatus-v1-apps)
    * `availableReplicas`
* `LabelSelector`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#labelselector-v1-meta)


## Reference
* [What is the correct pronunciation of Kubernetes in English? · Issue #44308 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/44308)

