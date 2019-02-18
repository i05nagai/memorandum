---
title: Kubernetes Object Volume
---

## Kubernetes Object Volume

* PersistentVolume
* PersistentVolumeClaim


## Volumes
* [Volumes | Kubernetes](https://kubernetes.io/docs/concepts/storage/volumes/)

Dockerのvolumeと違い、透過的に色々なdeviceをvolumeとして扱える。

* awsElasticBlockStore
* azureDisk
* azureFile
* cephfs
* csi
* downwardAPI
    * pods/containerのlabelなどの情報をvolumeとしてmountできる
* emptyDir
    * Containers in the Pod can all read and write the same files in the emptyDir volume
    * volume can be mounted at the same or different paths in each Container
    * NodeにPodが作られたとき作られる
    * PodがNodeから削除されると消える
    * containerがcrashしても消えない
    * defaultでnodeのvolumeに記録されている
        * `emptyDir.medium: memory` でnodeのtmpfsにもできるが、nodeのrebootとmemory limitによる制約をうける
    * Use case
        * disk based merge sort
        * checkpoint
        * podのcontainer間での読み書き可能なshared volume
            * git-sync sidecar
* fc (fibre channel)
* nfs
    * Podがremoteされても、unmountされるだけで中身は消えない
    * 複数のPodにmountして使うことができる
    * Mount前にdataが保持できる
    * NFS serverが必要
* persistentVolumeClaim
    * PersistentVolumeをmountするのに必要
* flocker
* gcePersistentDisk
    * Unfortunately, PDs can only be mounted by a single consumer in read-write mode - no simultaneous writers allowed
    * GCEのpersistent disk
    * 事前にgcloudでPersistent Diskを作っておく必要がある
    * `gcloud compute disks create --size=500GB --zone=us-central1-a my-data-disk`
    * regional persisten disk
* gitRepo
    * deprecated
    * credeintialsがいる場合はgit-syncを検討する
        * [kubernetes/git-sync: A sidecar app which clones a git repo and keeps it in sync with the upstream.](https://github.com/kubernetes/git-sync)
* glusterfs
* hostPath
    * NodeのPathをmountする
    * containerがdokcerを使う必要があるとき、`/var/lib/docker`を使う
* iscsi
* local
* nfs
    * [examples/staging/volumes/nfs at master · kubernetes/examples](https://github.com/kubernetes/examples/tree/master/staging/volumes/nfs)
    * [external-storage/nfs at master · kubernetes-incubator/external-storage](https://github.com/kubernetes-incubator/external-storage/tree/master/nfs)
* persistentVolumeClaim
* projected
* portworxVolume
* quobyte
* rbd
* scaleIO
* secret
* storageos
* vsphereVolume


## PersistentVolume
* [Persistent Volumes | Kubernetes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#capacity)

DBなどのStatufulなapplicationを使う場合に利用する。
`PersistenVolume`で利用するvolumeを確保して、`PersistentVolumeClaim`で利用する分を確保する。


* Provisioning
    * https://kubernetes.io/docs/concepts/storage/persistent-volumes/#provisioning
    * static
        * A cluster administrator creates a number of PVs before users claim it
    * dynamic

* volumeMode
* accessModes
* persistentVolumeReclaimPolicy
    * Recycle
    * Retain
    * mountOptions

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0003
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  mountOptions:
    - hard
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
```

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: slow
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - {key: environment, operator: In, values: [dev]}
```

* Acccess mode
    * ReadWriteOnce
        * single nodeでR/W
    * ReadOnlyMany
        * multi nodeでR
    * ReadWriteMany
        * multi nodeでR/W


```
gcloud compute disks create --size=500GB --zone=us-central1-a my-data-disk
```

## Persistent Volume Claim

* VolumeMode
    * https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding-block-volumes
    * Filesystem
        * e.g. `ext4` or `ntfs`
    * raw
* access mode
    * `ReadWriteOnce`
    * `ReadOnlyMany`
    * `ReadWriteMany`

## Reference
