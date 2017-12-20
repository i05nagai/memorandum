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


## Reference
* [What is the correct pronunciation of Kubernetes in English? · Issue #44308 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/44308)

