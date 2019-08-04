---
title: serverless AWS
---

## serverless AWS


## Configuration
- https://serverless.com/framework/docs/providers/aws/guide/iam/

```yaml
provider:
  # the role specified here will be default role for all functions
  # if the role is not specified in the function, this role is used
  role: myDefaultRole                                                  # must validly reference a role defined in the service
  role: arn:aws:iam::0123456789:role//my/default/path/roleInMyAccount  # must validly reference a role defined in your account
  role:                                                                # must validly resolve to the ARN of a role you have the rights to use
    Fn::GetAtt:
      - myRole
      - Arn
```

## Python

```
serverless create \
    --template aws-python3 \
    --path <service-dir> \
    --name <servie-name>
```

- `template`
    - `aws-python3`
    - `aws-python`

## Layers
- [Serverless Framework \- AWS Lambda Guide \- Layers](https://serverless.com/framework/docs/providers/aws/guide/layers/)




## Reference
* [Serverless Framework \- AWS Lambda Guide \- Quick Start](https://serverless.com/framework/docs/providers/aws/guide/quick-start/)
* [pulumi/pulumi: Define cloud apps and infrastructure in your favorite language and deploy to any cloud](https://github.com/pulumi/pulumi)
