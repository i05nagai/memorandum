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
* Namespace


### Nodes


### Namespace
* [Namespaces | Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)


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


### Labels and Selectors
* [Labels and Selectors | Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)

* Labels
    * key/value pair
    * Podなどのobjectに付与される
    * Labelやmaintenanceや効率的なquery/watchのために必要
    * Labelをつけない場合は、annotationを使う　

Labelの定義は、`PodTemplate`などにmetadataとして記載する。

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
* 


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
* emptyDir
    * NodeにPodが作られたとき作られる
    * PodがNodeから削除されると消える
    * containerがcrashしても消えない
    * Use case
        * disk based merge sort
        * checkpoint
        *
* fc (fibre channel)
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
* persistentVolumeClaim
* projected
* portworxVolume
* quobyte
* rbd
* scaleIO
* secret
* storageos
* vsphereVolume

### CondigMap
* [Configure Containers Using a ConfigMap | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configmap/)

* configmapはLinuxの`/etc`におかれるfileのようなもの


## CLI

### kubectl

Create resource from file

```
kubectl create -f filename
```

Run particular image on the cluster

```
kubectl run image
```

作成されたPods resourceの一覧

```
kubectl get pods
```

Label selectorでlabelを指定してdescribe

```
kubectl describe pods --selector key=value
```

### minikube

dashboard

```
minikube dashboard
```

`service-name`のserviceのURLを開く

```
minikube service <service-name>
```

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

## Examples
* [examples/guestbook at master · kubernetes/examples](https://github.com/kubernetes/examples/tree/master/guestbook)

## Reference
* [What is the correct pronunciation of Kubernetes in English? · Issue #44308 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/44308)
* [10 Most Common Reasons Kubernetes Deployments Fail (Part 1)](https://kukulinski.com/10-most-common-reasons-kubernetes-deployments-fail-part-1/)
* [Kubernetes: Using Kubernetes Namespaces to Manage Environments](http://blog.kubernetes.io/2015/08/using-kubernetes-namespaces-to-manage.html)
* [Making Kubernetes Production Ready – Part 2 - Applatix](https://applatix.com/making-kubernetes-production-ready-part-2/)
