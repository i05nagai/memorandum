---
title: Cloud IAM
---

## Cloud IAM

## Concepts
* Policy
    * https://cloud.google.com/iam/reference/rest/v1/Policy
    * https://cloud.google.com/iam/docs/policies
    * An allow policy is a collection of role bindings and metadata.
    * role bindings
        * It associates, or binds, one or more principals with a single IAM role and any context-specific conditions that change how and when the role is granted.
    * metadata
        * The metadata includes additional information about the allow policy, such as an etag and version to facilitate policy management.
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

## IAM Condition


https://cloud.google.com/iam/docs/configuring-resource-based-access

- parent-only permissions
    - 


## bindings


## OAuth
- 32555940559.apps.googleusercontent.com
    - 32555940559 is for gcloud CLI (Google Cloud SDK)


## identity fedration products and limitations
https://cloud.google.com/iam/docs/federated-identity-supported-services


## Service account
https://cloud.google.com/iam/docs/service-account-permissions
https://medium.com/@alexey.inkin/the-3-permissions-in-google-cloud-you-can-escalate-to-do-anything-f312bb8ab5e7
https://cloud.google.com/blog/topics/developers-practitioners/implementing-iam-access-control-code-hashicorp-terraform

- roles/iam.serviceAccountUser
    - lets a principal attach a service account to a resource.
- 

## Workforce identity federation

## Workload identity federation
https://cloud.google.com/iam/docs/workload-identities

### Attribute mapping
- google.subject
    - required
- google.groups
    - optional
    - Optional. A set of groups that the identity belongs to. This attribute is used in IAM principalSet:// role bindings to grant access to all members of a group.
- attribute.NAME
    - You can define up to 50 custom attributes and use these attributes in IAM principalSet:// role bindings to grant access to all identities with a certain attribute.


### Assetions from AWS
- Your attribute mapping can use the response fields for `GetCallerIdentity` as source attributes.
- https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html

## CLI

```
gcloud iam policies
```


```
gcloud projects get-iam-policy

```


## Workload identity from EKS
https://jasonstitt.com/google-vertex-aws-federated-workload-identity
https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes#eks



## Reference
