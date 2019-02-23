---
title: Kubernetes Role
---

## Kubernetes Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
# kubernetes versions before 1.8.0 should use rbac.authorization.k8s.io/v1beta1
kind: Role
metadata:
  namespace: kube-system
  name: kube-state-metrics-resizer
rules:
- apiGroups: [""]
  resources:
  - pods
  verbs: ["get"]
- apiGroups: ["extensions"]
  resources:
  - deployments
  resourceNames: ["kube-state-metrics"]
  verbs: ["get", "update"]
```

* `rule`
    * [Kubernetes API Reference Docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#apigrouplist-v1-meta)
* `roleRef`


* Cluster role binding
    * Permissions can be granted within a namespace with a ClusterBinding
* role binding
    * A role binding grants the permissions defined in a role to a user or set of users.
    * Permissions can be granted within a namespace with a RoleBinding

ClusterRole

* `rules`
    * PolicyRule array
    * https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#policyrule-v1beta1-rbac-authorization-k8s-io
    * `apiGroups`
        * API groups the resources belongs to
        * `*` is all groups
    * `resources`
        * Resources is a list of resources this rule applies to.
        * `\*` represents all resources in the specified apiGroups
        * `\*/foo` represents the subresource 'foo' for all resources in the specified apiGroups.
    * `nonResourceURLs`
    * `resources`
    * `resourceNames`
        * ResourceNames is an optional white list of names that the rule applies to.
        * An empty set means that everything is allowed.
    * `verbs`
        * Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rul


ClusterRoleBinding

* `kind`
* `subjects`
    * Subject array
    * Subjects holds references to the objects the role applies to.
    * `apiGroup`
        * Defaults to "" for ServiceAccount subjects
        * APIGroup holds the API group of the referenced subjec
        * Defaults to "rbac.authorization.k8s.io" for User and Group subjects.
    * `kind`
    * `name`
    * `namespace`
* `metadata`
* `roleRef`


## Examples


```yaml
# Allow reading the resource “pods” in the core API group
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
# Allow reading/writing “deployments” in both the “extensions” and “apps” API groups
rules:
- apiGroups: ["extensions", "apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

#### Rolebindings
* https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-binding-examples
    * how to specify subjects
    * user
    * group
    * service account


### RBAC Authorization
* [Using RBAC Authorization | Kubernetes](https://kubernetes.io/docs/admin/authorization/rbac/)

#### Default service account
* https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server

When you create a pod, if you do not specify a service account, it is automatically assigned the `default` service account in the same namespace.

#### Check which service account a Pod uses

```
kubectl describe pods <pod-name>
# then you can find a Secret attached to Volume which contains Service account credential
# e.g. 
  default-token-8anb4:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-8anb4
    Optional:    false
```


## Reference
