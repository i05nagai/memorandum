---
title: Kuberbetes Object Ingress
---

## Kuberbetes Object Ingress
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

## Reference
* [[Kubernetes] オンプレでも GKE Like な Ingress を使うために 自作 Ingress Controller を実装してみた | Tech Blog](https://adtech.cyberagent.io/techblog/archives/3758)
