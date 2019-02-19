---
title: Kubernetes Object Service
---

## Kubernetes Object Service
Pods are motal.
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

## Service Type
https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#servicespec-v1-core
https://rendezvous.m3.com/ai/aws-ai-infra/blob/master/terraform/archimedes/prod/terraform.tfvars

* ExternalName
    * ExternalName" maps to the specified externalName
* ClusterIP
    * Default
    * ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints
    * If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a stable IP. 
* NodePort
    * NodePort" builds on ClusterIP and allocates a port on every node which routes to the clusterIP
* LoadBalancer
    * "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the clusterIP

## Discovering services

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

## Example

## Reference
* https://kubernetes.io/docs/concepts/services-networking/service/
* [Services | Kubernetes](https://kubernetes.io/docs/concepts/services-networking/service/)
