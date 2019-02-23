---
title: autoscaler
---

## autoscaler

* Cluster autoscaler
* Vertical Pod autoscaler
* Addon Resizer

## addon-resizer
* [autoscaler/addon-resizer at master · kubernetes/autoscaler](https://github.com/kubernetes/autoscaler/tree/master/addon-resizer)
    * `gcr.io/google_containers/addon-resizer:1.8.1`

pod_nannyのbinaryが使われている。

## pod_nanny

```
/pod_nanny
```

* `--config-dir string`
    * Path of configuration containing base resource requirements.
    * default "MISSING"
* `--container string`
    * The name of the container to watch. This defaults to the nanny itself.
    * default "pod-nanny"
* `--cpu string`
    * The base CPU resource requirement.
* `--deployment string`
    * The name of the deployment being monitored. This is required.
* `--estimator string`
    * The estimator to use. Currently supported: linear, exponential
    * default "linear"
* `--extra-cpu string`
    * The amount of CPU to add per node.
* `--extra-memory string`
    * The amount of memory to add per node.
* `--extra-storage string`
    * The amount of storage to add per node.
    * default "0Gi"
* `--memory string`
    * The base memory resource requirement.
* `--minClusterSize uint`
    * The smallest number of nodes resources will be scaled to.
    * Must be > 1. This flag is used only when an exponential estimator is used.
    * default 16
* `--namespace string`
    * The namespace of the ward. This defaults to the nanny pod's own namespace.
* `--pod string`
    * The name of the pod to watch. This defaults to the nanny's own pod.
* `--poll-period int`
    * The time, in milliseconds, to poll the dependent container. 
    * default 10000
* `--storage string`
    * The base storage resource requirement.
    * default "MISSING"
* `--threshold int`
    * A number between 0-100. The dependent's resources are rewritten when they deviate from expected by more than threshold.


## Reference
* https://github.com/kubernetes/autoscaler
