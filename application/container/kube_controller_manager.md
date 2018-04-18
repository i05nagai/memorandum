---
title: kube-controller-manager
---

## kube-controller-manager
kubernetesの制御を実行するcontrollerの集まり。
kubernertesは各実行の制御をするprogram群を持っているが、simplicityのためにbinaryとしては一つにまとめている。
controll loopの中でresourceの実行を制御している。
controller-managerに含まれるcontrollerは

* replication controller
* endpoints controller
* namespace cntrolelr
* serviceaccounts controller
* etc.

などがある。


## Reference
* [kube-controller-manager | Kubernetes](https://kubernetes.io/docs/reference/generated/kube-controller-manager/)
