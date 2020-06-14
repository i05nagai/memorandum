---
title: AWS Cloud Formation
---

## AWS Cloud Formation

Yaml

```yaml
Fn::Equals: [value_1, value_2]
# short form
!Equals [value_1, value_2]
```

## Funcrtions

```yaml
LambdaPermissionHealthCheckSlToYggdrasil:
  Type: AWS::Lambda::Permission
  Properties:
    FunctionName: !GetAtt 
    - LogicalIDLambda
    - Arn
    Action: "lambda:InvokeFunction"
    Principal: principal
```

## Mappings
You can define mapping in `cloudformation.json`

```yaml
Mappings: 
  RegionMap: 
    us-east-1: 
      AMI: "ami-0ff8a91507f77f867"
      TestAz: "us-east-1a"
    us-west-1: 
      AMI: "ami-0bdb828fd58c52235"
      TestAz: "us-west-1a"
    us-west-2: 
      AMI: "ami-a0cfeed8"
      TestAz: "us-west-2a"
    eu-west-1: 
      AMI: "ami-047bb4163c506cd98"
      TestAz: "eu-west-1a"
    sa-east-1: 
      AMI: "ami-07b14488da8ea02a0"
      TestAz: "sa-east-1a"
    ap-southeast-1: 
      AMI: "ami-08569b978cc4dfa10"
      TestAz: "ap-southeast-1a"
```

## Parameters

```yaml
Parameters:
  EnvType:
    Description: Environment type.
    Default: dev
    Type: String
    AllowedValues:
      - prod
      - stg
      - dev
  ConstraintDescription: must specify prod/dev/stg.
```

## Conditions
- [Conditions \- AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html)

```
Conditions:
  Logical ID:
    Intrinsic function
```


```yaml
Parameters:
  Env:
    Description: Environment type.
    Default: dev
    Type: String
    AllowedValues:
    - prod
    - stg
    - dev
  ConstraintDescription: must specify prod/dev/stg.
  Conditions:
    IsDevOrStg:
      Fn::Or:
      - !Equals [!Ref Env, "stg"]
      - !Equals [!Ref Env, "dev"]
    # It doesn't work
    # IsDevOrStg:
    #   Fn::Or:
    #   - Fn::Equals: [!Ref Env, "stg"]
    #   - Fn::Equals: [!Ref Env, "dev"]
```

### Intrinsic function
- [Condition Functions \- AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html)

- Fn::And
- Fn::Equals
- Fn::If
- Fn::Not
- Fn::Or


#### UPDATE_ROLLBACK_FAILED
- [Continue Rolling Back an Update \- AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html)

- You can change the state manually from `UPDATE_ROLLBACK_FAILED` to `UPDATE_ROLLBACK_COMPLETE`


#### Reference resources accross stacks
* [Reference Resources across Stacks in AWS CloudFormation Templates](https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-reference-resource/)

You can use `Fn::ImportValue`.
[Fn::ImportValue \- AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html)

## CustomResource


#### Response object is too long
Custom Resource has limits of 4K for response of custom resources.

```
response object is too long.
```


## Referece
* [AWS CloudFormation - Infrastructure as Code & AWS Resource Provisioning](https://aws.amazon.com/cloudformation/)
