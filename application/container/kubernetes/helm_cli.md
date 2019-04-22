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


## helm upgrade

```
helm upgrade 
```

* `-f, --values valueFiles`
    * specify values in a YAML file or a URL(can specify multiple) (default [])
* `--verify`
    * verify the provenance of the chart before upgrading
* `--wait`
    * if set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment are in a ready state before marking the release as successful. It will wai t for as long as --timeout
* `--set stringArray`
    * set values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
* `--set-file stringArray`
    * set values from respective files specified via the command line (can specify multiple or separate values with commas: key1=path1,key2=path2)
* `--set-string stringArray`
    * set STRING values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
* `--namespace string`
    * namespace to install the release into (only used if --install is set).
    * Defaults to the current kube config namespace
* `-i, --install <package>`
    * if a release by this name doesn't already exist, run an install
* `--dry-run`
    * simulate an upgrade


```
helm upgrade \
    --install <package> \
    --values=values.yaml \
    --set-string airflowImageTag=$VERSION \
    --set-string <key1>=<value1> \
    --namespace=<kubenetes-namespace> \
    <path-to-chart>
```

## Reference
