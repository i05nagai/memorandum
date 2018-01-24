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
    * `dnsPolicy`
        * default value `ClusterFirst`
        * `ClusterFirstWithHostNet`
        * `ClusterFirst`
        * `Default`
        * `None`
    * `dnsConfig`
    * `volumes`
        * array of `Volume`
    * `securityContext`
        * `PodSecurityContext`
    * `terminationGracePeriodSeconds`
        * podがgracefullyにterminateする時間
        * 0はすぐ削除
        * defaultは`30`
* `Volume`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#volume-v1-core)
    * dockerのvolume containerやvolume driverに近い
    * Podごとに定義
    * `name`
        * `volumeMount`などでreferするvolumeの名前
    * `secret`
    * `configMap`
        * ConfigMapVolumeSource
    * `gitRepo`
    * `hostPath`
        * Nodeのpath
        * developでhostのfileをMountする場合に使う
* `ConfigMapVolumeSource`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#configmapvolumesource-v1-core)
    * `name`
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
    * `privileged`
        * docker runのprivileged option
* `PodSecurityContext`
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
* `NodePort`
    * 30000-32767の範囲
* `ServicePort`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#serviceport-v1-core)
    * `name`
        * DNS_LABEL
    * `nodePort`
        * serviceが使うnodeのport
    * `port`
        * serviceがexposeするport
    * `protocol`
        * TCP/UDP
        * defaultはTCP
    * `targetPort`
        * 数字がport名
        * stringの場合はpodのcontainer port名を調べる
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
* `Job`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#job-v1-batch)
    * `spec`
    * `status`
* `JobSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#jobspec-v1-batch)
    * `template`
        * `PodTemplateSpec`
    * `parallelism`
    * `backoffLimit`
        * number of retry
        * default 6
* `JobStatus`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#jobstatus-v1-batch)
* `Ingress`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/api-reference/v1.9/#ingress-v1beta1-extensions)
    * spec
        * IngresSpec
    * status
        * IngressStatus
* `IngressSpec`
    * `backend`
        * IngressBackend
    * `rules`
        * array of IngressRule
    * `tls`
        * IngressTLS
* `IngressBackend`
    * serviceName
        * forwardするservice名
    * servicePort
* `IngressRule`
    * host
        * FQDN of network host
    * http
        * HTTPIngressValue
* `HTTPIngressValue`
    * paths
        * array of HTTPIngressPath
* `HTTPIngressPath`
    * backend
        * IngressBackend
    * path
        * /から始まるpath
* `IngressTLS`
    * hosts
    * serviceName


## Reference

