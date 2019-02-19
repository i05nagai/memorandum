---
title: Kubernetes Logging
---

## Kubernetes Logging
`/var/log/pods` にpodsのlogが出力される。
hostsのdockerの`/var/log/containers/`のcontianerのlogへのsymbolic link

* Podのstdout/stderrの出力はcontainer engineがlogging driverによって処理する。
* docker json loginはmulti-lineの出力に対応してないので、multi-line messageはlogging agent levelで処理する。
* kubernetesはnodeのlogrotateの責任を持たないが、`kube-up.sh`でkubernetesをdeployした場合は、logrotateの設定がされる。
* dockerの`log-opt`でlogrotateの設定も可能、GCPのCOSはこの設定を使っている。
* `kubectl logs`はlog fileから直接logを読む
* systemdが動いているnodeでは、journaldに書き込まれる
    * kubernetes scheudler
    * kube-proxy
    * kubelet
    * container runtine (e.g. Docker)
* systemdが動いていない場合は、`/var/log`


Cluster level logging

kubernetesはcluster level logging の機能は提供してないが以下の方法がある

* (1) Use a node-level logging agent that runs on every node.
    * daemonsetでnodeにlogging agentをおく
        * podsをおく、nodeのnative processを使う方法もあるが、非推奨
    * GKEはfluentd
* (2) Include a dedicated sidecar container for logging in an application pod.
    * streaming side car containerをapplication containerに同居させる
* (3) Push logs directly to a backend from within an application.



## Monitoring and Logging
* [Core metrics pipeline | Kubernetes](https://kubernetes.io/docs/tasks/debug-application-cluster/core-metrics-pipeline/)

* [Logging Using Stackdriver | Kubernetes](https://kubernetes.io/docs/tasks/debug-application-cluster/logging-stackdriver/)
    * stackdriverでのlogは、standard output, standard errorのlogだけ
    * fileに出力されるlogなどが必要な場合は sidecarを使う

## GKE
* Nodeのcontainer engineはdocker, logging driverはjson-file


## Reference
* [Logging Architecture | Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
