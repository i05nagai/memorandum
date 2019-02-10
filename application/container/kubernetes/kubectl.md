---
title: kubectl
---

## kubectl

## create
Create resource from file

```
kubectl create -f filename
```

## run
Run particular image on the cluster

```
kubectl run image
```

## config

Show current configuration

```
kubectl config view
```

Specify default namespace

```
kubectl config set-context $(kubectl config current-context) --namespace=<insert-namespace-name-here>
```

Show cluster which you are managing

```
$ kubectl config current-context
```

Change cluster.

```
$ kubectl config set-cluster <cluster-name>
# for GKE
$ gcloud container clusters get-credentials <cluster-name>
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

delete all evicted pods

```
kubectl get pods --namespace namespace -a | grep Evicted | cut -f 1 -d ' ' | xargs kubectl delete pods --namespace namespace
```

nodeのannotationを取得

```
kubectl get nodes --show-labels
```

Horizontal Pod Autoscalerの取得

```
kubectl get hpa
```

## autoscaler

target cpu utilization 80%, minimum replica 2, max replica 5

```
kubectl autoscale rc foo --min=2 --max=5 --cpu-percent=80
```

## describe
podのdebugなどで使う。
humanreadableな形式で出力。
Resourceの情報が欲しい場合は、`get`を使う

```
kubectl describe <resource> <resource-name>
```

Label selectorでlabelを指定してdescribe

```
kubectl describe pods --selector key=value
```

## exec

* `--v=6`
    * verbose mode

```
kubectl exec --v=6
```

## Nodes

Get node labels

```
kubectl get nodes --show-labels
```

## proxy
`http://127.0.0.1:8001`にaccessするとkubernetes API serverにaccessできる。

```
kubectl proxy
```


## Cheatsheet
* [kubectl Cheat Sheet | Kubernetes](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

###
* [docker - kubectl: Error from server: No SSH tunnels currently open - Stack Overflow](https://stackoverflow.com/questions/36375030/kubectl-error-from-server-no-ssh-tunnels-currently-open)

* cluster do

## Reference
* [kubectl | Kubernetes](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/)
