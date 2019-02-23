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

#### Determine the request verb
https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb

## API reference

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
        * `SecretVolumeSource`
    * `configMap`
        * `ConfigMapVolumeSource`
    * `gitRepo`
    * `hostPath`
        * Nodeのpath
        * developでhostのfileをMountする場合に使う
* `SecretVolumeSource`
    * `secretName`
    * `items`
        * array of `KeyToPath`
        * 未指定だと、secretのKeyをfile名にvalueをfile contentとしてvolumeを作る
    * `defaultMode`
        * default `0644`
* `KeyToPath`
    * `key`
    * `mode`
        * default: volume default mode
    * `path`
        * `..`はだめ
        * relative/absolute path
* `ConfigMapVolumeSource`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#configmapvolumesource-v1-core)
    * `defaultMode`
        * default `0644`
    * `name`
    * `items`
        * array of `KeyToPath`
        * 未指定だと、secretのKeyをfile名にvalueをfile contentとしてvolumeを作る
    * `optional`
* `Container`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#container-v1-core)
    * `args`
        * argument to the entrypoint
        * `$(VAR_NAME)`はcontainerの環境で評価される
            * refering environment variables
            * parenthesis
    * `command`
        * dockerのentrypoint
        * `$(VAR_NAME)`はcontainerの環境で評価される
            * refering environment variables
            * parenthesis
    * `env`
    * `envFrom`
    * `image`
    * `imagePullPolicy`
        * `IfNotPresent`
        * `Always`
    * `lifecycle`
    * `livenessProbe`
    * `readinessProbe`
        * `Probe`
        * readiness用のurlを設定
        * commandが0ならhealthy, 1ならunhealty
    * `name`
    * `securityContext`
        * `SecurityContext`
    * `volumeMounts`
        * array of `VolumeMount`
* `Probe`
    * `httpGet`
    * `periodSeconds`
        * default to 10 sec
    * `timeoutSeconds`
        * default to 1 sec
    * `successThreshold`
        * default to 1
        * failした後に何度連続してsuccessになる必要があるか
    * `failureThreshold`
* `HTTPGetAction`
    * `host`
    * `httpHeaders `
    * `path`
    * `port`
    * `scheme`
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
* `PersistentVolume`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#persistentvolume-v1-core)
    * persistent volumeはvolumeの確保だけ、利用する場合は PersistentVolumeClaimを津アク
    * `kind`
        * PersistentVolume
    * `metadata`
    * `spec`
        * `PersistentVolumeSpec`
    * `status`
* `PersistentVolumeSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#persistentvolumespec-v1-core)
    * `accessModes`
    * `capacity`
        * object
        * [Persistent Volumes | Kubernetes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#capacity)
    * `gcePersistentDisk`
        * GCEPersistentDiskVolumeSource
    * `storageClassName`
    * `nfs`
        * `NFSVolumeSource`

```
  capacity:
    storage: 5Gi
```

* `NFSVolumeSource`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#nfsvolumesource-v1-core)
    * `path`
        * nfs serverのexportするdirのpath
    * `readOnly`
    * `server`
        * hostname, ip address
* `PersistentVolumeStatus`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#persistentvolumestatus-v1-core)
* `GCEPersistentDiskVolumeSource`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#gcepersistentdiskvolumesource-v1-core)
    * pdName
        * string
        * GCEのdisk
    * fsType
        * string
        * "ext4", "xfs", "ntfs".
    * readOnly
        * true/false
* `PersistentVolumeClaim`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#persistentvolumeclaim-v1-core)
    * kind
    * metadata
    * spec
        * `PersistentVolumeClaimSpec`
    * status
* `PersistentVolumeClaimSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#persistentvolumeclaimspec-v1-core)
    * accessModes
        * 以下のいずれか
        * ReadWriteOnce
        * ReadOnlyMany
        * ReadWriteMany
    * volumeMode
    * resources
    * storageClassName
    * selector
* `PersistentVolumeClaimStatus`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#persistentvolumeclaimspec-v1-core)
    * accessModes
    * resources
        * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#resourcerequirements-v1-core)
    * selector
    * storageClassName
    * volumeMode
    * volumeName
* `NetworkPolicy`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#networkpolicy-v1-networking)
    * spec
        * NetworkSpec
* `NetworkSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#networkpolicyspec-v1-networking)
    * `egress`
        * array of NetworkPolicyEgressRule
    * `ingress`
        * array of NetworkPolicyIngessRule
    * podSelector
        * LabelSelector
    * policyTypes
        * array of string
        * Ingress, Egress, Ingress and Egress
* `NetworkPolicyEgressRule`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#networkpolicyegressrule-v1-networking)
    * `ports`
        * array of NetworkPolicyPort
    * `to`
        * array of NetworkPolicyPeer
* `NetworkPolicyIngressRule`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#networkpolicyingressrule-v1-networking)
    * `from`
        * array of NetworkPolicyPeer
    * `ports`
        * array of NetworkPolicyPort
* `NetworkPolicyPeer`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#networkpolicypeer-v1-networking)
    * `ipBlock`
        * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#ipblock-v1-networking)
    * `namespaceSelector`
        * LabelSelector
    * `podSelector`
        * LabelSelector
* `IPBlock`
    * cidr
        * string
        * `"192.168.1.1/24"`
    * except
        * array of string
        * `"192.168.1.1/24"`
* `NetworkPolicyPort`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#networkpolicyport-v1-networking)
    * port
        * named port/ port number
    * protocol
        * TCP/UDP
* `Ingress`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/api-reference/v1.9/#ingress-v1beta1-extensions)
    * `spec`
        * IngressSpec
    * `status`
        * IngressStatus
* `IngressSpec`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#ingressspec-v1beta1-extensions)
    * `backend`
        * defaultのbackend
        * IngressBackend
        * ruleにmatchしないものはここにroutingされる
    * `rules`
        * array of IngressRule
    * `tls`
        * array of IngressRule
        * IngressTLS
* `IngressBackend`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#ingressbackend-v1beta1-extensions)
    * serviceName
        * string
        * forwardするservice名
    * servicePort
        * serviceのport
    * serviceName
* `IngressRule`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#ingressrule-v1beta1-extensions)
    * host
        * FQDN of network host
        * RFC 3986におけるhost
        * IPはだめ
        * `:`を含んではだめ、portはhostではない
        * hostを省略すると全てのrequestに対してroutingする
    * http
        * `HTTPIngressRuleValue`
* `HTTPIngressRuleValue`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#httpingressrulevalue-v1beta1-extensions)
    * paths
        * array of HTTPIngressPath
        * `http://<host>/<path>?<searchpart>`
            * `<path>`の部分を記述する
* `HTTPIngressValue`
    * paths
        * array of HTTPIngressPath
* `HTTPIngressPath`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#httpingresspath-v1beta1-extensions)
    * backend
        * IngressBackend
    * path
        * /から始まるpath
* `IngressTLS`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#ingresstls-v1beta1-extensions)
    * hosts
        * array of string
    * secretName
        * string
* `IngressStatus`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#ingressstatus-v1beta1-extensions)

## Reference
