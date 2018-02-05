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



## expose cluster in GKE
* [Setting up HTTP Load Balancing with Ingress  |  Kubernetes Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer)
    * TCP load balancerは`type: LoadBalancer`
    * HTTP(S) load balancerは`Ingress`
    * Ingressはephemeral external IP addressをdefaultで割り振る
    * static IP addressにしたい場合は２つの方法がある
    * [Global ingress in practice on Google Container Engine — Part 1: Discussion](https://medium.com/google-cloud/global-ingress-in-practice-on-google-container-engine-part-1-discussion-ccc1e5b27bd0)

外部にserviceを公開するには、ingressが必要。
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

```
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




## Configuring Network Policies for Applications
* [Configuring Network Policies for Applications  |  Kubernetes Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/tutorials/network-policy)
    * Pod内のnetwork policyの設定方法。

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


## Reference
* https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
