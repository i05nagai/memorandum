---
title: kubectl
---

## kubectl
設定の一覧を見る

```
kubectl config view 
```

defaultのnamespaceを設定する。

```
kubectl config set-context $(kubectl config current-context) --namespace=<insert-namespace-name-here>
```

## Cheatsheet
* [kubectl Cheat Sheet | Kubernetes](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)


## Reference
