---
title: Google Kubernetes Engine
---

## Google Kubernetes Engine
以下で`kubectl`の向き先が作成したclusterになる。

```
gcloud container clusters get-credentials <cluster_name> --zone <zone_name> --project <project>
```

## CLI
gcloudを使う。
project_idとzoneを設定している必要がある。
regionではないので注意。

```
gcloud config set project [PROJECT_ID]
gcloud config set compute/zone [COMPUTE_ZONE]
```


```
gcloud container builds
```

```
gcloud container clusters
```

```
gcloud container images
```

cluster接続用のcredentialの取得

```
gcloud container clusters get-credentials <cluster_name> --zone <zone_name> --project <project>
```

clusterのlist

```
gcloud container clusters list
```

clusterのdescribeができる。

```
gcloud container clusters describe <cluster_nane>
```

## Volume
GKEのpersistent disk volumeを使う。
cluster作成
terraformかgcloudから作る。

```
gcloud compute disks create --size 200GB mysql-disk
```

```
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: persistent-volume-database
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  gcePersistentDisk:
    pdName: pd-name
    fsType: ext4
```

## Dashboard
* [Kubernetes Engine Dashboards  |  Kubernetes Engine  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/concepts/dashboards)

kubectlでproxyを起動する。

```
kubectl proxy
```

`http://localhost:8001/ui`にaccessする。

## Aministrating clusters

