---
title: AWS Identity and Access Management
---

## AWS Identity and Access Management

## Concepts
* [Overview of Access Management: Permissions and Policies \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html)

Service -> Actions -> Resources

* Principal
    * An entity in AWS that can perform actions and access resources
    * Principal is the user, service, or account that receives permissions that are defined in a policy.
    * The principal is A in the statement "A has permission to do B to C."
* IAM user
    * they can't access anything in your account until you give them permission
* Permissions
    * Permissions are categorized as permissions policies and permissions boundaries
    * permission policies
    * permission boundaries
        * allows you to use policies to limit the maximum permissions that a principal can have
        * These boundaries can be applied to AWS Organizations organizations or to IAM users or roles
* Policy
    * [Policies and Permissions \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
    * [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html)
    * Identity-based policies
        * Attach managed and inline policies to IAM identities, such as users, groups to which users belong, and roles.
    * Resource-based policies
        * Resource-based policies are JSON policy documents that you attach to a resource such as an Amazon S3 bucket
        * attached to a resource
        * Resource-based policies differ from resource-level permissions
    * Organizations SCPs
    * Access control lists
        * Use ACLs to control what principals can access a resource. ACLs are similar to resource-based policies, although they are the only policy type that does not use the JSON policy document structure.
* Role
    * it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS
    * a role does not have standard long-term credentials (password or access keys) associated with it.
    * A set of permissions that grant access to actions and resources in AWS
* Role chaining
* AWS service role
    * A role that a service assumes to perform actions in your account on your behalf
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

## Policy
* [Policies and Permissions \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

JSON policy

[IAM JSON Policy Elements Reference \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)

* Version
    * Specify the version of the policy language that you want to use.
    * As a best practice, use the latest `2012-10-17` version.
    * `2008-10-17`
* Statement
    * Use this main policy element as a container for the following elements.
    * You can include more than one statement in a policy.
    * `Sid`
        * Statement id
        * Include an optional statement ID to differentiate between your statements.
    * `Effect`
        * Use `Allow` or `Deny` to indicate whether the policy allows or denies access.
    * `Principal`
        * Indicate the account, user, role, or federated user to which you would like to allow or deny access.
        * If you are creating a policy to attach to a user or role, you cannot include this element.
        * The principal is implied as that user or role.
        * map
        * `"Federated": "cognito-identity.amazonaws.com"`
        * `"AWS": "arn:aws:iam::AWS-account-ID:root"`
        * aws service
            * `long_service-name.amazonaws.com`
    * `NotPrincipal`
    * `Action`
        * The actions or operations that the principal wants to perform
        * Include a list of actions that the policy allows or denies.
        * Each AWS service has its own set of actions that describe tasks that you can perform with that service
        * `*` is allowed
            * `"Action": "iam:*AccessKey*"`
        * Actions for EC2
            * [Actions \- Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html)
        * Actions for S3
            * [Specifying Permissions in a Policy \- Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html)
    * `NotAction`
    * `Resource`
        * The AWS resource object upon which the actions or operations are performed
        * Specify a list of resources to which the actions apply.
        * Some services do not let you specify actions for individual resources; instead, any actions that you list in the Action or NotAction element apply to all resources in that service. In these cases, you use the wildcard * in the Resource element.
    * `Condition`
        * Optional
        * Specify the circumstances under which the policy grants permission.
* You can use some variables in the format
    * [IAM Policy Elements: Variables and Tags \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html)

## Policy
* [Example IAM Identity\-Based Policies \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)

It is difficult to find out what permissions is necessary for what you want to do.
Take a look at examples provided by AWS.

## Group

## User

## Role
* [IAM Roles \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html?icmpid=docs_iam_console)

## Resource
* [Identity\-Based Policies and Resource\-Based Policies \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)


## Principals
* https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying

* Specific AWS accounts
    * type
        * `AWS`
    * values
        * `arn:aws:iam::AWS-account-ID:root`
* Individual IAM user or users
    * type
        * `AWS`
    * values
        * ``
* Federated users 
    * type
        * ``
    * value
        * `cognito-identity.amazonaws.com`
* IAM role
    * `AWS`
    * `arn:aws:iam::AWS-account-ID:role/role-name`
* AWS service
    * 
* Everyone (anonymous users)
    * `AWS`
    * `*`

## Amazon Resource Nanme

* user account
    * `arn:aws:iam::AWS-account-ID:root`
    * `arn:aws:iam::AWS-account-ID:user/user-name`
* role
    * `arn:aws:iam::AWS-account-ID:role/role-name`
* assumed role
    * `arn:aws:sts::AWS-account-ID:assumed-role/role-name/role-session-name`
* aws service

## Instance profile
* [Using Instance Profiles \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)

An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts.

## Path
* [amazon web services \- In AWS IAM, What is the Purpose/Use of the "Path" Variable? \- Stack Overflow](https://stackoverflow.com/questions/46324062/in-aws-iam-what-is-the-purpose-use-of-the-path-variable)



## Reference
* [What Is IAM? \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
