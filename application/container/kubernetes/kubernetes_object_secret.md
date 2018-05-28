---
title: Kubernetes Object Secret
---

## Kubernetes Object Secret
* [Secrets | Kubernetes](https://kubernetes.io/docs/concepts/configuration/secret/)
    * 作成したseceretはPodにfileとしてvolumeに付与できる
    * enviroment variableとして付与できる

Password, OAuth token, ssh keysなどを保持する。
pod definitionやdocker imageに書くより柔軟に利用できる。
複数のpodで同じsecretを利用可能など。

secretを作成

```sh
# Create files needed for rest of example.
$ echo -n "admin" > ./username.txt
$ echo -n "1f2d1e2e67df" > ./password.txt
$ kubectl create secret generic db-user-pass --from-file=./username.txt --from-file=./password.txt
secret "db-user-pass" created
```

secretを取得

```sh
kubectl get secrets
```

secretの情報を見る

```sh
kubectl describe secrets/db-user-pass
```

Secretのdecode

```sh
$ kubectl get secret mysecret -o yaml
apiVersion: v1
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
kind: Secret
metadata:
  creationTimestamp: 2016-01-22T18:41:56Z
  name: mysecret
  namespace: default
  resourceVersion: "164619"
  selfLink: /api/v1/namespaces/default/secrets/mysecret
  uid: cfee02d6-c137-11e5-8d73-42010af00002
type: Opaque
```

decodeはbase64で行う。

```sh
$ echo "MWYyZDFlMmU2N2Rm" | base64 --decode
```

Podでfileとしてsecretを使う

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    secret:
      secretName: mysecret
```

fileのpermissionを`0400`などにしたい場合、10進数(256)で記載する。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      defaultMode: 256 # here
```

Environment variablesとして使う場合は

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: mycontainer
    image: redis
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: username
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
  restartPolicy: Never
```

**Use case: Pod with ssh-key**

```
kubectl create secret generic ssh-key-secret --from-file=ssh-privatekey=/path/to/.ssh/id_rsa --from-file=ssh-publickey=/path/to/.ssh/id_rsa.pub
```

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: secret-test-pod
  labels:
    name: secret-test
spec:
  volumes:
  - name: secret-volume
    secret:
      secretName: ssh-key-secret
  containers:
  - name: ssh-test-container
    image: mySshImage
    volumeMounts:
    - name: secret-volume
      readOnly: true
      mountPath: "/etc/secret-volume"
```

**Use-Case: Pods with prod / test credentials**

**Use-case: Dotfiles in secret volume**

## Reference
