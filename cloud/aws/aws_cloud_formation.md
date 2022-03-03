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


#### Dynamic Reference

Some restrictions for Dynamic Reference
[Using AWS Systems Manager Parameter Store Secure String parameters in AWS CloudFormation templates \| AWS Management & Governance Blog](https://aws.amazon.com/blogs/mt/using-aws-systems-manager-parameter-store-secure-string-parameters-in-aws-cloudformation-templates/)


## WaitCondition

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.html



```
import requests
import enum
import typing
import re
import logging
import json
import uuid


class ResourceHealthNotifier:
    """Notify resource health to Cloud Formation Wait Condition.

    :param endpoint: WaitConditionHandle URL.
    """

    class Status(enum.Enum):

        SUCCESS = "SUCCESS"
        FAILURE = "FAILURE"

    def __init__(self, endpoint: str) -> None:
        self._endpoint = self._get_url(endpoint)

    def _send(self, payload: typing.Dict):
        content_type = {"Content-Type": ""}
        response = requests.put(
            self._endpoint,
            data=json.dumps(payload),
            headers=content_type,
            verify=True
        )
        response.raise_for_status()
        return response

    def _get_url(self, url: str) -> str:
        if re.match(r"https?://.*", url):
            return url

        try:
            decoded_url = base64.b64decode(url)
        except TypeError:
            print(f"Cannot decode WaitConditionHandle URL: {url}")
            raise

        if not re.match(r"https?://.*", decoded_url):
            print(f"Decoded WaitConditionHandle URL is Invalid: {decoded_url}")
            raise ValueError()

    def notify(self, *, reason: str, data: str, unique_id: str, status: Status) -> typing.Dict[str, typing.Any]:
        """Notify the status.

        :param reason: Reason of the status.
        :param data: Data is any information that you want to send back with the signal
        :param unique_id: identifies the signal to AWS CloudFormation.
            If the Count property of the wait condition is greater than 1, the UniqueId value must be unique across
            all signals sent for a particular wait condition.
        :param status:
        """
        payload = {
            "Status": status.value,
            "Reason": reason,
            "Data": data,
            "UniqueId": unique_id
        }

        response = self._send(payload)
        print(f"CloudFormation signaled successfully with {payload['Status']}.")
        return response


endpoint = "https://cloudformation-waitcondition-eu-west-1.s3-eu-west-1.amazonaws.com/...."
a = ResourceHealthNotifier(endpoint)
d = a.notify(
    reason="ok",
    data="ok",
    unique_id=str(uuid.uuid4()),
    status=ResourceHealthNotifier.Status.SUCCESS,
)
print(d.text)
```



## Referece
* [AWS CloudFormation - Infrastructure as Code & AWS Resource Provisioning](https://aws.amazon.com/cloudformation/)