### Configuring Cluster networking
* [Internal Load Balancing  |  Kubernetes Engine  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)
* [Network Policies | Kubernetes](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
* [The Ins and Outs of Networking in Google Container Engine // Speaker Deck](https://speakerdeck.com/thockin/the-ins-and-outs-of-networking-in-google-container-engine)
    * Kubernetesのnetworkの仕組み
* [GKE/Kubernetes の Service はどう動いているのか // Speaker Deck](https://speakerdeck.com/apstndb/kubernetes-false-service-hatoudong-iteirufalseka)

## Setting up HTTP Load Balancing with Ingress
* [Setting up HTTP Load Balancing with Ingress  |  Kubernetes Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer)
    * TCP load balancerは`type: LoadBalancer`
    * HTTP(S) load balancerは`Ingress`
        * [GKEだとデフォルトでIngress Controller(=GLBC)がいる - まーぽんって誰がつけたの？](http://www.mpon.me/entry/2017/04/22/023142)
        * GKEではcluster作成時にmaster nodeにload balancerを作成するoptionがあるので、これをONにする
        * GKEでingressを作成したのに、ずっと`Creating Ingress`になっている場合は、clusterのload balancer optionがoffになっている
        * ingressのfirewallは別途あける必要がある
    * Ingressはephemeral external IP addressをdefaultで割り振る
    * static IP addressにしたい場合は２つの方法がある
    * [Global ingress in practice on Google Container Engine — Part 1: Discussion](https://medium.com/google-cloud/global-ingress-in-practice-on-google-container-engine-part-1-discussion-ccc1e5b27bd0)
* [kubernetes/ingress-gce: Ingress controller for Google Cloud](https://github.com/kubernetes/ingress-gce)
* [ingress-gce/gce.md at master · kubernetes/ingress-gce](https://github.com/kubernetes/ingress-gce/blob/master/docs/faq/gce.md#how-do-i-deploy-an-ingress-controller)
* [ingress-gce/examples/static-ip at master · kubernetes/ingress-gce](https://github.com/kubernetes/ingress-gce/tree/master/examples/static-ip)

外部にserviceを公開するには、ingress/Load balancerが必要。
GKEではingressはCloud Load Balancingで実装されている。


```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: basic-ingress
spec:
  backend:
    serviceName: nginx
    servicePort: 80
```

Global IPを使う場合は事前にIPを作成する。

```
gcloud compute addresses create <ip_name> --global
```

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: test
  annotations:
    kubernetes.io/ingress.global-static-ip-name: <ip_name>
    ingress.kubernetes.io/rewrite-target: /
spec:
  backend:
    serviceName: testsvc
    servicePort: 80
  rules:
  - http:
      paths:
      - path: /foo
        backend:
          serviceName: s1
          servicePort: 80
      - path: /bar
        backend:
          serviceName: s2
          servicePort: 80
```

ingressを作成しても、つながらない場合は、GCPのnetwork consoleに残っている`k8s-*`のPrefixのついたnetworkの設定を削除する。
https://github.com/kubernetes/kubernetes/issues/45438


Ingressの名前は以下の形式で作られるようなので、clusterの違いは判別できない？
更に63文字までにきりつめられる。

```
k8s-um-<namespace>-<ingress-name>-ingress-0
```


## Configuring Network Policies for Applications
* [Configuring Network Policies for Applications  |  Kubernetes Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/tutorials/network-policy)
    * Pod内のnetwork policyの設定方法。
    * network policyをenabledにすると、`ip-masq-agent`がdaemonsetで動く
    * `ip-masq-agent`が動いているとclusterの外との通信時にsource addressがPodsのIPのままになる。

Podへのincomming trafficの制限。
以下は、`app=hello`のlabelをもつPodへのaccessは`app=foo`というlabelを持つPodからだけ許可する。

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: hello-allow-from-foo
spec:
  policyTypes:
  - Ingress
  podSelector:
    matchLabels:
      app: hello
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: foo
```

Podからのoutgoing trafficの制限

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: foo-allow-to-hello
spec:
  policyTypes:
  - Egress
  podSelector:
    matchLabels:
      app: foo
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: hello
  - ports:
    - port: 53
      protocol: TCP
    - port: 53
      protocol: UDP
```


## Zone
* [Regions and Zones  |  Compute Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/compute/docs/regions-zones/#available)

## Disk
GKEでPDを作ると、GCEにDiskが作成される。
GKEでPVCを作っても、GCEにDiskが作成される。
cluster作成のさいのdiskは各Nodeの持つdisk sizeを決める。

GKEでGCEのvolumeを使う方法は

* PVCで作成する
    * GCEのdiskが自動で作成される
* GCEのdiskを作成後、Podに直接mountする
    * PVもPVCも使わない

GCEのpersistent diskを作成するにはあらかじめ、GCEのdiskを作成しておく必要がある。

```
gcloud compute disks create --size 200GB mysql-disk
gcloud compute disks create --size 200GB wordpress-disk
```

disk名でvolumeをmountできる。

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: mysql
  labels:
    app: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - image: mysql:5.6
          name: mysql
          env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql
                  key: password
          ports:
            - containerPort: 3306
              name: mysql
          volumeMounts:
            - name: mysql-persistent-storage
              mountPath: /var/lib/mysql
      volumes:
        - name: mysql-persistent-storage
          gcePersistentDisk:
            pdName: mysql-disk
            fsType: ext4
```

## Container cluster architecture
* [Container Cluster Architecture  |  Kubernetes Engine  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)

利用可能なkubernetesのversion

```
gcloud container get-server-config
```

## NGINX Ingress on GKE
* [Ingress with NGINX controller on Google Kubernetes Engine | Ingress with NGINX controller on Google Kubernetes Engine  |  Google Cloud Platform Community  |  Google Cloud Platform](https://cloud.google.com/community/tutorials/nginx-ingress-gke)
* [ingress-nginx/deploy at master · kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx/tree/master/deploy#installation-guide) 
* [external-dns/nginx-ingress.md at master · kubernetes-incubator/external-dns](https://github.com/kubernetes-incubator/external-dns/blob/master/docs/tutorials/nginx-ingress.md)

## List of OAuth scopes
* [OAuth 2.0 Scopes for Google APIs  |  Google Identity Platform  |  Google Developers](https://developers.google.com/identity/protocols/googlescopes)

## Cluasterのmaster
clusterのmasterはWebUIから見えない?

## Setting up IP aliasing
* [IP Aliases  |  Kubernetes Engine  |  Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases#considerations_for_cluster_sizing)

Advantages

* 他のComputer resourceとのIPの競合を防ぐ
* 任意のsourceからEgress traficに送られないようにanti-spoofingができる
* firewalll ruleをhost nodeとは別にpodに適用できる
* Podから直にserviceにaccessできる
* Aliased IPはBGPを通して、
The networking layer can perform anti-spoofing checks to ensure that egress traffic is not sent with arbitrary source IPs.
Pod IPs are natively routable within the Google Cloud Platform network (including via VPC Network Peering), so clusters can scale to larger sizes faster without using up route quota.
Aliased IPs can be announced through BGP by the cloud-router, enabling better support for connecting to on-premises networks.
Firewall controls for Pods can be applied separately from their hosting node.
IP aliases allow Pods to directly access hosted services without using a NAT gateway.

* Node IP
    * between `/19` and `/28`
    * between 8192 and 16
    * Each node requires `/24` block
* Pod IP
    * between `/9` and `/28`
    * between 8,192 and 2,097,152
    * clusterのCONTAINERにCIDRを指定できるが、`/9`-`/19`の間に収める必要がある。
* Service IP
    * between `/18` and `/22`
    * between 1,024 and 16,384 

## IP Masquerade Agent
* [IP Masquerade Agent  |  Kubernetes Engine  |  Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent)

* 以下の条件で動作
    * from Kubernetes 1.7
    * network policyがenabledかcluster CIDRが`10.0.0.0/8`以外
* `ip-masq-agent` がdaemonで動いて、iptablesを設定する
* defaultで`/etc/config/ip-masq-agent`の設定を60secでreaload
* ConfigMapで設定を変更できる

```
# iptables -t nat -L IP-MASQ-AGENT -v -n
Chain IP-MASQ-AGENT (1 references)
 pkts bytes target     prot opt in     out     source               destination
   13   828 RETURN     all  --  *      *       0.0.0.0/0            169.254.0.0/16       /* ip-masq-agent: local traffic is not subject to MASQUERADE */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            10.0.0.0/8           /* ip-masq-agent: local traffic is not subject to MASQUERADE */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            172.16.0.0/12        /* ip-masq-agent: local traffic is not subject to MASQUERADE */
    0     0 RETURN     all  --  *      *       0.0.0.0/0            192.168.0.0/16       /* ip-masq-agent: local traffic is not subject to MASQUERADE */
    0     0 MASQUERADE  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* ip-masq-agent: outbound traffic is subject to MASQUERADE (must be last in chain) */
```

## Error

### Error from server: No SSH tunnels currently open
* [docker - kubectl: Error from server: No SSH tunnels currently open - Stack Overflow](https://stackoverflow.com/questions/36375030/kubectl-error-from-server-no-ssh-tunnels-currently-open)
* [Proxy (ssh-tunnel) errors are not helpful when we have 0 tunnels. · Issue #12167 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/12167)

clusterを作ると、projectのmetadataとして以下が登録される。

* networkの情報
    * key: gke-<cluster-name>-....-cidr
    * value: `<network>:<cidr>`
* SSH key
    * key: sshKeys
    * value: `gke-...`


errorの原因として考えられるもの。

* Project level metadata is full, GKE cannot add its SSH key. GCE has a 32 KB limit on metadata values.
* Node(s) with instance-level SSH keys set. GCE allows instance-level SSH keys to override project-level keys. In this case gcloud compute ssh will also fail.
* SSH is firewalled. By default, GKE creates a firewall rule to give the master SSH access to the nodes, but it is possible to delete that rule.
    * Re-add a firewall rule that allows tcp:22 from the GKE master's IP.
* routingの設定
    * masterはexternal IPなので、default gatewayへの設定が正しくされてないとだめ

## Node Pool
* [Node Pools  |  Kubernetes Engine  |  Google Cloud](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools)

* 1つのclusterにNode poolを複数指定できる
* Node poolのinstanceは


### Access to node
In cloud shell

```
gcloud compute ssh <node_instance_name> --zone=<instance_zone>
```

Note `node_instance_name` is not IP addresss.

## Assign Pod to Node
GKEではNodeに対して自動でいくつかlabelが付与される

```
kubectl get nodes --show-labels
```

* `cloud.google.com/gke-nodepool=<node-pool-name>`
    * Node poolごとにNode pool名がNodeのlabelとして付与される。
* `kubernetes.io/hostname=gke-<cluster-name>-<node-pool-name>-<id>`
    * nodeごとに一意なidが付与される
* `beta.kubernetes.io/instance-type=n1-standard-1`
    * nodeのinstance typeが付与される

## Docker images
docker image 

* kube-dns
    * gcr.io/google_containers/k8s-dns-kube-dns-amd64:1.14.5
    * [kubernetes/dns: Kubernetes DNS service](https://github.com/kubernetes/dns)

## GPU
* [GPUs  \|  Kubernetes Engine  \|  Google Cloud](https://cloud.google.com/kubernetes-engine/docs/concepts/gpus)

* node pools equipped with NVIDIA Tesla® V100, P100, and K80 GPUs

## Reference
* https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
* [GKEのRegional Clusters(Beta)を試してみた - nFact](http://nokok.hatenablog.com/entry/2017/12/20/000043)
* [The Ins and Outs of Networking in Google Container Engine // Speaker Deck](https://speakerdeck.com/thockin/the-ins-and-outs-of-networking-in-google-container-engine)
