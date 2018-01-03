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
brew cask install minikube
```

* [minikube/drivers.md at master · kubernetes/minikube · GitHub](https://github.com/kubernetes/minikube/blob/master/docs/drivers.md#hyperkit-driver)

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/docker-machine-driver-hyperkit \
&& chmod +x docker-machine-driver-hyperkit \
&& sudo mv docker-machine-driver-hyperkit /usr/local/bin/ \
&& sudo chown root:wheel /usr/local/bin/docker-machine-driver-hyperkit \
&& sudo chmod u+s /usr/local/bin/docker-machine-driver-hyperkit
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

### Pull local docker images
Localのdocker imageをpullできるようにする。
事前に以下を実行

```
minikube start
eval $(minikube docker-env)
```

minikubeのdocker daemonが見えるようになる。

```
docker images
```

この状態でdocker-buildすれば良い。
Podの`container`は`IfNotPresent`にする。


```
        imagePullPolicy: IfNotPresent
```

Mount host directoryでできる？
ただOSXの場合はk、mountせずともhostの`/Users`がVMの`/Users`にMountされている。

```
mkdir ~/mount-dir
minikube mount ~/mount-dir:/mount-9p
```

## Tips

### Mount
Mountは以下の9pを使って行われる。

```
sudo mkdir -p /opt/local/airflow/aa || true;
sudo mount -t 9p -o trans=tcp,port=51249,dfltuid=1001,dfltgid=1001,version=9p2000.u,msize=262144 192.168.99.1 /opt/local/airflow/aa;
sudo chmod 775 /opt/local/airflow/aa;
```

### Error: Temporary Error: Could not find an IP address for
* [New cluster w/ HyperKit driver fails to start · Issue #1926 · kubernetes/minikube · GitHub](https://github.com/kubernetes/minikube/issues/1926)

一度deleteすると、修正される場合がある。

```
minikube delete
```

```
minikube start --loglevel 0
```

## Reference
* [kubernetes/minikube: Run Kubernetes locally](https://github.com/kubernetes/minikube)
