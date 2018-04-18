---
title: Google Kubernetes Engine Logging
---

## Google Kubernetes Engine Logging
Collecting Docker Log Files with Fluentd and sending to GCP.

* kubernetesの基本的なLoggingは同じ
    * heapster->kubelet->cadvisor
* fluentdでjournaldからcontainerのlogを送っている


## fluentd
* [Logging Using Stackdriver | Kubernetes](https://kubernetes.io/docs/tasks/debug-application-cluster/logging-stackdriver/)
* [Customizing Stackdriver Logs for Kubernetes Engine with Fluentd  |  Solutions  |  Google Cloud](https://cloud.google.com/solutions/customizing-stackdriver-logs-fluentd)
* [GoogleCloudPlatform/container-engine-customize-fluentd](https://github.com/GoogleCloudPlatform/container-engine-customize-fluentd)

* Dockerimages
    * [k8s-stackdriver/fluentd-gcp-image GoogleCloudPlatform/k8s-stackdriver](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/fluentd-gcp-image)
        * dockerfileが作られているrepository
    * DaemonSetでfluentdが動作しており、stackdriverにlogを送っている。
    * `/etc/fluent/config.d`にfluentdの設定をおけば動作するようにDocker imageが作られている。

* deployment
    * [kubernetes/cluster/addons/fluentd-gcp at master · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/fluentd-gcp)
        * addonとして定義されたfluentdkubernetesのdeploymentsなど
    * v1.10以降ではfluentdは自動でscaleするようになっている
        *  large volume of logs (i.e. over 100kB/s)を送る時 fluentd-gcp to fail with OutOfMemory errorsで落ちる
    * `fluentd-gcp-config-v?.?.?`の名前のconfig mapが`/etc/fluent/config.d`にvolumeとしてつけられている。
        * `containers.input.conf`
        * `monitoring.conf`
        * `output.conf`
        * `system.input.conf`
    * config-mapのsampleは以下にある
        * [container-engine-customize-fluentd/kubernetes at master · GoogleCloudPlatform/container-engine-customize-fluentd](https://github.com/GoogleCloudPlatform/container-engine-customize-fluentd/tree/master/kubernetes)

動いているfluentdのconfigmapを取得

```
$ kubectl get configmap --namespace kube-system
$ kubectl get configmap fluentd-gcp-config-v?.?.? -o yaml > fluentd-gcp-config.yml
```

Loggingの処理のながれはcommentに詳しく書かれている
[container-engine-customize-fluentd/fluentd-configmap.yaml at master · GoogleCloudPlatform/container-engine-customize-fluentd](https://github.com/GoogleCloudPlatform/container-engine-customize-fluentd/blob/master/kubernetes/fluentd-configmap.yaml)

* hostの`/var/lib/docker/containers/997599971ee6366d4a5920d25b79286ad45ff37a74494f262e3bc98d909d0a7b-json.log`にlogに出力される
    * filenameがdocker ID
* kubernetesはこのlog fileへのsymbolic linkを`/var/log/containers`にpodとcontainerの名前とともにはる
    * `/var/log/containers/synthetic-logger-0.25lps-pod_default-synth-lgr-997599971ee6366d4a5920d25b79286ad45ff37a74494f262e3bc98d909d0a7b.log`
    * -> `/var/lib/docker/containers/997599971ee6366d4a5920d25b79286ad45ff37a74494f262e3bc98d909d0a7b/997599971ee6366d4a5920d25b79286ad45ff37a74494f262e3bc98d909d0a7b-json.log`
* fluentdは`/var/log`をmountしているので、このlog fileからtagを以下のように作る
    * `var.log.containers.synthetic-logger-0.25lps-pod_default-synth-lgr-997599971ee6366d4a5920d25b79286ad45ff37a74494f262e3bc98d909d0a7b.log`
* record reformerが`var.log.containers`を消す
* `kubernetes.synthetic-logger-0.25lps-pod_default-synth-lgr`をtagにprefixとしてつける


```
<pod-name>_<namespace>_<container-name>-<container-id>.log
```

## prometheus-to-sd
* [k8s-stackdriver/prometheus-to-sd at master · GoogleCloudPlatform/k8s-stackdriver](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/prometheus-to-sd)

prometheus-to-sd is a simple component that can scrape metrics stored in prometheus text format from one or multiple components and push them to the Stackdriver. Main requirement: k8s cluster should run on GCE or GKE.

## Reference
* [GoogleCloudPlatform/k8s-stackdriver](https://github.com/GoogleCloudPlatform/k8s-stackdriver)
