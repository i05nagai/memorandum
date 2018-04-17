---
title: DataDog Kubernetes
---

## DataDog Kubernetes
datadogsは基本的に、`kube-state-metrics`からのdataを通して、metricsをo

## Metrics
* [Kubernetes](https://docs.datadoghq.com/integrations/kubernetes/)

datadogがkubernetesから取得できるMetricsの一覧は上にある通り。
`Kubernetes State`とついているものは、`kube-state-metrics`のdeployが必要。

### Log correction
envで `DD_LOGS_ENABLED`をtrueにする。

```
- name: DD_LOGS_ENABLED
    value: "true"
```

```
    (...)
      volumeMounts:
        (...)
        - name: pointerdir
            mountPath: /opt/datadog-agent/run
    (...)
    volumes:
      (...)
      - hostPath:
            path: /opt/datadog-agent/run
          name: pointerdir
    (...)
```

### Event collections
kubenertes API serverのeventをとれる。
取得できるeventの一覧は以下の通り。

* Backoff
* Conflict
* Delete
* DeletingAllPods
* Didn’t have enough resource
* Error
* Failed
* FailedCreate
* FailedDelete
* FailedMount
* FailedSync
* Failedvalidation
* FreeDiskSpaceFailed
* HostPortConflict
* InsufficientFreeCPU
* InsufficientFreeMemory
* InvalidDiskCapacity
* Killing
* KubeletsetupFailed
* NodeNotReady
* NodeoutofDisk
* OutofDisk
* Rebooted
* TerminatedAllPods
* Unable
* Unhealthy

## Reference
* [Kubernetes](https://docs.datadoghq.com/agent/basic_agent_usage/kubernetes/)
