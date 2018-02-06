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

## Patch

```
kubectl patch (-f filename.yml|resource) -p json_string
```

* `-f|resource`でpatchをあてたいresourceを指定する
* `-p`でpatchの内容を記述する
    * jsonでしかかけない

## Cheatsheet
* [kubectl Cheat Sheet | Kubernetes](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)


## Reference
* [kubectl | Kubernetes](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/)
