---
title: AWS Identity and Access Management CLI
---

## AWS Identity and Access Management CLI

## CLI
* [IAM Role Setup for Installation into AWS](https://avinetworks.com/docs/18.1/iam-role-setup-for-installation-into-aws/)


- [create\-role — AWS CLI 1\.16\.173 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html)

```
aws iam create-role \
    --role-name <value> \
    --path <value> \
    --permissions-boundary <value> \
    --assume-role-policy-document <value> 
```

- `--path`
- `--role-name`
- `--permissions-boundary`
    - arn of boudary
- `--max-session-duration`


* [create\-policy — AWS CLI 1\.16\.173 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/iam/create-policy.html)

```
aws iam create-policy
--policy-name <value>
[--path <value>]
--policy-document <value>
[--description <value>]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

- `--policy-name`
- `--path`
- `--policy-document`
    - path to policy document

```
aws iam create-instance-profile
    --instance-profile-name <value>
    [--path <value>]
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

- `--instance-profile-name`
- `--path`

```
aws iam add-role-to-instance-profile
    --instance-profile-name <value>
    --role-name <value>
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

- `--instance-profile-name`
- `--role-name`

```
aws iam list-policies
aws iam list-roles
```


## Usage

## Configuration

## Reference
* [iam — AWS CLI 1\.16\.88 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html#cli-aws-iam)
