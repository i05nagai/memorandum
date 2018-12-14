---
title: AWS Identity and Access Management
---

## AWS Identity and Access Management

## Concepts
* [Overview of Access Management: Permissions and Policies \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html)

* Principal
    * An entity in AWS that can perform actions and access resources
* IAM user
    * they can't access anything in your account until you give them permission
* Permissions
    * Permissions are categorized as permissions policies and permissions boundaries
    * permission policies
        * 
    * permission boundaries
        * allows you to use policies to limit the maximum permissions that a principal can have
        * These boundaries can be applied to AWS Organizations organizations or to IAM users or roles
* Role
    * it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS
    * a role does not have standard long-term credentials (password or access keys) associated with it.
    * A set of permissions that grant access to actions and resources in AWS
* Role chaining
    * kk
* AWS service role
    * A role that a service assumes to perform actions in your account on your behalf
* Policy
* Policy summary
    * policy summary tables that describe the access level, resources, and conditions that are allowed or denied for each service in a policy
    * The policy summary table includes a list of services
* service summary
    * Choose a service there to see the service summary.
    * This summary table includes a list of the actions and associated permissions for the chosen service.
* Action summary
    * You can choose an action from that table to view the action summary. 
* Identity federation
* Group
    * IAM groups
    * You can attach a policy to a group
    * all the users in a group have the permissions that are attached to the group

## Group

## User

## Role
* [IAM Roles \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html?icmpid=docs_iam_console)



## Reference
* [What Is IAM? \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
