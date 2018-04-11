---
title: kubeadm
---

## kubeadm
* [Installing kubeadm | Kubernetes](https://kubernetes.io/docs/setup/independent/install-kubeadm/)

OSXでは使えない

```
apt-get update && apt-get install -y apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update
apt-get install -y kubelet kubeadm kubectl
```


## Reference
* [Installing kubeadm | Kubernetes](https://kubernetes.io/docs/setup/independent/install-kubeadm/)
