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

## get

* `-o`
    * 出力形式
    * `jsonpath`
    * `json`
    * `yaml`

```
kubectl get <resource-type> <resource-name>
```

serviceのcluster IPのみ取得

```
kubectl get svc service_name -o jsonpath='{.spec.clusterIP}' | pbcopy
```

## describe
podのdebugなどで使う。
humanreadableな形式で出力。
Resourceの情報が欲しい場合は、`get`を使う

```
kubectl describe <resource> <resource-name>
```

## Cheatsheet
* [kubectl Cheat Sheet | Kubernetes](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)


## Reference
* [kubectl | Kubernetes](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/)
