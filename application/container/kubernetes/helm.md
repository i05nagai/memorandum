---
title: Helm
---

## Helm
The Kubernetes Package Manager.

* helm
    * client
* tiller
    * Helm server-side components
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


## Helm
o

## Error

#### User "system:serviceaccount:kube\-system:default" cannot get namespaces in the namespace "default"
* [User "system:serviceaccount:kube\-system:default" cannot get namespaces in the namespace "default" · Issue \#3130 · helm/helm](https://github.com/helm/helm/issues/3130)

## Reference
* [kubernetes/helm: The Kubernetes Package Manager](https://github.com/kubernetes/helm)
