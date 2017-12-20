---
title: Minikube
---

## Minikube
LocalでSingle NodeでKubernetesを実行するためのtool.
supportしている機能は以下の通り。

* DNS
* NodePorts
* ConfigMaps and Secrets
* Dashboards
* Container Runtime: Docker, rkt and CRI-O
* Enabling CNI (Container Network Interface)
* Ingress


### OSX
* [minikube/drivers.md at master · kubernetes/minikube](https://github.com/kubernetes/minikube/blob/master/docs/drivers.md#kvm-driver)

kubectlをinstallする

```
brew install kubectl
```

```
brew cask install minikube
```

## CLI

```
minikube start --vm-driver=xxx
```

* virtualbox
* vmwarefusion
* kvm (driver installation)
* xhyve (driver installation)
* hyperkit

```
minikube dashboard
```



## Reference
* [kubernetes/minikube: Run Kubernetes locally](https://github.com/kubernetes/minikube)
