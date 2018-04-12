---
title: Google Kubernetes Engine Logging
---

## Google Kubernetes Engine Logging
Collecting Docker Log Files with Fluentd and sending to GCP.


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

## prometheus-to-sd
* [k8s-stackdriver/prometheus-to-sd at master · GoogleCloudPlatform/k8s-stackdriver](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/prometheus-to-sd)

prometheus-to-sd is a simple component that can scrape metrics stored in prometheus text format from one or multiple components and push them to the Stackdriver. Main requirement: k8s cluster should run on GCE or GKE.

## Reference
* [GoogleCloudPlatform/k8s-stackdriver](https://github.com/GoogleCloudPlatform/k8s-stackdriver)
