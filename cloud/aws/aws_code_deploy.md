---
title: AWS CodeDeploy
---

## AWS CodeDeploy


## Concepts
Applications

= Compute type
    - AWS Lambda
    - ECS
    - EC2

#### Deployment Groups
- [Working with Deployment Groups in CodeDeploy \- AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups.html)

Deployment groups belongs to Application.

- Deployment settings
- Triggers
- Alarms
- Rolebacks
    - Roleback when a deployment fails
    - Rollback when alarms thresholds are met

- Application Revisions

#### Deployments

- In-place deployment
- Blue/green deployment
    - on an EC2/on-premises compute platform
    - on Lambda
    - on an ECS


- Revision location
    - S3
    - AppSpec file stored in S3
        - JSON/YAML from AppSpec editor
- Deployment group overrides
    - You can overrides the configuration from deployment group
- Rollback configuration overrides
    - You can overrides the configuration from deployment group

AppSpec file for Lambda

[Add an Application Specification File to a Revision for CodeDeploy \- AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-appspec-file.html#add-appspec-file-lambda)

- The AppSpec file contains instructions about the Lambda functions to be deployed and used for deployment validation.
- A revision is the same as an AppSpec file.
- An App Spec file can be written in JSON/YAML
- 


## API
- [CodeDeploy — Boto 3 Docs 1\.10\.8 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html)

CloudFormation doesn't support 


#### Create

Revision

- `string`
    - Information about the location of an AWS Lambda deployment revision stored as a RawString.
- `appSpecContent`
    - The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString

deploymentConfigName

- If not specified, the value configured in deployment group is used as a default value

ignoreApplicationStopFailures


targetInstances

- Information about the instances that belong to the replacement environment in a blue/green deployment.
    - `tagFilters`
        - The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. 
    - `autoRollbackConfiguration`
    - `updateOutdatedInstancesOnly`
    - `fileExistsBehavior`

## Trigger
[Create a Trigger for a CodeDeploy Event \- AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html)



- Deploy Function
    - Create first version
- Deploy this version


## Alias
- [Alias — AWS Cloud Development Kit 1\.15\.0 documentation](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/Alias.html)

- `from_alias_attributes(scope, id, *, alias_name, alias_version)`
- `aws_cdk.aws_lambda.Alias(scope, id, *, alias_name, version, additional_versions=None, description=None)`


## hook
- [AppSpec 'hooks' Section \- AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#reference-appspec-file-structure-hooks-list-lambda)


#### Lambda

- BeforeAllowTraffic
    - Use to run tasks before traffic is shifted to the deployed Lambda function version.
- AfterAllowTraffic
    - Use to run tasks after all traffic is shifted to the deployed Lambda function version.


Hook implementation

```python
response = client.put_lifecycle_event_hook_execution_status(
    deploymentId='string',
    lifecycleEventHookExecutionId='string',
    status='Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
)
```

## Rollback


- Fail the deployment — An error is reported and the deployment status is changed to Failed.
- Overwrite the content — The version of the file from the application revision replaces the version already on the instance.
- Retain the content — The file in the target location is kept and the version in the application revision is not copied to the instance.


## Reference
- [Implementing safe AWS Lambda deployments with AWS CodeDeploy \| AWS Compute Blog](https://aws.amazon.com/blogs/compute/implementing-safe-aws-lambda-deployments-with-aws-codedeploy/)
