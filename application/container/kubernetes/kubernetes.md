---
title: Kubernetes
---

## Kubernetes

<div style="text-align: center">
    <img src="http://30ux233xk6rt3h0hse1xnq9f-wpengine.netdna-ssl.com/wp-content/uploads/2017/05/harry-image.jpg">
</div>

* `kube-apiserver`
    * Kubernete's REST API entry point that processes operations on Kubernetes objects, i.e. Pods, Deployments, Stateful Sets, Persistent Volume Claims, Secrets, etc. An operation mutates (create / update / delete) or reads a spec describing the REST API object(s)
* `Etcd`
    * A highly available key-value store for kube-apiserver
* `kube-controller-manager`
    * Runs control loops that manage objects from kube-apiserver and perform actions to make sure these objects maintain the states described by their specs
* `kube-scheduler`
    * Gets pending Pods from kube-apiserver, assigns a minion to the Pod on which it should run, and writes the assignments back to API server. kube-scheduler assigns minions based on available resources, QoS, data locality and other policies described in its driving algorithm
* `kubelet`
    * A Kubernetes worker that runs on each minion. It watches Pods via kube-apiserver and looks for Pods that are assigned to itself. It then syncs these Pods if possible. The procedure of Syncing Pods requires resource provisioning (i.e. mount volume), talking with container runtime to manage Pod life cycle (i.e. pull images, run containers, check container health, delete containers and garbage collect containers)
* `kube-proxy`
    * A network proxy that reflects Service (defined in Kubernetes REST API) that runs on each node. Watches Service and Endpoint objects from kube-apiserver and modifies the underlying kernel iptable for routing and redirection.
* `user`
    * All kubernetes clusters have two type of users: `service account` maanged by Kubernetes and normal `user`
    * API requests are tied to either a normal user or a service account, or are treated as anonymous requests
    * `service account`
        * an account that Pod uses and is assigned to a Pod when the Pod is created
    * `user`
        * normal users are assumed to be managed by an outside of Kubernetes
        * Kubernetes does not have objects which represent normal user accounts.
* `Endpoint`
    * https://www.quora.com/What-is-an-endpoint-object-in-terms-of-Kubernetes
    * https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#endpoints-v1-core

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
    * [Kubernetes: The Distributed System ToolKit: Patterns for Composite Containers](http://blog.khttps://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#endpoints-v1-coreubernetes.io/2015/06/the-distributed-system-toolkit-patterns.html)
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
seelctorの指定は全てANDで考慮される。
selectorは、一意に指定できるように条件をつける。
labelの変更前後でselectorの一意性が崩れる場合がある。

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
ReplicaSetを直接使う場合は殆どない。Deploymentを使う。


### Service Account
* [Configure Service Accounts for Pods | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

* 何も指定しないとPodは同じNameSpaceの`default` SAを使う


### Encrypt secret data




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


## Examples
* [examples/guestbook at master · kubernetes/examples](https://github.com/kubernetes/examples/tree/master/guestbook)


## NFS
* [examples/staging/volumes/nfs at master · kubernetes/examples](https://github.com/kubernetes/examples/tree/master/staging/volumes/nfs)
* [How to create an kubernetes NFS volume on Google Container Engine - Stack Overflow](https://stackoverflow.com/questions/43358955/how-to-create-an-kubernetes-nfs-volume-on-google-container-engine)
* [Using NFS - Configuring Persistent Storage | Installation and Configuration | OpenShift Origin Latest](https://docs.openshift.org/latest/install_config/persistent_storage/persistent_storage_nfs.html)
* [How to create a kubernetes NFS volume on Google Container Engine · Issue #44377 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/44377)

## Network
* [GKE/Kubernetes でなぜ Pod と通信できるのか - Qiita](https://qiita.com/apstndb/items/9d13230c666db80e74d0)
* [The Ins and Outs of Networking in Google Container Engine // Speaker Deck](https://speakerdeck.com/thockin/the-ins-and-outs-of-networking-in-google-container-engine)

## Tips
* [10 Most Common Reasons Kubernetes Deployments Fail (Part 1)](https://kukulinski.com/10-most-common-reasons-kubernetes-deployments-fail-part-1/)


#### Evicted pods
* [Configure Out Of Resource Handling | Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/out-of-resource/)

```
The node was low on resource: nodefs.
```

#### Debugging Tips
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

#### Shared volumes in a Kubernetes Pod
* `emptyDir`を使えば同じpodの中でvolumeをshareできる

#### Pause container
* [The Almighty Pause Container - Ian Lewis](https://www.ianlewis.org/en/almighty-pause-container)
* [What is the role of 'pause' container? - Google Groups](https://groups.google.com/forum/#!topic/kubernetes-users/jVjv0QK4b_o)

#### Naming convention
* `<prefix>`
* namespace
    * `<prefix>-<service-name>`
    * namespace for each service
* container name
    * `<prefix>-<service-name>-<tier>`
* labels
    * app
        * `<prefix>-<service-name>`
    * service
    * tier
        * a component of a service
    * environment
        * dev/stg/prod

#### Adding lables to Pod template spec
```
The Deployment "name of deployment" is invalid: spec.template.metadata.labels: Invalid value: map[string]string{"tier":"service-tier", "app":"deployment-name", "service":"service-name", "environment":"dev"}: `selector` does not match template `labels`
```

selector is required

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: deployment-name
spec:
  replicas: 1
  selector: # required
    matchLabels:
      app: deployment-name
      environment: dev
      service: service-name
      tier: service-tier-name
  template:
    metadata:
      labels:
        app: deployment-name
        environment: dev
        service: service-name
        tier: service-tier-name
```

## Reference
* [What is the correct pronunciation of Kubernetes in English? · Issue #44308 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/44308)
* [Kubernetes: Using Kubernetes Namespaces to Manage Environments](http://blog.kubernetes.io/2015/08/using-kubernetes-namespaces-to-manage.html)
* [Making Kubernetes Production Ready – Part 2 - Applatix](https://applatix.com/making-kubernetes-production-ready-part-2/)
* [Storage Considerations for Docker-in-Docker on Kubernetes](https://blog.argoproj.io/storage-considerations-for-docker-in-docker-on-kubernetes-ed928a83331c)
