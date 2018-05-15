---
title: Kubernetes
---

## Kubernetes

<div style="text-align: center">
    <img src="http://30ux233xk6rt3h0hse1xnq9f-wpengine.netdna-ssl.com/wp-content/uploads/2017/05/harry-image.jpg">
</div>

* kube-apiserver
    * Kubernete's REST API entry point that processes operations on Kubernetes objects, i.e. Pods, Deployments, Stateful Sets, Persistent Volume Claims, Secrets, etc. An operation mutates (create / update / delete) or reads a spec describing the REST API object(s)
* Etcd
    * A highly available key-value store for kube-apiserver
* kube-controller-manager
    * Runs control loops that manage objects from kube-apiserver and perform actions to make sure these objects maintain the states described by their specs
* kube-scheduler
    * Gets pending Pods from kube-apiserver, assigns a minion to the Pod on which it should run, and writes the assignments back to API server. kube-scheduler assigns minions based on available resources, QoS, data locality and other policies described in its driving algorithm
* kubelet
    * A Kubernetes worker that runs on each minion. It watches Pods via kube-apiserver and looks for Pods that are assigned to itself. It then syncs these Pods if possible. The procedure of Syncing Pods requires resource provisioning (i.e. mount volume), talking with container runtime to manage Pod life cycle (i.e. pull images, run containers, check container health, delete containers and garbage collect containers)
* kube-proxy
    * A network proxy that reflects Service (defined in Kubernetes REST API) that runs on each node. Watches Service and Endpoint objects from kube-apiserver and modifies the underlying kernel iptable for routing and redirection.

## Concepts

* deployment
    * `.spec.strategy.type==Recreat`
        * 新しいpodを作る前にexisting podsが全てKillされる
    * `.spec.strategy.type==RollingUpdate`
    * `minReadySeconds`
        * podがreadyになった後どのくらい待つか
        * defaultは0で、ready状態になったらavailable扱い
        * readyになるかどうかは Probeできめる
    * `.spec.strategy.rollingUpdate.maxUnavailable `
        * updateの間にunavalableにできるpodの最大数
        * default valueは25%
        * 25%の場合は、25%までpodの数を減らし、あたらしいpodをdeployし、新しいpodがavailableになればその割合に応じて古いpodを更にunavalableにする
    * `.spec.strategy.rollingUpdate.maxSurge`
        * desired podの数を超えて作られるpodの数
        * percentageがpodの数で指定
        * `MaxUnavailable`が0だと0にできない
        * default avlueは25%
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
    * PodsはGrace periodでKillされる
        * defaultではgrace periodは30s
        * `kubectl delete --grace-period=<seconds>` で指定できる
        * 0secは force deleteだが、`--force` flagもつける必要がある

```
kubectl delete pods
```

