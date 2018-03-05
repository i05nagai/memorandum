---
title: Helm
---

## Helm
The Kubernetes Package Manager.

* helm
    * client
* tiller
    * server
    * kubernetes clusterの中で動く
* Chart
    * Helm package
* Repository
    * chartの集まり
    * CPANなどと同じ
* Release
    * chartのinstanceでkubernetes clusterの中で動作する

## Install

For OSX,

```
brew install kubernetes-helm
```

```
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh
chmod 700 get_helm.sh
./get_helm.sh
```


## Reference
* [kubernetes/helm: The Kubernetes Package Manager](https://github.com/kubernetes/helm)
