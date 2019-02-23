---
title: Kubernetes Service Account
---

## Kubernetes Service Account

#### Service accounts
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

There is `default` service accounts for Pods.

https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/

#### Service account automation

Three separate components cooperate to implement the automation around service accounts:

* A Service account admission controller
* A Token controller
* A Service account controller

Determination of Pods' service account 

* (1) If the pod does not have a ServiceAccount set, it sets the ServiceAccount to `default`
* (2) It ensures that the ServiceAccount referenced by the pod exists, and otherwise rejects it.
* (3) If the pod does not contain any `ImagePullSecrets`, then `ImagePullSecrets` of the `ServiceAccount` are added to the pod.
* (4) It adds a volume to the pod which contains a token for API access.
* (5) It adds a volumeSource to each container of the pod mounted at /var/run/secrets/kubernetes.io/serviceaccount.


#### Use non default service accounts when creating pods

```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: build-robot

  automountServiceAccountToken: false
```


## Reference
