---
title: Cloud IAM
---

## Cloud IAM

## Concepts
* Policy
    * https://cloud.google.com/iam/reference/rest/v1/Policy
    * A Policy consists of a list of bindings
* Binding
* Role
    * `roles/service.roleName` e.g. `roles/storage.objectAdmin`
* members
    * A list of one or more principals
* principle
    *  principal can be a Google Account (for end users), a service account (for applications and compute workloads), a Google group, or a Google Workspace account or Cloud Identity domain that can access a resource. Each principal has its own identifier, which is typically an email address.
    * An identifier for the principal, or member, which usually has the following form: `PRINCIPAL_TYPE:ID`
        * `user:my-user@example.com`
* resource_type
    * Use `projects`, `resource-manager` `folders`, or `organizations`.
* organizations
* folder
* project
* resource
    * GCP resources
* allow policy
    * allow policy consists of a list of role bindings

organizations -> folder -> project -> resource

## bindings


## CLI

```
gcloud iam policies
```


```
gcloud projects get-iam-policy

```

## Reference
