---
title: Kubernetes API
---

## Kubernetes API
* [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#-strong-api-overview-strong-)

APIの引数をyaml/jsonで記載する。
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



* `PodTemplateSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#podtemplatespec-v1-core)
    * `metadata `
    * `spec`
        * `PodSpec`
* `PodSpec`
    * `containers`
        * array of `Container`
    * `volumes`
        * array of `Volume`
* `Volume`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#volume-v1-core)
    * dockerのvolume containerやvolume driverに近い
    * Podごとに定義
    * `name`
        * `volumeMount`などでreferするvolumeの名前
    * `secret`
    * `gitRepo`
    * `hostPath`
        * Nodeのpath
        * developでhostのfileをMountする場合に釣っ買う
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
        * `IfNotPresent`
        * `Always`
    * `lifecycle`
    * `livenessProbe`
    * `name`
    * `securityContext`
        * `SecurityContext`
    * `volumeMounts`
        * array of `VolumeMount`
* `SecurityContext`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#securitycontext-v1-core)
    * `runAsUser`
        * containerのprcess実行時のUID
* `VolumeMount`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#volumemount-v1-core)
    * `mountPath`
        * container内のpath
        * `:`は含めない
    * `mountPropagation`
        * 将来的には消える
    * `name`
        * volumeの名前に一致
    * `readOnly`
        * boolean
* `ObjectMeta`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#objectmeta-v1-meta)
    * `name`
        * namespace内でunique
    * `namespace`
        * emptyは`default`
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
