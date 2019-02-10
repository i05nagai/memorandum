---
title: Helm CLI
---

## Helm CLI

```
helm init
```

* `--tiller-tls-verify <key-file>`
    * initialize cluster with TLS connection
* `--kube-context string`
    * name of the kubeconfig context to use
* `--kubeconfig string`
* `--node-selectors "beta.kubernetes.io/os"="linux"`
    * install Tiller specific nodes


```
helm repo update 
```

```
helm instll
```

* `--name <string>`
    * release name
* `--namespace <string>`
    * kubeconfig
* `--dry-run`


```
```


```
helm delete <release-name>
```

* delete installed release

```
helm list
helm ls
```

```
helm get -h
```


```
helm search
```

* find running charts in the cluster

```
helm reset --force
```

* uninstall Tiller from Cluster



## Reference