### RBAC Authorization
* [Using RBAC Authorization | Kubernetes](https://kubernetes.io/docs/admin/authorization/rbac/)



### Nodes
* [Assigning Pods to Nodes | Kubernetes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/)
    * nodeの指定は3種類
    * node selector
    * node affinity
    * inter-pod affinity

kubernetes 1.4からNodeに自動で以下のlabelが付与される。
値はprovider specific.

* kubernetes.io/hostname
* failure-domain.beta.kubernetes.io/zone
* failure-domain.beta.kubernetes.io/region
* beta.kubernetes.io/instance-type
* beta.kubernetes.io/os
* beta.kubernetes.io/arch


**Node selector**

* nodeを指定して、Podに割当ができる
* ndoeにlabelをつけられるので、labelで選択する
* PodsSpecにNodeのlabelを指定する。


```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    disktype: ssd
```


**Node Affinity**

nodeSelectorに似ているが、nodeSelectorより柔軟な表現でNodeの割当ができる。

* `requiredDuringSchedulingIgnoredDuringExecution`
    * hard
    * 割り当てられたNodeに必ずscheduleされる必要がある
    * 実行中の場合は無視する
* `preferredDuringSchedulingIgnoredDuringExecution`
    * soft
    * 割り当てられたNodeがなければ他のnodeで動く

PodSpecに記載する。

* available operator
    *  In, NotIn, Exists, DoesNotExist, Gt, Lt


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/e2e-az-name
            operator: In
            values:
            - e2e-az1
            - e2e-az2
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: another-node-label-key
            operator: In
            values:
            - another-node-label-value
  containers:
  - name: with-node-affinity
    image: k8s.gcr.io/pause:2.0
```

**inter-pod affinity and anti-affinity**

以下の形式でPodのscheduleのruleをかける。

This pod should (or, in the case of anti-affinity, should not) run in an X if that X is already running one or more pods that meet rule Y”

* Y
    * Label selectorで表現
    * namespaceも指定する
* X
    * topology domain like node, rack, cloud provider
    * `topologyKey` で指定
* affinityの計算は軽くないので、schedulerの負荷になるので、数百node程度までで使う
* use cases
    * 全てのpodsを同じnodeに置きたい
    * 全てのpodsを別のnodeに置きたい


### Namespace
* [Namespaces | Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

* Namespaceをいつ使うべきか?
    * userが10人程度であればnamespaceを使う必要はない
    * clusterのresourceをuserで分ける場合に使う
* default
    * The default namespace for objects with no other namespace
* kube-system
    * The namespace for objects created by the Kubernetes system
* kube-public
    * The namespace is created automatically and readable by all users (including those not authenticated).
    * This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.
* 全てのobjectがnamespaceに属するわけではない
    * Node, persistentVolumeなどは属さない
    * Eventは種類によって属すものと属さないものがある

defaultのnamespaceを設定する。

```
kubectl config set-context $(kubectl config current-context) --namespace=<insert-namespace-name-here>
```

Namespaceを指定してcommandを実行する

```
kubectl --namespace=<insert-namespace-name-here> get pods
```



### Service
* [Services | Kubernetes](https://kubernetes.io/docs/concepts/services-networking/service/)

Podsは寿命がある。
`ReplicationControllers`が、Podsを動的に作成し破棄する。
Serviceは、他のPodsへ継続的に提供され続けるような機能を提供し続ける。
kubernetesの`service`はmicro serviceのようなもの。

seviceがtargetするPodsの集まりは`LabelSelector`によって指定する。

```yaml
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
```

* `Service` objectの名前が`my-service`
* labelが`app=MyApp`
* 公開されているportが`9376`


Service without selectors

* productionとtestでそれぞれDBを持ちたい
* 別のnamespaceやclusterのserviceと接続したい
* kubernetesへ一部systemを移行中の場合一部のserviceはkubernetesの外部のsystem

以下のようにselectorなしのserviceを定義する。

```yaml
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
```

selectorがない場合は、対応する`Endpoints`は作られない
`Endpoint`は明示的に作る。

```yaml
kind: Endpoints
apiVersion: v1
metadata:
  name: my-service
subsets:
  - addresses:
      - ip: 1.2.3.4
    ports:
      - port: 9376
```

selectorのない`Service`へaccessする場合は、作成した`Endpoint`(1.2.3.4:9376)へとroutingされる。
selectorなしの`Service`は`externalName`を指定することでも作成できる。
cluster外のendpointへ名前を定義する。
clusterのDNSが`my-service.prod.svc.CLUSTER`へのaccessに対して`CNAME`として`my.database.example.com`を返す。

```yaml
kind: Service
apiVersion: v1
metadata:
  name: my-service
  namespace: prod
spec:
  type: ExternalName
  externalName: my.database.example.com
```

Virtual IPs and service proxies

Kubernets clusterの全てのnodeは`kube-proxy`を起動する。

* `Proxy-mode: userspace`
* `Proxy-mode: iptables`
* `Proxy-mode: ipvs`


Multi port service

```yaml
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 9376
  - name: https
    protocol: TCP
    port: 443
    targetPort: 9377
```

**Discovering services**

serivceを見つける方法

* Environment variable
* DNS

Environment variables

PodがNode上で起動するとき、`kubelet`はactiveな`Service`に対して環境変数を追加する。

* service name
    * `redis-master`
* port
    * TCP `6379`
* cluster IP address
    * `10.0.0.11`

生成されるenvironment variablesは

```
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11
```

Podより前にserviceが作られる必要がある。
なぜならPodにserviceの環境変数を埋め込む必要がある。
DNSの場合はこの制約はない。

DNS


`Publishing services - service types`

serviceをclusterの内外に公開したい時 `ServiceType`を以下から選ぶ。

* `ClusterIP`
    * cluster internal IPに公開する
    * clusterの中からのみaccess可能
* `NodePort`
* `LoadBalancer`
    * [Configure Your Cloud Provider’s Firewalls | Kubernetes](https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/)
    * accessするIP rangeを指定できる
* `ExternalName`

* ClusterIP
* NodePort
    * nodeのstatic portで公開する
    * 自動でservice用の`ClusterIP`が作られる
    * clusterの外から`<NodeIP>:<NodePort>`にrequest
* LoadBalancer
    * cloudのload balancerと体付ける
* ExternalName
    * serviceとCNAMEの値(e.g. `foo.bar.example.com`)を対応づける

**Discovering services**

serviceに関する情報は、以下の環境変数として他のPodから参照できる。

* `{SVCNAME}_SERVICE_HOST`
    * underscore delimited upper caseに変換される
    * `hoge-fuga` -> `HOGE_FUGA`
* `{SVCNAME}_SERVICE_PORT`


```yaml
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11
```

### annotation
[Annotations | Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)

annotationに書かれる内容

* annotationに設定値を書く
* release ID, git branch, pr number, image hash, registry address
* client library, tool informatin for debugging, 


### Labels and Selectors
* [Labels and Selectors | Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)

* Labels
    * key/value pair
    * Podなどのobjectに付与される
    * Labelやmaintenanceや効率的なquery/watchのために必要
    * Labelをつけない場合は、annotationを使う

Labelの定義は、`PodTemplate`などにmetadataとして記載する。
`metadata.labels`, `spec.metadata.labels`

```yaml
  metadata:
    labels:
      app: airflow
      tier: worker
```

Labelの例

* key
    * values
* "release"
    * "stable", "release" : "canary"
* "environment"
    * "dev", "environment" : "qa", "environment" : "production"
* "tier"
    * "frontend", "tier" : "backend", "tier" : "cache"
* "partition"
    * "customerA", "partition" : "customerB"
* "track"
    * "daily", "track" : "weekly"

Syntax for key

* `prefix/name`
    * name
        * 63char
        * `[a-z0-9A-Z]`, `-`, `_`, `.`.
    * `prefix`
        * optional
        * DSN subdomain
        * 253 char
        * `kubernetes.io/`は予約されている
    * prefixが省略された場合はkeyはprivate

Label selectors

LabelはIDやnameのようにuniqueではない。
Label selectorで指定したlabelをもつobjectを扱える。
Selectorがemtpyの場合は全てのcollection
null label selectorは何も変更しない。

**API**



**Service and ReplicationController**

serviceの適用対象のPodsの集まりは、label selectorによって定義される。
`ReplicationController`も同様である。

```yaml
selector:
    component: redis
```

`component=redis`の指定と同等である。


### ReplicaSet
Controllerの1つ。
`ReplicationController`をおきかえるもの。
今のところ`ReplicationController`との違いは、label selectorの有無。

### StatefulSet
以下の1つ以上が必要な場合に役に立つ。

* Stable, unique network identifiers.
* Stable, persistent storage.
* Ordered, graceful deployment and scaling.
* Ordered, graceful deletion and termination.
* Ordered, automated rolling updates.

StableはPod schedulingによる一貫性と同じ意味。

### Deployment
* [Deployments | Kubernetes](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

Controllerの1つ。
PodとRelicaSetに対するupdate方法を記載する。
Rolling updateをする場合は、`Deployment`を使う。
Deploymentが作成する、`ReplicaSet`は直接変更しない。

**Writing Pod template**

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

### Secrets
* [Secrets | Kubernetes](https://kubernetes.io/docs/concepts/configuration/secret/)
    * 作成したseceretはPodにfileとしてvolumeに付与できる
    * enviroment variableとして付与できる

Password, OAuth token, ssh keysなどを保持する。
pod definitionやdocker imageに書くより柔軟に利用できる。
複数のpodで同じsecretを利用可能など。

secretを作成

```sh
# Create files needed for rest of example.
$ echo -n "admin" > ./username.txt
$ echo -n "1f2d1e2e67df" > ./password.txt
$ kubectl create secret generic db-user-pass --from-file=./username.txt --from-file=./password.txt
secret "db-user-pass" created
```

secretを取得

```sh
kubectl get secrets
```

secretの情報を見る

```sh
kubectl describe secrets/db-user-pass
```

Secretのdecode

```sh
$ kubectl get secret mysecret -o yaml
apiVersion: v1
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
kind: Secret
metadata:
  creationTimestamp: 2016-01-22T18:41:56Z
  name: mysecret
  namespace: default
  resourceVersion: "164619"
  selfLink: /api/v1/namespaces/default/secrets/mysecret
  uid: cfee02d6-c137-11e5-8d73-42010af00002
type: Opaque
```

decodeはbase64で行う。

```sh
$ echo "MWYyZDFlMmU2N2Rm" | base64 --decode
```

Podでfileとしてsecretを使う

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    secret:
      secretName: mysecret
```

fileのpermissionを`0400`などにしたい場合、10進数(256)で記載する。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      defaultMode: 256 # here
```

Environment variablesとして使う場合は

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: mycontainer
    image: redis
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: username
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
  restartPolicy: Never
```

**Use case: Pod with ssh-key**

```
kubectl create secret generic ssh-key-secret --from-file=ssh-privatekey=/path/to/.ssh/id_rsa --from-file=ssh-publickey=/path/to/.ssh/id_rsa.pub
```

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: secret-test-pod
  labels:
    name: secret-test
spec:
  volumes:
  - name: secret-volume
    secret:
      secretName: ssh-key-secret
  containers:
  - name: ssh-test-container
    image: mySshImage
    volumeMounts:
    - name: secret-volume
      readOnly: true
      mountPath: "/etc/secret-volume"
```

**Use-Case: Pods with prod / test credentials**

**Use-case: Dotfiles in secret volume**

### Service Account
* [Configure Service Accounts for Pods | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

* 何も指定しないとPodは同じNameSpaceの`default` SAを使う


### Encrypt secret data


### Volumes
* [Volumes | Kubernetes](https://kubernetes.io/docs/concepts/storage/volumes/)

Dockerのvolumeと違い、透過的に色々なdeviceをvolumeとして扱える。

* awsElasticBlockStore
* azureDisk
* azureFile
* cephfs
* csi
* downwardAPI
    * pods/containerのlabelなどの情報をvolumeとしてmountできる
* emptyDir
    * NodeにPodが作られたとき作られる
    * PodがNodeから削除されると消える
    * containerがcrashしても消えない
    * defaultでnodeのvolumeに記録されている
        * `emptyDir.medium: memory` でnodeのtmpfsにもできるが、nodeのrebootとmemory limitによる制約をうける
    * Use case
        * disk based merge sort
        * checkpoint
        * podのcontainer間での読み書き可能なshared volume
            * git-sync sidecar
* fc (fibre channel)
* nfs
    * Podがremoteされても、unmountされるだけで中身は消えない
    * 複数のPodにmountして使うことができる
    * Mount前にdataが保持できる
    * NFS serverが必要
* persistentVolumeClaim
    * PersistentVolumeをmountするのに必要
* flocker
* gcePersistentDisk
    * GCEのpersistent disk
    * 事前にgcloudでPersistent Diskを作っておく必要がある
    * `gcloud compute disks create --size=500GB --zone=us-central1-a my-data-disk`
* gitRepo
    * credeintialsがいる場合はgit-syncを検討する
        * [kubernetes/git-sync: A sidecar app which clones a git repo and keeps it in sync with the upstream.](https://github.com/kubernetes/git-sync)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: server
spec:
  containers:
  - image: nginx
    name: nginx
    volumeMounts:
    - mountPath: /mypath
      name: git-volume
  volumes:
  - name: git-volume
    gitRepo:
      repository: "git@somewhere:me/my-git-repository.git"
      revision: "22f1d8406d464b0c0874075539c1f2e96c253775"
```

git-syncを使う。

```yaml
    spec:
      restartPolicy: Always
      containers:
      - name: git-sync
        image: k8s.gcr.io/git-sync:v2.0.4
        imagePullPolicy: Always
        volumeMounts:
        - name: git-secret
          mountPath: /etc/git-secret
        env:
        - name: GIT_SYNC_REPO
          value: "git@github.com:kubernetes/kubernetes.git"
        - name: GIT_SYNC_DEST
          value: "git"
        - name: GIT_SYNC_SSH
          value: "true"
      - name: redis
        image: redis
        ports:
        - name: management
          containerPort: 16379
        - name: node
          containerPort: 6379
        env:
        - name: REDIS_PASSWORD
          value: "airflow"
```

* glusterfs
* hostPath
    * NodeのPathをmountする
    * containerがdokcerを使う必要があるとき、`/var/lib/docker`を使う
* iscsi
* local
* nfs
    * [examples/staging/volumes/nfs at master · kubernetes/examples](https://github.com/kubernetes/examples/tree/master/staging/volumes/nfs)
    * [external-storage/nfs at master · kubernetes-incubator/external-storage](https://github.com/kubernetes-incubator/external-storage/tree/master/nfs)
* persistentVolumeClaim
* projected
* portworxVolume
* quobyte
* rbd
* scaleIO
* secret
* storageos
* vsphereVolume


### PersistentVolume
* [Persistent Volumes | Kubernetes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#capacity)

DBなどのStatufulなapplicationを使う場合に利用する。
`PersistenVolume`で利用するvolumeを確保して、`PersistentVolumeClaim`で利用する分を確保する。

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0003
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  mountOptions:
    - hard
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
```

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: slow
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - {key: environment, operator: In, values: [dev]}
```

* Acccess mode
    * ReadWriteOnce
        * single nodeでR/W
    * ReadOnlyMany
        * multi nodeでR
    * ReadWriteMany
        * multi nodeでR/W


```
gcloud compute disks create --size=500GB --zone=us-central1-a my-data-disk
```


### CondigMap
* [Configure Containers Using a ConfigMap | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configmap/)

* configmapはLinuxの`/etc`におかれるfileのようなもの


### Best Practice
* [Configuration Best Practices | Kubernetes](https://kubernetes.io/docs/concepts/configuration/overview/)

* General Config Tips
    * specify the latest stable API version (currently v1)
    * clusterにpushする前に、VCSにcommit
        * roll backが簡単になる
    * JSONでなくYAMLでかく
    * 関係するobjectはまとめて一つのfileにする
    * default valueはかかない
        * configはsimpleでminimalにする
    * objectの説明をannotationにかく
* Naked Pods vs Replication Controller and jobs
    * naked podsはNodeのfailでreschedulerされない
    * `restartPolicy: Never`になる場合を除き、殆ど`Replication Controller`を利用する
    * `Job` objectの機能を検討する
* Services
    * replication controllerを作成する前に、`Service`を作る
    * Nodeのdaemonように、本当に必要な場合を除き`hostPort`は使わない
        * debugなどでNodeのportにaccessする場合は、`proxy`や`apiserver proxy`, `port-foward`などを検討する
    * 同様の理由で`hostNetwork`は使わない
* Using Labels
    * semantic attributesでつける
    * Bad
        * serviceに `service: myservice`
        * controllerに`controller: mycontroller`
    * good
        * `{ app: myapp, tier: frontend, phase: test, deployment: v3 }`
* container image
    * productionで`latest`はさける
* Using kubectl
    * `kubectl create -f <dir>`は`dir`の`.yaml`, `.yml`, `.json`に対して`kubectl-create`
    * `kubectl-stop`より`kubectl-delete`を使うstopはdeprecated


### Expose Pod Information to Containers Through Environment Variables
* [Expose Pod Information to Containers Through Environment Variables | Kubernetes](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)

以下のように`fieldRef`と`fieldPath`でyamlの設定値を参照できる。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-envars-fieldref
spec:
  containers:
    - name: test-container
      image: k8s.gcr.io/busybox
      command: [ "sh", "-c"]
      args:
      - while true; do
          echo -en '\n';
          printenv MY_NODE_NAME MY_POD_NAME MY_POD_NAMESPACE;
          printenv MY_POD_IP MY_POD_SERVICE_ACCOUNT;
          sleep 10;
        done;
      env:
        - name: MY_NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
        - name: MY_POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: MY_POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: MY_POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        - name: MY_POD_SERVICE_ACCOUNT
          valueFrom:
            fieldRef:
              fieldPath: spec.serviceAccountName
  restartPolicy: Never
```

### Use environment variable in yaml
* [Using environment variables in Kubernetes deployment spec - Server Fault](https://serverfault.com/questions/791715/using-environment-variables-in-kubernetes-deployment-spec)

yaml fileの中でshellの環境変数は現状利用できない。
`envsubst`を使って、実行時に置き換えるか、`API`をprogramから呼び出す。

### Configuring Nodes to Authenticate to a Private Repository
* [Pull an Image from a Private Registry | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/)
    * GKEを使う場合は、GCRのcredentialの設定は`.dockercfg`に記載されている
    * [Using Google Container Registry (GCR) with Minikube · Ryan Eschinger Consulting](https://ryaneschinger.com/blog/using-google-container-registry-gcr-with-minikube/)
    * OSXの場合は`Security store docker logins in macOS keychain`をoffにしないと、`.docker/config.json`にcredentialは保存されない

`docker login`を実行すれば、`.config/config.json`にcredentialが生成されるので、これをsecretとしてexportすれば良い。
kubectlでは上記を行うcomandが用意されている。

`docker create secret docker-registry`を実行する。

```
kubectl create secret docker-registry \
    regsecret --docker-server=<your-registry-server> \
    --docker-username=<your-name> \
    --docker-password=<your-pword> \
    --docker-email=<your-email>
```

For GCP

```
kubectl create secret docker-registry <secret-name> \
    --docker-server=https://gcr.io \
    --docker-username=oauth2accesstoken \
    --docker-password="$(gcloud auth print-access-token)" \
    --docker-email=<your-email@here>
```

上記の設定のもと

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: some-name
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: some-app
    spec:
      restartPolicy: Always
      imagePullSecrets:
        - name: <secret-name>
      containers:
      - name: container-name
        image: gcr.io/project-id/name:tag
        imagePullPolicy: Always
```

もしくは、container内でdocker pull を行いたい場合は、以下のようにする。
`subPath`でfile名を指定できる。

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: secret-test-pod
  labels:
    name: secret-test
spec:
  containers:
  - name: ssh-test-container
    image: mySshImage
    volumeMounts:
    - name: volume-name
      readOnly: true
      mountPath: "/home/root/.docker"
  volumes:
  - name: volume-name
    projected:
      sources:
      - secret:
          name: <secret-name>
          items:
           - key: .dcokerconfigjson
             path: config.json
             mode: 400
```

## DNS
[DNS for Services and Pods | Kubernetes](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)

Serviceに対するA record

serviceのhostnmaeは以下の規則で付与される。
namespaceをまたいで、accessすることも可能。

```
<service-name>.<namespace>.svc.cluster.local
```

* PodのDNS Policy
    * `dnsPolicy:`
        * `Default`
            * 
        * `ClusterFirst`
            * clusterのdomain nameにmatchしないものは、nodeから受け継いだupstream DNSにforwardする
        * `ClusterFirstWithHostNet`
            * hostnetworkで動くPodの場合は設定が必要
        * `None`
            * Kubernetes 1.9から
            * kkubernetesのDNSの設定を無視する
            * `dnsConfig`で設定する
* PodのDNSの設定
    * `nameservers:`
        * DNS serverのIP address
        * 多くとも3つ
        * dnsPolich: Noneのときは最低1ついる
    * `searches:`
        * Podのhostname lookupで探すDomain
    * `options:`
        * DNS policyにoptionを渡せる


[Customizing DNS Service | Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/#inheriting-dns-from-the-node)


### Error


### Tips
* [10 Most Common Reasons Kubernetes Deployments Fail (Part 1)](https://kukulinski.com/10-most-common-reasons-kubernetes-deployments-fail-part-1/)

```
kubectl describe pod <pod-id>
```

## Examples
* [examples/guestbook at master · kubernetes/examples](https://github.com/kubernetes/examples/tree/master/guestbook)

## Ingress
readinessProbeの設定をかえた場合は

**health check**

* [ingress-gce/examples/health-checks at master · kubernetes/ingress-gce](https://github.com/kubernetes/ingress-gce/tree/master/examples/health-checks)
* [メルカリ社内ドキュメントツールの Crowi を Kubernetes に載せ替えました - Mercari Engineering Blog](http://tech.mercari.com/entry/2017/09/11/150000)
* health checkをpassするには以下のいずれかを満たす
    * status code: 200を`/`で返すか`readiness`のURLをserviceでexposeする
    * `/` で200を返す
* ingressのhealth checkの条件はingress controllerの実装による
    * [google compute engine - How to get a custom healthcheck path in a GCE L7 balancer serving a Kubernetes Ingress? - Stack Overflow](https://stackoverflow.com/questions/44584270/how-to-get-a-custom-healthcheck-path-in-a-gce-l7-balancer-serving-a-kubernetes-i)
    * GCE
        * https://github.com/kubernetes/ingress-gce/blob/master/README.md#health-checks

## NFS
* [examples/staging/volumes/nfs at master · kubernetes/examples](https://github.com/kubernetes/examples/tree/master/staging/volumes/nfs)
* [How to create an kubernetes NFS volume on Google Container Engine - Stack Overflow](https://stackoverflow.com/questions/43358955/how-to-create-an-kubernetes-nfs-volume-on-google-container-engine)
* [Using NFS - Configuring Persistent Storage | Installation and Configuration | OpenShift Origin Latest](https://docs.openshift.org/latest/install_config/persistent_storage/persistent_storage_nfs.html)
* [How to create a kubernetes NFS volume on Google Container Engine · Issue #44377 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/44377)

## Network
* [GKE/Kubernetes でなぜ Pod と通信できるのか - Qiita](https://qiita.com/apstndb/items/9d13230c666db80e74d0)
* [The Ins and Outs of Networking in Google Container Engine // Speaker Deck](https://speakerdeck.com/thockin/the-ins-and-outs-of-networking-in-google-container-engine)


## Evicted pods
* [Configure Out Of Resource Handling | Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/out-of-resource/)


```
The node was low on resource: nodefs.
```

## Horizontal Autoscaler
* [Horizontal Pod Autoscaler | Kubernetes](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

cpu負荷などに応じてreplica数を増減させる。
custom metricsにも対応している。
cluster autoscalerはresource limitに応じてpods用のnodeを確保する。

* `--horizontal-pod-autoscaler-sync-period` がcpu loadを計算するperiod
    * default 30 sec
* each podにresource request API経由でCPUなどの情報を取得し、
* Horizontal AUtoscalerは以下の2つの方法でmetricsにaccessする
    * Heapster
        * Heapsterにproxyを通してaccess
        * Heapseterがkube-systemにdeployされている必要がある
    * REST API
        * custom metrics用のAPIがある
        * [community/custom-metrics-api.md at master · kubernetes/community](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md)
* `--horizontal-pod-autoscaler-downscale-delay`
    * downscaleまでのdelay
    * default 5m
* `--horizontal-pod-autoscaler-upscale-delay`
    * upscaleまでのdelay
    * default 3m


kubectlでHorizontal Autoscalerの設定できる。



## Cluster Autoscale
* [autoscaler/FAQ.md at master · kubernetes/autoscaler](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
* [Advanced Scheduling and Pod Affinity/Anti-affinity - Scheduling | Cluster Administration | OpenShift Origin Latest](https://docs.openshift.org/latest/admin_guide/scheduling/pod_affinity.html)

* When does Cluster Autoscaler change the size of a cluster?
    * increasing
        * there are pods that failed to schedule on any of the current nodes due to insufficient resources.
        * adding a node similar to the nodes currently present in the cluster would help.
    * decreasing
        * some nodes are consistently unneeded for a significant amount of time.
        * A node is unneeded when it has low utilization and all of its important pods can be moved elsewhere.
* What types of pods can prevent CA from removing a node?
    * `PodDisruptionBudget`のあるpods
    * `kube-system`のpodで、`"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`が指定されていない
        * are not run on the node by default
        * don't have PDB or their PDB is too restrictive
    * deployment/replicasetなどcontroller objectに作られてないpods
    * Pods with local storage
        * `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`が指定されてない
    * node selectorやpod affinityの制約で動かせない
* What are the Service Level Objectives for Cluster Autoscaler?
    * pending podsをdeployできるnodeを自動で生成することが目的
    * SLOはpodがunschedulableになってから、CAがscale outの命令をnodeに送るまでのlatencyでみることができる
    * latencyはmax20secを目標としているが、実際のtestでは
        * No more than 30 sec latency on small clusters (less than 100 nodes with up to 30 pods each), with the average latency of about 5 sec.
        * No more than 60 sec latency on big clusters (100 to 1000 nodes), with average latency of about 15 sec.
        * またpod affinityがある環境では、上記の3倍以上の時間がかかる
* Autoscaleを使うにはkubernetesのmanifestでcontainerのresourcesを指定しておく必要がある
* Cluster AutoscaleはCPU usage based autoscalerとは違う
    * cluster autoscalerはresourceのrequestに応じてpodsを割り当てるためのnodeを作るのみ
* What are the key best practices for running Cluster Autoscaler?
    * k

特定のnodeのscale downを防ぐ場合は、nodeにannotationに以下をつける。

```
"cluster-autoscaler.kubernetes.io/scale-down-disabled": "true"
```

既存のnodeにつける場合は以下のようにする。

```
kubectl annotate node <nodename> cluster-autoscaler.kubernetes.io/scale-down-disabled=true
```

### Debugging Tips
* podが落ちていたら取り敢えず `kubectl describe`
* ちょっと、Kubernetesのpod/networkで何かを実行したい場合
    * 以下のpodをcreate

```
kubectl create -f pod.yaml
kubectl exec -it clinet -- get -T 2 -q nginx  -O -
```

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: client
  namespace: policy-demo
  labels:
    run: client
spec:
  containers:
  - name: busybox
    image: busybox
    args:
    - sleep
    - "10000"
```

### Shared volumes in a Kubernetes Pod
* `emptyDir`を使えば同じpodの中でvolumeをshareできる



## Reference
* [What is the correct pronunciation of Kubernetes in English? · Issue #44308 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/44308)
* [Kubernetes: Using Kubernetes Namespaces to Manage Environments](http://blog.kubernetes.io/2015/08/using-kubernetes-namespaces-to-manage.html)
* [Making Kubernetes Production Ready – Part 2 - Applatix](https://applatix.com/making-kubernetes-production-ready-part-2/)
* [Storage Considerations for Docker-in-Docker on Kubernetes](https://blog.argoproj.io/storage-considerations-for-docker-in-docker-on-kubernetes-ed928a83331c)
* [[Kubernetes] オンプレでも GKE Like な Ingress を使うために 自作 Ingress Controller を実装してみた | Tech Blog](https://adtech.cyberagent.io/techblog/archives/3758)
