---
title: kubelet
---

## kubelet
kubletはnode agentとして、各nodeで動いている。
kubeletはcAdvisorからdataを取得する。


## API
* [kubernetes/types.go at master · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/apis/stats/v1alpha1/types.go#L32)
    * 取得しているmetrics
    * kubernetes上はWebUIがport `4194`で動いている


## CLI


## Reference
* [kubelet | Kubernetes](https://kubernetes.io/docs/reference/generated/kubelet/)

